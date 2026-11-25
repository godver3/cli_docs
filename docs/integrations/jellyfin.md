---
title: Jellyfin
icon: simple/jellyfin
---

# Jellyfin

Jellyfin is a free, open-source alternative to Plex. CLI_Debrid supports Jellyfin for library management.

!!! tip "Jellyfin is recommended on Windows"
    If you're running CLI_Debrid on Windows with Symlinked/Local mode, use Jellyfin — Plex does not support symlinks on Windows.

---

## Prerequisites

- Jellyfin installed and running
- A working debrid mount ([Zurg + rclone](zurg.md) or [Decypharr](decypharr.md))
- The mount path accessible inside the Jellyfin container

---

## Pick a mode

Jellyfin and Emby work in both file management modes:

- **Symlinked/Local** (the steps below): Clyde builds a symlink folder and Jellyfin scans it. Jellyfin must see the mount and the symlink folder at the same paths as Clyde.
- **Direct Mount** (since 0.8.7): Jellyfin reads the mount itself, like Plex in Direct Mount. See [Direct Mount with Jellyfin or Emby](#direct-mount-with-jellyfin-or-emby) at the end of this page.

## Step 1 — Expose the debrid mount to Jellyfin

In Symlinked/Local mode you mount both the debrid storage and the symlink folder, and the container paths **must match Clyde exactly**.

| Host Path | Container Path |
|---|---|
| Your debrid mount (e.g. `/mnt/remotes/zurg`) | Must match Clyde exactly (e.g. `/media/mount`) |
| Your symlink folder (e.g. `/mnt/symlinks`) | Must match Clyde exactly (e.g. `/mnt/symlinked`) |

!!! warning "Paths must match cli_debrid exactly"
    Symlinks created by Clyde point to files inside the debrid mount using the container path. Jellyfin must mount both volumes at **identical container paths** to Clyde — otherwise symlinks will appear broken.

=== "Docker Compose"
    ```yaml
    services:
      jellyfin:
        image: lscr.io/linuxserver/jellyfin:latest
        container_name: jellyfin
        network_mode: bridge
        ports:
          - "8096:8096/tcp"
          - "7359:7359/udp"
        volumes:
          - /path/to/your/debrid/mount:/media/mount:ro    # e.g. /mnt/cache/zurg, /mnt/data/debrid — must match cli_debrid
          - /path/to/your/symlinks:/mnt/symlinked:ro       # e.g. /mnt/disk1/TVShows — must match cli_debrid
          - /path/to/jellyfin/appdata:/config:rw           # e.g. /mnt/cache/appdata/jellyfin
        environment:
          - TZ=America/New_York
          - PUID=0
          - PGID=0
          - UMASK=022
        restart: unless-stopped
    ```

    !!! warning "Unraid users"
        Use the actual pool path for the mount (e.g. `/mnt/cache/zurg` or `/mnt/downloadcache/zurg`), not `/mnt/user/zurg`. This avoids array startup issues.

=== "Unraid"
    Edit your Jellyfin docker template and add the path mapping above.

=== "Portainer / Dockge / Dockhand"
    Paste the same compose file from the Docker Compose tab into your stack editor and deploy.

    - **Portainer:** Stacks → Add Stack → paste → Deploy
    - **Dockge:** + Compose → paste → Deploy
    - **Dockhand:** Stacks → + Create → paste → Create & Start

=== "Windows"

    Jellyfin has a native Windows installer.

    1. Download from [jellyfin.org/downloads](https://jellyfin.org/downloads/)
    2. Run the installer
    3. Jellyfin will be available at `http://localhost:8096`

Restart Jellyfin after making this change.

---

## Step 2 — Add Debrid libraries in Jellyfin

1. In Jellyfin, go to **Dashboard → Libraries**
2. Click **Add Media Library**
3. For **Content Type**, select **Movies**
4. Name it `Movies-DB`
5. Add folder: `/data/movies`
6. Click **OK**

Repeat for TV Shows:

1. Add another library
2. **Content Type:** Shows
3. Name: `TV Shows-DB`
4. Folder: `/data/shows`

![Jellyfin add library dialog](../assets/screenshots/integrations/jellyfin-add-library.png)

---

## Step 3 — Configure CLI_Debrid for Jellyfin

In CLI_Debrid, go to **Settings → Required Settings**:

| Setting | Value |
|---|---|
| **File Management** | Plex (Jellyfin uses the same setting) |
| **Media Server Type** | Jellyfin |
| **Jellyfin URL** | `http://YOUR_JELLYFIN_IP:8096` |
| **Jellyfin API Key** | See below |
| **Shows Libraries** | `TV Shows-DB` |
| **Movie Libraries** | `Movies-DB` |

### Getting your Jellyfin API key

1. In Jellyfin, go to **Dashboard → API Keys**
2. Click **+** to create a new key
3. Name it `cli_debrid`
4. Copy the generated key

![Jellyfin API key creation](../assets/screenshots/integrations/jellyfin-api-key.png)

---

## Direct Mount with Jellyfin or Emby

Since 0.8.7, Direct Mount can run with Jellyfin or Emby instead of Plex: the server reads the mount, and Clyde asks it what it has.

1. Give Jellyfin the mount (read-only is fine). Its container path doesn't have to match Clyde's: Clyde matches library folders by name.
2. Add a **Movies** library on the mount's `Movies` folder and a **Shows** library on its `TV Shows` folder (the built-in mount and cli_mount create these).
3. In Clyde, set **File Management** to **Direct Mount**, pick **Jellyfin / Emby** as the **Media Server**, and enter the URL and API key.

New downloads are scanned in and collected once Jellyfin lists them; removals drop out. Plex-only features (labels, collections, reported issues, Plex watch history) stay off.

!!! tip "Subtitles on a read-only mount"
    Turn off **Save subtitles into media folders** in each library's settings, so Jellyfin can keep subtitles Clyde uploads in its own data folder. Emby takes no uploads: it gets subtitles as files next to the video, which needs a mount that accepts them (the built-in mount does).

## Troubleshooting

**New content not appearing in Jellyfin**

- Go to **Dashboard → Libraries** → click **Scan All Libraries**
- Or trigger a scan on just the Movies-DB or TV Shows-DB library

**Items showing with wrong metadata**

- In Jellyfin, right-click the item → **Identify** and search manually
