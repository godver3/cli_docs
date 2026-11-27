---
title: NFO Files
icon: material/file-document-outline
---

# NFO Files

NFO files are small XML files next to your episodes that tell the media server exactly which episode each file is, with its title, description and air date. Clyde can write them for your TV library and set Plex up to read them. Open the page from **Tools → NFO Files**. Added in 0.9.1.

!!! warning "Why this matters from 3 December 2026"
    On **3 December 2026** Plex stops using TheTVDB. After that it can only fill in TV episodes from TMDB, and it numbers shows the TMDB way. Clyde keeps naming episodes the TVDB way (aired, DVD, absolute, alternate…) or by the TMDB episode group you picked for a show. Where the two disagree, Plex shows the wrong episode titles and details. Many anime and any show with a custom order are affected. NFO files make Plex follow Clyde's numbering.

!!! note "Symlinked/Local only"
    NFO files need **Symlinked/Local** file management: Clyde writes them next to your symlinks. In Direct Mount mode there's no library folder to write to, so the page only explains this.

Plex, Jellyfin, Emby and Kodi all read the same files.

---

## Save Plex's current episode details (snapshot)

**Snapshot Plex now** reads what Plex shows today for every episode of the TV library that holds your symlinks, and saves it as NFO files next to the episodes. That includes TheTVDB titles, descriptions and air dates, and anything you edited by hand. It also writes a `tvshow.nfo` with each show's IDs.

- **Take it before 3 December.** After that date Plex may already show TMDB's details for shows it refreshed, so a new snapshot would save those instead
- **Plex isn't changed**, and you don't need to turn NFO files on. The files wait until you switch Plex (or Jellyfin, Emby, Kodi) to an agent that reads NFO files
- **Nothing of yours is replaced.** NFO files you made yourself, and the ones Clyde writes for an NFO mode below, are never overwritten by a snapshot
- **Upgrades keep their NFO.** When an episode is upgraded, its snapshot NFO moves to the new file. Deleting an episode deletes its NFO
- **Every snapshot is kept** with its date in `plex_metadata_snapshot.db`, so a later snapshot doesn't overwrite an earlier one. From the list you can **Use this one** to write an older snapshot back into the library, **Rewrite** the one in use, or **Delete snapshot NFO files**

---

## NFO files for your TV library

Pick one of three modes:

| Mode | What it does |
|---|---|
| **Off** (default) | No NFO files; Plex shows its own details, exactly as before. Shows whose numbering differs from Plex's will show Plex's episode details from 3 December |
| **Shows with a changed episode order** | NFO files only for shows you set to another order in **Show options** or **Manual Assign**, written as soon as you change it. Every other show looks exactly as Plex makes it |
| **All shows** | Every show gets NFO files. Also fixes default-order shows that TMDB numbers differently (many anime) |

**Looks like Plex's own agent.** When Plex already numbers an episode the same way, Clyde writes a minimal NFO, so Plex still fills in its title, description, thumbnail and cast. Only episodes Plex would mix up get the right episode's details: title, description, air date, thumbnail, director, writers and guest stars. The show's title, artwork, cast and ratings stay Plex's.

**What's written:** `tvshow.nfo` (IDs only) in each show folder and one `.nfo` per episode file, kept up to date as episodes are added, upgraded, removed or renumbered. Clyde marks the files it writes and only ever changes those; NFO files you made yourself are never changed or deleted.

**Turning NFO files off** puts Plex's previous agent back and deletes only the NFO files Clyde wrote. If you took a snapshot, its NFO files come back in their place.

### Per show

Under **Check a show in Plex**, find a show to see its order, file count and whether it gets NFO files. For each show you can choose:

- **Follow the mode** (default)
- **Always full details**: write the full episode details even where Plex numbers the episode the same way
- **No NFO files**: never write NFO files for this show

---

## Plex agent

Plex only reads NFO files through an agent that supports them. When you turn NFO files on, Clyde by default:

1. creates a Plex agent called **Clyde NFO + Plex Series**: the NFO file first, then Plex Series for anything the NFO doesn't say (cast, artwork, Discover), then local media
2. switches the TV library that reads your symlinks to it
3. refreshes that library

Shows keep their Plex identity, so watch history and collections stay. Shows without NFO files keep matching through Plex Series exactly as before. Needs **Plex Media Server 1.43.1 or newer**.

**Leave Plex alone instead:** untick **Switch my Plex TV library to the NFO agent when NFO files are turned on**. The NFO files are still written, and Plex stays exactly as it is (its agent, episode ordering and titles). You can switch later.

The **Plex** card shows each TV library, its folders and the agent it uses, with:

| Button | What it does |
|---|---|
| **Set up Plex agent** | Switch the TV libraries that read the symlinked folder to the NFO agent and refresh them |
| **Restore Plex's previous agent** | Put the TV libraries back on the agent they had before and refresh them |
| **Check** | Re-read the libraries and agents from Plex |

---

## Library tools

**Convert entire library** rewrites every show's NFO files, then sets up Plex and refreshes the library in one go.

**Check a show in Plex** compares every episode file of a show with what Plex shows for that season and episode. It lists episodes that are wrong or not in Plex, and has a **Fix** button that rewrites the show's NFO files and refreshes it in Plex.

---

## Troubleshooting

**Plex still shows the wrong episode titles**

- Check that the TV library uses **Clyde NFO + Plex Series** in the Plex card (or click **Set up Plex agent**)
- Use **Check a show in Plex**, then **Fix**. Absolute-numbered shows can take a few minutes longer for Plex to refresh
- Make sure the show gets NFO files: in **Shows with a changed episode order** mode only shows with a changed order do

**The NFO Files page says it needs Symlinked/Local**

- NFO files are written next to your symlinks. In Direct Mount mode there's no library folder Clyde can write to

**I have my own NFO files**

- They're left alone. Clyde only changes files it wrote itself and reports the rest as "left alone (not written by Clyde)"

**Movies**

- NFO files are for TV episodes only. Plex's movie agent is not affected by the TheTVDB change
