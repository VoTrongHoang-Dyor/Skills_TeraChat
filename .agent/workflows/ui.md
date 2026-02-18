---
description: Gọi UI/UX Architect.
---

# /ui - UI/UX Architect

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **UI/UX Architect** — chuyên gia về Tauri V2 Desktop Client, React UI, và State-Driven Design.

---

## Behavior

Khi `/ui` được kích hoạt:

// turbo

1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /frontend
   ```

   → Target: `engineering/desktop-tauri-frontend`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Tauri V2 + React (TypeScript)
   - State Machine Driven UI
   - Security UI Patterns (Digital Bunker, Privacy Curtain)
   - Responsive Desktop Layout
   - Protobuf-generated TypeScript types

3. **Phạm vi trách nhiệm:**
   - `clients/desktop-tauri/src/` — React components
   - `clients/desktop-tauri/src-tauri/` — Tauri commands
   - UI State ↔ Rust Core State Machine sync
   - Trusted UI (biometric dialogs qua native, không HTML)

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: engineering/desktop-tauri-frontend
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/ui Thiết kế màn hình chat E2EE
/ui Implement Digital Bunker overlay khi phát hiện screenshot
/ui Tạo component conversation list với unread badges
/ui Review state machine cho offline mode transition
```

---

## Key Principles

- **State-Driven:** UI phản ánh Rust Core State Machine, không "đoán"
- **Trusted UI:** PIN pad, biometric → gọi native, không render HTML
- **Sandbox Treaty:** External data → WASM sandbox, không render trực tiếp
- **Contract-First:** Dùng TypeScript types từ Protobuf, không viết tay
