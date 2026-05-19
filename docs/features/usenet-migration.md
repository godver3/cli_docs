---
title: Usenet Migration
icon: material/transfer
---

# Usenet Migration

This guide walks you through setting up Usenet with cli_debrid — from installing and configuring Decypharr to running your first migration and keeping your library healthy.

!!! info "What you need"
    - A **Usenet provider** account (e.g. Frugal, Newshosting, NewsDemon) — this is your NNTP server
    - At least **two paid NZB indexers** (e.g. NZBGeek, AltHub) — these are your search engines
    - [Decypharr](../integrations/decypharr.md) installed and running

---

## Step 1 — Install and configure Decypharr

Follow the [Decypharr installation guide](../integrations/decypharr.md) to get Decypharr installed and your debrid mount working.

Once installed, open the Decypharr web UI and complete two things:

### 1a — Set up virtual folders (content routing)

!!! note "Plex Direct mode only"
    Virtual folders are only required if you use **Plex Direct** mode (cli_debrid points Plex directly at the Decypharr mount). If you use **Symlink** mode, cli_debrid creates the folder structure itself — skip this step.

Configure virtual folders so Decypharr sorts NZB downloads into the right locations. Follow the [content routing section](../integrations/decypharr.md#content-routing) of the Decypharr docs — you can use DFS or Internal/External rclone.

Set up at minimum:

- `shows` — matches TV episode filenames
- `movies` — matches movie filenames
- `default` — catches everything else

### 1b — Add your NNTP provider(s)

In Decypharr's **Settings → Usenet**, click **Add Server** and fill in:

| Field | Description |
|---|---|
| **Server Host** | Your provider's NNTP hostname (e.g. `news.frugalusenet.com`) |
| **Username** | Your Usenet account username |
| **Password** | Your Usenet account password |
| **Port** | `563` for SSL (recommended), `119` for plain |
| **Max Connections** | Set to your plan's connection limit |
| **Priority** | Lower number = higher priority. Your primary provider should be `1` |
| **Use SSL** | Enable for port 563 |

Add additional providers as backups — Decypharr tries them in priority order if the primary fails to find a segment.

---

## Step 2 — Bind required folders to the cli_debrid container

!!! warning "Required for full functionality"
    Without these volume binds, the Decypharr DB cleanup tool, Decypharr DB backups, and the Plex Stuck Files task will **not work**.

Add the following to your cli_debrid `docker-compose.yml` volumes section:

```yaml
volumes:
  - /mnt/data/appdata/decypharr:/decypharr_data
  - /mnt/user/appdata/plex/Library/Application Support/Plex Media Server:/plex_data
```

Adjust the host paths to match your actual Decypharr and Plex appdata locations.

| Mount | Enables |
|---|---|
| `decypharr_data` | Decypharr DB backup, restore, and cleanup tools |
| `plex_data` | Plex Stuck Files task |

After adding the mounts, restart the cli_debrid container then configure the paths in settings:

!!! note "Configure the paths in cli_debrid settings"
    - **Plex data path** — go to **Settings → Additional Settings → Overlay Settings** and set **Plex Data Path** to `/plex_data`
    - **Decypharr data path** — go to **Settings → Required Settings → Usenet Provider** and set **Decypharr Data Path** to `/decypharr_data`

---

## Step 3 — Connect cli_debrid to Decypharr

In cli_debrid, go to **Settings → Required Settings → Usenet Provider**:

| Setting | Value |
|---|---|
| **Enabled** | ✓ |
| **Decypharr URL** | Use the host IP and port — e.g. `http://192.168.1.x:8888`. Do **not** use `localhost:8888` as this conflicts with Phalanx DB |
| **API Token** | Leave empty if Decypharr auth is disabled |
| **Download Folder** | Leave empty to use Decypharr's default |
| **Decypharr Data Path** | `/decypharr_data` (matches the volume bind from Step 2) |

---

## Step 4 — Add NZB indexers as scrapers

In cli_debrid, go to **Settings → Scrapers** and add your NZB indexers:

1. Click **Add Scraper** and select **Newznab**
2. Fill in the **Name**, **URL**, and **API Key** for each indexer
3. Enable each one and save

!!! tip "Use at least two paid indexers"
    Having two indexers (e.g. NZBGeek + AltHub) significantly improves coverage. Both are searched simultaneously for every query.

### Set Newznab scraper priority

For each version you use, give your Newznab indexers a higher bonus score than your debrid scrapers so NZB results are preferred:

1. Go to **Settings → Version Settings** and open a version
2. Enable **Scraper Priorities**
3. Set your Newznab indexers (e.g. `NZBGeek_1`, `althub_1`) to a high value such as `500`
4. Leave debrid scrapers (Jackett, Zilean, etc.) at `0` or lower
5. Repeat for every version you have configured

!!! tip
    Higher number = higher priority. A value of `500` on your NZB indexers ensures they consistently rank above debrid results when both are available.

---

## Step 5 — Enable recommended tasks

Go to **Task Manager** and enable:

| Task | Tab | Why |
|---|---|---|
| **Repair Broken NZBs** | Features | Automatically detects broken NZB downloads and finds replacements. Recommended interval: `6h` |
| **Plex Stuck Files** | Library | Detects Plex items stuck in a scanning loop and removes them. Default interval is `5m` — good when initially adding a lot of content. Once your library is settled, `1h` is sufficient. |

!!! danger "Required volume binds"
    These tasks will **not work** without the following mounts in your cli_debrid `docker-compose.yml`:

    ```yaml
    volumes:
      - /mnt/data/appdata/decypharr:/decypharr_data
      - /mnt/user/appdata/plex/Library/Application Support/Plex Media Server:/plex_data
    ```

    Adjust the host paths to match your actual Decypharr and Plex appdata locations.

Click **Save** after enabling.

---

## Step 6 — Migrate your existing library

!!! note "Already on Usenet only?"
    If you are setting up fresh without an existing debrid library, skip to [Step 7](#step-7-ongoing-maintenance).

### If you are switching from debrid to Usenet only

If you want to fully drop debrid and move your entire library to Usenet, follow these steps carefully:

**6a — Create a backup first**

In **Debrid Manager → Maintenance**, click **Run Now** in the Backup section to create a fresh backup of your debrid library.

**6b — Remove debrid provider from Decypharr**

In the Decypharr web UI, go to **Settings → Providers → Debrid** tab. Click the delete (🗑) button on your debrid account and click **Save Configuration**. This removes the debrid provider before you clear the database.

**6c — Stop everything**

1. Turn off Plex (or pause its library scanning)
2. In cli_debrid, click **Stop Program** in the top bar to halt all queue processing
3. Stop the Decypharr container

**6d — Clear the Decypharr database**

In Decypharr's appdata folder, **rename or delete the `db` folder**. This wipes Decypharr's torrent database so you start fresh with Usenet only.

!!! warning "This deletes all Decypharr torrent tracking"
    Make sure your backup was created before this step. The backup file contains everything needed for migration.

**6e — cli_debrid database**

Leave your existing collected items as-is. Once the migration completes and items are downloaded by Decypharr, the **Plex Full Scans** task will automatically detect the new files and update the existing cli_debrid database entries. No manual deletion needed.

**6f — Restart everything**

Start Decypharr first, then start cli_debrid and resume the program. Turn Plex back on.

### Run the migration

1. Go to **Debrid Manager → Maintenance**
2. Select a **Version** from the dropdown in the Backup Slots header (use `Default version` to accept any quality, or pick a specific version to filter results)
3. Click **→ Usenet** on the backup slot you want to migrate (use the most recent **1d** slot for the freshest list)

The migration searches all your Newznab indexers for every torrent in the backup and submits found NZBs to Decypharr. A progress bar shows live stats.

### Migration results

When the migration completes, two extra files are saved alongside the backup:

| File | Contents |
|---|---|
| `*_usenet_failed.json` | Items where an NZB was found but rejected (broken segments, etc.) |
| `*_usenet_not_found.json` | Items where no NZB was found on any indexer |

Both files appear in the **Extra Files** section of Backup Slots with their own **→ Usenet** buttons. Re-run them later to retry — new indexer coverage or reposts may find them on the next attempt.

### Backfill NZB Torrent IDs

!!! warning "Important — do this after migration"
    Run the **Plex Full Scans** task first to detect downloaded files and update the cli_debrid database. Once that completes, run or enable the **Backfill NZB Torrent IDs** task. This links Decypharr's job IDs to the cli_debrid database entries for all migrated items. Without it, the repair engine, health checks, and other NZB-dependent functions won't work correctly on your migrated library.

Go to **Task Manager** and either trigger or enable the **Backfill NZB Torrent IDs** task.

---

## Step 7 — Ongoing maintenance

### NZB repair engine

The repair engine runs automatically (if enabled in Step 5) every 6 hours. It:

1. Queries Decypharr's health API for broken NZBs
2. Matches broken items to cli_debrid's database
3. Searches Newznab indexers for a replacement
4. Submits the replacement to Decypharr and validates it

View repair history and trigger a manual run in **Debrid Manager → Usenet**.

### Decypharr DB tools

With the `decypharr_data` volume bind in place, the following tools are available in **Debug Functions**:

**Library tab → Decypharr DB Cleanup**

Removes entries for a specific debrid provider from Decypharr's `entries.db` and `items.db` using infohash matching. Useful when you have leftover debrid entries mixed in with your Usenet library.

!!! warning "Stop Decypharr before running a live cleanup"
    Always use **Dry Run** first to preview what will be removed. Stop the Decypharr container before running a live cleanup to avoid database corruption.

**Database tab → Decypharr DB Backup / Restore / Cleanup**

Decypharr's `entries.db` and `items.db` are automatically backed up on the same daily schedule as the cli_debrid database. Manual backup, restore from backup, and old backup cleanup are all available from the Database tab.

### Plex Stuck Files

Occasionally Plex gets stuck scanning a file repeatedly without completing. The **Plex Stuck Files** task detects these loops by watching Plex's log and removes the stuck items automatically. Requires the `plex_data` volume bind.

!!! warning "Plex log filename"
    The task looks for `Plex Media Server.log` inside the bound `plex_data` path (full path: `/plex_data/Logs/Plex Media Server.log`). Some systems name the log differently — e.g. `Plex Media Server 1.log`. If the task logs `Plex log not found`, check your Plex `Logs` folder and confirm the exact filename. The log file is created by Plex when it is running — if it's missing, make sure Plex is active.

---

## Troubleshooting

**NZBs fail with "ARTICLE_NOT_FOUND"**

The NZB segments have expired on your Usenet server's retention. Try a different indexer or search for a more recent repost of the same content. Decypharr verifies segment availability before downloading — this is expected for older content.

**Migration finds 0 results**

Check that your Newznab scrapers are enabled and their API keys are valid. Try running a manual search in the scraper results page for a known title first.

**Decypharr DB Cleanup shows no providers**

Ensure the `decypharr_data` volume bind is correctly set in your docker-compose and the **Decypharr Data Path** in settings matches (`/decypharr_data`). The provider list is read directly from Decypharr's `entries.db`.

**Plex Stuck Files task does nothing**

Verify the `plex_data` volume bind is in place and that the path matches your Plex appdata location. Check Task Manager that the task is enabled.
