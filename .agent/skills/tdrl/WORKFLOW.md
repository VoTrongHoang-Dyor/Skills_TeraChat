# WORKFLOW.md — Quy trình Enterprise Update (TDRL Delta Sync)

> **Mục tiêu:** Cập nhật Error Codes, Security Alerts, Slash Commands, và Adaptive Card Templates  
> **Không cần:** Recompile Rust, rebuild `.tapp`, hay restart server  
> **Phạm vi:** Tuân thủ Controlled Sync 3 tầng (Section 5.10) + Ed25519 signature verification

---

## Tổng quan Luồng Delta Update

```
[Admin Console]                [Private Cluster]              [Employee Desktop]
     (IT Admin)                  (Enterprise Server)            (TeraChat Client)
        |                               |                              |
  1. Sửa CSV files                     |                              |
     (errors_alerts.csv               |                              |
      slash_cmds.csv                  |                              |
      adaptive_cards.csv)             |                              |
        |                             |                              |
  2. Ký bundle                        |                              |
     Ed25519 sign(SHA-256)            |                              |
        |                             |                              |
  3. Upload manifest.json             |                              |
     + signed bundle             ─────►                              |
        |                             |                              |
        |                        4. Verify signature                  |
        |                           + OPA policy check               |
        |                           + Malware scan                   |
        |                             |                              |
        |                        5. Admin bấm                        |
        |                           "Apply to Cluster"               |
        |                             |                              |
        |                        6. Delta Update ──────────────────► |
        |                           (LAN/VPN only)                   |
        |                           chỉ file thay đổi               |
        |                             |                              |
        |                             |                        7. TDRL Engine:
        |                             |                           verify signature
        |                             |                           → load_into_sqlcipher()
        |                             |                           → rebuild HashMap index
        |                             |                           → hot-swap ResourceConfig
        |                             |                              |
        |                             |                        8. UI phản ánh ngay lập tức:
        |                             |                           - Command Palette mới
        |                             |                           - Alert messages mới
```

---

## Bước 1: Chỉnh sửa CSV (Admin/DevOps)

Mở file tương ứng trong `data/templates/` và thêm/sửa/xóa dòng:

| Nhu cầu | File cần sửa |
|---|---|
| Thêm mã lỗi / cảnh báo mới | `errors_alerts.csv` |
| Thêm slash command | `slash_cmds.csv` |
| Thêm UI card mới | `adaptive_cards.csv` |

**Quy tắc chỉnh sửa:**
- Không xóa dòng đang được production dùng — dùng `Auto_Action = Notify_User` để vô hiệu hóa.
- `Alert_ID` và `Template_ID` phải **globally unique** — check trước khi thêm.
- Message string không được chứa HTML (`<`, `>`, `&` sẽ bị ammonia strip).

---

## Bước 2: Ký Bundle (Admin Console)

### 2.1 Tính SHA-256 của bundle

```bash
# Tạo bundle file bằng cách concat các CSV đã cập nhật
cat errors_alerts.csv slash_cmds.csv adaptive_cards.csv > config_bundle.bin

# Tính hash (để verify sau)
sha256sum config_bundle.bin
# Output: f3ca9f2d...  config_bundle.bin
```

### 2.2 Ký bằng Ed25519 (Admin Private Key trong HSM)

```bash
# Dùng OpenSSL (nếu key lưu trong file)
openssl pkeyutl \
  -sign \
  -inkey admin_private_key.pem \
  -in config_bundle.bin \
  -out config_bundle.sig

# Hoặc dùng TeraChat CLI (key trong HSM/Secure Enclave)
terachat-admin sign-resource-bundle \
  --bundle config_bundle.bin \
  --output config_bundle.sig \
  --pubkey-hex $(terachat-admin get-admin-pubkey)
```

### 2.3 Tạo Delta Update Manifest

```json
{
  "version": "1.2.0",
  "base_hash": "f3ca9f2d...",
  "new_hash": "a7b8c9d0...",
  "changed_files": ["errors_alerts.csv"],
  "admin_signature_hex": "3045022100...",
  "admin_pubkey_hex": "04a1b2c3..."
}
```

Upload `manifest.json` + `config_bundle.sig` lên Admin Console.

---

## Bước 3: Tầng Kiểm soát — Private Cluster

Khi Admin bấm **"Apply to Cluster"**, Private Cluster thực hiện:

### 3.1 Verify Ed25519 Signature

```rust
// Cluster side verification (tương tự resource_loader.rs)
let manifest: DeltaUpdateManifest = serde_json::from_slice(&manifest_bytes)?;
manifest.verify()?;  // Err nếu signature sai → BLOCK ngay
```

> [!CAUTION]
> Nếu verify thất bại → **Block hoàn toàn**. Ghi audit log với event `SEC_RESOURCE_TAMPER`. Không apply bất kỳ thay đổi nào.

### 3.2 OPA Policy Check

```rego
# packages/3-policy-engine/tdrl_update_policy.rego
package terachat.tdrl

# Rule: Chỉ Admin được push resource update
allow_tdrl_update {
    input.actor.role == "admin"
    input.manifest.changed_files_count <= 3  # Giới hạn số file thay đổi/lần
}

# Rule: Command chỉ được thêm cho role đã tồn tại
valid_role_reference {
    input.new_commands[_].required_role in data.known_roles
}
```

### 3.3 Malware Scan (nội bộ, không dùng Cloud)

```bash
# ClamAV scan trên Cluster (air-gapped safe)
clamscan --infected --remove=no config_bundle.bin
```

---

## Bước 4: Delta Distribution (LAN/VPN Only)

Cluster gửi **chỉ các file thay đổi** tới mỗi Desktop client qua LAN/VPN nội bộ:

```
Không bao giờ tải từ Internet CDN.
Nguồn: Private Cluster (intranet only).
```

**Delta Sync:**
```json
{
  "delta_files": [
    {
      "filename": "errors_alerts.csv",
      "sha256": "a7b8c9d0...",
      "size_bytes": 4096,
      "download_url": "https://cluster.internal/tdrl/v1/files/errors_alerts.csv"
    }
  ]
}
```

Client chỉ tải file có trong `delta_files` — không tải lại toàn bộ bundle.

---

## Bước 5: Client-Side Apply (TDRL Engine)

```rust
// Trong TeraChat client khi nhận Delta từ Cluster
async fn apply_delta_update(
    loader: &ResourceLoader,
    manifest: DeltaUpdateManifest,
    new_bundle: SignedConfigBundle,
) -> Result<Arc<ResourceConfig>, TdrlError> {
    // 1. Verify signature (bắt buộc, dù Cluster đã verify)
    //    Nguyên tắc Zero-Trust: Client không tin hoàn toàn Cluster
    let config_hash = ResourceLoader::verify_signature(&new_bundle)?;

    // 2. Kiểm tra hash khớp với manifest
    if config_hash != manifest.new_hash {
        return Err(TdrlError::HashMismatch {
            expected: manifest.new_hash.clone(),
            actual: config_hash,
        });
    }

    // 3. Load config mới
    let new_config = loader.load(new_bundle).await?;

    // 4. Hot-swap (atomic)
    // Tauri State sử dụng RwLock để swap không cần restart
    // app.state::<Mutex<Arc<ResourceConfig>>>().lock().replace(new_config);

    Ok(new_config)
}
```

---

## Bước 6: Rollback

Nếu phiên bản mới gây lỗi, Admin có thể rollback:

```bash
# Via TeraChat CLI
terachat-admin resource rollback --version 1.1.0

# Via Slash Command (trong chat)
# /resource rollback 1.1.0
# → Yêu cầu biometric + confirmation
```

Cluster giữ lại **3 phiên bản gần nhất** trong storage để rollback nhanh.

---

## Checklist Release Gate — Resource Config

Trước khi push Delta Update lên Production:

- [ ] **SHA-256 hash** của bundle đã được verify bởi ít nhất 2 Admin
- [ ] **Ed25519 signature** được tạo bằng HSM/Secure Enclave (không phải file PEM trần)
- [ ] **OPA Policy Check** đã pass trên môi trường Staging
- [ ] **Malware Scan** (ClamAV) đã pass
- [ ] **Staging Validation:** Đã test Delta Update trên 1 máy Staging, ResourceConfig load thành công
- [ ] **Rollback Tested:** Đã verify rollback về phiên bản trước hoạt động đúng
- [ ] **Audit Log:** Mọi bước trên đã được ghi vào tamper-proof audit log

---

## Security Reminders

> [!WARNING]
> **Admin Private Key** dùng để ký resource bundle PHẢI nằm trong **HSM / Secure Enclave / USB Token PKCS#11**. Không được lưu dưới dạng file PEM trên ổ đĩa thường.

> [!CAUTION]
> **Không bao giờ** cho phép Client tải resource bundle trực tiếp từ Internet. Mọi update phải đi qua Private Cluster (Controlled Sync — Section 5.10).

> [!NOTE]
> Cơ chế này áp dụng **ngay cả khi** thay đổi chỉ là sửa typo trong một message tiếng Việt. Mọi thay đổi đều phải qua pipeline verify đầy đủ.
