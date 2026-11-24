---
title: Configure Clyde
icon: material/cog
---

# Step 4 — Configure Clyde

With Clyde installed and the onboarding wizard open, work through each section below. You will need the API keys and paths gathered in [Step 1](prerequisites.md) and the mount path from [Step 2](mount.md).

---

## Onboarding wizard

The wizard runs automatically on first launch. If you leave partway through, logging back in takes you to the first step you haven't finished.

| Step | What you do |
|---|---|
| **1. Admin account** | Set your username and password |
| **2. Connect your services** | Four sections: where your media comes from (debrid and/or Usenet), your mount, your library (Plex or Symlink mode) and metadata (TVDB/TMDB). Each connection has a **Test** button, and **Save & Validate** checks everything before you can move on |
| **3. Scrapers** | Debrid users get **Torrentio** added automatically. Usenet users add their indexers as **Newznab** scrapers |
| **3a. Versions** | The **Default** version (1080p) is added for you. Keep it, or switch to **Separate 1080p/4K Versions** or **Alternate Default Versions** |
| **4. Content sources** | Add at least one, e.g. **My Plex Watchlist** |
| **5. Library management** | Optionally scan or convert an existing library |
| **5a. Subtitles** (optional) | How Clyde handles subtitles, and whether it should. Choose **Yes** to set your languages, your OpenSubtitles.com login and optional SubDL/SubSource API keys, each with a **Test** button. Choose **No**, or just move on, to skip. See [Subtitles](../configuration/subtitles.md). |
| **6. Review & start** | A summary of your setup (including whether subtitles are on), a health check of every connection (including whether your media server sees the mount and symlink folder at the same paths), optional **Simple** poster overlays, then **Start Program & Go to Dashboard** (or **Finish Setup** to look around before starting) |

Scrapers and content sources can be edited in the wizard after you add them. You can change everything later under **Settings**.

The sections below explain the fields in step 2 in more detail.

---

## Debrid or Usenet provider

In the wizard's **Where your media comes from** section, tick **Debrid**, **Usenet** or both. Clyde needs at least one; you can add the other later under **Settings → Required Settings**.

=== "Debrid"

    | Field | Value |
    |---|---|
    | **Provider** | Select your debrid service |
    | **API Key** | Paste the key from [Step 1](prerequisites.md) |

    **Save & Validate** tests the key.

=== "Usenet"

    | Field | Value |
    |---|---|
    | **Usenet Mount** | **Built-in mount** (default), **cli_mount**, **NzbDAV** or **Zurg 2.0** |

    **Built-in mount:** the wizard asks for your news server instead of a URL:

    | Field | Value |
    |---|---|
    | **Usenet server** | Your provider's news server, e.g. `news.example.com` (not your indexer) |
    | **Port / SSL** | Usually `563` with SSL on |
    | **Connections** | What your plan allows; leave a few free if you also download elsewhere |
    | **Username / Password** | Your news server login |

    **Save & Validate** starts the mount and checks the login. Add more servers (backup or block accounts) later on the **Mount** page. See [Built-in mount](../integrations/builtin-mount.md).

    **cli_mount, NzbDAV or Zurg 2.0:**

    | Field | Value |
    |---|---|
    | **Mount URL** | cli_mount: `http://192.168.1.x:8282`, or `http://cli_mount:8282` in the [one-stack compose](../installation/docker.md#recommended-cli_debrid-and-cli_mount-in-one-stack). NzbDAV: port `3000`. Zurg 2.0: its own address. **Detect** looks for it and fills the field in when it finds exactly one |
    | **API Token (optional)** / **SABnzbd API Key** | cli_mount: only if you turned on authentication, otherwise leave blank. NzbDAV/Zurg: the SABnzbd API key |

    Click **Test connection** to check the URL and token before moving on. If you pick NzbDAV, the wizard also shows the NzbDAV setup helper.

    Use the server's IP or container name, **not** `localhost` — inside the Clyde container that points at Clyde itself.

    With these, your news server login lives in the mount app ([Step 2](mount.md)), not in Clyde. To find content you'll also add your indexers as **Newznab** scrapers in [Step 5](scrapers.md).

    After onboarding, **Settings → Required Settings → Usenet Mount** has more options:

    | Setting | Value |
    |---|---|
    | **Download Folder / Category** | Leave empty for cli_mount's default |
    | **cli_mount Data Path** | `/climount_data` if you mapped cli_mount's appdata into Clyde ([Step 3](install.md)). Enables the cli_mount DB tools. **Detect** (under **Provider**) fills it in |

!!! tip "Using both?"
    With debrid and Usenet both configured, torrent and NZB results are scored together using the same quality rules, and the best one wins.

### Recommended: checks before a file is collected

These live under **Settings → Required Settings** and are worth turning on once things work:

| Setting | Where | Recommendation |
|---|---|---|
| **Disable NZB Season Packs** | Usenet Mount | **Keep on** (it's the default). A single missing article in a season pack fails the whole pack, and the repair re-downloads the entire season. With this on, Clyde grabs NZBs per episode, so one bad file only affects one episode. Movies aren't affected. |
| **Ffprobe All NZBs** | Usenet Mount | Optional. Before an NZB file is collected, Clyde opens it with `ffprobe` to make sure it actually plays, on top of the normal missing-article check. |
| **Ffprobe All Debrid Additions** | Debrid Provider | Optional. The same playability check for debrid files. |

!!! info "What the ffprobe checks cost"
    The ffprobe checks catch files that look complete but won't play — corrupt or truncated files, wrong content, broken archives. A file that fails is rejected and scraped again, and in Direct Mount this happens **before** Clyde tells Plex about it, so broken files never show up in your library.

    The trade-off is speed: every new file has to be opened and read before it's collected, so additions take noticeably longer, especially for big batches. If additions feel slow, turn these off. A probe that only times out (rather than finding an actual problem) lets the file through.

---

## Your mount

Clyde doesn't download or store files itself. A mount tool ([Step 2](mount.md)) shows your debrid and Usenet files as a normal folder, and both Clyde and your media server read from it. The wizard's **Your mount** section asks for that folder:

| Field | Value |
|---|---|
| **Mount tool** | The tool you set up. It picks the example path shown under the field. **Built-in mount** (the default when the container can run it) also fills in its path, `/mnt/clid/__all__`, and runs the mount for debrid even without Usenet |
| **Mount Path** | The folder as Clyde sees it inside its container, e.g. `/mnt/clid/__all__`, `/mnt/cli_mount/__all__`, `/mnt/zurg/__all__` or `/mnt/decypharr/__all__` |

Click **Check path**. It tells you if the folder doesn't exist, can't be read, is empty, or is the parent of an `__all__` folder (point it at `__all__` itself). An empty folder is only a warning: a new Usenet-only setup stays empty until the first download.

The mount path is required in Symlink mode. In Direct Mount it's only needed for **Update Plex on file discovery**.

---

## Your library

The wizard's **Your library** section picks how Clyde gets files into your media server. **File Collection Management** is one of the most important settings, and it decides which fields show up below it.

=== "Direct Mount"

    Your media server reads straight from your mount, and Clyde uses its API to track what's in your library. Called **Plex mode** before 0.8.7.

    - **Media Server:** Plex, Silo or Jellyfin / Emby. For Silo or Jellyfin / Emby, enter its URL and API key instead of the Plex fields below
    - No symlinks
    - The media server must see the mount. Jellyfin, Emby and Silo may see it at another path: Clyde matches their library folders by name

    Click **Sign in to Plex** to fill the fields in, or enter them yourself (sign-in can fail when Plex can't work out your network; the direct IP and token always work):

    | Field | Value |
    |---|---|
    | **Plex URL** | `http://YOUR_PLEX_IP:32400`, without a trailing slash |
    | **Plex Token** | Your Plex auth token (see below) |
    | **Movie Libraries** | Comma-separated movie library names or IDs, e.g. `Movies,4K Movies` or `1,3` |
    | **TV Libraries** | Comma-separated TV library names or IDs, e.g. `TV Shows,Anime` or `2,4` |
    | **Update Plex on file discovery** | Optional. Tells Plex to scan a file as soon as Clyde finds it on the mount. Needs the mount path from [Your mount](#your-mount) |

    !!! tip "Using library IDs"
        You can use either the library name or its numeric ID. To find the ID, open your Plex library in the browser — the `source=` value at the end of the URL is the library ID. For example, `source=1` means the library ID is `1`.

    ### Finding your Plex token

    1. Open Plex Web and browse to any item
    2. Click the **...** menu → **Get Info** → **View XML**
    3. In the URL, copy the value after `X-Plex-Token=`

    Full guide: [:octicons-arrow-right-24: Plex integration](../integrations/plex.md){ .md-button }

=== "Symlink mode"

    Clyde makes a tidy folder of symlinks pointing into your mount, and your media server scans that folder. In the wizard this is **Symlinked/Local**.

    - Works with Plex, Jellyfin and Emby
    - On Windows it's off unless you tick **Allow Symlinks on Windows** (needs Admin or Developer Mode). Without it, use Direct Mount

    | Field | Value |
    |---|---|
    | **Symlinked Files Path** | Where the symlinks go, e.g. `/mnt/symlinks`. Clyde creates `Movies` and `TV Shows` folders inside it; point your media server's libraries at those |
    | **Media Server** | Optional: **None**, **Plex** or **Jellyfin / Emby**. Lets Clyde start a library scan when new files are added |
    | **Plex URL** / **Plex Token** | Shown when you pick Plex |
    | **Jellyfin / Emby URL** / **Jellyfin / Emby API Token** | Shown when you pick Jellyfin / Emby, e.g. `http://YOUR_JELLYFIN_IP:8096`. Create the key under Jellyfin → Dashboard → API Keys |

    !!! warning "Volume mounts must match exactly"
        Each symlink points at a file inside the mount. For it to resolve, **cli_debrid and your media server must see the mount and the symlink folder at identical paths**.

        For example, if Clyde has:
        ```
        /mnt/remotes/zurg  →  /media/mount   (debrid mount)
        /mnt/symlinks      →  /mnt/symlinked  (symlink folder)
        ```
        Then Plex/Jellyfin/Emby must have the exact same mappings:
        ```
        /mnt/remotes/zurg  →  /media/mount   (debrid mount)
        /mnt/symlinks      →  /mnt/symlinked  (symlink folder)
        ```
        If the paths differ between containers, symlinks will appear as broken files in your media server. The [one-stack compose](../installation/docker.md#recommended-cli_debrid-and-cli_mount-in-one-stack) avoids this by using the same path on the host and in every container.

    Full guide: [:octicons-arrow-right-24: Jellyfin integration](../integrations/jellyfin.md){ .md-button }

---

## Versions (quality profiles)

A **version** is a quality profile: which resolution you want, how big files can be, which releases to skip, and how results are scored. Every content source is assigned one or more versions, and Clyde picks the best result that matches.

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

Clyde looks up shows, seasons, episodes and release dates. The wizard's **Metadata** section asks for both keys from [Step 1](prerequisites.md), each with a **Test key** button:

| Key | Needed? | Used for |
|---|---|---|
| **TVDB API key** | Required, unless you use Trakt instead | Show and movie lookups, episode matching, alternative episode orders |
| **TMDB API key** | Recommended | Posters, digital/physical release dates, Discover |

Use TMDB's short **API Key**, not the long "API Read Access Token". The wizard tells you if you paste the wrong one.

You can change both later under **Settings → Required Settings**.

---

## Trakt (optional)

Trakt is not required to run Clyde. Without a TVDB key, Clyde looks shows and movies up on Trakt instead, and Trakt is needed for Trakt content sources. In the wizard, open **Use Trakt instead (optional)** under Metadata; after setup it's under **Settings → Tracking accounts**. Enter your Trakt **Client ID**, and the **Client Secret** if your Trakt app has one (new Trakt apps don't), then click **Authorize Trakt** and enter the code it shows on Trakt's site.

---

## Scrob (optional)

If you use [Scrob](https://github.com/ellite/scrob), go to **Settings → Tracking accounts → Scrob**:

| Field | Value |
|---|---|
| **URL** | Your Scrob address, e.g. `http://192.168.1.x:7330` |
| **API Key** | From Scrob's **Settings → Connections → API Key** |
| **Username / Password** | Optional — only needed if you want items removed from your Scrob lists/collection when you delete them in Clyde (Scrob's API key can't delete). Leave blank to skip. |

Once connected, Scrob lists show up on the **Discover** page and you can add Scrob content sources in [Step 6](content-sources.md).

---

## Verify the connection

**Save & Validate** in step 2 tests your provider, mount, media server and metadata keys. Failed checks have to be fixed before you can continue; warnings (like a missing TMDB key or an empty mount) don't block you. The wizard's last step runs the same checks again, plus a check that each scraper's server answers, before you start the program.

If any connection fails:

- Double-check the URL includes `http://` and the correct port
- Confirm the API key has no extra spaces
- Make sure Clyde can reach the service on your network (same Docker network, correct IP)

---

## Next step

[:octicons-arrow-right-24: Step 5 — Add scrapers](scrapers.md){ .md-button .md-button--primary }
