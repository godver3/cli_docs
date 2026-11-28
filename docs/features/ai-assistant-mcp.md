---
title: AI Assistant (MCP)
icon: material/robot-outline
---

# AI Assistant (MCP)

Connect Claude (Desktop or Code) or another MCP-capable AI assistant to Clyde. The assistant can then explain your settings, read your logs and help you troubleshoot. Open the page from **Tools → AI Assistant (MCP)**. You need to be an admin.

!!! note "Read-only"
    The assistant can look but never change anything. It tells you which setting to change and where. API keys, tokens and passwords are masked in everything it sees.

---

## Turn it on

1. Go to **Tools → AI Assistant (MCP)**
2. Tick **Turn on the MCP endpoint**

Clyde makes a token the first time you turn it on. The page then shows the URL, the token and the setup for your client.

---

## The token

Anyone with the token can read your settings (secrets masked), logs and library. Keep it private.

- **Show** / **Hide** reveals the token. Until you press Show, the commands below show `<token>` instead
- **Make a new token** replaces it. Clients using the old token stop working until you update them. Do this if the token leaks

---

## Connect your assistant

The page shows a ready-made setup for each client, with your URL and token filled in.

=== "Claude Code"
    Run this in a terminal:
    ```
    claude mcp add --transport http clyde http://YOUR-CLYDE:5000/mcp --header "Authorization: Bearer YOUR_TOKEN"
    ```

=== "Claude Desktop / other clients"
    Add this to the client's MCP config:
    ```json
    {
      "mcpServers": {
        "clyde": {
          "type": "http",
          "url": "http://YOUR-CLYDE:5000/mcp",
          "headers": { "Authorization": "Bearer YOUR_TOKEN" }
        }
      }
    }
    ```

Copy the text from the page rather than from here. It uses the address you opened Clyde with.

!!! warning "The URL must be reachable from where the assistant runs"
    If the assistant runs on another machine, or in the cloud, `localhost` won't work. Behind a reverse proxy, use your public Clyde address with `/mcp`, for example `https://clyde.example.com/mcp`. Anyone who can reach that address and has the token can read your data, so use HTTPS.

---

## What the assistant can see

| Tool | What it gives |
|---|---|
| `get_overview` | Version, whether Clyde is running, library mode, providers (which debrid accounts get new releases and which are streaming only), NFO mode, connection health and item counts. Start here |
| `list_settings` | The settings sections, or every setting in one section with its value (secrets masked), default, choices and description. Includes NFO, Upgrade Hub and preset collections |
| `explain_setting` | One setting: what it does, its value, default and choices |
| `search_logs` | Search recent log lines, from Clyde or the built-in mount |
| `recent_errors` | The latest warnings and errors |
| `queue_status` | Whether Clyde is running and how many items are in each state (Wanted, Scraping, Checking and so on) |
| `mount_status` | The built-in mount: engine state, problems, servers, cache and open files |
| `connection_health` | Which services (debrid, Plex, scrapers, content sources) are reachable |
| `external_scan_status` | Files found on the mount that were added outside Clyde, and whether they imported |
| `lookup_item` | A movie or episode by title or IMDb ID: state, version, release, file and related log lines |
| `get_help` | Clyde's built-in help pages |
| `prepare_issue_report` | Gathers what a bug report needs. Nothing is sent anywhere |

---

## Things to ask

- "Give me an overview of my Clyde setup. Anything wrong?"
- "Why is *Movie Name* stuck in Checking?"
- "What errors showed up in the logs today?"
- "What does the Upgrade Hub scan setting do, and what is mine set to?"
- "Is my debrid connection healthy?"
- "Did Clyde pick up the files I added through DMM?"
- "Help me write a bug report about this."

---

## Troubleshooting

| Problem | Cause |
|---|---|
| 404 "MCP is turned off" | The checkbox on the page is off |
| 401 "invalid or missing MCP token" | The token is wrong or was replaced. Copy the new setup from the page |
| Client can't connect | The URL isn't reachable from where the assistant runs. Check your reverse proxy forwards `/mcp` |
