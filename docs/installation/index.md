---
title: Installation Overview
icon: material/download
---

# Installation

cli_debrid runs as a Docker container and is the recommended installation method for all platforms. A Windows executable is also available for users who prefer not to use Docker.

---

## Choose your platform

<div class="grid cards single-col" markdown>

- ## :material-docker:{ .lg .middle } Docker

    **Recommended.** Works on any Linux, macOS, or Windows host with Docker installed. The most reliable and easiest to update.

    [:octicons-arrow-right-24: Docker Guide](docker.md){ .md-button .md-button--primary }

- ## :simple-unraid:{ .lg .middle } Unraid

    Install via Community Applications or Compose Manager.

    [:octicons-arrow-right-24: Unraid Guide](unraid.md){ .md-button }

- ## :material-view-dashboard:{ .lg .middle } Portainer / Dockge / Dockhand

    Install using any Docker compose GUI — works on any platform.

    [:octicons-arrow-right-24: Portainer / Dockge / Dockhand Guide](portainer-dockge.md){ .md-button }

- ## :simple-ubuntu:{ .lg .middle } Ubuntu / Debian

    Bare-metal or VM install using Docker Engine on Ubuntu or Debian.

    [:octicons-arrow-right-24: Ubuntu / Debian Guide](ubuntu.md){ .md-button }

- ## :simple-proxmox:{ .lg .middle } Proxmox

    Run inside a Debian/Ubuntu LXC container or VM with Docker.

    [:octicons-arrow-right-24: Proxmox Guide](proxmox.md){ .md-button }

- ## :simple-truenas:{ .lg .middle } TrueNAS

    Deploy via Custom App (SCALE) or inside a Linux VM (CORE).

    [:octicons-arrow-right-24: TrueNAS Guide](truenas.md){ .md-button }

- ## :material-microsoft-windows:{ .lg .middle } Windows

    Native Windows executable — no Docker required. Best for users running directly on Windows without a NAS or server.

    [:octicons-arrow-right-24: Windows Guide](windows.md){ .md-button }

</div>

---

## Before you begin

Regardless of platform, you will need the following before setting up cli_debrid:

| Requirement | Notes |
|---|---|
| **Debrid account** | Real-Debrid, AllDebrid, Premiumize, Torbox, or Debrid-Link |
| **Plex, Jellyfin, or Emby** | For library management and media scanning |
| **Mount tool** | [Zurg + rclone](../integrations/zurg.md) or [Decypharr](../integrations/decypharr.md) to mount your debrid storage as a local filesystem |

!!! tip "Set up your mount first"
    cli_debrid needs your debrid storage mounted as a local filesystem before it can manage your library. Set up [Zurg + rclone](../integrations/zurg.md) or [Decypharr](../integrations/decypharr.md) before installing cli_debrid.

---

## Community quick-install script

For experienced Linux users who want to get a full stack running in one go, there is a community-maintained setup script that automates the entire process.

!!! warning "Review before running"
    This script is **not officially maintained by the cli_debrid project** — it is a community contribution. It runs as root and installs Docker, rclone, and multiple containers automatically. Review the script before running it on any system you care about.

The script handles:

- Docker and rclone installation
- OS and architecture detection
- Interactive selection of media server, request manager, and optional components
- Full `docker-compose.yml` generation
- Backup, restore, update, and repair utilities

```bash
sudo curl -sO https://raw.githubusercontent.com/delete2020/cli_debrid-setup-/main/setup.sh && sudo chmod +x setup.sh && sudo ./setup.sh
```

---

## Updating

Once installed, see the [Updating](updating.md) guide to keep cli_debrid current.
