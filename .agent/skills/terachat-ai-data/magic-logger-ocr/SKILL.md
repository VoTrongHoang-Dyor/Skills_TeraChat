# Role: terachat-magic-logger-ocr
**Description:** Expert in On-Device AI, Computer Vision, and Embedded Vector Databases. Responsible for turning "Dumb Data" (Images/Logs) into "Smart Context" without leaking privacy.

## 1. Zero-Cloud Policy (Quy tắc Bất di bất dịch)
* **OCR Engine:** Bắt buộc sử dụng Native API của hệ điều hành hoặc thư viện nhúng (Embedded Lib).
    * **macOS/iOS:** Sử dụng `Vision Framework` (Cực nhanh, tối ưu NPU). Gọi qua Swift Bridge.
    * **Windows:** Sử dụng `Windows.Media.Ocr`.
    * **Linux:** Sử dụng `Tesseract 5` (bản tối ưu `wasm-simd`) hoặc `ONNX Runtime`.
* **Embedding Model:** Chạy mô hình ngôn ngữ nhỏ (ví dụ: `all-MiniLM-L6-v2` ~80MB) ngay trong Rust Core để biến văn bản thành Vector. **Không gọi OpenAI API để lấy Embedding.**

## 2. "Lazy & Thermal-Aware" Pipeline (Quản lý Hiệu năng)
Để tránh làm nóng máy hoặc tốn pin:
* **Queueing Strategy:** Khi nhận ảnh, không OCR ngay lập tức (trừ khi user yêu cầu). Đẩy vào hàng đợi ưu tiên thấp (`BackgroundQueue`).
* **Condition Check:**
    * Chỉ chạy OCR khi: `CPU Load < 30%` VÀ `Battery > 20%` (hoặc đang cắm sạc).
    * Nếu phát hiện `ThermalState == Serious` (Máy nóng), lập tức tạm dừng Indexing.
* **Batch Processing:** Xử lý từng ảnh một, `sleep(500ms)` giữa các lần xử lý để nhường CPU cho UI.

## 3. Local Vector Search (RAG tại chỗ)
* **Database:** Sử dụng `LanceDB` (Native Rust) hoặc `SQLite-vec` để lưu trữ Vector Embeddings.
* **Lợi ích:**
    * User có thể tìm kiếm tự nhiên: *"Hợp đồng ký với ông A tháng trước"* -> Hệ thống tự quét nội dung trong ảnh/PDF để trả về kết quả.
    * Tốc độ phản hồi < 50ms vì không cần mạng.

## 4. Secure Redaction (Trước khi lưu)
* Ngay sau khi OCR xong, text thô phải đi qua bộ lọc **Regex Guard**:
    * Tự động đánh dấu vị trí chứa SĐT, Email, Số thẻ trong metadata.
    * Khi hiển thị kết quả tìm kiếm, làm mờ các thông tin này (UI Masking) cho đến khi user bấm "Reveal".

## 5. Storage Lifecycle (Vòng đời dữ liệu)
* **Encrypted Storage:** Vector Database cũng phải được mã hóa bằng key của User (SQLCipher / ChaCha20).
* **Auto-Prune:** Tự động xóa Index của tin nhắn cũ hơn 90 ngày (hoặc theo chính sách công ty) để tiết kiệm dung lượng ổ cứng người dùng.
