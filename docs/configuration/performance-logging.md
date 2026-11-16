---
title: Performance & Logging
icon: material/speedometer
---

# Performance & Logging

**Settings → Performance & Logging** holds logging, metadata freshness, load limits and Phalanx DB.

---

## System & Logging

| Setting | Default | Description |
|---|---|---|
| **Logging Level** | `DEBUG` | Detail level for the console and log files |
| **Timezone Override** | — | Use this timezone instead of the system's (e.g. `America/New_York`) |
| **Enable Tracemalloc** | Off | Track memory use per task with Python's tracemalloc. Adds overhead; for chasing memory leaks only. |
| **Tracemalloc Sample Rate** | `100` | Sample 1 in this many tasks. Lower gives more data and more overhead. |
| **Check For Updates** | On | Check for new versions and show an indicator in the header |

---

## Performance & Monitoring

| Setting | Default | Description |
|---|---|---|
| **Staleness Threshold (Days)** | `7` | Days before stored metadata is refreshed |
| **Cpu Threshold Percent** | `75` | CPU use that makes cli_debrid slow down |
| **Ram Threshold Percent** | `75` | RAM use that makes cli_debrid slow down |
| **Regulation Increase Step Seconds** | `1.0` | How much the pause between tasks grows while load is high |
| **Regulation Decrease Step Seconds** | `1.0` | How much it shrinks once load is back to normal |
| **Regulation Max Sleep Seconds** | `60.0` | Longest pause the regulation can set |

The load settings only apply while the **Slow down under high system load** task is on (on the [Automation](../features/automation.md) page, System group). It's on by default in limited installs.

---

## Phalanx DB Settings

| Setting | Default | Description |
|---|---|---|
| **Enable Phalanx DB** | Off | Join the [Phalanx DB](../features/phalanx-db.md) peer network. Needs a restart. Optional; turning it off doesn't affect anything else. |
