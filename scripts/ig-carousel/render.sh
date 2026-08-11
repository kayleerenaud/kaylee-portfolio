#!/usr/bin/env bash
# Render the 3 carousel layouts to 1080x1350 (4:5) Instagram PNGs.
#   -> public/carousel/slide-a-cover.png
#   -> public/carousel/slide-b-concept.png
#   -> public/carousel/slide-c-quote.png
set -euo pipefail
cd "$(dirname "$0")"
W=540; H=675; PORT=8937
OUT=../../public/carousel
mkdir -p "$OUT"
python3 -m http.server "$PORT" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true; rm -f .raw.png' EXIT
sleep 1.2
shoot(){ # <html> <dest>
  screenshot "http://127.0.0.1:$PORT/$1" .raw.png "$W" "$H" 1800 >/dev/null
  cp .raw.png "$OUT/$2"
  echo "  $2  $(python3 -c "from PIL import Image;print('x'.join(map(str,Image.open('.raw.png').size)))")px"
}
shoot slide-a.html slide-a-cover.png
shoot slide-b.html slide-b-concept.png
shoot slide-c.html slide-c-quote.png
echo done.
