---
title: Notifications
icon: material/bell
---

# Notifications

cli_debrid can send notifications when items change state or the program starts/stops. You can add multiple notification services and configure each one independently.

To add a service go to **Settings → Notifications** and click **Add New Notification**, then select the type.

Each notification has a **Test** button to verify it is working before saving.

---

## Telegram

| Field | Required | Description |
|---|---|---|
| **Enabled** | — | Toggle this notification on/off |
| **Bot Token** | Yes | Your Telegram bot token from [@BotFather](https://t.me/BotFather) |
| **Chat ID** | Yes | The chat or channel ID to send messages to |
| **Notify On** | — | Which events trigger a notification (see below) |

**Getting your Bot Token and Chat ID:**

1. Message [@BotFather](https://t.me/BotFather) on Telegram and send `/newbot`
2. Follow the prompts — BotFather will give you the **Bot Token**
3. Add your bot to a channel or group, then message [@userinfobot](https://t.me/userinfobot) to get your **Chat ID**

---

## Discord

| Field | Required | Description |
|---|---|---|
| **Enabled** | — | Toggle this notification on/off |
| **Webhook URL** | Yes | Your Discord channel webhook URL |
| **Notify On** | — | Which events trigger a notification (see below) |

**Getting a Webhook URL:**

1. In Discord, go to your channel → **Edit Channel → Integrations → Webhooks**
2. Click **New Webhook**, give it a name, and click **Copy Webhook URL**

---

## NTFY

| Field | Required | Description |
|---|---|---|
| **Enabled** | — | Toggle this notification on/off |
| **Host** | Yes | Your NTFY server URL (e.g. `https://ntfy.sh`) |
| **Topic** | Yes | The NTFY topic to publish to |
| **API Key** | No | API key if your NTFY server requires authentication |
| **Priority** | No | Message priority: `min`, `low`, `default`, `high`, or `max` |
| **Notify On** | — | Which events trigger a notification (see below) |

---

## Email

| Field | Required | Description |
|---|---|---|
| **Enabled** | — | Toggle this notification on/off |
| **SMTP Server** | Yes | Your mail server hostname (e.g. `smtp.gmail.com`) |
| **SMTP Port** | Yes | Usually `587` (TLS) or `465` (SSL). Default: `587` |
| **SMTP Username** | No | SMTP authentication username (optional) |
| **SMTP Password** | No | SMTP authentication password (optional) |
| **From Address** | Yes | Sender email address |
| **To Address** | Yes | Recipient email address |
| **Notify On** | — | Which events trigger a notification (see below) |

---

## Notify On

Each notification service has a **Notify On** section to control which events trigger it.

| Event | Default | Description |
|---|---|---|
| **Collected** | On | An item has been successfully downloaded and added to the library |
| **Wanted** | Off | An item has been added to the Wanted queue |
| **Scraping** | Off | An item is being actively scraped |
| **Adding** | Off | An item is being added to debrid |
| **Checking** | Off | An item is in the Checking queue waiting to be confirmed |
| **Sleeping** | Off | An item has been moved to Sleeping (all known torrents blacklisted) |
| **Unreleased** | Off | An item is queued but not yet released |
| **Blacklisted** | Off | A torrent for an item has been blacklisted |
| **Pending Uncached** | Off | An item is waiting for an uncached torrent to finish downloading |
| **Upgrading** | Off | An item is being upgraded to a better version |
| **Program Stop** | On | The cli_debrid program has stopped |
| **Program Crash** | On | The cli_debrid program crashed |
| **Program Start** | On | The cli_debrid program has started |
| **Program Pause** | Off | The program has been paused. *Can be ticked, but cli_debrid doesn't currently send this notification.* |
| **Program Resume** | Off | The program has been resumed. *Can be ticked, but cli_debrid doesn't currently send this notification.* |
| **Queue Pause** | Off | A queue has been paused |
| **Queue Resume** | Off | A queue has been resumed |
| **Queue Start** | Off | A queue has been started |
| **Queue Stop** | Off | A queue has been stopped |

!!! note "Per-service defaults"
    Telegram defaults differ slightly — it does not include queue state events (Queue Pause/Resume/Start/Stop) and includes Program Pause/Resume instead.

---

## General Notification Options

| Setting | Default | Description |
|---|---|---|
| **Truncate Episode Notifications** | Off | Show only the first episode and a summary count instead of listing every episode in the notification |
| **Enabled Content Sources** | All | Filter notifications to only fire for specific content sources. Leave empty to include all. Hold Ctrl/Cmd to select multiple. |
