---
title: OpenClaw
icon: material/robot
---

# OpenClaw

OpenClaw is a self-hosted AI gateway that powers the [AI Butler](../features/ai-butler.md) inside cli_debrid. It handles session memory, AI provider routing, and can be used standalone via Telegram, Discord, WhatsApp, and other messaging platforms.

- **GitHub:** [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
- **Docs:** [docs.openclaw.ai](https://docs.openclaw.ai)
- **Default port:** `18789`
- **API:** OpenAI-compatible (`POST /v1/chat/completions`)

---

## Requirements

- Docker (recommended) or Node.js 22.16+
- Minimum 2 GB RAM
- An API key from an AI provider (Anthropic, OpenAI, Google, or a self-hosted model via Ollama/vLLM)

!!! tip "Paid AI API recommended"
    Works best with a paid API (OpenAI, Anthropic, Gemini). Free tier models may lack the context window or tool-calling capability needed for reliable responses.

---

## Installation

=== "Linux / macOS / WSL2"

    ```bash
    curl -fsSL https://openclaw.ai/install.sh | bash
    ```

=== "Windows (PowerShell)"

    ```powershell
    iwr -useb https://openclaw.ai/install.ps1 | iex
    ```

=== "Docker (recommended)"

    ```bash
    git clone https://github.com/openclaw/openclaw.git

    cd openclaw
    ./scripts/docker/setup.sh
    ```

    Or using the pre-built image:

    ```bash
    export OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"
    ./scripts/docker/setup.sh
    ```

=== "Unraid"

    1. Go to **Community Apps** and search for `openclaw`
    2. Install the template
    3. Set the config path to your preferred appdata location
    4. Start the container

=== "Portainer / Dockge / Dockhand"

    ```yaml
    services:
      openclaw:
        image: ghcr.io/openclaw/openclaw:latest
        container_name: openclaw
        ports:
          - "18789:18789"
        volumes:
          - /path/to/appdata/openclaw:/config
        restart: unless-stopped
    ```

    Paste into your stack editor and deploy.

---

## Onboarding

After installation, run the onboarding wizard to configure your AI provider, port, and auth:

```bash
openclaw onboard --install-daemon
# or with Docker:
docker compose run --rm openclaw-cli onboard
```

The wizard walks you through:

1. Selecting an AI provider and entering your API key
2. Setting the gateway port (default `18789`)
3. Choosing an authentication mode (token recommended)
4. Installing as a background daemon

**Access the dashboard:**

```bash
openclaw dashboard
# or with Docker:
docker compose run --rm openclaw-cli dashboard --no-open
```

Then open `http://127.0.0.1:18789/` in your browser.

---

## Enable required HTTP endpoints

!!! warning "Required step"
    Before cli_debrid can communicate with OpenClaw, two HTTP endpoints must be enabled. Without these the connection will fail silently.

1. Open the OpenClaw dashboard (`http://your-openclaw-url/`)
2. Go to **Settings → Infrastructure → Gateway HTTP API → Gateway HTTP Endpoints**
3. Enable **Chat Completions**
4. Enable **Responses**
5. Save the changes

These expose the OpenAI-compatible API that cli_debrid uses to send and receive messages.

---

## Connecting to cli_debrid

1. Open the AI Butler settings — click the **⚙ cog** in the chat header, or go to **Settings → Additional Settings → AI Assistant**
2. Set **OpenClaw URL** to the URL OpenClaw is listening on (must be reachable from inside the cli_debrid container)
3. Set **Bearer Token** to match the token configured in OpenClaw. Leave blank if no auth is configured.
4. Set **Agent ID** to `main` (or the ID of the agent you configured)
5. Set **Display Name** to your agent's name (found in its `IDENTITY.md` file in the workspace)
6. Click **Save** — the status dot will turn green if the connection succeeds

!!! note "Container networking"
    The OpenClaw URL must be reachable from **inside the cli_debrid Docker container**, not just from your browser. If you use a reverse proxy or Tailscale, use the internal/container-reachable address.

---

## Skill file (Tool API)

The skill file tells OpenClaw how to call back into cli_debrid's tool API so the AI can check queue status, search your library, trigger tasks, and more — from any connected messaging platform (Telegram, Discord, etc.).

### Install the skill

1. Go to **Settings → Additional Settings → AI Assistant**
2. Click **Download OpenClaw Skill File**
3. Drop the downloaded `cli_debrid_skill.md` into your OpenClaw workspace directory:
    - Default: `~/.openclaw/workspace/`
    - Docker: the `workspace/` folder in your Docker volume
4. Reload OpenClaw and assign the skill to your agent

The skill file is pre-filled with your cli_debrid URL and bearer token.

!!! warning "Security note"
    This skill requires cli_debrid to be publicly accessible — it cannot work via an internal IP only. Exposing cli_debrid publicly means anyone with your token can control it, so **User Management must be enabled** before downloading. For best security, use OIDC/SSO (e.g. Authentik) rather than local accounts.

---

## Available tools

Once the skill is installed, your OpenClaw agent can:

| Tool | Description |
|---|---|
| **queue_status** | Get current queue counts and whether the program is running |
| **library_stats** | Total movies/shows/episodes, wanted, blacklisted, collected in last 24h |
| **recently_collected** | List the most recently downloaded items (default 20, max 50) |
| **search_library** | Search your library by title — check if something is collected |
| **add_to_library** | Add a movie or TV show to the wanted list |
| **send_notification** | Send a message via your configured notification channels (Discord, Telegram, etc.) |

### Example prompts

```
What is currently downloading?
How many items are in the queue?
Is Breaking Bad in my library?
What was recently collected?
How many movies do I have?
Add The Bear (2022) to my library
Is the program running?
Send me a notification about the current queue status
```

---

## Authentication

The skill authenticates to cli_debrid via a query parameter (`?token=<value>`) rather than an Authorization header, for compatibility with clients that cannot set custom headers.

The token is the same value set in **Settings → Additional Settings → AI Assistant → OpenClaw Token** — it is the token OpenClaw uses to authenticate *to* cli_debrid, not a separate password.

---

## Troubleshooting

**Status dot is red**

- Check OpenClaw is running: `curl http://your-openclaw-url/healthz`
- Verify the URL is reachable from inside the cli_debrid container (not just your browser)
- Confirm the bearer token matches what OpenClaw expects

**Connection fails silently**

- Make sure Chat Completions and Responses endpoints are enabled in the OpenClaw dashboard (see [Enable required HTTP endpoints](#enable-required-http-endpoints))
