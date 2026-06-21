#!/usr/bin/env python3
"""Generate Kaylee's CV PDF (public/kaylee-renaud-cv.pdf) in the site's dark
aesthetic via WeasyPrint. Self-contained: fonts + headshot referenced by path.
Re-run after editing CONTENT below:  python3 scripts/build-cv-pdf.py
"""
import os, html
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def furl(rel): return 'file://' + os.path.join(ROOT, rel)

# ── CONTENT ───────────────────────────────────────────────────────────────────
NAME = "Kaylee Renaud"
TITLE = "Writer · Filmmaker · Costume Designer"
BIO = ("New York-based artist and writer drawn to character-driven stories and "
       "mixed media, with an enduring love of faith-based storytelling for young "
       "audiences. Across theater, marketing, live production, and wardrobe, she "
       "has contributed to over twenty stage productions and thirty short films. "
       "She is pursuing a BFA in Film & Television at NYU with additional focuses "
       "in Costume Design and Dance.")
EMAIL = "kayleeerenaud@gmail.com"; PHONE = "(518) 226-9586"; LOC = "New York, NY"
HARD = ["Photography / Videography","Procreate Illustration","Costume Design",
        "Costume Construction","Set Construction","Academic & Creative Writing",
        "Final Draft","Premiere Pro","Lightroom","Pro Tools","Google Workspace","Claude"]
SOFT = ["Teachable","Creative","Organized","Adaptable","Customer-oriented"]
EDU = [("BFA, Film & Television","New York University · Tisch School of the Arts",
        "Minor focuses: Costume Design & Dance","Expected May 2027")]
TIMELINE = [
 ("2026", [
   ("Eurydice","Costume Designer · NYU Tisch Drama, Experimental Theater Wing",
    ["Led a costume team from research through construction to production on stage","Budget and receipt tracking"]),
   ("Jean Doumanian Productions","Development Intern · New York, NY",
    ["Script coverage","Research for current and prospective JDP projects"]),
   ("Knights of the Old Republic, Ep. 2","Costume Director · Studio 70",
    ["Costume design for original characters","Delegated construction to domestic and international makers","Budget and receipt tracking"]),
   ("As You Like It","Costume Assistant · NYU Drama",
    ["A low-budget, high-concept take on Shakespeare’s classic","Assisted under Madison Barnett, mentored by Erin Black","Technical drawings, research, fittings, swatching, and delegating to makers"]),
   ("Weightless","Costume Designer · dir. Kevin Sherman",
    ["Costume design and sourcing for the short sci-fi film"]),
   ("Costume Techniques","Construction, Dying & Distressing",
    ["Permanent and temporary dying and distressing techniques","Draping and pattern drafting","Technical illustration and construction research"]),
 ]),
 ("2025", [
   ("Schmoopy","Writer · Director · Art Design",
    ["A short comedy about a hospital janitor mistaken for a nurse on his first day, who must help deliver a baby moments before his own is born"]),
   ("Costume Consultant","",
    ["“Anya” — costume & color consultant; five-time award-winning short by Adele Xu","“Sing Me to Sleep” — costume consultant; festival nominee by Pamela Fuller","“Yoko” — costume consultant; a short film by Josh Li"]),
   ("Good Company","Assistant Director · dir. Sofia Cohen",
    ["A short comedy-thriller about two young women the morning after a party, both with murder on their minds"]),
   ("Together, I’m Pieces","Director",
    ["A documentary following Kaylee’s quest to understand her past by interviewing her parents","NYU WinterFest selection · Honorable Mention, Fusion Film Festival"]),
   ("Carried by the Wind","B-Camera · dir. Ziyan Zheng",
    ["A documentary following the director home to Guangzhou to say goodbye to her childhood home before it’s sold"]),
   ("Renew College Church","Volunteer",
    ["Media team — recorded B-roll and interviewed players at a city-wide youth tournament","Designed event posters for NYU and Columbia students","Food crew volunteer"]),
   ("Developing the Dramatic Script","Florence, Italy",
    ["Highly selective screen- and dramatic-writing course with NYU professor John Warren","History of Italian Cinema with award-winning filmmaker Fede Gianni"]),
   ("Chick-fil-A","Front of House · Albany & New York, NY",
    ["Fast-paced, customer-forward environment with a focus on going the extra mile"]),
   ("Knights of the Old Republic, Ep. 1","Costume Re-design & Art Assistant · Studio 70",
    ["Costume re-design for the villain, Davik Kang","Art assistant across costume and props"]),
   ("Like Mother","Costume Designer & Fabricator · dir. Ziyan Zheng",
    ["Costume design and construction for the short film","Official Selection — Manhattan Film Festival & Fusion Film Festival"]),
   ("Spirit Temple No. 7","Director · Cinematographer · Editor",
    ["A documentary following two brothers and their magical friend Chris as they build a spirit temple along the Brooklyn coast"]),
   ("Costume Design Thesis","Costume Design Student",
    ["Concept, research, paperwork, and designs for Peter and the Starcatcher by Rick Elice"]),
 ]),
 ("2024", [
   ("Elli","Director · Editor",
    ["A documentary about Dianna Goodwin’s mother, based on Dianna’s memoir, Army Brat"]),
   ("Storytelling","Athens, Greece",
    ["Highly selective storytelling course taught by screenwriter John Warren"]),
   ("Production Assistant","New York, NY",
    ["PA on numerous intermediate and advanced NYU student films"]),
   ("New York Theater Ballet","Wardrobe",
    ["Costume alterations and repairs","Wardrobe packing and organization"]),
   ("Camp-of-the-Woods","Video Director & Marketing Assistant",
    ["Video director for live productions","Camera operator for live-streamed and recorded seminars","Marketing assistant and photographer"]),
 ]),
]
REFS = [
 ("Erin Black","Professor of Production & Design, NYU","eks4@nyu.edu"),
 ("Michael Huff","Executive Assistant, Jean Doumanian Productions","mhuff@jeandoumanian.com"),
 ("Michael Gray","Operator, Chick-fil-A Central Ave","+1 (256) 338-4429"),
]

e = html.escape
def chips(items): return "".join(f"<span class='chip'>{e(x)}</span>" for x in items)
def entry(t, role, lines):
    r = f"<p class='role'>{e(role)}</p>" if role else ""
    li = "".join(f"<li>{e(l)}</li>" for l in lines)
    return f"<article class='entry'><h4>{e(t)}</h4>{r}<ul>{li}</ul></article>"
def year(y, ents): return f"<h3 class='year'>{e(y)}</h3>" + "".join(entry(*x) for x in ents)
edu_html = "".join(f"<div class='edu'><p class='edu-deg'>{e(d)}</p><p class='edu-sch'>{e(s)}</p>"
                   f"<p class='edu-det'>{e(det)}</p><p class='edu-date'>{e(dt)}</p></div>" for d,s,det,dt in EDU)
refs_html = "".join(f"<div class='ref'><p class='ref-n'>{e(n)}</p><p class='ref-r'>{e(r)}</p>"
                    f"<p class='ref-c'>{e(c)}</p></div>" for n,r,c in REFS)
exp_html = "".join(year(y, ents) for y,ents in TIMELINE)

DOC = f"""<!doctype html><html><head><meta charset='utf-8'><style>
@font-face {{ font-family:'Kaylee Script'; src:url('{furl("public/fonts/KayleeScript-Regular.ttf")}'); }}
@font-face {{ font-family:'Spectral'; font-weight:400; src:url('{furl("scripts/cv-assets/Spectral-Regular.ttf")}'); }}
@font-face {{ font-family:'Spectral'; font-weight:500; src:url('{furl("scripts/cv-assets/Spectral-Medium.ttf")}'); }}
@font-face {{ font-family:'Spectral'; font-weight:600; src:url('{furl("scripts/cv-assets/Spectral-SemiBold.ttf")}'); }}
@page {{ size: Letter; margin: 0.55in 0; }}
* {{ box-sizing: border-box; }}
html, body {{ margin:0; padding:0; background:#14110f; color:#f1ece4;
  font-family:'Spectral', Georgia, serif; font-size:9.3pt; line-height:1.4; }}
.sidebar {{ position: fixed; top:0; left:0; bottom:0; width:2.45in; background:#1b1714;
  border-right:2px solid #7a4f5a; padding:0.12in 0.3in 0.3in; }}
.photo {{ width:1.55in; height:1.55in; border-radius:50%; margin:0 auto 0.28in;
  background-image:url('{furl("public/kaylee-headshot.jpg")}'); background-size:cover; background-position:center;
  border:2px solid #d98a9e; }}
.s-h {{ font-size:7.4pt; letter-spacing:.18em; text-transform:uppercase; color:#d98a9e;
  margin:0 0 .5em; padding-bottom:.3em; border-bottom:1px solid #2c2722; font-weight:600; }}
.block {{ margin-bottom:.95rem; }}
.contact p {{ margin:0 0 .2em; color:#bdb4a7; font-size:8.6pt; }}
.contact a {{ color:#bdb4a7; text-decoration:none; }}
.chip {{ display:inline-block; font-size:7.6pt; color:#efe9df; border:1px solid #6b4750;
  background:#241a1c; border-radius:40px; padding:.12em .6em; margin:0 .25em .3em 0; }}
.soft .chip {{ color:#bdb4a7; background:transparent; }}
.main {{ margin-left:2.45in; padding:0 0.5in; }}
.head {{ border-bottom:2px solid #7a4f5a; padding-bottom:.5rem; margin-bottom:1rem; }}
.head h1 {{ font-family:'Kaylee Script', cursive; font-weight:400; font-size:34pt; line-height:.9;
  margin:0; color:#f1ece4; }}
.head .title {{ font-size:8pt; letter-spacing:.2em; text-transform:uppercase; color:#d98a9e; margin:.5em 0 0; }}
.bio {{ color:#e7e0d4; margin:0 0 .8rem; }}
.section {{ font-family:'Kaylee Script', cursive; font-size:21pt; color:#f1ece4; margin:.3rem 0 .45rem; }}
.edu-deg {{ font-weight:600; margin:0; }}
.edu-sch {{ color:#bdb4a7; margin:.1em 0 0; font-size:8.6pt; }}
.edu-det {{ color:#a59c90; margin:.1em 0 0; font-size:8pt; font-style:italic; }}
.edu-date {{ color:#d98a9e; margin:.2em 0 0; font-size:7.8pt; letter-spacing:.04em; }}
.track {{ border-left:2px solid #5e4148; padding-left:.95rem; margin-left:.15rem; }}
.year {{ font-family:'Kaylee Script', cursive; font-size:17pt; color:#d98a9e; margin:.8rem 0 .4rem; position:relative; }}
.year::before {{ content:''; position:absolute; left:-1.27rem; top:.28em; width:10px; height:10px;
  border-radius:50%; background:#d98a9e; }}
.entry {{ margin:0 0 .42rem; position:relative; }}
.entry h4 {{ font-weight:600; font-size:10pt; margin:0; color:#f4efe6; }}
.role {{ color:#d98a9e; font-size:7.8pt; letter-spacing:.02em; margin:.12em 0 .2em; }}
.entry ul {{ margin:.1em 0 0; padding-left:1rem; }}
.entry li {{ color:#a59c90; margin:0 0 .12em; }}
.refs {{ margin-top:.7rem; }}
.ref {{ margin-bottom:.38rem; }}
.ref-n {{ font-weight:600; margin:0; }}
.ref-r {{ color:#a59c90; font-size:8pt; margin:.1em 0 0; }}
.ref-c {{ color:#d98a9e; font-size:8pt; margin:.05em 0 0; }}
.entry, .ref, .edu {{ break-inside:avoid; }}
.year {{ break-after:avoid; }}
</style></head><body>
<aside class='sidebar'>
  <div class='photo'></div>
  <div class='block contact'><p class='s-h'>Contact</p>
    <p><a href='mailto:{EMAIL}'>{e(EMAIL)}</a></p><p>{e(PHONE)}</p><p>{e(LOC)}</p></div>
  <div class='block'><p class='s-h'>Skills</p><div>{chips(HARD)}</div></div>
  <div class='block soft'><p class='s-h'>Strengths</p><div>{chips(SOFT)}</div></div>
</aside>
<main class='main'>
  <div class='head'><h1>{e(NAME)}</h1><p class='title'>{e(TITLE)}</p></div>
  <p class='bio'>{e(BIO)}</p>
  <h2 class='section'>Education</h2>{edu_html}
  <h2 class='section'>Experience</h2><div class='track'>{exp_html}</div>
  <h2 class='section refs-h'>References</h2><div class='refs'>{refs_html}</div>
</main>
</body></html>"""

out = os.path.join(ROOT, 'public', 'kaylee-renaud-cv.pdf')
doc = HTML(string=DOC, base_url=ROOT).render()
doc.write_pdf(out)
print(f"wrote {out}  ({os.path.getsize(out)//1024} KB, {len(doc.pages)} pages)")
