---
title: Install cli_debrid
icon: material/download
---

# Step 3 — Install cli_debrid

Select your platform below. All methods install the same app — only the steps differ.

!!! info "Using cli_mount?"
    cli_mount runs as its own container next to cli_debrid (you set it up in [Step 2](mount.md)). Two things to get right:

    - **Same mount path in both containers.** Map your mount folder into cli_debrid (and your media server) at the same path cli_mount uses, so file paths line up.
    - **Reach cli_mount by IP, not `localhost`.** cli_debrid talks to cli_mount on port `8888` — use `http://YOUR_SERVER_IP:8888` (or the container name on a shared Docker network). `localhost:8888` clashes with cli_debrid's built-in Phalanx DB.

    - **Port 8888 clash.** The `docker-compose.yml` from the cli_debrid repo (used in the Quick Start) publishes port `8888` for Phalanx DB, which is also cli_mount's default port. If both run on the same host, remove the `"8888:8888"` line from cli_debrid's compose (Phalanx DB is optional and off unless you enable it), or publish cli_mount on a different host port.

    Optional: also map cli_mount's appdata folder into cli_debrid as `/climount_data` to enable cli_mount DB backup and cleanup tools.

---

=== "Unraid"

    The easiest method on Unraid is via Community Applications using the pre-configured template.

    **Full guide:** [:octicons-arrow-right-24: Unraid installation](../installation/unraid.md){ .md-button }

    **Quick steps:**

    1. Open the **Apps** tab in Unraid
    2. Search for `CLI_Debrid`
    3. Click **Install** on the template by **mash2k3**
    4. Set your paths and timezone
    5. Click **Apply**

    Once running, go to `http://YOUR_UNRAID_IP:5000`

=== "Docker / Linux"

    Works on any Linux host, macOS, or Windows with Docker Desktop.

    **Full guide:** [:octicons-arrow-right-24: Docker installation](../installation/docker.md){ .md-button }

    **Quick steps:**

    ```bash
    mkdir -p ~/cli_debrid && cd ~/cli_debrid
    curl -O https://raw.githubusercontent.com/godver3/cli_debrid/main/docker-compose.yml
    # Edit docker-compose.yml — update volume paths and timezone
    docker compose up -d
    ```

    Once running, go to `http://YOUR_SERVER_IP:5000`

=== "Ubuntu / Debian"

    **Full guide:** [:octicons-arrow-right-24: Ubuntu installation](../installation/ubuntu.md){ .md-button }

    **Quick steps:**

    1. Install Docker Engine (not Docker Desktop)
    2. Create your compose file with correct volume paths
    3. Run `docker compose up -d`

    Once running, go to `http://YOUR_SERVER_IP:5000`

=== "Proxmox"

    Run cli_debrid in an LXC container or a VM with Docker.

    **Full guide:** [:octicons-arrow-right-24: Proxmox installation](../installation/proxmox.md){ .md-button }

    **Recommended approach:** Use a Debian/Ubuntu LXC, install Docker inside it, then follow the Docker steps.

=== "TrueNAS"

    Run cli_debrid as a TrueNAS App (SCALE) or in a jail (CORE).

    **Full guide:** [:octicons-arrow-right-24: TrueNAS installation](../installation/truenas.md){ .md-button }

    **TrueNAS SCALE:** Use the Docker Compose method inside a Custom App or deploy via TrueCharts if available.

=== "Windows"

    A native Windows executable is available — no Docker required.

    **Full guide:** [:octicons-arrow-right-24: Windows installation](../installation/windows.md){ .md-button }

    !!! warning "Symlinks on Windows"
        Windows requires Developer Mode enabled for symlink support. Plex does not support symlinks on Windows — use Jellyfin instead, or run cli_debrid in Docker.

---

## First launch

Regardless of platform, when you first open `http://YOUR_IP:5000` you will see:

**Phalanx DB prompt** — Select **No / Disable** unless you specifically want this experimental feature.

The **onboarding wizard** will then launch automatically and guide you through initial configuration.

!!! tip
    Have your API keys and paths from [Step 1](prerequisites.md) and [Step 2](mount.md) ready before proceeding through onboarding.

---

## Next step

[:octicons-arrow-right-24: Step 4 — Configure cli_debrid](configure.md){ .md-button .md-button--primary }
