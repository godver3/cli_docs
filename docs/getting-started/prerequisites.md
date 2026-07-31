---
title: Prerequisites
icon: material/clipboard-check
---

# Step 1 — Prerequisites

Before installing anything, sign up for the required services and gather your API keys. This takes 10–15 minutes and avoids stopping mid-install.

---

## Required services

### 1. Debrid service

A debrid service is a premium link provider that caches torrents in the cloud. cli_debrid uses it to stream content without downloading locally.

You need **one** of the following:

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

TVDB is used for TV show metadata and episode matching.

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
| [Bazarr](https://www.bazarr.media) | Automatic subtitle downloading |

### Trakt account

Trakt is optional. It can be used as a content source (watchlist, lists, collection) and as a metadata fallback for TV shows if you haven't configured a TVDB key.

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

- [ ] Debrid account + API key
- [ ] Plex, Jellyfin, or Emby installed
- [ ] TMDB API key
- [ ] TVDB API key (or Trakt, as a fallback for TV metadata)

---

## Next step

[:octicons-arrow-right-24: Step 2 — Mount your debrid storage](mount.md){ .md-button .md-button--primary }
