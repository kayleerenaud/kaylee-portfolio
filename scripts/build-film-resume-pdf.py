#!/usr/bin/env python3
"""Generate Kaylee's FILMMAKING & WRITING resume (public/kaylee-renaud-film-resume.pdf).

The film/writing counterpart to the costume resume: directing and writing credits
lead, each carrying its logline and festival note, followed by crew credits,
development work, and writing study. Wording is reused verbatim from
kaylee-renaud-resume.pdf and scripts/build-cv-pdf.py -- nothing is rewritten.

Shares its layout with the costume resume via scripts/resume_layout.py.
Re-run after editing CONTENT below:
    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-film-resume-pdf.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resume_layout import build

# ── CONTENT ───────────────────────────────────────────────────────────────────
TITLE = "Filmmaker, Writer, Costume Designer"

EDU_LEFT = ["<b>New York University, Tisch School of the Arts</b>",
            "BFA, Film &amp; Television, Expected May 2027",
            "Minor Focus: Costume Design and Dance"]
EDU_RIGHT = []

# (title, role, org, year, [bullets])
DIRECTING = [
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
 ("Elli", "Director · Editor", "", "2024",
  ["A documentary about Dianna Goodwin’s mother, based on Dianna’s memoir, Army Brat"]),
]

CREDITS = [
 ("Good Company", "Assistant Director", "NYU Intermediate Narrative · Dir. Sofia Cohen", "2025",
  ["A short comedy-thriller about two young women the morning after a party, "
   "both with murder on their minds"]),
 ("Carried by the Wind", "B-Camera",
  "NYU Sight &amp; Sound: Documentary · Dir. Ziyan Zheng", "2025",
  ["A documentary following the director home to Guangzhou to say goodbye to her "
   "childhood home before it’s sold"]),
 ("Like Mother", "Costume Designer &amp; Fabricator", "NYU · Dir. Ziyan Zheng", "2024",
  ["Costume design and construction for the short film",
   "Official Selection: Manhattan Film Festival &amp; Fusion Film Festival"]),
 ("Production Assistant", "", "", "New York, NY · 2024",
  ["PA on numerous intermediate and advanced NYU student films"]),
]

DEVELOPMENT = [
 ("Jean Doumanian Productions", "Development Intern", "", "New York, NY · 2026",
  ["Wrote script coverage and conducted research for current and prospective film projects",
   "Analyzed scripts for narrative structure, character development, and production potential"]),
]

STUDY = [
 ("Developing the Dramatic Script", "", "", "Florence, Italy · 2025",
  ["Highly selective screen- and dramatic-writing course with NYU professor John Warren",
   "History of Italian Cinema with award-winning filmmaker Fede Gianni"]),
 ("Storytelling", "", "", "Athens, Greece · 2024",
  ["Highly selective storytelling course taught by screenwriter John Warren"]),
]

ADDITIONAL = [
 ("NYU Costume Shop", "Costume Shop Assistant", "", "New York, NY · 2026–Present",
  ["Garment construction, crafting, and distressing",
   "Costume Loan: organizing and keeping itemized notes for the stock, and leading "
   "appointments to find items for NYU productions"]),
 ("Camp-of-the-Woods", "Video Director &amp; Marketing Assistant", "", "Speculator, NY · 2024",
  ["Video director for live productions",
   "Camera operator for live-streamed and recorded seminars",
   "Marketing assistant and photographer"]),
 ("Renew College Church", "Volunteer", "", "2025",
  ["Media team: recorded B-roll and interviewed players at a city-wide youth tournament",
   "Designed event posters for NYU and Columbia students"]),
 ("Chick-fil-A", "Front of House", "", "Albany &amp; New York, NY · 2025",
  ["Fast-paced, customer-forward environment with a focus on going the extra mile"]),
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
    "kaylee-renaud-film-resume.pdf",
    TITLE,
    EDU_LEFT, EDU_RIGHT,
    [("Directing &amp; Writing", DIRECTING),
     ("Film Credits", CREDITS),
     ("Development &amp; Industry", DEVELOPMENT),
     ("Writing &amp; Film Study", STUDY),
     ("Additional Experience", ADDITIONAL)],
    SKILLS,
    website="kayleerenaud.com",
    skill_key="1.22in",
    entry_gap=".2em", h2_margin=".55em 0 .18em",
)
