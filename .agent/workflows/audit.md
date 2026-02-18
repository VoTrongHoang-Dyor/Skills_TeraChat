---
description: "Quét mã nguồn tìm lỗi bảo mật (Log bẩn, Panic)."
---
# /audit - Security Audit

$ARGUMENTS

---

## Purpose

Quét toàn bộ mã nguồn để phát hiện các lỗ hổng bảo mật: log bẩn chứa PII, panic chưa xử lý, key material nằm ngoài `Secrecy`.

---

## Behavior

Khi `/audit` được kích hoạt:

// turbo

1. **Chạy Security Scanner**

   ```bash
   python3 scripts/security_audit.py
   ```

2. **Quét các Pattern nguy hiểm:**
   - 🔴 `println!` / `dbg!` / `eprintln!` chứa biến nhạy cảm
   - 🔴 `unwrap()` / `expect()` không có Panic Guard
   - 🔴 `request.body` bị log trực tiếp
   - 🟡 Struct chứa Key Material thiếu `#[derive(Zeroize)]`
   - 🟡 Biến nhạy cảm không được wrap trong `Secret<T>`

3. **Phân loại mức độ:**

   | Level | Ý nghĩa | Hành động |
   | ------- | --------- | ----------- |
   | 🔴 CRITICAL | Lộ PII / Key Material | BLOCK RELEASE |
   | 🟡 WARNING | Thiếu safeguard | Fix before merge |
   | 🟢 INFO | Best practice suggestion | Optional |

---

## Output Format

```text
🛡️ TERACHAT SECURITY AUDIT
==========================

📂 Scanning: ./core/rust-secure/src/

🔴 CRITICAL [dirty-log]
   File: src/api/handler.rs:45
   Issue: println! contains `request.body` (PII Leak)
   Fix: Remove debug log or use tracing with redaction

🟡 WARNING [missing-zeroize]
   File: src/crypto/keys.rs:12
   Issue: struct KeyPair does not derive Zeroize
   Fix: Add #[derive(Zeroize, ZeroizeOnDrop)]

Summary: 1 Critical, 1 Warning, 0 Info
⛔ RELEASE BLOCKED - Fix critical issues first
```

---

## Sub-commands

```text
/audit                - Full audit
/audit [path]         - Audit specific file/directory
/audit --fix          - Auto-fix safe patterns
/audit --report       - Generate detailed PDF report
```

---

## Examples

```bash
/audit
/audit core/rust-secure/src/
/audit --fix
```
