#!/usr/bin/env bash
# Render the story graphic to a 1080x1920 Instagram PNG -> public/ig-story-iso-sets.png
set -euo pipefail
cd "$(dirname "$0")"
W=540; H=960; PORT=8939
python3 -m http.server "$PORT" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true; rm -f .raw.png' EXIT
sleep 1.2
screenshot "http://127.0.0.1:$PORT/story-iso.html" .raw.png "$W" "$H" 1500 >/dev/null
cp .raw.png ../../public/ig-story-iso-sets.png
python3 -c "from PIL import Image;im=Image.open('.raw.png');print('  ig-story-iso-sets.png', 'x'.join(map(str,im.size)))"
echo done.
