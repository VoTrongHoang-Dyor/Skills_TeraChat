import sys
import re
import os
import json

def load_rules():
    """Simple parser for rules.yaml (subset) to avoid PyYAML dependency."""
    rules = []
    try:
        rules_path = os.path.join(os.path.dirname(__file__), '../rules.yaml')
        with open(rules_path, 'r') as f:
            for line in f:
                if line.strip().startswith('- "' or "- '"):
                    # Extract string content inside quotes
                    rule = line.split('"', 2)[1] if '"' in line else line.split("'", 2)[1]
                    rules.append(rule)
    except Exception as e:
        rules = ["CRITICAL: Could not load rules.yaml. Defaulting to Secure Mode."]
    return rules

def route_command(user_input):
    """
    Routing logic with System Prompt Injection.
    """
    commands = {
        # --- 1. Engineering ---
        "/core": "engineering/backend-core-rust",
        "/fintech": "engineering/backend-fintech-blind",
        "/ui": "engineering/desktop-tauri-frontend",
        "/bridge": "engineering/native-bridge-apple",
        
        # --- 1.1 Core Practices ---
        "/arch": "engineering/core-practices/system-design",
        "/review": "engineering/core-practices/code-review",
        "/db": "engineering/core-practices/database-design",

        
        # --- 2. Security & AI ---
        "/guard": "ai-data/ai-gateway-guard",
        "/audit": "SCRIPT:scripts/security_audit.py",
        
        # --- 3. Management ---
        "/orch": "orchestrator",
        "/product": "product", # Product Manager
        "/design": "ui-architect", # UI Architect
        "/docs": "documentation",
        
        # --- 4. Operations ---
        "/qa": "qa",
        "/infra": "infrastructure",
        "/init": "SCRIPT:scripts/scaffold_terachat.py",
        "/build": "SCRIPT:scripts/hermetic_build.py",
        "/test": "WORKFLOW:test_cycle", # Remapped to internal /test logic if needed
        "/ops": "infrastructure",
        
        # --- Legacy Aliases ---
        "/backend": "engineering/backend-core-rust",
        "/frontend": "engineering/desktop-tauri-frontend",
        "/native": "engineering/native-bridge-apple",
        "/security": "ai-data/ai-gateway-guard",
        "/doc": "documentation"
    }

    system_prompts = {
        "engineering/backend-core-rust": "You are a Rust Core Specialist. Focus on Memory Safety (Zeroize), Async Runtime (Tokio), and Cryptography (Ring). NO ORM, use SQLx.",
        "engineering/backend-fintech-blind": "You are a Fintech Specialist. STRICT 'Blind Bridge' principle. Never see/log raw payment data. Use Tokenization.",
        "engineering/desktop-tauri-frontend": "You are a UI Engineer (Tauri+React). Desktop-First. State-Driven. Trusted UI must use Native implementation, not HTML.",
        "engineering/native-bridge-apple": "You are an iOS Native Specialist. Swift + Secure Enclave. Handle 'Hostile Mock' scenarios. Zero Leaks.",
        "engineering/core-practices/system-design": "You are a System Architect. Focus on Trade-offs, Patterns, and ADRs. Keep it Simple.",
        "engineering/core-practices/code-review": "You are a Code Reviewer. Strict but fair. Focus on Security, Performance, and Clean Code.",
        "engineering/core-practices/database-design": "You are a Database Architect. SQLite Local-First focus. Sync-friendly schema (CRDTs).",
        "ai-data/ai-gateway-guard": "You are an AI Guard. Dual-Mask Protocol (Tokenize -> Send -> Rehydrate). Audit all prompts.",
        "product": "You are a Product Architect. Focus on Strategy, Onboarding, and 'Security Meets Usability'.",
        "ui-architect": "You are a UI Architect. Design for 'Living Color' Trust visualization. Zero-Latency. Offline-First.",
        "qa": "You are a QA Automation Engineer. 'Grey-Box Paranoid'. Test for functionality AND data leakage (sniffing).",
        "infrastructure": "You are a DevOps Architect. Hybrid Deployment (Erasure Coding). Air-Gapped Supply Chain. Immutable Infrastructure.",
        "documentation": "You are a Technical Writer. Clear, concise, single source of truth.",
        "orchestrator": "You are the System Orchestrator. Maintain architecture integrity and routing rules."
    }

    match = re.match(r"^(/[\w-]+)(?:\s+(.*))?$", user_input)
    
    response = {
        "action": "UNKNOWN",
        "target": None,
        "context": None,
        "system_prompt": None,
        "global_rules": load_rules()
    }

    if match:
        cmd = match.group(1)
        context = match.group(2) if match.group(2) else ""
        
        if cmd in commands:
            target = commands[cmd]
            response["target"] = target
            response["context"] = context
            
            if target.startswith("WORKFLOW:"):
                response["action"] = "TRIGGER_WORKFLOW"
                response["target"] = target.replace('WORKFLOW:', '')
            elif target.startswith("SCRIPT:"):
                response["action"] = "EXECUTE_SCRIPT"
                response["target"] = target.replace('SCRIPT:', '')
            else:
                response["action"] = "CHANGE_CONTEXT"
                response["system_prompt"] = system_prompts.get(target, "You are a TeraChat Specialist.")
    
    return json.dumps(response, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        full_command = " ".join(sys.argv[1:])
        print(route_command(full_command))
    else:
        print(route_command(""))
