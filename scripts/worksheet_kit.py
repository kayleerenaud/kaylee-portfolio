#!/usr/bin/env python3
"""Shared layout kit for the Kaylee Renaud printable worksheet family.

Every sheet in `public/planning/` is built from these primitives so a new sheet
comes out looking like a sibling rather than a stranger. The rules that decide
arguments live in `public/planning/worksheet-format-spec.md`:

  1. Ink is expensive, paper is cheap  — hairlines and small grey tints only.
  2. Every blank must be writable      — nothing under ~0.245in tall is a field.
  3. No half-empty pages               — content flows; pagination is tuned.

Usage:
    from worksheet_kit import *
    P = []
    P.append(masthead('Title', 'deck', ['meta line', ...]) + h2(1, 'SECTION') + rules(3))
    build(P, 'public/planning/my-sheet.pdf')
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def furl(rel):
    return 'file://' + os.path.join(ROOT, rel)


# ── core primitives (see spec §6) ─────────────────────────────────────────────
def rules(n=3, cls=''):
    """n blank ruled lines to write on. The default answer field."""
    return f"<div class='rules {cls}'>" + "".join("<div class='rl'></div>" for _ in range(n)) + "</div>"


def field(label, n=1, cls=''):
    return f"<div class='field {cls}'><span class='fl'>{label}</span>{rules(n)}</div>"


def inline(*labels):
    """Short labelled blanks side by side. For numbers and dates, never sentences."""
    cells = "".join(f"<div class='ib'><span class='fl'>{l}</span><span class='blank'></span></div>"
                    for l in labels)
    return f"<div class='inline'>{cells}</div>"


def table(cols, rows, widths=None, head_note='', cls='', rowlbls=None):
    """The workhorse. Explicit widths, uppercase headers, empty tds to write in.

    rowlbls: optional list of first-column labels; those rows get the #f4f2f0 tint.
    """
    widths = widths or [f"{100/len(cols):.4f}%"] * len(cols)
    ths = "".join(f"<th style='width:{w}'>{c}</th>" for c, w in zip(cols, widths))
    if rowlbls:
        body = "".join("<tr class='rowlbl'><td>" + lbl + "</td>"
                       + "".join("<td></td>" for _ in cols[1:]) + "</tr>" for lbl in rowlbls)
    else:
        body = "".join("<tr>" + "".join("<td></td>" for _ in cols) + "</tr>" for _ in range(rows))
    note = f"<p class='note'>{head_note}</p>" if head_note else ""
    c = f" class='{cls}'" if cls else ""
    return f"{note}<table{c}><thead><tr>{ths}</tr></thead><tbody>{body}</tbody></table>"


def checks(items, cols=2):
    """Checkbox list; each row ruled so an unchecked item still has a writing line."""
    lis = "".join(f"<li><span class='cb'></span>{i}</li>" for i in items)
    return f"<ul class='checks c{cols}'>{lis}</ul>"


def q(text):
    """A prompt question. Always immediately followed by rules()."""
    return f"<p class='q'>{text}</p>"


def box(title, inner, cls=''):
    return f"<section class='box {cls}'><h3>{title}</h3>{inner}</section>"


def h2(n, title, sub=''):
    s = f"<span class='sub'>{sub}</span>" if sub else ""
    return f"<h2><span class='num'>{n}</span>{title}{s}</h2>"


def h3(title):
    return f"<h3>{title}</h3>"


def note(text):
    return f"<p class='note'>{text}</p>"


def split(*cols, cls=''):
    inner = "".join(f"<div>{c}</div>" for c in cols)
    return f"<div class='split {cls}'>{inner}</div>"


def keep(inner):
    return f"<div class='keep'>{inner}</div>"


def foot(text):
    return f"<p class='foot'>{text}</p>"


# ── extensions added for the 2026 sheets (spec §6b) ───────────────────────────
def pick(items, other='', label=''):
    """Wrapped inline checkbox chips — a compact 'tick all that apply' row.

    Cheaper in space than checks() when there are many short options and the
    reader only ticks two or three. Always give it an `other` writable blank so
    the list stays descriptive, never prescriptive.
    """
    chips = "".join(f"<span class='chip'><span class='cb'></span>{i}</span>" for i in items)
    lbl = f"<span class='fl'>{label}</span>" if label else ""
    oth = (f"<div class='ib wide'><span class='fl'>{other}</span>"
           f"<span class='blank'></span></div>") if other else ""
    return f"<div class='pickwrap'>{lbl}<div class='pick'>{chips}</div>{oth}</div>"


def swatches(n=6, caption='', h='.55in'):
    """Empty squares to fill in with pencil, each with a ruled caption line under.

    Used for palettes. The box is a hairline outline, never a fill — see rule 1.
    """
    cells = "".join(
        f"<div class='sw'><div class='swbox' style='height:{h}'></div>"
        f"<div class='swcap'></div></div>" for _ in range(n))
    cap = f"<p class='note'>{caption}</p>" if caption else ""
    return f"{cap}<div class='swrow'>{cells}</div>"


def sketch(h='1.35in', label=''):
    """A bordered empty box for drawing. Hairline border, no fill."""
    lbl = f"<span class='fl'>{label}</span>" if label else ""
    return f"<div class='sketchwrap'>{lbl}<div class='sketch' style='height:{h}'></div></div>"


def strip(n=10, label='', ticks=None, h='.42in'):
    """A segmented horizontal bar — mark where something happened over a runtime.

    n equal cells with hairline dividers; `ticks` labels the cells underneath.
    """
    cells = "".join("<div class='stcell'></div>" for _ in range(n))
    tk = ""
    if ticks:
        tk = "<div class='sttick'>" + "".join(f"<span>{t}</span>" for t in ticks) + "</div>"
    lbl = f"<span class='fl'>{label}</span>" if label else ""
    return f"<div class='stripwrap'>{lbl}<div class='strip' style='height:{h}'>{cells}</div>{tk}</div>"


def masthead(title, dek, meta):
    m = "".join(f"<p>{x}</p>" for x in meta)
    return f"""
<div class='masthead'>
  <div>
    <h1>{title}</h1>
    <p class='dek'>{dek}</p>
  </div>
  <div class='mast-meta'>{m}</div>
</div>"""


# ── the house stylesheet ──────────────────────────────────────────────────────
def css(extra=''):
    return f"""
@font-face {{ font-family:'EBG'; src:url('{furl("scripts/resume-assets/EBGaramond-VF.ttf")}');
  font-weight:400 800; font-style:normal; }}
@font-face {{ font-family:'EBG'; src:url('{furl("scripts/resume-assets/EBGaramond-Italic-VF.ttf")}');
  font-weight:400 800; font-style:italic; }}
@font-face {{ font-family:'KScript'; src:url('{furl("public/fonts/KayleeScript-Regular.ttf")}'); }}
@page {{ size: Letter; margin: 0.42in 0.5in 0.38in;
  @bottom-right {{ content: counter(page) ' / ' counter(pages);
    font-family:'EBG', serif; font-size:6.6pt; color:#8a8a8a; }} }}
* {{ box-sizing:border-box; }}
html, body {{ margin:0; padding:0; color:#111; font-family:'EBG', Garamond, serif;
  font-size:8.1pt; line-height:1.22; }}

/* masthead */
.masthead {{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:1.6pt solid #111; padding-bottom:.3em; margin-bottom:.55em; }}
h1 {{ font-family:'KScript', cursive; font-size:26pt; font-weight:400; margin:0; line-height:.95; }}
.dek {{ margin:.3em 0 0; font-style:italic; font-size:8.4pt; color:#333; }}
.mast-meta {{ text-align:right; font-size:7.8pt; }}
.mast-meta p {{ margin:0 0 .22em; }}

/* section headers */
h2 {{ font-size:8.6pt; font-weight:700; letter-spacing:.13em; text-transform:uppercase;
  margin:.85em 0 .3em; padding-bottom:.14em; border-bottom:.6pt solid #999;
  break-after:avoid; }}
h2 .num {{ display:inline-block; min-width:1.7em; color:#777; font-weight:400; }}
h2 .sub {{ display:block; margin-top:.35em; font-weight:400; font-size:7.5pt; letter-spacing:0;
  text-transform:none; font-style:italic; color:#555; }}
h3 {{ font-size:8.2pt; font-weight:700; margin:.5em 0 .28em; break-after:avoid; }}
.note {{ margin:.15em 0 .4em; font-size:7.4pt; font-style:italic; color:#444; }}
.q {{ margin:.5em 0 .18em; font-size:7.9pt; color:#222; }}

/* ruled writing lines */
.rules {{ margin:.1em 0 .3em; }}
.rl {{ height:.245in; border-bottom:.5pt solid #b9b9b9; }}
.field {{ margin-bottom:.3em; }}
.fl {{ font-size:7.2pt; letter-spacing:.06em; text-transform:uppercase; color:#666; }}
.inline {{ display:flex; gap:.22in; margin:.3em 0 .1em; }}
.ib {{ flex:1; }}
.ib .blank {{ display:block; height:.245in; border-bottom:.5pt solid #b9b9b9; }}

/* tables */
table {{ width:100%; border-collapse:collapse; margin:.15em 0 .35em; }}
th {{ font-size:7.1pt; font-weight:700; letter-spacing:.05em; text-transform:uppercase;
  text-align:left; color:#333; border-bottom:.9pt solid #555; padding:.14em .28em; }}
td {{ height:.245in; border-bottom:.5pt solid #c2c2c2; padding:.1em .28em; }}
tr.rowlbl td:first-child {{ font-size:7.5pt; color:#333; background:#f4f2f0; }}
table.lanes td, table.reverse td, table.audit td, table.tall td {{ height:.29in; }}
table.taller td {{ height:.36in; }}
table.week td {{ height:.42in; border-right:.5pt solid #d8d8d8; }}
table.vgrid td, table.vgrid th {{ border-right:.5pt solid #d8d8d8; }}
table.vgrid td:last-child, table.vgrid th:last-child {{ border-right:none; }}
table.week td:first-child {{ font-size:7.2pt; color:#444; background:#f4f2f0; }}

/* checkbox lists */
.checks {{ list-style:none; margin:.15em 0 .3em; padding:0; }}
.checks li {{ display:flex; align-items:center; gap:.12in; height:.27in;
  border-bottom:.5pt solid #b9b9b9; }}
.cb {{ display:inline-block; flex:0 0 .13in; width:.13in; height:.13in;
  border:.8pt solid #777; box-sizing:border-box; }}

/* pick chips */
.pickwrap {{ margin:.2em 0 .3em; }}
.pick {{ display:flex; flex-wrap:wrap; gap:.05in .2in; margin:.16em 0 .1em; }}
.chip {{ display:flex; align-items:center; gap:.07in; font-size:7.6pt; color:#222;
  white-space:nowrap; }}
.chip .cb {{ flex:0 0 .11in; width:.11in; height:.11in; align-self:center; }}
.ib.wide {{ flex:none; width:100%; margin-top:.1em; }}

/* palette swatches */
.swrow {{ display:flex; gap:.16in; margin:.1em 0 .35em; }}
.sw {{ flex:1; }}
.swbox {{ border:.6pt solid #b9b9b9; }}
.swcap {{ height:.245in; border-bottom:.5pt solid #b9b9b9; }}

/* sketch box */
.sketchwrap {{ margin:.15em 0 .35em; }}
.sketch {{ border:.6pt solid #b9b9b9; margin-top:.12em; }}

/* runtime strip */
.stripwrap {{ margin:.2em 0 .4em; }}
.strip {{ display:flex; border:.6pt solid #b9b9b9; margin-top:.12em; }}
.stcell {{ flex:1; border-right:.5pt solid #d8d8d8; }}
.stcell:last-child {{ border-right:none; }}
.sttick {{ display:flex; margin-top:.1em; }}
.sttick span {{ flex:1; font-size:6.4pt; color:#8a8a8a; letter-spacing:.04em; }}

/* two-up blocks */
.split {{ display:flex; gap:.3in; }}
.split > div {{ flex:1; }}
.split.money > div:first-child {{ flex:.9; }}
.split.wide-left > div:first-child {{ flex:1.5; }}
.split.wide-right > div:last-child {{ flex:1.5; }}
.rung {{ break-inside:avoid; }}
table.lanes, table.week, table.reverse, table.rhythms, table.matrix {{ break-inside:avoid; }}
thead {{ display:table-header-group; }}   /* repeat headers when a table splits */
.split, .keep, .checks, .swrow, .stripwrap, .sketchwrap {{ break-inside:avoid; }}
.foot {{ margin-top:.5em; font-size:7pt; font-style:italic; color:#777; text-align:center; }}
{extra}
"""


def build(pages, out_rel, extra_css=''):
    """Render a list of page-HTML strings to a PDF under ROOT."""
    from weasyprint import HTML
    body = "".join(f"<div class='page'>{p}</div>" for p in pages)
    doc_html = (f"<!doctype html><html><head><meta charset='utf-8'>"
                f"<style>{css(extra_css)}</style></head><body>{body}</body></html>")
    out = os.path.join(ROOT, out_rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    doc = HTML(string=doc_html, base_url=ROOT).render()
    doc.write_pdf(out)
    print(f"wrote {out_rel}  ({os.path.getsize(out)//1024} KB, {len(doc.pages)} pages)")
    return out


def renumber(src_path):
    """Renumber h2(n, ...) in document order — never renumber by hand (spec §8)."""
    import re
    n = iter(range(1, 99))
    src = open(src_path).read()
    src = re.sub(r"h2\(\d+, ", lambda m: f"h2({next(n)}, ", src)
    open(src_path, 'w').write(src)
