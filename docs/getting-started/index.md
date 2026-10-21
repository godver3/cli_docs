---
title: Getting Started
icon: material/rocket-launch
---

# Getting Started

This guide walks you through everything needed to get cli_debrid up and running from scratch — from signing up for the required services to streaming your first file.

cli_debrid can get content from a **debrid service** (Real-Debrid, AllDebrid, etc.), from **Usenet**, or both. Each step below covers both options — follow whichever applies to you.

Follow the steps in order. Each page ends with a link to the next step.

---

## The setup flow

<div class="grid cards single-col" markdown>

- **Step 1 — Prerequisites**

    Sign up for required services and gather your API keys before installing anything.

    [:octicons-arrow-right-24: Prerequisites](prerequisites.md){ .md-button .md-button--primary }

- **Step 2 — Mount your storage**

    Use cli_mount, Decypharr or Zurg to mount your debrid and/or Usenet files as a local folder your media server can read.

    [:octicons-arrow-right-24: Mount setup](mount.md){ .md-button .md-button--primary }

- **Step 3 — Install cli_debrid**

    Install the app on your platform — Unraid, Docker, TrueNAS, Proxmox, Ubuntu, or Windows.

    [:octicons-arrow-right-24: Install](install.md){ .md-button .md-button--primary }

- **Step 4 — Configure cli_debrid**

    Connect your debrid service and/or Usenet provider, media server, and mount path. Choose Plex mode or symlink mode.

    [:octicons-arrow-right-24: Configure](configure.md){ .md-button .md-button--primary }

- **Step 5 — Add scrapers**

    Set up at least one scraper so cli_debrid can find torrents or NZBs for your content.

    [:octicons-arrow-right-24: Scrapers](scrapers.md){ .md-button .md-button--primary }

- **Step 6 — Add content sources**

    Tell cli_debrid what to download — Trakt watchlists, Seerr requests, or manual lists.

    [:octicons-arrow-right-24: Content sources](content-sources.md){ .md-button .md-button--primary }

</div>

---

## How it all fits together

```mermaid
flowchart LR
    A["Content Sources\nSeerr, Trakt, Watchlists"] --> B
    B["cli_debrid\nscrapes torrents & NZBs, manages library"] --> C
    C["Debrid Service and/or Usenet\nReal-Debrid / AllDebrid / news server"] --> D
    D["Mount Service\ncli_mount / Decypharr / Zurg"] --> E
    E["Media Server\nPlex / Jellyfin / Emby"]
    B -->|"triggers scan"| E
```

### File management modes

=== "Plex mode"

    ```mermaid
    flowchart LR
        A["Mount Service\ncli_mount / Decypharr / Zurg"] --> B["Plex\nreads files directly from mount"]
        C["cli_debrid"] --> D["Debrid Service / Usenet"]
        D --> A
        C -->|"triggers library scan via API"| B
    ```

    Plex reads files directly from the debrid mount. cli_debrid uses the Plex API to trigger scans. **Plex only.**

=== "Symlink mode"

    ```mermaid
    flowchart LR
        A["Mount Service\ncli_mount / Decypharr / Zurg"] --> B["cli_debrid\ncreates symlinks"]
        B --> C["Symlink path\norganised folder structure"]
        C --> D["Media Server\nPlex / Jellyfin / Emby"]
        E["Debrid Service / Usenet"] --> A
        B --> E
        B -->|"triggers scan"| D
    ```

    cli_debrid creates symlinks from the mount into an organised folder. Your media server scans the symlink folder. **Works with Plex, Jellyfin, and Emby.**

---

!!! tip "Already have some of this set up?"
    Jump straight to whichever step you need. Each page is self-contained.
