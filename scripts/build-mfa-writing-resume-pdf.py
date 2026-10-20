#!/usr/bin/env python3
"""Generate Kaylee's NYU DRAMATIC WRITING MFA resume (public/kaylee-renaud-mfa-writing-resume.pdf).

Prompt: "Please list any published or produced work, and any work experience
that is relevant to a writing career." So: produced work she wrote/directed
leads, then writing-relevant experience (development, new-play work, set),
then writing study. Costume-only and unrelated jobs are left off.

Same layout as the other resumes (scripts/resume_layout.py), but set in
Figtree -- a screen-legible sans -- since admissions reads it on screen.
Wording reused verbatim from the film resume / CV.
    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-mfa-writing-resume-pdf.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from resume_layout import build, REFS

TITLE = "Writer, Filmmaker"

EDU_LEFT = ["<b>New York University, Tisch School of the Arts</b>",
            "BFA, Film &amp; Television, Expected May 2027",
            "Minor Focus: Costume Design and Dance"]
EDU_RIGHT = []

# (title, role, org, year, [bullets])
PRODUCED = [
 ("Schmoopy", "Writer · Director · Art Design", "Short film · NYU", "2025",
  ["A short comedy about a hospital janitor mistaken for a nurse on his first day, "
   "who must help deliver a baby moments before his own is born"]),
 ("Together, I’m Pieces", "Director · Editor", "Documentary · NYU Sight &amp; Sound", "2025",
  ["A documentary following Kaylee’s quest to understand her past by interviewing her parents",
   "NYU WinterFest selection · Honorable Mention, Fusion Film Festival"]),
 ("Spirit Temple No. 7", "Director · Cinematographer · Editor",
  "Documentary · NYU Sight &amp; Sound", "2025",
  ["A documentary following two brothers and their magical friend Chris as they build "
   "a spirit temple along the Brooklyn coast"]),
 ("Elli", "Director · Editor", "Documentary", "2024",
  ["A documentary about Dianna Goodwin’s mother, based on Dianna’s memoir, Army Brat"]),
]

EXPERIENCE = [
 ("Jean Doumanian Productions", "Development Intern", "", "New York, NY · 2026",
  ["Wrote script coverage and conducted research for current and prospective film projects",
   "Analyzed scripts for narrative structure, character development, and production potential"]),
 ("Be All End All", "Costume Designer",
  "Playwrights Horizons · By Jenn Martin · Dir. Delia Dumont", "2026",
  ["Designing and dressing an original play"]),
 ("Good Company", "Assistant Director", "NYU Intermediate Narrative · Dir. Sofia Cohen", "2025",
  ["A short comedy-thriller about two young women the morning after a party, "
   "both with murder on their minds"]),
 ("Camp-of-the-Woods", "Video Director &amp; Marketing Assistant", "", "Speculator, NY · 2024",
  ["Video director for live productions",
   "Camera operator for live-streamed and recorded seminars"]),
]

STUDY = [
 ("Developing the Dramatic Script", "", "", "Florence, Italy · 2025",
  ["Highly selective screen- and dramatic-writing course with NYU professor John Warren",
   "History of Italian Cinema with award-winning filmmaker Fede Gianni"]),
 ("Storytelling", "", "", "Athens, Greece · 2024",
  ["Highly selective storytelling course taught by screenwriter John Warren"]),
]

SKILLS = [
 ("Writing", "Screenwriting · Dramatic writing · Script coverage · "
             "Research &amp; script analysis · Academic &amp; creative writing"),
 ("Software", "Final Draft · Adobe Premiere Pro · Google Workspace · Procreate"),
]

# Figtree runs wider and darker than Garamond: open up spacing for screen,
# soften the bold, and lift the small greys to a darker tone for contrast.
EXTRA = """
.ttl { font-weight:650; } .rn { font-weight:650; } h2 { font-weight:700; font-size:8.8pt; }
h1 { font-weight:600; letter-spacing:-.01em; white-space:nowrap; }
.org, .rr, .rc, .contact, .contact a, .subtitle { color:#3d3631; }
.yr { color:#544b45; font-size:8.6pt; }
.skill .k { font-style:normal; font-weight:650; }
"""

build(
    "kaylee-renaud-mfa-writing-resume.pdf",
    TITLE,
    EDU_LEFT, EDU_RIGHT,
    [("Produced Work", PRODUCED),
     ("Writing-Relevant Experience", EXPERIENCE),
     ("Writing Study", STUDY)],
    SKILLS,
    refs=[r for r in REFS if 'Chick-fil-A' not in r[1]],
    website="kayleerenaud.com",
    skill_key=".85in",
    font="figtree", extra_css=EXTRA,
    fs=9.6, lh=1.28, entry_gap=".36em", h2_margin=".8em 0 .28em",
    page_margin="0.45in 0.66in 0.35in",
)
