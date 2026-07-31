---
title: Configure cli_debrid
icon: material/cog
---

# Step 4 — Configure cli_debrid

With cli_debrid installed and the onboarding wizard open, work through each section below. You will need the API keys and paths gathered in [Step 1](prerequisites.md) and the mount path from [Step 2](mount.md).

---

## Onboarding wizard

The wizard runs automatically on first launch. It covers:

1. **Admin account** — set your username and password
2. **Required settings** — debrid provider, media server, mount path
3. **File management mode** — Plex mode or Symlink mode
4. **Scrapers** — add at least one scraper
5. **Content sources** — add at least one content source

You can re-visit any of these at any time under **Settings**.

---

## Debrid provider

Enter your debrid provider and API key.

| Field | Value |
|---|---|
| **Provider** | Select your debrid service |
| **API Key** | Paste the key from [Step 1](prerequisites.md) |

Click **Validate** to test the key before saving.

---

## Media server

=== "Plex"

    | Field | Value |
    |---|---|
    | **Plex URL** | `http://YOUR_PLEX_IP:32400` |
    | **Plex Token** | Your Plex auth token (see below) |
    | **Movies libraries** | Comma-separated list of your movie library names or IDs, e.g. `Movies,4K Movies` or `1,3` |
    | **Shows libraries** | Comma-separated list of your TV library names or IDs, e.g. `TV Shows,Anime` or `2,4` |

    !!! tip "Using library IDs"
        You can use either the library name or its numeric ID. To find the ID, open your Plex library in the browser — the `source=` value at the end of the URL is the library ID. For example, `source=1` means the library ID is `1`.

    ### Finding your Plex token

    1. Open Plex Web and browse to any item
    2. Click the **...** menu → **Get Info** → **View XML**
    3. In the URL, copy the value after `X-Plex-Token=`

    Full guide: [:octicons-arrow-right-24: Plex integration](../integrations/plex.md){ .md-button }

=== "Jellyfin"

    | Field | Value |
    |---|---|
    | **Jellyfin URL** | `http://YOUR_JELLYFIN_IP:8096` |
    | **API Key** | Create one under Jellyfin → Dashboard → API Keys |
    | **Movies libraries** | Comma-separated library names |
    | **Shows libraries** | Comma-separated library names |

    Full guide: [:octicons-arrow-right-24: Jellyfin integration](../integrations/jellyfin.md){ .md-button }

---

## File management mode

This is one of the most important settings.

=== "Plex mode"

    cli_debrid uses the Plex API to track which files are in your library. Plex reads directly from your debrid mount.

    - Plex only — does not work with Jellyfin or Emby
    - No symlinks needed
    - Plex must be able to read the mount path

    **Mounted File Location:** Set to your debrid mount path, e.g.:

    - Zurg: `/mnt/zurg/__all__`
    - Decypharr: `/mnt/decypharr/__all__`

=== "Symlink mode"

    cli_debrid creates symlinks from the mount into an organised folder structure. Your media server scans the symlink folder.

    - Works with Plex, Jellyfin, and Emby
    - Required for Jellyfin and Emby
    - Required on Windows (use Jellyfin — Plex doesn't support symlinks on Windows)

    | Field | Value |
    |---|---|
    | **Original files path** | Your debrid mount path (e.g. `/mnt/zurg/__all__` for Zurg, `/mnt/decypharr/__all__` for Decypharr) |
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

---

## TMDB API key

Go to **Settings → Required Settings** (or the wizard step) and enter your TMDB API key from [Step 1](prerequisites.md).

---

## TVDB API key

Enter your TVDB API key. Used for TV show episode matching.

---

## Trakt (optional)

Trakt is not required to run cli_debrid. If you want to use it as a content source or as a metadata fallback (when no TVDB key is set), go to **Settings → Additional Settings**, enter your Trakt **Client ID** and **Client Secret**, then click **Authorise Trakt** to complete the OAuth flow.

---

## Verify the connection

After saving, cli_debrid will test the connections to your debrid provider and media server. You should see green checkmarks next to each service on the dashboard.

If any connection fails:

- Double-check the URL includes `http://` and the correct port
- Confirm the API key has no extra spaces
- Make sure cli_debrid can reach the service on your network (same Docker network, correct IP)

---

## Next step

[:octicons-arrow-right-24: Step 5 — Add scrapers](scrapers.md){ .md-button .md-button--primary }
