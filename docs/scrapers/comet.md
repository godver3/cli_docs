---
title: Comet
icon: material/star-four-points
---

# Comet

Comet is a Stremio addon that searches torrents. It is a common backup when [Torrentio](torrentio.md) is blocked or down.

---

## Setup

1. Go to **Settings → Scrapers**
2. Click **Add Scraper** → select **Comet**
3. Set the **URL**:

    === "Public instance"
        ```
        https://comet.feels.legal
        ```
        Works with no setup and no account.

    === "Your own configured URL"
        Paste the manifest URL from your Comet configure page, for example:
        ```
        https://comet.example.com/<config>/manifest.json
        ```
        Clyde works out the base address from it. A `stremio://` link works too.

    === "Self-hosted on your network"
        Enter the address of your Comet, for example:
        ```
        192.168.1.5:8000
        ```
        Local addresses without a scheme use `http://`. Other addresses without a scheme use `https://`.

4. Toggle **Enabled** on
5. Click **Save Settings**

Use the **Test** button to check the manifest. It does not show the config.

| Field | Description |
|---|---|
| **URL** | A plain instance URL, or a manifest URL that already holds a config |
| **Config** | Optional. A base64 config or raw JSON. Only used when the URL is a plain instance URL without a config in it |
| **Priority** | Scraper priority score. Higher wins when results are otherwise similar |

---

## Notes

!!! warning "Leave Comet's own filters off"
    Clyde filters and ranks every result by your [versions](../configuration/versions.md). Anything Comet filters out never reaches Clyde. A "1080p only" Comet config, for example, hides every release from your 4K version and from upgrades. If you configure Comet, turn off its resolution, size and language filters. Set its results limit high or to unlimited.

!!! note "No debrid key needed"
    Clyde checks the cache on your debrid accounts itself. If you put a key in Comet's config anyway, it is only sent to that Comet instance.

- The config in the URL can hold your debrid key, so Clyde never writes it to the logs. Logs show `<config>` in its place.
- Some public instances, such as ElfHosted, refuse requests without a config (HTTP 403). Use your own configured manifest URL there.
- The sizes Comet reports are for the whole torrent, so a season pack shows the size of the full pack.
- If Comet is already scraping the same title, Clyde waits a few seconds and asks again.
- Self-hosting Comet is optional. See the [Comet GitHub](https://github.com/g0ldyy/comet) if you want your own.

---

## Troubleshooting

**No results from Comet**

- Check the Connections page
- Run a scrape in the [Scraper Tester](../features/scraper-tester.md) and see if Comet results appear
- A 403 or 401 in the logs means the instance rejected the request. Use a configured manifest URL
- "OBSOLETE CONFIGURATION" means the instance changed. Re-configure it on the instance and paste the new URL
