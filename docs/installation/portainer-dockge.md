---
title: Portainer / Dockge / Dockhand
icon: material/docker
---

# Portainer / Dockge / Dockhand

These GUI tools let you manage Docker containers and compose stacks through a web interface. All three work with the same Docker Compose file — just paste it into the stack editor.

!!! tip "Stack all services in one compose file"
    You can combine cli_debrid, Zurg/Decypharr, Plex, and Jellyfin into a single compose file by adding each as a separate service under the same `services:` block. This lets you manage your entire media stack from one place and start/stop everything with a single deploy.

---

## Docker Compose file

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
          - /path/to/appdata/db_content:/user/db_content        # e.g. /mnt/cache/appdata/cli_debrid/db_content
          - /path/to/appdata/config:/user/config                 # e.g. /mnt/cache/appdata/cli_debrid/config
          - /path/to/appdata/logs:/user/logs                     # e.g. /mnt/cache/appdata/cli_debrid/logs
          - /path/to/your/debrid/mount:/media/mount              # e.g. /mnt/cache/zurg, /mnt/data/debrid
          - /path/to/plex/appdata/Library/Application Support/Plex Media Server:/plex_data  # overlay feature
        environment:
          - TZ=America/New_York                                  # change to your timezone
          - MALLOC_ARENA_MAX=2                                   # optional — limits glibc memory arenas, reduces memory fragmentation in Python apps
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
          - /path/to/appdata/db_content:/user/db_content        # e.g. /mnt/cache/appdata/cli_debrid/db_content
          - /path/to/appdata/config:/user/config                 # e.g. /mnt/cache/appdata/cli_debrid/config
          - /path/to/appdata/logs:/user/logs                     # e.g. /mnt/cache/appdata/cli_debrid/logs
          - /path/to/your/debrid/mount:/media/mount              # e.g. /mnt/cache/zurg, /mnt/data/debrid — must match media server
          - /path/to/your/symlinks:/mnt/symlinked                # e.g. /mnt/disk1/TVShows — must match media server
          - /path/to/plex/appdata/Library/Application Support/Plex Media Server:/plex_data  # overlay feature (Plex only)
        environment:
          - TZ=America/New_York                                  # change to your timezone
          - MALLOC_ARENA_MAX=2                                   # optional — limits glibc memory arenas, reduces memory fragmentation in Python apps
        restart: unless-stopped
        tty: true
        stdin_open: true
    ```

    !!! warning "Container paths must match your media server"
        The debrid mount and symlink folder must use **identical container paths** in both cli_debrid and your media server. If they differ, symlinks will appear broken. See [Plex](../integrations/plex.md) and [Jellyfin](../integrations/jellyfin.md) guides.

!!! warning "Unraid users"
    Use the actual pool path for your volumes (e.g. `/mnt/cache/appdata/cli_debrid`), not the user share path (`/mnt/user/...`). This avoids array startup issues.

---

## Portainer

1. Open Portainer (default port: `9000` or `9443`)
2. Go to **Stacks → Add Stack**
3. Name it `cli_debrid`
4. Paste the compose file above into the web editor
5. Click **Deploy the stack**

---

## Dockge

1. Open Dockge (default port: `5001` — conflicts with cli_debrid's port 5001, adjust if needed)
2. Click **+ Compose** to create a new stack
3. Name it `cli_debrid`
4. Paste the compose file above
5. Click **Deploy**

---

## Dockhand

1. Open Dockhand and go to **Stacks → + Create**
2. Enter `cli_debrid` as the stack name
3. Paste the compose file above into the editor
4. Click **Create & Start**

---

## Next steps

- [Configure cli_debrid](../getting-started/configure.md)
- [Set up your debrid mount](../getting-started/mount.md)
