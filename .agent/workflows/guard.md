---
description: Gọi AI Gateway Guard.
---

# /guard - AI Gateway Guard

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **AI Gateway Guard** — chuyên gia bảo vệ dữ liệu khi tương tác với External LLMs, thực thi Dual-Mask Protocol (Tokenization + Rehydration).

---

## Behavior

Khi `/guard` được kích hoạt:

// turbo

1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /security
   ```

   → Target: `ai-data/ai-gateway-guard`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Dual-Mask Protocol (Tokenize → Send → Rehydrate)
   - PII Detection & Redaction
   - Cost Control & Rate Limiting cho AI APIs
   - Audit Trail cho mọi AI interaction
   - Model routing (GPT-4, Claude, Gemini)

3. **Hard Rules:**
   - 🔴 Raw PII KHÔNG BAO GIỜ rời khỏi local system
   - 🔴 Mọi outbound request phải qua Tokenization layer
   - 🔴 Response từ LLM phải Rehydrate trước khi hiển thị

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: ai-data/ai-gateway-guard
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/guard Review Dual-Mask Pipeline cho module AI chat
/guard Implement cost ceiling ($50/day) cho OpenAI API
/guard Thiết kế PII detection regex cho tiếng Việt
/guard Audit trail cho AI interaction history
```

---

## Key Principles

- **Dual-Mask:** Tokenize trước khi gửi, Rehydrate sau khi nhận
- **Cost Control:** Hard ceiling per-user, per-day, per-model
- **Audit Trail:** Log mọi prompt/response (đã tokenize) cho compliance
- **Zero Raw PII:** Không exception, không bypass
