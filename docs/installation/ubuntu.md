---
title: Ubuntu / Debian
icon: simple/ubuntu
---

# Install on Ubuntu / Debian

This guide covers installing Clyde on a bare-metal or VM Ubuntu/Debian server using Docker Engine.

!!! warning "Use Docker Engine, not Docker Desktop"
    On Linux servers, install Docker Engine directly. Docker Desktop on Linux runs in a VM and causes mount and permission issues.

---

## Prerequisites

- Ubuntu 22.04 / 24.04 or Debian 12 (recommended)
- A user with `sudo` access
- Your debrid mount already working (Zurg + rclone or Decypharr) — see [Step 2](../getting-started/mount.md)

---

## Step 1 — Install Docker Engine

```bash
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
newgrp docker
```

Verify:
```bash
docker --version
docker compose version
```

---

## Step 2 — Create directories

```bash
mkdir -p ~/cli_debrid/{db_content,config,logs}
cd ~/cli_debrid
```

---

## Step 3 — Create the compose file

```bash
nano docker-compose.yml
```

Paste:

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
          - ~/cli_debrid/db_content:/user/db_content
          - ~/cli_debrid/config:/user/config
          - ~/cli_debrid/logs:/user/logs
          - /path/to/your/debrid/mount:/media/mount          # e.g. /mnt/zurg, /mnt/data/debrid
          - /path/to/plex/Library/Application Support/Plex Media Server:/plex_data  # optional — overlay feature
        environment:
          - TZ=America/New_York                              # your timezone
          - MALLOC_ARENA_MAX=2                               # optional — limits glibc memory arenas, reduces memory fragmentation in Python apps
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
          - ~/cli_debrid/db_content:/user/db_content
          - ~/cli_debrid/config:/user/config
          - ~/cli_debrid/logs:/user/logs
          - /path/to/your/debrid/mount:/media/mount          # e.g. /mnt/zurg, /mnt/data/debrid — must match media server
          - /path/to/your/symlinks:/mnt/symlinked            # e.g. /mnt/symlinks — must match media server
          - /path/to/plex/Library/Application Support/Plex Media Server:/plex_data  # optional — overlay feature, Plex only
        environment:
          - TZ=America/New_York                              # your timezone
          - MALLOC_ARENA_MAX=2                               # optional — limits glibc memory arenas, reduces memory fragmentation in Python apps
        restart: unless-stopped
        tty: true
        stdin_open: true
    ```

---

## Step 4 — Start the container

```bash
docker compose up -d
docker compose logs -f
```

You should see:
```
cli_debrid  | Web interface available at http://0.0.0.0:5000
```

Press `Ctrl+C` to stop following logs.

---

## Step 5 — Access the web UI

```
http://YOUR_SERVER_IP:5000
```

Complete the onboarding wizard. See [Step 4 — Configure](../getting-started/configure.md) for what to enter.

---

## Updating

```bash
cd ~/cli_debrid
docker compose pull && docker compose up -d
```

---

## Next step

[:octicons-arrow-right-24: Back to Getting Started — Configure](../getting-started/configure.md){ .md-button .md-button--primary }
