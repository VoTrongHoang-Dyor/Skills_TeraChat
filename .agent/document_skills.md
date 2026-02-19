# 📘 TÀI LIỆU KỸ NĂNG & VAI TRÒ (TERACHAT AGENTIC OS)

> **Nguồn chân lý:** `agents-registry.yaml` — routing trung tâm cho GEMINI.md TIER 0.
> **Global Protocol:** `.agent/GEMINI.md` (`trigger: always_on`) — áp dụng cho MỌI agent.

---

## 1. 🏗️ Đội Ngũ Kỹ Thuật (Engineering)

| Slash CMD | Agent ID | Vai Trò | Data-Driven | Execution Gates |
| :--- | :--- | :--- | :---: | :--- |
| `/backend` | `rust-core-engineer` | **Pháo Đài Số** — Rust Core, Crypto, FFI. _Paranoid Security._ | ✅ `crypto-patterns.csv` | `mem_check`, `fuzz_test`, `clippy` |
| `/fintech` | `wasm-sandbox-architect` | **Người Vận Chuyển Mù** — Fintech Bridge, WASM Sandbox, `.tapp` module. | ❌ | `security_audit --scope wasm` |
| `/bridge` | `native-bridge-apple` | **Cầu Nối Apple** — Swift/macOS, Secure Enclave, Biometrics. | ❌ | `security_audit` |
| — | `native-bridge-windows` | **Cầu Nối Windows** — WinRT, TPM, VirtualLock. | ❌ | `security_audit` |

## 2. 🛡️ Bảo Mật (Security)

| Slash CMD | Agent ID | Vai Trò | Data-Driven | Execution Gates |
| :--- | :--- | :--- | :---: | :--- |
| `/audit` | `crypto-security-auditor` | **Giám Sát Bảo Mật** — Vuln Scanner, Red Team, Memory Hygiene. | ✅ `vuln-checklist.csv` | `security_audit`, `z3_solver`, `fuzz_test` |
| `/guard` | `ai-gateway-guard` | **Cổng Gác AI** — PII Redaction, Dual-Mask, BYOK, Zero-Retention. | ❌ | `security_audit --scope pii` |

## 3. 🏛️ Kiến Trúc & Giao Diện (Architecture & UI)

| Slash CMD | Agent ID | Vai Trò | Data-Driven | Execution Gates |
| :--- | :--- | :--- | :---: | :--- |
| `/ui` | `tauri-desktop-specialist` | **Kiến Trúc Sư Giao Diện** — Tauri, Stitch, List View, Offline-First. | ✅ `colors.csv`, `typography.csv` | `security_audit --scope ui` (XSS) |
| — | `terachat-orchestrator` | **Nhạc Trưởng** — Routing, FFI Rules, Iron Dome Protocol. Fallback only. | ❌ | — |

## 4. ⚙️ Vận Hành & Kiểm Thử (Operations & QA)

| Slash CMD | Agent ID | Vai Trò | Data-Driven | Execution Gates |
| :--- | :--- | :--- | :---: | :--- |
| `/infra` | `devops-architect` | **DevOps** — Hybrid Deploy (Tier 1/2), CI/CD, Air-Gapped. | ✅ `infra-gates.csv` | `security_audit --scope artifact`, `test_runner --suite chaos` |
| `/qa` | `qa-engineer` | **QA Paranoid** — E2E, Leakage Sniff, Chaos, TDD. | ✅ `test-scenarios.csv` | `test_runner`, Mitmproxy sniff |

## 5. 📦 Tài Liệu & Sản Phẩm

| Slash CMD | Agent ID | Vai Trò | Data-Driven |
| :--- | :--- | :--- | :---: |
| `/product` | `product-manager` | **Product Manager** — PRD, Onboarding, Reseller, Feature Flags. | ❌ |
| `/doc` | `technical-writer` | **Technical Writer** — ADR, RFC, CODEOWNERS, Runbooks. | ❌ |

## 6. 🔄 TDRL (Dynamic Resource Loader)

| Slash CMD | Agent ID | Vai Trò | Data-Driven |
| :--- | :--- | :--- | :---: |
| `/tdrl` | `tdrl-engine` | **TDRL** — Cập nhật CSV config động không cần recompile. Ed25519 verify. | ✅ `errors_alerts.csv`, `slash_cmds.csv`, `adaptive_cards.csv` |

---

## 7. 🛠️ CLI Scripts & Workflows

| Lệnh | Script / Workflow | Chức Năng |
| :--- | :--- | :--- |
| `/init` | `scripts/scaffold_terachat.py` | Khởi tạo Monorepo (Rust Core + Swift Bridge) |
| `/audit` | `scripts/security_audit.py` | Quét Log bẩn, PII, unsafe blocks |
| `/build` | `scripts/hermetic_build.py` + `workflows/build.md` | Build sạch Offline Clean Room |
| `/test` | `workflows/test.md` | Pipeline: Backend → Fintech → Native → QA |
| — | `scripts/fuzz_test.py` | Fuzzing parser ≥ 10 phút |
| — | `scripts/mem_check.py` | Memory leak + Zeroize verify |
| — | `scripts/z3_solver.py` | Z3 SMT — phải UNSAT mọi attack vector |
| — | `scripts/test_runner.py` | Unit + Integration, Coverage ≥ 80% |
