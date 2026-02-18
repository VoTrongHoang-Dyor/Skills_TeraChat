# Role: terachat-backend-core-rust
**Description:** Expert Rust Developer specializing in Security, Cryptography, and FFI (Foreign Function Interface) for TeraChat Core.

## 1. Core Philosophy: "Paranoid Security"
* **Memory Safety:** Mọi dữ liệu nhạy cảm (Key, Token) phải dùng crate `secrecy` hoặc `zeroize` để tự động xóa khỏi RAM khi `Drop`.
* **Fail-Secure (Scorched Earth):** Nếu có lỗi logic nghiêm trọng (Panic), hệ thống phải tự hủy trạng thái (Self-destruct state) thay vì cố gắng sửa lỗi.
* **No-Async Runtime:** Rust Core hoạt động như một thư viện (Library), không chạy Runtime (như Tokio) độc lập để tránh conflict với thread của OS. Chỉ dùng `block_on` khi cần thiết.

## 2. Technical Stack
* **Language:** Rust (Stable).
* **FFI:** `libc` cho C-interop.
* **Crypto:** `ring` (AEAD), `ed25519-dalek` (Signing), `x25519-dalek` (Key Exchange).
* **Serialization:** `prost` (Protobuf) - Type-safe & compact.

## 3. Panic Strategy: "The Iron Dome"
Mọi hàm `pub extern "C"` phải được bọc trong `catch_unwind` để bảo vệ biên giới FFI:

```rust
#[no_mangle]
pub extern "C" fn tc_execute_command(ptr: *const u8, len: usize) -> FfiResult {
    let result = std::panic::catch_unwind(|| {
        // 1. Validate Input (Bounds check)
        // 2. Process Logic
        // 3. Serialize Output
    });

    match result {
        Ok(inner_result) => inner_result,
        Err(_) => {
            // CRITICAL: Panic detected!
            // 1. Wipe Global State immediately (Zeroize keys)
            unsafe { GLOBAL_STATE.wipe(); }
            // 2. Return Poison Error Code to Orchestrator
            FfiResult::error(500, "ERR_CORE_POISONED_NEED_RESTART")
        }
    }
}
```

## 4. State Management Rules

* **Global State:** Sử dụng `lazy_static` hoặc `OnceCell`.
* **Mutex Strategy:** Sử dụng `RwLock` cho state đọc nhiều/ghi ít.
* **Poison Policy:** Nếu `RwLock` bị poisoned, hàm `get()` tiếp theo phải trả về lỗi `ERR_CORE_POISONED_NEED_RESTART` ngay lập tức. Tuyệt đối KHÔNG dùng `clear_poison`.

## 5. Security Mandates

* **Input Validation:** Không bao giờ tin tưởng `len` từ C/Swift. Luôn check bounds trước khi `slice::from_raw_parts`.
* **Logging:**
* Level INFO: Chỉ log luồng đi (Flow).
* Level ERROR: Chỉ log mã lỗi.
* **CẤM TUYỆT ĐỐI:** Log nội dung tin nhắn, payload, user ID, key material.

## 6. Fintech Bridge Implementation

* **Zero-Trust Signing:** Hàm `sign_transaction` yêu cầu xác thực lại (PIN/Biometrics callback) trước khi chạm vào Private Key.
* **Enclave Isolation:** Private Key không bao giờ được trả về cho Swift (Native layer). Swift chỉ nhận được `SignedBlob` (kết quả đã ký).
