---
title: TrueNAS
icon: simple/truenas
---

# Install on TrueNAS

Installation method depends on whether you're running **TrueNAS SCALE** (Linux-based) or **TrueNAS CORE** (FreeBSD-based).

---

## TrueNAS SCALE

=== "Discover Apps (Electric Eel+)"

    In TrueNAS SCALE 24.10 (Electric Eel) and later, you can search for cli_debrid directly in the app catalog:

    1. Go to **Apps → Discover Apps**
    2. Search for `cli_debrid`
    3. Click **Install**
    4. Fill in the required paths and timezone
    5. Click **Save**

    !!! note
        If cli_debrid is not yet in the official catalog, use the Custom App method below.

=== "Custom App"

    Works on all SCALE versions. Uses the Docker Compose format.

    1. Go to **Apps → Discover Apps → Custom App**
    2. Choose **Docker Compose** as the install method
    3. Paste the compose file from the **Compose file** tab below
    4. Click **Install**

=== "Portainer / Dockge / Dockhand"

    If you have Portainer, Dockge, or Dockhand running on TrueNAS, paste the compose file into your stack editor and deploy.

    - **Portainer:** Stacks → Add Stack → paste → Deploy
    - **Dockge:** + Compose → paste → Deploy
    - **Dockhand:** Stacks → + Create → paste → Create & Start

---

## Compose file

Choose the mode that matches your setup:

=== "Direct Mount"

    ```yaml title="docker-compose.yml"
    services:
      cli_debrid:
        image: godver3/cli_debrid:dev
        pull_policy: always
        container_name: cli_debrid
        ports:
          - "5000:5000"
          - "5001:5001"
        volumes:
          - /mnt/tank/appdata/cli_debrid/db_content:/user/db_content    # replace /mnt/tank with your pool name
          - /mnt/tank/appdata/cli_debrid/config:/user/config
          - /mnt/tank/appdata/cli_debrid/logs:/user/logs
          - /path/to/your/debrid/mount:/media/mount                     # e.g. /mnt/tank/zurg, /mnt/tank/debrid
          - /path/to/plex/Library/Application Support/Plex Media Server:/plex_data  # optional — overlay feature
        environment:
          - TZ=America/New_York
          - MALLOC_ARENA_MAX=2                                           # optional — limits glibc memory arenas, reduces memory fragmentation in Python apps
        restart: unless-stopped
        tty: true
        stdin_open: true
    ```

=== "Symlink mode"

    ```yaml title="docker-compose.yml"
    services:
      cli_debrid:
        image: godver3/cli_debrid:dev
        pull_policy: always
        container_name: cli_debrid
        ports:
          - "5000:5000"
          - "5001:5001"
        volumes:
          - /mnt/tank/appdata/cli_debrid/db_content:/user/db_content    # replace /mnt/tank with your pool name
          - /mnt/tank/appdata/cli_debrid/config:/user/config
          - /mnt/tank/appdata/cli_debrid/logs:/user/logs
          - /path/to/your/debrid/mount:/media/mount                     # e.g. /mnt/tank/zurg — must match media server
          - /path/to/your/symlinks:/mnt/symlinked                       # e.g. /mnt/tank/symlinks — must match media server
          - /path/to/plex/Library/Application Support/Plex Media Server:/plex_data  # optional — overlay feature, Plex only
        environment:
          - TZ=America/New_York
          - MALLOC_ARENA_MAX=2                                           # optional — limits glibc memory arenas, reduces memory fragmentation in Python apps
        restart: unless-stopped
        tty: true
        stdin_open: true
    ```

!!! note "Adjust paths"
    Replace `/mnt/tank` with your actual pool name. Replace the debrid mount path with your actual mount location.

!!! tip "Stack all services in one compose file"
    You can combine cli_debrid, Zurg/Decypharr, Plex, and Jellyfin into a single compose file by adding each as a separate service under the same `services:` block.

---

## TrueNAS CORE

CORE uses FreeBSD jails. The recommended approach is to create a Linux VM using TrueNAS CORE's VM feature, then follow the [Ubuntu installation guide](ubuntu.md) inside it.

Alternatively, install Docker inside a FreeBSD jail using `linux_enable` — but this is complex and not officially supported.

!!! tip "Consider migrating to SCALE"
    TrueNAS SCALE is the actively developed version and makes Docker much easier. If you're on CORE primarily for jails, consider SCALE with the Discover Apps or Custom App method above.

---

## Accessing the UI

```
http://YOUR_TRUENAS_IP:5000
```

---

## Next step

[:octicons-arrow-right-24: Back to Getting Started — Configure](../getting-started/configure.md){ .md-button .md-button--primary }
