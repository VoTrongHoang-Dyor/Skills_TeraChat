---
name: terachat-engineering-ai-integration
description: Zero-Retention AI, PII Redaction
---
# TeraChat AI Integration Skill (The Bridge)

## Description
Tôi là "Cây cầu" an toàn nối giữa dữ liệu nhạy cảm của TeraChat và các mô hình AI (LLMs) mạnh mẽ. Tôi tuân thủ tuyệt đối học thuyết "Data Sovereignty" (Chủ quyền dữ liệu): Dữ liệu của người dùng là tài sản của họ, không phải của AI.

## AI DATA SOVEREIGNTY DOCTRINE (Học thuyết Chủ quyền Dữ liệu - Section 5.8)

### 1. Pre-flight Sanitization (Redaction First)
- **Constraint:** KHÔNG một byte dữ liệu PII nào được phép rời khỏi cụm nội bộ dưới dạng plain-text.
- **Action:**
  - TRƯỚC KHI gửi prompt đến LLM Gateway:
    - Thực thi `PiiRedactor::scan_and_mask(input)`.
    - Mục tiêu: Thẻ tín dụng, SĐT, CCCD/CMND, Email.
    - Thay thế bằng: `[REDACTED_TYPE]`.
  - **Re-hydration:** Sau khi nhận phản hồi, client tự điền lại thông tin nếu cần thiết cho hiển thị.

### 2. Zero-Retention Mandate (Mệnh lệnh Không lưu vết)
- **API Flags:** Luôn bật cờ `zero_retention=true` (hoặc equivalent enterprise flag) trong mọi request gửi đi.
- **Storage Rules:**
  - **RAM:** Chỉ lưu tạm thời (ephemeral), ghi đè ngay sau khi xử lý (Process & Drop).
  - **Disk/DB:** TUYỆT ĐỐI KHÔNG lưu raw Prompt hoặc AI Response vào ổ cứng (trừ khi người dùng chủ động bấm "Lưu").
  - **RAG:** Vector Embeddings phải được lưu cục bộ (Local Vector DB) hoặc trên Private Cloud, không dùng Public Cloud Vector DB.

### 3. Blind Observability (Logging Mù)
- **Tamper-proof & Leakage-proof:** Log phải giúp debug nhưng không được làm lộ bí mật.
- **ALLOWED:** `timestamp`, `latency_ms`, `token_usage`, `model_id`, `error_code`, `request_id`.
- **FORBIDDEN:** `prompt_content`, `response_content`, `user_input_raw`.

## Actions (Bộ công cụ)

### `redact_pii_payload`
- **Mô tả:** Hàm quét và ẩn thông tin nhạy cảm trước khi gửi đi.

### `invoke_ai_gateway`
- **Mô tả:** Gọi AI Model thông qua Proxy bảo mật với cờ Zero-Retention.

### `enforce_data_sovereignty`
- **Mô tả:** Kiểm tra Policy người dùng (Local Only vs Cloud Allowed) để quyết định route request.

### `audit_ai_usage`
- **Mô tả:** Ghi log metadata (không nội dung) để kiểm toán chi phí và hiệu năng.
