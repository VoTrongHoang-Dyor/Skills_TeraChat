---
description: Chạy quy trình kiểm thử dây chuyền Agile.
---

# /test - TeraChat Agile Test Cycle

$ARGUMENTS

---

## Purpose

Chạy quy trình kiểm thử 4 bước dây chuyền, phối hợp nhiều agent chuyên trách để đảm bảo chất lượng toàn diện.

---

## Behavior

Khi `/test` được kích hoạt:

// turbo

1. **Chạy Test Runner**

   ```bash
   python3 scripts/test_runner.py
   ```

2. **Quy trình tuần tự (Collaboration Chain):**

### Bước 1: Unit Test & Security Audit (Backend Lead)

- **Agent:** `backend-core-rust`
- **Nhiệm vụ:**
  - Chạy `cargo test --release`
  - Kiểm tra bộ nhớ: mọi biến nhạy cảm đã `Drop` (Zeroize)
  - Báo cáo: "Core Logic: PASS/FAIL"

### Bước 2: Integration Test (Fintech Specialist)

- **Agent:** `backend-fintech-blind`
- **Nhiệm vụ:**
  - Kiểm tra module thanh toán
  - **Verify Hard-Rule:** Quét log xem có lộ `request.body` không
  - Nếu phát hiện log bẩn → **ABORT & ALERT IMMEDIATELY**

### Bước 3: UI/Regression Test (Native Bridge)

- **Agent:** `native-bridge-apple`
- **Nhiệm vụ:**
  - Giả lập thao tác người dùng (Simulate Tap/Click)
  - Kiểm tra cơ chế "Phoenix Rebirth" (Crash → Recovery)

### Bước 4: Final Report (QA Automation)

- **Agent:** `qa-automation`
- **Nhiệm vụ:** Tổng hợp kết quả từ 3 bước trên thành báo cáo release

---

## Output Format

```text
==========================================
🔄 STARTING TERACHAT AGILE TEST CYCLE
==========================================

🚀 [STEP] Unit Test & Security Audit
   👤 Agent: backend-core-rust
   📋 Task: Running 'cargo test --release' & Verifying Zeroize...
   ⏳ Running... DONE ✅

🚀 [STEP] Fintech Integration & Log Audit
   👤 Agent: backend-fintech-blind
   📋 Task: Scanning logs for 'request.body' (PII Leak Check)...
   ⏳ Running... DONE ✅

🚀 [STEP] Native Bridge UI Test
   👤 Agent: native-bridge-apple
   📋 Task: Simulating Touch Events & Phoenix Rebirth...
   ⏳ Running... DONE ✅

📊 GENERATING FINAL REPORT (QA Automation)...

✅ TEST CYCLE COMPLETED SUCCESSFULLY.
ALL SYSTEMS GO for Release candidate.
==========================================
```

---

## Sub-commands

```text
/test                - Full 4-step test cycle
/test unit           - Unit tests only (Step 1)
/test fintech        - Fintech integration only (Step 2)
/test ui             - UI regression only (Step 3)
/test report         - Generate report without re-running
```

---

## Examples

```bash
/test
/test unit
/test fintech
```
