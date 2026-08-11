# Instagram carousel template — Kaylee Renaud

Three reusable 4:5 (1080×1350) slide layouts in the brand system
(charcoal + rose, Spectral ExtraBold headlines, KayleeScript accents).

| File | Layout | Use for |
|------|--------|---------|
| `slide-a.html` | **A · Cover** | Slide 1 — big title + hook + swipe cue |
| `slide-b.html` | **B · Numbered concept** | Middle slides — one per structure (duplicate & edit) |
| `slide-c.html` | **C · Quote / closer** | Last slide — pull-quote + follow CTA |

## Edit
Open the `.html` files — each has a comment marking what to change.
- Cover: `.kicker`, `.headline`, `.flourish` (the handwritten line), `.sub`
- Concept: `.num`, `.name`, `.translit`, `.lead`, the four `.beat` rows
- Quote: `.q` (wrap a word in `<span class="em">` for the rose handwritten accent), `.attrib`

To make more concept slides, copy `slide-b.html` to `slide-b2.html`, edit, and add a
`shoot` line in `render.sh`.

## Render
```
bash render.sh
```
Outputs 1080×1350 PNGs to `../../public/carousel/`. Post them straight to Instagram,
or upload as backgrounds in Canva if you want to tweak there.

Brand: bg `#14110f` · rose `#d98a9e` / `#eeaabb` · ink `#f1ece4` · soft `#b0a89b`.
Fonts: Spectral (Regular/Medium/Bold/ExtraBold) + KayleeScript.
