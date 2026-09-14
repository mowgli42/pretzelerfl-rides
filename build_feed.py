#!/usr/bin/env python3
"""Regenerate feed.xml from rides.json for PretzelerFL rides."""
from __future__ import annotations

import html
import json
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RIDES_PATH = ROOT / "rides.json"
FEED_PATH = ROOT / "feed.xml"


def esc(s: str) -> str:
    return html.escape(s or "", quote=False)


def rfc2822(iso: str) -> str:
    dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return format_datetime(dt)


def build() -> None:
    data = json.loads(RIDES_PATH.read_text(encoding="utf-8"))
    ch = data["channel"]
    base = ch["link"].rstrip("/")
    feed_url = f"{base}/feed.xml"

    items: list[str] = []
    for r in sorted(data["rides"], key=lambda x: x["pubDate"], reverse=True):
        guid = f"{base}/rides/{r['id']}"
        desc = esc(r["description"])
        summary = esc(r.get("summary") or r["description"][:200])
        items.append(
            f"""    <item>
      <title>{esc(r['title'])}</title>
      <link>{esc(r.get('link') or base)}</link>
      <guid isPermaLink="false">{esc(guid)}</guid>
      <pubDate>{rfc2822(r['pubDate'])}</pubDate>
      <description>{desc}</description>
      <enclosure url="{esc(r['enclosureUrl'])}" length="{r['enclosureLength']}" type="{esc(r.get('enclosureType') or 'audio/mpeg')}" />
      <itunes:title>{esc(r['title'])}</itunes:title>
      <itunes:summary>{summary}</itunes:summary>
      <itunes:author>{esc(ch['author'])}</itunes:author>
      <itunes:duration>{esc(r['duration'])}</itunes:duration>
      <itunes:explicit>{esc(ch.get('explicit') or 'false')}</itunes:explicit>
      <itunes:episodeType>full</itunes:episodeType>
    </item>"""
        )

    now = format_datetime(datetime.now(timezone.utc))
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
  xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{esc(ch['title'])}</title>
    <link>{esc(ch['link'])}</link>
    <description>{esc(ch['description'])}</description>
    <language>{esc(ch.get('language') or 'en-us')}</language>
    <lastBuildDate>{now}</lastBuildDate>
    <atom:link href="{esc(feed_url)}" rel="self" type="application/rss+xml" />
    <itunes:author>{esc(ch['author'])}</itunes:author>
    <itunes:summary>{esc(ch['description'])}</itunes:summary>
    <itunes:owner>
      <itunes:name>{esc(ch['author'])}</itunes:name>
      <itunes:email>{esc(ch.get('email') or '')}</itunes:email>
    </itunes:owner>
    <itunes:explicit>{esc(ch.get('explicit') or 'false')}</itunes:explicit>
    <itunes:category text="{esc(ch.get('category') or 'Leisure')}" />
    <itunes:type>episodic</itunes:type>
{chr(10).join(items)}
  </channel>
</rss>
"""
    FEED_PATH.write_text(feed, encoding="utf-8")
    print(f"Wrote {FEED_PATH.name} ({len(data['rides'])} rides)")


if __name__ == "__main__":
    build()
