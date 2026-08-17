#!/usr/bin/env python3
"""Generate Kaylee's COSTUME-SPECIFIC resume (public/kaylee-renaud-costume-resume.pdf).

A costume-shop-facing cut of the general resume: every costume credit carries
responsibility bullets (pulled verbatim from the CV), plus the three non-costume
jobs that show work history (Jean Doumanian Productions, Camp-of-the-Woods,
Chick-fil-A). Wording is reused verbatim from kaylee-renaud-resume.pdf and
scripts/build-cv-pdf.py -- nothing here is rewritten.

Layout: one page, EB Garamond, a single entry format throughout --
  **Title** — Role                                                        YEAR
  Company · Director / festival note   (italic)
  • responsibility bullets

Re-run after editing CONTENT below:
    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-costume-resume-pdf.py
"""
import os
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def furl(rel): return 'file://' + os.path.join(ROOT, rel)

# ── CONTENT ───────────────────────────────────────────────────────────────────
NAME = "Kaylee Renaud"
TITLE = "Costume Designer, Filmmaker, Writer"
EMAIL = "kayleeerenaud@gmail.com"
PHONE = "(518)226-9586"

EDU_LEFT = ["<b>New York University, Tisch School of the Arts</b>",
            "BFA, Film &amp; Television, Expected May 2027",
            "Minor Focus: Costume Design and Dance"]
EDU_RIGHT = ["<b>Additional Study:</b>",
             "Developing the Dramatic Script — Florence, Italy",
             "Storytelling — Athens, Greece"]

# Every section uses the same shape: (title, role, org, year, [bullets])
COSTUME = [
 ("Eurydice", "Costume Designer",
  "NYU Tisch Drama, Experimental Theater Wing · Dir. Elia Monte-Brown", "2026",
  ["Led a costume team from research through construction to production on stage",
   "Budget and receipt tracking"]),
 ("As You Like It", "Costume Assistant",
  "NYU Classical Studio · Dir. Daniel Spector", "2026",
  ["A low-budget, high-concept take on Shakespeare’s classic",
   "Assisted under Madison Barnett, mentored by Erin Black",
   "Technical drawings, research, fittings, swatching, and delegating to makers"]),
 ("Knights of the Old Republic, Ep. 2", "Costume Director",
  "The King’s Academy Studio 70 · Dir. Austin Parenti", "2026",
  ["Costume design for original characters",
   "Delegated construction to domestic and international makers",
   "Budget and receipt tracking"]),
 ("Weightless", "Costume Designer",
  "NYU Intermediate Narrative · Dir. Kevin Sherman", "2026",
  ["Costume design and sourcing for the short sci-fi film"]),
 ("Knights of the Old Republic, Ep. 1", "Costume Re-design &amp; Art Assistant",
  "The King’s Academy Studio 70 · Dir. Austin Parenti", "2025",
  ["Costume re-design for the villain, Davik Kang",
   "Art assistant across costume and props"]),
 ("Costume Consultant", "", "", "2025",
  ["“Anya” — costume &amp; color consultant; five-time award-winning short by Adele Xu",
   "“Sing Me to Sleep” — costume consultant; festival nominee by Pamela Fuller",
   "“Yoko” — costume consultant; a short film by Josh Li"]),
 ("Like Mother", "Costume Designer &amp; Fabricator",
  "NYU · Manhattan Film Festival Nominee · Dir. Ziyan Zheng", "2024",
  ["Costume design and construction for the short film",
   "Official Selection — Manhattan Film Festival &amp; Fusion Film Festival"]),
]

WARDROBE = [
 ("New York Theater Ballet", "Wardrobe Intern", "", "New York, NY · 2024",
  ["Performed costume alterations and repairs for ballet productions",
   "Assisted with organization, packing, and maintenance of wardrobe inventory"]),
]

TRAINING = [
 ("Costume Techniques", "Construction, Dying &amp; Distressing", "", "2026",
  ["Permanent and temporary dying and distressing techniques",
   "Draping and pattern drafting",
   "Technical illustration and construction research"]),
 ("Costume Design Thesis", "Costume Design Student", "", "2025",
  ["Concept, research, paperwork, and designs for Peter and the Starcatcher by Rick Elice"]),
]

ADDITIONAL = [
 ("Jean Doumanian Productions", "Development Intern", "", "New York, NY · 2026",
  ["Wrote script coverage and conducted research for current and prospective film projects",
   "Analyzed scripts for narrative structure, character development, and production potential"]),
 ("Camp-of-the-Woods", "Video Director &amp; Marketing Assistant", "", "Speculator, NY · 2024",
  ["Directed video coverage for live productions and seminars",
   "Produced marketing photography and assisted with media production"]),
 ("Chick-fil-A", "Front of House", "", "Albany &amp; New York, NY · 2025",
  ["Fast-paced, customer-forward environment with a focus on going the extra mile"]),
]

SKILLS = [
 ("Costume", "Costume Design · Costume Construction · Technical Illustration · Fabric dyeing &amp; "
             "distressing techniques · Draping and pattern drafting · Set construction"),
 ("Software", "Procreate · Final Draft · Adobe Premiere Pro · Lightroom · Pro Tools · "
              "Google Workspace · Claude integration"),
 ("Additional", "Research &amp; script analysis · Production coordination · Budget and receipt tracking"),
]

REFS = [
 ("Erin Black", "Professor of Production &amp; Design, NYU", "eks4@nyu.edu"),
 ("Michael Huff", "Executive Assistant, Jean Doumanian Productions", "mhuff@jeandoumanian.com"),
 ("Michael Gray", "Operator, Chick-fil-A Central Ave", "+1 (256) 338-4429"),
]

# ── RENDER ────────────────────────────────────────────────────────────────────
def entry(title, role, org, year, lines):
    r = f"<span class='role'> — {role}</span>" if role else ""
    o = f"<p class='org'>{org}</p>" if org else ""
    li = "".join(f"<li>{l}</li>" for l in lines)
    return (f"<article class='entry'>"
            f"<div class='hd'><p class='ttl'>{title}{r}</p><p class='yr'>{year}</p></div>"
            f"{o}<ul>{li}</ul></article>")

def section(label, items):
    return f"<h2>{label}</h2>" + "".join(entry(*i) for i in items)

skills_html = "".join(
    f"<p class='skill'><span class='k'>{k}</span><span class='v'>{v}</span></p>"
    for k, v in SKILLS)
refs_html = "".join(
    f"<div class='ref'><p class='rn'>{n}</p><p class='rr'>{r}</p><p class='rc'>{c}</p></div>"
    for n, r, c in REFS)
edu_l = "".join(f"<p>{x}</p>" for x in EDU_LEFT)
edu_r = "".join(f"<p>{x}</p>" for x in EDU_RIGHT)

DOC = f"""<!doctype html><html><head><meta charset='utf-8'><style>
@font-face {{ font-family:'EBG'; src:url('{furl("scripts/resume-assets/EBGaramond-VF.ttf")}');
  font-weight:400 800; font-style:normal; }}
@font-face {{ font-family:'EBG'; src:url('{furl("scripts/resume-assets/EBGaramond-Italic-VF.ttf")}');
  font-weight:400 800; font-style:italic; }}
@page {{ size: Letter; margin: 0.42in 0.66in 0.3in; }}
* {{ box-sizing:border-box; }}
html, body {{ margin:0; padding:0; color:#14110f;
  font-family:'EBG', Garamond, Georgia, serif; font-size:9.2pt; line-height:1.1; }}

/* header */
.head {{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:1.1pt solid #14110f; padding-bottom:.2em; }}
h1 {{ font-size:21.5pt; font-weight:500; margin:0; line-height:1; }}
.subtitle {{ margin:.24em 0 0; font-size:9pt; letter-spacing:.11em;
  text-transform:uppercase; color:#4a423c; }}
.contact {{ text-align:right; font-size:9.3pt; color:#4a423c; }}
.contact p {{ margin:0 0 .12em; }}
.contact a {{ color:#4a423c; text-decoration:none; }}

/* education */
.edu {{ display:flex; margin:.4em 0 0; font-size:9.2pt; }}
.edu > div {{ width:50%; padding-right:.35in; }}
.edu p {{ margin:0 0 .04em; }}

/* sections */
h2 {{ font-size:9.2pt; font-weight:700; letter-spacing:.14em; text-transform:uppercase;
  color:#14110f; margin:.44em 0 .16em; padding-bottom:.12em;
  border-bottom:.5pt solid #b9afa6; break-after:avoid; }}

/* entries */
.entry {{ margin:0 0 .14em; break-inside:avoid; }}
.entry:last-child {{ margin-bottom:0; }}
.hd {{ display:flex; justify-content:space-between; align-items:baseline; gap:.6em; }}
.ttl {{ margin:0; font-weight:700; }}
.role {{ font-weight:400; }}
.yr {{ margin:0; white-space:nowrap; font-size:9pt; letter-spacing:.06em; color:#6b615a; }}
.org {{ margin:.02em 0 0; font-style:italic; font-size:9.2pt; color:#4a423c; }}
ul {{ margin:.05em 0 0; padding-left:.92em; }}
li {{ margin:0 0 .02em; padding-left:.06em; }}
li::marker {{ color:#8a7f76; }}

/* skills + references */
.skill {{ display:flex; gap:.1in; margin:0 0 .1em; }}
.skill .k {{ flex:0 0 .74in; font-weight:600; font-style:italic; font-size:9.2pt;
  letter-spacing:.01em; }}
.skill .v {{ flex:1; }}
.refs {{ display:flex; gap:.28in; break-inside:avoid; }}
.refs .ref {{ width:33.33%; }}
.rn {{ margin:0; font-weight:700; }}
.rr {{ margin:.01em 0 0; font-style:italic; font-size:8.9pt; color:#4a423c; }}
.rc {{ margin:.02em 0 0; font-size:9pt; color:#4a423c; }}
</style></head><body>
<div class='head'>
  <div><h1>{NAME}</h1><p class='subtitle'>{TITLE}</p></div>
  <div class='contact'><p><a href='mailto:{EMAIL}'>{EMAIL}</a></p><p>{PHONE}</p></div>
</div>
<div class='edu'><div>{edu_l}</div><div>{edu_r}</div></div>
{section("Costume &amp; Wardrobe Experience", COSTUME + WARDROBE)}
{section("Costume Training", TRAINING)}
{section("Additional Experience", ADDITIONAL)}
<h2>Skills</h2>{skills_html}
<h2>References</h2><div class='refs'>{refs_html}</div>
</body></html>"""

out = os.path.join(ROOT, 'public', 'kaylee-renaud-costume-resume.pdf')
doc = HTML(string=DOC, base_url=ROOT).render()
doc.write_pdf(out)
print(f"wrote {out}  ({os.path.getsize(out)//1024} KB, {len(doc.pages)} pages)")
