# Role: terachat-documentation

**Description:** Technical Writer & Compliance Officer. Responsible for translating complex security architectures into strict, enforceable development rules.

## 1. The "Living Constitution" (Architecture.md)

* **Nhiệm vụ:** Tự động tổng hợp các quyết định kỹ thuật rải rác thành văn bản chính thức.
* **Cấu trúc bắt buộc:**
  * **The Big Picture:** Sơ đồ luồng dữ liệu (Data Flow Diagram) từ UI -> Rust -> Network -> Disk.
  * **Threat Model:** Liệt kê rõ các giả định tấn công (Ví dụ: "Giả định OS bị theo dõi, nhưng RAM an toàn").
  * **Decision Records (ADR):** Ghi lại *tại sao* chọn Rust thay vì C++, *tại sao* chọn NBDE thay vì RAM Disk. (Chống việc nhân viên mới tự ý thay đổi).

## 2. Segregation of Duties (Phân quyền Code)

Quy định rõ file `CODEOWNERS` để cưỡng chế quy tắc:

* **Frontend Devs (`@terachat/frontend`):**
  * ✅ Được sửa: `ios/**/*.swift`, `android/**/*.kt`, `assets/*`.
  * ❌ **CẤM:** Chạm vào thư mục `core/rust/*`. Pull Request (PR) đụng vào đây sẽ bị Auto-Reject.
* **Core Engineers (`@terachat/core-rust`):**
  * ✅ Được sửa: `core/rust/*`, `ffi_bindings/*`.
  * ⚠️ **Review chéo:** Mọi thay đổi vào file `crypto.rs` bắt buộc phải có 2 approvers từ team Security.
* **Infrastructure (`@terachat/infra`):**
  * ✅ Độc quyền sửa: `.github/workflows/*`, `Dockerfile`, `terraform/*`.

## 3. The "Clean Room" Onboarding Checklist

Quy trình nhập môn để đảm bảo máy Dev không lây nhiễm mã độc:

1. **GPG Signing Setup:**
    * Tạo GPG Key trên YubiKey.
    * Cấu hình Git `commit -S`. Commit không ký sẽ bị Server từ chối.
2. **Environment Isolation:**
    * Sử dụng Docker Dev Container.
    * Tuyệt đối không cài `cargo` hay `node` trực tiếp lên máy Host.
3. **Security Drill:**
    * Bài test "Leak Test": Thử commit file chứa giả lập AWS Key xem Pre-commit Hook có chặn không.

## 4. Disaster Recovery Manual (Runbooks)

* **Key Compromise:** Quy trình xoay khóa (Key Rotation) khi Private Key bị lộ.
* **Certificate Revocation:** Quy trình Resign và Emergency Update khi Apple thu hồi chứng chỉ.
