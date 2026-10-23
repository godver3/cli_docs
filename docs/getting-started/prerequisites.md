---
title: Prerequisites
icon: material/clipboard-check
---

# Step 1 — Prerequisites

Before installing anything, sign up for the required services and gather your API keys. This takes 10–15 minutes and avoids stopping mid-install.

---

## Required services

### 1. A download source — debrid, Usenet, or both

cli_debrid needs at least one place to get content from:

| Option | What you need | Good for |
|---|---|---|
| **Debrid** | A debrid account (below) | Huge instant cache of popular torrents |
| **Usenet** | A Usenet provider + at least one indexer ([see 1b](#1b-usenet)) | Fast, reliable downloads with long retention |
| **Both** | Everything above | Usenet fills gaps in the debrid cache and vice versa |

You can start with one and add the other later.

### 1a. Debrid service

A debrid service is a premium link provider that caches torrents in the cloud. cli_debrid uses it to stream content without downloading locally.

If you're using debrid, you need **one** of the following:

| Service | Notes |
|---|---|
| [Real-Debrid](https://real-debrid.com) | Most popular, largest cache |
| [AllDebrid](https://alldebrid.com) | Good alternative |
| [Premiumize](https://www.premiumize.me) | Also supports Usenet |
| [Torbox](https://torbox.app) | Newer, growing cache |
| [Debrid-Link](https://debrid-link.com) | European provider |

!!! tip "Which one?"
    Real-Debrid has the largest torrent cache and is the most tested with cli_debrid. Start there if you're unsure.

After signing up, locate your API key:

=== "Real-Debrid"
    [real-debrid.com/apitoken](https://real-debrid.com/apitoken) — copy the token shown.

=== "AllDebrid"
    [alldebrid.com/apikeys](https://alldebrid.com/apikeys) — create a new API key.

=== "Premiumize"
    [premiumize.me/account](https://www.premiumize.me/account) — find **API Key** under your profile.

=== "Torbox"
    [torbox.app/settings](https://torbox.app/settings) — copy your API key.

=== "Debrid-Link"
    [debrid-link.com/webapp/apikey](https://debrid-link.com/webapp/apikey) — generate a key.

**Save this key — you will need it during cli_debrid setup.**

### 1b. Usenet

To use Usenet you need two things: a **provider** that serves the files, and an **indexer** that tells cli_debrid what's available.

| What | Examples | Notes |
|---|---|---|
| **Usenet provider** (news server) | Frugal Usenet, Newshosting, Eweka, UsenetExpress | Paid account. You'll need the server hostname, port (`563` for SSL), username, password and your plan's connection limit. |
| **Newznab indexer** | NZBGeek, NZBPlanet, DrunkenSlug, DogNZB | Usually a small yearly fee. You'll need the indexer URL and your API key from your account page. |

Nothing is downloaded to your server — [cli_mount](../integrations/cli_mount.md) streams NZB content from your provider through the same mount used for debrid.

**Save your provider login and indexer API key.**

---

### 2. Media server

cli_debrid works with Plex, Jellyfin, or Emby. You need one installed and accessible on your network.

| Media server | Notes |
|---|---|
| [Plex](https://www.plex.tv) | Most features supported. Plex Pass not required. |
| [Jellyfin](https://jellyfin.org) | Free and open source. |
| [Emby](https://emby.media) | Supported via Jellyfin-compatible mode. |

!!! info "File management modes"
    cli_debrid has two file management modes that affect which media servers are supported:

    - **Plex mode** — uses the Plex API to manage your library. Plex only.
    - **Symlink mode** — creates symlinks on disk. Works with Plex, Jellyfin, and Emby.

You don't need to configure any libraries yet — that happens after the mount is set up. See the integration guides for setup instructions: [Plex](../integrations/plex.md) · [Jellyfin](../integrations/jellyfin.md)

---

### 3. TMDB API key

TMDB (The Movie Database) is used for metadata, posters, the Discover page, and trending content.

1. Create a free account at [themoviedb.org](https://www.themoviedb.org/signup)
2. Go to **Settings → API**
3. Request a developer API key (instant approval)
4. Copy the **API Key (v3 auth)** value

**Save this key.**

---

### 4. TVDB API key

TVDB is where cli_debrid looks up shows and movies, and matches episodes. It's required unless you use Trakt instead.

1. Create a free account at [thetvdb.com](https://www.thetvdb.com/register)
2. Go to **API Keys** under your account: [thetvdb.com/dashboard/account/apikey](https://www.thetvdb.com/dashboard/account/apikey)
3. Create a new API key
4. Copy the key

**Save this key.**

---

## Optional services

These are not required to get started but are recommended once running:

| Service | Purpose |
|---|---|
| [Seerr](https://docs.seerr.dev) | Request movies/shows via a clean UI — supports Plex and Jellyfin |
| [MDBList](https://mdblist.com) | Curated media lists (IMDb Top 250, genre lists, etc.) usable as content sources |
| [Scrob](https://github.com/ellite/scrob) | Self-hosted watch tracker (a private Trakt/Letterboxd) — its lists and collection can be content sources |
| [Bazarr](https://www.bazarr.media) | Automatic subtitle downloading |

### Trakt or Scrob

Both are optional. Trakt is the hosted service; [Scrob](https://github.com/ellite/scrob) is a self-hosted alternative that syncs with Plex, Jellyfin and Emby. Either can feed lists and recommendations into cli_debrid — use whichever you prefer, or both.

**Scrob:** you only need your Scrob URL (e.g. `http://192.168.1.x:7330`) and an API key from **Settings → Connections → API Key** in Scrob.

**Trakt:** Trakt is optional. It can be used as a content source (watchlist, lists, collection) and as a metadata fallback for TV shows if you haven't configured a TVDB key.

1. Create a free account at [trakt.tv](https://trakt.tv/auth/join)
2. Go to [trakt.tv/oauth/applications](https://trakt.tv/oauth/applications)
3. Click **New Application**
4. Fill in:
    - **Name:** `cli_debrid`
    - **Redirect URI:** `urn:ietf:wg:oauth:2.0:oob`
5. Copy the **Client ID** and **Client Secret**

**Save both values if you plan to use Trakt.**

---

## Summary checklist

Before moving on, confirm you have:

- [ ] A download source: debrid account + API key, **and/or** a Usenet provider login + indexer API key
- [ ] Plex, Jellyfin, or Emby installed
- [ ] TMDB API key
- [ ] TVDB API key (or Trakt instead)

---

## Next step

[:octicons-arrow-right-24: Step 2 — Mount your storage](mount.md){ .md-button .md-button--primary }
