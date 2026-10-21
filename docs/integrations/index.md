---
title: Integrations Overview
icon: material/connection
---

# Integrations

CLI_Debrid integrates with a number of external services. Some are required, others are optional.

---

## Required

| Integration | Purpose |
|---|---|
| [Zurg + rclone](zurg.md) | Mounts your debrid cloud library as a local filesystem Plex can read |
| [Decypharr](decypharr.md) | All-in-one debrid client with built-in DFS/rclone mounting and symlink delivery |
| [Plex](plex.md) | Media server — scans and serves your Debrid library |

---

## Recommended

| Integration | Purpose |
|---|---|
| [Seerr](seerr.md) | Request management — lets users request movies and shows |

---

## Optional

| Integration | Purpose |
|---|---|
| [Jellyfin](jellyfin.md) | Alternative to Plex |
| [Trakt](../configuration/additional.md#trakt) | Content source (watchlist, lists, collection) and metadata fallback if no TVDB key is set |
| [Bazarr](../configuration/additional.md#bazarr-integration) | Automatic subtitle downloading |
| [TMDB](../configuration/additional.md#tmdb) | Poster art, Discover page, trending content |
