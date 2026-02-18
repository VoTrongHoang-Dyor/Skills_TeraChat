---
description: Gọi Fintech Blind Bridge Specialist.
---

# /fintech - Fintech Blind Bridge Specialist

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Fintech Blind Bridge Specialist** — chuyên gia xử lý thanh toán với nguyên tắc "Blind Bridge" (không bao giờ nhìn thấy dữ liệu tài chính thô).

---

## Behavior

Khi `/fintech` được kích hoạt:

// turbo

1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /fintech
   ```

   → Target: `terachat-engineering/backend-fintech-blind`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Tokenization & Detokenization pipeline
   - PCI-DSS compliance patterns
   - Payment gateway integration (PayPal, Stripe)
   - Approval workflow engines
   - Audit trail với tamper-proof logging

3. **Hard Rules (Vi phạm = ABORT):**
   - 🔴 KHÔNG BAO GIỜ log `request.body` chứa payment data
   - 🔴 KHÔNG lưu card number / CVV ở bất kỳ đâu
   - 🔴 Mọi transaction phải có idempotency key

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: terachat-engineering/backend-fintech-blind
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/fintech Thiết kế flow thanh toán subscription
/fintech Review blind bridge cho module invoice
/fintech Implement approval workflow cho payment > $10K
/fintech Audit trail cho transaction history
```

---

## Key Principles

- **Blind Bridge:** Server chỉ thấy token, không thấy raw data
- **Idempotency:** Mọi mutation phải có unique key
- **Audit Trail:** Mọi action đều được ghi log bất biến
- **PII Redaction:** Log chỉ chứa masked values (`****1234`)
