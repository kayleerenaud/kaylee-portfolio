#!/usr/bin/env bash
# Render both card faces to 300 DPI PNGs and a print-ready two-page PDF.
#   -> public/business-card-front.png
#   -> public/business-card-back.png
#   -> public/business-card-print.pdf   (3.75 x 2.25in each page, with bleed)
set -euo pipefail
cd "$(dirname "$0")"

W=563; H=338; PORT=8934
PY=python3

python3 -m http.server "$PORT" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true; rm -f .raw.png' EXIT
sleep 1.2

shoot () {  # <html> <dest.png>
  screenshot "http://127.0.0.1:$PORT/$1" .raw.png "$W" "$H" 1800 >/dev/null
  cp .raw.png "../../public/$2"
  echo "  $2  $($PY -c "from PIL import Image;print('x'.join(map(str,Image.open('.raw.png').size)))")px"
}

shoot front.html business-card-front.png
shoot back.html  business-card-back.png

# --- assemble the print PDF (front page 1, back page 2) ----------------------
$PY - <<'PY'
from PIL import Image
front = Image.open('../../public/business-card-front.png').convert('RGB')
back  = Image.open('../../public/business-card-back.png').convert('RGB')
# 3.75 x 2.25in card; DPI = pixel_width / 3.75
dpi = round(front.size[0] / 3.75)
front.save('../../public/business-card-print.pdf', 'PDF', resolution=dpi,
           save_all=True, append_images=[back])
print(f'  business-card-print.pdf  ({dpi} DPI, 2 pages)')
PY
echo "done."
