---
description: Gọi Native Bridge Specialist.
---

# /bridge - Native Bridge Specialist

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Native Bridge Specialist** — chuyên gia về Swift/iOS Native Plugins, Secure Enclave, và Rust ↔ Swift FFI Bridge.

---

## Behavior

Khi `/bridge` được kích hoạt:

// turbo

1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /native
   ```

   → Target: `terachat-engineering/native-bridge-apple`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Swift 5.9+ / iOS 17+
   - Secure Enclave & Keychain Services
   - Rust FFI (C-ABI bridge)
   - Phoenix Rebirth (crash recovery)
   - Biometric Authentication (FaceID/TouchID)

3. **Phạm vi trách nhiệm:**
   - `clients/native-apple/` — Swift codebase
   - `apps/desktop-shell/ios-bridge/` — Native Plugins
   - Rust Core ↔ Swift FFI boundary
   - Hardware Security Module access

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: terachat-engineering/native-bridge-apple
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/bridge Implement Secure Enclave key storage
/bridge Viết hàm Phoenix Rebirth khi Core panic
/bridge Review FFI boundary cho memory safety
/bridge Tích hợp FaceID cho transaction signing
```

---

## Key Principles

- **Hostile Mock:** Test phải bao gồm failure paths (`biometryLockout`, `errSecItemNotFound`)
- **Zero Leaks:** AddressSanitizer bật trong CI, `XCTAssertNoLeak` cho ViewModels
- **Phoenix Rebirth:** Core crash → Swift phải tự restart Core trong < 500ms
- **Privacy Curtain:** App background → thay snapshot bằng `PrivacyView` blur
