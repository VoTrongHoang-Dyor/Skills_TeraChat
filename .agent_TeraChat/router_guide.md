# TeraChat Router & Workflow Guide

This guide explains how to use the new Orchestrator Router and Workflows to manage the TeraChat development process.

## 1. Orchestrator Router (`scripts/orchestrator_router.py`)

The router is the central nervous system of the TeraChat agent. It takes slash commands and routes them to the appropriate specialist agent or workflow.

### Usage
Run the script with a command as an argument:
```bash
python3 .agent_TeraChat/scripts/orchestrator_router.py "/command [arguments]"
```

### Supported Commands
| Command | Target Agent/Workflow | Purpose |
| :--- | :--- | :--- |
| `/backend` | `terachat-engineering/backend-core-rust` | Core Rust Backend tasks |
| `/frontend` | `terachat-engineering/desktop-tauri-frontend` | Frontend Tauri/React tasks |
| `/native` | `terachat-engineering/native-bridge-apple` | iOS/macOS Native Bridge tasks |
| `/fintech` | `terachat-engineering/backend-fintech-blind` | Fintech & Payment modules |
| `/security` | `terachat-ai-data/ai-gateway-guard` | Security & AI Gateway |
| `/devops` | `terachat-infrastructure/devops-cicd` | CI/CD & Infrastructure |
| `/doc` | `terachat-documentation` | Documentation updates |
| `/test` | **WORKFLOW: test_cycle** | Triggers the Agile Testing Cycle |

## 2. Agile Testing Workflow (`workflows/test_cycle.md`)

The `/test` command triggers a comprehensive testing cycle defined in `workflows/test_cycle.md`.

### Execution Flow
1. **Unit Test & Security Audit**: Checks core logic and memory safety (Zeroize).
2. **Integration Test**: Verifies fintech modules and ensures no sensitive data logging.
3. **UI/Regression Test**: Simulates user interactions and checks crash recovery.
4. **Final Report**: Generates a release report.

To simulate this workflow, run:
```bash
python3 .agent_TeraChat/scripts/test_runner.py
```
