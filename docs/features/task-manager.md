---
title: Task Manager
icon: material/clock-check
---

# Task Manager

The Task Manager lets you view, configure, enable/disable, and manually trigger all of cli_debrid's scheduled background tasks.

---

## How it works

Tasks run on a fixed interval in the background. Each task has a default interval that can be customised. A live countdown shows when each task will next run.

The info banner at the top includes a collapsible flowchart showing how items move through the queue states:

```
Content Source → Wanted → Scraping → Adding → Checking → Collected
```

Including sleep/retry loops, blacklisting, and the Final Scrape state.

---

## Tabs

Tasks are grouped into six categories:

| Tab | What it contains |
|---|---|
| **Queues** | Adding, Upgrading, Checking queue processors |
| **Content Sources** | Trakt, MDBList, Plex Watchlist, and other source checks |
| **System Tasks** | Database maintenance, health checks |
| **Library** | Plex file checking, library scans, symlink verification |
| **Metadata** | TVDB/TMDB metadata sync tasks |
| **Features** | Background feature tasks (overlays, upgrade hub, etc.) |

Each tab shows a badge with the count of tasks in that category.

A **search bar** at the top lets you filter tasks across all categories by name — useful when you know the task name and don't want to browse tabs.

---

## Per-task controls

Each task tile shows:

| Element | Description |
|---|---|
| **Status dot** | Green = enabled, Red = disabled |
| **Task name** | Display name of the task |
| **Library label** | e.g. "Plex library only" or "Symlink library only" where applicable |
| **Interval badge** | Configured interval (hover to see the default) |
| **Countdown timer** | HH:MM:SS until next run — shows `--:--:--` when disabled |
| **Toggle** | Enable or disable the task |
| **Interval input** | Override the interval in seconds — turns orange when different from the default |
| **ⓘ Info button** | Opens a detail panel showing the task description, category, status, configured interval, and default interval |

**Click a task tile** to trigger it immediately. A confirmation popup appears before it runs.

**Click the ⓘ button** on any tile to open the task info panel — shows the task description, what it does, and its current interval settings without triggering it.

---

## Interval formatting

| Raw value | Displayed as |
|---|---|
| < 60 seconds | `X sec` |
| < 60 minutes | `X min` |
| Longer | `Xh Ym` |

---

## Actions

| Button | Description |
|---|---|
| **Save** | Persist all toggle states and custom intervals |
| **Reset All to Default** | Delete all custom settings and restore defaults. Requires a program restart. |

---

## Notable tasks

### Features tab

| Task | Default | Enabled | Description |
|---|---|---|---|
| **Repair Broken NZBs** | 6h | No | Detects broken NZB downloads via Decypharr's health API, scrapes replacements, and resubmits. See [Usenet Migration](usenet-migration.md). |
| **Plex Stuck Files** | 5m | No | Detects Plex items stuck in a scanning loop and removes them. 5m is good when actively adding content; reduce to 1h once your library is settled. Requires Plex configured. |
| **Overlays** | 24h | No | Generates and uploads overlay posters to Plex. |
| **Upgrade Hub** | 6h | No | Checks collected items against upgrade criteria and triggers scrapes for better versions. |

### Library tab

| Task | Default | Enabled | Description |
|---|---|---|---|
| **Check Plex Files** | 5m | Yes | Verifies that Collecting items exist on the Plex mount and marks them Collected. |
| **Library Maintenance** | 24h | Yes | Cleans up stale entries, repairs missing metadata, and syncs the library state. |

---

## Notes

- The interval input turns **orange** when it differs from the default value
- The countdown timer pauses while you hover over a tile to prevent jitter
- If the program is not running, task states are loaded from the last saved configuration
- The **Library Maintenance** task shows an extra warning before triggering — it assumes cli_debrid has access to your mount location
