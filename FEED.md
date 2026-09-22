# The news.toca.io JSON feed: how to integrate

This file is served unlisted at https://news.toca.io/llms.txt for people and agents working on toca.io, toca.health and toca.legal. It is not linked from the site. Source: `FEED.md` in the news.toca.io repo; edit it there.

News is published once, on news.toca.io, and every other Toca site reads it from here. Do not hardcode story lists on the sister sites, copy images across, or link to Medium directly.

## Endpoints

Everything is on `https://news.toca.io`. CORS is open on every endpoint. The format is JSON Feed 1.1 (https://jsonfeed.org/version/1.1) with a small `_toca` extension.

| path | what | cache |
| --- | --- | --- |
| `/feed.json` | newest 50 stories, all sites | 300s |
| `/feed/io.json`, `/feed/health.json`, `/feed/legal.json` | the same, filtered to stories flagged for one site | 300s |
| `/archive.json` | everything, all sites | 3600s |
| `/img/cards/*.webp` | card thumbnails, up to 640px wide, referenced by `items[].image` | 7 days |
| `/news-cards.js` | the drop-in renderer, if not vendored | 3600s |
| `/llms.txt` | this file | 3600s |

Until news.toca.io DNS is pointed, test against the Netlify URL of the site. The `url` and `image` values inside items are always absolute to news.toca.io regardless.

## The easy route: the drop-in renderer

    <div data-news-cards data-site="health" data-count="3" hidden></div>
    <script src="https://news.toca.io/news-cards.js" defer></script>

`data-site` is `io`, `health` or `legal`. `data-count` defaults to 3. The script fetches the per-site feed, renders cards and unhides the box. On any failure it leaves the box hidden, so the host page never shows a broken strip. Style the cards to match the host site.

If you vendor the script instead of loading it from here, three rules must survive any edit: every string is set via `textContent`; only expected fields are read and every URL is checked against the allow-list; any failure hides the container.

## Rendering it yourself

Fetch the per-site feed, or `/feed.json` and filter on `_toca.sites`. Link to `url` in the same tab: it is the Medium or partner page for external stories and the page here for native ones.

Standard item fields: `id`, `url`, `title`, `summary`, `date_published` (09:00Z on the story date), `tags` (one entry: the type, such as Case Study, Events, Partners, Blog), `image` (absent when there is none), `content_html` (native stories only; sanitise before injecting).

`_toca` on each item: `kind` (`customer` or `news`), `sites` (any of io, health, legal), `external` (bool), `source` (Medium, Legal Geek, news.toca.io, or a hostname), `slug`, `image_width`, `image_height`, `link_text` (optional). Customer stories add `customer`, `sector`, and where present `figure`, `figure_label`, `quote`, `quote_by`, `quote_role`. A story with a film adds `video` (YouTube ID) and `page` (the page here where it plays).

Feed level: `_toca.built` (YYYY-MM-DD), `_toca.sites`, and `next_url` pointing at the archive.

Underscore fields are ours and may grow; the rest is the JSON Feed standard. Treat unknown fields as optional and ignore them.

## Common uses

- A "From the news" strip: the drop-in above, or the newest three items from the site's feed.
- A customer proof strip: filter `_toca.kind == "customer"`, then by `_toca.sector`. Sectors in use: Healthcare, Law, Finance, Charity, Housing, Immigration, Technology, Professional services. Show `figure` and `figure_label` where present; they come from Toca's own copy and must not be rounded or invented.
- A quote: `quote`, `quote_by`, `quote_role` on customer stories that have one.
- "See all" links: `https://news.toca.io/` is the customer story wall, `https://news.toca.io/blog/` the blog. The wall takes hash filters, `/#sector=Law`, `/#site=health`; the blog takes `/blog/#site=health` and `/blog/#q=referrals`.

## House rules that carry over

No em dashes in any copy shown on Toca sites. Figures only from Toca's own copy. One pink thing per view; everything else neutral.
