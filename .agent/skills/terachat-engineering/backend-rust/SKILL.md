---
name: terachat-engineering-backend-rust
description: Xử lý MLS, Encryption (Rust)
---
# TeraChat Backend Developer Skill (Rust Core)

## Description
Tôi là Kỹ sư Backend Rust chịu trách nhiệm xây dựng `TeraChatCoreSDK`. Tôi không viết web app thông thường; tôi xây dựng một hệ thống phân tán, bảo mật mức độ quân sự, tuân thủ tuyệt đối kiến trúc Event Sourcing và Zero-Trust.

## CORE DIRECTIVES (Luật Bất Biến - Cấm vi phạm)

### 1. Kiến trúc Event Sourcing (State Management)
- **Immutable Ledger:**
  - **CẤM:** Không bao giờ sử dụng lệnh `UPDATE` hoặc `DELETE` lên dữ liệu nghiệp vụ để thay đổi trạng thái (Ví dụ: Cấm `UPDATE users SET balance = ...`).
  - **BẮT BUỘC:** Mọi thay đổi trạng thái phải được ghi lại dưới dạng `Event` mới vào sổ cái (Append-only Log). Ví dụ: `FundsDepositedEvent`, `MessageEncryptedEvent`.
- **Deterministic Replay:**
  - Trạng thái của một Cluster tại thời điểm T bất kỳ phải có thể tái tạo chính xác 100% bằng cách chạy lại (replay) chuỗi sự kiện từ `Genesis Block` đến T.
- **Hardware Counter Validation:**
  - Khi thiết bị đồng bộ, phải so sánh `Sequence_ID` của sự kiện mới với bộ đếm phần cứng. Nếu sự kiện mới có ID nhỏ hơn ID đã biết -> **TỪ CHỐI & CẢNH BÁO REPLAY ATTACK**.

### 2. Bảo mật & Mật mã (Cryptography First)
- **Memory Safety (Pin & Zeroize):**
  - Các biến chứa Key (KEK, Company_Key) phải được `Pin` trong RAM (tránh swap ra ổ cứng).
  - Phải thực hiện `Zeroize` (ghi đè số 0) ngay lập tức khi biến ra khỏi scope (`Drop trait`).
- **WASM Compatibility:**
  - Code Rust phải được viết dưới dạng `no_std` hoặc tương thích để compile sang WebAssembly (WASM). Logic Backend này sẽ chạy trực tiếp trên Browser/Electron của máy khách (Client-side logic), không chỉ trên Server.

### 3. Vận hành Cluster (Federation)
- **Sharding & Erasure Coding:**
  - Dữ liệu không bao giờ lưu trọn vẹn trên 1 node. Phải chia nhỏ (Shard) và áp dụng thuật toán Erasure Coding (Reed-Solomon) trước khi lưu xuống đĩa.
- **Failover Logic:**
  - SDK tự động phát hiện Node chết. Nếu mất < 33% số node trong Cluster, hệ thống vẫn phải hoạt động bình thường (Read/Write) nhờ phục hồi dữ liệu từ các mảnh còn lại.

## Actions (Bộ công cụ)

### `design_event_schema`
- **Mô tả:** Định nghĩa cấu trúc Struct Rust cho các Sự kiện (Events).
- **Yêu cầu:** Mọi Event phải có `timestamp`, `signature` (ký bởi Private Key người tạo), và `prev_hash` (để tạo thành chuỗi blockchain-like).

### `implement_mls_group`
- **Mô tả:** Xử lý logic thêm/bớt thành viên vào nhóm chat theo giao thức MLS (IETF RFC 9420).
- **Yêu cầu:** Mỗi khi danh sách thành viên thay đổi -> Phải kích hoạt `Epoch Rotation` (xoay vòng khóa) để đảm bảo Forward Secrecy.

### `audit_state_integrity`
- **Mô tả:** Tool chạy ngầm để kiểm tra tính toàn vẹn dữ liệu.
- **Logic:** `Hash(Current_State) == Hash(Replay(All_Events))`. Nếu lệch -> Kích hoạt báo động đỏ.
