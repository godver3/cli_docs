---
title: Required Settings
icon: material/alert-circle
---

# Required Settings

These settings must be configured for cli_debrid to function. They are collected during onboarding and can be updated at any time from **Settings → Required Settings**.

![Required settings tab](../assets/screenshots/configuration/required-settings.png)

---

## Debrid Provider

| Setting | Description |
|---|---|
| **Provider** | Your debrid service: Real-Debrid, AllDebrid, Premiumize, Torbox, or Debrid-Link |
| **API Key** | Your debrid API key — found in your account dashboard |

!!! tip "Getting your API key"
    === "Real-Debrid"
        Go to [real-debrid.com/apitoken](https://real-debrid.com/apitoken) while logged in.

    === "AllDebrid"
        Go to [alldebrid.com/apikeys](https://alldebrid.com/apikeys) while logged in.

    === "Premiumize"
        Go to [premiumize.me/account](https://www.premiumize.me/account) and look for **API Key**.

    === "Torbox"
        Go to [torbox.app/settings](https://torbox.app/settings) while logged in.

    === "Debrid-Link"
        Go to [debrid-link.com/webapp/apikey](https://debrid-link.com/webapp/apikey) while logged in.

### Fallback Providers

You can configure additional fallback debrid providers. When the primary provider fails — due to rate limits, DMCA blocks, or errors — cli_debrid automatically tries the next provider in order.

Click **Add Fallback Provider** in the Debrid Provider section to add a fallback. Each fallback has its own provider selection and API key. Fallbacks are tried in the order they are listed.

### More debrid options

| Setting | Description |
|---|---|
| **Ffprobe All Debrid Additions** | Before collecting a debrid file, open it with `ffprobe` to confirm it plays, on top of the normal checks. Catches broken files before they reach your library (in Plex mode, before Plex is told about them), but makes every addition slower. |
| **Enable Debrid Naming** | *cli_mount only.* Rename debrid entries in cli_mount's DFS mount to `{title} ({year}) - {imdb-id} - {version} - (original)` for movies and `{title} ({year}) - SxxExx - {episode title} - {imdb-id} - {version} - (original)` for episodes. Only the entry in cli_mount is renamed. Needs cli_mount configured as the Usenet provider (URL set). |
| ↳ **Include Version In Debrid Naming** | Add the version to the name. On by default. |
| ↳ **Include Content Source In Debrid Naming** | Add the content source's display name. Off by default. |

---

## Plex / Jellyfin

=== "Plex"

    | Setting | Description |
    |---|---|
    | **Plex URL** | Full URL to your Plex server, e.g. `http://192.168.1.10:32400` |
    | **Plex Token** | Your Plex authentication token |
    | **Shows Libraries** | Comma-separated list of your TV library names or IDs, e.g. `TV Shows,Anime` or `2,4` |
    | **Movie Libraries** | Comma-separated list of your movie library names or IDs, e.g. `Movies,4K Movies` or `1,3` |

    !!! tip "Using library IDs"
        You can use either the library name or its numeric ID. To find the ID, open your Plex library in the browser — the `source=` value at the end of the URL is the library ID. For example, `source=1` means the library ID is `1`.

    | Setting | Description |
    |---|---|
    | **Update Plex On File Discovery** | Tell Plex to scan as soon as a file is found on the mount. cli_debrid must be able to read the mount at the **Mounted File Location**. |
    | **Disable Plex Library Checks** | A "local only" mode for third-party symlinking: cli_debrid confirms files using the **Mounted File Location** instead of asking Plex. With no location set, items are marked Collected as soon as they're added. |

    ### Finding your Plex token

    1. Open [Plex Web](https://app.plex.tv) and browse to any media item
    2. Click the **...** menu → **Get Info** → **View XML**
    3. In the URL bar, copy the value after `X-Plex-Token=`

    Full guide: [:octicons-arrow-right-24: Plex integration](../integrations/plex.md){ .md-button }


=== "Jellyfin / Emby"

    !!! warning "Symlink mode required"
        Jellyfin and Emby do not support the Plex API. You must use **Symlinked/Local** file management mode. See [File Management](#file-management) below.

    | Setting | Description |
    |---|---|
    | **Jellyfin/Emby URL** | Full URL to your Jellyfin/Emby server, e.g. `http://192.168.1.10:8096` |
    | **Jellyfin/Emby Token** | Your Jellyfin/Emby API token |
    | **Shows Libraries** | Comma-separated list of your TV library names |
    | **Movie Libraries** | Comma-separated list of your movie library names |

    ### Getting your Jellyfin API key

    1. In Jellyfin, go to **Dashboard → API Keys**
    2. Click **+** to create a new key
    3. Name it `cli_debrid` and copy the generated key

    Full guide: [:octicons-arrow-right-24: Jellyfin integration](../integrations/jellyfin.md){ .md-button }

---

## File Management

This is one of the most important settings.

=== "Plex mode"

    cli_debrid uses the Plex API to track which files are in your library. Plex reads directly from your debrid mount.

    - Plex only — does not work with Jellyfin or Emby
    - No symlinks needed
    - Plex must be able to read the mount path

    **Mounted File Location:** Set to your mount path, e.g.:

    - cli_mount: `/path/to/debrid/__all__`
    - Zurg: `/mnt/zurg/__all__`
    - Decypharr: `/mnt/decypharr/__all__`

=== "Symlink mode"

    cli_debrid creates symlinks from the mount into an organised folder structure. Your media server scans the symlink folder.

    - Works with Plex, Jellyfin, and Emby
    - Required for Jellyfin and Emby
    - Required on Windows (use Jellyfin — Plex doesn't support symlinks on Windows)

    | Field | Value |
    |---|---|
    | **Original files path** | Your mount path (e.g. `/path/to/debrid/__all__` for cli_mount, `/mnt/zurg/__all__` for Zurg, `/mnt/decypharr/__all__` for Decypharr) |
    | **Symlinked files path** | Where organised symlinks go, e.g. `/mnt/symlinks` |

    !!! warning "Volume mounts must match exactly"
        In symlink mode, cli_debrid creates symlinks that point to files inside the debrid mount. For these symlinks to resolve correctly, **both cli_debrid and your media server containers must mount the debrid storage and symlink folder at identical paths**.

        For example, if cli_debrid has:
        ```
        /mnt/remotes/zurg  →  /media/mount   (debrid mount)
        /mnt/symlinks      →  /mnt/symlinked  (symlink folder)
        ```
        Then Plex/Jellyfin/Emby must have the exact same mappings:
        ```
        /mnt/remotes/zurg  →  /media/mount   (debrid mount)
        /mnt/symlinks      →  /mnt/symlinked  (symlink folder)
        ```
        If the paths differ between containers, symlinks will appear as broken files in your media server.

!!! warning "Symlinked/Local mode on Windows"
    Windows requires Developer Mode enabled for symlinks. Plex does NOT support symlinks on Windows — use Jellyfin instead.

### More file management options

| Setting | Description |
|---|---|
| **File Collection Management** | `Plex` or `Symlinked/Local` — the mode chosen above. On Windows, Symlinked/Local uses hardlinks instead of symlinks. |
| **Symlink Organize By Type** | Put symlinks in separate Movies and TV Shows folders. On by default. |
| **Symlink Organize By Resolution** | Add a resolution folder (e.g. `1080p`, `2160p`) before the type folders. |
| **Symlink Organize By Version** | Add a version folder (e.g. `Remux`, `WEB-DL`) before the type folders. |
| **Media Server Type** | `plex` or `jellyfin` — which server to notify about new symlinks. |
| **Plex URL For Symlink** / **Plex Token For Symlink** | The Plex server to scan after creating symlinks (symlink mode). |
| **Scan Mount For External Adds** | Regularly scan the original files path for content added *outside* cli_debrid (e.g. via DMM or your debrid provider's website) and import it — symlink it and trigger a scan. Use this if your mount has no library-update hook (cli_mount, Decypharr, plain rclone); Zurg users get this through Zurg's `on_library_update`. The first run only records what's already there, without importing it. |
| **Process Non Checking Items** | Also process files reported by the rclone webhook that don't match an item cli_debrid is currently checking. |

---

## Usenet Provider

Optional. Needed to download NZBs found by [Newznab scrapers](../scrapers/newznab.md). Works alongside a debrid provider, or on its own (leave the debrid API key empty for a Usenet-only setup).

| Setting | Description |
|---|---|
| **Enable Usenet** | Turn on Usenet support |
| **Provider** | `cli_mount` (recommended), `NzbDAV`, or `Zurg` (Zurg 2.0's SABnzbd-compatible endpoint) |
| **Provider URL** | e.g. `http://192.168.1.x:8282` for cli_mount or `:3000` for NzbDAV. Use the host IP or container name — **not** `localhost`, which inside the cli_debrid container points at cli_debrid itself. |
| **API Token** | Only if your provider has authentication enabled |
| **Download Folder / Category** | Leave empty for the provider's default |
| **cli_mount Data Path** | cli_mount's appdata folder as seen *inside the cli_debrid container* — needed for the cli_mount DB backup, restore and cleanup tools. Add `- /path/to/appdata/cli_mount:/climount_data` to your cli_debrid volumes and set this to `/climount_data`. |
| **Usenet Retention Days** | Ignore NZB results older than this many days. Default `5000`; `0` turns it off. |
| **Disable NZB Season Packs** | **On by default — recommended.** Skips NZB season packs (movies aren't affected). One missing article in a season pack fails the whole pack and the repair re-downloads the entire season; per-episode NZBs keep a bad file to one episode. |
| **Ffprobe All NZBs** | Before collecting an NZB file, open it with `ffprobe` to confirm it plays, on top of the missing-article health check. Catches broken files before they reach your library (in Plex mode, before Plex is told about them), but makes every addition slower. Requires `ffprobe` (included in the Docker image). |
| **Enable NZB File Naming** | Name NZB jobs as `{title} ({year}) - {imdb-id} - {version} - (original)` for movies and `{title} ({year}) - SxxExx - {episode title} - {imdb-id} - {version} - (original)` for episodes, instead of the raw release name. |
| ↳ **Include Version in NZB Name** | Add the version (e.g. `Default`, `4K Remux`) to the name. On by default. |
| ↳ **Include Content Source in NZB Name** | Add the content source's display name. Off by default. |

**NzbDAV / Zurg only**

| Setting | Description |
|---|---|
| **Repair: Owned Categories** | Comma-separated NzbDAV categories cli_debrid's repair tool may touch. NzbDAV's history is shared with other apps (e.g. Lidarr), so repair must never act on their entries. Leave empty to use the categories cli_debrid itself grabs into. |
| **Repair: Exclude Categories** | Categories the repair tool must always ignore — e.g. ones Radarr/Sonarr use on the same NzbDAV. |
| `nzbdav_category_map` | *(config file only)* Which categories to use and what they're called on your instance, as `bucket=name` pairs, e.g. `movies=movies, shows=shows, fallback=__unplayable__`. Omitted buckets fall back to their parent category. |

See [cli_mount](../integrations/cli_mount.md#usenet-with-cli_mount) and [Getting Started](../getting-started/configure.md#debrid-or-usenet-provider) for the full setup. Switching between cli_mount and NzbDAV? See [Usenet Migration](../features/usenet-migration.md).

!!! info "Trakt is optional"
    Trakt used to be listed here as a required setting. It is now an **optional** integration — cli_debrid no longer requires Trakt authorization to start or run the queue. See [Additional Settings → Trakt](additional.md#trakt) to configure it.
