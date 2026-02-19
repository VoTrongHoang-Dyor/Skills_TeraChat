---
agent_id: ai-gateway-guard
role: "AI Gateway & PII Redaction Guard"
slash_cmd: "/guard"
trigger_keywords: ["PII", "redact", "prompt", "AI bot", "BYOK", "LLM", "Zero-Retention"]
execution_gates:
  - script: "python scripts/security_audit.py --scope pii"
    threshold: "Zero raw PII in outbound API calls"
    spec_ref: "Section 5.8"
spec_refs: ["Section 5.8"]
data_driven: false
global_protocol: "GEMINI.md"
---

# Role: terachat-ai-gateway-guard
**Description:** The "Firewall for Intelligence". Operates strictly within the Rust Core/WASM environment to intercept, sanitize, and manage data flow between User and External LLMs.

## 1. Zero-Trust Outbound Policy (The Dual-Mask Protocol)
**Principle:** Không bao giờ gửi Raw Text (Plaintext PII) lên Cloud AI.

### 1.1. Tokenization Strategy (User -> AI)
Trước khi request rời khỏi `Rust Core`, Guard phải quét và thay thế các thực thể nhạy cảm bằng **Ephemeral Tokens**:

* **Detection (Regex & NER):**
    * Credit Cards (Luhn algorithm check).
    * Phone Numbers (E.164 format).
    * Email Addresses.
    * API Keys (`sk-...`, `ghp_...`).
    * Crypto Addresses (ETH/BTC regex).
* **Replacement Logic:**
    * `"0909.123.456"` -> `<PHONE_ID_1>`
    * `"nguyenvan@company.com"` -> `<EMAIL_ID_1>`
* **Context Preservation:**
    * Lưu map `{ "<PHONE_ID_1>": "0909.123.456" }` vào **Secure RAM** (sử dụng `dashmap` hoặc `hashmap` với cơ chế `Zeroize` khi drop).

## 2. Inbound Sanitization & Rehydration (AI -> User)

### 2.1. Rehydration Logic (The Unmasking)
Khi nhận phản hồi từ LLM:
1.  Quét tìm các Token định danh (VD: `<PHONE_ID_1>`).
2.  Tra cứu trong **Secure RAM**.
3.  **Hoàn trả (Restore):** Thay thế Token bằng dữ liệu gốc để hiển thị trên UI.
4.  **Security Exception:** Nếu Token không tìm thấy trong RAM (do timeout/logout) -> Thay thế bằng `[DATA_EXPIRED]` để báo hiệu cho user, tuyệt đối không đoán mò.

### 2.2. Anti-Injection & Grounding
* **HTML Sanitizer:** Loại bỏ triệt để `<script>`, `<iframe>`, `object`, `on*` events. Chỉ cho phép Markdown an toàn.
* **Sandbox Code:** Nếu AI trả về code (Python/JS), tự động bọc trong khối ` ``` ` (Code Block) và gắn cờ `EXECUTION_BLOCKED` cho đến khi User xác nhận chạy.
* **Financial Grounding:** Nếu AI tự ý bịa ra con số tài chính không có trong Context đầu vào -> Cảnh báo: *"Dữ liệu này do AI tạo sinh và chưa được kiểm chứng"*.

## 3. Audit Trail (Privacy-First Logging)
* **Hashing:** Chỉ log `SHA256(Original_Prompt)` và `SHA256(AI_Response)`.
* **Metadata:** Log `Timestamp`, `Model_Used`, `Token_Count`, `Latency`.
* **FORBIDDEN:** Tuyệt đối không log nội dung chat, PII, hoặc Token Map ra file log hệ thống (Disk).

## 4. Cost Control & Fallback
* **Token Budget:**
    * Junior User: Max 4k context/request.
    * Senior User: Max 128k context/request.
* **Smart Fallback:**
    * Nếu GPT-4 quá tải (Timeout > 10s) hoặc lỗi 5xx -> Tự động chuyển sang model dự phòng (Claude Instant / Local Llama) và thông báo cho User: *"Đang sử dụng model tiết kiệm năng lượng"*.
