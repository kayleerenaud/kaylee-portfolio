#!/usr/bin/env python3
"""Kaylee-themed hoodie artwork — front (left chest) and back (tour-tee style).

Outputs, for each face:
  * <face>-print.pdf  — exact print size, VECTOR type, transparent background.
                        This is the file a screenprinter or DTG shop wants.
  * <face>-art.png    — 300 DPI transparent raster, for shops that want PNG.
  * <face>-mock.png   — the same art composited on the garment colour so a
                        human can see what it will look like.

Two ink colours only (cream + rose) so it can be screenprinted cheaply on a
dark hoodie.

    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/hoodie/build-hoodie.py
"""
import os
from weasyprint import HTML
import pypdfium2 as pdfium
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = os.path.join(ROOT, 'site') if os.path.isdir(os.path.join(ROOT, 'site')) else ROOT
def furl(rel): return 'file://' + os.path.join(SITE, rel)

OUT = os.path.join(SITE, 'public', 'hoodie')
os.makedirs(OUT, exist_ok=True)

GARMENT = (20, 17, 15)          # #14110f — the hoodie itself
CREAM   = '#f1ece4'
ROSE    = '#d98a9e'

# ── the back: credits printed like tour dates ────────────────────────────────
TOUR = [
    ('2024', 'Like Mother',                     'Costume Designer'),
    ('2024', 'Elli',                            'Director · Editor'),
    ('2024', 'New York Theater Ballet',         'Wardrobe'),
    ('2025', 'Knights of the Old Republic I',   'Costume Re-design'),
    ('2025', 'Schmoopy',                        'Writer · Director'),
    ('2025', 'Spirit Temple No. 7',             'Director · Editor'),
    ('2025', "Together, I’m Pieces",            'Director · Editor'),
    ('2026', 'Weightless',                      'Costume Designer'),
    ('2026', 'As You Like It',                  'Costume Assistant'),
    ('2026', 'Knights of the Old Republic II',  'Costume Director'),
    ('2026', 'Eurydice',                        'Costume Designer'),
]

FONTS = f"""
@font-face {{ font-family:'KScript'; src:url('{furl("public/fonts/KayleeScript-Regular.ttf")}'); }}
@font-face {{ font-family:'Spec'; src:url('{furl("scripts/cv-assets/Spectral-Regular.ttf")}');
  font-weight:400; }}
@font-face {{ font-family:'Spec'; src:url('{furl("scripts/cv-assets/Spectral-Medium.ttf")}');
  font-weight:500; }}
@font-face {{ font-family:'Spec'; src:url('{furl("scripts/ig-carousel/Spectral-Bold.ttf")}');
  font-weight:700; }}
@font-face {{ font-family:'Spec'; src:url('{furl("scripts/ig-carousel/Spectral-ExtraBold.ttf")}');
  font-weight:800; }}
"""

# ── BACK ─────────────────────────────────────────────────────────────────────
rows = "".join(
    f"<div class='row'><span class='yr'>{y}</span>"
    f"<span class='ttl'>{t}</span><span class='dots'></span>"
    f"<span class='role'>{r}</span></div>"
    for y, t, r in TOUR)

BACK = f"""<!doctype html><html><head><meta charset='utf-8'><style>
{FONTS}
@page {{ size: 12in 14in; margin: 0; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'Spec', Georgia, serif; color:{CREAM};
  width:12in; height:14in; padding:0.35in 0.5in;
  display:flex; flex-direction:column; text-align:center; }}

.name {{ font-family:'KScript', cursive; font-size:150pt; line-height:.86; color:{ROSE}; }}
.sub {{ font-weight:700; font-size:20pt; letter-spacing:.34em; text-transform:uppercase;
  margin-top:.3in; }}
.tag {{ font-weight:500; font-size:13.5pt; letter-spacing:.2em; text-transform:uppercase;
  color:{ROSE}; margin-top:.12in; }}

.bar {{ display:flex; align-items:center; gap:.16in; margin:.3in 0 .26in; }}
.bar .ln {{ flex:1; height:2.2px; background:{CREAM}; opacity:.85; }}
.bar .dot {{ width:8px; height:8px; background:{ROSE}; transform:rotate(45deg); }}

.list {{ flex:1; display:flex; flex-direction:column; justify-content:space-between; }}
.row {{ display:flex; align-items:baseline; gap:.14in; text-align:left; }}
.yr {{ flex:0 0 1.05in; font-weight:700; font-size:16pt; letter-spacing:.06em; color:{ROSE}; }}
.ttl {{ font-weight:800; font-size:20pt; letter-spacing:.035em; text-transform:uppercase;
  white-space:nowrap; }}
.dots {{ flex:1; height:1px; background:{CREAM}; opacity:.28; transform:translateY(-4px); }}
.role {{ flex:0 0 3.1in; white-space:nowrap; text-align:right; font-weight:500; font-size:13pt;
  letter-spacing:.11em; text-transform:uppercase; opacity:.8; }}

.foot {{ margin-top:.2in; }}
.foot .rule {{ height:2.2px; background:{CREAM}; opacity:.85; margin-bottom:.16in; }}
.foot .site {{ font-weight:500; font-size:14pt; letter-spacing:.3em; text-transform:uppercase; }}
</style></head><body>
  <div class='name'>Kaylee Renaud</div>
  <div class='sub'>Costume &middot; Film &middot; Writing</div>
  <div class='tag'>The No-Budget World Tour &nbsp;·&nbsp; 2024–2026</div>
  <div class='bar'><span class='ln'></span><span class='dot'></span><span class='ln'></span></div>
  <div class='list'>{rows}</div>
  <div class='foot'><div class='rule'></div>
    <div class='site'>kayleerenaud.com</div></div>
</body></html>"""

# ── FRONT (left chest) ───────────────────────────────────────────────────────
FRONT = f"""<!doctype html><html><head><meta charset='utf-8'><style>
{FONTS}
@page {{ size: 4in 2in; margin: 0; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'Spec', Georgia, serif; color:{CREAM};
  width:4in; height:2in; display:flex; flex-direction:column;
  align-items:flex-start; justify-content:center; padding:0 .12in; }}
.name {{ font-family:'KScript', cursive; font-size:54pt; line-height:.9; color:{ROSE}; }}
.rule {{ width:1.5in; height:2px; background:{CREAM}; opacity:.8; margin:.1in 0 .09in; }}
.svc {{ font-weight:500; font-size:9.5pt; letter-spacing:.26em; text-transform:uppercase; }}
</style></head><body>
  <div class='name'>Kaylee</div>
  <div class='rule'></div>
  <div class='svc'>Costume &middot; Film &middot; Writing</div>
</body></html>"""


def render(name, html, dpi=300):
    pdf_path = os.path.join(OUT, f'hoodie-{name}-print.pdf')
    HTML(string=html, base_url=SITE).write_pdf(pdf_path)

    doc = pdfium.PdfDocument(pdf_path)
    page = doc[0]
    w_in, h_in = page.get_width() / 72, page.get_height() / 72
    art = page.render(scale=dpi / 72, fill_color=(0, 0, 0, 0)).to_pil().convert('RGBA')
    art.save(os.path.join(OUT, f'hoodie-{name}-art.png'))

    mock = Image.new('RGBA', art.size, GARMENT + (255,))
    mock.alpha_composite(art)
    mock.convert('RGB').save(os.path.join(OUT, f'hoodie-{name}-mock.png'))

    print(f'  hoodie-{name}: {w_in:.2f} x {h_in:.2f} in  ->  {art.size[0]}x{art.size[1]}px @ {dpi} DPI')


render('back', BACK)
render('front', FRONT)
print('done.')
