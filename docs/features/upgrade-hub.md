---
title: Upgrade Hub
icon: material/arrow-up-bold
---

# Upgrade Hub

The Upgrade Hub scans your collected library and identifies items where a significantly better quality version is available — then lets you review and queue them for upgrade in bulk.

Open it from **Tools → Upgrade Hub**.

!!! warning "Beta feature"
    The Upgrade Hub is in beta. Verify suggestions before queuing and report issues on Discord.

!!! note "Sources"
    Scans check your Newznab indexers' releases and, if you run one, a self-hosted [Zilean](../scrapers/zilean.md#upgrade-hub-direct-db-connection) instance, against the whole library. They also search your scrapers for a few recently released items. Choose sources under **Bulk Sources** in the Settings tab.

![Upgrade Hub overview](../assets/screenshots/features/upgrade-hub-overview.png)

---

## How upgrades work

Clyde gives each collected item a **quality score** from your version settings: resolution, codec, HDR format, audio, release type and size. A release that scores enough higher than the current file is an upgrade.

Upgrades are found in two ways:

| | What it covers | Where it's set |
|---|---|---|
| **Upgrading after collecting** | A newly collected recent release is searched again every hour for a while, and replaced as soon as something better turns up. | The **Upgrading** group in the [Settings tab](#settings-tab) |
| **Upgrade Hub scans** | Your whole library, including items collected long ago. A better release that appears months later shows up here. | The rest of the [Settings tab](#settings-tab) |

The **Score Δ** column shows the improvement percentage and the before→after scores.

### Scan sources

| Source | How it works |
|---|---|
| **NZB indexers** | Checks every release your Newznab indexers posted in the last 90 days for your library. The **Upgrade Hub NZB feed sync** task reads what's new on each indexer every 30 minutes (usually one or two API calls each) and keeps the releases that match your library; scans match against that history. Releases the indexer tags with an IMDb ID are matched by ID. |
| **Zilean** | Reads a self-hosted Zilean instance for every collected item. Fast with the [direct DB connection](../scrapers/zilean.md#upgrade-hub-direct-db-connection), slow without it. |
| **Fresh Release Search** | Runs a normal search with your scrapers (Torrentio, Jackett, Newznab and so on) for up to 20 items released in the last 30 days, when better encodes keep appearing. Each item costs a search on every indexer, so it's capped. Items checked longest ago go first. |

When two sources find an upgrade for the same item, the bigger improvement wins.

---

## Scanning

!!! info "Scheduled tasks"
    | Task | Default interval |
    |---|---|
    | **Upgrade Hub scan** | Every **24 hours** |
    | **Upgrade Hub auto-queue** | Every **24 hours** |
    | **Upgrade Hub NZB feed sync** | Every **30 minutes**, only while Upgrade Hub scan is on |

    The scan and auto-queue are off by default. **Automatic Scan** and **Auto Queue** in the Settings tab switch them on (the same switches as on the Automation page). Adjust intervals or run them now on the [Automation](automation.md) page (Library & Upgrades group).

Click **Scan for Upgrades** to start a scan. The button shows how long ago the last scan ran (e.g. `2h ago`). During a scan a progress bar shows the current phase and ETA:

- Starting → Loading Zilean data → Scoring episodes & packs → Scanning movies → Checking NZB indexers → Searching fresh releases with your scrapers → Done

Phases for sources you don't use are skipped. Scheduled scans run in the background, so they don't hold up other tasks.

After scanning, summary chips show: upgrades found, packs found, movies scanned, episodes scanned, and any errors.

### Search Recent Releases

**Search Recent Releases**, next to **Scan for Upgrades**, searches your scrapers for every collected item released in the last N days. Use it when you want recent titles checked now, beyond what Fresh Release Search covers each scan. It's handy after raising **Release Age**, which only affects items collected from then on.

1. Enter the number of days. The default is your **Release Age** setting.
2. Clyde shows how many movies and episodes were released in that window. Click **Search** to start.
3. Only your scrapers are searched (Zilean and the NZB history are skipped), so it starts right away. Better releases are added to the Upgrades tab next to your last scan's results, to queue as usual or for **Auto Queue**.

It isn't limited by Fresh Release Search's cap and works even with it off. It searches up to 2,000 items per run, longest-unchecked first. If more were released in the window, run it again for the rest. Items with no known release date, or that aren't out yet, are left out.

---

## Upgrades tab

Individual movie and episode upgrade candidates.

**Filters:**

| Filter | Description |
|---|---|
| **Search** | Text or regex on title, filename, type, version |
| **Type** | All, Movies, Shows |
| **Recent Only** | Toggle to show only candidates indexed ≤90 days ago (configurable) |
| **Min Threshold slider** | Filter out candidates below this improvement % (0–200% in 5% steps) |

**Columns:**

| Column | Description |
|---|---|
| **Type** | `Movie` or `S##E##` episode badge |
| **Title** | Movie/show name with year |
| **Current / Best Candidate** | Current filename (muted) and candidate filename (highlighted) |
| **Version** | Release info with cache badges (see below) |
| **Score Δ** | Improvement % and before→after scores |
| **Size** | Current and candidate sizes in GB |

**Cache badges:**

| Badge | Meaning |
|---|---|
| **Live search** | Found by searching with your scrapers (Fresh Release Search or Search Recent Releases) |
| **Recent** | Candidate indexed ≤90 days ago |
| **Older · Xd ago** | Candidate age in days |
| **⚡ Cached Bypass** | Not in recent Zilean results, but kept because your debrid service reports it cached (only with **Only Show Recent Items** on) |
| **⚡ Cached** | Your debrid service reports the torrent cached |
| **✗ Not Cached** | Your debrid service reports the torrent not cached |

Cache status comes from services that can answer without adding the torrent: TorBox's cache check, or [Phalanx](phalanx-db.md) for Real-Debrid. On other providers, and for NZBs, no cache badge is shown and the release is checked when it's queued. **Auto Queue** queues cached candidates first and skips ones reported not cached, unless you accept uncached results.

**Actions:**

| Button | Description |
|---|---|
| **Queue Selected** | Add selected items to the upgrading queue |
| **Ignore Selected** | Dismiss — these candidates will be skipped in future scans |

Select all visible items with the **Select All** checkbox. Items are loaded in batches of 75 as you scroll.

![Upgrades tab](../assets/screenshots/features/upgrade-hub-upgrades.png)

---

## Season Packs tab

TV seasons where a complete season pack is available — often better than upgrading individual episodes.

**Additional columns:**

| Column | Description |
|---|---|
| **Show** | Show title and year |
| **Season** | Season number badge |
| **Collected** | Episodes collected / total with a progress bar |
| **Current / Best Pack** | Expandable list of current episode files, and the candidate pack filename |

Click the episode count button (e.g. `10 episodes`) to expand and see individual episode filenames and quality tags.

Same filters, cache badges, and Queue/Ignore actions as the Upgrades tab.

---

## Settings tab

### Upgrading

What happens right after a new release is collected. These used to be under Settings → Scraping and Settings → Queues & Upgrades.

| Setting | Default | Description |
|---|---|---|
| **Keep Searching After Collecting** | Off | Send newly collected recent releases to the Upgrading queue, where they're searched again every hour |
| **Release Age** | `7` days | Only items released this many days ago or less get the upgrade window when they're collected, including items found by the local library scan. Raise it to include older titles, but each one is searched hourly for the whole window, so large values add a lot of searches. Scans cover older items more cheaply. To check items you've already collected, use [Search Recent Releases](#search-recent-releases). |
| **Upgrade Window** | `24` hours | How long an item keeps being searched before it settles as Collected |
| **Score Improvement Needed** | `10%` | How much higher a release must score to replace the current file. Scans use it too. |
| **Stop at Score** | `0` | Items already scoring this or higher aren't searched again. `0` means no limit. |
| **One Extra Search After Release** | `0` days | Search once more this many days after release, when better encodes have usually appeared. `0` turns it off. |
| **Remove the Old Copy** | On | After an upgrade is collected, remove the original from the media server and the debrid service |

### Scans

| Setting | Default | Description |
|---|---|---|
| **Automatic Scan** | Off | Run a scan every 24 hours. This is the same switch as the **Upgrade Hub scan** task on the [Automation](automation.md) page. |
| **Score Threshold** | `0%` | Minimum improvement % to show a candidate. Applied to both Upgrades and Season Packs. |
| **Only Show Recent Items** | Off | Hide candidates older than the recent threshold from both tabs by default |
| **Recent Threshold** | `90` days | How many days back defines "recent" |
| **Fresh Release Search** | `30` days, `20` items | Each scan also searches your scrapers for up to this many items released within this many days, longest-unchecked first. `0` items turns it off. |
| **Scan Limit** | All | Max collected items the Zilean and NZB sources check per run — `100`, `500`, `1000`, `2000`, `5000`, or `All`. Fresh Release Search isn't affected. |
| **Auto Queue** | Off | Automatically queue candidates above the threshold after each scheduled scan. Respects Upgrades Per Run limit. |
| **Hide Episodes Already in Season Packs** | Off | Don't show individual episode upgrades in the Upgrades tab if they are already covered by a Season Pack candidate |
| **Upgrades Per Run** | `10` | Max items queued per category (upgrades and packs independently) per auto-queue run |
| **Excluded Genres** | — | Skip items from these genres during scan. Applies to movies and shows. |
| **Bulk Sources** | Both | Which whole-library sources to check: Zilean, NZB indexers, both, or none (Fresh Release Search only). Zilean is fast with its [direct DB connection](../scrapers/zilean.md#upgrade-hub-direct-db-connection) and slow without it. |
| **Exclude NAS Items** | Off | Skip items whose file path matches a configured NAS path prefix (set in Settings → Library & Files → Library → NAS / Network Drive Paths). NAS items will not be scanned or listed. |

**Settings actions:**

| Button | Description |
|---|---|
| **Save Settings** | Persist all settings |
| **Clear Hub Queue** | Revert hub-queued items back to Collected state |
| **Run Upgrade Cleanup** | Remove old files and torrents for all completed upgrades in the background |

---

## Activity tab

Log of all scan, queue, and upgrade processed events.

| Column | Description |
|---|---|
| **Date / Time** | Timestamp of the event |
| **Action** | Scan, Queue, or Upgrade Processed |
| **By** | System or username that triggered the action |
| **Result** | success, initiated, partial, or failed |
| **Details** | Summary stats for scans; title and from→to filenames for processed upgrades |

Filter by action type. Paginated at 50 entries per page. Auto-refreshes every 30 seconds on page 1.

![Upgrade Hub activity log](../assets/screenshots/features/upgrade-hub-activity.png)

---

## Upgrade process

When an item is queued for upgrade:

1. It enters the **Upgrading** queue state
2. Clyde adds the release the scan found (no new search is needed)
3. The new version is added to debrid or usenet and checked in
4. Once confirmed, the old version is removed if **Remove the Old Copy** is on in the Settings tab

If the release can't be added, the item goes back to Collected and that release is skipped in future scans.

The Upgrade Hub polls in the background and automatically removes rows for items that have been successfully upgraded.
