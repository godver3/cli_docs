---
title: Newznab
icon: material/newspaper-variant
---

# Newznab

Newznab is the standard API protocol used by most Usenet indexers. Adding a Newznab scraper lets cli_debrid search Usenet alongside torrents and deliver NZB downloads via [Decypharr](../integrations/decypharr.md).

!!! info "Usenet prerequisite"
    Newznab scrapers require Decypharr configured as your Usenet provider. See the [Usenet Migration](../features/usenet-migration.md) guide for full setup.

---

## Compatible indexers

Any Newznab-compatible indexer works, including:

- **NZBGeek**
- **NZBPlanet**
- **DrunkenSlug**
- **NinjacentRAL**
- **DogNZB**
- Any private or public Newznab-compatible site

---

## Adding a Newznab scraper

1. Go to **Settings → Scrapers**
2. Click **Add Scraper** and select **Newznab**
3. Fill in the required fields:

| Field | Description |
|---|---|
| **Name** | A display name for this indexer (e.g. `NZBGeek`) |
| **URL** | Base URL of your indexer (e.g. `https://api.nzbgeek.info`) |
| **API Key** | Your indexer API key — found in your indexer account settings |

4. Toggle **Enabled** on
5. Click **Save Settings**

You can add multiple Newznab indexers. All enabled Newznab scrapers are searched simultaneously for every query.

---

## How NZB results work

When cli_debrid searches for content:

- Newznab indexers are queried alongside all other scrapers
- NZB results appear in scraper results with a **NZB** badge instead of a cache status indicator
- Results go through the same version filter scoring as torrent results
- Clicking **ADD** submits the NZB to Decypharr for download

### Season packs

For season pack searches, cli_debrid searches each episode individually across all Newznab indexers in parallel, then groups results by release group and resolution. Only groups that cover the complete season are surfaced as virtual season packs.

### File list

Clicking the folder icon on an NZB result fetches the NZB XML and lists the files inside. For season packs the per-episode filenames and sizes are shown.

---

## Broken NZB handling

If an NZB download fails health validation after submission to Decypharr, the segment ID is added to a not-wanted list. Future searches will skip that specific NZB automatically, and clicking ADD on a known-broken NZB will show an error before submission.

The [NZB Repair Engine](../features/debrid-manager.md#usenet) automatically detects broken downloads and finds replacements.
