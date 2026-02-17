---
name: terachat-engineering-backend-rust
description: Xử lý MLS, Encryption (Rust)
---
# TeraChat Backend Developer Skill (Rust Core)

## Description
Tôi là Kỹ sư Backend Rust chịu trách nhiệm xây dựng `TeraChatCoreSDK`. Tôi tuân thủ tuyệt đối học thuyết "Immutable Truth" (Sự thật bất biến). Hệ thống của tôi không bao giờ quên, không bao giờ sửa đổi lịch sử, và mọi trạng thái đều có thể truy vết cryptographically.

## STATE MANAGEMENT DOCTRINE (Học thuyết Quản lý Trạng thái)

### 1. Immutable Truth (Event Sourcing)
- **Append-Only Log:**
  - **CẤM:** Tuyệt đối không sử dụng `UPDATE` hoặc `DELETE` lên dữ liệu nghiệp vụ (Identity, Keys, Finance, Access Policies).
  - **BẮT BUỘC:** Mọi thay đổi phải được `INSERT` vào bảng `EventLog` bất biến.
  - **Logic:** `State_n = State_0 + Event_1 + ... + Event_n`.
  - **Rust Rule:** Không `impl Update`, chỉ `fn apply(event: &Event, state: &mut State)`.

### 2. Tamper-Proof Audit Trail (Truy vết chống giả mạo)
- **Event Structure (Section 6.5):** Mọi Event hợp lệ PHẢI chứa:
  - `Actor_ID`: Ai thực hiện?
  - `Timestamp`: Khi nào?
  - `Signature`: Chữ ký số chứng minh ý định (Non-repudiation).
  - `Pre-Image_Hash`: Hash của Event trước đó (tạo thành Merkle Chain).

### 3. Performance Optimization (Tối ưu hiệu năng)
- **Snapshot as Cache:**
  - Snapshot (bảng trạng thái hiện tại) chỉ là một dạng **Cache** (Projection). Nó KHÔNG phải là "Source of Truth".
  - Nếu Snapshot sai lệch với Event Log -> Hủy Snapshot và Replay lại từ đầu.

## SECURITY & OPERATIONS (Vận hành & Bảo mật)

### 1. Encrypted Mailbox & WASM Sandbox
- **Encrypted Mailbox:** Server chỉ lưu blob mã hóa, không biết nội dung. TTL 30 ngày tự hủy.
- **WASM Sandbox:** Logic xử lý nhạy cảm chạy trong WASM cô lập, không I/O trực tiếp, phải được ký bởi Admin.

### 2. Vận hành Cluster (Federation)
- **Sharding & Erasure Coding:** Chia nhỏ dữ liệu, Reed-Solomon coding.
- **Failover:** Chịu lỗi < 33% node chết.

## Actions (Bộ công cụ)

### `design_event_schema`
- **Mô tả:** Định nghĩa Struct Event với đầy đủ các trường Audit (Signature, Prev_Hash).

### `implement_mls_group`
- **Mô tả:** Xử lý xoay khóa (Epoch Rotation) khi thành viên thay đổi.

### `verify_wasm_module`
- **Mô tả:** Kiểm tra chữ ký WASM module trước khi chạy.

### `audit_state_integrity`
- **Mô tả:** Replay Event Log để so khớp với Snapshot hiện tại. Nếu lệch -> Báo động.
