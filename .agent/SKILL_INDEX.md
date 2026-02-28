# TeraChat Agent Skills Index

This index lists all specialized skills available to the TeraChat Agent. Each skill acts as a specific role within the development team.

---

## 🔧 Technical Teams (Bộ phận Kỹ thuật)

| Skill ID | Slash | Skill Path | Chuyên Môn |
|---|---|---|---|
| `frontend-developer` | `/frontend` | `skills/frontend/` | HTML, CSS, JavaScript, React, Vue, Angular |
| `rust-core-engineer` | `/backend` | `skills/engineering/backend-core-rust/` | Rust, Crypto, Memory Safety, FFI |
| `fullstack-developer` | `/fullstack` | `skills/fullstack/` | Next.js, Node.js, Laravel, PostgreSQL, API design |
| `qa-engineer` | `/qa` | `skills/qa/qa-automation/` | Unit Test, E2E, Playwright, coverage ≥80% |
| `devops-architect` | `/infra` | `skills/infrastructure/devops-cicd/` | Docker, Kubernetes, Helm, Terraform, CI/CD |
| `data-engineer` | `/data` | `skills/data/` | Python, SQL, Airflow, BigQuery, ML models |

---

## 🎨 Product & Design (Bộ phận Sản phẩm)

| Skill ID | Slash | Skill Path | Chuyên Môn |
|---|---|---|---|
| `tauri-desktop-specialist` | `/ui` | `skills/ui-architect/` | Desktop UI, Stitch, Shadcn/UI, Tauri, Offline-First |
| `product-manager` | `/product` | `skills/product/` | PRD, Feature Flags, Roadmap, Onboarding, MSP |
| `project-manager` | `/pm` | `skills/project-manager/` | Scrum, Sprint Planning, RACI, Risk Register |

---

## 💼 Business & Ops (Bộ phận Kinh doanh)

| Skill ID | Slash | Skill Path | Chuyên Môn |
|---|---|---|---|
| `business-analyst` | `/ba` | `skills/business-analyst/` | BRD, User Stories, BPMN, Gap Analysis |
| `marketing-sales` | `/marketing` | `skills/marketing/` | SEO, Content, Campaign, Pitch Deck, Email Drip |
| `customer-support` | `/cs` | `skills/customer-support/` | Support Script, FAQ, SLA, Escalation Matrix |

---

## 🛡️ Security & Specialized

| Skill ID | Slash | Skill Path | Chuyên Môn |
|---|---|---|---|
| `crypto-security-auditor` | `/audit` | `skills/engineering/secure-coding-practices/` | MLS, Remote Attestation, Z3 Solver |
| `ai-gateway-guard` | `/guard` | `skills/ai-data/ai-gateway-guard/` | PII Redaction, BYOK, Zero-Retention |
| `wasm-sandbox-architect` | `/bridge` | `skills/engineering/` | WASM, .tapp mini-app, Sandbox isolation |
| `technical-writer` | `/doc` | `skills/documentation/` | Markdown, RFC, README, TechSpec |
| `tdrl-engine` | `/tdrl` | `skills/tdrl/` | Dynamic Resource Loader (CSV, alerts, slash cmds) |

---

## 🛠️ Action Scripts

- `scripts/orchestrator_router.py` — Routes slash commands to the correct agent
- `scripts/security_audit.py` (`/audit`) — Automated security scanner
- `scripts/hermetic_build.py` (`/build`) — Offline secure build simulator
- `scripts/test_runner.py` — Agile Testing Cycle runner
- `scripts/scaffold_terachat.py` (`/init`) — Project scaffolding (Rust Core + Tauri)

---

## 🔄 Workflows

| Workflow | Slash | Mô tả |
|---|---|---|
| `workflows/frontend.md` | `/frontend` | Frontend Developer agent |
| `workflows/backend.md` | `/backend` | Backend Rust Specialist agent |
| `workflows/fullstack.md` | `/fullstack` | Fullstack Developer agent |
| `workflows/qa.md` | `/qa` | QA Automation Engineer agent |
| `workflows/infra.md` | `/infra` | DevOps Infrastructure agent |
| `workflows/data.md` | `/data` | Data Engineer/Scientist agent |
| `workflows/ui.md` | `/ui` | UI/UX Architect agent |
| `workflows/product.md` | `/product` | Product Manager agent |
| `workflows/pm.md` | `/pm` | Project Manager agent |
| `workflows/ba.md` | `/ba` | Business Analyst agent |
| `workflows/marketing.md` | `/marketing` | Marketing & Sales agent |
| `workflows/cs.md` | `/cs` | Customer Support agent |
| `workflows/audit.md` | `/audit` | Security Audit agent |
| `workflows/guard.md` | `/guard` | AI Gateway Guard agent |
| `workflows/doc.md` | `/doc` | Technical Writer agent |
| `workflows/test.md` | `/test` | Agile Test Cycle chain |
| `workflows/build.md` | `/build` | Hermetic Build pipeline |
| `workflows/init.md` | `/init` | Project scaffold |
