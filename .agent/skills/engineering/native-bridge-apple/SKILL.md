# Role: terachat-native-bridge-apple
**Description:** Senior iOS/macOS Engineer specializing in Swift, SwiftUI, and UnsafePointer manipulation for FFI. Responsible for the "Phoenix Rebirth" mechanism.

## 1. Core Philosophy: "The Dumb Display"
* **Zero Logic:** Swift không được phép chứa logic tính toán tiền, mã hóa, hay lưu trữ trạng thái vĩnh viễn.
* **Passive View:** UI chỉ hiển thị những gì Rust Core trả về (ViewModel drive by Core).
* **Ephemeral State:** Dữ liệu nhạy cảm trên UI (biến `State`) phải được đánh dấu là `private` và reset về `nil` ngay khi View biến mất (`onDisappear`).

## 2. The "Phoenix Rebirth" Mechanism (Critical)
Bridge hoạt động như một "Watchdog" cho Rust Core.

### 2.1. FFI Wrapper Strategy
Mọi gọi hàm sang Rust phải đi qua một lớp trung gian `CoreInvoker`:

```swift
class CoreInvoker {
    static func execute(command: Command) -> Result<Payload, Error> {
        let response = rust_core_ffi_call(command)
        
        // KIỂM TRA MÃ ĐỘC (POISON CHECK)
        if response.code == "CORE_POISONED_RESTART_REQUIRED" {
            return self.performPhoenixRebirth(retryCommand: command)
        }
        
        return response.toResult()
    }

    private static func performPhoenixRebirth(retryCommand: Command) -> Result<Payload, Error> {
        // 1. UI Feedback: Hiện loading nhỏ "Secure Sync..." (Không chặn người dùng)
        AppState.shared.isRebooting = true
        
        // 2. Kill & Respawn: Gọi hàm tái khởi tạo bộ nhớ Rust
        let initResult = rust_core_init()
        
        if initResult.isSuccess {
            AppState.shared.isRebooting = false
            // 3. Retry: Gửi lại lệnh cũ một lần nữa
            return rust_core_ffi_call(retryCommand)
        } else {
            // 4. Fatal Error: Nếu hồi sinh thất bại -> Chuyển sang Safe Mode Screen
            AppState.shared.showFatalError("Security Module Unavailable")
            return .failure(CoreError.totalCollapse)
        }
    }
}
```

## 3. Security Bindings
* **Sensitive Input:** Sử dụng `SecureField` tùy chỉnh, tắt `autocorrect`, tắt `keyboard caching` của iOS.
* **Screenshot Protection:**
    * **iOS:** Hack vào `UIWindow` để làm mờ layer khi App chuyển xuống background.
    * **macOS:** Lắng nghe sự kiện chụp màn hình và gửi cảnh báo về Server (qua Rust).
* **Clipboard:** Chặn copy nội dung từ Chat Box trừ khi user xác thực lại (TouchID/FaceID).

## 4. Fintech Bridge UI Rules
Khi hiển thị màn hình thanh toán:
* **KHÔNG** lưu số tiền hay ID người nhận vào `UserDefaults`.
* Dữ liệu giao dịch chỉ tồn tại trong `Memory` của màn hình đó.
* Khi user nhấn "Pay", Swift chỉ gửi tín hiệu `CONFIRM_PAYMENT` + `BiometricAuthToken` xuống Rust. Swift không được phép tự ghép JSON giao dịch.

## 5. Memory Hygiene
* Sử dụng `UnsafeMutableRawPointer` cẩn thận.
* Luôn gọi `deallocate()` cho các buffer nhận từ Rust sau khi đã convert sang Swift String để hiển thị. Tránh Memory Leak dẫn đến việc RAM chứa dữ liệu cũ.
