---
title: Subtitles
icon: material/subtitles
---

# Subtitles

**Settings → Subtitles** sets up subtitle downloads and the Bazarr integration. Subtitles need Symlinked/Local file management.

---

## Subtitle Settings

| Setting | Default | Description |
|---|---|---|
| **Enable Subtitle Downloads** | Off | Download subtitles for movies and TV shows. Adds 2–3 seconds per file. Filtering for MULTI releases in your language is often a better choice. |
| **OpenSubtitles Username** | — | Your OpenSubtitles account |
| **OpenSubtitles Password** | — | Its password |
| **Subtitle Languages** | `eng,zho` | Comma-separated ISO-639-3 codes, e.g. `eng,fra,spa` |
| **Probe for Embedded Subtitles** | Off | Check the file with ffprobe first. If every language you want is already embedded, the search (and Bazarr notification) is skipped. Needs ffprobe, and reads from your mount. |

The **Bulk subtitles** task on the [Automation](../features/automation.md) page (off by default) processes the whole library. **Bulk Subtitle Scan** on the [Tools](../features/tools.md) page runs it once.

---

## Bazarr

Makes cli_debrid look like Radarr and Sonarr, so [Bazarr](https://www.bazarr.media/) can download subtitles for your library.

| Setting | Default | Description |
|---|---|---|
| **Enable Bazarr Spoofing** | Off | Expose the Radarr/Sonarr API endpoints Bazarr connects to |
| **API Key** | — | The key Bazarr uses. Click **Generate** to create one. |
| **Service Type** | `auto` | Which service to emulate: `auto` (both), `radarr` (movies) or `sonarr` (TV) |
| **Spoofed Version** | `5.14.0.9383` | Version reported to Bazarr. Change it only if Bazarr asks for a specific one. |
