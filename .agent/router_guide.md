# TeraChat Router & Workflow Guide

This guide explains how to use the new Orchestrator Router and Workflows to manage the TeraChat development process.

## 1. Orchestrator Router (`scripts/orchestrator_router.py`)

The router is the central nervous system of the TeraChat agent. It takes slash commands and routes them to the appropriate specialist agent, script, or workflow.

### Usage

Run the script with a command as an argument:

```bash
python3 .agent_TeraChat/scripts/orchestrator_router.py "/command [arguments]"
```

### Supported Commands (Short Aliases)

#### 🏗️ Engineering (Dev Team)

| Command | Target | Purpose |
| :--- | :--- | :--- |
| `/core` | `backend-core-rust` | Core Rust Backend (Logic, Crypto) |
| `/fintech` | `backend-fintech-blind` | Fintech Blind Bridge (Payments) |
| `/ui` | `desktop-tauri-frontend` | Frontend/Desktop (Tauri, React) |
| `/bridge` | `native-bridge-apple` | Native Bridge (Swift, Secure Enclave) |

#### 🛡️ Security & AI

| Command | Target | Purpose |
| :--- | :--- | :--- |
| `/guard` | `ai-gateway-guard` | AI Gateway (PII Filtering) |
| `/audit` | **Script: security_audit.py** | Run Security Audit Scanner |

#### 🧠 Management & Design

| Command | Target | Purpose |
| :--- | :--- | :--- |
| `/orch` | `terachat-orchestrator` | Architecture & Routing |
| `/design` | `terachat-ui-architect` | Hybrid UI Design (Stitch + Secure) |
| `/docs` | `terachat-documentation` | Documentation updates |

### Output Format (JSON)

The router now outputs structured JSON for the Agent to parse:

```json
{
  "action": "CHANGE_CONTEXT",
  "target": "engineering/backend-core-rust",
  "context": "Implement AES-GCM",
  "system_prompt": "You are a Rust Core Specialist...",
  "global_rules": [
    "CONTEXT_FIRST...",
    "SECURITY_HARD..."
  ]
}
```

This ensures the Agent receives the **Target Skill**, the **User Context**, and the **Rules of Engagement** in a single packet.
