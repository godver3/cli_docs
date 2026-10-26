---
title: Usenet Migration
icon: material/transfer
---

# Usenet Migration

Moves your Usenet library from one mount provider to the other: **cli_mount → NzbDAV** or **NzbDAV → cli_mount**. Each item's stored `.nzb` is copied to the new provider, which fetches it from Usenet again. Nothing is searched for again, so you keep the exact releases you have.

The tool is in **Debug Functions → Library → Migrate between usenet providers**.

!!! info "Before you start"
    - The new provider downloads everything again, so it uses your Usenet provider's connections and depends on its retention. Older releases may have expired.
    - It's best-effort. cli_mount trims old `.nzb` files, so part of an older cli_mount library may not be transferable.
    - Don't run it during a Plex scan of the same library.
    - Test with a small **Limit** first, then transfer the rest.

---

## What each direction needs

cli_debrid runs in a container without Docker access, so it reads NzbDAV over HTTP and reads cli_mount's `.nzb` files from a folder bound into the container.

=== "cli_mount → NzbDAV"

    | Field | Value |
    |---|---|
    | **cli_mount nzb-store path (source)** | cli_mount's stored `.nzb` files as seen inside the cli_debrid container. With the usual bind `- /path/to/appdata/cli_mount:/climount_data` (the same one the cli_mount DB tools use, see [cli_mount Data Path](../configuration/required.md#usenet-provider)), this is `/climount_data/usenet/nzbs`. |
    | **NzbDAV URL (target)** | e.g. `http://192.168.1.x:3000`. Not `localhost`. |
    | **NzbDAV SAB API token** | NzbDAV's SABnzbd API key |
    | **Target category (NzbDAV)** | cli_mount's nzb store has no categories, so everything lands in this one. It must already exist in NzbDAV. To keep categories, migrate one category at a time by pointing the path at that category's releases. |

=== "NzbDAV → cli_mount"

    | Field | Value |
    |---|---|
    | **NzbDAV URL (source)** | e.g. `http://192.168.1.x:3000` |
    | **NzbDAV SAB API token** | NzbDAV's SABnzbd API key |
    | **cli_mount URL (target)** | e.g. `http://192.168.1.x:8282` |
    | **cli_mount API token** | Only if cli_mount authentication is on |

    Only NzbDAV history entries that still have their stored `.nzb` can be moved. Each keeps its NzbDAV category as its cli_mount download folder.

Fields for your current Usenet Provider are filled in from **Settings → Required Settings → Usenet Provider**.

### Options

| Option | Default | What it does |
|---|---|---|
| **Skip items already at target** | On | Leaves out releases whose name is already on the target, so you can re-run a transfer safely |
| **Max target queue depth** | `3` | NzbDAV target only: waits while NzbDAV's queue has this many jobs, so it isn't flooded |
| **Limit** | `0` (all) | Transfer only the first N items |

---

## Running it

1. Pick the **Direction** and fill in the fields.
2. Click **Preview source** to see how many items can be moved and a sample of their names.
3. Set a small **Limit** and click **Start transfer**. The progress shows submitted, skipped and failed counts, with a reason for each failure.
4. Check those items play from the new provider, then set **Limit** back to `0` and run it again. With **Skip items already at target** on, the ones you already moved are skipped.

**Cancel** stops after the current item. Progress is kept in memory only, so a cli_debrid restart loses the progress view (items already submitted stay on the target).

---

## After the transfer

The tool only moves the downloads. It doesn't change cli_debrid's settings, database or symlinks. Once you're happy with the new provider:

1. In **Settings → Required Settings → Usenet Provider**, set **Provider**, **Provider URL** and **API Token** to the new provider.
2. Point your library at the new provider's mount: the Plex library folders in Plex mode, or **Original Files Path** in Symlink mode.

!!! warning "Existing library entries still point at the old provider"
    cli_debrid's database records and symlinks keep the old provider's file paths and job IDs. Keep the old provider running until you've checked that items play from the new one.

---

## Troubleshooting

**"Path not found in this container"**
:   The cli_mount appdata folder isn't bound into cli_debrid, or the path is wrong. Add the bind to cli_debrid's `docker-compose.yml`, restart it, and use the path as seen inside the container.

**Items fail with `rejected` on NzbDAV**
:   NzbDAV refused the file. Check that the target category exists in NzbDAV.

**Fewer items than expected in Preview**
:   cli_mount has already trimmed their `.nzb` files, or NzbDAV history entries have no stored `.nzb`. Those releases have to be searched for again.
