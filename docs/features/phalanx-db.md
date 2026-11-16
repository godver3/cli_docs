---
title: Phalanx DB
icon: material/database-sync
---

# Phalanx DB

Phalanx DB is a distributed hash-checking network that allows multiple cli_debrid instances to share cached torrent hash data with each other. When enabled, your instance can check whether a torrent hash is cached on debrid without having to query the debrid API directly — using data contributed by other nodes in the network.

Enable it in **Settings → Performance & Logging → Phalanx DB Settings → Enable Phalanx DB**.

---

## Status page

The Phalanx DB status page shows the current connection state and node diagnostics.

### Connection status

| State | Meaning |
|---|---|
| **Disabled** | Phalanx DB is turned off in settings |
| **Connected** | Successfully connected to the Phalanx DB service |
| **Not Connected** | Service is running but not connected — may be under heavy load |

When disabled, the rest of the page is hidden.

### Node information

| Field | Description |
|---|---|
| **Node ID** | This node's unique identifier in the network |
| **Database Entries** | Total number of hashes stored locally |
| **Last Sync** | Timestamp of the last peer synchronisation |

### Memory usage

| Field | Description |
|---|---|
| **RSS** | Resident Set Size — total physical memory in use |
| **Heap Total** | Total JavaScript heap allocated |
| **Heap Used** | JavaScript heap currently in use |
| **External** | Memory used by C++ objects bound to JavaScript |

### Network stats

| Field | Description |
|---|---|
| **Active Connections** | Number of currently connected peers |

---

## Hash Tester

Test whether a specific torrent hash is known to the Phalanx DB network.

1. Enter the torrent info hash into the input field
2. Click **Test Hash**

| Result | Meaning |
|---|---|
| **Cached** (green) | Hash is known and confirmed cached |
| **Not Cached** (red) | Hash is known but not cached |
| **Not Found** (yellow) | Hash is not in the Phalanx DB network |

If found, **Last Modified** and **Expires** timestamps are also shown.
