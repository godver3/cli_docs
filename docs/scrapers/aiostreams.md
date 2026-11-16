---
title: AIOStreams
icon: material/magnify
---

# AIOStreams

AIOStreams is a self-hosted Stremio addon aggregator that combines multiple Stremio addons (Torrentio, MediaFusion, Comet, etc.) into a single endpoint. cli_debrid supports two integration modes.

---

## Prerequisites

- A running AIOStreams instance (self-hosted)
- Your AIOStreams URL, UUID, and password

---

## Configuration

=== "Stremio Endpoint"

    ### Connect to cli_debrid

    1. Go to **Settings → Scrapers**
    2. Click **Add Scraper** and select **AIOStreams (Stremio Endpoint)**
    3. Enter your AIOStreams manifest URL, e.g.:
       ```
       http://YOUR_AIOSTREAMS_IP:PORT/manifest.json
       ```
    4. Toggle **Enabled** on
    5. Click **Save Settings**

    ---

    ### Required AIOStreams configuration

    !!! warning "Additional setup required"
        Without the steps below, AIOStreams will not return usable results. The custom description template is required for cli_debrid to extract torrent information.

    **Step 1 — Install P2P-compatible addons**

    Add source addons that support P2P torrents — for example Comet, TorrentsDB, or MediaFusion. In each addon's settings, enable **Include P2P** or the equivalent option.

    !!! info "What 'P2P' means here"
        Enabling P2P in AIOStreams does **not** create direct peer-to-peer connections. It simply filters for torrent-based streams (infohashes) that cli_debrid can send to your debrid service. All downloading is handled through your debrid provider, not through direct P2P connections.

    **Step 2 — Configure stream type filters**

    1. Go to **AIOStreams → Filters → Stream Type**
    2. Set **P2P** as the **Primary Stream Type**
    3. Set **P2P** as a **Required Stream Type**

    **Step 3 — Set the custom description format**

    This template is required for cli_debrid to extract addon and indexer information from results.

    1. Go to **AIOStreams → Formatter**
    2. Under **Formatter Selection**, choose **Custom** from the dropdown
    3. Paste the following into the **Description Template** field:

    ```
    {stream.message::exists["ℹ️ {stream.message}"||""]}
    {stream.title::exists["📁 {stream.title::title}"||""]}{stream.year::exists[" ({stream.year})"||""]}{stream.seasonEpisode::exists[" {stream.seasonEpisode::join(' • ')}"||""]}
    {stream.filename::exists["ℹ️ {stream.filename}"||""]}
    {stream.infoHash::exists["ℹ️ {stream.infoHash}"||""]}
    {addon.name::exists["ℹ️ {addon.name}"||""]}
    {stream.indexer::exists["ℹ️ {stream.indexer}"||""]}
    {stream.quality::exists["🎥 {stream.quality} "||""]}{stream.encode::exists["🎞️ {stream.encode} "||""]}{stream.releaseGroup::exists["🏷️ {stream.releaseGroup}"||""]}
    {stream.visualTags::exists["📺 {stream.visualTags::join(' • ')} "||""]}{stream.audioTags::exists["🎧 {stream.audioTags::join(' • ')} "||""]}{stream.audioChannels::exists["🔊 {stream.audioChannels::join(' • ')}"||""]}
    {stream.size::>0["📦 {stream.size::bytes} "||""]}{stream.folderSize::>0["/ 📦 {stream.folderSize::bytes}"||""]}{stream.duration::>0["⏱️ {stream.duration::time} "||""]}{stream.age::exists["📅 {stream.age} "||""]}{stream.indexer::exists["🔍 {stream.indexer}"||""]}
    {stream.languageEmojis::exists["🌐 {stream.languageEmojis::join(' / ')}"||""]}
    ```

    **Step 4 — Optimise your filters**

    - Fine-tune resolution, quality, and content filters to match your use case
    - Disable addons or sources you don't need — fewer active sources means faster responses

    **Step 5 — Increase the scraper timeout**

    AIOStreams queries multiple addons simultaneously, which can be slow. The default cli_debrid timeout is too short.

    1. Go to **Settings → Scraping**
    2. Find **Scraper Timeout**
    3. Set it to **15 seconds minimum** — 20–30 seconds recommended

    !!! tip
        If AIOStreams returns no results after following all steps, the timeout is the most likely cause. Increase it first before troubleshooting elsewhere.

=== "API"

    ### Connect to cli_debrid

    1. Go to **Settings → Scrapers**
    2. Click **Add Scraper** and select **AIOStreams (API)**
    3. Fill in the fields:

        | Field | Description | Example |
        |---|---|---|
        | **Base URL** | Your AIOStreams instance URL — without `/api/v1` | `https://aiostreams.example.com` |
        | **UUID** | Your AIOStreams user UUID | `4110365a-df6e-41bb-bc98-5faadd054cdc` |
        | **Password** | Your AIOStreams password | |

    4. Toggle **Enabled** on
    5. Click **Save Settings**

    ---

    ### Required AIOStreams configuration

    !!! warning "Additional setup required"
        Without the steps below, AIOStreams will not return usable results.

    **Step 1 — Configure AIOStreams in Advanced mode**

    AIOStreams must be configured in **Advanced** mode. Take time to tune your filters carefully:

    - Set your resolution, quality, and content filters to match your use case
    - Disable addons or sources you don't need — fewer active sources means faster responses
    - The more precisely you filter, the less time cli_debrid spends waiting for results

    **Step 2 — Increase the scraper timeout**

    AIOStreams queries multiple addons and sources simultaneously, which can be slow. The default cli_debrid scraper timeout is too short.

    1. Go to **Settings → Scraping**
    2. Find **Scraper Timeout**
    3. Set it to **15 seconds minimum** — 20–30 seconds recommended

    !!! tip
        If AIOStreams returns no results after tuning your filters, the timeout is the most likely cause. Increase it first before troubleshooting elsewhere.

---

## Further reading

- [AIOStreams GitHub](https://github.com/aiostreams/aiostreams)
