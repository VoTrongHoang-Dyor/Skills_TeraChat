# TeraChat Dynamic Resource Loader (TDRL)

> **Version:** 1.0.0 | **Spec Refs:** Section 2.1, 3.3, 4.1, 4.3, 5.1, 5.10, 5.11, 6.6

Skill này cung cấp cơ chế **Data-Driven Configuration** cho TeraChat, cho phép cập nhật Error Codes, Security Alerts, Slash Commands và Adaptive Card Templates **mà không cần recompile Rust Core hay rebuild `.tapp` packages**.

---

## Cấu trúc Skill

```text
.agent/skills/tdrl/
├── SKILL.md          ← Hướng dẫn agent (Data-Driven workflow)
├── WORKFLOW.md       ← Quy trình Enterprise Delta Update
├── src/
│   └── resource_loader.rs  ← Rust engine mẫu
└── data/templates/
    ├── errors_alerts.csv   ← Error codes & Security Alerts
    ├── slash_cmds.csv      ← Slash Commands + OPA roles
    └── adaptive_cards.csv  ← Adaptive Card UI templates
```

---

## Quick Start: Thêm tài nguyên mới

### Thêm Security Alert
Mở `data/templates/errors_alerts.csv` và thêm dòng:
```csv
MY_ALERT,SECURITY,my.trigger.event,CRITICAL,"Cảnh báo VI","EN Alert",Notify_User,terachat.security.my_policy,60,true
```

### Thêm Slash Command
Mở `data/templates/slash_cmds.csv` và thêm dòng:
```csv
/my_cmd,"Mô tả VI","EN Desc",Manager,terachat.authz.my_policy,ZONE_1,true,false,1
```

### Thêm Adaptive Card
Mở `data/templates/adaptive_cards.csv` và thêm dòng:
```csv
CARD_MY_FORM,"Card VI","Card EN",assets/cards/my_form.wasm,/my_cmd,,Manager,ZONE_1,true,1.0.0
```

Sau khi sửa CSV → thực hiện **Delta Sync** theo quy trình trong `WORKFLOW.md`.

---

## Đọc thêm

- **SKILL.md** — Quy tắc chi tiết, checklist column bắt buộc, security constraints
- **WORKFLOW.md** — Toàn bộ pipeline Delta Update (signing → distribution → hot-swap)
- **src/resource_loader.rs** — Định nghĩa đầy đủ struct, enum, và logic Rust

---

## Nguyên tắc Cốt lõi

| Nguyên tắc | Cơ chế |
|---|---|
| **Signature-Gated** | Ed25519 verify bắt buộc trước khi load vào SQLCipher |
| **Sanitization Mandatory** | Mọi CSV string → `sanitize_display_string()` trước UI |
| **Zero-Allocation Hot Path** | Lookup trả `&T`, không allocate heap |
| **Offline-First** | Load < 500ms từ SQLCipher khi không có mạng |
| **LAN-Only Distribution** | Không bao giờ tải từ Internet CDN |
