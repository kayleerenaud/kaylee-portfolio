#!/usr/bin/env bash
# Render the carousel slides to 1080x1350 (4:5) Instagram PNGs -> public/carousel/
set -euo pipefail
cd "$(dirname "$0")"
W=540; H=675; PORT=8937
OUT=../../public/carousel
mkdir -p "$OUT"
rm -f "$OUT"/slide-*.png       # clear old naming so the folder is the current post
python3 -m http.server "$PORT" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true; rm -f .raw.png' EXIT
sleep 1.2
shoot(){ # <html> <dest>
  screenshot "http://127.0.0.1:$PORT/$1" .raw.png "$W" "$H" 1800 >/dev/null
  cp .raw.png "$OUT/$2"
  echo "  $2  $(python3 -c "from PIL import Image;print('x'.join(map(str,Image.open('.raw.png').size)))")px"
}
shoot slide-01-cover.html       slide-01-cover.png
shoot slide-02-daisychain.html  slide-02-daisychain.png
shoot slide-03-sliceoflife.html slide-03-sliceoflife.png
shoot slide-04-mastery.html     slide-04-mastery.png
shoot slide-05-takeaway.html    slide-05-takeaway.png
echo done.
