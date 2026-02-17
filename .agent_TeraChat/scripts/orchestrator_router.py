import sys
import re

def route_command(user_input):
    """
    Điều hướng lệnh người dùng đến đúng bộ phận kỹ thuật TeraChat.
    """
    commands = {
        # --- 1. Nhóm Kỹ Thuật (Dev Team) ---
        "/core": "terachat-engineering/backend-core-rust",
        "/fintech": "terachat-engineering/backend-fintech-blind",
        "/ui": "terachat-engineering/desktop-tauri-frontend",
        "/bridge": "terachat-engineering/native-bridge-apple",
        
        # --- 2. Bảo Mật & AI ---
        "/guard": "terachat-ai-data/ai-gateway-guard",
        "/audit": "SCRIPT:scripts/security_audit.py", # Chạy script
        
        # --- 3. Quản Trị & Thiết Kế ---
        "/orch": "terachat-orchestrator",
        "/design": "terachat-ui-architect",
        "/docs": "terachat-documentation",
        
        # --- 4. Vận Hành & Hành Động (Action) ---
        "/init": "SCRIPT:scripts/scaffold_terachat.py",
        "/build": "SCRIPT:scripts/hermetic_build.py",
        "/test": "WORKFLOW:test_cycle",
        "/ops": "terachat-infrastructure/devops-cicd",

        # --- Legacy Support (Backwards Compatibility) ---
        "/backend": "terachat-engineering/backend-core-rust",
        "/frontend": "terachat-engineering/desktop-tauri-frontend",
        "/native": "terachat-engineering/native-bridge-apple",
        "/security": "terachat-ai-data/ai-gateway-guard",
        "/doc": "terachat-documentation"
    }

    # Tách lệnh đầu tiên (ví dụ: /core)
    match = re.match(r"^(/[\w-]+)", user_input)
    if match:
        cmd = match.group(1)
        if cmd in commands:
            target = commands[cmd]
            
            if target.startswith("WORKFLOW:"):
                return f"🔄 Kích hoạt quy trình phối hợp: {target.replace('WORKFLOW:', '')}"
            
            if target.startswith("SCRIPT:"):
                script_path = target.replace('SCRIPT:', '')
                return f"⚡ Thực thi Script: python3 .agent_TeraChat/{script_path}"
                
            return f"🛡️ Đang kết nối tới bộ phận: {target}..."
    
    return "💡 TeraChat Orchestrator: Gõ /help hoặc xem router_guide.md để biết danh sách lệnh."

if __name__ == "__main__":
    # Giả lập nhận input từ dòng lệnh
    if len(sys.argv) > 1:
        print(route_command(sys.argv[1]))
    else:
        print(route_command(""))
