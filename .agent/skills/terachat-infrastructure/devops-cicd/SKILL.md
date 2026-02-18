# Role: terachat-ci-cd-pipeline
**Description:** DevOps Architect specializing in DevSecOps, Hermetic Builds, and Supply Chain Security.

## 1. The "Clean Room" Policy (Hermetic Build)
**Nguyên tắc:** Biến quá trình build thành một hộp đen cô lập.
* **Vendoring Mandate:**
    * **Rust:** Toàn bộ Crates phải được `cargo vendor` và commit vào Repo nội bộ hoặc lưu trong Artifactory riêng (Offline Mirror).
    * **Swift:** Swift Packages phải được mirror về Local.
* **Offline Compilation:**
    * Container Build (Docker) chạy với flag `--network none`.
    * Nếu lệnh Build cố gắng kết nối ra ngoài -> **FAIL NGAY LẬP TỨC**.
    * **Mục tiêu:** Ngăn chặn các script `build.rs` độc hại lén tải mã độc hoặc gửi telemetry ra ngoài.

## 1.2 Base Image Provenance (Nguồn gốc Image)
* **NO DOCKER HUB DIRECT:** Cấm sử dụng `FROM rust:latest` hoặc các image cộng đồng trong Dockerfile sản xuất.
* **Bootstrapping Process:**
    1. Start from `debian:bookworm-slim` (Verified SHA256 từ trang chủ Debian).
    2. Download `rustup-init`.
    3. **MANDATORY:** Verify GPG Signature của `rustup-init` với Key công khai của Rust Foundation.
    4. Install Toolchain -> Export ra Docker Image nội bộ (`terachat-core-builder`).
* **SBOM (Software Bill of Materials):** Mọi Image nội bộ phải đi kèm file SBOM (danh sách toàn bộ gói phần mềm bên trong) để quét lỗ hổng định kỳ (dùng `syft` hoặc `trivy`).

## 2. Reproducible Builds (Xây dựng lặp lại)
**Goal:** `Hash(Build_Hôm_Nay) == Hash(Build_Ngày_Mai)` với cùng một Source Code.
* **Technique:**
    * Set `SOURCE_DATE_EPOCH` để cố định timestamp trong binary.
    * Xóa bỏ mọi đường dẫn tuyệt đối (Absolute Path) trong debug symbols (`-remap-path-prefix`).
    * **Immutable Build Environment:** Sử dụng Docker Image được định danh bằng Digest SHA256 (VD: `rust@sha256:abc...`), tuyệt đối KHÔNG dùng tag động như `:latest`.

## 3. The Signing Ceremony (Quy trình ký số tách biệt)
Server CI (GitHub Actions/GitLab CI) **KHÔNG ĐƯỢC PHÉP** chứa Private Key.

* **Bước 1 (Build):** CI Server (Offline) tạo ra file `TeraChat-Unsigned.dmg` / `.exe`.
* **Bước 2 (Transport):** Gửi Hash của file sang **Secure Signing Server** (Server vật lý hoặc Cloud KMS trong VPC riêng biệt).
* **Bước 3 (Sign):** Signing Server dùng Key nằm trong HSM (YubiKey/AWS KMS) để ký lên Hash đó.
* **Bước 4 (Verify & Attach):** Trả về Signature. CI Server ghép lại thành `TeraChat-Signed.dmg`.

## 4. Artifact Hardening
* **Windows:** Bắt buộc bật ASLR (Address Space Layout Randomization) và DEP/NX bit.
* **macOS:** Bắt buộc Hardened Runtime, Notarization ticket (stapled).
* **Linux:** Strip binaries, check RPATH để tránh bị load thư viện lạ (DLL Hijacking).

## 5. Deployment Gates (Chốt chặn cuối cùng)
Trước khi release, hệ thống tự động chạy:
1.  **SAST:** Scan code tĩnh tìm lỗ hổng.
2.  **Dependency Audit:** Check CVE của thư viện (`cargo audit` với database offline).
3.  **VirusTotal Check:** Upload hash lên VirusTotal (từ vùng DMZ có mạng) để đảm bảo không bị nhận diện nhầm là malware.
