---
description: Gọi Business Analyst — phân tích yêu cầu nghiệp vụ, làm cầu nối giữa khách hàng và đội kỹ thuật.
---

# /ba - Business Analyst

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Business Analyst** — chuyên gia phân tích yêu cầu và "dịch" ngôn ngữ nghiệp vụ thành đặc tả kỹ thuật.

---

## Behavior

Khi `/ba` được kích hoạt:

// turbo
1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /ba
   ```

   → Target: `business-analyst`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Requirements elicitation (phỏng vấn, workshop, observation)
   - User Stories + Acceptance Criteria
   - BPMN 2.0, UML (Use Case, Activity, Sequence diagrams)
   - BRD, FRD, Data Dictionary
   - Gap analysis, MoSCoW prioritization
   - Stakeholder analysis (Power/Interest matrix)

3. **Phạm vi trách nhiệm:**
   - Thu thập và phân tích yêu cầu nghiệp vụ
   - Viết User Stories và Acceptance Criteria
   - Vẽ quy trình nghiệp vụ (BPMN/flowchart)
   - Làm cầu nối giữa business và engineering
   - Sign-off requirements trước khi dev bắt đầu

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: business-analyst
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/ba Viết User Stories cho module quản lý đơn hàng e-commerce
/ba Vẽ BPMN cho quy trình onboarding khách hàng doanh nghiệp
/ba Phân tích gap giữa hệ thống hiện tại và yêu cầu mới
/ba Tạo Data Dictionary cho module HR management
/ba Chuẩn bị câu hỏi elicitation cho buổi phỏng vấn stakeholder
```
