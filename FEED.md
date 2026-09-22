# The JSON feed

Not linked from the site; this is for toca.io, toca.health and toca.legal. JSON Feed 1.1 with a small `_toca` extension. CORS is open on everything here.

| path | what | cache |
| --- | --- | --- |
| `/feed.json` | newest 50 stories, all sites | 300s |
| `/feed/io.json`, `/feed/health.json`, `/feed/legal.json` | the same, filtered to one site | 300s |
| `/archive.json` | everything | 3600s |
| `/img/cards/*.webp` | card thumbnails, up to 640px wide, referenced by `items[].image` | 7 days |
| `/news-cards.js` | the drop-in renderer, if not vendored | 3600s |

## Drop-in

    <div data-news-cards data-site="health" data-count="3" hidden></div>
    <script src="https://news.toca.io/news-cards.js" defer></script>

Three rules in the script; keep them: every string via `textContent`; only expected fields, every URL checked against the allow-list; any failure hides the container.

## Item fields

Standard: `id`, `url` (Medium or partner URL for external stories, the page here for native ones), `title`, `summary`, `date_published` (09:00Z on the story date), `tags` (one entry: the type), `image` (absent when none), `content_html` (native stories only; sanitise before injecting).

`_toca`: `kind` (`customer` or `news`), `sites` (any of io, health, legal), `external` (bool), `source` (Medium, Legal Geek, news.toca.io, or hostname), `slug`, `image_width`, `image_height`, `link_text` (optional). Customer stories add `customer`, `sector`, and where present `figure`, `figure_label`, `quote`, `quote_by`, `quote_role`. A story with a film adds `video` (YouTube ID) and `page` (the page here where it plays). To show "customer stories for my sector": filter `_toca.kind == 'customer'` and `_toca.sector`.

Feed level `_toca`: `built` (YYYY-MM-DD), `sites`.

Underscore fields are ours and may grow; the rest is the JSON Feed standard.
