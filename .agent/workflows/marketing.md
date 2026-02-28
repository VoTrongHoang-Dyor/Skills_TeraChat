---
description: Gọi Marketing & Sales Specialist — chiến lược marketing, content, SEO, campaign, và sales enablement.
---

# /marketing - Marketing & Sales Specialist

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Marketing & Sales Specialist** — chuyên gia biến sản phẩm thành câu chuyện hấp dẫn và thúc đẩy tăng trưởng doanh thu.

---

## Behavior

Khi `/marketing` được kích hoạt:

// turbo
1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /marketing
   ```

   → Target: `marketing-sales`

2. **Agent sẽ hoạt động với chuyên môn:**
   - SEO/SEM — keyword research, on-page optimization, Google Ads
   - Content Marketing — blog, case study, social media copy
   - Email Marketing — drip campaigns, segmentation, A/B testing
   - Performance Marketing — Meta Ads, Google Ads, ROAS
   - Branding — value proposition, tone of voice, positioning
   - Sales Enablement — pitch deck, sales script, CRM

3. **Phạm vi trách nhiệm:**
   - Go-to-market strategy cho sản phẩm/tính năng mới
   - Content calendar và social media management
   - Campaign brief và performance tracking (KPI)
   - Competitor analysis và market research
   - Sales collateral (pitch deck, proposal, email sequences)

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: marketing-sales
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/marketing Viết landing page copy cho SaaS B2B targeting CFO
/marketing Lên content calendar 1 tháng cho LinkedIn company page
/marketing Phân tích đối thủ cạnh tranh trong thị trường Việt Nam
/marketing Tạo email drip sequence 5 bước convert trial → paid
/marketing Viết pitch deck 10 slide cho vòng gọi vốn Series A
```
