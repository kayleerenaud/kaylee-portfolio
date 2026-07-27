#!/usr/bin/env bash
# Render the email signature card to retina PNGs with transparent rounded corners.
#   -> public/email-signature.png       the card; icons sit below it as real links
#   -> public/email-signature-full.png  all-in-one flat card with the icons baked in
# (headless Chromium renders at DPR 2, so output is 2x the CSS size)
set -euo pipefail
cd "$(dirname "$0")"

W=500; H=168; PORT=8931

# --- build the no-icons variant ---------------------------------------------
python3 - <<'PY'
import re
s = open('signature.html').read()
# drop the "|" divider and the icon badges from the bottom row
s = re.sub(r'\s*<span class="divider"></span>.*?</span>\s*(?=</div>)', '\n        ',
           s, flags=re.S)
open('.noicons.html', 'w').write(s)
PY

python3 -m http.server "$PORT" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true; rm -f .noicons.html .raw.png' EXIT
sleep 1.5

shoot () {   # <src html> <dest png>
  screenshot "http://127.0.0.1:$PORT/$1" .raw.png "$W" "$H" 1500 >/dev/null
  python3 - "$2" <<'PY'
import sys
from PIL import Image, ImageDraw
im = Image.open('.raw.png').convert('RGBA')
scale = im.size[0] / 500          # actual device-pixel ratio of the render
mask = Image.new('L', im.size, 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.size[0]-1, im.size[1]-1],
                                       radius=round(10*scale), fill=255)
im.putalpha(mask)
im.save('../../public/' + sys.argv[1])
print(f'  {sys.argv[1]}  {im.size[0]}x{im.size[1]}px')
PY
}

shoot .noicons.html   email-signature.png       # card only; icons live below it
shoot signature.html  email-signature-full.png  # all-in-one flat card (icons baked in)
