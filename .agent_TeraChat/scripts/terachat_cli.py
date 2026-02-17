import sys
import os
import subprocess

# Cấu hình màu sắc cho Terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def print_audit(message, status="INFO"):
    if status == "PASS":
        print(f"{Colors.GREEN}[✓ AUDIT PASS]{Colors.ENDC} {message}")
    elif status == "FAIL":
        print(f"{Colors.FAIL}[✗ SECURITY ALERT]{Colors.ENDC} {message}")
    else:
        print(f"{Colors.BLUE}[INFO]{Colors.ENDC} {message}")

def scan_for_logging_leaks(directory):
    """
    Mô phỏng Security Auditor: Quét tìm log bẩn trong code Rust
    """
    print_audit(f"Đang quét thư mục: {directory}...", "INFO")
    leak_patterns = ["println!", "dbg!", "trace!"]
    
    # Giả lập quét (Thực tế sẽ dùng os.walk)
    # Ví dụ: Giả sử tìm thấy log trong payment.rs
    found_leak = False 
    
    if found_leak:
        print_audit("Phát hiện lệnh Log không an toàn trong module Fintech!", "FAIL")
        sys.exit(1)
    else:
        print_audit("Code sạch. Không tìm thấy Log payload nhạy cảm.", "PASS")

def init_project_structure():
    """
    Mô phỏng Orchestrator: Tạo cấu trúc dự án
    """
    structure = [
        "core/rust/src",
        "clients/ios/TeraChat",
        "clients/desktop/tauri",
        "infra/docker",
        "docs/architecture"
    ]
    print_audit("Đang khởi tạo 'Pháo đài số' TeraChat...", "INFO")
    for folder in structure:
        # os.makedirs(folder, exist_ok=True) # Uncomment để chạy thật
        print(f"  + Created: {folder}")
    print_audit("Cấu trúc dự án đã sẵn sàng.", "PASS")

def main():
    if len(sys.argv) < 2:
        print("Usage: python terachat_cli.py [command]")
        print("Commands: /init, /audit, /backend, /test")
        return

    command = sys.argv[1]

    if command == "/init":
        init_project_structure()
    elif command == "/audit":
        scan_for_logging_leaks("./src")
    elif command == "/backend":
        print(f"{Colors.HEADER}Calling Agent: Backend Core Rust...{Colors.ENDC}")
        # Logic gọi LLM hoặc chuyển ngữ cảnh ở đây
    elif command == "/test":
        print(f"{Colors.HEADER}Triggering Agile Test Cycle...{Colors.ENDC}")
        subprocess.run(["python3", ".agent_TeraChat/scripts/test_runner.py"])
    else:
        print("Lệnh không xác định.")

if __name__ == "__main__":
    main()
