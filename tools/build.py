"""Build an offline-friendly static course; no CDN or browser dependencies."""
from pathlib import Path
import html
import re
import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'docs'
OUT.mkdir(exist_ok=True)
files = [ROOT / 'README.md'] + sorted(ROOT.glob('[0-9][0-9]_*.md')) + [ROOT / 'appendix.md', ROOT / 'references.md']

def target(p):
    return 'index.html' if p.name == 'README.md' else p.stem + '.html'

def title(p):
    return p.read_text(encoding='utf-8').splitlines()[0].removeprefix('# ')

for index, source in enumerate(files):
    raw = source.read_text(encoding='utf-8')
    raw = re.sub(r'\]\(([^):]+)\.md(#[^)]*)?\)', lambda m: '](' + ('index' if m[1] == 'README' else m[1]) + '.html' + (m[2] or '') + ')', raw)
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'], extension_configs={'toc': {'permalink': False}})
    body = md.convert(raw)
    nav = ''.join(f'<a {"aria-current=\"page\"" if f == source else ""} href="{target(f)}"><span>{"START" if i == 0 else f"{i-1:02}" if i < 15 else "+"}</span>{html.escape(title(f))}</a>' for i,f in enumerate(files))
    prev = f'<a href="{target(files[index-1])}">← {html.escape(title(files[index-1]))}</a>' if index else '<span></span>'
    nxt = f'<a href="{target(files[index+1])}">{html.escape(title(files[index+1]))} →</a>' if index+1 < len(files) else '<a href="index.html">教材のトップへ →</a>'
    home = '''<section class="hero"><div class="eyebrow">FACTFULNESS / SELF-STUDY GUIDE</div><p class="hero-title">思い込みから、<br><em>確かめる習慣へ。</em></p><p>ニュースにも、仕事にも、日々の選択にも。<br>10の本能を手がかりに、数字との付き合い方を学ぶ。</p><a class="button" href="00_introduction.html">学習をはじめる <span>↗</span></a><div class="hero-stats"><span>10 <small>の本能</small></span><span>自分のペースで <small>読む・考える・試す</small></span></div><div class="orb" aria-hidden="true"><i></i><i></i><i></i><b>FACT<br>FULL<br>NESS<span>見方を、ひらく。</span></b></div></section>''' if index == 0 else ''
    page = f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="FACTFULNESSの10の本能と統計の基礎を、独自の解説・架空データ・演習で学ぶ日本語自習教材。"><title>{html.escape(title(source))} | FACTFULNESS 学習ノート</title><link rel="stylesheet" href="style.css"></head>
<body><a class="skip" href="#content">本文へ移動</a><header><a class="brand" href="index.html"><span class="brand-icon">f.</span> FACTFULNESS <small>学習ノート</small></a><span class="header-note">数字を、判断の味方に。</span></header><div class="layout"><aside><div class="nav-label">LEARNING PATH <span>学習の道すじ</span></div><nav aria-label="教材の目次">{nav}</nav><p class="aside-note">独自に作成した非公式教材<br>予備知識なしで、ここから。</p></aside><main id="content">{home}<div class="page-meta">SELF-STUDY / 日本語の自習教材 <span>{index+1:02} / {len(files):02}</span></div><article>{body}</article><nav class="pager" aria-label="前後のページ">{prev}{nxt}</nav><footer>FACTFULNESS 学習ノート · 独自の解説と演習で学ぶ<br>数値例はすべて架空データです。実測統計ではありません。 <a href="references.html">出典と教材の位置づけ</a></footer></main></div></body></html>'''
    (OUT / target(source)).write_text(page, encoding='utf-8')
(OUT / '.nojekyll').touch()
print(f'Built {len(files)} pages into {OUT}')
