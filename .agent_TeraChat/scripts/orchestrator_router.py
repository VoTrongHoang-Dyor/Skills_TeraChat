import sys
import re

def route_command(user_input):
    """
    Điều hướng lệnh người dùng đến đúng bộ phận kỹ thuật TeraChat.
    """
    commands = {
        "/backend": "terachat-engineering/backend-core-rust",
        "/frontend": "terachat-engineering/desktop-tauri-frontend",
        "/native": "terachat-engineering/native-bridge-apple",
        "/fintech": "terachat-engineering/backend-fintech-blind",
        "/security": "terachat-ai-data/ai-gateway-guard",
        "/devops": "terachat-infrastructure/devops-cicd",
        "/doc": "terachat-documentation",
        "/test": "WORKFLOW:test_cycle" # Lệnh đặc biệt gọi cả quy trình
    }

    # Tách lệnh đầu tiên (ví dụ: /backend)
    match = re.match(r"^(/[\w-]+)", user_input)
    if match:
        cmd = match.group(1)
        if cmd in commands:
            target = commands[cmd]
            if target.startswith("WORKFLOW:"):
                return f"🔄 Kích hoạt quy trình phối hợp: {target.replace('WORKFLOW:', '')}"
            return f"🛡️ Đang kết nối tới bộ phận: {target}..."
    
    return "💡 Đây là TeraChat Orchestrator. Vui lòng dùng lệnh (ví dụ: /backend, /test) để giao việc."

if __name__ == "__main__":
    # Giả lập nhận input từ dòng lệnh
    if len(sys.argv) > 1:
        print(route_command(sys.argv[1]))
    else:
        print(route_command(""))
