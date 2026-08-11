#!/usr/bin/env bash
# Render Post 2 (non-western structures) to 1080x1350 PNGs -> public/carousel-2/
set -euo pipefail
cd "$(dirname "$0")"
W=540; H=675; PORT=8938
OUT=../../public/carousel-2
mkdir -p "$OUT"
rm -f "$OUT"/p2-*.png
python3 -m http.server "$PORT" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true; rm -f .raw.png' EXIT
sleep 1.2
shoot(){ # <html> <dest>
  screenshot "http://127.0.0.1:$PORT/$1" .raw.png "$W" "$H" 1800 >/dev/null
  cp .raw.png "$OUT/$2"
  echo "  $2  $(python3 -c "from PIL import Image;print('x'.join(map(str,Image.open('.raw.png').size)))")px"
}
shoot p2-01-cover.html         p2-01-cover.png
shoot p2-02-kishotenketsu.html p2-02-kishotenketsu.png
shoot p2-03-rashomon.html      p2-03-rashomon.png
shoot p2-04-johakyu.html       p2-04-johakyu.png
shoot p2-05-takeaway.html      p2-05-takeaway.png
echo done.
