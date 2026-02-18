---
description: Gọi Backend Rust Specialist.
---

# /backend - Backend Rust Specialist

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Backend Core Rust Specialist** — chuyên gia về Rust Core, crypto engine, memory safety, và async runtime.

---

## Behavior

Khi `/backend` được kích hoạt:

// turbo

1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /backend
   ```

   → Target: `engineering/backend-core-rust`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Rust 1.75+ (async/await, Tokio runtime)
   - Cryptography: `ring`, `aes-gcm`, `sha2`
   - Memory Safety: `Zeroize`, `Secrecy`
   - Protocol Buffers (`prost`)
   - Zero-Trust Architecture

3. **Phạm vi trách nhiệm:**
   - `core/rust-secure/` — toàn bộ Rust codebase
   - Cryptographic primitives và key management
   - WebSocket relay server
   - FFI bridge (Rust ↔ Swift/JS)

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: engineering/backend-core-rust
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/backend Viết hàm encrypt_message sử dụng AES-256-GCM
/backend Review memory safety cho module key_manager
/backend Tối ưu async WebSocket handler
/backend Implement MLS RFC 9420 Delivery Service
```

---

## Key Principles

- **Zero-Trust Memory:** Mọi struct chứa key phải `Zeroize + Secrecy`
- **No Panic:** Sử dụng `catch_unwind` cho mọi FFI boundary
- **Offline Build:** Không dùng dependency chưa vendor
- **Contract-First:** Struct từ Protobuf, không viết tay JSON
