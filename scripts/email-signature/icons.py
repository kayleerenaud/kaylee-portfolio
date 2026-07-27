#!/usr/bin/env python3
"""
Draw the standalone Instagram / YouTube glyphs that sit BELOW the signature card
as their own clickable links.

They're drawn with PIL (rather than screenshotted) so they keep a real alpha
channel — that way they sit cleanly on a white Gmail background *and* on a dark
one, with no white box around them.

Colour is the deeper cousin of the site's rose accent (--accent #d98a9e), dark
enough to read as a link on white.

  out: public/sig/icon-instagram.png, public/sig/icon-youtube.png  (2x)
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, '..', '..', 'public', 'sig'))
os.makedirs(OUT, exist_ok=True)

SIZE = 22          # display size in px
SCALE = 2          # retina
SS = 8             # supersample factor for smooth edges
ROSE = (168, 79, 104, 255)   # #a84f68

D = SIZE * SCALE * SS        # working canvas edge
STROKE = round(2.1 * SCALE * SS / SCALE)  # ~2.1 css px of stroke, supersampled
STROKE = round(2.1 * SS)


def canvas():
    im = Image.new('RGBA', (D, D), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)


def u(v):
    """css px (in a 22-unit box) -> supersampled px"""
    return v / SIZE * D


def finish(im, name):
    im = im.resize((SIZE * SCALE, SIZE * SCALE), Image.LANCZOS)
    im.save(os.path.join(OUT, name))
    print(f'  sig/{name}  {im.size[0]}x{im.size[1]}px -> displays {SIZE}x{SIZE}')


# --- Instagram: rounded square + circle + corner dot -------------------------
im, d = canvas()
inset = u(1.4)
d.rounded_rectangle([inset, inset, D - inset, D - inset],
                    radius=u(6.0), outline=ROSE, width=STROKE)
r = u(4.8)
c = D / 2
d.ellipse([c - r, c - r, c + r, c + r], outline=ROSE, width=STROKE)
dot, dr = u(15.9), u(1.35)
d.ellipse([dot - dr, u(6.1) - dr, dot + dr, u(6.1) + dr], fill=ROSE)
finish(im, 'icon-instagram.png')

# --- YouTube: rounded rect + play triangle ----------------------------------
im, d = canvas()
top, bot = u(3.6), u(18.4)
d.rounded_rectangle([u(0.9), top, D - u(0.9), bot],
                    radius=u(4.6), outline=ROSE, width=STROKE)
d.polygon([(u(9.0), u(7.6)), (u(14.6), u(11.0)), (u(9.0), u(14.4))], fill=ROSE)
finish(im, 'icon-youtube.png')

# --- Site: her handwritten "K" in a badge, matching the favicon mark ---------
# Drawn from the real KayleeScript glyph (same source as public/favicon.svg) so
# the tab icon and the signature icon are the same mark.
from PIL import ImageFont

FONT = os.path.abspath(os.path.join(HERE, '..', '..', 'public', 'fonts',
                                    'KayleeScript-Regular.ttf'))

im, d = canvas()
d.rounded_rectangle([inset, inset, D - inset, D - inset],
                    radius=u(6.0), outline=ROSE, width=STROKE)

# size the K to sit comfortably inside the badge, then optically centre it
# KayleeScript is a fine monoline, so a bare "K" reads far lighter than the
# 2.1px badge outline beside it. stroke_width thickens the glyph to match.
f = ImageFont.truetype(FONT, int(u(15.2)))
sw = round(u(0.45))
x0, y0, x1, y1 = d.textbbox((0, 0), 'K', font=f, stroke_width=sw)
d.text(((D - (x1 - x0)) / 2 - x0, (D - (y1 - y0)) / 2 - y0), 'K', font=f,
       fill=ROSE, stroke_width=sw, stroke_fill=ROSE)
finish(im, 'icon-site.png')
