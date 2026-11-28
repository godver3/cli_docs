---
title: Database Browser
icon: material/database
---

# Database Browser

The Database Browser lets you view, filter, sort, and take actions on every item in your media library directly — without needing a separate SQLite tool. It's the go-to place for bulk operations and inspecting item states.

![Database browser overview](../assets/screenshots/features/database-overview.png)

---

## Top bar and stats

The top bar shows **Total Items**, **Unique Items** (versions of the same movie or episode count once), **Pages** and a **Per Page** menu (100, 250, 500 or 1000). Total and Unique cover everything your filter matches, not just the loaded page. Row numbers keep counting across pages.

Click the chart icon to expand the Stats panel showing total Movies, Shows and Episodes in your database.

Rows load as you scroll. When you reach the end of the loaded rows, the next page loads. Changing a filter, sort or letter does not reset **Per Page**.

---

## Content type & alphabet filters

| Filter | Options |
|---|---|
| **Content type** | All, Movies, Episodes |
| **Alphabet** | All, #, A–Z — jump to items starting with that letter |

---

## Advanced filtering

Click **Add Filter** to build multi-condition filters. Quick filter buttons for common columns (Title, State, Version, IMDB ID, Type) are also available.

| Filter option | Description |
|---|---|
| **Column** | Any column in the table |
| **Operator** | contains, equals, greater than, less than, etc. |
| **Value** | Text input or dropdown (pre-populated for State, Type, Version, Content Source, Upgraded, Early Release) |
| **Logic** | AND (all filters must match) or OR (any filter matches) |

---

## Sorting

Use the **Sort Column** dropdown and **Ascending / Descending** toggle, or click a column header. Click **Apply** to update results.

---

## Saved presets

Click **Save Preset** to keep the current filters and sort. Your presets are listed under **Saved Presets**. Presets are stored in your browser.

---

## Column customisation

Click **Select Columns to Display** to open the column manager:

- Move columns between **Available** and **Selected** lists
- Reorder selected columns with the ▲ ▼ buttons
- Drag column headers to resize widths
- All choices persist in your browser (localStorage)

Every column of the items table can be shown, plus **size** (in GB). **Reset Cols** restores the default column widths.

---

## Per-item actions

Each row has inline action buttons:

| Action | Description |
|---|---|
| **Delete (×)** | Remove item from the database. Optionally blacklist to prevent re-adding. |
| **Rescrape (↻)** | Delete and move back to the Wanted queue for a fresh scrape |
| **Open in Library** | Open the item in the Library |
| **Move to Wanted** | Move the item back to Wanted |
| **Blacklist** | Blacklist the item |

---

## Bulk operations

Select items using checkboxes. Use **Shift+click** to select a range. Then choose an action from the bulk action bar:

| Action | Description |
|---|---|
| **Delete Selected** | Remove all selected items. Optionally blacklist. |
| **Rescrape Selected** | Move all selected back to Wanted |
| **Move to Queue** | Move all selected to a specific queue state |
| **Change Version** | Apply a different quality profile to all selected |
| **Tags** | Assign one of your tags to all selected |
| **Early Release** | Flag selected items for early-release handling |
| **Force Priority** | Mark items to jump to the front of the queue |
| **Resync Selected** | Resync symlinks and database paths for selected items |
| **Verify Symlinks** | Add selected items to the symlink verification queue |

!!! tip "Select across all pages"
    **Select All** ticks the rows loaded on screen. A **Select all N matching** link then appears to select every item the current filter matches. Ticks stay put as you scroll, even for rows that scrolled out of view.

Bulk operations are batched (450 items per batch) to avoid database lock issues.

---

## Item states

| State | Meaning |
|---|---|
| **Wanted** | Waiting to be scraped — will be processed next cycle |
| **Scraping** | Currently being searched |
| **Adding** | Torrent found, being submitted to debrid |
| **Checking** | Waiting for file to appear at mount |
| **Collected** | In your library |
| **Sleeping** | All known torrents blacklisted — waiting to retry |
| **Blacklisted** | Torrent blacklisted for this item |
| **All Versions Blacklisted** | Every version has been blacklisted |
| **Unreleased** | Release date not yet reached — will auto-move to Wanted on release |
| **Pending Uncached** | Waiting for an uncached download slot |
| **Upgrading** | Better version being sought |
| **Final Scrape** | One last scrape attempt before blacklisting |
| **Ghostlisted** | Soft-deleted — hidden from library but preserved in the database |

---

## Common tasks

### Finding a stuck item

1. Filter by **State** → select the stuck state (e.g. Sleeping)
2. Search for the title
3. Use **Rescrape** to retry, or **Move to Queue** to force a state

### Bulk-clearing sleeping items

1. Filter by **State = Sleeping**
2. Click **Select All** then **Select all N matching**
3. Click **Move to Queue** → **Wanted**

### Removing a show completely

1. Filter by title
2. Select all episodes and the show entry
3. Click **Delete Selected**
4. Check **Blacklist** if you don't want it re-added from content sources

### Fixing an incorrect episode number

1. Find the item in the database
2. Note the Item ID
3. Go to **System → Maintenance → Cleanup & repair → Fix Episode Numbers**
4. Enter the Item ID and correct episode number
