---
name: Secure Coding Practices
description: Memory Hygiene, Log Sanitization, and Desktop Security Hardening.
---

# Secure Coding Practices (Principal Level)

**Context:** TeraChat processes top-secret data. A single memory leak or log entry can compromise the entire organization.

## 1. Memory Hygiene (The "Toxic Waste" Rule)

> **Principle:** Metadata is toxic. Key material is radioactive. Treat them accordingly.

### 1.1 Zeroize Everything

- **Rust:** Use `secrecy::Secret<T>` for all keys/passwords.
  - `Drop` trait MUST implement `zeroize()`.
  - **Never** `Clone` a secret unless absolutely necessary (and documented).
- **TypeScript/React:**
  - Avoid holding plain-text passwords in generic State Managers (Redux/Zustand devtools).
  - Use `Uint8Array` for sensitive data, explicitly `fill(0)` when done.

### 1.2 Anti-Forensics

- **Swap File:** Prevent OS from swapping sensitive memory to disk.
  - Rust: `mlock(2)` or `VirtualLock`.
- **Core Dumps:** Disable core dumps in production builds (`ulimit -c 0`).

## 2. Log Sanitization (The "Silent" Rule)

> **Principle:** Logging is the #1 source of data leaks.

### 2.1 The Blacklist

- **NEVER LOG:**
  - Raw Payloads (JSON bodies).
  - Access Tokens / Session IDs.
  - PII (Names, Emails, IPs).
- **INSTEAD LOG:**
  - Correlation IDs (`request_id`).
  - Error Codes (`E_AUTH_FAILED`).
  - Anonymized stats ("Processed 5kb payload").

## 3. Desktop Security Hardening

### 3.1 IPC (Inter-Process Communication)

- **Constraint:** Frontend (Webview) is untrusted.
- **Rule:** Never expose generic `fs.read()` or `shell.exec()`.
- **Pattern:** Create specific commands: `save_encrypted_file(path, data)` instead of `write_file(path, data)`.

### 3.2 XSS in Desktop

- **Context:** An XSS in Electron/Tauri can lead to RCE (Remote Code Execution).
- **Defense:**
  - **CSP:** `script-src 'self'; object-src 'none';`.
  - **Isolation:** Enable `contextIsolation: true`.
  - **Sanitizer:** Use DOMPurify for any rendered markdown/HTML.
  - **Context Isolation:** Enable `contextIsolation: true` in main process.

---

## 4. Vulnerability Management (Scanner Protocols)

> **Source:** Antigravity `vulnerability-scanner` Skill

### 4.1 OWASP Top 10:2025 (Focus Areas)

| Rank | Category | Key Question |
|------|----------|--------------|
| **A01** | Broken Access Control | "Can User A see User B's data?" (IDOR) |
| **A03** | **Supply Chain Security** | "Did we npm install a malware?" |
| **A05** | Injection | "Can I drop tables via this input?" |
| **A10** | **Exceptional Conditions** | "Does it fail securely or crash open?" |

### 4.2 Supply Chain Defense (The "Left of Bang" Rule)

- **Lockfiles:** Must be committed and audited.
- **Dependencies:** Pin versions strictly (`1.2.3`, not `^1.2.3`).
- **CI/CD:** Sign artifacts. Verify checksums.

### 4.3 Risk Prioritization Matrix

Don't fix everything. Fix what matters.

```text
Is it actively exploited (EPSS > 0.5)?
├── YES → CRITICAL: Wake up the CISO.
└── NO → Check CVSS
         ├── ≥ 9.0 → HIGH: Fix in next sprint.
         ├── < 7.0 → LOW: Backlog.
```

---

## 5. Red Team Tactics (Adversary Simulation)

> **Source:** Antigravity `red-team-tactics` Skill

### 5.1 The Attack Lifecycle (MITRE ATT&CK)

```text
RECON → ACCESS → PERSISTENCE → ESCALATION → EVASION → ACTION
```

### 5.2 Tactics & Techniques

#### 1. Reconnaissance (Mapping the Surface)

- **Passive:** DNS enumeration, GitHub dorking (finding leaked keys).
- **Active:** Port scanning (Nmap), Fuzzing endpoints.
- **Defense:** Monitor logs for "loud" scanning patterns.

#### 2. Initial Access & Persistence

- **Phishing:** The #1 vector. Train users.
- **Valid Accounts:** Credential stuffing. Enforce 2FA.
- **Persistence:** Scheduled tasks, Registry run keys (Windows), Cron jobs (Linux).

#### 3. Defense Evasion

- **Living off the Land (LOLBins):** Attacker uses `certutil.exe` or `bash` to download malware (looks legit).
- **Obfuscation:** Base64 encoding payloads to bypass naive WAFs.

### 5.3 Reporting Findings ("The Narrative")

Don't just dump a CVE. Tell the story:

1. **Access:** "I found an exposed .git folder."
2. **Exploit:** "I extracted the config and found a DB password."
3. **Impact:** "I dumped the customer table (1M records)."
4. **Fix:** "Deny access to .git in Nginx config."

---

## ⚙️ Execution Gates

> Không output nào được chấp nhận nếu chưa pass TẤT CẢ gates. (GEMINI.md — TIER 2)

| Gate | Script | Threshold | Spec |
|---|---|---|---|
| Security Audit | `python scripts/security_audit.py` | Zero PII in logs, zero unsafe undocumented | Section 2.7 |
| Z3 Solver | `python scripts/z3_solver.py` | UNSAT cho mọi attack vector | Section 2.9 |
| Fuzzing | `python scripts/fuzz_test.py` | ≥ 10 phút, zero crashes | Section 2.8 |

## ⚡ Slash Commands

| Lệnh | Mô tả | Workflow |
|---|---|---|
| `/audit` | Kích hoạt Security Auditor | `.agent/workflows/audit.md` |

## 📊 Data Sources

Trước khi audit, đọc `resources/vuln-checklist.csv` để tham chiếu 15 vulnerability patterns phổ biến nhất trong TeraChat:

```bash
cat .agent/skills/engineering/secure-coding-practices/resources/vuln-checklist.csv
```

> Mỗi entry có `CWE_ID`, `Detection_Script`, và `Fix_Approach` cụ thể.

