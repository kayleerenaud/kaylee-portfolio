# Instagram carousel — Kaylee Renaud

**Post 1: "You don't need conflict to tell your story"** — 5 slides, 1080×1350 (4:5),
brand system (charcoal + rose, Spectral ExtraBold headlines, KayleeScript accents).

| File | Slide | Layout |
|------|-------|--------|
| `slide-01-cover.html` | Cover / hook | A · Cover |
| `slide-02-daisychain.html` | Daisy Chain | B · Structure + examples |
| `slide-03-sliceoflife.html` | Slice of Life | B · Structure + examples |
| `slide-04-mastery.html` | Mastery Narrative | B · Structure + examples |
| `slide-05-takeaway.html` | Takeaway / CTA | C · Quote / closer |

Held for **Post 2 (non-western structures)**: Kishōtenketsu, Rashomon, Jo-ha-kyū.
Held as spare conflict-less options: Bridge Narrative, LIST, Ergodic, Epistolary/Found.

## Editing the reusable layouts
Each `.html` has a comment marking what to change.
- **Structure slide** (copy `slide-02` as a base): `.num`, `.name`, `.tag` (handwritten
  line), `.def`, and the three `.exrow` examples (`extag` = FILM / BOOK / POETRY; add
  class `alt` for the outlined book/poetry tag). Wrap a word in `<span class="hot">` for rose.
- **Cover**: `.headline` (wrap a word in `<span class="em">` for rose), `.flourish`, `.sub`.
- **Quote**: `.q` (wrap a word in `<span class="em">` for the handwritten rose accent),
  `.note`, `.teaser`.

## Render
```
bash render.sh          # -> ../../public/carousel/slide-0X-*.png
```
Post the PNGs straight to Instagram, or upload as backgrounds in Canva to tweak.

Brand: bg `#14110f` · rose `#d98a9e` / `#eeaabb` · ink `#f1ece4` · soft `#b0a89b`.
Fonts: Spectral (Regular/Medium/Bold/ExtraBold) + KayleeScript.
