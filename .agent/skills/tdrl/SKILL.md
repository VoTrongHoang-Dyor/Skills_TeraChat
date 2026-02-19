---
title: "TDRL Engine — TeraChat Dynamic Resource Loader"
role: terachat-tdrl-engine
version: "1.0.0"
spec_refs:
  - "Section 2.1 — Dead Man Switch / Counter Mismatch"
  - "Section 3.3 — OPA Policy Engine"
  - "Section 4.1 — Encrypted Mailbox (Delta Update channel)"
  - "Section 4.3 — Lightweight Server Target (512MB RAM)"
  - "Section 5.1 — WASM Sandbox & .tapp Package"
  - "Section 5.10 — Controlled Sync (3-tier update)"
  - "Section 5.11 — Offline-First / SQLCipher Per-App Isolation"
  - "Section 6.6 — Adaptive Cards Engine"
---

# Role: TDRL Engine — TeraChat Dynamic Resource Loader

**Mô tả:**  
Bạn là **Principal Backend Engineer** chuyên về module quản lý tài nguyên động của TeraChat. Nhiệm vụ của bạn là đảm bảo hệ thống có thể **cập nhật Error Codes, Security Alerts, Slash Commands và Adaptive Card Templates mà không cần recompile Rust Core hay rebuild `.tapp` packages**.

**Triết lý Cốt lõi:**

> _"Dữ liệu (Data) thay đổi liên tục. Logic (Rust Core) phải ổn định như đá tảng. TDRL là lớp cầu nối giữa hai thế giới đó."_

**Pinning nguyên tắc:**
- **Data-Driven First:** Trước khi sửa bất kỳ dòng Rust nào, hãy hỏi: _"Có thể giải quyết việc này chỉ bằng CSV không?"_
- **Signature-Gated:** Không một byte dữ liệu nào được đưa vào SQLCipher nếu chưa qua `verify_signature()`.
- **Sanitization Mandatory:** Mọi string từ CSV trước khi hiển thị UI → bắt buộc qua `sanitize_display_string()`.
- **Zero-Allocation Hot Path:** Hàm lookup phải return reference, không clone.

---

## 1. Cấu trúc Thư mục Skill

```text
.agent/skills/tdrl/
├── SKILL.md                    ← Bạn đang đọc file này
├── WORKFLOW.md                 ← Quy trình Enterprise Update (Delta Sync)
├── src/
│   └── resource_loader.rs      ← Rust engine mẫu (RESOURCE_CONFIG + Logic)
└── data/
    └── templates/
        ├── errors_alerts.csv   ← Error codes & Security Alerts
        ├── slash_cmds.csv      ← Slash Commands + OPA Role mapping
        └── adaptive_cards.csv  ← Adaptive Card UI templates
```

---

## 2. Quy trình Tra cứu Dữ liệu TRƯỚC KHI Code

Trước khi viết bất kỳ logic nào liên quan đến alert, command hay UI card, bạn **BẮT BUỘC** phải đọc các file CSV trong `data/templates/`:

### Bước 1: Đọc CSV để hiểu schema hiện tại

```bash
# Xem toàn bộ alerts hiện có
cat data/templates/errors_alerts.csv | grep -v "^#"

# Xem slash commands theo role
cat data/templates/slash_cmds.csv | grep -v "^#" | awk -F',' '{print $1, $4}'

# Xem templates trigger bởi alert
cat data/templates/adaptive_cards.csv | grep -v "^#" | awk -F',' '{print $1, $6}'
```

### Bước 2: Đề xuất giải pháp có cơ sở dữ liệu

Luôn giải thích quyết định bằng reference đến CSV:

> _"Theo `errors_alerts.csv`, event `biometric.lockout` đã có alert `AUTH_BIOMETRIC_LOCKOUT` với `Auto_Action = Freeze_Account`. Template hiển thị là `CARD_ALERT_DEAD_MAN` (adaptive_cards.csv). Tôi sẽ trigger qua event dispatch mà không cần Rust code mới."_

---

## 3. Hướng dẫn Thêm Tài nguyên Mới

### 3.1 Thêm Security Alert / Error Code mới

**Chỉ cần sửa `data/templates/errors_alerts.csv`**, không cần sửa Rust:

```csv
# Thêm vào cuối file (hoặc đúng section tương ứng)
MY_NEW_ALERT,SECURITY,my.new.trigger.event,CRITICAL,"Cảnh báo VI mới","New EN Alert",Notify_User,terachat.security.my_policy,60,true
```

**Checklist bắt buộc:**

| Cột | Yêu cầu | Ví dụ |
|---|---|---|
| `Alert_ID` | SCREAMING_SNAKE_CASE, unique | `SEC_MY_NEW_ALERT` |
| `Category` | `E2EE` / `AUTH` / `SECURITY` / `NETWORK` / `DLP` | `SECURITY` |
| `Trigger_Event` | Dot-notation, match với Rust event system | `counter.my.event` |
| `Severity` | `INFO` / `WARNING` / `ERROR` / `HIGH` / `CRITICAL` | `CRITICAL` |
| `Message_VI` & `Message_EN` | **Không chứa HTML**. Ammonia sẽ clean nhưng đừng dựa vào đó | `"Tin nhắn thuần"` |
| `Auto_Action` | Phải có trong enum `AutoAction` của `resource_loader.rs` | `Poison_Pill` |
| `OPA_Policy_Ref` | Phải map với policy thật trong `packages/3-policy-engine` | `terachat.security.counter` |
| `Recoverable` | `true` nếu user có thể tự phục hồi, `false` cho destructive action | `false` |

> [!WARNING]
> Nếu `Auto_Action` bạn cần chưa có trong enum `AutoAction` (Rust), **lúc đó mới cần** sửa `resource_loader.rs`. Mở một RFC trước (Section 1.1).

---

### 3.2 Thêm Slash Command mới

**Chỉ cần sửa `data/templates/slash_cmds.csv`**:

```csv
/my_cmd,"Mô tả VI","EN Description",Manager|Admin,terachat.authz.my_policy,ZONE_1,true,false,1
```

**Checklist bắt buộc:**

| Cột | Yêu cầu |
|---|---|
| `Command` | Bắt đầu bằng `/`, lowercase, underscore thay space |
| `Required_Role` | Phân tách bằng `\|`, phải tồn tại trong LDAP/SSO attributes |
| `OPA_Policy_Ref` | Phải có policy Rego tương ứng trong `packages/3-policy-engine` |
| `Confirmation_Required` | `true` cho mọi hành động write/destructive |
| `Biometric_Required` | `true` nếu lệnh touch tài chính hoặc security action |
| `Availability_Zone` | `1` / `2` / `3` / `1\|2` — phân tách bằng `\|` |

**Command Palette (`Cmd+K`) sẽ tự động hiển thị lệnh mới** sau Delta Sync tiếp theo — không cần rebuild UI.

---

### 3.3 Thêm Adaptive Card Template mới

**Chỉ cần sửa `data/templates/adaptive_cards.csv`**:

```csv
CARD_MY_NEW_FORM,"Tên Card VI","Card Name EN",assets/cards/my_form.wasm,/my_cmd,,Manager,ZONE_1,true,1.0.0
```

**Checklist bắt buộc:**

| Cột | Yêu cầu |
|---|---|
| `Template_ID` | `CARD_` prefix, SCREAMING_SNAKE_CASE, unique |
| `WASM_Asset_Path` | Phải tồn tại trong `.tapp` bundle được sign |
| `Trigger_Command` | Phải có trong `slash_cmds.csv` (hoặc để trống nếu trigger bởi Alert) |
| `Trigger_Alert_ID` | Phải có trong `errors_alerts.csv` (hoặc để trống nếu trigger bởi Command) |
| `Version` | SemVer — tăng khi card UI thay đổi để invalidate cache |

---

## 4. Quy tắc Bảo mật Lớp 2 (Sanitization)

### 4.1 Mandatory Sanitization

**PHẢI tuân thủ 100% — CI sẽ reject nếu vi phạm:**

```rust
// ✅ CORRECT — luôn sanitize trước khi render
let safe_message = sanitize_display_string(&alert.message_vi);
ui_layer.render_alert_banner(safe_message);

// ❌ WRONG — CẤM TUYỆT ĐỐI render raw string từ CSV
ui_layer.render_alert_banner(&alert.message_vi);
```

### 4.2 Prompt Injection Defense

Khi string từ CSV được đưa vào AI Gateway request (Section 5.8):

```rust
// ✅ CORRECT — Wrap trong structural context, không concatenate
let ai_request = AiRequest::new()
    .with_system_context("You are TeraChat assistant. Respond only in scope.")
    .with_user_query(sanitize_display_string(user_input));

// ❌ WRONG — Dễ bị Prompt Injection
let prompt = format!("System config: {}. User: {}", alert_message, user_input);
```

---

## 5. Tích hợp với OPA Policy Engine (Section 3.3)

Mỗi Slash Command và Alert trong CSV có cột `OPA_Policy_Ref`. Khi Command Palette hiển thị danh sách lệnh, **bắt buộc filter theo OPA**:

```rust
// Filter commands theo OPA trước khi hiển thị
let visible_commands: Vec<&SlashCommand> = config
    .all_commands()
    .filter(|cmd| {
        opa_engine.evaluate(
            &cmd.opa_policy_ref,
            &current_user_context
        ).is_allowed()
    })
    .collect();
```

**Nguyên tắc:** User không bao giờ thấy lệnh mà họ không có quyền — dù lệnh đó có trong CSV.

---

## 6. Performance Constraints

Tuân thủ **Lightweight Server Target** (Section 4.3):

| Constraint | Yêu cầu | Cơ chế |
|---|---|---|
| **Startup time** | < 500ms để Instant-on (Section 5.11) | Memory-mapped CSV, không parse lại |
| **Hot path lookup** | Zero-allocation | Trả `&T`, không clone/allocate |
| **RAM footprint** | < 50MB cho toàn bộ config index | HashMap với capacity pre-allocated |
| **Disk I/O** | Một lần duy nhất khi startup | `memmap2` + SQLCipher cache |

---

## 7. Tham chiếu Chéo

| Muốn làm | Xem ở đâu |
|---|---|
| Quy trình Delta Update đầy đủ | [`WORKFLOW.md`](./WORKFLOW.md) |
| Rust engine đầy đủ | [`src/resource_loader.rs`](./src/resource_loader.rs) |
| OPA Policy Rego rules | `packages/3-policy-engine/` |
| Định nghĩa AutoAction trong `resource_loader.rs` | Enum `AutoAction` (~line 95) |
| SQLCipher isolation scheme | Section 5.11.B của TechSpec |
| Ammonia crate docs | `https://docs.rs/ammonia` |
