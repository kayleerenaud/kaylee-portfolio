#!/usr/bin/env python3
"""Generate Kaylee's COSTUME-SPECIFIC resume (public/kaylee-renaud-costume-resume.pdf).

A costume-shop-facing cut of the general resume: every costume credit carries
responsibility bullets (pulled verbatim from the CV), plus the three non-costume
jobs that show work history (Jean Doumanian Productions, Camp-of-the-Woods,
Chick-fil-A). Wording is reused verbatim from kaylee-renaud-resume.pdf and
scripts/build-cv-pdf.py -- nothing here is rewritten.

Matches the plain, ATS-friendly EB Garamond look of the general resume.
Re-run after editing CONTENT below:
    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-costume-resume-pdf.py
"""
import os, html
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def furl(rel): return 'file://' + os.path.join(ROOT, rel)

# ── CONTENT ───────────────────────────────────────────────────────────────────
NAME = "Kaylee Renaud"
TITLE = "Costume Designer, Filmmaker, Writer"
EMAIL = "kayleeerenaud@gmail.com"
PHONE = "(518)226-9586"

EDU_LEFT = ["New York University, Tisch School of the Arts",
            "BFA, Film &amp; Television, Expected May 2027",
            "Minor Focus: Costume Design and Dance"]
EDU_RIGHT = ["Additional Study:",
             "Developing the Dramatic Script — Florence, Italy",
             "Storytelling — Athens, Greece"]

# (title, role, meta, [bullets])
COSTUME = [
 ("Eurydice", "Costume Designer",
  "NYU Tisch Drama, Experimental Theater Wing | 2026 | Dir. Elia Monte-Brown",
  ["Led a costume team from research through construction to production on stage",
   "Budget and receipt tracking"]),
 ("As You Like It", "Costume Assistant",
  "NYU Classical Studio | 2026 | Dir. Daniel Spector",
  ["A low-budget, high-concept take on Shakespeare’s classic",
   "Assisted under Madison Barnett, mentored by Erin Black",
   "Technical drawings, research, fittings, swatching, and delegating to makers"]),
 ("Knights of the Old Republic, Ep. 2", "Costume Director",
  "The King’s Academy Studio 70 | 2026 | Dir. Austin Parenti",
  ["Costume design for original characters",
   "Delegated construction to domestic and international makers",
   "Budget and receipt tracking"]),
 ("Weightless", "Costume Designer",
  "NYU Intermediate Narrative | 2026 | Dir. Kevin Sherman",
  ["Costume design and sourcing for the short sci-fi film"]),
 ("Knights of the Old Republic, Ep. 1", "Costume Re-design &amp; Art Assistant",
  "The King’s Academy Studio 70 | 2025 | Dir. Austin Parenti",
  ["Costume re-design for the villain, Davik Kang",
   "Art assistant across costume and props"]),
 ("Costume Consultant", "",
  "2025",
  ["“Anya” — costume &amp; color consultant; five-time award-winning short by Adele Xu",
   "“Sing Me to Sleep” — costume consultant; festival nominee by Pamela Fuller",
   "“Yoko” — costume consultant; a short film by Josh Li"]),
 ("Like Mother", "Costume Designer &amp; Fabricator",
  "NYU | 2024 | Manhattan Film Festival Nominee | Dir. Ziyan Zheng",
  ["Costume design and construction for the short film",
   "Official Selection — Manhattan Film Festival &amp; Fusion Film Festival"]),
]

WARDROBE = [
 ("Wardrobe Intern", "New York Theater Ballet — New York, NY | 2024",
  ["Performed costume alterations and repairs for ballet productions",
   "Assisted with organization, packing, and maintenance of wardrobe inventory"]),
]

TRAINING = [
 ("Costume Techniques", "Construction, Dying &amp; Distressing | 2026",
  ["Permanent and temporary dying and distressing techniques",
   "Draping and pattern drafting",
   "Technical illustration and construction research"]),
 ("Costume Design Thesis", "Costume Design Student | 2025",
  ["Concept, research, paperwork, and designs for Peter and the Starcatcher by Rick Elice"]),
]

ADDITIONAL = [
 ("Development Intern", "Jean Doumanian Productions — New York, NY | 2026",
  ["Wrote script coverage and conducted research for current and prospective film projects",
   "Analyzed scripts for narrative structure, character development, and production potential"]),
 ("Video Director &amp; Marketing Assistant", "Camp-of-the-Woods — Speculator, NY | 2024",
  ["Directed video coverage for live productions and seminars",
   "Produced marketing photography and assisted with media production"]),
 ("Front of House", "Chick-fil-A — Albany &amp; New York, NY | 2025",
  ["Fast-paced, customer-forward environment with a focus on going the extra mile"]),
]

SKILLS = [
 ("Costume:", "Costume Design, Costume Construction, Technical Illustration, Fabric dyeing &amp; "
              "distressing techniques, draping and pattern drafting, set construction"),
 ("Software:", "Procreate, Final Draft, Adobe Premiere Pro, Lightroom, Pro Tools, Google Workspace, "
               "Claude integration"),
 ("Additional:", "Research &amp; script analysis, production coordination, budget and receipt tracking"),
]

REFS = [
 ("Erin Black", "Professor of Production &amp; Design, NYU", "eks4@nyu.edu"),
 ("Michael Huff", "Executive Assistant, Jean Doumanian Productions", "mhuff@jeandoumanian.com"),
 ("Michael Gray", "Operator, Chick-fil-A Central Ave", "+1 (256) 338-4429"),
]

# ── RENDER ────────────────────────────────────────────────────────────────────
def bullets(lines):
    return "".join(f"<li>{l}</li>" for l in lines)

def credit(title, role, meta, lines):
    r = f" <span class='role'>- {role}</span>" if role else ""
    return (f"<article class='entry'><p class='hd'><span class='ttl'>{title}</span>{r}"
            f" <span class='meta'>| {meta}</span></p><ul>{bullets(lines)}</ul></article>")

def job(role, where, lines):
    return (f"<article class='entry'><p class='hd'><span class='ttl'>{role}</span>"
            f"<span class='where'> | {where}</span></p><ul>{bullets(lines)}</ul></article>")

costume_html  = "".join(credit(*c) for c in COSTUME)
wardrobe_html = "".join(job(*j) for j in WARDROBE)
training_html = "".join(job(*t) for t in TRAINING)
addl_html     = "".join(job(*j) for j in ADDITIONAL)
skills_html   = "".join(f"<p class='skill'><b>{k}</b> {v}</p>" for k, v in SKILLS)
refs_html     = "".join(f"<p class='ref'><b>{n}</b> — {r} · {c}</p>" for n, r, c in REFS)
edu_l = "".join(f"<p>{x}</p>" for x in EDU_LEFT)
edu_r = "".join(f"<p>{x}</p>" for x in EDU_RIGHT)

DOC = f"""<!doctype html><html><head><meta charset='utf-8'><style>
@font-face {{ font-family:'EBG'; src:url('{furl("scripts/resume-assets/EBGaramond-VF.ttf")}');
  font-weight:400 800; font-style:normal; }}
@font-face {{ font-family:'EBG'; src:url('{furl("scripts/resume-assets/EBGaramond-Italic-VF.ttf")}');
  font-weight:400 800; font-style:italic; }}
@page {{ size: Letter; margin: 0.45in 0.62in 0.35in; }}
* {{ box-sizing:border-box; }}
html, body {{ margin:0; padding:0; color:#111; font-family:'EBG', Garamond, Georgia, serif;
  font-size:9.6pt; line-height:1.14; }}
.head {{ display:flex; justify-content:space-between; align-items:flex-start; }}
h1 {{ font-size:21pt; font-weight:400; margin:0; letter-spacing:.005em; }}
.title {{ margin:.1em 0 0; font-size:10.4pt; }}
.contact {{ text-align:right; font-size:9.6pt; padding-top:.3em; }}
.contact p {{ margin:0 0 .1em; }}
.contact a {{ color:#1155cc; }}
.edu {{ display:flex; gap:.95in; margin:.5em 0 .1em; font-size:9.7pt; }}
.edu p {{ margin:0 0 .02em; }}
h2 {{ font-size:10.8pt; font-weight:700; letter-spacing:.02em; text-transform:uppercase;
  margin:.5em 0 .16em; }}
.entry {{ margin:0 0 .16em; break-inside:avoid; }}
.hd {{ margin:0; }}
.ttl {{ font-weight:700; }}
.role, .where {{ font-weight:400; }}
.meta {{ font-size:9.1pt; font-style:italic; color:#333; }}
ul {{ margin:0; padding-left:1em; }}
li {{ margin:0; }}
.skill {{ margin:0 0 .04em; }}
.ref {{ margin:0 0 .04em; }}
h2 {{ break-after:avoid; }}
</style></head><body>
<div class='head'>
  <div><h1>{NAME}</h1><p class='title'>{TITLE}</p></div>
  <div class='contact'><p>email: <a href='mailto:{EMAIL}'>{EMAIL}</a></p><p>tel. {PHONE}</p></div>
</div>
<div class='edu'><div>{edu_l}</div><div>{edu_r}</div></div>

<h2>Costume Experience</h2>{costume_html}
<h2>Wardrobe Experience</h2>{wardrobe_html}
<h2>Costume Training</h2>{training_html}
<h2>Additional Experience</h2>{addl_html}
<h2>Skills</h2>{skills_html}
<h2>References</h2>{refs_html}
</body></html>"""

out = os.path.join(ROOT, 'public', 'kaylee-renaud-costume-resume.pdf')
doc = HTML(string=DOC, base_url=ROOT).render()
doc.write_pdf(out)
print(f"wrote {out}  ({os.path.getsize(out)//1024} KB, {len(doc.pages)} pages)")
