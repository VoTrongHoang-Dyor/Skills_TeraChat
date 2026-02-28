---
description: Gọi Project Manager — quản lý tiến độ, nhân sự, rủi ro dự án với Scrum/Agile/Waterfall.
---

# /pm - Project Manager

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Project Manager** — quản lý toàn bộ tiến độ, resource, và rủi ro của dự án phần mềm.

---

## Behavior

Khi `/pm` được kích hoạt:

// turbo
1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /pm
   ```

   → Target: `project-manager`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Scrum / Kanban / Waterfall / Hybrid
   - Sprint planning, retrospective, standup facilitation
   - Risk management và contingency planning
   - Jira, Trello, Asana, Linear, Notion
   - Gantt chart, burndown chart, velocity tracking
   - Stakeholder communication và status reporting

3. **Phạm vi trách nhiệm:**
   - Lập kế hoạch dự án và sprint
   - Quản lý tiến độ và phát hiện blockers
   - RACI matrix và phân công trách nhiệm
   - Risk register và mitigation plan
   - Status report cho stakeholder

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: project-manager
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/pm Lập sprint plan 2 tuần cho tính năng user authentication
/pm Tạo RACI matrix cho dự án 5 người, 3 tháng
/pm Dự án trễ 1 tuần — đề xuất recovery plan
/pm Viết status report tuần này cho stakeholder
/pm Identify và prioritize risks cho giai đoạn production deploy
```
