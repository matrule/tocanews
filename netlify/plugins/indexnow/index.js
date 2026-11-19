/* IndexNow after a production deploy (17 Nov 2026; toca.io's SEO-GEO.md 1.4).
   Sends every URL in the deployed sitemap to IndexNow (Bing, and through it Copilot and ChatGPT search, plus
   Yandex and others), so a new Learn article or story is known the same day instead of waiting for a crawl.
   The key file is written by build.py (INDEXNOW_KEY) into the site root. Its address is worked out from the
   sitemap's first URL, which is BASE/, so this keeps working when BASE moves from news.toca.io to
   www.toca.io/news (the key file then sits at www.toca.io/news/<key>.txt and covers the URLs beneath it).
   Production deploys only; set INDEXNOW=off in Netlify's environment variables to stop it. Never fails the deploy. */
'use strict';
const fs = require('fs');
const path = require('path');

module.exports = {
  async onSuccess({ constants }) {
    if (process.env.CONTEXT !== 'production' || process.env.INDEXNOW === 'off') {
      console.log('indexnow: skipped (production deploys only, and INDEXNOW is not off)');
      return;
    }
    try {
      const dir = constants.PUBLISH_DIR;
      const keyFile = fs.readdirSync(dir).find(f => /^[0-9a-f]{32}\.txt$/.test(f));
      if (!keyFile) { console.log('indexnow: no key file in the publish folder'); return; }
      const key = fs.readFileSync(path.join(dir, keyFile), 'utf8').trim();
      const sitemap = fs.readFileSync(path.join(dir, 'sitemap.xml'), 'utf8');
      const urls = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]);
      if (!urls.length) { console.log('indexnow: the sitemap has no URLs'); return; }
      const base = urls[0].endsWith('/') ? urls[0] : urls[0] + '/';   // BASE/, the home page
      const host = new URL(base).host;
      const r = await fetch('https://api.indexnow.org/indexnow', {
        method: 'POST',
        headers: { 'content-type': 'application/json; charset=utf-8' },
        body: JSON.stringify({ host, key, keyLocation: base + keyFile, urlList: urls })
      });
      console.log(`indexnow: sent ${urls.length} URLs for ${host}, status ${r.status}`);
    } catch (e) {
      console.log('indexnow: ping failed, deploy unaffected: ' + (e && e.message));
    }
  }
};
