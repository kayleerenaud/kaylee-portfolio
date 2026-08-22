#!/usr/bin/env python3
"""Generate Kaylee's GENERAL resume (public/kaylee-renaud-general-resume.pdf).

The all-purpose cut for applications that aren't specifically costume or film:
paid/industry work first, then the strongest film & writing credits, then the
strongest costume credits -- one or two bullets each so the page stays scannable.
Wording is reused verbatim from kaylee-renaud-resume.pdf and
scripts/build-cv-pdf.py -- nothing is rewritten.

Shares its layout with the costume and film resumes via scripts/resume_layout.py.
Re-run after editing CONTENT below:
    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-general-resume-pdf.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resume_layout import build

# ── CONTENT ───────────────────────────────────────────────────────────────────
TITLE = "Filmmaker, Writer, Costume Designer"

EDU_LEFT = ["<b>New York University, Tisch School of the Arts</b>",
            "BFA, Film &amp; Television, Expected May 2027",
            "Additional Focuses: Costume Design and Dance"]
EDU_RIGHT = ["<b>Additional Study:</b>",
             "Developing the Dramatic Script — Florence, Italy",
             "Storytelling — Athens, Greece"]

# (title, role, org, year, [bullets])
INDUSTRY = [
 ("NYU Costume Shop", "Costume Shop Assistant", "", "New York, NY · 2026–Present",
  ["Garment construction, crafting, and distressing",
   "Costume Loan — organizing and keeping itemized notes for the stock, and leading "
   "appointments to find items for NYU productions"]),
 ("Jean Doumanian Productions", "Development Intern", "", "New York, NY · 2026",
  ["Wrote script coverage and conducted research for current and prospective film projects",
   "Analyzed scripts for narrative structure, character development, and production potential"]),
 ("New York Theater Ballet", "Wardrobe Intern", "", "New York, NY · 2024",
  ["Performed costume alterations and repairs for ballet productions",
   "Assisted with organization, packing, and maintenance of wardrobe inventory"]),
 ("Camp-of-the-Woods", "Video Director &amp; Marketing Assistant", "", "Speculator, NY · 2024",
  ["Directed video coverage for live productions and seminars",
   "Produced marketing photography and assisted with media production"]),
]

FILM = [
 ("Schmoopy", "Writer · Director · Art Design", "NYU", "2025",
  ["A short comedy about a hospital janitor mistaken for a nurse on his first day, "
   "who must help deliver a baby moments before his own is born"]),
 ("Together, I’m Pieces", "Director · Editor", "NYU Sight &amp; Sound: Documentary", "2025",
  ["A documentary following Kaylee’s quest to understand her past by interviewing her parents",
   "NYU WinterFest selection · Honorable Mention, Fusion Film Festival"]),
 ("Spirit Temple No. 7", "Director · Cinematographer · Editor",
  "NYU Sight &amp; Sound: Documentary", "2025",
  ["A documentary following two brothers and their magical friend Chris as they build "
   "a spirit temple along the Brooklyn coast"]),
 ("Good Company", "Assistant Director", "NYU Intermediate Narrative · Dir. Sofia Cohen", "2025",
  ["A short comedy-thriller about two young women the morning after a party, "
   "both with murder on their minds"]),
 ("Production Assistant", "", "", "New York, NY · 2024",
  ["PA on numerous intermediate and advanced NYU student films"]),
]

COSTUME = [
 ("Eurydice", "Costume Designer",
  "NYU Tisch Drama, Experimental Theater Wing · Dir. Elia Monte-Brown", "2026",
  ["Led a costume team from research through construction to production on stage",
   "Budget and receipt tracking"]),
 ("Knights of the Old Republic, Ep. 2", "Costume Director",
  "The King’s Academy Studio 70 · Dir. Austin Parenti", "2026",
  ["Costume design for original characters",
   "Delegated construction to domestic and international makers"]),
 ("As You Like It", "Costume Assistant", "NYU Classical Studio · Dir. Daniel Spector", "2026",
  ["Technical drawings, research, fittings, swatching, and delegating to makers"]),
 ("Weightless", "Costume Designer", "NYU Intermediate Narrative · Dir. Kevin Sherman", "2026",
  ["Costume design and sourcing for the short sci-fi film"]),
 ("Like Mother", "Costume Designer &amp; Fabricator", "NYU · Dir. Ziyan Zheng", "2024",
  ["Costume design and construction for the short film",
   "Official Selection — Manhattan Film Festival &amp; Fusion Film Festival"]),
]

OTHER_WORK = [
 ("Chick-fil-A", "Front of House", "", "Albany &amp; New York, NY · 2025",
  ["Fast-paced, customer-forward environment with a focus on going the extra mile"]),
 ("Camp-of-the-Woods", "Waitress", "", "Speculator, NY · 2023",
  ["Served guests in a fast-paced family dining hall",
   "Cleaning and upkeep of the dining hall · OSHA trained"]),
]

SKILLS = [
 ("Creative &amp; Production", "Directing · Screenwriting · Costume Design · "
                               "Costume Construction · Technical Illustration"),
 ("Software", "Final Draft · Adobe Premiere Pro · Lightroom · Pro Tools · Procreate · "
              "Google Workspace · Claude integration"),
 ("Additional", "Research &amp; script analysis · Production coordination · "
                "Fabric dyeing &amp; distressing techniques"),
]

build(
    "kaylee-renaud-general-resume.pdf",
    TITLE,
    EDU_LEFT, EDU_RIGHT,
    [("Industry Experience", INDUSTRY),
     ("Film &amp; Writing", FILM),
     ("Costume Design", COSTUME),
     ("Additional Work Experience", OTHER_WORK)],
    SKILLS,
    fs=8.95, lh=1.06, page_margin="0.36in 0.6in 0.24in",
    website="kayleerenaud.com",
    skill_key="1.22in",
    entry_gap=".11em", h2_margin=".38em 0 .14em",
)
