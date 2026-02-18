# Workflow: TeraChat Agile Testing Cycle
**Trigger:** `/test`

## Quy trình Liên kết (Collaboration Chain)

Khi lệnh `/test` được kích hoạt, hệ thống sẽ thực hiện tuần tự:

### Bước 1: Unit Test & Security Audit (Backend Lead)
* **Agent:** `backend-core-rust`
* **Nhiệm vụ:**
    1.  Chạy `cargo test`.
    2.  Kiểm tra bộ nhớ: Đảm bảo mọi biến nhạy cảm đã `Drop` (Zeroize).
    3.  Báo cáo: "Core Logic: PASS/FAIL".

### Bước 2: Integration Test (Fintech Specialist)
* **Agent:** `backend-fintech-blind`
* **Nhiệm vụ:**
    1.  Kiểm tra module thanh toán.
    2.  **Verify Hard-Rule:** Quét log xem có lộ `request.body` không.
    3.  Nếu phát hiện log bẩn -> **ABORT & ALERT IMMEDIATELY**.

### Bước 3: UI/Regression Test (Native Bridge)
* **Agent:** `native-bridge-apple`
* **Nhiệm vụ:**
    1.  Giả lập thao tác người dùng (Simulate Tap/Click).
    2.  Kiểm tra cơ chế "Phoenix Rebirth" (Thử làm crash Core và xem UI có hồi phục không).

### Bước 4: Final Report (QA Automation)
* **Agent:** `qa-automation`
* **Nhiệm vụ:** Tổng hợp kết quả từ 3 bước trên thành báo cáo release.
