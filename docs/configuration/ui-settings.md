---
title: UI Settings
icon: material/monitor
---

# UI Settings

---

## Appearance

| Setting | Default | Description |
|---|---|---|
| **Program Logo** | Default | Logo displayed in the UI — Default, Plex-Inspired, or Color Icon. Credits to @mrcuriousny for the Plex-Inspired logo. |
| **Compact View** | Off | Use compact view for the statistics page |
| **Hide Support Message** | Off | Hide the Patreon support message in the header |

---

## Date & Time Formatting

| Setting | Default | Description |
|---|---|---|
| **Use 24-Hour Format** | Off | Use 24-hour time format instead of 12-hour |
| **Date Format** | `%b %d, %Y` | Preferred date format string. Click the info button in the UI for available parameters. |
| **Time Format** | `%H:%M:%S` | Preferred time format string. Click the info button in the UI for available parameters. |

---

## Statistics Display

| Setting | Default | Description |
|---|---|---|
| **Recently Added Limit** | `14` | Number of items shown in the Recently Added section on the statistics page |
| **Recently Upgraded Limit** | `7` | Number of items shown in the Recently Upgraded section on the statistics page |
| **Upcoming Releases Start Limit** | `7` | How many days back to show (`0` = today, `7` = one week back) |
| **Upcoming Releases End Limit** | `365` | How many days forward to show on the statistics page |
| **Stats Provider Priority** | `auto` | Whose stats the Statistics page shows: `auto` (debrid if configured, otherwise Usenet), `debrid`, `usenet` (cli_mount stats even when debrid is also set up), or `combined` (total size and broken count across all debrid providers and Usenet — no subscription days) |

---

## System Behavior

| Setting | Default | Description |
|---|---|---|
| **Enable User System** | Off | Enable the user account system with roles |
| **Auto Run Program** | Off | Automatically start the program running when the application starts |
| **Disable Initialization** | Off | Skip the initialization process on startup — useful for testing or manual control |
| **Disable Auto Browser** | Off | Disable automatic browser launch on Windows systems |
| **Enable Caching** | Off | Enable web caching and compression for faster page loads. Disable if experiencing issues with updates not appearing. |
