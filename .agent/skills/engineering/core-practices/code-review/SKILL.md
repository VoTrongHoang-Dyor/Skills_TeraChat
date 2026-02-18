---
name: code-review
description: Code review guidelines covering code quality, security, and best practices.
allowed-tools: Read, Glob, Grep
---

# Code Review Checklist

## Quick Review Checklist

### Correctness

- [ ] Code does what it's supposed to do
- [ ] Edge cases handled
- [ ] Error handling in place
- [ ] No obvious bugs

### Security (TeraChat Critical)

- [ ] Input validated and sanitized
- [ ] **Zeroize Protocol:** Sensitive memory wiped?
- [ ] **Log Hygiene:** No PII/Secrets in logs?
- [ ] **Desktop Security:** No unsafe IPC calls?

### Performance

- [ ] No N+1 queries
- [ ] No unnecessary loops
- [ ] Appropriate caching
- [ ] Bundle size impact considered

### Code Quality

- [ ] Clear naming
- [ ] DRY - no duplicate code
- [ ] SOLID principles followed
- [ ] Appropriate abstraction level

### Testing

- [ ] Unit tests for new code
- [ ] Edge cases tested
- [ ] Tests readable and maintainable

### Documentation

- [ ] Complex logic commented
- [ ] Public APIs documented
- [ ] README updated if needed

## AI & LLM Review Patterns

### Logic & Hallucinations

- [ ] **Chain of Thought:** Does the logic follow a verifiable path?
- [ ] **Edge Cases:** Did the AI account for empty states, timeouts, and partial failures?
- [ ] **External State:** Is the code making safe assumptions about file systems or networks?

## Anti-Patterns to Flag

```typescript
// ❌ Magic numbers
if (status === 3) { ... }

// ✅ Named constants
if (status === Status.ACTIVE) { ... }

// ❌ Deep nesting
if (a) { if (b) { if (c) { ... } } }

// ✅ Early returns
if (!a) return;
if (!b) return;
if (!c) return;
// do work

// ❌ Long functions (100+ lines)
// ✅ Small, focused functions

// ❌ any type
const data: any = ...

// ✅ Proper types
const data: UserData = ...
```

## Review Comments Guide

```
// Blocking issues use 🔴
🔴 BLOCKING: SQL injection vulnerability here

// Important suggestions use 🟡
🟡 SUGGESTION: Consider using useMemo for performance

// Minor nits use 🟢
🟢 NIT: Prefer const over let for immutable variable

// Questions use ❓
❓ QUESTION: What happens if user is null here?
```
