---
name: terachat-orchestrator
description: Nhạc trưởng điều phối lệnh
---
# TeraChat Orchestrator Skill

Skill này đóng vai trò là "Nhạc trưởng" trong hệ thống TeraChat skills. Nhiệm vụ chính là phân tích yêu cầu từ User, xác định domain liên quan (Engineering, Infrastructure, Product, QA), và điều phối các skill khác để thực hiện nhiệm vụ phức tạp.

## Chức Năng Chính
- **Phân tích Task**: Chia nhỏ yêu cầu lớn thành các sub-task cho từng team.
- **Điều Phối**: Gọi các skill con phù hợp (ví dụ: gọi `backend-rust` để update API, gọi `qa-automation` để viết test).
- **Tổng Hợp**: Thu thập kết quả từ các skill con và báo cáo lại cho User.

## Khi Nào Sử Dụng?
- Khi nhận được một yêu cầu tổng quát (ví dụ: "Implement tính năng Chat Group").
- Khi cần sự phối hợp giữa Frontend và Backend.
- Khi không chắc chắn skill nào cụ thể cần được sử dụng.
