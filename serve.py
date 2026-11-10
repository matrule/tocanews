#!/usr/bin/env python3
"""Preview site/ the way it is served: under /news/, as at www.toca.io/news/ (toca.io's proxy) and at
news.toca.io (netlify.toml's /news/* rewrite). The pages link root-absolute under /news/ (build.py PATH),
so they no longer open styled from file://. A folder is served without adding the trailing slash, as
www.toca.io/news is through the proxy, so a relative link would show up broken here too.

Run: python3 serve.py [port]   then open http://localhost:8002/news/"""
import http.server, os, pathlib, sys

SITE = pathlib.Path(__file__).parent / 'site'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=str(SITE), **k)

    def translate_path(self, path):
        bare = path.split('?', 1)[0].split('#', 1)[0]
        if bare == '/news' or bare.startswith('/news/'): path = path[len('/news'):] or '/'
        fs = super().translate_path(path)
        index = os.path.join(fs, 'index.html')
        return index if os.path.isdir(fs) and os.path.isfile(index) else fs

    def send_error(self, code, message=None, explain=None):
        page = SITE / '404.html'
        if code != 404 or not page.exists(): return super().send_error(code, message, explain)
        body = page.read_bytes()
        self.send_response(404); self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body))); self.end_headers()
        if self.command != 'HEAD': self.wfile.write(body)

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8002
    print(f'http://localhost:{port}/news/')
    http.server.ThreadingHTTPServer.request_queue_size = 64   # the default 5 resets a page's burst of font requests
    http.server.ThreadingHTTPServer(('127.0.0.1', port), Handler).serve_forever()
