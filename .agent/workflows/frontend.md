---
description: Gọi Frontend Developer — xây dựng giao diện người dùng với HTML, CSS, JavaScript, React, Vue, Angular.
---

# /frontend - Frontend Developer

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Frontend Developer** — chuyên gia xây dựng giao diện, component, layout, animation, và tất cả những gì người dùng nhìn thấy.

---

## Behavior

Khi `/frontend` được kích hoạt:

// turbo
1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /frontend
   ```

   → Target: `frontend-developer`

2. **Agent sẽ hoạt động với chuyên môn:**
   - HTML5, CSS3 / SCSS, JavaScript (ES2023+), TypeScript
   - React + Next.js, Vue 3 + Nuxt.js, Angular
   - Tailwind CSS, Shadcn/UI, Styled Components
   - Vite, Webpack — Build & bundling
   - Playwright, Vitest — Frontend testing

3. **Phạm vi trách nhiệm:**
   - UI components và layouts
   - Responsive design (mobile → desktop)
   - State management (Redux, Pinia, Zustand)
   - API integration (Axios, React Query, SWR)
   - Performance optimization (bundle size, Core Web Vitals)

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: frontend-developer
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/frontend Xây dựng responsive navbar với hamburger menu cho mobile
/frontend Tạo dark mode toggle trong React app
/frontend Tối ưu Largest Contentful Paint (LCP) xuống dưới 2.5s
/frontend Viết Vue 3 component cho form đăng ký với validation
/frontend Fix layout bị vỡ trên Safari iOS 16
```
