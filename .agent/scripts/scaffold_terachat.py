#!/usr/bin/env python3
"""
TERACHAT SCAFFOLDING ENGINE (The Constructor)
=============================================
Script này tự động tạo cấu trúc dự án Monorepo cho TeraChat theo chuẩn quân sự.
Nó đảm bảo mọi thành phần (Core, UI, Bridge) nằm đúng vị trí quy định.

Cấu trúc tạo ra:
/terachat-monorepo
  ├── core/rust-secure        (Trái tim: Rust + Crypto)
  ├── clients/desktop-tauri   (Mặt tiền: React + Tauri)
  ├── clients/native-apple    (Cầu nối: Swift + Secure Enclave)
  ├── infra/clean-room        (Nhà máy: Docker Offline Build)
  └── docs/architecture       (Hiến pháp: Documentation)
"""

import os
import subprocess
import sys
import json

# --- CẤU HÌNH MÀU SẮC ---
class Colors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

ROOT_DIR = "terachat-monorepo"

def create_dir(path):
    full_path = os.path.join(ROOT_DIR, path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"  [+] Created directory: {full_path}")
    else:
        print(f"  [.] Exists: {full_path}")

def create_file(path, content):
    full_path = os.path.join(ROOT_DIR, path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"  [+] Created file: {full_path}")

def init_rust_core():
    print(f"\n{Colors.HEADER}>>> Initializing Backend Core (Rust)...{Colors.ENDC}")
    base_path = "core/rust-secure"
    create_dir(f"{base_path}/src")
    
    # Cargo.toml với các thư viện bảo mật bắt buộc
    cargo_toml = """
[package]
name = "terachat-core"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib", "rlib"]

[dependencies]
# --- SECURITY & CRYPTO ---
ring = "0.17"
zeroize = { version = "1.7", features = ["derive"] } # Tự động xóa RAM
secrecy = "0.8" # Bảo vệ biến nhạy cảm
aes-gcm = "0.10"
sha2 = "0.10"

# --- ASYNC RUNTIME ---
tokio = { version = "1", features = ["full"] }

# --- SERIALIZATION ---
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
prost = "0.12" # Protobuf

# --- LOGGING (SECURE) ---
tracing = "0.1"
"""
    create_file(f"{base_path}/Cargo.toml", cargo_toml)

    # File lib.rs mẫu với cơ chế Panic Guard
    lib_rs = """
use zeroize::Zeroize;
use std::panic;

// GLOBAL STATE GUARD
pub struct SecureMemory;

impl Drop for SecureMemory {
    fn drop(&mut self) {
        // Tự động kích hoạt khi Core bị Drop/Panic
        println!("[CORE] Wiping sensitive memory...");
    }
}

#[no_mangle]
pub extern "C" fn init_core() {
    let result = panic::catch_unwind(|| {
        println!("[CORE] Initializing TeraChat Secure Enclave...");
        // Logic khởi tạo ở đây
    });

    if result.is_err() {
        eprintln!("[CORE] CRITICAL: PANIC DETECTED DURING INIT");
    }
}
"""
    create_file(f"{base_path}/src/lib.rs", lib_rs)

def init_tauri_client():
    print(f"\n{Colors.HEADER}>>> Initializing Desktop Client (Tauri)...{Colors.ENDC}")
    base_path = "clients/desktop-tauri"
    create_dir(f"{base_path}/src-tauri")
    create_dir(f"{base_path}/src")
    
    # Tauri Config mẫu
    tauri_conf = {
        "build": {
            "beforeDevCommand": "npm run dev",
            "beforeBuildCommand": "npm run build",
            "devPath": "http://localhost:1420",
            "distDir": "../dist"
        },
        "package": {
            "productName": "TeraChat Enterprise",
            "version": "0.1.0"
        },
        "tauri": {
            "allowlist": {
                "all": False,
                "shell": {
                    "all": False,
                    "open": True
                }
            },
            "security": {
                "csp": "default-src 'self'; img-src 'self' asset: https://asset.localhost"
            }
        }
    }
    create_file(f"{base_path}/src-tauri/tauri.conf.json", json.dumps(tauri_conf, indent=2))

def init_native_bridge():
    print(f"\n{Colors.HEADER}>>> Initializing Native Bridge (Apple)...{Colors.ENDC}")
    base_path = "clients/native-apple"
    create_dir(f"{base_path}/TeraChatBridge")
    
    # File Swift mẫu xử lý Phoenix Rebirth
    bridge_swift = """
import Foundation

class CoreInvoker {
    // Hàm gọi xuống Rust Core
    static func sendCommand(_ command: String) {
        // Mô phỏng gọi FFI
        print("[Swift] Sending to Rust: \(command)")
    }
    
    // Hàm xử lý khi Rust Core bị crash
    static func handlePanic() {
        print("[Swift] ALERT: Core Panic Detected! Initiating Phoenix Rebirth...")
        // Code hồi sinh Core ở đây
    }
}
"""
    create_file(f"{base_path}/TeraChatBridge/CoreInvoker.swift", bridge_swift)

def init_infra_docs():
    print(f"\n{Colors.HEADER}>>> Initializing Infra & Docs...{Colors.ENDC}")
    
    # Dockerfile mẫu cho Clean Room Build
    dockerfile = """
# GIAI ĐOẠN 1: CLEAN ROOM BUILD
# Không có internet, chỉ dùng vendor dependencies
FROM rust:1.75-slim as builder
WORKDIR /app
COPY . .
# Chặn mạng bằng cách không cấu hình DNS/Gateway trong container run
RUN cargo build --release --offline
"""
    create_dir("infra/clean-room")
    create_file("infra/clean-room/Dockerfile.secure", dockerfile)

    # Documentation
    create_dir("docs/architecture")
    create_file("docs/architecture/MANIFESTO.md", "# TERACHAT SECURITY MANIFESTO\n\n1. Zero Trust.\n2. Verify Everything.\n3. Fail Secure.")

def main():
    print(f"{Colors.OKGREEN}=== TERACHAT PROJECT SCAFFOLDING ==={Colors.ENDC}")
    
    # Tạo thư mục gốc
    if not os.path.exists(ROOT_DIR):
        os.makedirs(ROOT_DIR)
    
    init_rust_core()
    init_tauri_client()
    init_native_bridge()
    init_infra_docs()
    
    print(f"\n{Colors.OKGREEN}✅ DONE! Project created at './{ROOT_DIR}'{Colors.ENDC}")
    print(f"👉 Next steps:")
    print(f"   cd {ROOT_DIR}")
    print(f"   cargo test  (in core/rust-secure)")

if __name__ == "__main__":
    main()
