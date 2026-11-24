---
title: Plex Labels
icon: material/label
---

# Plex Label Manager

The Plex Label Manager automatically labels your Plex items based on which content source added them, or who requested them via Seerr. This lets you create Plex smart collections and see at a glance where content came from.

![Plex Label Manager](../assets/screenshots/features/plex-labels-overview.png)

---

## What are Plex labels?

Plex labels are tags applied to movies and TV shows in your Plex library. Clyde manages these automatically based on your content source configuration. Use them to:

- **Track requesters** — see who requested each item (e.g. `Requested by John`)
- **Identify sources** — know which source added an item (e.g. `Overseerr`, `Trakt: Family Movies`)
- **Create smart collections** — use Plex's smart filter feature to build persistent filtered views
- **Monitor usage** — track which users are actively requesting content

---

## Label modes

Configure the label mode per content source in **Settings → Content Sources → [Source] → Plex Labels**:

| Mode | Label applied | Example |
|---|---|---|
| **List Name** | The content source's display name | `Trakt Watchlist`, `MDBList Sci-Fi` |
| **Fixed** | A custom label you define | `Auto-Downloaded` |
| **Requester** | Seerr requester's username | `john`, `alice` |

---

## How labels are applied

Labels are applied in two ways:

- **During collection** — when an item is successfully collected, labels are generated and synced to Plex immediately
- **Manual sync** — use the label tools on the [Tools](tools.md#plex-labels) page to sync labels for existing items

---

## Utilities (Tools → Plex Labels)

Access all label management tools from **Tools → All Tools → Plex Labels → Plex Labels Management**.

### View Items by Label

Search for all items in your library that have a specific label applied. Useful for auditing label application and verifying which items are tagged.

### Bulk Apply Labels from Source

Retroactively apply labels from a specific content source to all matching collected items. Use this after enabling Plex labels for a source that already had collected items.

**How:** Select a source from the dropdown → **Preview** to see what will be labelled → **Apply Labels**

### Bulk Remove Labels

Remove a specific label from all items in the database and Plex. Use when disabling a source, renaming a label, or cleaning up old labels.

**How:** Enter the label name → **Preview** → **Remove Label**

### Orphaned Label Cleanup

Finds and removes labels that are tracked in the database but whose content source no longer exists or has been disabled. Keeps your Plex label list clean.

**How:** **Find Orphaned Labels** → **Cleanup**

### Sync Labels from Content Sources

Re-syncs all labels based on current content source configurations. Applies labels to all Collected items from sources that have Plex labels enabled.

---

## Sync functions (Automation)

| Function | Processes | Updates DB? | Syncs to Plex? | Time | Use case |
|---|---|---|---|---|---|
| **Sync Plex Labels** | Collected items due for sync | ✅ Labels | ✅ | Minutes | Automatic periodic sync (every 30 min) |
| **Rebuild Plex labels (all)** | ALL items | ✅ Requester names and labels | ✅ | Hours on a large library | Initial setup, after config changes |
| **Rebuild Plex labels (recent)** | Recently changed/new items | ✅ Requester names and labels | ✅ | Minutes | Catch-up, missing labels |

The two rebuild tasks are in the **One-time fixes** group on the [Automation](automation.md) page (shown in Advanced view). They replace the old "from details", "missing" and "backfill" variants: each first fills in missing requester names, then syncs the labels.

### Sync Plex Labels

!!! info "Scheduled task"
    Runs automatically every **30 minutes** by default. Turn it on, adjust the interval or run it now on the [Automation](automation.md) page (Plex & Media Server group).

The automatic periodic task that runs in the background. Syncs labels for Collected items that are due for a sync. You can also trigger it manually to force an immediate sync without waiting for the next scheduled run.

### Rebuild Plex labels (all)

Fills in missing requester names (from Seerr), regenerates labels for **every** collected item from current content source data, and syncs them to Plex. Sets the timestamps the recent rebuild uses.

!!! warning "Slow on a large library"
    At 2–3 items a second, 5000 items take 13–14 hours. Run it overnight and follow progress on the Logs page. It's safe to restart if interrupted and won't duplicate labels.

### Rebuild Plex labels (recent)

The same, but only for items that were never synced or were collected in the last 7 days. Usually done in minutes — use this for routine catch-up.

---

## Recommended workflows

### Initial setup

1. Configure label settings in **Settings → Content Sources**
2. Run **Rebuild Plex labels (all)** overnight
3. Check in Plex that the labels appear

### Routine maintenance

**Sync Plex labels** runs every 30 minutes once it's on. Run **Rebuild Plex labels (recent)** if items are missing labels.

### After configuration changes

Run **Rebuild Plex labels (all)** so every item reflects the new configuration.

---

## Using labels in Plex

Once labels are applied you can filter by them in Plex:

1. In your library, click **All** → **Filters**
2. Select **Label** → choose your label
3. Save as a **Smart Collection** for a persistent filtered view

Examples:
- *"Requested by Alice"*
- *"From Trakt Watchlist"*
- *"From MDBList Horror"*

![Plex smart collection using labels](../assets/screenshots/features/plex-labels-smart-collection.png)

---

## Troubleshooting

**Labels not appearing in Plex**

1. Check **Settings → Content Sources** — verify labels are enabled for the source
2. Run **Rebuild Plex labels (all)**
3. Force a metadata refresh in Plex

**Labels show "Unknown" instead of names**

Run **Rebuild Plex labels (all)** or **(recent)**. Both fetch the requester names from Seerr before syncing.

**Some items have labels, others don't**

- Run **Rebuild Plex labels (recent)**
- Check the logs for errors about specific titles
- Check that the items exist in Plex

**The full rebuild takes too long**

- That's expected — 5000 items at 2–3 items a second take 13–14 hours
- Let it run overnight and follow progress on the Logs page
- Use the recent rebuild for routine catch-up

---

## Technical notes

- **TV shows:** Labels are applied at the show level, not per episode. Processing 100 episodes of a show makes only **1 API call** to Plex.
- **Rate limiting:** Processes ~2–3 items/second to avoid overwhelming the Plex API.
- **Database fields:** `content_source`, `content_source_detail`, `plex_labels` (JSON), `plex_labels_last_synced` (timestamp for incremental mode).

### Custom sync interval (API)

To sync items from a custom window instead of the default 7 days:

```bash
# Sync items from last 30 days
curl -X POST http://localhost:5000/debug/sync_plex_labels \
  -H "Content-Type: application/json" \
  -d '{"incremental": true, "days_back": 30}'
```
