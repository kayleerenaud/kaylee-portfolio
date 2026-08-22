#!/usr/bin/env python3
"""Shared one-page resume layout (EB Garamond, right-aligned year column).

Used by build-costume-resume-pdf.py and build-film-resume-pdf.py so the two
tailored resumes stay visually identical and only their content differs.

Entry shape used everywhere: (title, role, org, year, [bullets])
  **Title** · Role                                                        YEAR
  Org · Director / festival note   (italic; omitted when empty)
  • bullets
"""
import os
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def furl(rel): return 'file://' + os.path.join(ROOT, rel)

NAME = "Kaylee Renaud"
EMAIL = "kayleeerenaud@gmail.com"
PHONE = "(518)226-9586"

REFS = [
 ("Erin Black", "Professor of Production &amp; Design, NYU", "eks4@nyu.edu"),
 ("Michael Huff", "Executive Assistant, Jean Doumanian Productions", "mhuff@jeandoumanian.com"),
 ("Michael Gray", "Operator, Chick-fil-A Central Ave", "+1 (256) 338-4429"),
]


def entry(title, role, org, year, lines):
    r = f"<span class='role'> · {role}</span>" if role else ""
    o = f"<p class='org'>{org}</p>" if org else ""
    li = "".join(f"<li>{l}</li>" for l in lines)
    return (f"<article class='entry'>"
            f"<div class='hd'><p class='ttl'>{title}{r}</p><p class='yr'>{year}</p></div>"
            f"{o}<ul>{li}</ul></article>")


def section(label, items):
    return f"<h2>{label}</h2>" + "".join(entry(*i) for i in items)


CSS = """
@font-face { font-family:'EBG'; src:url('%(reg)s'); font-weight:400 800; font-style:normal; }
@font-face { font-family:'EBG'; src:url('%(ital)s'); font-weight:400 800; font-style:italic; }
@page { size: Letter; margin: %(page_margin)s; }
* { box-sizing:border-box; }
html, body { margin:0; padding:0; color:#14110f;
  font-family:'EBG', Garamond, Georgia, serif; font-size:%(fs)spt; line-height:%(lh)s; }

/* header */
.head { display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:1.1pt solid #14110f; padding-bottom:.2em; }
h1 { font-size:21.5pt; font-weight:500; margin:0; line-height:1; }
.subtitle { margin:.24em 0 0; font-size:9pt; letter-spacing:.11em;
  text-transform:uppercase; color:#4a423c; }
.contact { text-align:right; font-size:9.3pt; color:#4a423c; }
.contact p { margin:0 0 .12em; }
.contact a { color:#4a423c; text-decoration:none; }

/* education */
.edu { display:flex; margin:.4em 0 0; font-size:9.2pt; }
.edu > div { width:50%%; padding-right:.35in; }
.edu p { margin:0 0 .04em; }

/* sections */
h2 { font-size:9.2pt; font-weight:700; letter-spacing:.14em; text-transform:uppercase;
  color:#14110f; margin:%(h2_margin)s; padding-bottom:.12em;
  border-bottom:.5pt solid #b9afa6; break-after:avoid; }

/* entries */
.entry { margin:0 0 %(entry_gap)s; break-inside:avoid; }
.entry:last-child { margin-bottom:0; }
.hd { display:flex; justify-content:space-between; align-items:baseline; gap:.6em; }
.ttl { margin:0; font-weight:700; }
.role { font-weight:400; }
.yr { margin:0; white-space:nowrap; font-size:9pt; letter-spacing:.06em; color:#6b615a; }
.org { margin:.02em 0 0; font-style:italic; font-size:9.2pt; color:#4a423c; }
ul { margin:.05em 0 0; padding-left:.92em; }
li { margin:0 0 .02em; padding-left:.06em; }
li::marker { color:#8a7f76; }

/* skills + references */
.skill { display:flex; gap:.1in; margin:0 0 .1em; }
.skill .k { flex:0 0 %(skill_key)s; font-weight:600; font-style:italic; font-size:9.2pt;
  letter-spacing:.01em; }
.skill .v { flex:1; }
.refs { display:flex; gap:.28in; break-inside:avoid; }
.refs .ref { width:33.33%%; }
.rn { margin:0; font-weight:700; }
.rr { margin:.01em 0 0; font-style:italic; font-size:8.9pt; color:#4a423c; }
.rc { margin:.02em 0 0; font-size:9pt; color:#4a423c; }
"""


def build(out_name, title, edu_left, edu_right, sections, skills, website=None,
          fs=9.2, lh=1.1, entry_gap=".14em", h2_margin=".44em 0 .16em",
          page_margin="0.42in 0.66in 0.3in", skill_key=".74in"):
    """sections: list of (label, [entries]); skills: list of (label, value)."""
    css = CSS % dict(reg=furl("scripts/resume-assets/EBGaramond-VF.ttf"),
                     ital=furl("scripts/resume-assets/EBGaramond-Italic-VF.ttf"),
                     fs=fs, lh=lh, entry_gap=entry_gap, h2_margin=h2_margin,
                     page_margin=page_margin, skill_key=skill_key)
    body = "".join(section(lbl, items) for lbl, items in sections)
    skills_html = "".join(
        f"<p class='skill'><span class='k'>{k}</span><span class='v'>{v}</span></p>"
        for k, v in skills)
    refs_html = "".join(
        f"<div class='ref'><p class='rn'>{n}</p><p class='rr'>{r}</p><p class='rc'>{c}</p></div>"
        for n, r, c in REFS)
    site = f"<p><a href='https://{website}'>{website}</a></p>" if website else ""
    edu_l = "".join(f"<p>{x}</p>" for x in edu_left)
    edu_r = "".join(f"<p>{x}</p>" for x in edu_right)

    doc_html = f"""<!doctype html><html><head><meta charset='utf-8'><style>{css}</style>
</head><body>
<div class='head'>
  <div><h1>{NAME}</h1><p class='subtitle'>{title}</p></div>
  <div class='contact'><p><a href='mailto:{EMAIL}'>{EMAIL}</a></p><p>{PHONE}</p>{site}</div>
</div>
<div class='edu'><div>{edu_l}</div><div>{edu_r}</div></div>
{body}
<h2>Skills</h2>{skills_html}
<h2>References</h2><div class='refs'>{refs_html}</div>
</body></html>"""

    out = os.path.join(ROOT, 'public', out_name)
    doc = HTML(string=doc_html, base_url=ROOT).render()
    doc.write_pdf(out)
    print(f"wrote {out}  ({os.path.getsize(out)//1024} KB, {len(doc.pages)} pages)")
    return len(doc.pages)
