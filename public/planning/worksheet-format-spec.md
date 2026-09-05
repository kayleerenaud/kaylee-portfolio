# Format spec — Kaylee Renaud printable planning worksheet

A handoff sheet for another agent. It describes **how the worksheet is formatted**, not what it
says, so a new sheet in the same family (habit tracker, packing list, shot-list planner, budget
sheet) comes out looking like a sibling rather than a stranger.

Reference artefact: `public/planning/career-planning-worksheet.pdf` (8 pp.)
Build script: `scripts/build-planning-worksheet.py`

---

## 1. Design brief in one paragraph

A dense, small-print, **black-on-white worksheet meant to be printed on a cheap printer and
written on by hand**. It maximises prompts-per-page without becoming unusable: every blank is a
real ruled line at handwriting height, and no element uses a large ink area. It is a working
document, not a keepsake — the person filling it in should feel free to cross things out.

Three rules that decide most arguments:

1. **Ink is expensive, paper is cheap.** No dark fills, no reversed type, no full-bleed colour.
   Hairlines and small grey tints only.
2. **Every blank must be writable.** If a line is under ~0.24in tall, it is decoration, not a field.
3. **No half-empty pages.** Content flows continuously; pagination is tuned until every page is full.

---

## 2. Page setup

| Property | Value |
|---|---|
| Page size | US Letter (8.5 × 11in) |
| Margins | `0.42in` top · `0.5in` left/right · `0.38in` bottom |
| Page number | Bottom-right, `counter(page) ' / ' counter(pages)`, 6.6pt, `#8a8a8a` |
| Orientation | Portrait |
| Colour | Black on white only; no bleed, no background fills beyond the row tint below |

```css
@page { size: Letter; margin: 0.42in 0.5in 0.38in;
  @bottom-right { content: counter(page) ' / ' counter(pages);
    font-family:'EBG', serif; font-size:6.6pt; color:#8a8a8a; } }
```

---

## 3. Typography

One serif for everything, one script for the title only. Small sizes are deliberate — this is a
"lots of content" sheet.

| Element | Font | Size | Style |
|---|---|---|---|
| Title (`h1`) | KayleeScript | 26pt | weight 400, line-height .95 |
| Deck under title (`.dek`) | EB Garamond | 8.4pt | italic, `#333` |
| Masthead meta (`.mast-meta`) | EB Garamond | 7.8pt | right-aligned |
| Section head (`h2`) | EB Garamond | 8.6pt | bold, UPPERCASE, letter-spacing `.13em` |
| Section number (`h2 .num`) | EB Garamond | inherit | weight 400, `#777`, `min-width:1.7em` |
| Section subtitle (`h2 .sub`) | EB Garamond | 7.5pt | italic, `#555`, own line |
| Sub-head (`h3`) | EB Garamond | 8.2pt | bold |
| Explanatory note (`.note`) | EB Garamond | 7.4pt | italic, `#444` |
| Prompt / question (`.q`) | EB Garamond | 7.9pt | roman, `#222` |
| Body default | EB Garamond | 8.1pt | line-height 1.22, `#111` |
| Table header (`th`) | EB Garamond | 7.1pt | bold, UPPERCASE, letter-spacing `.05em`, `#333` |
| Field label (`.fl`) | EB Garamond | 7.2pt | UPPERCASE, letter-spacing `.06em`, `#666` |
| Footer line (`.foot`) | EB Garamond | 7pt | italic, centred, `#777` |

> **`min-width:1.7em` on the section number is load-bearing.** At `1.15em` the two-digit numbers
> (10, 14, 18) collided with their titles and rendered as `10THE WEEK I WANT`. Any redesign that
> touches the number must be re-checked at section 10+.

Fonts are loaded from disk by `file://` URL — EB Garamond variable roman + variable italic, and
KayleeScript for the title. Declare the variable fonts with `font-weight:400 800`.

---

## 4. The ink palette

Greyscale only. Each value has a job; do not add new greys casually.

| Hex | Used for |
|---|---|
| `#111` | Body text, masthead rule (1.6pt) |
| `#222` / `#333` / `#444` / `#555` | Prompts, table headers, notes, subtitles — descending emphasis |
| `#666` / `#777` | Field labels, section numbers, checkbox borders, footer |
| `#8a8a8a` | Page numbers |
| `#999` | Section-head underline (.6pt) |
| `#b9b9b9` | **Writing lines** (.5pt) — the line the pen sits on |
| `#c2c2c2` | Table cell dividers (.5pt) |
| `#d8d8d8` | Vertical grid lines in the week table (.5pt) |
| `#f4f2f0` | Row-label tint — the only fill in the document |

---

## 5. Writing-space metrics

These are the numbers that make it usable rather than pretty. Do not shrink them to win space —
cut content instead.

| Element | Height | Rule |
|---|---|---|
| Ruled writing line (`.rl`) | `0.245in` | `.5pt solid #b9b9b9` bottom |
| Standard table cell (`td`) | `0.245in` | `.5pt solid #c2c2c2` bottom |
| Labelled-row table (`.lanes`, `.reverse`, `.audit`) | `0.29in` | taller because answers are phrases |
| Week grid cell (`.week`) | `0.42in` | plus `.5pt` right border for columns |
| Checkbox row (`.checks li`) | `0.27in` | ruled bottom, box `0.13in` sq / `.8pt` border |
| Inline blank (`.ib .blank`) | `0.245in` | label above, rule below |

---

## 6. Component vocabulary

Build pages from these seven primitives. Python helpers in the script emit the HTML; the CSS is
what matters if you rebuild in another tool.

**`rules(n)`** — *n* blank ruled lines. The default answer field.
```html
<div class="rules"><div class="rl"></div><div class="rl"></div></div>
```

**`q(text)`** — a prompt question. Always immediately followed by `rules()`.

**`inline(a, b, c)`** — short labelled blanks side by side, equal width, `.22in` gap. For numbers
and dates (totals, deadlines), never for sentences.
```html
<div class="inline"><div class="ib"><span class="fl">TOTAL IN</span><span class="blank"></span></div>…</div>
```

**`table(cols, rows, widths)`** — the workhorse. Explicit percentage widths, uppercase headers,
empty `<td>`s to write in. Give a table a `tr.rowlbl` first column when the rows are fixed prompts
(that column gets the `#f4f2f0` tint and 7.5pt type).

**`checks(items)`** — checkbox list; each row ruled so an unchecked item still has a writing line.

**`split`** — two equal columns, `.3in` gutter, for paired prompts (fear / what's true, what I
need / where it comes from). One variant, `.split.money`, weights the first column `flex:.9` where
the right side carries a table. Never nest a `split` inside a `split`.

**`h2(n, title, sub)`** — numbered section head with optional italic subtitle. Numbers run in
**document order**; renumber programmatically, never by hand (see §8).

---

## 7. Pagination rules

The single most important formatting decision: **do not force page breaks per section.** An early
draft gave each thematic group its own page and produced 8 pages where 3 were two-thirds empty.
Content now flows continuously and the page count is whatever it is.

```css
thead { display: table-header-group; }        /* headers repeat when a table splits */
h2    { break-after: avoid; }                 /* never strand a head at a page foot */
h3    { break-after: avoid; }
.rung, .split, .keep, .checks { break-inside: avoid; }
table.lanes, table.week, table.reverse, table.rhythms { break-inside: avoid; }
```

The distinction that matters:

- **Long, uniform log tables** (pipeline, materials audit, people, monthly check-in) **may split**
  across pages. A repeated header makes the continuation legible.
- **Matrix tables read as a unit** (three-lane comparison, week grid, reverse-plan, faith rhythms)
  **must not split** — half a matrix is unreadable. Wrap any other must-stay-whole block in
  `<div class="keep">`.
- If keeping a table whole strands a single orphan row on the next page, either add rows so it
  fills or wrap it in `.keep` so it moves wholesale. Both were used here.

---

## 8. Section numbering

Section numbers are passed as literals to `h2()`, so inserting a section mid-document breaks the
sequence. Renumber in document order with one regex pass over the source **after** any insertion:

```python
import re
n = iter(range(1, 99))
src = re.sub(r"h2\(\d+, '", lambda m: f"h2({next(n)}, '", src)
```

Two hand-renumbering attempts produced duplicates (two §9s, two §10s) before this was automated.

---

## 9. Toolchain

| Step | Tool |
|---|---|
| Layout | HTML + CSS |
| PDF render | **WeasyPrint 69** (`HTML(string=…).render()` → `write_pdf()`) |
| Fonts | Local `.ttf` referenced by absolute `file://` URL |
| Visual check | **pypdfium2** → PNG per page → look at every page |

```bash
PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
  python3 scripts/build-planning-worksheet.py
```

Content lives in Python data structures at the top of the script, layout helpers and the CSS block
below — so an edit to wording never risks the layout.

---

## 10. Verification checklist

Render **every page to PNG and actually look at it** before shipping. Automated size checks do not
catch these:

- [ ] No page more than ~15% empty at the foot (except the last, where slack is fine)
- [ ] No section head stranded at the bottom of a page
- [ ] No orphaned single table row on a following page
- [ ] Two-digit section numbers clear of their titles
- [ ] Matrix tables intact on one page
- [ ] Every blank at least 0.245in tall
- [ ] Prints legibly in greyscale draft mode — no element relies on colour

---

## 11. Voice conventions (formatting-adjacent, worth keeping)

- Prompts are written **first-person-as-self**: "What am I avoiding, and why?" — not "Identify
  avoidance patterns."
- Every section head carries an italic subtitle that says *why the section exists*
  ("Not the ones I wish I had", "The worksheet is worthless without this part").
- Notes explain the *method* before the table, so the sheet teaches while it collects.
- Prefer a specific prompt over a generic label: "What would make me decide NOT to go?" beats
  "Considerations".
- Tables end with a decision column — *keep · cut · shrink · grow*, *grow / hold / pause* — so the
  sheet forces a call rather than an inventory.

---

*Reference build: `scripts/build-planning-worksheet.py` · US Letter · EB Garamond · WeasyPrint 69*
