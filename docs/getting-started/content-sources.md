---
title: Add content sources
icon: material/playlist-plus
---

# Step 6 — Add content sources

Content sources tell cli_debrid *what* to find. Without a content source, cli_debrid won't download anything.

Add at least one source to get started. For full details on every source and its settings, see the [:octicons-arrow-right-24: Content Sources reference](../configuration/content-sources.md).

---

## Available content sources

| Source | What it does | Requires |
|---|---|---|
| **Trakt Watchlist** | Downloads everything on your Trakt watchlist | Trakt account (configured in Step 4) |
| **Trakt Lists** | Follow any public or private Trakt list | Trakt account |
| **Seerr** | Downloads approved requests from Seerr | Seerr installed |
| **Plex Watchlist** | Downloads items from your Plex watchlist | Plex Pass |
| **MDBList** | Follow curated lists from MDBList.com | Free MDBList account |
| **Manual** | Add individual titles directly in cli_debrid | Nothing |

---

## Recommended: Trakt Watchlist

The quickest way to get started. Anything you add to your Trakt watchlist will be picked up by cli_debrid automatically.

1. Go to **Settings → Content Sources**
2. Enable **Trakt Watchlist**
3. Save

Now add something to your Trakt watchlist at [trakt.tv](https://trakt.tv) — cli_debrid will find and add it within the next queue cycle.

---

## Seerr

Seerr gives you a polished request UI — users search for content and submit requests, which cli_debrid then fulfils automatically.

Full setup guide: [:octicons-arrow-right-24: Seerr integration](../integrations/seerr.md){ .md-button }

**Setup overview:**

1. Install Seerr (see guide above)
2. In Seerr, go to **Settings → General** and copy your API key
3. In cli_debrid → **Settings → Content Sources**, enable **Seerr**
4. Enter your Seerr URL and API key
5. Save

Approved requests in Seerr will now feed automatically into cli_debrid.

---

## Plex Watchlist

If you have Plex Pass, you can use your Plex watchlist as a content source.

1. Go to **Settings → Content Sources**
2. Enable **Plex Watchlist**
3. Save

---

## MDBList

MDBList hosts curated lists (e.g. IMDb Top 250, popular by genre). You can point cli_debrid at any list.

1. Create a free account at [mdblist.com](https://mdblist.com)
2. Find a list you want to follow, copy its URL
3. In cli_debrid → **Settings → Content Sources**, add an **MDBList** source with the list URL
4. Save

---

## Verify it's working

After adding a content source:

1. Go to the **Queues** page
2. You should see items appearing in the **Wanted** queue
3. Items will move through **Scraping → Adding → Checking → Collected** as they are processed

!!! tip "Nothing appearing in Wanted?"
    - If using a Trakt source, check that Trakt authorisation completed successfully (**Settings → Additional Settings**)
    - Make sure your watchlist/list has items in it
    - Check the logs for errors: **Logs** page in the nav

---

## Next step

[:octicons-arrow-right-24: What's next](whats-next.md){ .md-button .md-button--primary }
