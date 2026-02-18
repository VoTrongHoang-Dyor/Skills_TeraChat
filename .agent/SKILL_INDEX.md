# TeraChat Agent Skills Index

This index lists all specialized skills available to the TeraChat Agent. Each skill acts as a specific role within the development team.

## 🏗️ Engineering (The Builders)
*   **`terachat-engineering/backend-core-rust`** (`/core`): The "Fortress Builder". Handles Core Logic, Cryptography, and FFI in Rust. Rules: "Paranoid Security", No-Async Runtime.
*   **`terachat-engineering/backend-fintech-blind`** (`/fintech`): The "Blind Courier". Handles financial transactions without ever seeing the payload. Rules: Zero-Parse, Blind Idempotency.
*   **`terachat-engineering/desktop-tauri-frontend`** (`/ui`): The "Face". Builds the Desktop UI using Tauri & React.
*   **`terachat-engineering/native-bridge-apple`** (`/bridge`): The "Bridge". Manages Swift/Objective-C code for macOS/iOS, specifically Secure Enclave integration.
*   **`terachat-engineering/native-bridge-windows`**: The "Bridge". Manages Windows-specific native integrations.

## 🧠 AI & Data (The Brains)
*   **`terachat-ai-data/ai-gateway-guard`** (`/guard`): The "Firewall". Intercepts and sanitizes data between User and LLMs. Protocols: Tokenization, Rehydration, Anti-Injection.

## 🏛️ Architecture (The Designers)
*   **`terachat-orchestrator`** (`/orch`): The "Conductor". Routes commands between UI, Core, and Native layers. Enforces "Iron Dome" protocol against panics.
*   **`terachat-ui-architect`** (`/design`): The "Stylist". Hybrid role combining Stitch's aesthetic (Shadcn) with TeraChat's security. Protocols: Zero-Latency UI, Offline-First.

## ⚙️ Operations & Process
*   **`terachat-infrastructure`** (`/ops`): DevOps, CI/CD, and Hermetic Build management.
*   **`terachat-qa`**: Quality Assurance and Testing workflows.
*   **`terachat-product`**: Product management and requirements definitions.
*   **`terachat-documentation`** (`/docs`): Documentation maintenance and "Single Source of Truth".

## 🛠️ Action Scripts (The Hands)
*   **`scripts/terachat_cli.py`**: Main entry point.
*   **`scripts/scaffold_terachat.py`** (`/init`): Automates project creation (Rust Core, Swift Bridge).
*   **`scripts/security_audit.py`** (`/audit`): Automated security scanner (Hard-Constraint enforcement).
*   **`scripts/hermetic_build.py`** (`/build`): Simulates offline, secure builds.
*   **`scripts/orchestrator_router.py`**: Routes specialized commands to the correct agent.
*   **`scripts/test_runner.py`**: Simulates the Agile Testing Cycle.

## 🔄 Workflows
*   **`workflows/test_cycle.md`** (`/test`): Defines the collaboration chain for the `/test` command (Backend -> Fintech -> Native -> QA).
