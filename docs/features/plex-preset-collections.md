---
title: Plex Preset Collections
icon: simple/plex
---

# Plex Preset Collections

Ready-made Plex collections you switch on one by one, in the spirit of Kometa's default collections: **Christmas Movies**, **Box Office Blockbusters**, **Trending**, **1990s Movies**, **Oscar Best Picture Winners**, **Pixar** and more. Clyde builds them from titles that are already in your Plex library and keeps them up to date. Added in 0.9.2.

!!! note "Plex only"
    Preset collections need Plex as your media server, in either Direct Mount or Symlinked/Local mode.

!!! info "Nothing is downloaded"
    Presets only group what you already have. Titles from a list that aren't in your library are skipped, never requested. To fill a list in, add it as a [content source](../configuration/content-sources.md) instead (and use [Plex Collections](plex-collections.md) for its collection).

---

## Setup

Open **Settings → Media Server → Plex Collections → Preset collections**, tick the presets you want and click **Save Settings**. Every preset is off until you tick it.

Saving starts a sync straight away, so the collections appear in Plex within a minute or so. No restart is needed.

| Setting | Default | Description |
|---|---|---|
| **Preset checkboxes** | All off | One per collection, grouped as below |
| **Minimum titles for a collection** | 3 | A preset only becomes a collection once at least this many matching titles are in the library. A collection that drops below it is removed on the next run |
| **Run Now** | | Syncs every enabled preset immediately. The line next to it shows the last run, how many collections are managed and any preset that was skipped |

---

## Presets

### Seasonal

| Preset | Collection | Source |
|---|---|---|
| Christmas | Christmas Movies | TMDB keyword `christmas` |
| Halloween | Halloween Movies | TMDB keyword `halloween` |
| Thanksgiving | Thanksgiving Movies | TMDB keyword `thanksgiving` |
| Valentine's Day | Valentine's Day Movies | TMDB keyword `valentine's day` |
| New Year's Eve | New Year's Eve Movies | TMDB keyword `new year's eve` |

Seasonal collections are visible all year.

### Charts

These are kept in rank order inside the collection. Presets marked *movies + shows* make one collection in each library type (for example **Top Rated Movies** and **Top Rated Shows**).

| Preset | Collection | Source |
|---|---|---|
| Box Office Blockbusters | Box Office Blockbusters | TMDB, highest box-office revenue (top 200) |
| Top Rated | Top Rated Movies / Shows | TMDB Top Rated (top 400), movies + shows |
| Trending This Week | Trending Movies / Shows | TMDB weekly trending (top 100), movies + shows |
| Popular | Popular Movies / Shows | TMDB Popular (top 200), movies + shows |

### Decades & Genres

Built from your Plex library itself, with no outside lists.

| Preset | Collections |
|---|---|
| Decades | One per decade: **1980s Movies**, **1990s Shows**… |
| Genres | One per Plex genre: **Action Movies**, **Horror Movies**… |

!!! tip "Genres is optional"
    Plex already lets you browse and filter by genre, so **Genres** mostly adds a lot of collections (one per genre per library). Leave it off unless you want them as collections.

### Awards

Winners come from [Wikidata](https://www.wikidata.org/) (no API key needed) and are matched by IMDb ID.

| Preset | Collection |
|---|---|
| Oscar Best Picture | Oscar Best Picture Winners |
| Oscar Best Animated Feature | Oscar Best Animated Feature Winners |
| Palme d'Or | Palme d'Or Winners |
| Emmy Outstanding Drama Series | Emmy Outstanding Drama Series Winners (shows) |
| Emmy Outstanding Comedy Series | Emmy Outstanding Comedy Series Winners (shows) |

### Studios

Movies by TMDB production company: **Pixar**, **Walt Disney Animation Studios**, **DreamWorks Animation**, **Illumination**, **Studio Ghibli**, **Marvel Studios**, **DC** (DC Films and DC Studios), **Lucasfilm**, **A24** and **Blumhouse**.

---

## How it works

On each run, for every enabled preset:

1. **Get the list.** TMDB presets need the TMDB API key (**Settings → Required**). Lists are cached: Trending and Popular for 12 hours, everything else for 7 days.
2. **Keep what's in Plex.** Each title is matched to your Plex library by TMDB ID, then IMDb ID, then an exact title and year. Titles that aren't in the library are skipped.
3. **Update the collection.** New matches are added and titles that left the list are removed. Chart presets are put back in rank order; the others sort by release date.

If a list can't be fetched (TMDB or Wikidata down, no TMDB key), that preset is skipped and its existing collections are left as they are. The status line next to **Run Now** says which presets were skipped.

### Your own collections are safe

- **Switching a preset off** deletes the collection Clyde made for it. The same happens when a collection drops below **Minimum titles**.
- **A collection that already existed** with the same name (one you made yourself, or one from Kometa) is taken over **add-only**: Clyde adds matching titles to it but never removes anything from it, and never deletes it. When you switch that preset off, Clyde just stops managing it.

---

## Schedule

Preset collections refresh:

- once a day, through the **Preset collections** task on the [Automation](automation.md) page (on by default when Plex is your media server; it does nothing until a preset is ticked)
- whenever you save the preset settings
- when you click **Run Now**

---

## Troubleshooting

**A collection didn't appear**

- You need at least **Minimum titles** matching titles in that library. Lower the setting to 1 or 2 to see small collections such as Palme d'Or Winners
- TMDB presets need the TMDB API key. Check the status line next to **Run Now** for skipped presets
- Titles are matched by their Plex IDs. An item Plex matched to the wrong movie or show won't land in the right collection

**Too many collections**

- Switch **Genres** off: it makes one collection per genre per library. Clyde deletes the genre collections it made on the next run

**State file**

- What Clyde manages is kept in `plex_preset_collection_state.json` in your config folder. Deleting it makes Clyde forget its collections: it then treats them as existing collections (add-only) and won't delete them when you switch a preset off
