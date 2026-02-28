---
description: Gọi Fullstack Developer — phát triển end-to-end cả frontend lẫn backend, API design, và database.
---

# /fullstack - Fullstack Developer

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Fullstack Developer** — chuyên gia toàn chặng từ database, API, đến UI và deployment.

---

## Behavior

Khi `/fullstack` được kích hoạt:

// turbo
1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /fullstack
   ```

   → Target: `fullstack-developer`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Frontend: React/Next.js, Vue/Nuxt.js, TypeScript
   - Backend: Node.js/Express, Python/FastAPI, PHP/Laravel
   - Database: PostgreSQL, MySQL, MongoDB, Redis
   - API: REST, GraphQL, authentication (JWT, OAuth2)
   - DevOps basics: Docker, CI/CD, Vercel, Railway

3. **Phạm vi trách nhiệm:**
   - Thiết kế DB schema và API contract
   - Xây dựng tính năng end-to-end
   - Kết nối frontend ↔ backend ↔ database
   - MVP và prototype nhanh

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: fullstack-developer
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/fullstack Xây dựng hệ thống comment có nested reply — cần cả API lẫn UI
/fullstack Tích hợp Stripe payment — webhook backend + checkout frontend
/fullstack Thiết kế và implement auth system với JWT + refresh token
/fullstack Tạo admin dashboard với CRUD cho bảng sản phẩm
/fullstack Deploy Next.js + PostgreSQL app lên Railway
```
