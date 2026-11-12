#!/usr/bin/env python3
"""news.toca.io · static generator. No backend, no CMS.

  content/articles/*.md   one file per story: YAML front matter, optional Markdown body
  content/images/*        source images, any size
  site/                   the output (see OUTPUTS below)

Front matter fields:
  title, subtitle, date (YYYY-MM-DD), tag, sites (["io"], ["health"], ["legal"] or any mix),
  image (file name in content/images), external (URL: the story lives elsewhere, the card links out),
  link_text (optional), draft: true (optional: built to preview, left out of the index and every feed).
  author, author_role (optional: a person's byline; Article markup names them), updated (YYYY-MM-DD, optional: shown and
  used as dateModified), reviewed_by (optional: "Name, role, firm", shown under the byline).
  section: learn          (optional) a guide or comparison written for search and AI answers: it lives at /learn/<slug>/, is listed on
                          the Learn pages by its tag (the category: "Comparisons", "Guides", ...), and stays off the blog, the home page's
                          latest strip and every feed. feed: true puts one in the feeds as well, deliberately.
  A native article whose body has a "## Questions" section of ### question / answer paragraphs also gets FAQPage markup.
  kind: customer          puts the story on the customer wall (the home page). With it:
    customer, sector      who and which sector filter ("Healthcare", "Law", "Finance", "Charity", ...)
    logo                  file name in content/images, single-colour ink mark (recoloured to paper for the dark page); the name is used until one exists
    lead: true            pins this story as the wall's lead tile; otherwise the newest customer story leads
    wide: true            gives the tile two of the wall's three columns (every seventh tile is wide anyway); the lead always takes all three
    figure, figure_label  one number and its claim ("15%", "of England's GP referrals")
    quote, quote_by, quote_role
    video, video_start    a YouTube ID (and optional start second). The film plays on a page here, whatever `external` says.

A story with a body and no `external` gets its own page at /articles/<slug>/ and the card links there (as /news/articles/<slug>/: see PATH).

OUTPUTS
  index.html              customer stories: the lead as a spotlight, then sector filters over the wall, plus the latest news
  blog/index.html         the blog, everything that is not a customer story: lead, the latest BLOG_RECENT, then the archive as rows
  articles/<slug>/        native stories, and pages for any story with a film (the film plays here)
  learn/index.html        Learn: the guides and comparisons as rows, after fin.ai/learn; learn/category/<tag>/ one per category
  learn/<slug>/           a Learn article (its old articles/<slug>/ address forwards to it)
  feed.json               JSON Feed 1.1, newest FEED_MAX, all sites
  feed/<site>.json        the same, filtered to one site (io, health, legal)
  archive.json            everything, all sites
  news-cards.js           the drop-in renderer, served from here as well as vendored
  img/cards/*.webp        card thumbnails, CARD_W wide
  img/og/*.jpg            link-preview images (og:image, Article JSON-LD), OG_W wide
  img/full/*.webp         images inside native articles, FULL_W wide (a .gif or .svg is copied here unchanged)
  toca-mark.svg           the mark for the header, footer and favicon (source: img/toca-mark.svg)
  llms.txt                FEED.md served as plain text: the integration how-to, unlisted
  404.html, robots.txt, sitemap.xml, _headers

The JSON is for the sister sites; it is not linked from the pages. FEED.md documents it.
Run: python3 build.py   (needs: pip install -r requirements.txt)"""
import re, json, pathlib, html, shutil, datetime
import frontmatter, markdown
from PIL import Image

ROOT = pathlib.Path(__file__).parent
CONTENT, SITE = ROOT / 'content', ROOT / 'site'
BASE = 'https://news.toca.io'    # the pages' address: canonicals, Open Graph, JSON-LD, the feeds' item URLs, sitemap, robots.txt.
                                 # Becomes 'https://www.toca.io/news' at go-live, with the DNS move, not before (HANDOVER.md).
FEEDS = 'https://news.toca.io'   # where the feeds, card images, news-cards.js and llms.txt are fetched from, CORS open:
                                 # stays here when BASE moves, because toca.io's and toca.health's cards read them here.
# The pages are served at www.toca.io/news/ through toca.io's proxy (Mat, 10 Nov 2026: what the blog earns in search
# builds www.toca.io), so every link and asset the pages use is root-absolute under PATH. netlify.toml rewrites
# /news/* to /:splat, so the same links work at news.toca.io. Never write a relative link: Netlify cannot add the
# trailing slash to www.toca.io/news, and a relative link there resolves against www.toca.io. main() refuses to build one.
PATH = '/news/'
CARD_W = 640
OG_W = 1200   # link-preview image (og:image): JPEG, since not every unfurler reads WebP
FULL_W = 1600          # images inside an article body
FEED_MAX = 50
SITES = {'io': 'toca.io', 'health': 'toca.health', 'legal': 'toca.legal'}
IO = 'https://www.toca.io'   # toca.io, where the shared nav and footer point: the go-live address (toca-io-rebuild gen.py SITE)
FONTS = ''   # toca.io's footer line face, wide Barlow 600, is self-hosted now (fonts/barlow-600.woff2, @font-face in css/news.css; Mat, 11 Nov 2026): it came from Google Fonts
# The strip, nav and footer are toca.io's (Mat, 10 Nov 2026: "acts and looks the toca.io one"): the markup mirrors
# toca-io-rebuild gen.py chrome() and FOOT with every link absolute, the rules mirror its css/io.css (in css/news.css,
# "chrome"), and the phone menu is its js/site.js nav toggle. Change both sites together.
NAV_JS = '''(function () {
  var nav = document.querySelector('.nav'), toggle = document.querySelector('.nav-toggle');
  if (!nav || !toggle) return;
  function shut(focus) { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); if (focus) toggle.focus(); }
  /* the open menu scrolls inside itself (css/news.css): --menu-room is the height left under the header, as on toca.io */
  var menu = nav.querySelector('.nav-links');
  function room() {
    if (!menu || !nav.classList.contains('open')) return;
    var vh = window.visualViewport ? window.visualViewport.height : window.innerHeight;
    menu.style.setProperty('--menu-room', Math.max(160, Math.floor(vh - nav.getBoundingClientRect().bottom - 12)) + 'px');
  }
  addEventListener('scroll', room, { passive: true });
  addEventListener('resize', room);
  nav.addEventListener('transitionend', room);
  toggle.addEventListener('click', function () { var open = nav.classList.toggle('open'); toggle.setAttribute('aria-expanded', open ? 'true' : 'false'); room(); });
  document.addEventListener('click', function (e) { if (nav.classList.contains('open') && !nav.contains(e.target)) shut(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) shut(true); });
  /* the header comes back when you scroll up, as on toca.io (its js/site.js): sticky, hidden while reading down */
  var root = document.documentElement, lastY = window.scrollY, NUDGE = 6;
  function start() { var p = nav.previousElementSibling; return p ? p.offsetTop + p.offsetHeight : 0; }
  function apply(y) {
    var stuck = y > start(), past = y > start() + nav.offsetHeight;
    if (!stuck || nav.classList.contains('open') || nav.contains(document.activeElement)) nav.classList.remove('nav--hidden');
    else if (past && y > lastY + NUDGE) nav.classList.add('nav--hidden');
    else if (y < lastY - NUDGE) nav.classList.remove('nav--hidden');
    root.classList.toggle('nav-stuck', stuck);
    if (Math.abs(y - lastY) > NUDGE || !stuck) lastY = y;
  }
  if (window.scrollY > start() + nav.offsetHeight) nav.classList.add('nav--hidden');
  apply(window.scrollY);
  addEventListener('scroll', function () { apply(window.scrollY); }, { passive: true });
  nav.addEventListener('focusin', function () { nav.classList.remove('nav--hidden'); apply(window.scrollY); });
})();'''
BLOG_RECENT = 6
# Learn categories, in pill order, with the line under each category page's heading. A tag missing here still works (no intro line).
LEARN = {'Comparisons': 'Side-by-side comparisons of low-code, automation and integration platforms for regulated, high-volume work: where each one runs, what it costs, and when to choose something else.',
         'Guides': 'How to automate a regulated process step by step, what it saves, and how to show a regulator who decided what.'}
LEARN_INTRO = 'Guides and side-by-side comparisons for regulated, high-volume work: what each option does, where it runs, and when to choose something else.'
def cat_slug(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
SOURCES = {'medium.com': 'Medium', 'legalgeek.co': 'Legal Geek', 'youtube.com': 'YouTube', 'youtu.be': 'YouTube', 'linkedin.com': 'LinkedIn'}
BUILT = datetime.date.today().isoformat()

def slug_of(path): return re.sub(r'^\d{4}-\d{2}-\d{2}-', '', path.stem)
def esc(s): return html.escape(str(s), quote=True)
def nice(d, long=False): return datetime.date.fromisoformat(d).strftime('%-d %B %Y' if long else '%-d %b %Y')
def source_of(url):
    host = re.sub(r'^www\.', '', re.sub(r'^https?://([^/]+).*$', r'\1', url or ''))
    for k, v in SOURCES.items():
        if host.endswith(k): return v
    return host

def card_image(name):
    """Resize once to a card thumbnail (WebP, CARD_W wide). Returns (url, w, h) or None."""
    if not name: return None
    src = CONTENT / 'images' / name
    if not src.exists(): print('  missing image', name); return None
    out = SITE / 'img/cards' / (pathlib.Path(name).stem + '.webp'); out.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert('RGB')
    if im.width > CARD_W: im = im.resize((CARD_W, round(im.height * CARD_W / im.width)), Image.LANCZOS)
    im.save(out, 'WEBP', quality=78)
    return f'{FEEDS}/img/cards/{out.name}', im.width, im.height

def og_image(name):
    """The link-preview image: JPEG, at most OG_W wide. Returns (url, w, h)."""
    src = CONTENT / 'images' / name
    out = SITE / 'img/og' / (pathlib.Path(name).stem + '.jpg'); out.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert('RGB')
    if im.width > OG_W: im = im.resize((OG_W, round(im.height * OG_W / im.width)), Image.LANCZOS)
    im.save(out, 'JPEG', quality=82, optimize=True)
    return f'{BASE}/img/og/{out.name}', im.width, im.height

def full_image(name):
    """Resize once for an article body (WebP, at most FULL_W wide). Returns the site-relative path or None.
    A GIF or an SVG is copied as it is: re-encoding would stop an animation and rasterise a drawing."""
    src = CONTENT / 'images' / name
    if not src.exists(): print('  missing image', name); return None
    if src.suffix.lower() in ('.gif', '.svg'):
        out = SITE / 'img/full' / src.name; out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, out)
        return f'img/full/{out.name}'
    out = SITE / 'img/full' / (pathlib.Path(name).stem + '.webp'); out.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert('RGB')
    if im.width > FULL_W: im = im.resize((FULL_W, round(im.height * FULL_W / im.width)), Image.LANCZOS)
    im.save(out, 'WEBP', quality=82)
    return f'img/full/{out.name}'

def logo_image(name, colour=(244, 243, 238)):
    """A single-colour ink mark from content/images, recoloured for the dark page with its alpha kept. Returns site-relative path or None."""
    src = CONTENT / 'images' / name
    if not src.exists(): print('  missing logo', name); return None
    out = SITE / 'img/logos' / (pathlib.Path(name).stem + '.png'); out.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert('RGBA'); a = im.getchannel('A').point(lambda v: 0 if v < 28 else v)   # the ink marks carry a faint alpha wash that ghosts on navy
    Image.merge('RGBA', (*[Image.new('L', im.size, c) for c in colour], a)).save(out, 'PNG', optimize=True)
    return f'img/logos/{out.name}'

def body_images(body):
    """![alt](file.jpg) with a bare file name points at content/images; rewrite to the built full-size copy."""
    used = []
    def sub(m):
        alt, name = m.group(1), m.group(2)
        if '/' in name or name.startswith('http'): return m.group(0)
        path = full_image(name)
        if not path: return ''
        used.append(name)
        return f'![{alt}]({BASE}/{path})'
    return re.sub(r'!\[([^\]]*)\]\(([^)\s]+)\)', sub, body), used

def lazy_images(h):
    """Every body image after the first loads lazily: a story can carry several animations."""
    seen = []
    def sub(m): seen.append(1); return m.group(0) if len(seen) == 1 else '<img loading="lazy" '
    return re.sub(r'<img ', sub, h)

def load():
    arts = []
    for p in sorted((CONTENT / 'articles').glob('*.md')):
        fm = frontmatter.load(p)
        a = dict(fm.metadata); a['body'] = fm.content.strip(); a['slug'] = slug_of(p)
        a['date'] = str(a['date'])[:10]
        if a.get('updated'): a['updated'] = str(a['updated'])[:10]
        a.setdefault('sites', ['io']); a.setdefault('tag', 'Blog'); a.setdefault('subtitle', '')
        a['customer_story'] = a.get('kind') == 'customer'
        a['learn'] = a.get('section') == 'learn'
        a['in_feed'] = not a['learn'] or a.get('feed') is True   # Learn articles stay out of the feeds unless marked feed: true
        for k in ('customer', 'sector', 'figure', 'figure_label', 'quote', 'quote_by', 'quote_role', 'video', 'logo'): a.setdefault(k, '')
        a['video'] = str(a['video']) if a['video'] else ''
        bad = [s for s in a['sites'] if s not in SITES]
        assert not bad, f'{p.name}: unknown site {bad}'
        a['dir'] = 'learn' if a['learn'] else 'articles'
        assert not (a['learn'] and (a.get('external') or a['customer_story'])), f'{p.name}: a Learn article is native and not a customer story'
        a['url'] = a.get('external') or f'{BASE}/{a["dir"]}/{a["slug"]}/'
        # 'url' is the absolute, canonical link (used in JSON, canonical tags, sitemap: these must stay absolute
        # regardless of where the site is hosted). 'href' is what pages link with: external stories still go
        # out to their absolute URL, but a native story links root-absolute under PATH, so cards work the
        # same at www.toca.io/news/, at news.toca.io and on a Netlify preview domain.
        a['href'] = f'{PATH}{a["dir"]}/{a["slug"]}/' if (a['video'] or not a.get('external')) else a['external']
        a['source'] = source_of(a['external']) if a.get('external') else 'news.toca.io'
        a['card'] = card_image(a.get('image'))
        a['og'] = og_image(a.get('image')) if a['card'] and (a['video'] or not a.get('external')) else None   # only stories with a page here
        a['body_images'] = []
        if a['body'] and not a.get('external'):
            a['body'], a['body_images'] = body_images(a['body'])
            a['html'] = lazy_images(markdown.markdown(a['body'], extensions=['extra', 'smarty']))
        else: a['html'] = ''
        arts.append(a)
    arts.sort(key=lambda a: a['date'], reverse=True)
    return arts

# ---------------------------------------------------------------- feeds
def feed_item(a):
    it = {'id': a['url'], 'url': a['url'], 'title': a['title'], 'summary': a['subtitle'],
          'date_published': a['date'] + 'T09:00:00Z', 'tags': [a['tag']],
          '_toca': {'slug': a['slug'], 'sites': a['sites'], 'external': bool(a.get('external')), 'source': a['source'],
                    'kind': 'customer' if a['customer_story'] else 'news'}}
    if a['customer_story']:
        it['_toca'].update({k: a[k] for k in ('customer', 'sector', 'figure', 'figure_label', 'quote', 'quote_by', 'quote_role') if a[k]})
    if a['video']: it['_toca']['video'] = a['video']; it['_toca']['page'] = f'{BASE}/articles/{a["slug"]}/'
    if a.get('link_text'): it['_toca']['link_text'] = a['link_text']
    if a['html']: it['content_html'] = a['html']
    if a['card']:
        it['image'] = a['card'][0]; it['_toca']['image_width'], it['_toca']['image_height'] = a['card'][1], a['card'][2]
    return it

def feed_doc(arts, feed_url, title, next_url=None):
    d = {'version': 'https://jsonfeed.org/version/1.1', 'title': title, 'home_page_url': BASE + '/', 'feed_url': feed_url,
         'description': 'Case studies, partner news, events and writing from Toca.', 'language': 'en-GB',
         'authors': [{'name': 'Toca', 'url': 'https://toca.io'}],
         '_toca': {'built': BUILT, 'sites': list(SITES)}}
    if next_url: d['next_url'] = next_url
    d['items'] = [feed_item(a) for a in arts]
    return json.dumps(d, indent=1, ensure_ascii=False)

def write_feeds(arts):
    arts = [a for a in arts if a['in_feed']]
    (SITE / 'feed.json').write_text(feed_doc(arts[:FEED_MAX], FEEDS + '/feed.json', 'Toca news', FEEDS + '/archive.json'))
    (SITE / 'archive.json').write_text(feed_doc(arts, FEEDS + '/archive.json', 'Toca news · archive'))
    (SITE / 'feed').mkdir(exist_ok=True)
    for s, host in SITES.items():
        sub = [a for a in arts if s in a['sites']]
        (SITE / 'feed' / f'{s}.json').write_text(feed_doc(sub[:FEED_MAX], f'{FEEDS}/feed/{s}.json', f'Toca news · {host}'))

# ---------------------------------------------------------------- page chrome
def social_meta(title, desc, canonical, a=None):
    """Open Graph and Twitter tags for every page; for a native story also article dates and Article JSON-LD.
    A story whose canonical is elsewhere (an external story with a film page here) gets the tags but no JSON-LD:
    the article itself lives at the other site, and claiming it here would contradict the canonical tag."""
    og_title = a['title'] if a else title
    tags = [('property', 'og:site_name', 'Toca news'), ('property', 'og:locale', 'en_GB'),
            ('property', 'og:type', 'article' if a else 'website'), ('property', 'og:title', og_title),
            ('property', 'og:description', desc), ('property', 'og:url', canonical)]
    img = a and a['og']
    if img:
        tags += [('property', 'og:image', img[0]), ('property', 'og:image:width', img[1]), ('property', 'og:image:height', img[2])]
    if a:
        tags.append(('property', 'article:published_time', a['date'] + 'T09:00:00Z'))
        tags.append(('property', 'article:section', a['tag']))
    tags += [('name', 'twitter:card', 'summary_large_image' if img else 'summary'),
             ('name', 'twitter:title', og_title), ('name', 'twitter:description', desc)]
    out = ''.join(f'<meta {k}="{n}" content="{esc(v)}">' for k, n, v in tags)
    if a and a.get('draft'): out += '<meta name="robots" content="noindex">'
    if a and not a.get('external'):
        ld = {'@context': 'https://schema.org', '@type': 'Article', 'headline': a['title'], 'description': a['subtitle'],
              'datePublished': a['date'], 'url': canonical, 'mainEntityOfPage': canonical, 'inLanguage': 'en-GB',
              'articleSection': a['tag'], 'author': ({'@type': 'Person', 'name': a['author'], **({'jobTitle': a['author_role']} if a.get('author_role') else {}), 'worksFor': {'@type': 'Organization', 'name': 'Toca', 'url': IO}} if a.get('author') else {'@type': 'Organization', 'name': 'Toca', 'url': IO}),
              'publisher': {'@type': 'Organization', 'name': 'Toca', 'url': IO}}
        if img: ld['image'] = img[0]
        if a['video']: ld['video'] = {'@type': 'VideoObject', 'name': a['title'], 'description': a['subtitle'] or a['title'],
                                      'embedUrl': f'https://www.youtube-nocookie.com/embed/{a["video"]}',
                                      'thumbnailUrl': f'https://i.ytimg.com/vi/{a["video"]}/hqdefault.jpg', 'uploadDate': a['date']}
        if a.get('updated'): ld['dateModified'] = a['updated']
        out += '\n<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace('</', '<\\/') + '</script>'
        faq = faqs_of(a['html'])
        if faq:
            fq = {'@context': 'https://schema.org', '@type': 'FAQPage', 'url': canonical,
                  'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': ans}} for q, ans in faq]}
            out += '\n<script type="application/ld+json">' + json.dumps(fq, ensure_ascii=False).replace('</', '<\\/') + '</script>'
    return out

def faqs_of(h):
    """the question and answer pairs under a "Questions" h2: each h3, then its paragraphs, as plain text"""
    m = re.search(r'<h2[^>]*>Questions</h2>(.*?)(?=<h2|$)', h, re.S)
    if not m: return []
    txt = lambda x: re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', x))).strip()
    return [(txt(q), txt(a)) for q, a in re.findall(r'<h3[^>]*>(.*?)</h3>(.*?)(?=<h3|$)', m.group(1), re.S)]

# toca.io's footer social links (gen.py SOCIAL, copied as written; Mat, 11 Nov 2026): LinkedIn, GitHub, Instagram,
# YouTube, by how active each account is. No Facebook or X.
SOCIAL = '''<ul class="foot-social">
      <li><a href="https://www.linkedin.com/company/tocaio" rel="noopener" aria-label="Toca on LinkedIn"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" fill-rule="evenodd" d="M3 1h18a2 2 0 0 1 2 2v18a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2zM7 5.4a1.75 1.75 0 1 0 0 3.5a1.75 1.75 0 1 0 0-3.5zM5.5 10h3v9h-3zM10.5 10h2.9v1.3c.5-.9 1.6-1.5 2.9-1.5 2.4 0 3.2 1.5 3.2 3.9V19h-3v-4.3c0-1-.2-1.9-1.3-1.9s-1.6.8-1.6 1.9V19h-3.1z"/></svg></a></li>
      <li><a href="https://github.com/tocalabs" rel="noopener" aria-label="Toca on GitHub"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg></a></li>
      <li><a href="https://www.instagram.com/toca.io/" rel="noopener" aria-label="Toca on Instagram"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.4" cy="6.6" r="1.2" fill="currentColor"/></svg></a></li>
      <li><a href="https://www.youtube.com/@tocabot" rel="noopener" aria-label="Toca on YouTube"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" fill-rule="evenodd" d="M22.5 7.2a2.8 2.8 0 0 0-2-2C18.7 4.7 12 4.7 12 4.7s-6.7 0-8.5.5a2.8 2.8 0 0 0-2 2C1 9 1 12 1 12s0 3 .5 4.8a2.8 2.8 0 0 0 2 2c1.8.5 8.5.5 8.5.5s6.7 0 8.5-.5a2.8 2.8 0 0 0 2-2C23 15 23 12 23 12s0-3-.5-4.8zM9.8 15.2V8.8l5.6 3.2z"/></svg></a></li>
    </ul>'''


def chrome(title, desc, body, canonical, current='', dark=False, article=None):
    R = PATH   # root-absolute: the pages are served at www.toca.io/news/ and news.toca.io alike
    cur = lambda k: ' aria-current="page"' if k == current else ''
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
{social_meta(title, desc, canonical, article)}
<link rel="alternate" type="application/feed+json" title="Toca news" href="{FEEDS}/feed.json">
<link rel="icon" href="{R}toca-mark.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="{R}css/site.css"><link rel="stylesheet" href="{R}css/news.css">
</head>
<body{' class="dark"' if dark else ''}>
<a class="skip" href="#main">Skip to content</a>
<div class="family">
  <div class="band-narrow">
  <ul>
    <li><a href="{IO}/">toca.io</a></li>
    <li><a href="{IO}/health/">toca.health</a></li>
  </ul>
  </div>
</div>
<header class="nav nav--paper">
  <div class="band-narrow">
  <a class="wordmark" href="{IO}/"><img class="mark" src="{R}toca-mark.svg" alt="" width="26" height="26"><span>toca<span class="tld">.io</span></span></a>
  <nav class="nav-links" id="navlinks" aria-label="Site">
    <a href="{IO}/">Home</a>
    <div class="has-menu">
      <a href="{IO}/platform.html">Platform</a>
      <ul class="menu">
        <li><a href="{IO}/platform.html">Overview<small>three products, two layers</small></a></li>
        <li class="sep"></li>
        <li><a href="{IO}/platform.html#apps">Apps and Portals<small>product</small></a></li>
        <li><a href="{IO}/platform.html#automation">Automation<small>product</small></a></li>
        <li><a href="{IO}/spectral.html">Spectral<small>product</small></a></li>
        <li class="sep"></li>
        <li><a href="{IO}/platform.html#integration">Integration<small>enabling layer</small></a></li>
        <li><a href="{IO}/platform.html#tdk">Toca Development Kit<small>enabling layer</small></a></li>
      </ul>
    </div>
    <a href="{IO}/spectral.html">Spectral</a>
    <div class="has-menu">
      <a href="{IO}/company.html#customers">Sectors</a>
      <ul class="menu">
        <li><a href="{IO}/legal/">Law firms<small>automation and AI for volume law</small></a></li>
        <li><a href="{IO}/health/">Healthcare<small>eTriage, clinical letters and coding</small></a></li>
        <li><a href="{IO}/company.html#customers">More sectors<small>payroll, accounting, charities and immigration</small></a></li>
      </ul>
    </div>
    <a href="{IO}/partners.html">Partners</a>
    <a href="{IO}/company.html">Company</a>
    <a href="{R}" aria-current="page">News</a>
  </nav>
  <div class="nav-cta">
    <a class="chip chip--solid" href="{IO}/contact.html">Talk to us</a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="navlinks"><span class="burger">Menu</span><span class="x">Close</span></button>
  </div>
  </div>
</header>
<nav class="subnav" aria-label="News"><div class="band-narrow"><span class="lbl">News</span><a href="{R}"{cur('customers')}>Customer stories</a><a href="{R}blog/"{cur('blog')}>Blog</a><a href="{R}learn/"{cur('learn')}>Learn</a></div></nav>
<main id="main">{body}</main>
<footer class="foot">
  <div class="band-narrow">
  <p class="foot-line">The platform the platforms are built on.</p>
  <ul class="foot-links">
    <li><a href="{IO}/platform.html">Platform</a></li>
    <li><a href="{IO}/spectral.html">Spectral</a></li>
    <li><a href="{IO}/legal/">Legal</a></li>
    <li><a href="{IO}/health/">toca.health</a></li>
    <li><a href="{IO}/partners.html">Partners</a></li>
    <li><a href="{IO}/company.html">Company</a></li>
    <li><a href="{R}">News</a></li>
    <li><a href="https://github.com/tocalabs/toca-docs">Documentation</a></li>
    <li><a href="{IO}/contact.html">Contact</a></li>
  </ul>
  <div class="foot-meta">
    <span class="wordmark"><img class="mark" src="{R}toca-mark.svg" alt="" width="26" height="26"><span>toca<span class="tld">.io</span></span></span>
    {SOCIAL}
    <span>&copy; 2026 Toca</span>
  </div>
  <ul class="foot-links foot-links--small">
    <li><a href="{IO}/terms.html">Terms and policies</a></li>
    <li><a href="{IO}/privacy-policy.html">Privacy policy</a></li>
    <li><a href="{IO}/cloud-terms.html">Cloud terms</a></li>
    <li><a href="{IO}/carbon-reduction.html">Carbon reduction plan</a></li>
  </ul>
  <p class="foot-company">Tocalabs Limited, trading as Toca. Registered in England &amp; Wales, company no. 11396834. Registered office 5th Floor, One New Change, London EC4M 9AF. VAT GB&nbsp;303504844. Offices in Reading. Toca&reg;, Toca.Health&reg;, Tocabot&reg; and Tocalabs&reg; are registered trademarks of Tocalabs Ltd. <a href="mailto:sales@toca.io">sales@toca.io</a></p>
  </div>
</footer>
<script>{NAV_JS}</script>
</body></html>'''

# ---------------------------------------------------------------- index
def rel(h):
    """Links and image URLs written with this site's address (either one), made root-absolute under PATH,
    so a reader stays on whichever host they came in on."""
    for b in {BASE, FEEDS}:
        if h.startswith(b + '/'): return PATH + h[len(b) + 1:]
    return h

def card(a, lead=False):
    img = f'<img src="{esc(rel(a["card"][0]))}" width="{a["card"][1]}" height="{a["card"][2]}" alt="" loading="{"eager" if lead else "lazy"}">' if a['card'] else '<span class="noimg" aria-hidden="true"></span>'
    ext = a.get('external')
    ext = ext and not a['video']   # a film opens its page here, then links out
    target = ' target="_blank" rel="noopener"' if ext else ''
    where = f'<span class="where">{esc(a["source"])} &nearr;</span>' if ext else (f'<span class="where">Film</span>' if a['video'] else '')
    cls = 'story lead' if lead else 'story'
    h = 'h2' if lead else 'h3'
    return (f'<a class="{cls}" href="{esc(a["href"])}"{target} data-tag="{esc(a["tag"])}" data-sites="{esc(" ".join(a["sites"]))}">'
            f'{img}<span class="body"><span class="meta"><time datetime="{a["date"]}">{nice(a["date"])}</time><span class="tag">{esc(a["tag"])}</span>{where}</span>'
            f'<{h}>{esc(a["title"])}</{h}><p>{esc(a["subtitle"])}</p></span></a>')

INDEX_JS = r'''
(function(){
  var page=document.querySelector('.archive')||document.querySelector('.news');
  var state={tag:'',site:'',q:''};var box=document.getElementById('q'),own=false;
  function read(){var h=location.hash.replace(/^#/,'');state={tag:'',site:'',q:''};h.split('&').forEach(function(kv){var p=kv.split('=');if(p[0]==='tag')state.tag=decodeURIComponent(p[1]||'');if(p[0]==='site')state.site=decodeURIComponent(p[1]||'');if(p[0]==='q')state.q=decodeURIComponent(p[1]||'');});if(box&&box.value!==state.q)box.value=state.q;}
  function write(){var parts=[];if(state.tag)parts.push('tag='+encodeURIComponent(state.tag));if(state.site)parts.push('site='+encodeURIComponent(state.site));if(state.q)parts.push('q='+encodeURIComponent(state.q));var h=parts.length?'#'+parts.join('&'):'';if(h!==location.hash){own=true;if(h)location.hash=h;else history.replaceState(null,'',location.pathname);setTimeout(function(){own=false;},0);}}
  function apply(){
    document.querySelectorAll('.filters a').forEach(function(x){var k=x.getAttribute('data-key'),v=x.getAttribute('data-val');x.toggleAttribute('aria-current',state[k]===v);});
    var n=0,q=state.q.trim().toLowerCase();
    document.querySelectorAll('.archive .story').forEach(function(c){var ok=(!state.tag||c.getAttribute('data-tag')===state.tag)&&(!state.site||c.getAttribute('data-sites').split(' ').indexOf(state.site)>=0)&&(!q||c.textContent.toLowerCase().indexOf(q)>=0);c.hidden=!ok;if(ok)n++;});
    document.querySelectorAll('.year').forEach(function(y){var g=y.nextElementSibling,k=g.querySelectorAll('.story:not([hidden])').length;y.hidden=!k;y.querySelector('.n').textContent=k;});
    
    var empty=document.querySelector('.empty');if(empty)empty.hidden=n>0;
    var count=document.querySelector('.count');if(count)count.textContent=(q||state.tag||state.site)?n+(n===1?' story':' stories'):'';
  }
  page.addEventListener('click',function(e){var a=e.target.closest('.filters a');if(!a)return;e.preventDefault();var k=a.getAttribute('data-key'),v=a.getAttribute('data-val');state[k]=(state[k]===v&&v)?'':v;write();apply();});
  window.addEventListener('hashchange',function(){if(own)return;read();apply();});
  if(box){var t;box.addEventListener('input',function(){state.q=box.value;apply();clearTimeout(t);t=setTimeout(write,150);});}
  read();apply();
})();'''

# ---------------------------------------------------------------- customer stories (the home page)
def logo(a):
    """The customer's mark if we have one; the name set in the display face until we do."""
    if a['logo']:
        path = logo_image(a['logo'])
        if path: return f'<img class="mark" src="{PATH}{esc(path)}" alt="{esc(a["customer"])}">'
    return f'<span class="mark-text">{esc(a["customer"] or a["title"])}</span>'

def yt_thumb(vid): return f'https://i.ytimg.com/vi/{vid}/hqdefault.jpg'

def tile(a, i):
    """One tile on the customer wall. The first is the lead; every seventh after it is wide.
    Shape follows the data: a film gets a play tile, a quote gets a quote card, a figure gets a figure card."""
    href = a['href']
    ext = a.get('external') and not a['video']
    target = ' target="_blank" rel="noopener"' if ext else ''
    sector = f'<span class="sector">{esc(a["sector"])}</span>' if a['sector'] else ''
    fig = f'<span class="fig"><b>{esc(a["figure"])}</b><span>{esc(a["figure_label"])}</span></span>' if a['figure'] else ''
    common = f'data-sector="{esc(a["sector"])}" href="{esc(href)}"{target}'
    poster = esc(rel(a["card"][0])) if a['card'] else (yt_thumb(a['video']) if a['video'] else '')
    filmpic = lambda eager: f'<span class="pic film"><img src="{poster}" alt="" loading="{"eager" if eager else "lazy"}" onerror="this.remove()"><span class="play" aria-hidden="true"></span></span>'
    if i == 0:
        pic = filmpic(True) if a['video'] else (f'<span class="pic"><img src="{esc(rel(a["card"][0]))}" alt="" loading="eager"></span>' if a['card'] else '<span class="pic empty"></span>')
        by = f'<span class="by"><b>{esc(a["quote_by"])}</b>{esc(a["quote_role"])}</span>' if a['quote_by'] and not fig else ''
        return f'<a class="tile lead" {common}><span class="txt">{logo(a)}{sector}<h2>{esc(a["title"])}</h2><p>{esc(a["subtitle"])}</p>{fig}{by}</span>{pic}</a>'
    wide = i % 7 == 0 or bool(a.get('wide'))
    if a['video']:
        if wide:   # text left, film right, like the lead
            return f'<a class="tile film wide pictured" {common}><span class="txt">{logo(a)}{sector}<h3>{esc(a["title"])}</h3><p>{esc(a["subtitle"])}</p>{fig}</span>{filmpic(False)}</a>'
        return f'<a class="tile film" {common}>{filmpic(False)}<span class="txt">{logo(a)}{sector}<h3>{esc(a["title"])}</h3></span></a>'
    if a['quote']:
        by = f'<span class="by"><b>{esc(a["quote_by"])}</b>{esc(a["quote_role"])}</span>' if a['quote_by'] else ''
        return f'<a class="tile said{" wide" if wide else ""}" {common}>{logo(a)}<blockquote>{esc(a["quote"])}</blockquote>{by}</a>'
    if wide and a['card']:
        return f'<a class="tile wide pictured" {common}><span class="txt">{logo(a)}{sector}<h3>{esc(a["title"])}</h3><p>{esc(a["subtitle"])}</p>{fig}</span><span class="pic"><img src="{esc(rel(a["card"][0]))}" alt="" loading="lazy"></span></a>'
    return f'<a class="tile story" {common}>{logo(a)}{sector}<h3>{esc(a["title"])}</h3><p>{esc(a["subtitle"])}</p>{fig}</a>'

WALL_JS = (ROOT / 'js' / 'wall.js').read_text()

def write_home(arts):
    cust = sorted([a for a in arts if a['customer_story']], key=lambda a: (not a.get('lead'), ))  # stable: keeps date order after the pinned lead
    news = [a for a in arts if not a['customer_story'] and not a['learn']][:3]
    sectors = sorted({a['sector'] for a in cust if a['sector']})
    filt = '<nav class="sectors" aria-label="Sector"><a href="#" data-val="">All</a>' + ''.join(f'<a href="#sector={esc(x)}" data-val="{esc(x)}">{esc(x)}</a>' for x in sectors) + '</nav>'
    spot = tile(cust[0], 0) if cust else ''                                   # the lead: the spotlight, above the filters and never filtered
    wall = ''.join(tile(a, i) for i, a in enumerate(cust) if i)              # indices kept so every seventh tile stays wide
    latest = ''.join(card(a) for a in news)
    body = f'''
<section class="page-head"><div class="band-narrow"><p class="kicker">Customer stories</p><h1>Built on Toca.</h1><p class="support">NHS trusts, law firms, charities and a portfolio platform: what they built, in their numbers and their words.</p></div></section>
<section class="band wall"><div class="band-narrow">
<div class="spot">{spot}</div>
{filt}
<div class="wallgrid">{wall}</div>
<p class="empty" hidden>No stories in that sector yet.</p>
</div></section>
<section class="band latest"><div class="band-narrow">
<div class="strip-head"><h2>Latest from Toca</h2><a class="tlink" href="{PATH}blog/">All news and writing &rarr;</a></div>
<div class="grid">{latest}</div>
</div></section>
<script>{WALL_JS}</script>'''
    (SITE / 'index.html').write_text(chrome('Customer stories | Toca', 'What NHS trusts, law firms, charities and a portfolio platform built on Toca.', body, BASE + '/', current='customers', dark=True))

# ---------------------------------------------------------------- the blog
def write_blog(all_arts):
    arts = [a for a in all_arts if not a['customer_story'] and not a['learn']]
    lead, recent, older = arts[0], arts[1:BLOG_RECENT + 1], arts[BLOG_RECENT + 1:]
    tags = sorted({a['tag'] for a in arts})
    def links(key, items, all_label):
        out = f'<a href="#" data-key="{key}" data-val="">{all_label}</a>'
        return out + ''.join(f'<a href="#{key}={esc(v)}" data-key="{key}" data-val="{esc(v)}">{esc(lbl)}</a>' for v, lbl in items)
    filt = (f'<nav class="filters" aria-label="Filter"><div class="frow"><span class="flab">Type</span>{links("tag", [(t, t) for t in tags], "All")}</div>'
            f'<div class="frow"><span class="flab">Site</span>{links("site", list(SITES.items()), "All three")}</div></nav>')
    def row(a):
        href = a['href']
        ext = a.get('external') and not a['video']
        tgt = ' target="_blank" rel="noopener"' if ext else ''
        return (f'<a class="story row" href="{esc(href)}"{tgt} data-tag="{esc(a["tag"])}" data-sites="{esc(" ".join(a["sites"]))}">'
                f'<time datetime="{a["date"]}">{nice(a["date"])}</time><span class="rt">{esc(a["title"])}</span><span class="tag">{esc(a["tag"])}</span></a>')
    years = {}
    for a in older: years.setdefault(a['date'][:4], []).append(a)
    archive = ''.join(f'<p class="year"><span>{y}</span><span class="n">{len(items)}</span></p><div class="rows">{"".join(row(a) for a in items)}</div>' for y, items in years.items())
    body = f'''
<section class="page-head"><div class="band-narrow"><p class="kicker">Blog</p><h1>What Toca has been up to.</h1><p class="support">Announcements, events, partner news and writing. Customer stories live <a class="tlink" href="{PATH}">on their own page</a>.</p></div></section>
<section class="band news"><div class="band-narrow">
<div class="lead-wrap">{card(lead, lead=True)}</div>
<div class="grid">{''.join(card(a) for a in recent)}</div>
</div></section>
<section class="band archive"><div class="band-narrow">
<div class="strip-head"><h2>Everything else</h2><span class="count-static">{len(older)} more, back to {nice(arts[-1]["date"], True)}</span></div>
<form class="search" role="search" onsubmit="return false"><label class="vh" for="q">Search the archive</label><input id="q" type="search" placeholder="Search the archive" autocomplete="off"><span class="count" aria-live="polite"></span></form>
{filt}
{archive}
<p class="empty" hidden>Nothing matches that combination.</p>
</div></section>
<script>{INDEX_JS}</script>'''
    (SITE / 'blog').mkdir(exist_ok=True)
    (SITE / 'blog' / 'index.html').write_text(chrome('Blog | Toca news', 'Announcements, events, partner news and writing from Toca.', body, BASE + '/blog/', current='blog'))

# ---------------------------------------------------------------- articles
def byline(a):
    """who wrote it, when it was last checked, and who reviewed it: what readers and AI assistants look for before citing"""
    if not (a.get('author') or a.get('updated')): return ''
    who = esc(a['author']) + (f', {esc(a["author_role"])}' if a.get('author_role') else '') if a.get('author') else ''
    when = f'Last updated <time datetime="{a["updated"]}">{nice(a["updated"], True)}</time>' if a.get('updated') else ''
    line = ' <span class="sep">·</span> '.join(x for x in (who and 'By ' + who, when) if x)
    rev = f'<br>Reviewed by {esc(a["reviewed_by"])}' if a.get('reviewed_by') else ''
    return f'<p class="byline">{line}{rev}</p>'

def write_article(a):
    if a.get('external') and not a['video']: return
    if not a['body'] and not a['video']: return
    d = SITE / a['dir'] / a['slug']; d.mkdir(parents=True, exist_ok=True)
    show_hero = a['card'] and a.get('image') not in a['body_images'] and not a['video']
    hero = f'<img class="hero" src="{PATH}img/cards/{pathlib.Path(a["image"]).stem}.webp" alt="">' if show_hero else ''
    film = ''
    if a['video']:
        start = f'&start={int(a["video_start"])}' if a.get('video_start') else ''
        film = f'<div class="film-wrap"><iframe src="https://www.youtube-nocookie.com/embed/{esc(a["video"])}?rel=0{start}" title="{esc(a["title"])}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>'
    draft = '<p class="draft">Draft. Built to preview; not in the index or any feed.</p>' if a.get('draft') else ''
    # body images, and links to other stories here written as https://news.toca.io/articles/...: attribute values only
    html_body = re.sub(r'="(https://[^"]*)"', lambda m: '="' + rel(m.group(1)) + '"', a['html'])
    readon = f'<p class="readon"><a class="tlink" href="{esc(a["external"])}" target="_blank" rel="noopener">{esc(a.get("link_text") or "Read the full story")} on {esc(a["source"])} &nearr;</a></p>' if a.get('external') else ''
    kick = f'{esc(a["customer"])} <span class="sep">·</span> ' if a['customer'] else ''
    where = f'Published on news.toca.io, {nice(a["date"], True)}' if not a.get('external') else f'Story dated {nice(a["date"], True)}'
    back = ('', 'Customer stories') if a['customer_story'] else (('learn/', 'Learn') if a['learn'] else ('blog/', 'Blog'))
    if a['learn']:   # a breadcrumb: Learn, then the category
        kick = f'<a href="{PATH}learn/">Learn</a> <span class="sep">&rsaquo;</span> <a href="{PATH}learn/category/{cat_slug(a["tag"])}/">{esc(a["tag"])}</a> <span class="sep">·</span> '
        tag_txt = ''
    else: tag_txt = esc(a["tag"]) + ' <span class="sep">·</span> '
    body = f'''
<article class="article"><div class="band-narrow measure">
<p class="kicker">{kick}{tag_txt}<time datetime="{a["date"]}">{nice(a["date"], True)}</time></p>
<h1>{esc(a["title"])}</h1><p class="support lead">{esc(a["subtitle"])}</p>{byline(a)}{draft}{film}{hero}
<div class="prose">{html_body}</div>{readon}
<p class="source">{where}. Shown on {", ".join(SITES[s] for s in a["sites"])}.</p>
<p><a class="tlink" href="{PATH}{back[0]}">&larr; {back[1]}</a></p>
</div></article>'''
    (d / 'index.html').write_text(chrome(a['title'] + (' | Toca' if a['learn'] else ' | Toca news'), a['subtitle'], body, a['url'], current='learn' if a['learn'] else '', article=a))
    if a['learn']:   # it was first published under articles/ (11 Nov 2026): forward that address. A page, not a Netlify
        # redirect: a redirect's root-relative target escapes toca.io's proxy (netlify.toml)
        old = SITE / 'articles' / a['slug']; old.mkdir(parents=True, exist_ok=True)
        to = f'{PATH}learn/{a["slug"]}/'
        old.joinpath('index.html').write_text(f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{esc(a["title"])}</title>
<link rel="canonical" href="{a["url"]}"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url={to}"></head>
<body><p>This article has moved to <a href="{to}">{esc(a["title"])}</a>.</p><script>location.replace({json.dumps(to)} + location.hash)</script></body></html>''')

# ---------------------------------------------------------------- learn (after fin.ai/learn): guides and comparisons as rows
def write_learn(all_arts):
    arts = [a for a in all_arts if a['learn']]
    cats = list(LEARN) + sorted({a['tag'] for a in arts} - set(LEARN))
    cats = [c for c in cats if any(a['tag'] == c for a in arts)]
    crumbs_ld = lambda items: {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(items)]}
    def page(cat):
        shown = [a for a in arts if not cat or a['tag'] == cat]
        here = f'{BASE}/learn/' + (f'category/{cat_slug(cat)}/' if cat else '')
        on = lambda yes: ' aria-current="page"' if yes else ''
        pills = f'<nav class="sectors pills" aria-label="Category"><a href="{PATH}learn/"{on(not cat)}>All</a>' + ''.join(
            f'<a href="{PATH}learn/category/{cat_slug(c)}/"{on(c == cat)}>{esc(c)}</a>' for c in cats) + '</nav>'
        rows = ''.join(f'<a class="lrow" href="{esc(a["href"])}"><span class="lt">{esc(a["title"])}</span><span class="ls">{esc(a["subtitle"])}</span>'
                       f'<time datetime="{a.get("updated") or a["date"]}">{nice(a.get("updated") or a["date"], True)}</time></a>' for a in shown)
        crumb = f'<a href="{PATH}">News</a> <span class="sep">&rsaquo;</span> ' + (f'<a href="{PATH}learn/">Learn</a> <span class="sep">&rsaquo;</span> <span>{esc(cat)}</span>' if cat else '<span>Learn</span>')
        trail = [('News', BASE + '/'), ('Learn', BASE + '/learn/')] + ([(cat, here)] if cat else [])
        ld = [crumbs_ld(trail), {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': cat or 'Learn', 'url': here, 'inLanguage': 'en-GB',
              'mainEntity': {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': a['url'], 'name': a['title']} for i, a in enumerate(shown)]}}]
        ld_html = ''.join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False).replace('</', '<\\/') + '</script>' for x in ld)
        intro = LEARN.get(cat, '') if cat else LEARN_INTRO
        body = f'''
<section class="page-head learn-head"><div class="band-narrow"><p class="crumbs">{crumb}</p><h1>{esc(cat or "Learn")}</h1>{f'<p class="support">{esc(intro)}</p>' if intro else ''}</div></section>
<section class="band learn"><div class="band-narrow">
{pills}
<p class="lcount">{len(shown)} article{"" if len(shown) == 1 else "s"}</p>
<div class="lrows">{rows}</div>
</div></section>{ld_html}'''
        title = f'{cat} | Toca Learn' if cat else 'Learn: guides and comparisons | Toca'
        d = SITE / 'learn' / ('category/' + cat_slug(cat) if cat else ''); d.mkdir(parents=True, exist_ok=True)
        (d / 'index.html').write_text(chrome(title, intro or LEARN_INTRO, body, here, current='learn'))
        return here
    return [page('')] + [page(c) for c in cats]

def write_404():
    body = f'''
<section class="page-head"><div class="band-narrow"><p class="kicker">404</p><h1>Not here.</h1><p class="support">That story may have moved to Medium, or the link is old. <a class="tlink" href="{PATH}">All news</a>.</p></div></section>'''
    (SITE / '404.html').write_text(chrome('Not found | Toca news', 'Page not found.', body, BASE + '/404.html'))

# ---------------------------------------------------------------- main
def main():
    for d in ('articles', 'feed', 'fonts', 'img/full', 'img/logos', 'blog', 'learn'):
        if (SITE / d).exists(): shutil.rmtree(SITE / d)
    (SITE / 'css').mkdir(parents=True, exist_ok=True)
    for c in ('site.css', 'news.css'): shutil.copy(ROOT / 'css' / c, SITE / 'css' / c)
    # the shared site.css loads fonts from url(../assets/fonts/…) relative to /css/, so they live at /assets/fonts/
    fdst = SITE / 'assets/fonts'; fdst.mkdir(parents=True, exist_ok=True)
    for f in (ROOT / 'fonts').glob('*.woff2'): shutil.copy(f, fdst / f.name)
    shutil.copy(ROOT / 'news-cards.js', SITE / 'news-cards.js')
    shutil.copy(ROOT / 'img' / 'toca-mark.svg', SITE / 'toca-mark.svg')   # header, footer and favicon; the pink mark as toca.health serves it
    shutil.copy(ROOT / 'FEED.md', SITE / 'llms.txt')   # the integration how-to for the sister sites' people and agents; unlisted, plain text
    everything = load(); arts = [a for a in everything if not a.get('draft')]
    write_feeds(arts); write_home(arts); write_blog(arts); learn_urls = write_learn(arts); write_404()
    for a in everything: write_article(a)   # drafts get a page to preview, but no card and no feed entry
    (SITE / '_headers').write_text('''/feed.json
  Access-Control-Allow-Origin: *
  Cache-Control: public, max-age=300
/feed/*.json
  Access-Control-Allow-Origin: *
  Cache-Control: public, max-age=300
/archive.json
  Access-Control-Allow-Origin: *
  Cache-Control: public, max-age=3600
/img/cards/*
  Access-Control-Allow-Origin: *
  Cache-Control: public, max-age=604800
/news-cards.js
  Access-Control-Allow-Origin: *
  Cache-Control: public, max-age=3600
/llms.txt
  Access-Control-Allow-Origin: *
  Content-Type: text/plain; charset=utf-8
  Cache-Control: public, max-age=3600
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
''')
    (SITE / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + BASE + '/sitemap.xml\n')
    urls = [f'<url><loc>{BASE}/</loc><lastmod>{BUILT}</lastmod></url>', f'<url><loc>{BASE}/blog/</loc><lastmod>{BUILT}</lastmod></url>']
    urls += [f'<url><loc>{u}</loc><lastmod>{BUILT}</lastmod></url>' for u in learn_urls]
    urls += [f'<url><loc>{a["url"]}</loc><lastmod>{a.get("updated") or a["date"]}</lastmod></url>' for a in arts if not a.get('external') or a['video']]
    (SITE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(urls) + '</urlset>')
    # house rule shared with gen.py on toca.io: no em dashes in anything we write (site.css is shared, and has one in a comment)
    for p in SITE.rglob('*'):
        if p.suffix in ('.html', '.json', '.js', '.xml', '.txt') and '\u2014' in p.read_text():
            raise SystemExit(f'em dash in {p.relative_to(SITE)}')
    # every link and asset the pages use is root-absolute under PATH, a full URL, a fragment or mailto: (see PATH)
    for p in SITE.rglob('*.html'):
        bad = [v for v in re.findall(r'\s(?:href|src|poster|action)="([^"]*)"', p.read_text()) if not v.startswith((PATH, 'https://', 'http://', '#', 'mailto:'))]
        if bad: raise SystemExit(f'link not under {PATH} in {p.relative_to(SITE)}: {", ".join(bad[:3])}')
    n_local = sum(1 for a in arts if not a.get('external') or a['video']); n_draft = len(everything) - len(arts); n_cust = sum(1 for a in arts if a['customer_story'])
    n_learn = sum(1 for a in arts if a['learn'])
    fed = [a for a in arts if a['in_feed']]
    print(f'built {len(arts)} stories ({n_cust} customer, {n_learn} learn (not in feeds unless feed: true), {n_local} with their own page, {n_draft} draft); feed.json has {min(len(fed), FEED_MAX)}; per site: ' + ', '.join(f'{s} {sum(1 for a in fed if s in a["sites"])}' for s in SITES))

if __name__ == '__main__': main()
