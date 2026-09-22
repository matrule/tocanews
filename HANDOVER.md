# Handover: toca.io rebuild and news.toca.io

For the next Claude session working with Mat (sysop at Toca). Written 21 September 2026. Read this, then `README.md`, `PAGES.md`, `TASKS.md` and `ANIMATION-PROPOSALS.md` in the toca.io repo; they are current.

## Who you are working with

Mat reviews renders and catches specific problems (padding, colour, a border out of line). He scopes tightly ("make it simpler", "that's enough messing around"), approves direction before you proceed, and brings references (toca.legal and toca.health are the pattern; fin.ai for tone). Show him a screenshot of anything visual; verify in a headless browser before claiming it works; say plainly what you could not do and why. Do not pad.

## The two repos

### toca-io-rebuild (the main site)

Static site, generated. **Never edit the HTML pages; edit `gen.py` and run `python3 gen.py`.** Everything regenerates byte-identically, so a diff of the HTML shows only what you meant to change.

- `gen.py`: all twelve pages. Page bodies are literal HTML in Python strings. Helpers: `head()`, `chrome(current)`, `video(yid, title, note, wide, start)`, `subnav()`. Inlines `assets/img/toca-mark.svg`, `assets/img/england-footprint.svg`. Ends with `_bake_rids()` (see RIDs) and a post-pass that inlines the BBS manifest into every page as `#bbs-data`.
- `*_block.py` files (`index_block.py`, `company_contact_block.py`, `partners_block.py`, `basic_ref_block.py`, …): mirrors of page sections, kept in step by editing both. Some are stale copies rather than imports; `basic_ref_block.py` is a real import. When editing a page section, grep for the same string in the block files and change it there too.
- `gen.py` asserts **no em dashes** anywhere in output. Use a colon, a comma, a middle dot or a full stop.
- **RIDs.** Every text element gets `data-rid="tag-hash8"`, a hash of tag plus text. Mat's copy spreadsheets target elements by RID. To apply a copy pass: map each RID to its element in the generated HTML, find that literal inner text in `gen.py` (and mirrors), replace. The last pass (`toca-copy-humanisation-pass.xlsx`, 10 Sept) applied 108 rows this way in one script; the approach is in the PAGES.md "Copy pass" note.
- CSS: `css/site.css` is shared with the sister sites (design tokens, `.proof-bar`, legacy `.journey-stage` rules; avoid editing it). `css/io.css` is this site's. Tokens: `--color-accent` (Toca pink), `--color-ink`, `--color-paper*`, `--font-display` (Barlow Condensed), `--font-mono` (Geist Mono), `--ease-out`, `--space-*`.
- Conventions established for every animation: authored markup is the finished state; a JS `.is-live` class hides then reveals; reduced motion and no-JS both read the page as written; visually-hidden `.vh` copies for screen readers while text moves; trigger on the whole element being in view or its top crossing 70% of the viewport; scroll can drive a sequence forward but never back.

### news-toca-io (new, 21 Sept)

Also static, also generated. `build.py` reads `content/articles/*.md` (front matter, optional Markdown body) and writes `site/`: `index.html` with tag filters, `articles/<slug>/` for native stories, `feed.json` (JSON Feed 1.1, newest 50, card thumbnails at 640px WebP in `img/cards/`), `archive.json` (everything), `_headers` (CORS on the feeds and cards), `robots.txt`, `sitemap.xml`. Seeded with the 61 stories that used to be `news.json` on toca.io; all of them currently `external:` links to Medium, so no native article pages exist yet. One draft (`2026-09-21-writing-for-news-toca-io.md`) documents the schema and shows what a native article looks like; drafts get a page to preview but no card and no feed entry.

`news-cards.js` is the drop-in for toca.io and toca.health: `<div data-news-cards data-site="health" data-count="3"></div>`. It applies three rules and the next session must keep them: every string via `textContent`, never `innerHTML`; only expected fields, every URL checked against the allow-list (`news.toca.io`, `medium.com/@toca.io`, `legalgeek.co`) or the item is skipped; any failure hides the container. It is **not yet wired into toca.io** (see next steps).

Build note: the shared `css/site.css` loads fonts from `url(../assets/fonts/…)`, so `build.py` copies `fonts/*.woff2` to `site/assets/fonts/` (fixed 21 Sept; the index was unstyled before). All paths in the built pages are relative (the generator passes a depth to `chrome()`), so `site/index.html` and the article pages open styled straight from `file://` as well as from the site root.

Deploy target: not created yet. A Netlify site for `news.toca.io`, publish directory `site/`, build command `python3 build.py` (Python with `markdown python-frontmatter Pillow`), or build locally and drag `site/` in.

## State of toca.io, 21 Sept (v45)

Done and verified:
- All six homepage animation builds (01 hero mosaic, 02 ledger count, 03 England footprint, 04 claim journey, 05 rebalancing band, 06 products assembling). Platform section fits one viewport above 60rem. Hero copy aligned to the page gutter; hero title "The platform the platforms are built on."
- Proof bar: eight single-colour marks to one standard (`tools/mark_from_colour.py`; NHS lozenge 15px; legal marks keep toca.legal's sizes), linking to `company.html#customers` where the full wall lives. Tikker, Prostate Cancer UK, LaborCI, Atlantic House and CHP are still text there, waiting on logo files.
- The Toca BBS behind the `>_` glyph: `js/bbs.js`, content from `bbs_content.py` (bulletins, files, who's on and system info are read from the generated pages at build time). Every area of the TASKS.md §5 spec, three editors, Bamboozle!, Careers, and the BASIC door (`js/basic.js`, reference at `basic.html`, `HELP` links to it). Hidden words: `HOLLY`, `DAVE`, `SMEG`, `SUDO`, `RM`, `VIM`, `BAMBOOZLE`, `BASIC`. Sysop message 017 is the clue. Kernel "Kickstart 3.1 (40.68)", shell "OSH 5.2" (Old Speckled Hen, an inside joke; do not explain it on the board).
- BASIC has nine built-in programs incl. TETRIS, GORILLAS, LUNAR (credited to Jim Storer and David H. Ahl), HERO (draws on the hero mosaic via `SCREEN 1` / `window.TocaMosaic`). `RUN` clears the terminal; `CLS` at the prompt clears it too. `ESC` only breaks a running program. Programs save to `localStorage`.
- Copy: the 10 Sept humanisation pass applied. Pricing reads as "How we price" (decision D6 still open). Careers section removed from the company page (careers now lives on the BBS [C]).
- News removed from toca.io: no `news.html`, no `news.json`, no `assets/news`. Nav and footer "News" and the five "read the case study" links point at `https://news.toca.io`.

Open items, in priority order:
1. **Wire news into toca.io** (and toca.health): decide teaser placement (a small "From the news" strip above the footer on the homepage is the obvious one), add `js/news-cards.js`, a `<div data-news-cards data-site="io">` and card styles matching the dossier. Then create the news.toca.io Netlify site and point DNS. Until news.toca.io is live, the News links 404: either deploy news first or hold v45.
2. **Marks**: Tikker, Prostate Cancer UK, LaborCI, Atlantic House, CHP. Run each PNG through `tools/mark_from_colour.py`, add the `img` with the printed size, delete the `span.firm`.
3. **Netlify Forms** on `tocaiorebuild` are off; the contact form and BBS [M]/[C] post to them. Enable in site settings (Mat has to say yes; it is a settings change).
4. **Deploying from the sandbox**: `netlify-mcp.netlify.app` and `api.netlify.com` must be on the environment's allowed domains; Mat added the first on 17 Sept but a running container does not pick it up. In a fresh session, try the Netlify MCP `deploy-site`, then run the `npx @netlify/mcp … --proxy-path` command it returns from inside the repo folder. Fallback is drag-and-drop of the folder onto the Deploys tab.
5. **Pass 2 animations** (ANIMATION-PROPOSALS.md): P1 platform "five stations", S1/S2 Spectral, AU1 automation, plus the company family tree. Three animation-slot notes are still on those pages by design ("remove when built").
6. **Pricing D6**: whether pricing.html stays in the nav.
7. **Privacy notice** link on Contact is still a placeholder.
8. Web437 font for the BBS is not in the repo; the board uses the system monospace with box-drawing glyphs. Drop the woff2 in `assets/fonts/` and add `@font-face` if wanted.

## How to verify things here

Playwright with Chromium is available in the sandbox (`from playwright.sync_api import sync_playwright`). Open pages with `file:///…/index.html`; the site uses `scroll-behavior: smooth`, so scroll with `window.scrollTo({top, behavior:'instant'})` before measuring. The news site's built pages open styled from `file://` too. Check `pg.on('pageerror')` for JS errors on every page after a change. `node -e "new Function(require('fs').readFileSync('js/x.js','utf8'))"` parses a script quickly.

## Things not to do

- Do not reproduce GORILLA.BAS, Ahl's LUNAR listing, or anyone else's code or lyrics; our versions are our own and say so.
- Do not add a dark mode, ads, a CMS or a backend. The whole estate is static and Mat wants it that way.
- Do not put em dashes in copy; `gen.py` will refuse to build.
- Do not describe the BBS as "retro" on the site. It is a bulletin board. The whimsy is deliberate and dry.

## 21 Sept, later session: news.toca.io built out

Done and verified in Chromium at 1400 and 390 wide, no JS errors, no horizontal overflow:
- Index: lead story as the leading card (1.5px pink border, the one pink thing per view), filter rows for type and site driven by the URL hash so sister sites can deep-link (`/#site=health`), year rows as hairline ledger lines, cards on paper 3 with hairline and 10px radius, chrome aligned to the same left edge as the content.
- `/feed/`: the page for integrators. Endpoints, drop-in snippet, JS and Python fetch examples, the schema as ledger rows, the first feed item printed raw as built, rules of the road.
- Per-site feeds at `feed/io.json`, `feed/health.json`, `feed/legal.json` beside `feed.json` and `archive.json`. Items gained `_toca.slug`, `_toca.source` (Medium, Legal Geek, news.toca.io), `_toca.link_text`, and `content_html` for native stories. Feed-level `_toca.built` and `authors`.
- `news-cards.js` is also served at `/news-cards.js` with CORS; tested end to end against the built feed: health renders 3 cards, legal (no stories yet) hides its box.
- `404.html`, `netlify.toml` (publish `site/`, Python 3.11 build), `requirements.txt`. `_headers` covers the new paths.
- Build asserts no em dashes in output (site.css is shared and excluded; it has one in a comment).

Still to do: create the Netlify site and DNS; wire the teaser into toca.io and toca.health (item 1 above); the card sources are small (many 300x200 or square), so the lead image upscales softly until better artwork exists; toca.legal has no stories flagged yet, so `feed/legal.json` is valid but empty.

Later still, 21 Sept: Mat asked for the JSON and architecture to come off the pages (the site is just the news). Removed the `/feed/` page, the ledger strip, and the header and footer links to the JSON; the feeds themselves are unchanged and still built, documented in `FEED.md` in the repo. Added a search bar above the filters: matches title, summary, type and date text on the cards, lives in the hash as `q=` alongside `tag=` and `site=`, hides the lead card while anything is active. Verified: search, filters and deep links, back button, no JS errors, 1400 and 390 wide.

22 Sept: restructured after looking at Fin's site. Home is now Customer stories (the Fin-style wall: lead tile, then story / quote / film tiles, every seventh wide, sector filters); `/blog/` is lead plus the latest six then the archive as compact rows with search. Nav: Customer stories · Blog · Knowledge Hub. Knowledge Hub URL is `KNOWLEDGE_HUB` in build.py, still empty (Mat: it's what lives on Vault). Stories become customer stories with `kind: customer` and carry customer/sector/figure/quote/video; thirteen tagged so far, figures taken from Toca's own copy (subtitles and the brand deck) only. A `video:` (YouTube ID) gets an on-site page with the film embedded and a link out to Medium if that's where the write-up is; Immpact has `Iev9ko9NUFI` start 13; SolarNet and Royal Berkshire films need IDs (RBH has no story yet). Logos: none in this repo; `logo:` takes an ink mark from content/images and the customer name is set in Barlow Condensed until then. The shared site.css has a `.quote` rule, so the quote tile is `.tile.said`. Feed items gained `_toca.kind`, sector and video fields (FEED.md). Verified served over HTTP: wall filters, blog cards from /blog/, film page, back links, 404, 1400 and 390 wide, no JS errors.

22 Sept, later: customer stories page is dark (Mat, after Fin). Tried the deck's ink/scrim first; Mat found brown behind blue-toned photos unconvincing, so it is navy: page #0B1020, tiles #141C3A (a gradient a step lighter), hairlines #283157, headings #F4F3EE, muted #9AA3C4, pink lifted to #FF4D86 for text so it clears 4.5:1. A knowing departure from brand vol 3 (navy retired); pink is still the only accent. Done by remapping the tokens under `body.dark` in news.css, applied with `chrome(..., dark=True)` on the home page only; blog and articles stay on paper.

22 Sept, later still: films and case studies pulled in from the toca.io deploy (Mat sent the deploy zip; `yt.json` lists the channel, `assets/img/logos` the ink marks). Wall now has 17 customer stories in a mix of film, photo, quote and figure tiles.
- Films attached: Prostate Cancer UK `6WmRGTiuYas`, SolarNet `M9iLxPtmd6g` (Immpact already had `Iev9ko9NUFI`).
- New native customer stories, all dated 22 Sept 2026 (the day they were published here), short bodies written by Claude from toca.io's own copy and figures: Royal Berkshire (film `M4_brphr6k8`, 51% less referral admin, pinned as lead with `lead: true`), JMK Solicitors (25% fewer files at risk), Tikker (£30bn; carries a [bracketed] line asking for a quote and a figure), "Why our customers love working with Toca" (film `zwtD0-qa8y8`, no sector, shows under All only), a law firm's wills/probate quote generation (film `j-xZux8-JBk`), Sandhata ATM (film `6XtmMfhhhXw`). Winn gained 160 hrs/month and its mark.
- Marks for RBH, ESNEFT, Winn, Immpact, JMK are in content/images and recoloured to paper at build (`logo_image`, alpha under 28 floored: the source PNGs carry a faint alpha wash that ghosts on navy). Shared site.css paints a background on img, so `.tile .mark` sets `background: none`.
- Not used from the channel: the product demos, webinars, WealthOS/PIMFA demos, the energy portal, Morningstar talk. They are not customer stories. `HQpZpLtTJ9k` Cancer Pathways is unclear; ask Mat.
- Slater and Gordon, Bond Turner, E-Capital appear on toca.io as customers but have no story or figure; marks exist for bond-turner and slater-gordon if Mat wants tiles.

Knowledge Hub resolved: it is Toca Vault at vault.toca.io, kept under that name. It sits in the family bar as a fifth site ("Docs and training") and the nav item and its [link] placeholder are gone.

Footer is now toca.io\x27s exactly (display line, link row, meta row with wordmark and sister sites, company line), using site.css\x27s own .foot rules; news.css only aligns its left edge to the header. Wordmark and mark follow the dark tokens on the customer page.
