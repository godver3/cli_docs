---
title: Configure cli_debrid
icon: material/cog
---

# Step 4 — Configure cli_debrid

With cli_debrid installed and the onboarding wizard open, work through each section below. You will need the API keys and paths gathered in [Step 1](prerequisites.md) and the mount path from [Step 2](mount.md).

---

## Onboarding wizard

The wizard runs automatically on first launch. If you leave partway through, logging back in takes you to the first step you haven't finished.

| Step | What you do |
|---|---|
| **1. Admin account** | Set your username and password |
| **2. Connect your services** | Four sections: where your media comes from (debrid and/or Usenet), your mount, your library (Plex or Symlink mode) and metadata (TVDB/TMDB). Each connection has a **Test** button, and **Save & Validate** checks everything before you can move on |
| **3. Scrapers** | Debrid users get **Torrentio** added automatically. Usenet users add their indexers as **Newznab** scrapers |
| **3a. Versions** | The **Default** version (1080p) is added for you. Keep it or pick another option |
| **4. Content sources** | Add at least one, e.g. **My Plex Watchlist** |
| **5. Library management** | Optionally scan or convert an existing library |
| **6. Review & start** | A summary of your setup, a health check of every connection, and **Start Program** |

Scrapers and content sources can be edited in the wizard after you add them. You can change everything later under **Settings**.

The sections below explain the fields in step 2 in more detail.

---

## Debrid or Usenet provider

In the wizard's **Where your media comes from** section, tick **Debrid**, **Usenet** or both. cli_debrid needs at least one; you can add the other later under **Settings → Required Settings**.

=== "Debrid"

    | Field | Value |
    |---|---|
    | **Provider** | Select your debrid service |
    | **API Key** | Paste the key from [Step 1](prerequisites.md) |

    **Save & Validate** tests the key.

=== "Usenet"

    | Field | Value |
    |---|---|
    | **Usenet Provider** | **cli_mount** (recommended), **NzbDAV** or **Zurg 2.0** |
    | **URL** | cli_mount: `http://192.168.1.x:8282`. NzbDAV: port `3000`. Zurg 2.0: its own address |
    | **API Token** | cli_mount: only if you turned on authentication, otherwise leave blank. NzbDAV/Zurg: the SABnzbd API key |

    Click **Test connection** to check the URL and token before moving on. If you pick NzbDAV, the wizard also shows the NzbDAV setup helper.

    Use the server's IP or container name, **not** `localhost` — inside the cli_debrid container that points at cli_debrid itself.

    Your news server login lives in cli_mount ([Step 2](mount.md)), not in cli_debrid. To find content you'll also add your indexers as **Newznab** scrapers in [Step 5](scrapers.md).

    After onboarding, **Settings → Required Settings → Usenet Provider** has more options:

    | Setting | Value |
    |---|---|
    | **Download Folder** | Leave empty for cli_mount's default |
    | **Data Path** | `/climount_data` if you mapped cli_mount's appdata into cli_debrid ([Step 3](install.md)) — enables the cli_mount DB tools |

!!! tip "Using both?"
    With debrid and Usenet both configured, torrent and NZB results are scored together using the same quality rules, and the best one wins.

### Recommended: checks before a file is collected

These live under **Settings → Required Settings** and are worth turning on once things work:

| Setting | Where | Recommendation |
|---|---|---|
| **Disable NZB Season Packs** | Usenet Provider | **Keep on** (it's the default). A single missing article in a season pack fails the whole pack, and the repair re-downloads the entire season. With this on, cli_debrid grabs NZBs per episode, so one bad file only affects one episode. Movies aren't affected. |
| **Ffprobe All NZBs** | Usenet Provider | Optional. Before an NZB file is collected, cli_debrid opens it with `ffprobe` to make sure it actually plays, on top of the normal missing-article check. |
| **Ffprobe All Debrid Additions** | Debrid Provider | Optional. The same playability check for debrid files. |

!!! info "What the ffprobe checks cost"
    The ffprobe checks catch files that look complete but won't play — corrupt or truncated files, wrong content, broken archives. A file that fails is rejected and scraped again, and in Plex mode this happens **before** cli_debrid tells Plex about it, so broken files never show up in your library.

    The trade-off is speed: every new file has to be opened and read before it's collected, so additions take noticeably longer, especially for big batches. If additions feel slow, turn these off. A probe that only times out (rather than finding an actual problem) lets the file through.

---

## Your mount

cli_debrid doesn't download or store files itself. A mount tool ([Step 2](mount.md)) shows your debrid and Usenet files as a normal folder, and both cli_debrid and your media server read from it. The wizard's **Your mount** section asks for that folder:

| Field | Value |
|---|---|
| **Mount tool** | The tool you set up. It only picks the example path shown under the field |
| **Mount Path** | The folder as cli_debrid sees it inside its container, e.g. `/mnt/climount/__all__`, `/mnt/zurg/__all__` or `/mnt/decypharr/__all__` |

Click **Check path**. It tells you if the folder doesn't exist, can't be read, is empty, or is the parent of an `__all__` folder (point it at `__all__` itself). An empty folder is only a warning: a new Usenet-only setup stays empty until the first download.

The mount path is required in Symlink mode. In Plex mode it's only needed for **Update Plex on file discovery**.

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

    **Mounted File Location:** Set to your mount path, e.g.:

    - cli_mount: `/path/to/debrid/__all__` (the folder you mapped to `/mnt` in cli_mount)
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

---

## Versions (quality profiles)

A **version** is a quality profile: which resolution you want, how big files can be, which releases to skip, and how results are scored. Every content source is assigned one or more versions, and cli_debrid picks the best result that matches.

You can start with **Add Default Version** under **Settings → Version Settings**, or import a ready-made profile.

### Example: a tuned 1080p version

This is a real, battle-tested 1080p version from a debrid + Usenet setup. Import it and adjust from there:

1. Download [:octicons-download-24: 1080p-example.json](../assets/versions/1080p-example.json){ download }
2. Go to **Settings → Version Settings** and click **Import**
3. Choose the file. If a version with the same name exists, pick **Rename**, **Overwrite** or **Skip**
4. Assign the version to your content sources ([Step 6](content-sources.md))

What it does:

| Setting | Value | Why |
|---|---|---|
| **Max Resolution** / **Resolution Wanted** | `1080p` / `<=` | 1080p, falling back to lower resolutions rather than finding nothing |
| **Min Size** | `0.4` GB | Skips tiny, heavily compressed encodes |
| **Min / Max Bitrate** | `3` / `18` Mbps | Skips low-quality encodes and huge remuxes |
| **Bitrate Weight** | `5` | Strongly prefers higher bitrate (better quality) within those limits |
| **Similarity Threshold** | `0.75` | How closely a release name must match the title |
| **Language Code** / **Foreign Language Penalty** | `en` / `100` | Pushes releases tagged with another audio language (e.g. `GERMAN`) down the list |

Its **Filter Out** list skips:

| Pattern(s) | Skips |
|---|---|
| `й`, `я`, `д`, `г`, `ё`, `ж`, `ф`, `Ц` | Releases with Cyrillic (Russian-titled) names |
| `Telesync`, `HD-TS`, `.TS.`, `HDTS`, `HDTC`, `Telecine`, `.CAM.`, `HDCAM`, `TS` at the end | Cam and telesync rips |
| `.3D.` | 3D releases |
| `READNFO` | Releases flagged *READNFO* — usually a known problem described in the NFO |
| `HINDI`, `bilibili` | Hindi dubs and Bilibili web rips |
| `DoVi` | Dolby Vision releases, which can show wrong colours on players without Dolby Vision support |
| `AV1` | AV1 encodes, which many devices can't direct-play |
| `dem3nt3` | One specific release group — a personal preference, remove it if you like |
| `WEB-DL`, `WEB.x264`/`WEB.H264`, `HDTV.x264`/`HDTV.XviD` *(debrid only, case-sensitive)* | Generic web/TV releases from **debrid only**, so those come from Usenet instead — remove this one if you don't use Usenet |

!!! tip "Filters can target debrid, Usenet or both"
    Each filter has a **source**: **Both**, **Debrid** or **Usenet**. Filters are regular expressions, so `(?i)` makes one case-insensitive and `\b` matches a word boundary.

Full reference for every version setting: [:octicons-arrow-right-24: Versions](../configuration/versions.md){ .md-button }

---

## Metadata (TVDB and TMDB)

cli_debrid looks up shows, seasons, episodes and release dates. The wizard's **Metadata** section asks for both keys from [Step 1](prerequisites.md), each with a **Test key** button:

| Key | Needed? | Used for |
|---|---|---|
| **TVDB API key** | Required, unless you use Trakt instead | Show and movie lookups, episode matching, alternative episode orders |
| **TMDB API key** | Recommended | Posters, digital/physical release dates, Discover |

Use TMDB's short **API Key**, not the long "API Read Access Token". The wizard tells you if you paste the wrong one.

You can change both later under **Settings → Required Settings**.

---

## Trakt (optional)

Trakt is not required to run cli_debrid. Without a TVDB key, cli_debrid looks shows and movies up on Trakt instead, and Trakt is needed for Trakt content sources. In the wizard, open **Use Trakt instead (optional)** under Metadata; after setup it's under **Settings → Additional Settings**. Enter your Trakt **Client ID** and **Client Secret**, then click **Authorize Trakt** to complete the OAuth flow.

---

## Scrob (optional)

If you use [Scrob](https://github.com/ellite/scrob), go to **Settings → Additional Settings → Scrob**:

| Field | Value |
|---|---|
| **URL** | Your Scrob address, e.g. `http://192.168.1.x:7330` |
| **API Key** | From Scrob's **Settings → Connections → API Key** |
| **Username / Password** | Optional — only needed if you want items removed from your Scrob lists/collection when you delete them in cli_debrid (Scrob's API key can't delete). Leave blank to skip. |

Once connected, Scrob lists show up on the **Discover** page and you can add Scrob content sources in [Step 6](content-sources.md).

---

## Verify the connection

**Save & Validate** in step 2 tests your provider, mount, media server and metadata keys. Failed checks have to be fixed before you can continue; warnings (like a missing TMDB key or an empty mount) don't block you. The wizard's last step runs the same checks again, plus a check that each scraper's server answers, before you start the program.

If any connection fails:

- Double-check the URL includes `http://` and the correct port
- Confirm the API key has no extra spaces
- Make sure cli_debrid can reach the service on your network (same Docker network, correct IP)

---

## Next step

[:octicons-arrow-right-24: Step 5 — Add scrapers](scrapers.md){ .md-button .md-button--primary }
