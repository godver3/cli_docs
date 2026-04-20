---
title: Mount your debrid storage
icon: material/harddisk
---

# Step 2 — Mount your debrid storage

Before cli_debrid can manage your library, your debrid cloud storage needs to be mounted as a local folder. Your media server (Plex/Jellyfin) reads from this folder as if it were a regular hard drive.

Two tools handle this:

| Tool | Debrid support | Notes |
|---|---|---|
| **Zurg + rclone** | Real-Debrid, AllDebrid, Debrid-Link | Most popular, well-tested |
| **Decypharr** | Real-Debrid, AllDebrid, Torbox, Premiumize | Newer, all-in-one alternative |

Choose one. **Zurg is recommended** for Real-Debrid users.

---

## Option A — Zurg + rclone

Zurg exposes your debrid library as a WebDAV server. rclone mounts it as a local filesystem.

Full setup guide: [:octicons-arrow-right-24: Zurg + rclone](../integrations/zurg.md){ .md-button }

After setup you will have a folder like `/mnt/zurg` (or `/mnt/user/zurg` on Unraid) containing your debrid files organised as:

```
/mnt/zurg/
  __all__/          ← all files
  movies/           ← Zurg-categorised movies
  shows/            ← Zurg-categorised shows
```

Note the path — you'll need it in the next step.

---

## Option B — Decypharr

Decypharr is an all-in-one debrid mount tool that also handles symlink management and supports multiple debrid providers.

Full setup guide: [:octicons-arrow-right-24: Decypharr](../integrations/decypharr.md){ .md-button }

---

## Verify the mount works

Before proceeding, confirm the mount is working by listing your mount path:

=== "Zurg + rclone"
    ```bash
    ls /mnt/zurg/__all__
    ```

=== "Decypharr"
    ```bash
    ls /path/to/debrid
    ```

You should see your debrid files listed. If the folder is empty or the command fails, fix the mount before continuing.

!!! warning "Mount must be working before installing cli_debrid"
    cli_debrid needs to be able to read the mount path at startup. If the mount isn't working, cli_debrid won't be able to verify files exist.

---

## Next step

[:octicons-arrow-right-24: Step 3 — Install cli_debrid](install.md){ .md-button .md-button--primary }
