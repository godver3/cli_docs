---
title: Add scrapers
icon: material/magnify
---

# Step 5 — Add scrapers

Scrapers are how cli_debrid finds torrents and NZBs for your content. You need at least one scraper configured before cli_debrid can add anything.

- **Debrid users** need at least one **torrent** scraper (below).
- **Usenet users** need at least one **Newznab** indexer ([see below](#newznab-usenet-indexers)).
- Using both? Add both — results are compared together.

---

## Recommended for beginners

**Start with Zilean and Torrentio.** Both are free, require no self-hosting, and cover the vast majority of content.

| Scraper | Type | Requires | Best for |
|---|---|---|---|
| [Zilean](../scrapers/zilean.md) | Debrid cache index | Nothing | Speed — checks what's already cached in debrid |
| [Torrentio](../scrapers/torrentio.md) | Torrent indexer | Nothing | Wide coverage, easy setup |
| [MediaFusion](../scrapers/mediafusion.md) | Torrent indexer | Nothing (public) or self-hosted | High-quality results |
| [Jackett](../scrapers/jackett.md) | Torrent proxy | Self-hosted | Access to private trackers |
| [Prowlarr](../scrapers/prowlarr.md) | Torrent proxy | Self-hosted | Modern replacement for Jackett |
| [Nyaa](../scrapers/nyaa.md) | Torrent indexer | Nothing | Anime |
| [Newznab](../scrapers/newznab.md) | Usenet indexer | Indexer account + Usenet provider | NZBs via cli_mount |

---

## Adding a scraper

1. Go to **Settings → Scrapers**
2. Click **Add Scraper**
3. Select the scraper type and fill in the URL
4. Save

### Zilean (recommended first scraper)

Zilean indexes what's already cached in your debrid account. Hits are instant — no waiting for debrid to download.

Full guide: [:octicons-arrow-right-24: Zilean setup](../scrapers/zilean.md){ .md-button }

Default URL (public instance):
```
https://zileanfortheweebs.midnightignite.me
```

### Torrentio

Torrentio is a Stremio addon that also works as a scraper API. No account or URL needed — cli_debrid uses the public instance.

Full guide: [:octicons-arrow-right-24: Torrentio setup](../scrapers/torrentio.md){ .md-button }

### MediaFusion

MediaFusion is a more advanced scraper with better filtering. Can be used with the public instance or self-hosted.

Full guide: [:octicons-arrow-right-24: MediaFusion setup](../scrapers/mediafusion.md){ .md-button }

### Newznab (Usenet indexers)

Each Usenet indexer is added as its own **Newznab** scraper. Requires a Usenet provider set up in [Step 4](configure.md).

1. Go to **Settings → Scrapers** and click **Add Scraper**
2. Select **Newznab**
3. Fill in:

    | Field | Value |
    |---|---|
    | **Name** | A display name, e.g. `NZBGeek` |
    | **URL** | Your indexer's API URL, e.g. `https://api.nzbgeek.info` |
    | **API Key** | From your indexer account page |

4. Enable it and save. Repeat for each indexer — all enabled indexers are searched at the same time.

Full guide: [:octicons-arrow-right-24: Newznab setup](../scrapers/newznab.md){ .md-button }

---

## Scraper priority

Scrapers are checked in order. Put your fastest/most reliable scraper first:

1. Zilean (fastest — cache hits only)
2. Torrentio or MediaFusion (broader search)
3. Newznab indexers (Usenet)
4. Jackett/Prowlarr (private trackers, slowest)

Change the order by dragging scrapers by their handle in **Settings → Scrapers**.

---

## Testing a scraper

After adding a scraper, open **Tools → Tester** to search for a known title and confirm results come back. It also shows how each release is scored, so you can tune your quality settings.

---

For full documentation on all supported scrapers and advanced configuration, see the [:octicons-arrow-right-24: Scrapers reference](../scrapers/index.md#available-scrapers).

---

## Next step

[:octicons-arrow-right-24: Step 6 — Add content sources](content-sources.md){ .md-button .md-button--primary }
