---
title: Advanced Settings
icon: material/tune
---

# Advanced Settings

Configure advanced and debug options.

---

## System & Logging

| Setting | Default | Description |
|---|---|---|
| **Logging Level** | `DEBUG` | Logging level for console output and file logging |
| **Timezone Override** | — | Override system timezone (e.g. `America/New_York`). Leave empty to use system timezone. |
| **Check For Updates** | On | Check for updates and display update indicator in the header |
| **Enable Tracemalloc** | Off | Enable Python's tracemalloc for detailed memory usage tracking per task. Adds overhead — use only for debugging memory leaks. |
| **Tracemalloc Sample Rate** | `100` | Sample rate for tracemalloc (1 in X tasks). Lower values give more frequent data but increase overhead. |

---

## Library Management

| Setting | Default | Description |
|---|---|---|
| **Skip Initial Plex Update** | Off | Skip Plex initial collection scan on startup |
| **Enable Plex Removal Caching** | On | Enable caching of Plex removal operations before executing them |
| **Plex Removal Cache Delay (Minutes)** | `360` | Delay in minutes before processing a cached Plex removal operation |
| **Cinesync Path** | — | Absolute path to your CineSync MediaHub `main.py` file |
| **Enable Unmatched Items Check** | On | Enable checking and fixing of unmatched or incorrectly matched items in Plex during collection scans |
| **Enable Library Maintenance Task** | Off | Run the library maintenance task periodically. This is a destructive process — use with caution. |

---

## Content Processing

| Setting | Default | Description |
|---|---|---|
| **Do Not Add Plex Watch History Items To Queue** | Off | Do not add Plex watch history items to the queue |
| **Item Process Delay (Seconds)** | `0` | Pause between processing each queue item. Useful to reduce API rate limiting. |
| **Disable Content Source Caching** | Off | Disable content source caching |
| **Enable Granular Version Additions** | On | Enable granular version additions for Wanted items |

---

## Queue & Upgrade Management

| Setting | Default | Description |
|---|---|---|
| **Sort By Uncached Status** | Off | Sort results by uncached status over cached status |
| **Checking Queue Period** | `3600` | Max time (in seconds) before moving items from the Checking queue back to Wanted |
| **Ignore Wanted Queue Throttling** | Off | Allow the Wanted queue to move all eligible items to Scraping regardless of queue size. Use with caution. |
| **Disable Not Wanted Check** | Off | Disable the not-wanted check for items in the queue |
| **Staleness Threshold (Days)** | `7` | Number of days before metadata is considered stale |
| **Allow Partial Overseerr Requests** | Off | Allow partial show requests from Overseerr |
| **Max Upgrading Score** | `0.0` | Upgrades are disabled once this score is reached. Set to `0` to disable the limit. |
| **Upgrade Queue Duration (Hours)** | `24` | How long to keep items in the upgrade queue before moving them to Collected state |
| **Only Current File** | Off | Only process subtitles for the current file being processed instead of scanning all folders |
| **Enable Library Maintenance Task** | Off | Enable the periodic library maintenance task |

---

## Filtering & Blacklist

| Setting | Default | Description |
|---|---|---|
| **Filename/Folder Name Filter Out List** | — | Comma-separated list of filenames or folder names to filter out |
| **Sanitizer Replacement Character** | `_` | Character used when replacing invalid characters in filenames. Must be valid on both Windows and Linux. |
| **Enable Unblacklisting** | On | Automatically unblacklist items after their blacklist duration expires |
| **Blacklist Duration (Days)** | `7` | How long a failed torrent stays blacklisted before it can be retried |
| **Unblacklisting Cutoff Date** | — | Only unblacklist items with a release date after this date (`YYYY-MM-DD`) or within the last X days (e.g. `30`). Leave empty to process all. |

---

## Notifications & Display

| Setting | Default | Description |
|---|---|---|
| **Truncate Episode Notifications** | Off | Show only the first episode and a summary count in notifications instead of listing all episodes |
| **Enable Detailed Notification Information** | Off | Include content source and content source details in notifications |

---

## Watchlist Management

| Setting | Default | Description |
|---|---|---|
| **Plex Watchlist Removal** | Off | Remove items from Plex Watchlist when collected (My Plex Watchlist and Other Plex Watchlist sources only) |
| **Plex Watchlist Keep Series** | Off | When removing collected items from Plex Watchlist, keep series — only remove movies |
| **Trakt Watchlist Removal** | Off | Remove items from Trakt Watchlist when collected |
| **Trakt Watchlist Keep Series** | Off | When removing collected items from Trakt Watchlist, keep series — only remove movies |

---

## Symlink & Naming

| Setting | Default | Description |
|---|---|---|
| **Symlink Movie Template** | `{title} ({year})/{title} ({year}) - {imdb_id} - {version} - ({original_filename})` | Template for movie symlink names. Variables: `{title}`, `{year}`, `{imdb_id}`, `{tmdb_id}`, `{quality}`, `{original_filename}` |
| **Symlink Episode Template** | `{title} ({year})/Season {season_number:02d}/...` | Template for episode symlink names. Variables: `{title}`, `{year}`, `{imdb_id}`, `{tmdb_id}`, `{season_number}`, `{episode_number}`, `{episode_title}`, `{version}`, `{original_filename}` |
| **Anime Renaming Using AniDB** | Off | Use AniDB to rename anime episodes instead of Trakt metadata (symlink mode only) |
| **Enable Separate Anime Folders** | Off | Create separate folders for anime content when organising symlinks |
| **Enable Separate Documentary Folders** | Off | Create separate folders for documentary content when organising symlinks |
| **Movies Folder Name** | `Movies` | Custom name for the Movies folder |
| **TV Shows Folder Name** | `TV Shows` | Custom name for the TV Shows folder |
| **Anime Movies Folder Name** | `Anime Movies` | Custom name for the Anime Movies folder |
| **Anime TV Shows Folder Name** | `Anime TV Shows` | Custom name for the Anime TV Shows folder |
| **Documentary Movies Folder Name** | `Documentary Movies` | Custom name for the Documentary Movies folder |
| **Documentary TV Shows Folder Name** | `Documentary TV Shows` | Custom name for the Documentary TV Shows folder |
| **Allow Symlinks on Windows** | Off | Allow symlinks on Windows. Requires administrator privileges or Developer Mode. |

---

## Scraping & Scoring

| Setting | Default | Description |
|---|---|---|
| **Ultimate Sort Order** | `None` | Override quality score sorting to order results by file size instead |
| **Soft Max Size GB** | Off | Apply the assigned max size to results, but if no results are returned accept the smallest available |
| **Sort By Uncached Status** | Off | Sort results by uncached status over cached status |
| **Emphasize Number Of Items Over Quality** | On | Prioritise quantity of results over quality when ranking |
| **Delayed Scrape Based On Score** | Off | Only accept results above the minimum scrape score for a set period before accepting lower-scored releases |
| **Delayed Scrape Time Limit (Hours)** | `6.0` | How long to enforce the minimum scrape score before accepting lower results |
| **Minimum Scrape Score** | `0.0` | Minimum score threshold for accepting results |
| **Scale Final Scores** | Off | Scale final scores to a range of 0–100 |

---

## Scraping Strategy

| Setting | Default | Description |
|---|---|---|
| **Enable Reverse Order Scraping** | Off | Scrape items in reverse order |
| **Enable Alternate Scraping Time Strategy** | Off | Instead of scraping based on queue offsets/airtime/release date, scrape all items with release dates within the past 24 hours of a set daily time |
| **Alternate Scrape Time (24h format)** | `00:00` | Daily scrape time (HH:MM) used when the alternate strategy is enabled |
| **Skip Initial Multi-Scrape For New Content** | Off | Skip the initial multi-provider scrape for content released within the past 7 days |

---

## Testing & Development

!!! warning
    These settings should not typically be changed unless troubleshooting specific issues or instructed by support. Changing them can affect system stability and performance.

| Setting | Default | Description |
|---|---|---|
| **Enable Crash Test** | Off | Enable crash testing functionality |
