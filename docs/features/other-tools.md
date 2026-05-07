---
title: Other Tools
icon: material/tools
---

# Other Tools

A collection of smaller utility pages available in the navigation.

---

## Logs

Real-time log viewer with live streaming via Server-Sent Events.

**Controls:**

| Control | Description |
|---|---|
| **Log Level** | Filter by Debug, Info, Warning, Error, Critical |
| **Log Lines** | How many lines to load — 100, 500, 1000, 2000, 5000 |
| **Filter Logs** | Text input to pre-filter the stream before display |
| **Search** | Search through displayed logs with Enter/Shift+Enter to navigate matches — shows X/Y position |
| **Source chips** | Filter by source file group (queues, scraper, database, plex, trakt, etc.) — click Hide All/Show All to manage |
| **↓ Bottom** | Jump to the latest log entry (appears when you scroll up) |
| **Share Logs** | Uploads logs to a paste service and gives you a `wget` + `lnav` command for local viewing |

**Behaviour:**
- Auto-scrolls to the bottom when new logs arrive — pauses automatically when you scroll up
- Logs are colour-coded by level: Debug (blue), Info (green), Warning (orange), Error (red), Critical (purple)
- Duration values in log messages are highlighted in yellow
- Maximum ~1500 entries displayed at once for performance — older entries are removed automatically

---

## API Call Summary

Shows aggregated counts of outgoing API calls to external services, grouped by time period.

| Control | Description |
|---|---|
| **Time Frame** | Hourly, Daily, or Monthly |
| **Update** | Refresh the table after changing the time frame |

The table shows one row per time period and one column per domain (api.trakt.tv, api.real-debrid.com, api.github.com, etc.) with call counts. Useful for monitoring rate limit usage and quota consumption.

---

## Real-time API Calls

A live feed of every outgoing API call, updating approximately every second.

| Column | Description |
|---|---|
| **Timestamp** | When the call was initiated |
| **Domain** | Base URL of the service (e.g. `api.trakt.tv`) |
| **Endpoint** | Specific path called (e.g. `/users/settings`) |
| **Method** | HTTP verb — GET, POST, PUT, DELETE |
| **Status Code** | Response code (200, 401, 429, 500, etc.) |

Filter by domain using the dropdown. Useful for low-level debugging of external service interactions.

---

## Reverse Parser

Configures the default version assigned to releases when the parser cannot automatically identify a version from the filename or metadata.

| Setting | Description |
|---|---|
| **Default Version** | The version profile to assign as a fallback when parsing can't determine one automatically |

Configure this to ensure releases without clear version indicators still get assigned a sensible quality profile.

---

## Manual Blacklist

Manage a blacklist of media items by IMDb ID. Blacklisted items will not be re-added by content sources.

**Adding an item:**

1. Enter the IMDb ID (e.g. `tt1234567`)
2. Click **Add to Blacklist**

For TV shows, expand the row to see individual seasons — check/uncheck seasons to control which are blacklisted. Use **Shift+click** to select a range of seasons. Click **Save All Changes** to apply.

**Columns:** IMDb ID, Title, Year, Media Type, Seasons, Delete

---

## Trakt Friends

Authorise a friend's Trakt account so their watchlist can be used as a content source.

**Adding a friend:**

1. Ask your friend to create a Trakt API application at [trakt.tv/oauth/applications](https://trakt.tv/oauth/applications) and share their **Client ID** and **Client Secret**
2. Enter those credentials and click **Start Authorization**
3. A code and verification URL appear — your friend visits the URL and enters the code
4. Authorization completes within 60 seconds — a countdown timer shows the remaining time

**Authorised friends list:** Shows friend name, Trakt username, and token expiry. Use **Refresh Token** to renew an expired token, or **Delete** to remove access.

---

## Plex User Tokens

Collect Plex authentication tokens from other users so their libraries or watchlists can be used as content sources.

**How it works:**

1. Click **Generate User Login Link**
2. A code and auth URL are generated
3. Send the link to the other user — they visit it and sign in to their Plex account
4. Once authorised, their username and token appear in the **Stored Tokens** list

Tokens are stored locally in a JSON file. The page polls every 5 seconds and times out after 5 minutes if the user doesn't complete auth.

!!! warning "Security"
    Anyone with a stored token has access to that user's Plex data. Ensure your server is properly secured.

---

## Symlink Tools

Manually create a symlink for a media file using custom metadata — useful for files that cli_debrid couldn't automatically match.

**How to use:**

1. Enter or browse to the **Source File Path**
2. Click **Validate File** to confirm it exists
3. Fill in: Title, Year, Media Type, Version, IMDb/TMDB ID (optional), Content Source
4. For TV episodes: Season Number, Episode Number, Episode Title (optional)
5. Click **Preview Symlink Path** to see the generated path before committing
6. Click **Create Symlink** to create it

The file browser lets you navigate your mount directories to find files. Media file extensions (`.mkv`, `.mp4`, `.avi`, etc.) are highlighted.

Current symlink settings (original files path and symlink base path) are shown at the top of the page.

---

## Metadata Debug

View, recreate, or delete metadata entries in the battery database for a specific item.

**How to use:**

1. Enter an IMDb ID (e.g. `tt1234567`)
2. Click **Fetch** to display the current metadata

**Actions:**

| Button | Description |
|---|---|
| **Fetch** | Retrieve and display the current metadata entry |
| **Recreate** | Delete the existing entry and re-fetch fresh metadata from the source |
| **Delete** | Remove the metadata entry without re-fetching |

Results are displayed as formatted, collapsible JSON blocks for Item, Metadata, and Seasons. Each nested object or array can be expanded or collapsed individually using the **+** / **−** buttons to the left of the key. Recreate and Delete require confirmation before executing.

---

## Torrent Status

Shows near real-time activity from your debrid service.

**Active Downloads** — torrents currently downloading, with name, progress percentage, speed, and state (Downloading, Waiting, Seeding).

**Recently Completed** — the 10 most recently finished torrents. Click **Show More** to expand the full list, **Show Less** to collapse back to 10.

---

## Magnet Assign

Manually assign a magnet link or `.torrent` file to a specific movie or TV show in your library. Useful when the automatic scraper can't find a torrent but you have one sourced manually.

**How to use:**

1. Search for the title by name using the search form
2. Select the correct result from the search results
3. For TV shows, choose a **Selection Type**:
    - **Full Series** — assigns the magnet to the entire show
    - **Season Pack** — select one or more seasons
    - **Single Episode** — select a specific season and episode
4. Paste a magnet link or upload a `.torrent` file
5. Select a **Version** (quality profile)
6. Click **Assign**

**Layout:**

On desktop, TV show pages display the **Selection Type** panel and the **Magnet Link / Torrent File** panel side by side in two columns for a more compact view. On mobile, these stack vertically and the show's backdrop image is used instead of the poster for a better small-screen experience.

**Opening from Library or Discover:**

The magnet assign button (orange magnet icon) appears directly on season headers and individual episode rows in both the **Library show detail page** and the **Discover show detail page**. Clicking it opens Magnet Assign pre-filled with the correct show, season, episode, and version — no manual selection needed.
