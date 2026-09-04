#!/usr/bin/env python3
"""Crop the rendered card faces to trim size and write the print PDFs."""
from PIL import Image

OUT = '../../public/'
full = [Image.open(OUT + f'business-card-{f}.png').convert('RGB') for f in ('front', 'back')]

# The art is drawn 3.75 x 2.25in: trim 3.5 x 2in plus 1/8in bleed on every side.
dpi = round(full[0].size[0] / 3.75)
bleed = round(0.125 * dpi)
trim = [im.crop((bleed, bleed, im.size[0] - bleed, im.size[1] - bleed)) for im in full]

# with-bleed version, for printers that ask for it
full[0].save(OUT + 'business-card-print-with-bleed.pdf', 'PDF', resolution=dpi,
             save_all=True, append_images=[full[1]])
# exact 3.5 x 2in trim -- the standard US business card size
trim[0].save(OUT + 'business-card-print.pdf', 'PDF', resolution=dpi,
             save_all=True, append_images=[trim[1]])
# the PNGs show the card as it will actually be cut
for im, f in zip(trim, ('front', 'back')):
    im.save(OUT + f'business-card-{f}.png')

w, h = trim[0].size
fw, fh = full[0].size
print(f'  business-card-print.pdf             {w}x{h}px = {w/dpi:.2f} x {h/dpi:.2f}in @ {dpi} DPI')
print(f'  business-card-print-with-bleed.pdf  {fw}x{fh}px = {fw/dpi:.2f} x {fh/dpi:.2f}in @ {dpi} DPI')
