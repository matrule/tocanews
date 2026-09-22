# news.toca.io

The news site for all three Toca sites. Static, generated, no backend.

    pip install -r requirements.txt
    python3 build.py        # writes site/

## Content

- `content/articles/*.md`: one story per file, `YYYY-MM-DD-slug.md`, YAML front matter (the draft `2026-09-21-writing-for-news-toca-io.md` is the schema and a live example). `external:` makes the card link out; a body without `external` gets its own page at `/articles/<slug>/`. `sites:` is any of `io`, `health`, `legal`; the build refuses anything else.
- Customer stories: add `kind: customer` plus `customer`, `sector`, and any of `figure`/`figure_label`, `quote`/`quote_by`/`quote_role`, `video`/`video_start` (YouTube ID), `logo` (ink mark in `content/images`, recoloured to paper for the dark page), `lead: true` to pin the wall's lead. The tile shape follows the data: film, quote, figure, or photo when it falls on a wide slot.
- `content/images/`: source images; the build makes 640px WebP cards in `site/img/cards/`. Cards crop to 16:10, so landscape sources look best.

## What gets built

| path | what |
| --- | --- |
| `index.html` | customer stories: the wall (lead tile with the one pink border, then story, quote and film tiles, every seventh wide), sector filters in the hash (`#sector=Law`), plus the latest three news |
| `blog/index.html` | the blog: lead, the latest six as cards, then the archive as dated rows with search and type/site filters (`#q=nhs`, `#tag=Events`) |
| `articles/<slug>/` | native stories, and a page for any story with a `video:` (the film plays here, with a link out if the write-up is on Medium); drafts get a page to preview but no card and no feed entry |

| `feed.json`, `feed/*.json`, `archive.json`, `news-cards.js` | the JSON for the sister sites; not linked from the pages, see `FEED.md` |
| `404.html`, `robots.txt`, `sitemap.xml`, `_headers` | CORS on all JSON, cards and the script; cache headers; nosniff |

The build asserts no em dashes in anything it writes, same as `gen.py` on toca.io.

## Using the feed from another site

    <div data-news-cards data-site="health" data-count="3" hidden></div>
    <script src="https://news.toca.io/news-cards.js" defer></script>

Three rules in `news-cards.js`; keep them: every string via `textContent`; only expected fields, every URL checked against the allow-list; any failure hides the container. Style `.news-card` on the host site.

## Deploy

Toca Vault (docs and training) is the fifth site in the family bar; `VAULT` in `build.py`.

Netlify, `netlify.toml` is in the repo: publish directory `site/`, build command installs `requirements.txt` and runs `build.py` on Python 3.11. Or build locally and drag `site/` onto the Deploys tab. Then point `news.toca.io` at it.
