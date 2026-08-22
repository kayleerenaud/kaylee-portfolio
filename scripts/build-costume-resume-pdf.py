#!/usr/bin/env python3
"""Generate Kaylee's COSTUME-SPECIFIC resume (public/kaylee-renaud-costume-resume.pdf).

A costume-shop-facing cut of the general resume: every costume credit carries
responsibility bullets (pulled verbatim from the CV), plus the three non-costume
jobs that show work history (Jean Doumanian Productions, Camp-of-the-Woods,
Chick-fil-A). Wording is reused verbatim from kaylee-renaud-resume.pdf and
scripts/build-cv-pdf.py -- nothing here is rewritten.

Layout: one page, EB Garamond, a single entry format throughout --
  **Title** · Role                                                        YEAR
  Company · Director / festival note   (italic)
  • responsibility bullets

Re-run after editing CONTENT below:
    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-costume-resume-pdf.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resume_layout import build, REFS

# ── CONTENT ───────────────────────────────────────────────────────────────────
TITLE = "Costume Designer, Filmmaker, Writer"

EDU_LEFT = ["<b>New York University, Tisch School of the Arts</b>",
            "BFA, Film &amp; Television, Expected May 2027",
            "Minor Focus: Costume Design and Dance"]
EDU_RIGHT = ["<b>Additional Study:</b>",
             "Developing the Dramatic Script · Florence, Italy",
             "Storytelling · Athens, Greece"]

# Every section uses the same shape: (title, role, org, year, [bullets])
COSTUME = [
 ("NYU Costume Shop", "Costume Shop Assistant", "", "New York, NY · 2026–Present",
  ["Garment construction, crafting, and distressing",
   "Costume Loan: organizing and keeping itemized notes for the stock, and leading "
   "appointments to find items for NYU productions"]),
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
  ["“Anya”: costume &amp; color consultant; five-time award-winning short by Adele Xu",
   "“Sing Me to Sleep”: costume consultant; festival nominee by Pamela Fuller",
   "“Yoko”: costume consultant; a short film by Josh Li"]),
 ("Like Mother", "Costume Designer &amp; Fabricator",
  "NYU · Manhattan Film Festival Nominee · Dir. Ziyan Zheng", "2024",
  ["Costume design and construction for the short film",
   "Official Selection: Manhattan Film Festival &amp; Fusion Film Festival"]),
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
]

SKILLS = [
 ("Costume", "Costume Design · Costume Construction · Technical Illustration · Fabric dyeing &amp; "
             "distressing techniques · Draping and pattern drafting · Set construction"),
 ("Software", "Procreate · Final Draft · Adobe Premiere Pro · Lightroom · Pro Tools · "
              "Google Workspace · Claude integration"),
 ("Additional", "Research &amp; script analysis · Production coordination · Budget and receipt tracking"),
]

build(
    "kaylee-renaud-costume-resume.pdf",
    TITLE,
    EDU_LEFT, EDU_RIGHT,
    [("Costume &amp; Wardrobe Experience", COSTUME + WARDROBE),
     ("Costume Training", TRAINING),
     ("Additional Experience", ADDITIONAL)],
    SKILLS,
    refs=[r for r in REFS if 'Chick-fil-A' not in r[1]],
)
