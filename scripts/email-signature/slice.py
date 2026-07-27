#!/usr/bin/env python3
"""
Slice the master signature card into individually-linkable pieces and emit a
Gmail-pasteable HTML signature.

Gmail lets an inserted image carry exactly ONE link, so the Instagram / YouTube
icons in a single flat PNG can't be clicked. This cuts the same artwork into 4
tiles laid out in a table, each wrapped in its own <a>, so the design is pixel
identical but the icons are real links.

  in : public/email-signature.png   (2x master, 1000x336)
  out: public/sig/*.png             (2x tiles)
       public/email-signature/index.html  (the copy-paste page)
"""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PUB = os.path.join(ROOT, 'public')

SITE = 'https://kayleerenaud.com'
IG = 'https://www.instagram.com/the.miss.kaylee/'
YT = 'https://www.youtube.com/@the.miss.kaylee'

W, H = 500, 168          # design (CSS) size of the card

master = Image.open(os.path.join(PUB, 'email-signature.png')).convert('RGBA')
scale = master.size[0] / W

# Gmail can't be trusted with alpha on some clients — flatten onto the card bg.
flat = Image.new('RGB', master.size, (20, 17, 15))
flat.paste(master, (0, 0), master)

# --- slice geometry, in design px -------------------------------------------
SPLIT_Y = 110            # horizontal cut: above = name block, below = link row
IG_X0, IG_X1 = 290, 331  # gutters either side of the instagram badge
YT_X1 = 368              # gutter after the youtube badge

TILES = [
    # name,       box (design px),                  link
    ('top',       (0,      0,       W,     SPLIT_Y), SITE),
    ('row-left',  (0,      SPLIT_Y, IG_X0, H),       SITE),
    ('row-ig',    (IG_X0,  SPLIT_Y, IG_X1, H),       IG),
    ('row-yt',    (IG_X1,  SPLIT_Y, YT_X1, H),       YT),
    ('row-right', (YT_X1,  SPLIT_Y, W,     H),       SITE),
]

os.makedirs(os.path.join(PUB, 'sig'), exist_ok=True)
os.makedirs(os.path.join(PUB, 'email-signature'), exist_ok=True)

cells = []
link = {}
for name, (x0, y0, x1, y1), href in TILES:
    box = tuple(round(v * scale) for v in (x0, y0, x1, y1))
    flat.crop(box).save(os.path.join(PUB, 'sig', f'{name}.png'))
    cells.append((name, x1 - x0, y1 - y0))
    link[name] = href
    print(f'  sig/{name}.png  {box[2]-box[0]}x{box[3]-box[1]}px  -> displays {x1-x0}x{y1-y0}')


def img(name, w, h, href, alt=''):
    return (
        f'<a href="{href}" style="text-decoration:none;border:0;">'
        f'<img src="{SITE}/sig/{name}.png" width="{w}" height="{h}" alt="{alt}" '
        f'style="display:block;border:0;outline:none;text-decoration:none;'
        f'-ms-interpolation-mode:bicubic;" /></a>'
    )


top_w, top_h = cells[0][1], cells[0][2]
row = ''.join(
    f'<td style="padding:0;font-size:0;line-height:0;">'
    f'{img(n, w, h, link[n], alt)}</td>'
    for (n, w, h), alt in zip(cells[1:], ['Kaylee Renaud — kayleerenaud.com',
                                          'Instagram', 'YouTube', ''])
)

signature = f'''<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
  <tr>
    <td colspan="4" style="padding:0;font-size:0;line-height:0;">
      {img(cells[0][0], top_w, top_h, SITE, 'Kaylee Renaud — Film, Costume, Writing')}
    </td>
  </tr>
  <tr>{row}</tr>
</table>'''


# ---------------------------------------------------------------------------
#  OPTION A (recommended): ONE flat image + a real-text link row underneath.
#  Nothing to come apart when dragged, and the links still work when a
#  recipient's client blocks images (which would erase an image-only sig).
# ---------------------------------------------------------------------------
ROSE_TEXT = '#a84f68'   # deeper rose — same hue as --accent, readable on white
MUTED = '#9a9089'

def textlink(label, href):
    return (f'<a href="{href}" style="color:{ROSE_TEXT};text-decoration:none;'
            f'font-family:Georgia,\'Times New Roman\',serif;font-size:12px;'
            f'letter-spacing:.06em;">{label}</a>')


sep = (f'<span style="color:{MUTED};font-family:Georgia,serif;font-size:12px;'
       f'padding:0 8px;">&middot;</span>')

flat_sig = f'''<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;">
  <tr>
    <td style="padding:0;font-size:0;line-height:0;">
      <a href="{SITE}" style="text-decoration:none;border:0;"><img
        src="{SITE}/email-signature.png" width="{W}" height="{H}"
        alt="Kaylee Renaud — Film, Costume, Writing — kayleerenaud.com"
        style="display:block;border:0;outline:none;-ms-interpolation-mode:bicubic;" /></a>
    </td>
  </tr>
  <tr>
    <td style="padding:9px 0 0 4px;line-height:1.4;">
      {textlink('kayleerenaud.com', SITE)}{sep}{textlink('Instagram', IG)}{sep}{textlink('YouTube', YT)}
    </td>
  </tr>
</table>'''

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Email signature &mdash; Kaylee Renaud</title>
<style>
  body {{ margin:0; padding:40px 20px 72px; background:#14110f; color:#f1ece4;
         font-family:Georgia,serif; line-height:1.6; }}
  .wrap {{ max-width:660px; margin:0 auto; }}
  h1 {{ font-size:1.5rem; font-weight:600; margin:0 0 .3rem; }}
  h2 {{ font-size:1.05rem; font-weight:600; margin:2.6rem 0 .3rem; color:#f1ece4; }}
  .tag {{ display:inline-block; font-size:.7rem; letter-spacing:.12em;
          text-transform:uppercase; padding:.18rem .5rem; border-radius:3px;
          vertical-align:.18em; margin-left:.5rem; }}
  .rec {{ background:#d98a9e; color:#14110f; }}
  .alt {{ background:#2c2722; color:#b0a89b; }}
  p  {{ color:#b0a89b; font-size:.95rem; }}
  ol {{ color:#b0a89b; font-size:.95rem; padding-left:1.2rem; }}
  li {{ margin:.35rem 0; }}
  .stage {{ background:#fff; padding:26px; border-radius:6px; margin:1.1rem 0 1.4rem; }}
  code {{ background:#1d1916; padding:.1rem .35rem; border-radius:3px; color:#d98a9e; }}
  hr {{ border:0; border-top:1px solid #2c2722; margin:3rem 0 0; }}
  a.dl {{ color:#d98a9e; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>Your email signature</h1>
  <p>Two versions. Pick one, select everything in the white box, copy, and paste it into
     <b>Gmail &rarr; Settings &rarr; See all settings &rarr; General &rarr; Signature</b>.</p>

  <h2>Option A &mdash; one solid image<span class="tag rec">recommended</span></h2>
  <p>The card is a single picture, so it can never come apart when you drag it.
     The card itself links to your portfolio, and the small line underneath carries all
     three links as real text &mdash; which also means they still work for anyone whose
     email app blocks images.</p>

  <div class="stage">
{flat_sig}
  </div>

  <h2>Option B &mdash; clickable icons<span class="tag alt">fragile</span></h2>
  <p>Identical artwork, but cut into tiles so the Instagram and YouTube badges are
     themselves links. Works fine once pasted &mdash; but if you click and drag it inside
     the editor, the tiles can separate.</p>

  <div class="stage">
{signature}
  </div>

  <hr>

  <h2>Pasting it in</h2>
  <ol>
    <li>Click just above the card and drag to just below it to select the whole thing.</li>
    <li><b>Copy</b> (Cmd&#8209;C / Ctrl&#8209;C). Don&rsquo;t drag the image after pasting &mdash; just click once and type around it.</li>
    <li>In Gmail: <b>Settings &rarr; See all settings &rarr; General &rarr; Signature &rarr; Create new</b>.</li>
    <li><b>Paste</b>, then <b>Save Changes</b> at the very bottom of the page.</li>
  </ol>
  <p>Raw file if you ever need it: <a class="dl" href="/email-signature.png">email-signature.png</a>
     (1000&times;336, retina). Insert with Gmail&rsquo;s image button, then select it and link it to
     <code>kayleerenaud.com</code>.</p>
</div>
</body>
</html>
'''

with open(os.path.join(PUB, 'email-signature', 'index.html'), 'w') as f:
    f.write(page)
print('  email-signature/index.html written (options A + B)')
