#!/usr/bin/env bash
# Render the email signature card to a retina PNG with transparent rounded corners.
#   scripts/email-signature/render.sh  ->  public/email-signature.png
# (headless Chromium renders at DPR 2, so the output is 2x the CSS size)
set -euo pipefail
cd "$(dirname "$0")"

W=500; H=168; PORT=8931

python3 -m http.server "$PORT" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true' EXIT
sleep 1.5

screenshot "http://127.0.0.1:$PORT/signature.html" .raw.png "$W" "$H" 1500

python3 - <<'PY'
from PIL import Image, ImageDraw
im = Image.open('.raw.png').convert('RGBA')
scale = im.size[0] / 500          # actual device-pixel ratio of the render
mask = Image.new('L', im.size, 0)
ImageDraw.Draw(mask).rounded_rectangle([0, 0, im.size[0]-1, im.size[1]-1],
                                       radius=round(10*scale), fill=255)
im.putalpha(mask)
im.save('../../public/email-signature.png')
print('wrote public/email-signature.png', im.size)
PY

rm -f .raw.png
