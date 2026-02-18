---
name: system-design
description: Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design.
allowed-tools: Read, Glob, Grep
---

# Architecture Decision Framework

> "Requirements drive architecture. Trade-offs inform decisions. ADRs capture rationale."

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the request!** Check the content map, find what you need.

| File | Description | When to Read |
|------|-------------|--------------|
| `docs/rfcs/*.md` | Active Requests for Comment | Starting architecture design |
| `docs/architecture/*.md` | Current System Architecture | Understanding context |
| `ADR-TEMPLATE.md` | Decision Record Template | Documenting decisions |

---

## 🔗 Related Skills

| Skill | Use For |
|-------|---------|
| `@[skills/engineering/core-practices/database-design]` | Database schema design |
| `@[skills/engineering/backend-core-rust]` | Rust Core Implementation |
| `@[skills/infrastructure]` | Deployment architecture |

---

## Core Principle

**"Simplicity is the ultimate sophistication."**

- Start simple
- Add complexity ONLY when proven necessary
- You can always add patterns later
- Removing complexity is MUCH harder than adding it

---

## Validation Checklist

Before finalizing architecture:

- [ ] Requirements clearly understood
- [ ] Constraints identified (Offline-First, Zero-Knowledge)
- [ ] Each decision has trade-off analysis
- [ ] Simpler alternatives considered
- [ ] ADRs written for significant decisions
- [ ] Security impact assessed (Threat Model)
