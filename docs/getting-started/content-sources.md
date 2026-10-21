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
| **My Plex Watchlist** | Downloads items from your Plex watchlist | Plex account (uses your Plex token) |
| **Plex Friends Watchlist** | Downloads items from your Plex friends' watchlists | Plex account |
| **Other Plex Watchlist** | Follows another Plex user's watchlist, e.g. a Plex Home member | That user's Plex login |
| **My Plex RSS Watchlist** | Follows your Plex watchlist RSS feed | The RSS feed URL from Plex |
| **Seerr** (shown as *Overseerr* in settings) | Downloads approved requests from Seerr | Seerr installed |
| **Trakt Watchlist / Lists / Collection** | Your Trakt watchlist, any public or private list, or your collection | Trakt account (configured in Step 4) |
| **MDBList** | Follow curated lists from MDBList.com | Free MDBList account |
| **Agregarr** | Requests Agregarr makes through Seerr, kept separate from your users' Seerr requests | Agregarr + Seerr |
| **Scrob Lists / Collection / Special Lists** | Your Scrob lists or collection, or Scrob's discovery lists (Now Playing, Upcoming, Hidden Gems, New Episodes, For You…) | Scrob connected (Step 4) |
| **Adaptive List** | Builds a list from TMDB discover filters (genre, rating, year…) that refreshes over time | TMDB key (Step 1) |

To add a single title by hand, use the **Discover** page, or **Magnet Assign** to add a specific torrent or NZB — no content source needed.

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

Your Plex watchlist works as a content source with any Plex account — it uses the Plex token from [Step 4](configure.md).

1. Go to **Settings → Content Sources**
2. Add a **My Plex Watchlist** source
3. Save

To also pick up what your Plex friends add to their watchlists, add a **Plex Friends Watchlist** source the same way.

---

## MDBList

MDBList hosts curated lists (e.g. IMDb Top 250, popular by genre). You can point cli_debrid at any list.

1. Create a free account at [mdblist.com](https://mdblist.com)
2. Find a list you want to follow, copy its URL
3. In cli_debrid → **Settings → Content Sources**, add an **MDBList** source with the list URL
4. Save

---

## Scrob

If you connected [Scrob](https://github.com/ellite/scrob) in [Step 4](configure.md#scrob-optional):

1. Go to **Settings → Content Sources**
2. Add a **Scrob Lists** source and enter the list IDs to follow (comma-separated, e.g. `2,7`; shown in the list's URL in Scrob), or add **Scrob Collection** to follow your whole collection
3. Save

---

## Verify it's working

After adding a content source:

1. Go to the **Queues** page
2. You should see items appearing in the **Wanted** queue
3. Items will move through **Scraping → Adding → Checking → Collected** as they are processed

!!! tip "Nothing appearing in Wanted?"
    - If using a Trakt source, check that Trakt authorisation completed successfully (**Settings → Additional Settings**)
    - If using a Scrob source, check the Scrob URL and API key under **Settings → Additional Settings → Scrob**
    - Make sure your watchlist/list has items in it
    - Check the logs for errors: **Logs** page in the nav

---

## Next step

[:octicons-arrow-right-24: What's next](whats-next.md){ .md-button .md-button--primary }
