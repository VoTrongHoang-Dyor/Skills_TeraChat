---
name: database-design
description: Database design principles and decision-making. Schema design, indexing strategy, ORM selection.
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Database Design

> **Learn to THINK, not copy SQL patterns.**

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the request!** Check the content map, find what you need.

| File | Description | When to Read |
|------|-------------|--------------|
| `docs/architecture/database.md` | Current DB Schema | Understanding context |
| `migrations/` | Migration History | Schema changes |

---

## ⚠️ Core Principle

- **Local-First:** SQLite is the primary citizen.
- **Sync Friendly:** Schema must support CRDTs / Merkle Trees.
- **Encrypted-at-Rest:** Sensitive fields must be encrypted (SQLCipher).

---

## Decision Checklist

Before designing schema:

- [ ] Support for Offline Mode?
- [ ] Conflict Resolution strategy defined?
- [ ] Indexing for local query performance?
- [ ] Migration backward compatibility?
- [ ] Encryption requirements met?

---

## Anti-Patterns

❌ Default to PostgreSQL for client-side storage
❌ Skip indexing on foreign keys
❌ Use SELECT * in large tables
❌ Store JSON when structured data is better
❌ Ignore N+1 queries in loop
