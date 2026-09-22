---
title: "How to write for news.toca.io"
subtitle: "One Markdown file per story. This one is a draft, so it is built but kept out of the feed."
date: 2026-09-21
tag: "Blog"
sites: ["io", "health"]
image: ""
draft: true
---
A story is a file in `content/articles/`, named `YYYY-MM-DD-slug.md`. The front matter above is the whole schema.

## Two kinds of story

Leave `external` out and write a body, and the story gets its own page here. Set `external` to a URL and leave the body empty, and the card links out (to Medium, a partner's site, wherever). Both appear in the feed the same way.

## Sites

`sites` says who shows it. `["io"]` is the default; add `"health"` or `"legal"` and that site's teaser box picks it up. Nothing else needs changing anywhere.
