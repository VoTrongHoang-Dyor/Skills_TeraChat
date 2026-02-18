---
description: Khởi tạo cấu trúc dự án chuẩn bảo mật (Rust Core + Tauri).
---

# /init - TeraChat Project Scaffolding

$ARGUMENTS

---

## Purpose

Khởi tạo cấu trúc Monorepo chuẩn quân sự cho TeraChat Enterprise OS.

---

## Behavior

Khi `/init` được kích hoạt:

// turbo

1. **Chạy Scaffolding Engine**

   ```bash
   python3 scripts/scaffold_terachat.py
   ```

2. **Tạo cấu trúc dự án:**

   ```text
   /terachat-monorepo
     ├── core/rust-secure        (Rust Core + Crypto)
     ├── clients/desktop-tauri   (React + Tauri V2)
     ├── clients/native-apple    (Swift + Secure Enclave)
     ├── infra/clean-room        (Docker Offline Build)
     └── docs/architecture       (Documentation)
   ```

3. **Verify Output:**
   - Kiểm tra `Cargo.toml` có đầy đủ dependencies bảo mật (`zeroize`, `secrecy`, `ring`)
   - Kiểm tra `tauri.conf.json` có CSP policy
   - Kiểm tra `CoreInvoker.swift` có panic handler

---

## Output Format

```text
=== TERACHAT PROJECT SCAFFOLDING ===

>>> Initializing Backend Core (Rust)...
  [+] Created directory: terachat-monorepo/core/rust-secure/src
  [+] Created file: Cargo.toml
  [+] Created file: src/lib.rs

>>> Initializing Desktop Client (Tauri)...
  [+] Created directory: clients/desktop-tauri

>>> Initializing Native Bridge (Apple)...
  [+] Created file: CoreInvoker.swift

>>> Initializing Infra & Docs...
  [+] Created file: Dockerfile.secure

✅ DONE! Project created at './terachat-monorepo'
```

---

## Examples

```bash
/init
/init --dry-run
```
