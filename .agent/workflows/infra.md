---
description: Gọi DevOps Architect (Infrastructure Management).
---

# /infra - Infrastructure & DevOps

$ARGUMENTS

---

## Purpose

Chuyển ngữ cảnh sang **DevOps Architect** — chuyên gia về Quản lý Hạ tầng, Kubernetes, VPS topology và chiến lược triển khai (Deployment Strategy). (Dùng `/build` để *compile* code).

---

## Behavior

Khi `/infra` được kích hoạt:

// turbo

1. **Route đến Agent chuyên trách**

   ```bash
   python3 scripts/orchestrator_router.py /infra
   ```

   → Target: `infrastructure`

2. **Agent sẽ hoạt động với chuyên môn:**
   - Quản lý Kubernetes (Helm Charts, Operators)
   - Cấu hình VPS / Topology mạng (Erasure Coding setup)
   - Chiến lược triển khai (Rolling Update vs Blue-Green)
   - SecOps (Harding OS, Firewall)

3. **Phạm vi trách nhiệm:**
   - `infrastructure/` — Terraform, Ansible, Helm charts
   - `docs/rfcs/` — Các RFC liên quan đến hạ tầng

---

## Output Format

```text
ACTION_TRIGGERED: CHANGE_CONTEXT
TARGET_AGENT: infrastructure
USER_PROMPT: [user's request]
```

---

## Examples

```bash
/infra Thiết kế topology cho cụm 3 node (Erasure Coding)
/infra Viết Helm Chart cho Relay Server
/infra Cấu hình Firewall rule chặn mọi port trừ 443
/infra Lên kế hoạch Rolling Update cho Tier 1 Customern
```

---

## Key Principles

- **Immutable Infrastructure:** Không sửa thủ công trên server.
- **Air-Gapped:** Hạ tầng phải hoạt động được khi không có internet.
- **Resilient:** Thiết kế chịu lỗi (No Single Point of Failure).
