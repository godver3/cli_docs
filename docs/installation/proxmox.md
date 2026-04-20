---
title: Proxmox
icon: simple/proxmox
---

# Install on Proxmox

The recommended approach is to run cli_debrid inside a **Debian/Ubuntu LXC container** with Docker installed. This gives you an isolated environment that's easy to snapshot and restore.

---

## Option A — Debian LXC with Docker (recommended)

### Step 1 — Create an LXC container

In the Proxmox web UI:

1. Click **Create CT**
2. Use the **Debian 12** or **Ubuntu 24.04** template
3. Recommended specs:
    - **CPU:** 2 cores
    - **RAM:** 2 GB (4 GB if running other services)
    - **Disk:** 10 GB (cli_debrid itself is small — data is on your debrid cloud)
4. Set a static IP or use DHCP with a reserved address

!!! important "Privileged container for mounts"
    If you plan to pass your debrid mount (Zurg/rclone or Decypharr) into the LXC, you may need a **privileged** container or configure bind mounts from the Proxmox host. See the note below.

### Step 2 — Install Docker inside the LXC

SSH into the container, then:

```bash
curl -fsSL https://get.docker.com | sh
usermod -aG docker $USER
newgrp docker
```

### Step 3 — Deploy cli_debrid

=== "Docker Compose / Ubuntu guide"

    Follow the [Ubuntu installation guide](ubuntu.md) to create the compose file and start cli_debrid.

=== "Portainer / Dockge / Dockhand"

    If you have Portainer, Dockge, or Dockhand running inside or alongside your LXC, paste the compose file from the [Docker guide](docker.md) into your stack editor and deploy.

    - **Portainer:** Stacks → Add Stack → paste → Deploy
    - **Dockge:** + Compose → paste → Deploy
    - **Dockhand:** Stacks → + Create → paste → Create & Start

---

## Passing in your debrid mount

If your debrid mount (Zurg + rclone or Decypharr) is running on the Proxmox host or another LXC, you need to bind-mount the path into your cli_debrid LXC.

In `/etc/pve/lxc/YOUR_CTID.conf` on the Proxmox host, add a line pointing to your mount path:

=== "Zurg + rclone"
    ```
    mp0: /mnt/zurg,mp=/mnt/zurg
    ```

=== "Decypharr"
    ```
    mp0: /path/to/debrid,mp=/path/to/debrid
    ```

Then restart the container:

```bash
pct restart YOUR_CTID
```

The mount will appear at the same path inside the container.

!!! warning "Privileged containers only"
    Bind mounts with FUSE filesystems (rclone/Decypharr) typically require a privileged LXC. Unprivileged containers may block FUSE access.

---

## Option B — VM with Docker

Create a standard Debian/Ubuntu VM and follow the [Ubuntu installation guide](ubuntu.md). Mounts are simpler in a full VM since there are no LXC restrictions.

---

## Next step

[:octicons-arrow-right-24: Back to Getting Started — Configure](../getting-started/configure.md){ .md-button .md-button--primary }
