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

#### ⚙️ Operations & Actions
| Command | Target | Purpose |
| :--- | :--- | :--- |
| `/init` | **Script: scaffold_terachat.py** | Initialize Project Structure |
| `/build` | **Script: hermetic_build.py** | Run Hermetic Build |
| `/test` | **Workflow: test_cycle** | Trigger Agile Test Cycle |
| `/ops` | `terachat-infrastructure` | DevOps/Infrastructure |

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
