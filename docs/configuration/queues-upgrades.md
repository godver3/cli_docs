---
title: Queues & Upgrades
icon: material/tray-full
---

# Queues & Upgrades

**Settings → Queues & Upgrades** controls the order items are scraped in, how long they wait between attempts, and how upgrades are handled. See [Queues](../features/queues.md) for what each queue does.

---

## Queue

| Setting | Default | Description |
|---|---|---|
| **Queue Sort Order** | `None` | `None`, `Movies First` or `Episodes First` |
| **Sort By Release Date Desc** | Off | After the sort above, put the newest releases first. Items with no date go last. |
| **Content Source Priority** | — | Comma-separated content sources in the order they should be scraped, e.g. `Plex,Trakt,Overseerr`. Sources not listed go last. |
| **Wake Limit** | `24` | How many times a sleeping item is woken before it's blacklisted |
| **Sleep Duration Minutes** | `30` | How long an item sleeps between attempts |
| **Blacklist Final Scrape Delay Hours** | `0` | Wait this long, then try one last scrape before blacklisting. `0` turns it off. |
| **Movie Airtime Offset** | `0` | Hours after midnight at the start of the release date to start scraping new movies. If nothing is found that day, the movie is searched again every hour, and those retries don't count toward the wake limit. Shows use their air time instead. |
| **Episode Airtime Offset** | `0` | Hours after the show's airtime to start scraping new episodes. Negative values scrape early. Without Trakt, airtime defaults to 19:00. |
| **Enable Pause Schedule** | Off | Pause the queue every day between the two times below |
| **Pause Start Time** / **Pause End Time** | `00:00` | The daily pause window (HH:MM) |
| **Queue Pool Workers** | `2` | How many queue items (scraping, adding, checking…) are handled at once. `1` for slow machines, `3` for fast ones. Applies on save; also adjustable from the **Queues** page. |
| **Main Loop Sleep Seconds** | `0.0` | Minimum pause between tasks, to lower system load |
| **Pre Release Scrape Days** | `0` | Start scraping movies this many days before release. `0` turns it off. |

**Blacklist Duration** is under [Scraping → Filtering & Blacklist](scraping.md#filtering-blacklist).

---

## Queue Management

| Setting | Default | Description |
|---|---|---|
| **Checking Queue Period** | `3600` | Seconds an item can stay in Checking before it goes back to Wanted |
| **Ignore Wanted Queue Throttling** | Off | Let Wanted move every eligible item to Scraping, however full Scraping is. Use with care. |
| **Disable Not Wanted Check** | Off | Skip the not-wanted check for queued items |

Upgrade settings (turning upgrading on, the upgrade window, score limits) are in the **Upgrading** group of the [Upgrade Hub](../features/upgrade-hub.md#upgrading) Settings tab.

---

## Content Processing

| Setting | Default | Description |
|---|---|---|
| **Do Not Add Plex Watch History Items To Queue** | Off | Don't queue items that come from Plex watch history |
| **Disable Content Source Caching** | Off | Fetch content sources fresh every time instead of caching them |
| **Enable Granular Version Additions** | On | Add Wanted items per version |

How often each content source is checked is set per source on the [Automation](../features/automation.md) page (Content Sources group, Advanced view). Options such as removing collected items from a watchlist are on each source under [Content Sources](content-sources.md).
