#!/usr/bin/env python3
"""news.toca.io · static generator. No backend, no CMS.

  content/articles/*.md   one file per story: YAML front matter, optional Markdown body
  content/images/*        source images, any size
  site/                   the output (see OUTPUTS below)

Front matter fields:
  title, subtitle, date (YYYY-MM-DD), tag, sites (["io"], ["health"], ["legal"] or any mix),
  image (file name in content/images), external (URL: the story lives elsewhere, the card links out),
  link_text (optional), draft: true (optional: built to preview, left out of the index and every feed).
  kind: customer          puts the story on the customer wall (the home page). With it:
    customer, sector      who and which sector filter ("Healthcare", "Law", "Finance", "Charity", ...)
    logo                  file name in content/images, single-colour ink mark (recoloured to paper for the dark page); the name is used until one exists
    lead: true            pins this story as the wall's lead tile; otherwise the newest customer story leads
    wide: true            gives the tile two of the wall's three columns (every seventh tile is wide anyway); the lead always takes all three
    figure, figure_label  one number and its claim ("15%", "of England's GP referrals")
    quote, quote_by, quote_role
    video, video_start    a YouTube ID (and optional start second). The film plays on a page here, whatever `external` says.

A story with a body and no `external` gets its own page at /articles/<slug>/ and the card links there.

OUTPUTS
  index.html              customer stories: the wall, filters by sector, plus the latest news
  blog/index.html         the blog, everything that is not a customer story: lead, the latest BLOG_RECENT, then the archive as rows
  articles/<slug>/        native stories, and pages for any story with a film (the film plays here)
  feed.json               JSON Feed 1.1, newest FEED_MAX, all sites
  feed/<site>.json        the same, filtered to one site (io, health, legal)
  archive.json            everything, all sites
  news-cards.js           the drop-in renderer, served from here as well as vendored
  img/cards/*.webp        card thumbnails, CARD_W wide
  img/full/*.webp         images inside native articles, FULL_W wide
  404.html, robots.txt, sitemap.xml, _headers

The JSON is for the sister sites; it is not linked from the pages. FEED.md documents it.
Run: python3 build.py   (needs: pip install -r requirements.txt)"""
import re, json, pathlib, html, shutil, datetime
import frontmatter, markdown
from PIL import Image

ROOT = pathlib.Path(__file__).parent
CONTENT, SITE = ROOT / 'content', ROOT / 'site'
BASE = 'https://news.toca.io'
CARD_W = 640
FULL_W = 1600          # images inside an article body
FEED_MAX = 50
SITES = {'io': 'toca.io', 'health': 'toca.health', 'legal': 'toca.legal'}
VAULT = 'https://vault.toca.io'   # Toca Vault: docs and training, a fifth site in the family bar
BLOG_RECENT = 6
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
    return f'{BASE}/img/cards/{out.name}', im.width, im.height

def full_image(name):
    """Resize once for an article body (WebP, at most FULL_W wide). Returns the site-relative path or None."""
    src = CONTENT / 'images' / name
    if not src.exists(): print('  missing image', name); return None
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

def load():
    arts = []
    for p in sorted((CONTENT / 'articles').glob('*.md')):
        fm = frontmatter.load(p)
        a = dict(fm.metadata); a['body'] = fm.content.strip(); a['slug'] = slug_of(p)
        a['date'] = str(a['date'])[:10]
        a.setdefault('sites', ['io']); a.setdefault('tag', 'Blog'); a.setdefault('subtitle', '')
        a['customer_story'] = a.get('kind') == 'customer'
        for k in ('customer', 'sector', 'figure', 'figure_label', 'quote', 'quote_by', 'quote_role', 'video', 'logo'): a.setdefault(k, '')
        a['video'] = str(a['video']) if a['video'] else ''
        bad = [s for s in a['sites'] if s not in SITES]
        assert not bad, f'{p.name}: unknown site {bad}'
        a['url'] = a.get('external') or f'{BASE}/articles/{a["slug"]}/'
        # 'url' is the absolute, canonical link (used in JSON, canonical tags, sitemap: these must stay absolute
        # regardless of where the site is hosted). 'href' is what pages link with: external stories still go
        # out to their absolute URL, but a native story links relative to the site root, so cards work the
        # same on a Netlify preview domain as on news.toca.io once DNS is pointed.
        a['href'] = f'articles/{a["slug"]}/' if (a['video'] or not a.get('external')) else a['external']
        a['source'] = source_of(a['external']) if a.get('external') else 'news.toca.io'
        a['card'] = card_image(a.get('image'))
        a['body_images'] = []
        if a['body'] and not a.get('external'):
            a['body'], a['body_images'] = body_images(a['body'])
            a['html'] = markdown.markdown(a['body'], extensions=['extra', 'smarty'])
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
    (SITE / 'feed.json').write_text(feed_doc(arts[:FEED_MAX], BASE + '/feed.json', 'Toca news', BASE + '/archive.json'))
    (SITE / 'archive.json').write_text(feed_doc(arts, BASE + '/archive.json', 'Toca news · archive'))
    (SITE / 'feed').mkdir(exist_ok=True)
    for s, host in SITES.items():
        sub = [a for a in arts if s in a['sites']]
        (SITE / 'feed' / f'{s}.json').write_text(feed_doc(sub[:FEED_MAX], f'{BASE}/feed/{s}.json', f'Toca news · {host}'))

# ---------------------------------------------------------------- page chrome
def chrome(title, desc, body, canonical, depth=0, current='', dark=False):
    R = '../' * depth   # relative root, so the built pages open styled from file:// as well as the site root
    cur = lambda k: ' aria-current="page"' if k == current else ''
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" type="application/feed+json" title="Toca news" href="{BASE}/feed.json">
<link rel="icon" href="{R}toca-mark.svg" type="image/svg+xml">
<link rel="stylesheet" href="{R}css/site.css"><link rel="stylesheet" href="{R}css/news.css">
</head>
<body{' class="dark"' if dark else ''}>
<a class="skip" href="#main">Skip to content</a>
<div class="family"><nav class="family-in" aria-label="Toca sites"><a class="fsite" href="https://toca.io"><b>toca<span class="dim">.io</span></b><span class="what">The platform</span></a><a class="fsite" href="https://toca.health"><b>toca<span class="dim">.health</span></b><span class="what">Healthcare</span></a><a class="fsite" href="https://toca.legal"><b>toca<span class="dim">.legal</span></b><span class="what">Law firms</span></a><a class="fsite" href="{VAULT}"><b>vault<span class="dim">.toca.io</span></b><span class="what">Docs and training</span></a><span class="fsite fhere" aria-current="page"><b>news<span class="dim">.toca.io</span></b><span class="what">You are here</span></span></nav></div>
<header class="hdr"><div class="hdr-in"><a class="brand" href="{R}index.html"><img src="{R}toca-mark.svg" alt="" width="28" height="28"><span>toca.io</span> <span class="brand-sub">news</span></a><nav class="hdr-nav" aria-label="Site"><a href="{R}index.html"{cur('customers')}>Customer stories</a><a href="{R}blog/index.html"{cur('blog')}>Blog</a></nav></div></header>
<main id="main">{body}</main>
<footer class="foot">
  <p class="foot-line">The platform the platforms are built on.</p>
  <ul class="foot-links">
    <li><a href="{R}index.html">Customer stories</a></li>
    <li><a href="{R}blog/index.html">Blog</a></li>
    <li><a href="https://toca.io/platform.html">Platform</a></li>
    <li><a href="https://toca.io/partners.html">Partners</a></li>
    <li><a href="https://toca.io/company.html">Company</a></li>
    <li><a href="https://toca.io/pricing.html">Pricing</a></li>
    <li><a href="{VAULT}">Vault</a></li>
    <li><a href="https://toca.io/contact.html">Contact</a></li>
  </ul>
  <div class="foot-meta">
    <span class="wordmark"><img class="mark" src="{R}toca-mark.svg" alt="" width="26" height="26"><span>toca<span class="tld">.io</span></span></span>
    <a href="https://toca.health">toca.health</a>
    <a href="https://toca.legal">toca.legal</a>
    <a href="{R}index.html">news.toca.io</a>
    <span>&copy; 2026 Toca</span>
  </div>
  <p class="foot-company">TocaLabs Limited, trading as Toca. Registered in England &amp; Wales, company no. 11396834. VAT GB&nbsp;303504844. Reading, United Kingdom. Toca&reg;, Toca.Health&reg;, Tocabot&reg; and Tocalabs&reg; are registered trademarks of Tocalabs Ltd. <a href="mailto:sales@toca.io">sales@toca.io</a></p>
</footer>
</body></html>'''

# ---------------------------------------------------------------- index
def rel(url): return url.replace(BASE + '/', '')

def card(a, lead=False, R=''):
    img = f'<img src="{R}{esc(rel(a["card"][0]))}" width="{a["card"][1]}" height="{a["card"][2]}" alt="" loading="{"eager" if lead else "lazy"}">' if a['card'] else '<span class="noimg" aria-hidden="true"></span>'
    ext = a.get('external')
    ext = ext and not a['video']   # a film opens its page here, then links out
    target = ' target="_blank" rel="noopener"' if ext else ''
    where = f'<span class="where">{esc(a["source"])} &nearr;</span>' if ext else (f'<span class="where">Film</span>' if a['video'] else '')
    cls = 'story lead' if lead else 'story'
    h = 'h2' if lead else 'h3'
    href = a['href'] if a['href'].startswith('http') else R + a['href']
    return (f'<a class="{cls}" href="{esc(href)}"{target} data-tag="{esc(a["tag"])}" data-sites="{esc(" ".join(a["sites"]))}">'
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
def logo(a, R=''):
    """The customer's mark if we have one; the name set in the display face until we do."""
    if a['logo']:
        path = logo_image(a['logo'])
        if path: return f'<img class="mark" src="{R}{esc(path)}" alt="{esc(a["customer"])}">'
    return f'<span class="mark-text">{esc(a["customer"] or a["title"])}</span>'

def yt_thumb(vid): return f'https://i.ytimg.com/vi/{vid}/hqdefault.jpg'

def tile(a, i, R=''):
    """One tile on the customer wall. The first is the lead; every seventh after it is wide.
    Shape follows the data: a film gets a play tile, a quote gets a quote card, a figure gets a figure card."""
    href = a['href'] if a['href'].startswith('http') else R + a['href']
    ext = a.get('external') and not a['video']
    target = ' target="_blank" rel="noopener"' if ext else ''
    sector = f'<span class="sector">{esc(a["sector"])}</span>' if a['sector'] else ''
    fig = f'<span class="fig"><b>{esc(a["figure"])}</b><span>{esc(a["figure_label"])}</span></span>' if a['figure'] else ''
    common = f'data-sector="{esc(a["sector"])}" href="{esc(href)}"{target}'
    poster = f'{R}{esc(rel(a["card"][0]))}' if a['card'] else (yt_thumb(a['video']) if a['video'] else '')
    filmpic = lambda eager: f'<span class="pic film"><img src="{poster}" alt="" loading="{"eager" if eager else "lazy"}" onerror="this.remove()"><span class="play" aria-hidden="true"></span></span>'
    if i == 0:
        pic = filmpic(True) if a['video'] else (f'<span class="pic"><img src="{R}{esc(rel(a["card"][0]))}" alt="" loading="eager"></span>' if a['card'] else '<span class="pic empty"></span>')
        by = f'<span class="by"><b>{esc(a["quote_by"])}</b>{esc(a["quote_role"])}</span>' if a['quote_by'] and not fig else ''
        return f'<a class="tile lead" {common}><span class="txt">{logo(a, R)}{sector}<h2>{esc(a["title"])}</h2><p>{esc(a["subtitle"])}</p>{fig}{by}</span>{pic}</a>'
    wide = i % 7 == 0 or bool(a.get('wide'))
    if a['video']:
        if wide:   # text left, film right, like the lead
            return f'<a class="tile film wide pictured" {common}><span class="txt">{logo(a, R)}{sector}<h3>{esc(a["title"])}</h3><p>{esc(a["subtitle"])}</p>{fig}</span>{filmpic(False)}</a>'
        return f'<a class="tile film" {common}>{filmpic(False)}<span class="txt">{logo(a, R)}{sector}<h3>{esc(a["title"])}</h3></span></a>'
    if a['quote']:
        by = f'<span class="by"><b>{esc(a["quote_by"])}</b>{esc(a["quote_role"])}</span>' if a['quote_by'] else ''
        return f'<a class="tile said{" wide" if wide else ""}" {common}>{logo(a, R)}<blockquote>{esc(a["quote"])}</blockquote>{by}</a>'
    if wide and a['card']:
        return f'<a class="tile wide pictured" {common}><span class="txt">{logo(a, R)}{sector}<h3>{esc(a["title"])}</h3><p>{esc(a["subtitle"])}</p>{fig}</span><span class="pic"><img src="{R}{esc(rel(a["card"][0]))}" alt="" loading="lazy"></span></a>'
    return f'<a class="tile story" {common}>{logo(a, R)}{sector}<h3>{esc(a["title"])}</h3><p>{esc(a["subtitle"])}</p>{fig}</a>'

WALL_JS = (ROOT / 'js' / 'wall.js').read_text()

def write_home(arts):
    cust = sorted([a for a in arts if a['customer_story']], key=lambda a: (not a.get('lead'), ))  # stable: keeps date order after the pinned lead
    news = [a for a in arts if not a['customer_story']][:3]
    sectors = sorted({a['sector'] for a in cust if a['sector']})
    filt = '<nav class="sectors" aria-label="Sector"><a href="#" data-val="">All</a>' + ''.join(f'<a href="#sector={esc(x)}" data-val="{esc(x)}">{esc(x)}</a>' for x in sectors) + '</nav>'
    wall = ''.join(tile(a, i) for i, a in enumerate(cust))
    latest = ''.join(card(a) for a in news)
    body = f'''
<section class="page-head"><div class="band-narrow"><p class="kicker">Customer stories</p><h1>Built on Toca.</h1><p class="support">NHS trusts, law firms, charities and a portfolio platform: what they built, in their numbers and their words.</p></div></section>
<section class="band wall"><div class="band-narrow">
{filt}
<div class="wallgrid">{wall}</div>
<p class="empty" hidden>No stories in that sector yet.</p>
</div></section>
<section class="band latest"><div class="band-narrow">
<div class="strip-head"><h2>Latest from Toca</h2><a class="tlink" href="blog/index.html">All news and writing &rarr;</a></div>
<div class="grid">{latest}</div>
</div></section>
<script>{WALL_JS}</script>'''
    (SITE / 'index.html').write_text(chrome('Customer stories | Toca', 'What NHS trusts, law firms, charities and a portfolio platform built on Toca.', body, BASE + '/', current='customers', dark=True))

# ---------------------------------------------------------------- the blog
def write_blog(all_arts):
    R = '../'
    arts = [a for a in all_arts if not a['customer_story']]
    lead, recent, older = arts[0], arts[1:BLOG_RECENT + 1], arts[BLOG_RECENT + 1:]
    tags = sorted({a['tag'] for a in arts})
    def links(key, items, all_label):
        out = f'<a href="#" data-key="{key}" data-val="">{all_label}</a>'
        return out + ''.join(f'<a href="#{key}={esc(v)}" data-key="{key}" data-val="{esc(v)}">{esc(lbl)}</a>' for v, lbl in items)
    filt = (f'<nav class="filters" aria-label="Filter"><div class="frow"><span class="flab">Type</span>{links("tag", [(t, t) for t in tags], "All")}</div>'
            f'<div class="frow"><span class="flab">Site</span>{links("site", list(SITES.items()), "All three")}</div></nav>')
    def row(a):
        href = a['href'] if a['href'].startswith('http') else R + a['href']
        ext = a.get('external') and not a['video']
        tgt = ' target="_blank" rel="noopener"' if ext else ''
        return (f'<a class="story row" href="{esc(href)}"{tgt} data-tag="{esc(a["tag"])}" data-sites="{esc(" ".join(a["sites"]))}">'
                f'<time datetime="{a["date"]}">{nice(a["date"])}</time><span class="rt">{esc(a["title"])}</span><span class="tag">{esc(a["tag"])}</span></a>')
    years = {}
    for a in older: years.setdefault(a['date'][:4], []).append(a)
    archive = ''.join(f'<p class="year"><span>{y}</span><span class="n">{len(items)}</span></p><div class="rows">{"".join(row(a) for a in items)}</div>' for y, items in years.items())
    body = f'''
<section class="page-head"><div class="band-narrow"><p class="kicker">Blog</p><h1>What Toca has been up to.</h1><p class="support">Announcements, events, partner news and writing. Customer stories live <a class="tlink" href="../index.html">on their own page</a>.</p></div></section>
<section class="band news"><div class="band-narrow">
<div class="lead-wrap">{card(lead, lead=True, R=R)}</div>
<div class="grid">{''.join(card(a, R=R) for a in recent)}</div>
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
    (SITE / 'blog' / 'index.html').write_text(chrome('Blog | Toca news', 'Announcements, events, partner news and writing from Toca.', body, BASE + '/blog/', depth=1, current='blog'))

# ---------------------------------------------------------------- articles
def write_article(a):
    if a.get('external') and not a['video']: return
    if not a['body'] and not a['video']: return
    d = SITE / 'articles' / a['slug']; d.mkdir(parents=True, exist_ok=True)
    show_hero = a['card'] and a.get('image') not in a['body_images'] and not a['video']
    hero = f'<img class="hero" src="../../img/cards/{pathlib.Path(a["image"]).stem}.webp" alt="">' if show_hero else ''
    film = ''
    if a['video']:
        start = f'&start={int(a["video_start"])}' if a.get('video_start') else ''
        film = f'<div class="film-wrap"><iframe src="https://www.youtube-nocookie.com/embed/{esc(a["video"])}?rel=0{start}" title="{esc(a["title"])}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe></div>'
    draft = '<p class="draft">Draft. Built to preview; not in the index or any feed.</p>' if a.get('draft') else ''
    html_body = a['html'].replace(f'src="{BASE}/img/full/', 'src="../../img/full/')
    readon = f'<p class="readon"><a class="tlink" href="{esc(a["external"])}" target="_blank" rel="noopener">{esc(a.get("link_text") or "Read the full story")} on {esc(a["source"])} &nearr;</a></p>' if a.get('external') else ''
    kick = f'{esc(a["customer"])} <span class="sep">·</span> ' if a['customer'] else ''
    where = f'Published on news.toca.io, {nice(a["date"], True)}' if not a.get('external') else f'Story dated {nice(a["date"], True)}'
    back = ('index.html', 'Customer stories') if a['customer_story'] else ('blog/index.html', 'Blog')
    body = f'''
<article class="article"><div class="band-narrow measure">
<p class="kicker">{kick}{esc(a["tag"])} <span class="sep">·</span> <time datetime="{a["date"]}">{nice(a["date"], True)}</time></p>
<h1>{esc(a["title"])}</h1><p class="support lead">{esc(a["subtitle"])}</p>{draft}{film}{hero}
<div class="prose">{html_body}</div>{readon}
<p class="source">{where}. Shown on {", ".join(SITES[s] for s in a["sites"])}.</p>
<p><a class="tlink" href="../../{back[0]}">&larr; {back[1]}</a></p>
</div></article>'''
    (d / 'index.html').write_text(chrome(a['title'] + ' | Toca news', a['subtitle'], body, a['url'], depth=2))

def write_404():
    body = '''
<section class="page-head"><div class="band-narrow"><p class="kicker">404</p><h1>Not here.</h1><p class="support">That story may have moved to Medium, or the link is old. <a class="tlink" href="/">All news</a>.</p></div></section>'''
    (SITE / '404.html').write_text(chrome('Not found | Toca news', 'Page not found.', body, BASE + '/404.html'))

# ---------------------------------------------------------------- main
def main():
    for d in ('articles', 'feed', 'fonts', 'img/full', 'img/logos', 'blog'):
        if (SITE / d).exists(): shutil.rmtree(SITE / d)
    (SITE / 'css').mkdir(parents=True, exist_ok=True)
    for c in ('site.css', 'news.css'): shutil.copy(ROOT / 'css' / c, SITE / 'css' / c)
    # the shared site.css loads fonts from url(../assets/fonts/…) relative to /css/, so they live at /assets/fonts/
    fdst = SITE / 'assets/fonts'; fdst.mkdir(parents=True, exist_ok=True)
    for f in (ROOT / 'fonts').glob('*.woff2'): shutil.copy(f, fdst / f.name)
    shutil.copy(ROOT / 'news-cards.js', SITE / 'news-cards.js')
    everything = load(); arts = [a for a in everything if not a.get('draft')]
    write_feeds(arts); write_home(arts); write_blog(arts); write_404()
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
/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
''')
    (SITE / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: ' + BASE + '/sitemap.xml\n')
    urls = [f'<url><loc>{BASE}/</loc><lastmod>{BUILT}</lastmod></url>', f'<url><loc>{BASE}/blog/</loc><lastmod>{BUILT}</lastmod></url>']
    urls += [f'<url><loc>{BASE}/articles/{a["slug"]}/</loc><lastmod>{a["date"]}</lastmod></url>' for a in arts if not a.get('external') or a['video']]
    (SITE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(urls) + '</urlset>')
    # house rule shared with gen.py on toca.io: no em dashes in anything we write (site.css is shared, and has one in a comment)
    for p in SITE.rglob('*'):
        if p.suffix in ('.html', '.json', '.js', '.xml', '.txt') and '\u2014' in p.read_text():
            raise SystemExit(f'em dash in {p.relative_to(SITE)}')
    n_local = sum(1 for a in arts if not a.get('external') or a['video']); n_draft = len(everything) - len(arts); n_cust = sum(1 for a in arts if a['customer_story'])
    print(f'built {len(arts)} stories ({n_cust} customer, {n_local} with their own page, {n_draft} draft); feed.json has {min(len(arts), FEED_MAX)}; per site: ' + ', '.join(f'{s} {sum(1 for a in arts if s in a["sites"])}' for s in SITES))

if __name__ == '__main__': main()
