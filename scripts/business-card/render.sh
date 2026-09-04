#!/usr/bin/env bash
# Render both card faces at 300 DPI and assemble print-ready two-page PDFs.
#   -> public/business-card-front.png            (3.5 x 2in trim, 300 DPI)
#   -> public/business-card-back.png             (3.5 x 2in trim, 300 DPI)
#   -> public/business-card-print.pdf            (3.5 x 2in trim -- standard US card)
#   -> public/business-card-print-with-bleed.pdf (3.75 x 2.25in, 1/8in bleed all round)
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

$PY assemble.py
echo "done."
