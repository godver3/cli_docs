---
title: Overlays
icon: material/image-multiple
---

# Poster Overlays

The Overlay system automatically adds informational badges to your poster artwork — resolution, HDR format, audio codec, ratings, and more. These display in Plex on top of your existing posters.

![Overlays overview](../assets/screenshots/features/overlays-overview.png)

---

## How it works

1. **Sync Library** — Clyde matches its database items to Plex using IMDB/TMDB IDs
2. For each matched item, a customised poster is generated with badges applied
3. The modified poster is uploaded back to Plex, replacing the original
4. Original posters are backed up and can be restored at any time

---

## Statistics cards

The top row shows a live summary of your overlay state:

| Card | Description |
|---|---|
| **Total Layouts** | Number of layouts defined, broken down by Movie/Show/Season |
| **Overlays Applied** | Items with an active overlay, broken down by type |
| **Unprocessed** | Items not yet processed — click to filter the grid to these items |
| **Cleaned Up** | Old overlay posters deleted by the [poster cleanup](#poster-cleanup) and the space freed. Click 👁 to preview what the next cleanup would delete (nothing is deleted). Turns orange when cleanup can't do its job: a data path without Plex's Metadata folder, or no permission to delete. Click ↺ to reset the counter. |
| **Failed** | Items where overlay generation failed — click to filter. Click ↺ to retry all. |
| **Last Sync** | When the overlay sync last ran, how many overlays it rendered, and how many existing overlays it sent back for a re-render (hover for quality / content / poster). Turns orange if it keeps re-rendering the same posters sync after sync, which means something is wrong: check the logs. |
| **Backup Size** | Total size of backed-up original posters and orphaned backup count. Use the trash button to clean up orphaned backups, or the broom button to delete all backups and reset overlays to pending. |

---

## Sync Library

Before overlays can be applied, Clyde must match its database items to Plex entries using IMDB/TMDB IDs. Click **Sync Library** to run a full sync.

Required:

- After first enabling overlays
- After adding large amounts of new content
- If overlays stop applying to certain items

A title+year fallback is used for items without IMDB/TMDB GUIDs.

---

## Movies tab

Shows all movies in a poster grid with their current overlay status.

| Status badge | Meaning |
|---|---|
| **Applied** | Overlay is active on this poster |
| **Pending** | Queued for generation |
| **Failed** | Generation failed — reason shown below the poster |
| **Not Started** | Not yet queued |

**Controls:**

| Button | Description |
|---|---|
| **Layout selector** | Choose which layout to use when generating |
| **Generate Library** | Generate overlays for ALL movies in the database |
| **Generate Selected** | Generate overlays for checked items only |
| **Remove Selected** | Remove overlays and restore original posters for checked items |
| **Select All** | Select all visible items |

**Per-card actions (on hover):**

| Button | Description |
|---|---|
| **↻ Regenerate** | Regenerate this poster's overlay using the current library poster |
| **✎ Poster Picker** | Choose an alternative poster from TMDB, then apply overlay on top |

Click a card to select/deselect it. Items with multiple versions show a version count badge.

The grid shows up to 300 items — use search to refine when your library is larger.

![Overlays movies tab](../assets/screenshots/features/overlays-movies.png)

---

## TV Shows tab

Same as Movies with two additional features per show card:

- **Seasons button** — opens the Season Overlays modal to manage per-season posters
- **Unprocessed seasons badge** — shows which season numbers still need overlays (e.g. `S1 · S2 unprocessed`). Click to open the Season modal directly.

### Season Overlays modal

Manage poster overlays for individual seasons of a show. Select a layout (or use Auto to pick the best available) and click **Generate Library** to apply across all seasons for all shows.

---

## Layouts tab

Create and manage overlay layout configurations. A layout defines which badges to show, where they are positioned, and their visual style.

**Layout actions:**

| Button | Description |
|---|---|
| **Create Layout** | Open the layout builder to create a new layout from scratch |
| **Import Layout** | Import a layout from a JSON file |
| **Load Default Layouts** | Import any missing built-in defaults (Movies, Shows, Seasons) |

Each layout card shows its name, description, type, and active status.

**Per-layout actions:** Edit, Deactivate / Set Active, Duplicate, Export, Delete

Different layouts can be assigned to Movies, Shows, and Seasons independently.

![Layout builder](../assets/screenshots/features/overlays-layout-builder.png)

---

## Layout Builder

The Layout Builder lets you design overlay layouts by placing and configuring badges on a live preview canvas.

### Badge types

There are five distinct badge categories in the palette, each working differently:

**Tray**

A background panel with no content of its own. Place a tray behind other badges to create a unified strip or box — typically at the bottom of the poster. Supports solid or gradient fills, borders, border radius, and opacity control.

---

**Text Badges**

The most versatile type. Renders text onto the poster using a `{{variable}}` template. Supports a background box, an optional icon to the left or right, full font customisation (family, size, weight, colour, alignment), and vertical stacking for two-line labels.

Presets cover every common data type — select from the **Badge Type** dropdown:

| Preset | What it shows |
|---|---|
| IMDb / TMDb / Trakt Rating | Rating score with service logo |
| RT Critics / RT Audience | Rotten Tomatoes score |
| Resolution | `4K`, `1080p`, `720p`, etc. |
| HDR Format | `DV`, `HDR10+`, `HDR10`, `HLG` |
| Audio Codec | `TrueHD Atmos`, `DTS:X`, `DD+`, etc. |
| Audio Channels | `7.1`, `5.1`, `2.0` |
| Video Codec | `HEVC`, `AVC`, `AV1` |
| Format / Source | `REMUX`, `WEB-DL`, `WEBRip`, `HDTV` |
| Network | TV network name |
| Studio | Production studio name |
| Content Rating | `PG-13`, `TV-MA`, `R`, etc. |
| Show Status | `Returning`, `Airing`, `Ended`, `Canceled` |
| Versions / Duplicates | Count shown only when multiple versions exist |
| Custom Badge | Any combination of static text and `{{variables}}` |
| **File Match** | Conditional — see below |

---

**Smart Badges (Library Badges)**

Image-based badges. Instead of rendering text, the system selects a matching PNG image from your **Badge Library** (`/overlays/badges`) automatically based on the item's metadata. You control the size and position in the layout; the correct image is chosen at render time. If no matching asset exists for a given item, the badge is silently skipped.

Badge Library categories and their available slots:

| Category | Slots |
|---|---|
| **Audio Codec** | AAC, Dolby Atmos, Atmos Standalone, DD+ Atmos, Dolby Digital, Dolby Digital+, DTS, DTS-ES, DTS-HD, DTS-HD HRA, DTS-HD MA, DTS:X, FLAC, MP3, PCM, TrueHD, TrueHD Atmos |
| **Video Codec** | AV1, AVC, HEVC, VP9 |
| **Resolution** | 480p, 720p, 1080p, 2160p/4K |
| **HDR Format** | Dolby Vision, DV+HDR, DV+HDR10, DV+HDR10+, HDR, HDR10, HDR10+, HLG |
| **Format / Source** | Blu-ray, DVD, HDTV, WEB-DL, WEBRip |

Upload your own PNG badge images via the **Badges** tab or at `/overlays/badges`. Each slot can have one image — upload to the slot that matches the metadata value you want to display. Custom variation slots can be added for metadata values not in the default list.

---

**Designed Badges**

Procedurally rendered vector badges — no image uploads required. Each preset generates a styled badge at render time using the item's actual metadata. Select a preset from the dropdown to control what data is shown:

| Preset | What it shows |
|---|---|
| Custom (manual text) | Static text or custom layout you configure manually |
| Resolution + HDR | Resolution and HDR type combined in one badge |
| Resolution | Video resolution only |
| HDR Format | HDR type only |
| Audio Codec | Audio codec name |
| Audio Channels | Channel layout only |
| Audio Codec + Channels | Codec and channels side by side |
| Audio Stacked (codec / channels) | Codec and channels stacked vertically |
| Video Codec | Video codec name |
| Format / Source | Release source (e.g. `REMUX`, `WEB-DL`) |
| IMDb Rating | IMDb score |
| TMDb Rating | TMDb score |
| Trakt Rating | Trakt score |
| RT Critics | Rotten Tomatoes critics score |
| RT Audience | Rotten Tomatoes audience score |
| Network | TV network name |
| Studio | Production studio name |
| Content Rating | MPAA/TV content rating |
| Show Status | Current show status |
| Versions / Duplicates | Version count badge |

---

**Title Logo**

Renders the title onto the poster. When **Enable Textless / Clean Posters** is on and a textless poster is found, the title is rendered as a clearlogo PNG from TMDB — the official transparent title treatment. If no clearlogo exists, falls back to text in the configured font. This is the main reason to use textless posters: place the title exactly where you want it rather than relying on the baked-in title from a standard poster.

---

### File Match badge

The **File Match** badge is useful for flagging attributes that aren't available as standard metadata — for example, `EXTENDED`, `DIRECTOR'S CUT`, `REMASTERED`, or a specific encode group present in the filename.

**How it works:**

1. Add a Text Badge and set the type to **File Match**
2. Enter a **Search Term** — the badge only renders if this text is found in the video filename (case-insensitive)
3. Optionally enter a **Display Text** — shown on the badge instead of the search term. Leave empty to use the search term itself.
4. Toggle **Use icon instead of text** to show an icon (configured in the Icon section) rather than text

Use the **Background**, **Icon**, and **Text / Value** sections to style the badge exactly as you would any other badge. The canvas preview always shows the badge so you can design its appearance.

**Examples:**

- Search term `REMUX` → badge appears only on remux files, displaying `REMUX`
- Search term `extended`, display text `Extended Cut` → styled label on extended editions only
- Search term `x265` with an icon → icon badge visible only on x265 encodes

---

## Badges tab

Browse and manage badge PNG assets. Badges are auto-selected at render time based on the media item's metadata (codec, resolution, HDR format, etc.).

Shows a summary of badge types, total variations, and uploaded assets. Click **Open Badge Library** to manage badge assets at `/overlays/badges`.

---

## Activity tab

A chronological audit log of all overlay operations.

Filter by action type:

- Overlay Sync, Cleanup
- Generate / Regenerate / Generate All / Regenerate All
- Remove / Remove All
- Layout Created / Updated / Deleted
- Sync Library
- Season Generate / Regenerate / Remove
- Poster Reset

Entries are paginated (50 per page) and colour-coded by result (success, failed, partial).

---

## Settings

Overlay settings are accessible directly from the **Overlay Management** page via the **Settings** button in the top action bar — no need to navigate to the Settings menu.

Click **Settings** (top right of the Overlay Management page) to open the Overlay Settings modal:

| Setting | Default | Description |
|---|---|---|
| **Enable Overlay System** | Off | Master toggle. When enabled, overlay sync tasks run automatically and apply media info badges to Plex posters. Requires Plex URL and token to be configured. |
| **Enable Textless / Clean Posters** | Off | When enabled, Clyde fetches a language-neutral (textless) poster from TMDB as the base image — these have no baked-in title text so the **Title Logo** badge can render cleanly at your chosen position. Use the Title Logo badge in the layout editor to add the show or movie title as a transparent clearlogo PNG (with text fallback if no clearlogo exists). The Title Logo badge is only available in the layout editor when this setting is on. **Note:** Not all titles have textless posters on TMDB — if none is found, the standard English poster is used as fallback. |
| **Media Server Data Path** | — | Plex's data folder as Clyde sees it: the folder that contains Plex's `Metadata` folder (e.g. `/plex_data` with the mount from the install guides). Only used by the [poster cleanup](#poster-cleanup). The modal checks it when you save and offers the right folder if it's one level off. |
| **Ratings Check Interval (days)** | `7` | How often to re-fetch ratings (IMDb/TMDB/Trakt/RT) and show status to detect changes. Set to `0` to check every sync run. Version count changes are always checked every sync regardless of this setting. |
| **Items Per Sync Run** | `200` | Maximum number of shows/movies processed per overlay sync run. Higher values clear backlogs faster but each run takes longer (~1s per item). |

**Poster Reset:**

Use these when migrating from another overlay app (Kometa, PMM, etc.) or to clear any foreign overlays. Overlays will **not** be re-applied automatically after a reset — use **Generate All** when ready.

| Option | Description |
|---|---|
| **Reset All Posters** | Reset ALL posters to clean originals from TMDB |
| **Review & Reset Selected** | Opens a selective grid to choose specific items to reset |

---

## Poster cleanup

Every time an overlay is re-rendered, Plex keeps the previous version of the poster on disk. Over months this adds up to gigabytes. The **Poster overlay cleanup** task deletes those old versions.

It only deletes uploaded posters that Plex reports as **not selected**, on items Clyde has overlaid. Posters you or other tools (Kometa, PMM) uploaded to other items are never touched, and neither is any poster Plex is currently showing.

### 1. Mount Plex's data folder and set the path

Clyde needs to reach Plex's data folder. The install guides mount it at `/plex_data`:

```yaml
volumes:
  - /path/to/plex/Library/Application Support/Plex Media Server:/plex_data
```

Then set **Media Server Data Path** to `/plex_data` in Overlay Settings. Don't mount it read-only (`:ro`): cleanup has to delete files.

The path must point at the folder that **contains `Metadata`**. A common mistake is one level too high: mounting `/var/lib/plexmediaserver` and setting the path to `/var/lib/plexmediaserver/Library`. The right path there is `/var/lib/plexmediaserver/Library/Application Support/Plex Media Server`. The Overlay Settings modal spots this and offers **Use this**.

### 2. Make sure Clyde may delete there

Plex owns its data folder. If Clyde runs as a different user, it can read the posters but not delete them. You'll see this as:

- the **Cleaned Up** card saying old posters couldn't be deleted,
- the 👁 preview saying files can't be deleted, with the command below,
- one warning per run in the logs: `Plex poster cleanup: N file(s) not deleted, no write access`.

| Your setup | What to do |
|---|---|
| Plex in Docker with the same `PUID` as Clyde | Nothing, it already works |
| Plex installed on the Linux host (runs as the `plex` user) | Run the command below once |
| Plex in Docker with a different `PUID` | Run the command below once, on the host path of Plex's config folder |
| Windows | Usually nothing |

On the Linux host, give Clyde's user write access to Plex's Metadata folders. Replace `1000` with Clyde's `PUID` and use the **host** path to Plex's folder:

```bash
sudo find "/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Metadata" \
  -type d -exec setfacl -m u:1000:rwx,d:u:1000:rwx {} +
```

This adds an access rule for that one user and doesn't change who owns the files or how Plex runs. The `d:` part makes folders Plex creates later get the same rule. Adding Clyde to the `plex` group doesn't work: the container doesn't keep host groups.

### 3. Preview, then run it

Click 👁 on the **Cleaned Up** card to see what the next cleanup would delete and how much space it frees. Nothing is changed. Then run **Poster overlay cleanup** from the [Automation](automation.md) page, or let it run on its daily schedule. The first run on an older install can delete thousands of files; after that each run only checks items re-rendered since the last one.

---

## Top-level actions

| Button | Description |
|---|---|
| **Regenerate All** | Force re-render all overlays for movies, shows, and seasons — overwrites existing |
| **Remove All** | Remove all overlays from the entire library and restore original posters |

Long-running operations show a **Task Progress** overlay with a live progress bar, item counter, and failure count. Click **Continue in background** to hide the modal while the task runs.

---

## Automatic regeneration

When overlays are enabled, newly collected items are automatically queued for overlay generation. Configure the check interval via the **Settings** button on the Overlay Management page, or under **Settings → Media Server → Overlay Settings → Overlay Content Check Interval Days**.

!!! info "Scheduled tasks"
    | Task | Default interval |
    |---|---|
    | **Poster overlays** | Every **1 hour** |
    | **Poster overlay cleanup** | Every **24 hours** |

    Adjust intervals or run them now on the [Automation](automation.md) page (Plex & Media Server group).
