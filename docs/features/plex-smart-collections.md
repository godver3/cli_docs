---
title: Plex Smart Collection Posters
icon: simple/plex
---

# Plex Smart Collection Posters

CLI Debrid can apply custom designed posters to the built-in smart collections Plex auto-generates — "Recently Added", "Top Rated", and similar library-level collections.

!!! warning "Posters only — no collection creation"
    This feature does **not** create smart collections. It only applies custom posters to smart collections that Plex has already created. Plex generates these automatically based on your library content.

!!! note "Plex only"
    Plex Smart Collection Posters requires Plex as your media server.

---

## Overview

Plex automatically maintains smart collections in each library section. This feature applies a consistent, custom-designed poster to whichever of those collections you enable — keeping your Collections view visually uniform with the rest of your CLI Debrid posters.

- **One shared design** — a single poster design applies across all enabled smart collections
- **Per-collection control** — enable or disable poster overrides for individual smart collections
- **Efficient re-runs** — collections whose content fingerprint hasn't changed are skipped
- **Same layouts as Plex Collections** — layouts 1–5 with identical configuration options

---

## Setup

In **Settings → Additional Settings → Plex Smart Collection Posters**, enable the feature and configure the shared poster design. Once enabled, all discovered smart collections appear as individual toggles below the design settings.

| Setting | Description |
|---|---|
| **Enable Plex Smart Collection Posters** | Turns the feature on/off |
| **Poster Design** | Layout applied to all enabled collections. Options: Plex Default, Layout 1–5 |
| **Poster Accent Color** | Accent color for header text, glow, and decorative elements. Leave unset to use each layout's built-in default |
| **Eyebrow Text** | Small text displayed above the collection title on the poster. Leave blank to hide |
| **Poster Icon** | Icon displayed on the poster. Defaults to the CLI Debrid icon |
| **Card Overlay Opacity** | Darkness of the gradient fade at the bottom of each card. Range: 0–100%, default 60% |
| **Accent Glow Opacity** | Brightness of the accent color glow around the poster edges. Range: 0–100%, default 80% |
| **Accent Glow Radius** | How far the accent color spreads across the poster background. Range: 10–200, default 55 |
| **Per-collection toggles** | After enabling, each discovered Plex smart collection appears as an individual toggle |

!!! tip "Per-collection toggles"
    Toggles only appear after the feature is enabled and a run has completed (or triggered manually). If no toggles appear, verify Plex has at least one smart collection in any library section.

---

## How it works

On each run, CLI Debrid:

1. Scans all Plex library sections for smart collections
2. For each enabled smart collection, fetches up to 4 movie or show thumbnails from Plex
3. Renders the poster using the configured design, accent color, eyebrow text, and icon
4. Uploads the poster directly to Plex
5. Skips collections whose content fingerprint hasn't changed since the last run

---

## Schedule and manual trigger

Runs automatically on a **24-hour schedule**. To trigger immediately:

- **Task Manager** — find "Plex Smart Collection Posters" and click Run
- **Settings** — use the **Run Now** button in the Plex Smart Collection Posters settings section

---

## State file

CLI Debrid tracks content fingerprints in `plex_smart_collection_state.json` to avoid re-rendering unchanged posters. To force a full re-render on the next run:

**Debug → Manage Cache Files → Plex Smart Collection State** — delete the state file, then trigger the task manually.

---

## Requirements

- Plex URL and token configured under **Settings → Plex**
- TMDB API key (used for artwork)
- At least one smart collection present in any Plex library section

---

## Troubleshooting

**No smart collections appearing as toggles**

- Plex must have generated at least one smart collection in any library section — check your library's Collections view in Plex
- Trigger the task manually after enabling the feature to force a discovery scan

**Poster not updating in Plex**

- Clear the Smart Collection State cache file via Debug → Manage Cache Files, then trigger the task manually
- Plex may briefly show the old poster while processing — wait 10–15 seconds and refresh

**Wrong or unexpected poster on a collection**

- The shared design applies to all enabled collections — adjust the design settings and trigger a re-run, or disable the toggle for that specific collection to revert to Plex's default poster
