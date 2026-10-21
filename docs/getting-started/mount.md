---
title: Mount your storage
icon: material/harddisk
---

# Step 2 — Mount your storage

Before cli_debrid can manage your library, your debrid and/or Usenet content needs to be mounted as a local folder. Your media server (Plex/Jellyfin) reads from this folder as if it were a regular hard drive — nothing is downloaded to your server.

Three tools handle this:

| Tool | Debrid | Usenet | Notes |
|---|---|---|---|
| **cli_mount** | Real-Debrid, AllDebrid, Torbox, Premiumize | ✓ | **Recommended.** All-in-one, built alongside cli_debrid |
| **Decypharr** | Real-Debrid, AllDebrid, Torbox, Premiumize | | The original project cli_mount is forked from |
| **Zurg + rclone** | Real-Debrid, AllDebrid, Debrid-Link | ✓ (Zurg 2.0) | Long-standing, well-tested Real-Debrid setup |

Choose one. **cli_mount is recommended** — it handles debrid and Usenet in a single container and works directly with cli_debrid for imports and repairs. If you only use Real-Debrid and already run Zurg, that works too.

---

## Option A — cli_mount (recommended)

cli_mount mounts your debrid library and streams Usenet NZBs from your news server, all in one container. It's a fork of [Decypharr](https://github.com/sirrobot01/decypharr) maintained by mash2k3 ([source](https://github.com/mash2k3/decypharr/tree/dev)).

Full setup guide: [:octicons-arrow-right-24: cli_mount](../integrations/cli_mount.md){ .md-button }

In short:

1. Run the `ghcr.io/mash2k3/cli_mount:dev` container (needs `/dev/fuse`), with your mount folder mapped to `/mnt`
2. Open the cli_mount web UI at `http://YOUR_SERVER_IP:8282`
3. **Debrid:** under **Settings → Providers → Debrid**, click **Add Account** and enter your debrid provider and API key
4. **Usenet:** under **Settings → Providers → Usenet**, click **Add Server** and enter your provider's host, port (`563` with SSL), username, password and max connections

After setup you will have a mount folder (e.g. `/path/to/debrid`) containing your debrid and Usenet files.

Note the path and the cli_mount URL (`http://YOUR_SERVER_IP:8282`) — you'll need both in [Step 4](configure.md).

---

## Option B — Decypharr

Decypharr is an all-in-one debrid mount tool that also handles symlink management and supports multiple debrid providers.

Full setup guide: [:octicons-arrow-right-24: Decypharr](../integrations/decypharr.md){ .md-button }

---

## Option C — Zurg + rclone

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

## Verify the mount works

Before proceeding, confirm the mount is working by listing your mount path:

=== "cli_mount"
    ```bash
    ls /path/to/debrid
    ```

=== "Decypharr"
    ```bash
    ls /path/to/debrid
    ```

=== "Zurg + rclone"
    ```bash
    ls /mnt/zurg/__all__
    ```

You should see your files listed (a new Usenet-only setup will be empty until the first NZB is added). If the command fails or the command fails, fix the mount before continuing.

!!! warning "Mount must be working before installing cli_debrid"
    cli_debrid needs to be able to read the mount path at startup. If the mount isn't working, cli_debrid won't be able to verify files exist.

---

## Next step

[:octicons-arrow-right-24: Step 3 — Install cli_debrid](install.md){ .md-button .md-button--primary }
