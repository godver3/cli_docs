---
title: Usenet Migration
icon: material/transfer
---

# Usenet Migration

This guide walks you through setting up Usenet with cli_debrid — from installing and configuring cli_mount to running your first migration and keeping your library healthy.

!!! info "What you need"
    - A **Usenet provider** account (e.g. Frugal, Newshosting, NewsDemon) — this is your NNTP server
    - At least **two paid NZB indexers** (e.g. NZBGeek, AltHub) — these are your search engines
    - [cli_mount](../integrations/cli_mount.md) installed and running (or [Decypharr](../integrations/decypharr.md), which it is forked from)

---

## Step 1 — Install and configure cli_mount

Follow the [cli_mount installation guide](../integrations/cli_mount.md) to get cli_mount installed and your debrid mount working.

Once installed, open the cli_mount web UI and complete two things:

### 1a — Set up virtual folders (content routing)

!!! note "Plex Direct mode only"
    Virtual folders are only required if you use **Plex Direct** mode (cli_debrid points Plex directly at the cli_mount mount). If you use **Symlink** mode, cli_debrid creates the folder structure itself — skip this step.

Configure virtual folders so cli_mount sorts NZB downloads into the right locations. Follow the [content routing section](../integrations/cli_mount.md#content-routing) of the cli_mount docs — you can use DFS or Internal/External rclone.

Set up at minimum:

- `shows` — matches TV episode filenames
- `movies` — matches movie filenames
- `default` — catches everything else

### 1b — Add your NNTP provider(s)

In cli_mount's **Settings → Providers → Usenet**, click **Add Server** and fill in:

| Field | Description |
|---|---|
| **Server Host** | Your provider's NNTP hostname (e.g. `news.frugalusenet.com`) |
| **Username** | Your Usenet account username |
| **Password** | Your Usenet account password |
| **Port** | `563` for SSL (recommended), `119` for plain |
| **Max Connections** | Set to your plan's connection limit |
| **Priority** | Lower number = higher priority. Your primary provider should be `1` |
| **Use SSL** | Enable for port 563 |

Add additional providers as backups — cli_mount tries them in priority order if the primary fails to find a segment.

---

## Step 2 — Bind required folders to the cli_debrid container

!!! warning "Required for full functionality"
    Without the `climount_data` bind, the cli_mount DB cleanup tool and cli_mount DB backups will **not work**. The `plex_data` bind is optional — it's only used to clean up overlay posters (see [Overlays](overlays.md)).

Add the following to your cli_debrid `docker-compose.yml` volumes section:

```yaml
volumes:
  - /mnt/data/appdata/cli_mount:/climount_data
  - /mnt/user/appdata/plex/Library/Application Support/Plex Media Server:/plex_data
```

Adjust the host paths to match your actual cli_mount and Plex appdata locations.

| Mount | Enables |
|---|---|
| `climount_data` | cli_mount DB backup, restore, and cleanup tools |
| `plex_data` | Optional — overlay poster cleanup |

After adding the mounts, restart the cli_debrid container then configure the paths in settings:

!!! note "Configure the paths in cli_debrid settings"
    - **Plex data path** — go to **Settings → Additional Settings → Overlay Settings** and set **Plex Data Path** to `/plex_data`
    - **cli_mount data path** — go to **Settings → Required Settings → Usenet Provider** and set **cli_mount Data Path** to `/climount_data`

---

## Step 3 — Connect cli_debrid to cli_mount

In cli_debrid, go to **Settings → Required Settings → Usenet Provider**:

| Setting | Value |
|---|---|
| **Enabled** | ✓ |
| **Provider** | `climount` |
| **Provider URL** | Use the host IP and port — e.g. `http://192.168.1.x:8888`. Do **not** use `localhost:8888` as this conflicts with Phalanx DB |
| **API Token** | Leave empty if cli_mount auth is disabled |
| **Download Folder / Category** | Leave empty to use cli_mount's default |
| **cli_mount Data Path** | `/climount_data` (matches the volume bind from Step 2) |
| **Disable NZB Season Packs** | Keep on (default) — see [Required Settings](../configuration/required.md#usenet-provider) |

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

!!! note
    Repair needs the Usenet provider configured as in [Step 3](#step-3-connect-cli_debrid-to-cli_mount).

Click **Save** after enabling.

---

## Step 6 — Migrate your existing library

!!! note "Already on Usenet only?"
    If you are setting up fresh without an existing debrid library, skip to [Step 7](#step-7-ongoing-maintenance).

### If you are switching from debrid to Usenet only

If you want to fully drop debrid and move your entire library to Usenet, follow these steps carefully:

**6a — Create a backup first**

In **Debrid Manager → Maintenance**, click **Run Now** in the Backup section to create a fresh backup of your debrid library.

**6b — Remove debrid provider from cli_mount**

In the cli_mount web UI, go to **Settings → Providers → Debrid** tab. Click the delete (🗑) button on your debrid account and click **Save Configuration**. This removes the debrid provider before you clear the database.

**6c — Stop everything**

1. Turn off Plex (or pause its library scanning)
2. In cli_debrid, click **Stop Program** in the top bar to halt all queue processing
3. Stop the cli_mount container

**6d — Clear the cli_mount database**

In cli_mount's appdata folder, **rename or delete the `db` folder**. This wipes cli_mount's torrent database so you start fresh with Usenet only.

!!! warning "This deletes all cli_mount torrent tracking"
    Make sure your backup was created before this step. The backup file contains everything needed for migration.

**6e — cli_debrid database**

Leave your existing collected items as-is. Once the migration completes and items are downloaded by cli_mount, the **Plex Full Scan** task will automatically detect the new files and update the existing cli_debrid database entries. No manual deletion needed.

**6f — Restart everything**

Start cli_mount first, then start cli_debrid and resume the program. Turn Plex back on.

### Run the migration

1. Go to **Debrid Manager → Maintenance**
2. Select a **Version** from the dropdown in the Backup Slots header (use `Default version` to accept any quality, or pick a specific version to filter results)
3. Click **→ Usenet** on the backup slot you want to migrate (use the most recent **1d** slot for the freshest list)

The migration searches all your Newznab indexers for every torrent in the backup and submits found NZBs to cli_mount. A progress bar shows live stats.

### Migration results

When the migration completes, two extra files are saved alongside the backup:

| File | Contents |
|---|---|
| `*_usenet_failed.json` | Items where an NZB was found but rejected (broken segments, etc.) |
| `*_usenet_not_found.json` | Items where no NZB was found on any indexer |

Both files appear in the **Extra Files** section of Backup Slots with their own **→ Usenet** buttons. Re-run them later to retry — new indexer coverage or reposts may find them on the next attempt.

### Backfill NZB Torrent IDs

!!! warning "Important — do this after migration"
    Run the **Plex Full Scan** task first to detect downloaded files and update the cli_debrid database. Once that completes, run or enable the **Backfill NZB Torrent IDs** task. This links cli_mount's job IDs to the cli_debrid database entries for all migrated items. Without it, the repair engine, health checks, and other NZB-dependent functions won't work correctly on your migrated library.

Go to **Task Manager** and either trigger or enable the **Backfill NZB Torrent IDs** task.

---

## Step 7 — Ongoing maintenance

### NZB repair engine

The repair engine runs automatically (if enabled in Step 5) every 6 hours. It:

1. Queries cli_mount's health API for broken NZBs
2. Matches broken items to cli_debrid's database
3. Searches Newznab indexers for a replacement
4. Submits the replacement to cli_mount and validates it

View repair history and trigger a manual run in **Debrid Manager → Usenet**.

### cli_mount DB tools

With the `climount_data` volume bind in place, the following tools are available in **Debug Functions**:

**Library tab → cli_mount DB Cleanup**

Removes entries for a specific debrid provider from cli_mount's `entries.db` and `items.db` using infohash matching. Useful when you have leftover debrid entries mixed in with your Usenet library.

!!! warning "Stop cli_mount before running a live cleanup"
    Always use **Dry Run** first to preview what will be removed. Stop the cli_mount container before running a live cleanup to avoid database corruption.

**Database tab → cli_mount DB Backup / Restore / Cleanup**

cli_mount's `entries.db` and `items.db` are automatically backed up on the same daily schedule as the cli_debrid database. Manual backup, restore from backup, and old backup cleanup are all available from the Database tab.


---

## Troubleshooting

**NZBs fail with "ARTICLE_NOT_FOUND"**

The NZB segments have expired on your Usenet server's retention. Try a different indexer or search for a more recent repost of the same content. cli_mount verifies segment availability before downloading — this is expected for older content.

**Migration finds 0 results**

Check that your Newznab scrapers are enabled and their API keys are valid. Try running a manual search in the scraper results page for a known title first.

**cli_mount DB Cleanup shows no providers**

Ensure the `climount_data` volume bind is correctly set in your docker-compose and the **cli_mount Data Path** in settings matches (`/climount_data`). The provider list is read directly from cli_mount's `entries.db`.

