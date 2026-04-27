---
title: Additional Settings
icon: material/dots-horizontal
---

# Additional Settings

---

## TMDB

| Setting | Description |
|---|---|
| **API Key** | Your TMDB API key — enables poster art, discover, and trending features |
| **Enable Discovery** | Show the Discover page powered by TMDB |

!!! tip "Getting a TMDB API key"
    Register at [themoviedb.org](https://www.themoviedb.org/), go to your account **Settings → API**, and request a free API key.

---

## TVDB

| Setting | Default | Description |
|---|---|---|
| **API Key** | — | TVDB v4 API key. When set, uses TVDB instead of Trakt for TV metadata lookups. A TMDB API key is also required for full release date support. Get a key at [thetvdb.com/api-information](https://thetvdb.com/api-information). |

---

## MDBList

| Setting | Default | Description |
|---|---|---|
| **API Key** | — | MDBList API key — enables curated lists from IMDB, Trakt, Netflix, Disney+, and more on the Discover page. Get your key at [mdblist.com/preferences](https://mdblist.com/preferences/). |
| **Cache Duration (hours)** | `24` | How long to cache MDBList data. Lower values give fresher data but use more API calls. Min: 1, Max: 168. |

---

## Queue

| Setting | Default | Description |
|---|---|---|
| **Queue Sort Order** | `None` | Sort order for the scraping queue — `None`, `Movies First`, or `Episodes First` |
| **Sort By Release Date (desc)** | Off | Apply secondary sorting by release date (newest first) after primary sort. Items with unknown dates appear last. |
| **Content Source Priority** | — | Comma-separated priority order for content sources in the scraping queue, e.g. `Plex,Trakt,Overseerr`. Unlisted sources are processed last. |
| **Wake Limit** | `24` | Number of times to wake a sleeping item before blacklisting it |
| **Sleep Duration (minutes)** | `30` | How long an item sleeps between wake attempts |
| **Blacklist Final Scrape Delay (hours)** | `0` | Hours to wait before performing one final scrape attempt after an item would normally be blacklisted. Set to `0` to disable. |
| **Movie Airtime Offset (hours)** | `0` | Hours after midnight to start scraping for new movies |
| **Episode Airtime Offset (hours)** | `0` | Offset from the show's airtime to start scraping new episodes. Positive = delay, negative = scrape early. Requires Trakt login for accurate airtime. |
| **Blacklist Duration (days)** | `30` | Days after which blacklisted items are automatically removed for a re-scrape (if unblacklisting is enabled) |
| **Enable Pause Schedule** | Off | Pause the queue during a scheduled time window |
| **Pause Start Time** | `00:00` | Start time for the scheduled queue pause (HH:MM) |
| **Pause End Time** | `00:00` | End time for the scheduled queue pause (HH:MM) |
| **Main Loop Sleep (seconds)** | `0.0` | Minimum delay between task executions to reduce system load |
| **Item Process Delay (seconds)** | `0.0` | Artificial delay after processing each item in Scraping/Adding queues to reduce peak CPU usage |
| **Pre-Release Scrape Days** | `0` | Days before a movie's release date to start scraping. Set to `0` to disable. |

---

## System Load Regulation

Automatically adjusts the queue sleep time based on current CPU and RAM usage.

| Setting | Default | Description |
|---|---|---|
| **CPU Threshold (%)** | `75` | CPU usage percentage that triggers increased sleep time |
| **RAM Threshold (%)** | `75` | RAM usage percentage that triggers increased sleep time |
| **Regulation Increase Step (seconds)** | `1.0` | How much to increase sleep duration when load is high |
| **Regulation Decrease Step (seconds)** | `1.0` | How much to decrease sleep duration when load returns to normal |
| **Regulation Max Sleep (seconds)** | `60.0` | Maximum sleep time auto-regulation can set |

---

## Library Manager

| Setting | Default | Description |
|---|---|---|
| **Ghostlist Mode** | Off | Add shows and movies to the ghostlist when deleted to prevent them from being re-added. When enabled, deleting content marks it as ghosted in the database. When disabled, deleted content can be re-added by dynamic content sources. |
| **Remove From Content Sources** | Off | Remove items from content sources (Trakt lists, Overseerr requests, Plex Watchlist, etc.) during deletion. Prevents items from being automatically re-added, but makes deletion slower. **Tip:** Enable when Ghostlist Mode is OFF. Disable when Ghostlist Mode is ON — ghostlist already prevents re-addition and disabling makes deletion much faster. |

### Clear Artwork Cache

Remove all cached posters and backdrops. Artwork will be re-downloaded from TMDB on the next library load. Use the **Clear Cache** button to trigger this.

---

## Discover Settings

| Setting | Default | Description |
|---|---|---|
| **Hide No Rating** | Off | Hide items without a rating from Discover results |
| **Hide No Poster** | Off | Hide items without a poster image from Discover results |
| **Only Show Missing** | Off | Only show items not already in your library |
| **TV Show Episode View** | `discover` | Where to navigate when clicking a TV show not in the library — `discover` (details page) or `add_media` |

---

## Overlay Settings

| Setting | Default | Description |
|---|---|---|
| **Overlays Enabled** | Off | Enable the poster overlay system. When enabled, overlay sync tasks run automatically and apply media info badges to Plex posters. Requires Plex URL and token. |
| **Plex Data Path** | — | Path to the Plex Media Server data directory (e.g. `/config/Library/Application Support/Plex Media Server`). Required for the poster cleanup task. |
| **Overlay Content Check Interval (days)** | `7` | How often to re-fetch ratings and show status to detect changes that should trigger an overlay refresh. Set to `0` to check on every sync run. |
| **Sync Items Per Run** | `200` | Maximum number of items to process per overlay sync run. Higher values clear backlogs faster but each run takes longer. |

---

## Bazarr Integration

Spoof cli_debrid as Radarr/Sonarr so Bazarr can automatically download subtitles for your library.

| Setting | Default | Description |
|---|---|---|
| **Enable Bazarr Spoofing** | Off | Enable the Bazarr integration spoof |
| **API Key** | — | API key used to authenticate Bazarr. Use the Generate button to create one. |
| **Service Type** | `Auto (Both)` | Which service to spoof — Auto (Both), Radarr Only, or Sonarr Only |
| **Spoofed Version** | `5.14.0.9383` | Version string reported to Bazarr |

---

## Phalanx DB Settings

Distributed hash-based duplicate detection across multiple cli_debrid instances.

| Setting | Default | Description |
|---|---|---|
| **Enable Phalanx DB** | Off | Enable the Phalanx DB peer network |

!!! note
    Phalanx DB is optional and can be disabled with no impact to core functionality. Requires a program restart when toggled.

---

## Symlink Settings

Controls how symlink filenames and folder structures are built. Only applies in Symlink mode.

| Setting | Default | Description |
|---|---|---|
| **Symlink Movie Template** | `{title} ({year})/{title} ({year}) - {imdb_id} - {version} - ({original_filename})` | Template for movie symlink names. Variables: `{title}`, `{year}`, `{imdb_id}`, `{tmdb_id}`, `{quality}`, `{original_filename}` |
| **Symlink Episode Template** | `{title} ({year})/Season {season_number:02d}/{title} ({year}) - S{season_number:02d}E{episode_number:02d} - {episode_title} - {imdb_id} - {version} - ({original_filename})` | Template for episode symlink names. Variables: `{title}`, `{year}`, `{imdb_id}`, `{tmdb_id}`, `{season_number}`, `{episode_number}`, `{episode_title}`, `{version}`, `{original_filename}` |
| **Organize By Resolution** | Off | Add a resolution subfolder to the symlink structure |
| **Organize By Version** | Off | Add a version subfolder to the symlink structure |
| **Symlink Folder Order** | `type,version,resolution` | Drag-to-reorder the folder hierarchy for symlink organisation |
| **Enable Separate Anime Folders** | Off | Create separate folders for anime content |
| **Enable Separate Documentary Folders** | Off | Create separate folders for documentary content |
| **Movies Folder Name** | `Movies` | Custom name for the Movies folder |
| **TV Shows Folder Name** | `TV Shows` | Custom name for the TV Shows folder |
| **Anime Movies Folder Name** | `Anime Movies` | Custom name for the Anime Movies folder |
| **Anime TV Shows Folder Name** | `Anime TV Shows` | Custom name for the Anime TV Shows folder |
| **Documentary Movies Folder Name** | `Documentary Movies` | Custom name for the Documentary Movies folder |
| **Documentary TV Shows Folder Name** | `Documentary TV Shows` | Custom name for the Documentary TV Shows folder |

---

## Subtitle Settings

!!! info "Scheduled task"
    **Process Bulk Subtitles** runs automatically every **1 hour** by default. Adjust the interval or trigger manually in the [Task Manager](../features/task-manager.md) under the **Features** tab.

Symlink mode only. Adds ~2–3s overhead per file.

| Setting | Default | Description |
|---|---|---|
| **Enable Subtitle Downloads** | Off | Enable automatic subtitle downloading (Symlink mode only) |
| **OpenSubtitles Username** | — | Your OpenSubtitles account username |
| **OpenSubtitles Password** | — | Your OpenSubtitles account password |
| **Subtitle Languages** | `eng,zho` | Comma-separated ISO-639-3 language codes, e.g. `eng,fra,spa` |
| **Probe for Embedded Subtitles** | Off | Use ffprobe to check for embedded subtitles before searching externally |

---

## Custom Post-Processing Settings

Run a custom script after an item is collected.

| Setting | Default | Description |
|---|---|---|
| **Enable Custom Script** | Off | Run a custom script during post-processing |
| **Custom Script Path** | — | Absolute path to the script to run |
| **Custom Script Arguments** | `{title} {imdb_id}` | Arguments passed to the script. Available variables: `{title}`, `{year}`, `{type}`, `{imdb_id}`, `{location_on_disk}`, `{original_path_for_symlink}`, `{state}`, `{version}` |

---

## AI Assistant

An AI assistant powered by OpenClaw. See the [AI Butler feature guide](../features/ai-butler.md) for full details.

!!! tip "Paid AI API recommended"
    Works best with a paid AI API (e.g. OpenAI, Anthropic, Gemini). Free tier models may lack the context window or tool-calling capability needed for reliable responses.

| Setting | Default | Description |
|---|---|---|
| **Enable AI Butler** | Off | Enable the AI Butler chat widget on all pages. Requires OpenClaw to be installed and configured. |
| **OpenClaw URL** | — | URL of your OpenClaw instance, e.g. `http://192.168.1.x:18789`. OpenClaw handles AI provider selection and session memory. |
| **OpenClaw Token** | — | Bearer token for OpenClaw authentication. Leave blank if OpenClaw has no auth configured. |
| **Agent ID** | `main` | OpenClaw agent ID to use |
| **Health Notifications** | On | Send proactive alerts via your notification channels when the AI Butler detects issues (stuck queues, high blacklist rate, errors, etc.) |
| **Health Check Interval (seconds)** | `900` | How often the AI Butler runs background health checks. Minimum 300 (5 minutes). Default 900 (15 minutes). |
| **Settings Assistant** | On | Allow the AI to read your full settings schema and suggest or apply configuration changes via chat. When enabled, the AI can send `APPLY_SETTING` blocks that let you update settings with a single click. Disabling means the AI will still answer questions but cannot propose or apply setting changes — useful for a read-only assistant. |
| **Proactive Notifications** | On | Allow the AI Health Monitor to run background checks every few minutes and push plain-English alerts to your notification channels (Telegram, Discord, etc.) when it detects problems such as stuck queues, high blacklist rates, excessive errors, or a large database. Disabling stops all automatic health checks and alerts — you can still ask the AI about health manually in the chat. |
| **Content Recommendations** | On | Allow the AI to recommend content based on your watch history and collected library, and add items directly to your wanted list via chat with a single click. When enabled, the AI receives a summary of your recently watched and collected titles. Disabling removes watch/library context from the AI prompt and disables the add-to-library action. |
| **Habit Learning** | On | Record significant user actions (running wanted sources, triggering upgrade scans, pausing queues, adding library items) in the background and surface pattern summaries to the AI. Disabling stops all habit recording and removes the pattern summary from the AI context — no data is deleted, it just won't be updated or shown to the AI. |
| **Share Full Config with AI** | On | When enabled, the AI receives your full configuration (up to 15 000 chars), extended log tails (up to 20 000 chars), upgrade activity history, and recent notification logs. Secrets (API keys, tokens, passwords) are always redacted. When disabled, the AI only receives a short config excerpt (2 000 chars) and a brief log tail (3 000 chars). |
| **Apply Plex Label** | Off | Apply a Plex label to items added to your library via the AI Butler |
| **Label Mode** | `Fixed Label` | How the label is determined — currently Fixed Label |
| **Fixed Label** | `AI Butler` | Label applied to all AI Butler additions. Comma-separated for multiple labels. |

### OpenClaw Skill File

Click **Download SKILL.md** to download a pre-configured OpenClaw skill file with your URL and API token already filled in. Drop it into `~/.openclaw/skills/` on your OpenClaw machine, then reload OpenClaw. Your agent will then be able to answer questions about your library from external messengers like Telegram or Discord.

!!! warning "Security note"
    This skill requires cli_debrid to be publicly accessible — it cannot work via an internal IP only. Exposing cli_debrid publicly means anyone with your token can control it, so **User Management must be enabled** before downloading. For best security, use OIDC/SSO (e.g. Authentik) rather than local accounts.

---

## Plex Smart Collection Posters

Applies custom designed posters to Plex's built-in smart collections. See the [Plex Smart Collection Posters](../features/plex-smart-collections.md) feature guide for full details.

| Setting | Default | Description |
|---|---|---|
| **Enable** | Off | Enable automatic poster application to Plex smart collections |
| **Poster Design** | Plex Default | Layout applied to all enabled collections (Plex Default, Layout 1–5) |
| **Poster Accent Color** | — | Accent color for the poster. Leave unset to use each layout's built-in default |
| **Eyebrow Text** | — | Small text above the collection title on the poster. Leave blank to hide |
| **Poster Icon** | — | Icon displayed on the poster. Defaults to the CLI Debrid icon |
| **Card Overlay Opacity** | 60% | Darkness of the gradient fade at the bottom of each card thumbnail |
| **Accent Glow Opacity** | 80% | Brightness of the accent color glow on the poster background |
| **Accent Glow Radius** | 55 | How far the accent color spreads across the poster (range 10–200) |
| **Per-collection toggles** | — | Individual on/off switches for each discovered Plex smart collection |

---

## Plex Movie Box Sets

Automatically discovers TMDB franchise memberships for your movies, creates matching Plex collections, applies franchise posters, and optionally queues missing franchise movies. See the [Plex Movie Box Sets](../features/plex-movie-box-sets.md) feature guide for full details.

| Setting | Default | Description |
|---|---|---|
| **Enable** | Off | Enable automatic box set collection management |
| **Grab Missing Movies** | Off | Add missing franchise movies to the wanted queue |
| **Version to Grab** | Default | Quality/version used when grabbing missing movies |
| **Collection Name Pattern** | `{title} Collection` | Template for Plex collection names. `{title}` = franchise name. Examples: `{title} Box Set`, `{title} Saga` |
| **Minimum Owned Movies** | 2 | Minimum owned movies to create or keep a collection. Collections that drop below this are automatically removed from Plex |
| **Collection Sort Order** | Release Date | How movies are ordered inside the Plex collection (Release Date, Title, Custom) |
