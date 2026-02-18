# 📘 TÀI LIỆU KỸ NĂNG & VAI TRÒ (TERACHAT AGENT)

Đây là danh sách toàn bộ các kỹ năng (Skills), vai trò (Roles) và lệnh tắt (Shortcuts) của Agent TeraChat.

## 1. 🏗️ Đội Ngũ Kỹ Thuật (Engineering)

| Lệnh Tắt | Skill ID | Vai Trò & Nhiệm Vụ |
| :--- | :--- | :--- |
| `/core` | `backend-core-rust` | **Pháo Đài Số (The Fortress)**<br>Phát triển Core Logic bằng Rust. Chịu trách nhiệm mã hóa, quản lý bộ nhớ an toàn (Zeroize).<br>_Nguyên tắc: "Paranoid Security", No-Async Runtime._ |
| `/fintech` | `backend-fintech-blind` | **Người Vận Chuyển Mù (The Blind Courier)**<br>Xử lý giao dịch tài chính. Chuyển tiếp dữ liệu thanh toán mà không cần giải mã.<br>_Nguyên tắc: Zero-Parse, Blind Idempotency._ |
| `/ui` | `desktop-tauri-frontend` | **Giao Diện (The Face)**<br>Xây dựng UI Desktop với Tauri & React. Tối ưu trải nghiệm người dùng. |
| `/bridge` | `native-bridge-apple` | **Cầu Nối Tự Nhiên (The Bridge)**<br>Kết nối Swift/Objective-C trên macOS/iOS. Quản lý Secure Enclave & Biometrics. |
| - | `native-bridge-windows` | **Cầu Nối Windows**<br>Quản lý tích hợp native trên Windows. |

## 2. 🛡️ Trí Tuệ & Bảo Mật (AI & Security)

| Lệnh Tắt | Skill ID | Vai Trò & Nhiệm Vụ |
| :--- | :--- | :--- |
| `/guard` | `ai-gateway-guard` | **Cổng Gác AI (The Firewall)**<br>Chặn và làm sạch dữ liệu nhạy cảm (PII) trước khi gửi ra ngoài.<br>_Giao thức: Tokenization, Anti-Injection._ |

## 3. 🏛️ Kiến Trúc & Thiết Kế (Architecture)

| Lệnh Tắt | Skill ID | Vai Trò & Nhiệm Vụ |
| :--- | :--- | :--- |
| `/orch` | `terachat-orchestrator` | **Nhạc Trưởng (The Conductor)**<br>Điều phối lệnh giữa UI, Core và Native. Ngăn chặn Panic.<br>_Giao thức: "Iron Dome" (Vòm Sắt)._ |
| `/design` | `terachat-ui-architect` | **Kiến Trúc Sư Giao Diện (The Stylist)**<br>Kết hợp thẩm mỹ (Stitch/Shadcn) với bảo mật (TeraChat).<br>_Giao thức: Zero-Latency UI, Offline-First._ |

## 4. ⚙️ Vận Hành & Quy Trình (Operations)

| Lệnh Tắt | Skill ID | Vai Trò & Nhiệm Vụ |
| :--- | :--- | :--- |
| `/ops` | `terachat-infrastructure` | **Vận Hành (DevOps)**<br>Quản lý CI/CD, Server, và quy trình Build Hermetic (Khép kín). |
| - | `terachat-qa` | **Kiểm Thử (QA)**<br>Quy trình kiểm thử chất lượng phần mềm. |
| - | `terachat-product` | **Sản Phẩm (Product)**<br>Quản lý yêu cầu và định nghĩa tính năng. |
| `/docs` | `terachat-documentation` | **Tài Liệu (Documentation)**<br>Duy trì "Nguồn sự thật duy nhất" (Single Source of Truth). |

## 5. 🛠️ Công Cụ & Script Hỗ Trợ (Actions)

| Lệnh Tắt | Script / Workflow | Chức Năng |
| :--- | :--- | :--- |
| `/init` | `scaffold_terachat.py` | **Khởi Tạo Dự Án**<br>Tự động tạo cấu trúc Monorepo (Rust Core, Swift Bridge). |
| `/audit` | `security_audit.py` | **Kiểm Tra Bảo Mật**<br>Quét mã nguồn tìm lỗi bảo mật nghiêm trọng (Log bẩn, Panic). |
| `/build` | `hermetic_build.py` | **Đóng Gói An Toàn**<br>Giả lập quy trình build sạch (Offline). |
| `/test` | `workflow:test_cycle` | **Kiểm Thử Toàn Diện**<br>Chạy quy trình: Backend -> Fintech -> Native -> QA. |
| - | `terachat_cli.py` | CLI chính của hệ thống. |
| - | `orchestrator_router.py` | Bộ định tuyến lệnh trung tâm. |
