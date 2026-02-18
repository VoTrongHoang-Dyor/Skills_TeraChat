---
description: Gọi QA Automation Engineer (Viết Test).
---

# /qa - QA Automation Engineer

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **QA Automation Engineer** — chuyên gia viết kịch bản kiểm thử (Test Scripts), thiết lập Chaos Testing và Security Sniffing. (Dùng `/test` để *chạy* test).

---

## Behavior

Khi `/qa` được kích hoạt:

// turbo

1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /qa
   ```

   → Target: `qa/qa-automation`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Viết kịch bản Playwright (E2EE functional)
   - Viết kịch bản Mitmproxy (Leakage detection)
   - Cấu hình Chaos Mesh (Nodes failure)
   - Định nghĩa Performance Thresholds

3. **Phạm vi trách nhiệm:**
   - `tests/e2e/` — Kịch bản test
   - `infrastructure/chaos-mesh/` — Cấu hình chaos
   - `.github/workflows/test.yml` — CI pipeline configuration

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: qa/qa-automation
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/qa Viết kịch bản test E2EE chat 1-1 bằng Playwright
/qa Cấu hình Chaos Mesh để kill random node mỗi 5 phút
/qa Tạo script Mitmproxy để phát hiện rò rỉ PII
/qa Thiết lập ngưỡng performance cho Cold Start (< 2s)
```

---

## Key Principles

- **Grey-Box Paranoid:** Tin ở Client, Ngờ ở Network.
- **Dual-Layer Testing:** Luôn test cả Chức năng (UI) và Bảo mật (Sniffing).
- **Chaos First:** Hệ thống phải sống sót khi node chết.
