#!/usr/bin/env python3
"""Crop the rendered card faces to trim size and write the print PDFs."""
from PIL import Image

OUT = '../../public/'
full = [Image.open(OUT + f'business-card-{f}.png').convert('RGB') for f in ('front', 'back')]

# The art is drawn 2.25 x 3.75in: trim 2 x 3.5in plus 1/8in bleed on every side.
dpi = round(full[0].size[1] / 3.75)   # tall side is 3.75in with bleed
bleed = round(0.125 * dpi)
trim = [im.crop((bleed, bleed, im.size[0] - bleed, im.size[1] - bleed)) for im in full]

# with-bleed version, for printers that ask for it
full[0].save(OUT + 'business-card-print-with-bleed.pdf', 'PDF', resolution=dpi,
             save_all=True, append_images=[full[1]])
# exact 2 x 3.5in trim -- standard US business card, vertical
trim[0].save(OUT + 'business-card-print.pdf', 'PDF', resolution=dpi,
             save_all=True, append_images=[trim[1]])
# the PNGs show the card as it will actually be cut
for im, f in zip(trim, ('front', 'back')):
    im.save(OUT + f'business-card-{f}.png')

# one-sided card: single page, blank back (an NFC tag goes there)
single_full = Image.open(OUT + 'business-card-single.png').convert('RGB')
sdpi = round(single_full.size[1] / 3.75)          # rendered at 2x -> 600 DPI
sbleed = round(0.125 * sdpi)
single = single_full.crop((sbleed, sbleed,
                           single_full.size[0] - sbleed, single_full.size[1] - sbleed))
single.save(OUT + 'business-card-single-print.pdf', 'PDF', resolution=sdpi)
single_full.save(OUT + 'business-card-single-print-with-bleed.pdf', 'PDF', resolution=sdpi)
single.save(OUT + 'business-card-single.png')

w, h = trim[0].size
fw, fh = full[0].size
print(f'  business-card-print.pdf             {w}x{h}px = {w/dpi:.2f} x {h/dpi:.2f}in @ {dpi} DPI')
print(f'  business-card-print-with-bleed.pdf  {fw}x{fh}px = {fw/dpi:.2f} x {fh/dpi:.2f}in @ {dpi} DPI')
sw, sh = single.size
print(f'  business-card-single-print.pdf      {sw}x{sh}px = {sw/sdpi:.2f} x {sh/sdpi:.2f}in @ {sdpi} DPI, 1 page')
