---
description: Build dự án trong môi trường sạch (Clean Room).
---

# /build - Hermetic Build

$ARGUMENTS

---

## Purpose

Build dự án trong môi trường cách ly hoàn toàn (Clean Room) — không có kết nối internet, chỉ dùng vendored dependencies. Đảm bảo Supply Chain Sovereignty.

---

## Behavior

Khi `/build` được kích hoạt:

// turbo

1. **Chạy Hermetic Build Engine**

   ```bash
   python3 scripts/hermetic_build.py
   ```

2. **Quy trình Build:**
   - Kiểm tra dependencies đã vendor chưa
   - Build trong Docker Container offline
   - `cargo build --release --offline`
   - Tạo Signed SBOM (Software Bill of Materials)

3. **Security Gates:**
   - ❌ Nếu phát hiện dependency chưa vendor → ABORT
   - ❌ Nếu build env có internet access → ABORT
   - ✅ Chỉ pass khi 100% offline build thành công

---

## Output Format

```text
🔒 HERMETIC BUILD - CLEAN ROOM
===============================

[1/4] Verifying vendored dependencies... ✅
[2/4] Starting Docker container (offline)... ✅
[3/4] Building: cargo build --release --offline...
      Compiling terachat-core v0.1.0
      Finished release [optimized] target(s)
[4/4] Generating SBOM... ✅

✅ BUILD SUCCESSFUL
   Binary: target/release/terachat-core
   SBOM: build/sbom-v0.1.0.json
   Duration: 2m 34s
```

---

## Sub-commands

```text
/build              - Full hermetic build
/build --debug      - Debug build (faster, not for release)
/build --verify     - Verify existing build artifacts
```

---

## Examples

```bash
/build
/build --debug
```
