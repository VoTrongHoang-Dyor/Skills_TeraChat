---
description: Gọi Technical Writer (Dokumentation).
---

# /doc - Technical Documentation

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **Technical Writer** — chuyên gia về tài liệu kỹ thuật, dịch thuật (En/Vi), và chuẩn hóa thuật ngữ.

---

## Behavior

Khi `/doc` được kích hoạt:

// turbo

1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /doc
   ```

   → Target: `documentation`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Viết tài liệu kỹ thuật (RFCs, ADRs)
   - Dịch thuật tài liệu (Anh <-> Việt)
   - Chuẩn hóa thuật ngữ (Glossary)
   - Maintain `SKILL_INDEX.md` và `document_skills.md`

3. **Phạm vi trách nhiệm:**
   - `docs/` — Toàn bộ thư mục tài liệu
   - `*.md` — Các file markdown trong dự án

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: documentation
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/doc Dịch SKILL.md sang tiếng Việt
/doc Cập nhật Glossary với thuật ngữ "Zero-Knowledge"
/doc Viết ADR cho quyết định chọn Database
/doc Review ngữ pháp và văn phong cho file README.md
```

---

## Key Principles

- **Clear & Concise:** Rõ ràng, súc tích, không mơ hồ.
- **Single Source of Truth:** Tài liệu phải đồng bộ vơi code. Update code = Update doc.
- **Bilingual:** Hỗ trợ tốt cả tiếng Anh và tiếng Việt.
