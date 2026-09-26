# AGENTS.md - guide for AI coding agents

pretzelerfl-rides is a personal Overcast ride queue: static site (`index.html`) + podcast feed (`feed.xml`) generated from `rides.json`.

## Change flow

```bash
# 1. Edit rides.json — append an object to the `rides` array
python3 build_feed.py   # rebuilds feed.xml + index.html
```

Verify by diffing `feed.xml` or opening `index.html`. Live site: https://mowgli42.github.io/pretzelerfl-rides/

## Secrets

Do not commit private keys, *-key.pem, *.key, .env secrets, or BEGIN … PRIVATE KEY. Generate locally; gitignore keys.
