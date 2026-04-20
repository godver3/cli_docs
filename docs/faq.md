---
title: FAQ
icon: material/frequently-asked-questions
---

# Frequently Asked Questions

---

## Setup & Installation

**Do I need all the API keys to get started?**

The minimum required is: a debrid API key, Plex or Jellyfin URL + token, and a TMDB API key. Trakt is required for metadata lookups and most content sources. TVDB is optional (used instead of Trakt for TV metadata if configured).

---

**Which Docker image tag should I use?**

Always use `godver3/cli_debrid:dev`. The `:latest` tag does not include all features or receive new feature updates.

---

**What TMDB API key format do I need?**

Use the **API Key (v3 auth)** from your TMDB account settings — not the Read Access Token. Go to [themoviedb.org](https://www.themoviedb.org/) → Settings → API.

---

**The onboarding wizard isn't completing / settings aren't saving**

- Make sure all required fields are filled in (debrid key, Plex URL, TMDB key, Trakt)
- Click **Validate** on the debrid key before saving
- Check the Logs page for any errors during save

---

**Can I run cli_debrid on ARM / Raspberry Pi?**

Yes, ARM builds are available. Use the same `godver3/cli_debrid:dev` image — it supports `linux/arm64`.

---

**How do I enable multi-user access?**

Go to **Settings → UI Settings → System Behavior → Enable User System**. Then manage users under **Manage Users** in the sidebar.

---

## Plex & Jellyfin

**Plex isn't picking up new content after it's downloaded**

- Verify the mount path is accessible inside the Plex container (volumes must match exactly)
- Enable **Scan my library automatically** and **Run a partial scan when changes are detected** in Plex → Settings → Library
- For Zurg users: ensure `plex_update.sh` is configured and executable
- Manually trigger a scan: Library → ⋮ → **Scan Library Files**

---

**Items appear in cli_debrid as Collected but aren't showing in Plex**

- Check that the mount path inside the Plex container matches exactly what cli_debrid uses
- In symlink mode, both containers must mount the debrid storage and symlink folder at **identical paths**
- Force a Plex library scan manually

---

**Wrong metadata / wrong show matched in Plex**

- Use **Fix Incorrect Match** in Plex (right-click the item) and search manually
- Common with titles that share names or anime with non-standard naming
- For anime: consider enabling **Anime Renaming Using AniDB** in Additional Settings → Symlink Settings

---

**Plex library sync is taking a very long time**

- Full Plex scans on large libraries can take hours — this is normal
- Use **Run a partial scan when changes are detected** to reduce scan time for new additions
- The Plex Labels full sync (5000+ items) takes 13–14 hours — run overnight

---

**How do I find my Plex token?**

1. Open [Plex Web](https://app.plex.tv) → browse to any item → ⋮ → **Get Info** → **View XML**
2. Copy the value after `X-Plex-Token=` in the URL bar

See [Plex integration](integrations/plex.md#finding-your-plex-token) for full details.

---

## Debrid & Scraping

**Items are stuck in the Checking state**

Checking means cli_debrid is waiting for the file to appear at the mount path. Common causes:

- The debrid torrent is uncached — it needs to download first (can take hours)
- The mount path isn't accessible inside the container
- Zurg/rclone isn't running or the mount is stale — try remounting

Items stay in Checking for up to 1 hour before being moved back. For uncached content, set **Uncached Content Handling** to `Hybrid` in **Settings → Versions → Other Scraping Settings**.

---

**Items keep getting blacklisted / cycling without downloading**

- The torrent was found but failed verification — check if the mount path is accessible
- All known torrents for that item may be blacklisted — use **Rescrape** to retry with a fresh search
- Check logs for "no suitable video files" errors — the torrent may not contain the right files

---

**Real-Debrid API rate limiting / temporary ban**

RD has a 400GB/day bandwidth limit and API rate limits. To reduce calls:

- Lower the **Main Loop Sleep** interval in Advanced Settings → Queue
- Disable unnecessary scrapers
- Check **Monitoring → Rate Limit State** in Debug Functions to see current counts

---

**Scraper returning no results / timing out**

- Check **Connections** page — is the scraper showing as reachable?
- Use the [Scraper Tester](features/scraper-tester.md) to run a test search and see what's returned
- For Jackett: verify the API key and that Jackett can reach the trackers
- For public scrapers (Torrentio, Zilean): URLs change periodically — check Discord for current URLs

---

**"No suitable video files" error**

The torrent was added to debrid but contained no valid video files (e.g. only RAR archives, samples, or NFO files). The item will be blacklisted for that torrent and retry with another. Add `RAR` and `.nfo` to your Filter Out list in Version Settings to avoid these.

---

**How do I use uncached content?**

In **Settings → Versions → Other Scraping Settings**, set **Uncached Content Handling** to `Hybrid` (tries cache first, falls back to uncached if nothing found) or `Full` (always takes the best result regardless of cache status). Note: uncached downloads can take hours.

---

## Queue & States

**What do the queue states mean?**

| State | Meaning |
|---|---|
| **Wanted** | Waiting to be scraped next cycle |
| **Scraping** | Actively searching for torrents |
| **Adding** | Torrent found, being submitted to debrid |
| **Checking** | Waiting for the file to appear at the mount |
| **Collected** | Successfully in your library |
| **Sleeping** | All known torrents blacklisted — retrying after delay |
| **Unreleased** | Not yet released — will move to Wanted on release date |
| **Pending Uncached** | Waiting for uncached download slot |
| **Upgrading** | Looking for a better quality version |

---

**Items are showing as Unreleased but they've already been released**

Release dates may be outdated in the database. Go to **Debug Functions → Library → Refresh Release Dates** to re-fetch dates from TMDB.

---

**How do I move items stuck in Sleeping back to Wanted?**

1. Go to **Debug Functions → Library → Bulk Queue Actions**
2. Select **Source Queue = Sleeping**
3. Select All → Move to **Wanted**

Or use the **Database Browser**, filter by State = Sleeping, select all, and Move to Queue → Wanted.

---

**How does blacklisting work?**

When a torrent fails (wrong files, download error, mismatch), it's added to the blacklist for that item. cli_debrid won't try that torrent again until the **Blacklist Duration** expires (default 30 days). Items with all torrents blacklisted move to **Sleeping**. Use **Rescrape** to force a fresh search.

---

**The program stopped running / queue isn't processing**

- Check the program is running (▶ button in the top right should show as running)
- Check **Logs** for crash errors
- If using **Auto Run Program** in UI Settings, verify it's enabled
- Restart the container if needed

---

## Anime

**Anime episodes have wrong season/episode numbers**

Anime uses absolute episode numbering on some sources but Plex expects season-based. Solutions:

- Enable **Anime Renaming Using AniDB** in Additional Settings → Symlink Settings (symlink mode only)
- Enable **Enable Separate Anime Folders** to keep anime in its own folder structure
- Lower the **Similarity Threshold (Anime)** in Version Settings (default 0.80) if matches are being rejected

---

**Anime requests from Overseerr have wrong episode counts**

This is a known issue — Overseerr uses TMDB metadata which sometimes has incorrect season/episode counts for anime. The item may need to be manually searched or requested by IMDB ID.

---

**Nyaa scraper not returning results**

- Nyaa requires no setup — it's a public tracker, just enable it
- Check the **Scraper Tester** with an anime title to verify results
- Some anime titles need the **Use Alternative Titles** option enabled in Version Settings

---

**Non-English filenames (Chinese characters, etc.) failing**

Enable the **Sanitizer Replacement Character** in Advanced Settings → File System to replace unsupported characters. Make sure your filesystem supports Unicode filenames.

---

## Integrations

**Overseerr/Seerr requests aren't being picked up**

- Verify the Seerr content source is enabled in Settings → Content Sources
- Check the URL (`http://YOUR_SEERR_IP:5055`) and API key are correct
- Set up the **webhook** for instant pickup: in Seerr go to Settings → Notifications → Webhook → set URL to `http://YOUR_CLI_DEBRID_IP:5000/webhook` and enable **Request Approved**
- Without the webhook, cli_debrid checks Seerr every ~60 seconds

---

**Overseerr status isn't updating to "Available" after download**

- Make sure Seerr has your Plex libraries synced (Settings → Plex → Sync Libraries)
- Include your Debrid libraries (`Movies-DB`, `TV Shows-DB`) in the sync
- Trigger a Plex scan so Seerr sees the new content

---

**Zurg mount is empty or showing stale content**

- Verify Zurg is running: `docker compose logs zurg`
- Verify rclone is running: `docker compose logs rclone`
- Check `rclone.conf` has the correct Zurg WebDAV URL
- If the mount is stuck: `fusermount -uz /your/mount/path` then remount
- On Unraid: use the actual pool path (e.g. `/mnt/cache/zurg`) not `/mnt/user/zurg`

---

**Zurg/rclone files take 20–30 seconds to appear after being added**

This is normal — rclone's directory cache needs to refresh. Reduce `--dir-cache-time` in your rclone mount command (e.g. `10s`) to speed this up, at the cost of slightly more API calls.

---

**Decypharr vs Zurg — which should I use?**

Both expose your debrid library as a local mount. Zurg is Real-Debrid specific and very mature. Decypharr supports multiple debrid providers. Use Zurg if you're on Real-Debrid; use Decypharr for AllDebrid, Torbox, or multi-provider setups.

---

**Trakt 401 errors / deactivated account**

- Go to Settings → Required Settings → click **Authorise Trakt** again to refresh the OAuth token
- Trakt tokens expire and need periodic re-authorisation

---

## Overlays & Plex Labels

**Overlays aren't being applied to some items**

- Run **Sync Library** on the Overlays page to match database items to Plex entries
- Use **Debug Functions → Test Plex Item Lookup** to check if cli_debrid can find the item in Plex
- Items without IMDB/TMDB IDs won't sync — use **Fix Missing IMDb ID** in Debug Functions
- The title+year fallback handles items without external IDs, but requires a good title match

---

**Overlays stopped working after updating**

- Re-run **Sync Library** from the Overlays page
- Check the Overlay Settings — ensure **Enable Overlay System** is still on
- If you migrated from Kometa/PMM, use **Reset All Posters** first to clear foreign overlays

---

**Plex labels show "Unknown" instead of requester names**

Run **Backfill Plex Labels Content Source Detail** from Debug Functions → Run Task Manually. This queries Overseerr to fill in the actual requester names.

---

**Plex labels aren't appearing on new items**

Labels are applied automatically when items are collected. If they're missing:

- Run **Backfill Missing Labels** from Debug Functions
- Verify labels are enabled for the content source in Settings → Content Sources

---

## Performance & Memory

**cli_debrid is using a lot of memory**

- Normal baselines: ~280–300 MB cold start, ~350–400 MB warm idle
- Use the [Performance Dashboard](features/performance.md) (click Uptime on the dashboard) to monitor RSS over time
- Click **Trim Memory** on the Performance page to release memory back to the OS
- Set `MALLOC_ARENA_MAX=2` in your Docker environment variables to reduce memory fragmentation
- Reduce **Sync Items Per Run** in Overlay Settings if overlay sync is consuming a lot of memory

---

**The app is slow / UI isn't responding**

- Check the **Performance Dashboard** for CPU and memory spikes
- Large libraries with overlays enabled will use more resources during sync
- Reduce the number of enabled scrapers if API calls are excessive
- Check **Debug Functions → Monitoring → Rate Limit State** for throttling

---

**How do I share logs when reporting a bug?**

Go to **Logs** → click **Share Logs**. This uploads the log to a paste service and gives you a link to share. API keys and tokens are **not** automatically redacted — review carefully before sharing publicly. Alternatively use **Debug Functions → Download Logs** and redact manually.

---

## Common Errors

**`Database is locked` / `OperationalError`**

The SQLite database is being accessed by multiple processes simultaneously. Usually resolves itself. If persistent:

- Restart the container
- Check if another process (backup script, manual SQLite access) is holding the database open

---

**`ModuleNotFoundError: No module named 'flask_session'`**

The container image is outdated or didn't pull correctly. Run:

```bash
docker pull godver3/cli_debrid:dev
docker compose up -d
```

---

**`OSError: [Errno 28] No space left on device`**

Your server has run out of disk space. Common causes:

- Log files growing too large — check `/user/logs/`
- Docker overlay storage filling up — run `docker system prune`
- Database backups accumulating — use **Debug Functions → Clean Up Old Database Files**

---

**`WantedQueue object has no attribute 'contains_item_id'`**

Stale Python bytecode from an old version. Pull the latest image:

```bash
docker pull godver3/cli_debrid:dev
docker compose up -d
```

---

**TMDB API 401 Unauthorized**

Your TMDB API key is invalid or using the wrong format. Use the **API Key (v3 auth)** — not the Read Access Token. Regenerate at [themoviedb.org](https://www.themoviedb.org/) → Settings → API.

---

**Port 5000 already in use**

Another service is using port 5000. Either:

- Change cli_debrid's port mapping in docker-compose.yml (e.g. `"5080:5000"`)
- Stop the conflicting service

On macOS, AirPlay Receiver uses port 5000 — disable it in System Settings → General → AirDrop & Handoff.
