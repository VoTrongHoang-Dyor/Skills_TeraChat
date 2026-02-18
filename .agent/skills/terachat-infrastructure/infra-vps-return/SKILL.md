# Role: terachat-infra-vps-return
**Description:** Site Reliability Engineer (SRE) specializing in Hardened Linux, NBDE, and Zero-Knowledge Routing.

## 1. The "Heartbeat Leash" Protocol (Security)
* **Encryption At Rest:** 100% ổ cứng (trừ phân vùng `/boot`) được mã hóa LUKS2 AES-256.
* **Boot Strategy (Clevis/Tang):**
    * VPS đóng vai trò Client (Clevis).
    * Auth Server đóng vai trò Key Server (Tang).
    * **Rule:** VPS không lưu Key giải mã. Khi boot, nó kết nối tới Tang Server qua TLS. Nếu Tang Server từ chối (hoặc không tìm thấy), VPS kẹt ở màn hình boot mãi mãi.
* **Runtime Watchdog (Dead Man's Switch):**
    * Chạy script ngầm (Daemon) ping về Auth Server mỗi 60 giây.
    * **Self-Destruct Condition:** Nếu mất kết nối quá 15 phút (nghi ngờ bị cô lập mạng để điều tra), script tự động thực hiện:
        1. `cryptsetup luksErase`: Xóa header LUKS (biến dữ liệu thành rác vĩnh viễn).
        2. `sysrq-trigger`: Gây Kernel Panic để sập nguồn ngay lập tức.

## 2. Zero-Knowledge Routing (Privacy)
* **Role:** VPS chỉ là "người đưa thư mù" (Blind Relay).
* **Data Flow:**
    * Nhận `EncryptedBlob` từ User A.
    * Đẩy vào Queue (Redis/RabbitMQ).
    * User B online -> Kéo về -> Xóa khỏi Queue.
* **No-Log Policy:**
    * Log Level: `CRITICAL` only.
    * Tuyệt đối không ghi IP người dùng vào file log (tránh truy vết metadata).
    * Sử dụng `rsyslog` chuyển tiếp log về `/dev/null` cho các module không cần thiết.

## 3. Infrastructure as Code (IaC)
* **Immutable Infrastructure:** Không bao giờ SSH vào sửa server thủ công.
* **Tooling:**
    * **Terraform:** Để tạo/hủy VPS trên các Cloud Provider (AWS, DO, Vultr).
    * **Ansible:** Để cấu hình OS, cài đặt Docker và Clevis tự động.
* **Update Strategy:** Khi cần update OS, ta hủy VPS cũ, tạo VPS mới (Blue-Green Deployment) để đảm bảo không tồn tại rác hệ thống.

## 4. Anti-Tamper & Firewall
* **Port Locking:** Chỉ mở Port 443 (TLS) và Port WireGuard (VPN Admin). Đóng toàn bộ Port 22 (SSH) public.
* **Intrusion Detection (Fail2Ban):** Ban IP vĩnh viễn nếu cố gắng scan port hoặc gửi packet dị dạng.
* **Kernel Hardening:** Vô hiệu hóa module USB Storage (để không ai cắm USB vào copy dữ liệu được tại trung tâm dữ liệu).
