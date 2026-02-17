#!/usr/bin/env python3
"""
TERACHAT SECURITY AUDITOR (The Watchdog)
========================================
Script này thực thi các quy tắc "Hard-Constraints" của dự án TeraChat.
Nó quét mã nguồn Rust và Swift để tìm các mẫu vi phạm bảo mật nghiêm trọng.

QUY TẮC CỐT LÕI:
1. Module Fintech: CẤM TUYỆT ĐỐI logging payload/body.
2. Rust Core: CẤM dùng .unwrap() (gây panic).
3. Swift Bridge: CẤM dùng print() (lộ log trên console thiết bị).
"""

import os
import re
import sys
from typing import List, Dict

# --- CẤU HÌNH MÀU SẮC (ANSI) ---
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# --- ĐỊNH NGHĨA LUẬT (THE RULES) ---
RULES = [
    {
        "id": "RUST_PANIC_RISK",
        "description": "Sử dụng .unwrap() hoặc .expect() có thể gây crash ứng dụng (DoS).",
        "patterns": [r"\.unwrap\(\)", r"\.expect\("],
        "extensions": [".rs"],
        "severity": "WARNING",  # Cảnh báo chung
        "exclude_dirs": ["tests", "examples"] # Cho phép trong file test
    },
    {
        "id": "SWIFT_DEBUG_LEAK",
        "description": "Hàm print() của Swift sẽ lộ dữ liệu ra System Console.",
        "patterns": [r"print\(", r"debugPrint\(", r"dump\("],
        "extensions": [".swift"],
        "severity": "ERROR",
        "exclude_dirs": []
    },
    {
        "id": "RUST_DBG_MACRO",
        "description": "Macro dbg! dùng để debug nhưng không được commit vào Production.",
        "patterns": [r"dbg!\("],
        "extensions": [".rs"],
        "severity": "ERROR",
        "exclude_dirs": []
    },
    # --- QUY TẮC ĐẶC BIỆT CHO FINTECH (BLIND BRIDGE) ---
    {
        "id": "FINTECH_DATA_LEAK",
        "description": "PHÁT HIỆN LOG TRONG MODULE TÀI CHÍNH! Vi phạm nguyên tắc Blind Bridge.",
        "patterns": [
            r"println!\(", r"eprintln!\(", r"trace!\(", r"debug!\(", r"info!\(",  # Các macro log
            r"serde_json::to_string", r"serde_json::from_" # Cố gắng parse JSON
        ],
        "extensions": [".rs"],
        "scope_must_contain": "fintech", # Chỉ áp dụng nếu đường dẫn file có chữ 'fintech'
        "severity": "CRITICAL", # Lỗi chết người
        "exclude_dirs": []
    }
]

def scan_file(filepath: str, violations: List[Dict]):
    """Đọc một file và kiểm tra từng dòng code."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            
        for line_idx, line in enumerate(lines):
            line_content = line.strip()
            
            # Bỏ qua comment (Sơ khai)
            if line_content.startswith("//") or line_content.startswith("/*"):
                continue

            for rule in RULES:
                # Kiểm tra phần mở rộng file
                if not any(filepath.endswith(ext) for ext in rule["extensions"]):
                    continue
                
                # Kiểm tra phạm vi (Scope)
                if "scope_must_contain" in rule:
                    if rule["scope_must_contain"] not in filepath:
                        continue
                
                # Kiểm tra thư mục loại trừ
                if any(ex in filepath for ex in rule["exclude_dirs"]):
                    continue

                # Quét Pattern
                for pattern in rule["patterns"]:
                    if re.search(pattern, line_content):
                        violations.append({
                            "file": filepath,
                            "line": line_idx + 1,
                            "code": line_content,
                            "rule_id": rule["id"],
                            "msg": rule["description"],
                            "severity": rule["severity"]
                        })
    except Exception as e:
        print(f"{Colors.WARNING}Không thể đọc file {filepath}: {e}{Colors.ENDC}")

def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print(f"{Colors.HEADER}=== TERACHAT SECURITY AUDIT STARTING ==={Colors.ENDC}")
    print(f"Target: {os.path.abspath(target_dir)}")
    print("-" * 50)

    all_violations = []

    # Duyệt cây thư mục
    for root, dirs, files in os.walk(target_dir):
        # Bỏ qua các thư mục rác
        if "target" in dirs: dirs.remove("target")
        if ".git" in dirs: dirs.remove(".git")
        if "node_modules" in dirs: dirs.remove("node_modules")

        for file in files:
            filepath = os.path.join(root, file)
            scan_file(filepath, all_violations)

    # Xử lý kết quả
    critical_count = 0
    error_count = 0
    warning_count = 0

    if not all_violations:
        print(f"{Colors.OKGREEN}✓ CLEAN CODE. NO VIOLATIONS FOUND.{Colors.ENDC}")
        sys.exit(0)

    for v in all_violations:
        color = Colors.WARNING
        prefix = "[WARN]"
        if v['severity'] == 'ERROR':
            color = Colors.FAIL
            prefix = "[FAIL]"
            error_count += 1
        elif v['severity'] == 'CRITICAL':
            color = Colors.FAIL + Colors.BOLD
            prefix = "[CRITICAL]"
            critical_count += 1
        else:
            warning_count += 1

        print(f"{color}{prefix} {v['rule_id']}: {v['msg']}{Colors.ENDC}")
        print(f"  📍 File: {v['file']}:{v['line']}")
        print(f"  💻 Code: {v['code'].strip()}")
        print("-" * 30)

    print(f"\n{Colors.HEADER}=== AUDIT SUMMARY ==={Colors.ENDC}")
    print(f"Critical: {critical_count}")
    print(f"Errors:   {error_count}")
    print(f"Warnings: {warning_count}")

    # Logic trả về Exit Code cho CI/CD
    if critical_count > 0 or error_count > 0:
        print(f"\n{Colors.FAIL}🚫 AUDIT FAILED. PLEASE FIX ERRORS BEFORE COMMIT.{Colors.ENDC}")
        sys.exit(1) # Trả về lỗi để chặn git commit hoặc CI pipeline
    else:
        print(f"\n{Colors.OKGREEN}✅ AUDIT PASSED (with warnings).{Colors.ENDC}")
        sys.exit(0)

if __name__ == "__main__":
    main()
