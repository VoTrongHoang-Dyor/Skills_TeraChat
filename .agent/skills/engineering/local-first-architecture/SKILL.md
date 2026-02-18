---
name: Local-First Architecture
description: Offline-First Strategy, SQLite Optimization, and CRDT Synchronization.
---

# Local-First Architecture (Principal Level)

**Context:** TeraChat must work perfectly when the internet cable is cut. The Local Device is the "Source of Truth".

## 1. The "Database as State" Pattern

> **Principle:** Do not duplicate state in Redux/Context if it lives in SQLite.

### 1.1 Schema Design (SQLite)

- **Wal Mode:** Enable `PRAGMA journal_mode=WAL;` for concurrency.
- **FTS5:** Use Full-Text Search for message search (local performance > remote search).
- **Indexes:** Analyze query patterns. Every `WHERE` clause needs an index.

### 1.2 React Integration

- **Stale-While-Revalidate:**
  1. UI reads from SQLite (Instant).
  2. Background Worker fetches updates from Peer/Server.
  3. Worker writes to SQLite.
  4. UI observes SQLite changes and re-renders.
  - **Result:** Zero spinners.

## 2. Synchronization Strategy (CRDTs)

### 2.1 Conflict Resolution

- **Problem:** Two devices edit the same message offline.
- **Solution:** Hybrid Logical Clocks (HLC) + Last-Write-Wins (LWW) per field.
- **Structure:**

  ```rust
  struct Message {
      id: Uuid,
      content: String,
      updated_at: HLC, // Timestamp + Counter
      is_deleted: bool, // Soft Delete
  }
  ```

### 2.2 Sync Protocol (P2P/Relay)

- **Incremental:** Only sync records changed since `last_sync_vector`.
- **Batching:** Group updates into transactions (500ms debounce).

## 3. Desktop Performance

### 3.1 Threading Model

- **Main Thread:** UI Rendering Only (60FPS).
- **Worker 1 (Database):** SQL Writes, Indexing.
- **Worker 2 (Crypto):** Argon2 hashing, AES-GCM encryption.
- **Rust Core:** Networking & File I/O.

### 3.2 No "Loading" States

- **Direct:** If data isn't in memory, query SQLite synchronously (if < 1ms) or asynchronously with a placeholder (skeleton).
- **Never block:** Use `IntersectionObserver` to lazy-load old history.
