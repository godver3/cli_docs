---
title: Subtitles
icon: material/subtitles
---

# Subtitles

cli_debrid can download subtitles for everything it collects, in both file management modes, so you don't need Bazarr. Turn it on during [onboarding](../getting-started/configure.md#onboarding-wizard) (the optional **Subtitles** step) or under **Settings → Subtitles**, and manage it from **Tools → Subtitle Manager**.

---

## How it works

When an item is collected, cli_debrid searches every selected provider for each language you want and picks, best first:

1. **A subtitle made for your exact file.** OpenSubtitles matches by file hash, so the timing is right.
2. **One for the same release group** (and source).
3. **One from the same master:** a Blu-ray rip of the same title, or a WEB release from the same streaming service.
4. Otherwise the best match on title, season and episode, then the closest release name, then the most downloaded.

A subtitle for a different episode or movie is never used. cli_debrid uses the IDs and episode numbers from its database, so obfuscated file names (`tGcr.mkv`) don't confuse it.

Where the subtitle goes:

| Mode | Saved as |
|---|---|
| **Symlinked/Local** | A file next to the library file, e.g. `Movie (2020).en.srt`. Plex, Jellyfin and Emby all pick it up. |
| **Direct Mount** | Uploaded to the Plex item (the mount is read-only), so it shows in the Plex subtitle menu. |

With **Probe for Embedded Subtitles** on, a language the file already has as a good embedded text track (not forced, not commentary) is skipped. The Subtitle Manager also shows such languages as present, unless **Ignore Embedded Subtitles** is on.

---

## Subtitle Settings

| Setting | Default | Description |
|---|---|---|
| **Enable Subtitle Downloads** | Off | Download subtitles when an item is collected |
| **OpenSubtitles Username / Password** | — | Your free [OpenSubtitles.com](https://www.opensubtitles.com/en/users/sign_up) account. Searching works without one, but **downloading needs it**. A free account can download about 20 subtitles a day. |
| **Subtitle Languages** | `eng,zho` | The languages you want. Pick them from the list. |
| **Subtitle Providers** | OpenSubtitles.com, Podnapisi, Gestdown, TVsubtitles | Every selected provider is searched. See [Providers](#providers). |
| **SubDL API Key** | — | Free key from [subdl.com](https://subdl.com) → account → API. Add **subdl** to the providers to use it. |
| **SubSource API Key** | — | Free key from [subsource.net](https://subsource.net) → profile → API. Add **subsource** to the providers to use it. |
| **Avoid Transcoding Formats** | Off | Styled ASS/SSA and image (PGS/VobSub) subtitles make most clients transcode. On: downloaded ASS/SSA is converted to plain SRT, and an embedded image or styled track doesn't count as having that language. |
| **Ignore Embedded Subtitles** | Off | Always download a separate subtitle, even when the file has a good embedded track in that language |
| **Probe for Embedded Subtitles** | Off | Skip languages the file already has embedded. Reuses the add-time ffprobe check when that's on. In Direct Mount it uses Plex's own track list. |

### Providers

| Provider | Account | Notes |
|---|---|---|
| **opensubtitlescom** | Free login, needed to download | The largest catalog, and the only one with file-hash matches |
| **subdl** | Free API key | Large catalog, strong for TV |
| **subsource** | Free API key | Large catalog |
| **podnapisi** | None | |
| **gestdown** | None | Addic7ed mirror, TV only |
| **tvsubtitles** | None | TV only |
| **subtitulamos** | None | Spanish |
| **bsplayer** | None | |
| **opensubtitles** | Login | The legacy OpenSubtitles.org API |

When a provider runs out of downloads or its login fails, it's paused (6 hours for the daily limit, 1 hour for a bad login, 15 minutes for a rate limit) and the others carry on. The Subtitle Manager shows which ones are paused.

---

## Subtitle Manager

**Tools → Subtitle Manager** shows every collected movie and episode with the languages it has, grouped by show and season.

| Action | What it does |
|---|---|
| **Search** (per row, season or show) | Search the providers for the missing languages and save the best match |
| **Search all missing** | The same for everything matching the search box and filters. Use it after turning subtitles on for an existing library. |
| **Fix existing subtitles** | For each subtitle you already have: replace it with one made for this release (file hash, same release group, or same Blu-ray/WEB source) when a provider has one, else keep it. Only the file's 64 KB hash is read. |
| **Search providers** (item details) | List every candidate with its score and why it matched, and pick one by hand. **Auto-pick best** takes the top one. |
| **Delete** (item details) | Remove a subtitle: a sidecar file, or a subtitle uploaded to Plex. Embedded tracks inside the video are never touched. |
| **History** tab | What was downloaded, from which provider, with which score |

### Remove orphaned subtitles

Symlinked/Local only. When a file is replaced, upgraded or repaired, its old subtitle files can stay in the folder. Plex may still offer them for that movie or episode, and sometimes picks one. **Remove orphaned subtitles** scans your library for subtitle files named after a video that's no longer in their folder, shows how many there are with examples, and deletes them permanently once you type `DELETE`.

!!! danger "Permanent"
    Deleted files can't be recovered. Only separate subtitle files are removed. Subtitles inside your videos, subtitles that came with a release, and the subtitles of videos still in the folder (including ones the Subtitle Manager added) are never touched. A leftover that was still right for a renamed file is removed too; search again for that item afterwards.

Deleting an item from cli_debrid always removes its own subtitle files with it.

Searches and fixes run in the background with their own progress and **Stop** button.

The **Bulk subtitles** task on the [Automation](../features/automation.md) page (off by default) searches up to 200 items an hour that are missing a language. Items searched in the last 24 hours without a result are skipped.

---

## Bazarr

### Moving from Bazarr

**Subtitle Manager → Import from Bazarr** copies Bazarr's languages, providers, OpenSubtitles.com login and embedded-subtitle settings into Subtitle Settings. Bazarr's subsync isn't copied: cli_debrid doesn't re-time subtitles, it picks ones made for your release. Subtitles Bazarr already synced or matched are marked as checked, so **Fix existing subtitles** leaves them alone. Nothing in Bazarr is changed. You'll need Bazarr's URL and API key (Bazarr → Settings → General → Security). From Docker, use the host's IP rather than `localhost`.

### Keeping Bazarr

cli_debrid can pose as Radarr and Sonarr so Bazarr can download subtitles for your library.

| Setting | Default | Description |
|---|---|---|
| **Enable Bazarr Spoofing** | Off | Expose the Radarr/Sonarr API endpoints Bazarr connects to |
| **API Key** | — | The key Bazarr uses. Click **Generate** to create one. |
| **Service Type** | `auto` | Which service to emulate: `auto` (both), `radarr` (movies) or `sonarr` (TV) |
| **Spoofed Version** | `5.14.0.9383` | Version reported to Bazarr. Change it only if Bazarr asks for a specific one. |
