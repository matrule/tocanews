/* news-cards.js · drop-in for toca.io and toca.health
   Renders the latest stories from news.toca.io/feed.json into a container.

   <div data-news-cards data-site="health" data-count="3"></div>
   <script src="/js/news-cards.js" defer></script>

   Three rules, in the code:
     1. The feed is data. Every string lands via textContent; no innerHTML anywhere.
     2. Only expected fields are read, and every URL must start with an allowed origin
        (news.toca.io itself, plus the places our stories are published), or the item is skipped.
     3. Fail quietly. Bad JSON, a network error or an empty result hides the container. */
(function () {
  'use strict';
  var FEED = 'https://news.toca.io/feed.json';
  var ALLOWED = ['https://news.toca.io/', 'https://medium.com/@toca.io/', 'https://www.legalgeek.co/'];
  var ok = function (u) { return typeof u === 'string' && ALLOWED.some(function (a) { return u.indexOf(a) === 0; }); };

  document.querySelectorAll('[data-news-cards]').forEach(function (box) {
    var site = box.getAttribute('data-site') || 'io', count = parseInt(box.getAttribute('data-count'), 10) || 3;
    fetch(FEED, { mode: 'cors', credentials: 'omit' })
      .then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (feed) {
        var items = (feed && Array.isArray(feed.items) ? feed.items : []).filter(function (it) {
          return it && typeof it.title === 'string' && ok(it.url) && (!it.image || ok(it.image)) && it._toca && Array.isArray(it._toca.sites) && it._toca.sites.indexOf(site) >= 0;
        }).slice(0, count);
        if (!items.length) throw 0;
        var frag = document.createDocumentFragment();
        items.forEach(function (it) {
          var a = document.createElement('a'); a.className = 'news-card'; a.href = it.url; if (it.url.indexOf('https://news.toca.io/') !== 0) { a.target = '_blank'; a.rel = 'noopener'; }
          if (it.image) { var img = document.createElement('img'); img.src = it.image; img.alt = ''; img.loading = 'lazy'; if (it._toca.image_width) { img.width = it._toca.image_width; img.height = it._toca.image_height; } a.appendChild(img); }
          var t = document.createElement('b'); t.textContent = it.title; a.appendChild(t);
          if (typeof it.summary === 'string' && it.summary) { var p = document.createElement('p'); p.textContent = it.summary; a.appendChild(p); }
          var m = document.createElement('span'); m.className = 'source'; m.textContent = (typeof it.date_published === 'string' ? it.date_published.slice(0, 10) : '') + (Array.isArray(it.tags) && typeof it.tags[0] === 'string' ? ' · ' + it.tags[0] : ''); a.appendChild(m);
          frag.appendChild(a);
        });
        box.textContent = ''; box.appendChild(frag); box.hidden = false;
      })
      .catch(function () { box.hidden = true; });
  });
})();
