# PretzelerFL rides

Personal Overcast ride queue for ~25-minute listens at **1.5×** (about 15–18 minutes of drive time). Home-life only — stories, focus, curiosity. 

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
| `description` | Full notes + **attribution** + 1.5× tip |
| `enclosureUrl` | Real MP3 URL (public-domain / CC only) |
| `enclosureType` | Usually `audio/mpeg` |
| `enclosureLength` | File size in **bytes** |
| `link` | Episode or source page |
| `attribution` | License / source credit |
| `tags` | Optional labels |

Prefer real redistributable audio (LibriVox, Internet Archive, clear Creative Commons). Do not invent fake enclosure URLs.

## GitHub Pages

Deploy from branch **`main`**, folder **`/` (root)**.

If the site is not live yet: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `/ (root)` → Save**.

## Attribution

Starter episodes are LibriVox public-domain readings hosted on Internet Archive. Each item description credits the collection. This feed is a personal curation playlist — not affiliated with LibriVox or Archive.org beyond fair use of public-domain audio.

## License

Feed curation and site files: yours to keep personal. Enclosed audio remains under its original public-domain / CC terms.
