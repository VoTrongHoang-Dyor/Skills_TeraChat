---
trigger: always_on
description: "TeraChat Enterprise OS — Security & Architecture Protocol"
version: "2.0.0"
spec_ref: "TeraChat-V0.2.1-TechSpec.md"
applies_to: ALL_AGENTS
---

# TERACHAT.md — Enterprise OS Security Protocol

> **Dự án:** TeraChat Alpha (macOS, Windows, Linux)
> **Kiến trúc lõi:** Desktop-First (Rust + Tauri), Federated Clusters.
> **Nguyên tắc tối thượng:** Dữ liệu không bao giờ rời khỏi thiết bị nếu chưa được mã hóa bằng `Company_Key`. _(Section 1.1)_

---

## 🔴 CRITICAL: SECURITY & ARCHITECTURE PROTOCOL (START HERE)

> **MANDATORY:** Mọi tác vụ lập trình phải tuân thủ nghiêm ngặt mô hình **Zero-Trust**. Bất kỳ dòng code nào xử lý dữ liệu plain-text (chưa mã hóa) ở tầng Network đều bị **reject lập tức**.

### 1. Hạ tầng Cốt lõi (Infra Rules) — _Section 1.1_

- **Không Centralized Server:** Thay thế hoàn toàn kiến trúc VPS đơn lẻ (Single Point of Failure) bằng **Federated Private Clusters**.
- **Routing & Storage:** Sử dụng Cụm VPS Relay (3–5 Nodes chạy **Erasure Coding**) cho mỗi doanh nghiệp. Client kết nối trực tiếp vào Cluster nội bộ, không qua public cloud.
- **Authenticated Identity:** Mọi thiết bị phải pass **Remote Attestation** (Section 2.6) trước khi Server cấp phát Key.

### 2. Tích hợp AI (AI Gateway Bypass) — _Section 5.8_

- **Không LLM Local:** Hệ thống sử dụng **API AI Gateway** (OpenAI/Claude/Azure) qua Middleware.
- **Bảo mật Dữ liệu AI:** Mô hình **BYOK** (Bring Your Own Key). BẮT BUỘC gắn cờ `Zero-Retention` trong mọi API call để đảm bảo nhà cung cấp không dùng dữ liệu để huấn luyện.
- **PII Redactor:** AI Gateway Middleware PHẢI chạy **PII Redaction** trước khi gửi dữ liệu ra ngoài.

---

## 📥 TIER 0: REQUEST CLASSIFIER & AGENT ROUTING

**Hệ thống tự động phân loại và gọi Agent chuyên trách trước khi viết code.**

> 🤖 **Quy tắc Báo cáo:** BẮT BUỘC in ra dòng `🤖 **Applying knowledge of @[agent-name]...**` trước khi trả lời mọi yêu cầu kỹ thuật.

| Loại Yêu Cầu | Keywords (Ví dụ) | Agent Chuyên Trách | Skill Path | Kết Quả Trả Về |
|---|---|---|---|---|
| **🔧 Frontend** | "HTML", "CSS", "React", "Vue", "giao diện", "landing page" | `@frontend-developer` | `skills/frontend/` | HTML/CSS/JS, React/Vue component |
| **🔧 Backend** | "Xử lý file", "SQLite", "CRDT", "Rust", "API server" | `@rust-core-engineer` | `skills/engineering/` | Code Rust logic, API, DB handler |
| **🔧 Fullstack** | "fullstack", "end-to-end", "Next.js", "cả frontend backend" | `@fullstack-developer` | `skills/fullstack/` | Full-stack code (FE + API + DB) |
| **🔧 QA/Testing** | "test", "fuzz", "unit test", "E2E", "kiểm tra" | `@qa-engineer` | `skills/qa/` | Test scripts, coverage report |
| **🔧 DevOps** | "deploy", "Helm", "cluster", "Terraform", "Docker", "CI/CD" | `@devops-architect` | `skills/infrastructure/` | K8s Helm chart, IaC, CI pipeline |
| **🔧 Data** | "data pipeline", "ETL", "BigQuery", "machine learning", "phân tích dữ liệu" | `@data-engineer` | `skills/data/` | Python/SQL scripts, ML model, dashboard |
| **🎨 UI/UX** | "Vẽ UI", "list view", "layout", "Stitch", "design" | `@tauri-desktop-specialist` | `skills/ui-architect/` | UI Component (React/HTML + Tauri) |
| **🎨 Product** | "tính năng mới", "roadmap", "reseller", "onboarding", "PRD" | `@product-manager` | `skills/product/` | PRD, Feature Spec |
| **🎨 Project Mgmt** | "tiến độ", "deadline", "sprint", "scrum", "RACI", "risk" | `@project-manager` | `skills/project-manager/` | Sprint plan, RACI, risk register |
| **💼 BA** | "yêu cầu nghiệp vụ", "user story", "BPMN", "gap analysis" | `@business-analyst` | `skills/business-analyst/` | BRD, User Stories, BPMN diagram |
| **💼 Marketing** | "marketing", "SEO", "content", "campaign", "pitch deck" | `@marketing-sales` | `skills/marketing/` | Marketing plan, copy, pitch deck |
| **💼 CS** | "hỗ trợ khách hàng", "ticket", "FAQ", "SLA", "khiếu nại" | `@customer-support` | `skills/customer-support/` | Support script, FAQ, escalation guide |
| **🛡️ Bảo mật** | "Mã hóa", "P2P", "Key", "MLS", "attestation", "CVE" | `@crypto-security-auditor` | `skills/engineering/secure-coding-practices/` | Implementation MLS, Enclave |
| **🛡️ AI Gateway** | "PII", "redact", "BYOK", "Zero-Retention", "LLM" | `@ai-gateway-guard` | `skills/ai-data/` | Gateway Middleware, Dual-Mask |
| **📝 Tài liệu** | "viết docs", "README", "spec", "RFC", "tài liệu" | `@technical-writer` | `skills/documentation/` | Markdown, RFC |
| **⚙️ TDRL** | "alert", "slash cmd", "CSV config", "error code" | `@tdrl-engine` | `skills/tdrl/` | Cập nhật CSV templates |

---

## 🛑 TIER 1: CORE DEVELOPMENT RULES

### 1. Giao diện (UI/UX Philosophy) — "Data Density" — _Section 1.4_

- **Nghiêm cấm Chat Bubbles:** Không thiết kế giao diện bong bóng chat kiểu mạng xã hội (Facebook/Zalo).
- **Chuẩn hiển thị:** Dùng giao diện **List View** (Slack/Terminal style) để tối đa hóa lượng thông tin — đạt **20 dòng tin nhắn** trên màn hình 13 inch (so với 8 dòng của Zalo).
- **Điều hướng:** Thiết kế **Keyboard-centric** với **Command Palette (`Cmd+K`)** và Slash Commands (`/`) làm trung tâm.
- **Offline-First UI:** Dùng Optimistic UI — phản hồi ngay lập tức khi user thao tác, Rust xử lý ngầm. Nếu lỗi thì rollback state — không gây hoảng loạn cho user.
- **CẤM TUYỆT ĐỐI:** CDN, Google Fonts, remote icons, remote CSS trong bất kỳ asset nào.

### 2. Mã hóa & Bảo vệ Bộ nhớ (Rust Core) — _Section 2.1–2.7_

- **Crypto-Shredding:** Khi xóa dữ liệu, BẮT BUỘC thực hiện xóa **KEK (Key Encryption Key)** từ Secure Enclave/TPM thay vì chỉ overwrite dữ liệu — chống Wear Leveling của SSD/NVMe. _(Section 2.2)_
- **RAM Pinning:** Sử dụng `mlock()` (Linux/macOS) hoặc `VirtualLock()` (Windows) để ghim các trang nhớ chứa Key — tuyệt đối không cho phép OS swap xuống ổ cứng. _(Section 2.3)_
- **Chống dịch ngược:** Bắt buộc dùng crate `obfstr` để mã hóa XOR các chuỗi string nhạy cảm tại thời điểm biên dịch. _(Section 2.7)_
- **Zeroize on Drop:** Mọi struct chứa key material BẮT BUỘC derive `zeroize::Zeroize + ZeroizeOnDrop`.
- **Hardware-Backed Signing:** Private Key KHÔNG BAO GIỜ rời khỏi Secure Enclave/TPM. Ký được thực hiện bên trong chip. _(Section 2.4)_
- **Dead Man Switch:** Thiết bị không verify counter sau **72 giờ offline** → tự động Freeze. _(Section 2.1)_

### 3. Kiến trúc Tiện ích (App Runtime) — _Section 5.1, 5.11_

- **WASM Sandbox:** Mọi Mini-App doanh nghiệp (`.tapp`) **KHÔNG** được gọi thẳng vào OS. Phải chạy cách ly trong **WebAssembly** — không có quyền truy cập Clipboard hệ thống. _(Section 5.1)_
- **Bộ nhớ Cục bộ:** Mỗi Mini-App được cấp một vùng **DB riêng trong SQLCipher** (`App_ID + User_Key`), dữ liệu ghi vào local trước — chỉ đẩy lên Cluster qua Sync Worker khi có mạng. _(Section 5.11.B)_
- **Digital Signature:** App `.tapp` PHẢI có chữ ký Ed25519 của TeraChat hoặc của Doanh nghiệp mới được khởi chạy.
- **Instant-on:** App mở lên là chạy ngay (< **500ms**) — không có màn hình loading khi offline.

### 4. Phân quyền & Kiểm soát Truy cập — _Section 3.3_

- **OPA/ABAC:** Mọi hành động (join group, send file, approve payout) phải được kiểm tra qua **OPA Policy Engine** trước khi thực thi.
- **Identity Lock:** Tên hiển thị bị khóa theo danh tính doanh nghiệp — user **không được tự đổi**.
- **Revocation Immediate:** Khi HR xóa nhân viên → SCIM trigger → TeraChat thu hồi quyền **trong vòng 15 phút** (Custom API) hoặc **real-time** (SCIM 2.0).

### 5. Lưu lượng Dữ liệu & DLP — _Section 4.4_

- **Vùng 1 (Nội bộ):** Dữ liệu **KHÔNG BAO GIỜ** rời khỏi Private Cluster.
- **Vùng 2 (Đối ngoại):** Audit Log **BẮT BUỘC** cho mọi tin nhắn qua Federation Bridge.
- **File nặng:** Gửi file > 1MB qua **P2P trực tiếp** (TeraShare) — không qua Server để tiết kiệm băng thông.

---

## 🛠 TIER 2: FINAL CHECKLIST & DEPLOYMENT PROTOCOL

> **Không một Pull Request hay thay đổi nào được chấp nhận** nếu chưa pass các script kiểm định sau:

| Lệnh Kiểm Định | Mục Tiêu (Ngưỡng Pass) | Section Spec |
|---|---|---|
| `python scripts/fuzz_test.py` | Fuzzing bộ parse dữ liệu — chống Buffer/Integer Overflow, DoS. **Phải chạy ≥ 10 phút.** | 2.8 |
| `python scripts/mem_check.py` | Memory Leak (ASan/MSan) và kiểm tra **Zeroized** vùng nhớ Key sau khi dùng. | 2.3 |
| `python scripts/z3_solver.py` | Chạy Z3 SMT Solver kiểm tra logic Phân quyền (OPA). Kết quả phải là **`UNSAT`** cho mọi attack vector. | 2.9 |
| `cargo clippy -- -D warnings` | **Zero warning** trong toàn bộ Rust Core. | — |
| `python scripts/security_audit.py` | Quét Log bẩn (PII), Panic handler, unsafe blocks. | 2.7 |
| `python scripts/test_runner.py` | Chạy toàn bộ Unit + Integration test. Coverage ≥ 80%. | — |

> **Thái độ của Dev/CEO:**
>
> _"Nếu `mem_check.py` hoặc `fuzz_test.py` thất bại — hủy toàn bộ quy trình merge. Đừng viết thêm tính năng khi nền móng đang có lỗ hổng bộ nhớ."_

### Release Gate (Version Tag `vX.Y.Z`)

Trước khi push tag, tất cả sign-off bắt buộc:

- [ ] **RFC Compliance:** Implementation khớp Spec? _(Architect)_
- [ ] **Z3 Proof:** `UNSAT` cho mọi attack vector? _(Security)_
- [ ] **Fuzzing:** Parser sống sót ≥ 24h fuzzing? _(Backend)_
- [ ] **Chaos Drill:** Hệ thống phục hồi sau 30% node failure? _(DevOps)_
- [ ] **Zeroize Test:** RAM dump sau wipe command = garbage? _(Security)_

---

## 📚 TÀI LIỆU THAM KHẢO

| Tài liệu | Mô tả |
|---|---|
| [`TeraChat-V0.2.1-TechSpec.md`](../TeraChat-V0.2.1-TechSpec.md) | Đặc tả kỹ thuật đầy đủ — nguồn chân lý duy nhất |
| [`router_guide.md`](.agent/router_guide.md) | Hướng dẫn routing và slash commands |
| [`skills/tdrl/SKILL.md`](.agent/skills/tdrl/SKILL.md) | Data-Driven resource loader (Alert/Command updates) |
| [`skills/ui-architect/SKILL.md`](.agent/skills/ui-architect/SKILL.md) | UI/UX design system guidelines |
| [`document_skills.md`](.agent/document_skills.md) | Chỉ số toàn bộ skills |
