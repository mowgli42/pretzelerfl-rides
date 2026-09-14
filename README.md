# PretzelerFL rides

Personal Overcast ride queue of curated ~25-minute habits / personal-systems briefings at **1.5×** (roughly 15–23 minutes of drive time). Home-life only — habits, systems, focus. 

## Subscribe (Overcast)

1. Overcast → **Add URL**
2. Paste:

```
https://mowgli42.github.io/pretzelerfl-rides/feed.xml
```

3. Playback → **1.5×**

Site: https://mowgli42.github.io/pretzelerfl-rides/

## Add a new ride

1. Edit **`rides.json`** — append an object to the `rides` array.
2. Run the rebuild script:

```bash
python3 build_feed.py
```

3. Commit and push `rides.json` + `feed.xml` (and any README notes you want).

### Ride fields

| Field | Notes |
| --- | --- |
| `id` | Stable slug (used in GUID) |
| `title` | Shown in Overcast |
| `pubDate` | ISO-8601 UTC, e.g. `2026-09-14T12:00:00Z` |
| `duration` | `HH:MM:SS` |
| `durationSeconds` | Integer seconds |
| `summary` | Short itunes summary |
| `description` | Full notes + **show credit** |
| `enclosureUrl` | Real MP3 URL from the show's public feed |
| `enclosureType` | Usually `audio/mpeg` |
| `enclosureLength` | File size in **bytes** |
| `link` | Episode or source page |
| `attribution` | Show / episode credit |
| `tags` | Optional labels |

Use real enclosure URLs taken from each show's own public RSS feed. Do not invent fake enclosure URLs, and do not re-host or copy the audio files.

## GitHub Pages

Deploy from branch **`main`**, folder **`/` (root)**.

If the site is not live yet: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `/ (root)` → Save**.

## Attribution

Episodes are curated third-party podcast episodes (TED Audio Collective, TED Talks Daily, Beyond the To-Do List, Deep Questions with Cal Newport, Happier with Gretchen Rubin). Enclosures point directly at each show's own publicly served audio — nothing is re-hosted. Each item description and `attribution` field credits the original show. This is a personal Overcast curation playlist, not affiliated with or endorsed by any of the shows.

## License

Feed curation and site files: yours to keep personal. Enclosed audio remains the property of its original publishers under their own terms; this feed only links to their public episode URLs for personal listening.
