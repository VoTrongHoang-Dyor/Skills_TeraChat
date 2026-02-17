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

    # Tách lệnh đầu tiên (ví dụ: /core) khỏi phần còn lại (arguments)
    # Ví dụ: "/core fix memory leak" -> cmd="/core", context="fix memory leak"
    match = re.match(r"^(/[\w-]+)(?:\s+(.*))?$", user_input)
    
    if match:
        cmd = match.group(1)
        context = match.group(2) if match.group(2) else ""
        
        if cmd in commands:
            target = commands[cmd]
            
            if target.startswith("WORKFLOW:"):
                workflow_name = target.replace('WORKFLOW:', '')
                return f"🔄 Kích hoạt quy trình phối hợp: {workflow_name}\nCONTEXT: {context}"
            
            if target.startswith("SCRIPT:"):
                script_path = target.replace('SCRIPT:', '')
                # Trong thực tế, hệ thống sẽ chạy lệnh này. Ở đây ta in ra hướng dẫn.
                return f"⚡ Thực thi Script: python3 .agent_TeraChat/{script_path} {context}"
                
            # Trả về format chuẩn để Agent nhận diện
            return f"🛡️ ROUTING_TO: {target}\nCONTEXT: {context}"
    
    return "💡 TeraChat Orchestrator: Gõ /help hoặc xem Document_Skills.md để biết danh sách lệnh."

if __name__ == "__main__":
    # Nối tất cả tham số dòng lệnh thành một chuỗi duy nhất để xử lý
    # Ví dụ: python script.py /core fix bug -> "/core fix bug"
    if len(sys.argv) > 1:
        full_command = " ".join(sys.argv[1:])
        print(route_command(full_command))
    else:
        print(route_command(""))
