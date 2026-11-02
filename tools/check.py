"""Validate generated links, chapter/answer coverage and all local pages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re

root = Path(__file__).resolve().parent.parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]; self.ids=set(); self.lang=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='html': self.lang=a.get('lang')=='ja'
        if 'id' in a: self.ids.add(a['id'])
        for name in ('href','src'):
            if name in a: self.links.append(a[name])

pages={}
for f in (root/'docs').glob('*.html'):
    p=Page(); p.feed(f.read_text()); pages[f.name]=p
assert len(pages)==17, len(pages)
for name,p in pages.items():
    assert p.lang, name
    for href in p.links:
        u=urlsplit(href)
        if u.scheme or u.netloc: continue
        dest=(root/'docs'/unquote(u.path)) if u.path else root/'docs'/name
        assert dest.is_file(), (name,href)
        if u.fragment and dest.suffix=='.html': assert unquote(u.fragment) in pages[dest.name].ids, (name,href)
appendix=(root/'appendix.md').read_text()
for n in range(2,12):
    f=next(root.glob(f'{n:02}_*.md')); s=f.read_text()
    assert 2000 <= len(s) <=3500, (f,len(s))
    for section in ['学習目標','導入ケース','考えてみよう','基本解説','具体例','対処法','注意点','演習','章の要点']: assert section in s,(f,section)
    for suffix in ('Q','W','P'): assert f'{n}-{suffix}' in s and f'{n}-{suffix}' in appendix
    assert ('架空の場面' if n == 10 else '架空データ') in s, f
for f in root.glob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
        if not urlsplit(link).scheme: assert (root/urlsplit(link).path).is_file(),(f,link)
print('PASS: 17 HTML pages; local links/assets/fragments; 10 chapters and 30 matched exercises; Markdown links; chapter lengths')
