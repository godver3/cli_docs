---
title: Plex Movie Box Sets
icon: simple/plex
---

# Plex Movie Box Sets

CLI Debrid automatically discovers which movies in your library belong to TMDB franchise collections, creates matching Plex collections for them, applies franchise posters, and optionally queues missing franchise movies to the wanted list.

!!! note "Plex only"
    Plex Movie Box Sets requires Plex as your media server.

!!! note "Movies only"
    Box sets are built from TMDB franchise/collection data, which covers movies only. TV shows are not included.

---

## Overview

TMDB groups movies into franchise collections — "The Godfather Collection", "Star Wars Collection", and so on. Box Sets uses this data to:

- **Auto-discover franchises** — every movie in your database is checked against TMDB to find its franchise membership
- **Create Plex collections** — one Plex collection per franchise, kept in sync with your library
- **Apply franchise posters** — TMDB's official franchise poster is downloaded and applied directly; a rendered fallback is used if none exists
- **Queue missing movies** — optionally adds franchise movies you don't own to the wanted queue

---

## Setup

In **Settings → Additional Settings → Plex Movie Box Sets**, enable the feature and configure the options below.

| Setting | Default | Description |
|---|---|---|
| **Enable** | Off | Turns the feature on/off |
| **Grab Missing Movies** | Off | Adds franchise movies not in your library to the wanted queue |
| **Version to Grab** | Default | Quality/version used when grabbing missing movies |
| **Collection Name Pattern** | `{title} Collection` | Template for Plex collection names. `{title}` is the franchise name (e.g. "The Godfather"). Examples: `{title} Box Set`, `{title} Saga` |
| **Minimum Owned Movies** | 2 | Minimum number of owned movies required to create a collection. Collections that drop below this threshold are automatically deleted from Plex on the next run |
| **Collection Sort Order** | Release Date | How movies are ordered inside the Plex collection (Release Date, Title, Custom) |

---

## How it works

Each run processes in five phases:

1. **TMDB lookup** — every movie in the database is queried against TMDB to check franchise membership. Already-checked movies are skipped on subsequent runs. The first run takes approximately 30 minutes for large libraries; subsequent runs are near-instant.
2. **Build box set list** — movies are grouped by franchise. Only franchises with at least the configured minimum number of owned movies are included. Full collection details and posters are fetched from TMDB.
3. **Sync Plex collections** — Plex collections are created or updated. The configured sort order is applied.
4. **Apply posters** — the TMDB franchise poster is downloaded and uploaded to Plex. If TMDB has no poster for the franchise, a fallback Layout 1 poster is rendered using the CLI Debrid icon. Collections whose content fingerprint hasn't changed are skipped.
5. **Queue missing movies** *(optional)* — if **Grab Missing Movies** is enabled, franchise members not in your library are added to the wanted queue.

---

## Collection naming

The **Collection Name Pattern** setting uses `{title}` as a placeholder for the franchise name from TMDB.

Suffix words are automatically stripped from the TMDB franchise name before your pattern is applied, so you never get doubled suffixes:

> TMDB name: `The Godfather Collection`
> Stripped to: `The Godfather`
> Pattern `{title} Box Set` → **The Godfather Box Set**

Stripped suffixes: Collection, Box Set, Saga, Series, Trilogy, Universe, Franchise.

For franchises where TMDB has no collection name, the title of the earliest owned movie in the franchise is used as the base name.

---

## Minimum movies threshold

Collections that fall below the **Minimum Owned Movies** threshold — because you deleted a movie or the threshold was increased — are automatically removed from Plex on the next run. No manual cleanup needed.

---

## Schedule and manual trigger

Runs automatically on a **24-hour schedule**. To trigger immediately:

- **Task Manager** — find "Plex Movie Box Sets" and click Run
- **Settings** — use the **Run Now** button in the Plex Movie Box Sets settings section

---

## State file

CLI Debrid tracks content fingerprints in `plex_boxsets_state.json` to avoid re-uploading unchanged posters. To force a full poster re-apply on the next run:

**Debug → Manage Cache Files → Plex Box Sets State** — delete the state file, then trigger the task manually.

---

## Requirements

- Plex URL and token configured under **Settings → Plex**
- TMDB API key (used for franchise lookups and poster downloads)

---

## Troubleshooting

**Too many collections created**

- Lower the **Minimum Owned Movies** threshold. Any franchise collection that doesn't meet the new minimum is automatically deleted from Plex on the next run.

**A collection is not showing in Plex**

- The franchise must have at least the configured minimum number of movies in `Collected` state with a Plex rating key recorded in the database
- Check that the movie has been matched to TMDB — the TMDB lookup phase must have run for that movie at least once

**Wrong or missing poster**

- Clear the Box Sets State cache file via Debug → Manage Cache Files → Plex Box Sets State, then trigger the task manually to force a full re-apply

**Sort order is wrong inside a collection**

- Sort order is re-applied on every run — trigger the task manually to correct it immediately

**Missing movies not being queued**

- Confirm **Grab Missing Movies** is enabled and a **Version to Grab** is set
- The TMDB lookup phase must complete for the relevant movies before missing members can be identified
