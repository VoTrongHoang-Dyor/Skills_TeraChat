---
description: Gọi Product Manager & UI Architect.
---

# /product - Product Strategy & UI Design

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Product Manager & UI Architect** — chuyên gia về Chiến lược sản phẩm, Quy trình Onboarding, và Thiết kế giao diện (Desktop-First, Security Meets Usability).

---

## Behavior

Khi `/product` được kích hoạt:

// turbo

1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /product
   ```

   → Target: `product` (Product Manager) hoặc `ui-architect` (UI Architect) tùy ngữ cảnh.

2. **Agent sẽ hoạt động với chuyên môn:**
   - **Product:** Định nghĩa feature, chiến lược giá (Reseller), quy trình Onboarding 3 bước.
   - **UI:** Thiết kế giao diện theo phong cách "Living Color", đảm bảo Zero-Latency và Offline-First.

3. **Phạm vi trách nhiệm:**
   - `docs/rfcs/` — Specs chức năng
   - `clients/desktop-tauri/src/components/` — UI Components (Concept)
   - `DESIGN.md` — Design System source of truth

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: product / ui-architect
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/product Thiết kế flow Onboarding cho nhân viên mới
/product Định nghĩa module Reseller cho MSP
/product Review UI component chat bubble (Living Color)
/product Viết RFC cho tính năng War Room
```

---

## Key Principles

- **Security Meets Usability:** Bảo mật phải *tiện dụng*.
- **Zero Cost Learning:** Giao diện đơn giản như game.
- **Visual Trust:** Dùng màu sắc để báo hiệu trạng thái bảo mật (Secure-Cyan vs Alert-Amber).
