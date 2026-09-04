#!/usr/bin/env python3
"""Printable career & goal planning worksheet for Kaylee.

Dense, small-print, black-on-white so it prints cheaply and leaves room to
write. Tailored to her actual situation: BFA Film & TV at NYU (May 2027),
three working lanes (costume / film / writing), grad-school applications
for Fall 2027, the NYU
Costume Shop job, and the festival + application cycle she is already in.

    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-planning-worksheet.py
"""
import os
from weasyprint import HTML

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def furl(rel): return 'file://' + os.path.join(ROOT, rel)

# ── little builders ───────────────────────────────────────────────────────────
def rules(n=3, cls=''):
    """n blank ruled lines to write on."""
    return f"<div class='rules {cls}'>" + "".join("<div class='rl'></div>" for _ in range(n)) + "</div>"

def field(label, n=1, cls=''):
    return f"<div class='field {cls}'><span class='fl'>{label}</span>{rules(n)}</div>"

def inline(*labels):
    """short labelled blanks on one row"""
    cells = "".join(f"<div class='ib'><span class='fl'>{l}</span><span class='blank'></span></div>"
                    for l in labels)
    return f"<div class='inline'>{cells}</div>"

def table(cols, rows, widths=None, head_note=''):
    widths = widths or [f"{100/len(cols):.4f}%"] * len(cols)
    ths = "".join(f"<th style='width:{w}'>{c}</th>" for c, w in zip(cols, widths))
    body = "".join("<tr>" + "".join("<td></td>" for _ in cols) + "</tr>" for _ in range(rows))
    note = f"<p class='note'>{head_note}</p>" if head_note else ""
    return f"{note}<table><thead><tr>{ths}</tr></thead><tbody>{body}</tbody></table>"

def checks(items, cols=2):
    lis = "".join(f"<li><span class='cb'></span>{i}</li>" for i in items)
    return f"<ul class='checks c{cols}'>{lis}</ul>"

def q(text):
    return f"<p class='q'>{text}</p>"

def box(title, inner, cls=''):
    return f"<section class='box {cls}'><h3>{title}</h3>{inner}</section>"

def h2(n, title, sub=''):
    s = f"<span class='sub'>{sub}</span>" if sub else ""
    return f"<h2><span class='num'>{n}</span>{title}{s}</h2>"

P = []   # pages

# ── PAGE 1 — WHERE I ACTUALLY AM ──────────────────────────────────────────────
P.append(f"""
<div class='masthead'>
  <div>
    <h1>Career &amp; Goal Planning</h1>
    <p class='dek'>A working worksheet — write in it, cross things out, be honest rather than impressive.</p>
  </div>
  <div class='mast-meta'>
    <p>Kaylee Renaud</p>
    <p>Date filled in: ____________________</p>
    <p>Horizon: ____________ to ____________</p>
  </div>
</div>

{h2(1, 'The hours I actually have', 'Not the ones I wish I had')}
<p class='note'>List every standing commitment for a normal week this semester — classes, the costume shop, shoots, church,
commute, sleep, seeing people you love. Add the hours up before you plan anything. The number at the bottom is the truth
you have to build on.</p>
{table(['Commitment', 'Hrs / wk', 'Paid?', 'Which lane does it feed?', 'Keep · Cut · Shrink · Grow'],
       11, ['30%','8%','8%','30%','24%'])}
{inline('Total committed hours', 'Hours left over', 'Hours I want back')}

{h2(2, 'My three lanes, told straight')}
<p class='note'>Costume · Film · Writing. Fill a column for each. A lane can be excellent and still be the wrong
one to push this year — that is what the last row is for.</p>
<table class='lanes'>
  <thead><tr><th style='width:22%'></th><th style='width:26%'>Costume</th><th style='width:26%'>Film</th><th style='width:26%'>Writing</th></tr></thead>
  <tbody>
    <tr class='rowlbl'><td>What I'm known for <em>now</em></td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Strongest piece of proof I have</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>What I want to be known for by 2029</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>The weakest link between here and there</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Does it pay yet? Could it?</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Does it feed me or drain me?</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>This year: <em>grow / hold / pause</em></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

{h2(3, 'What is not up for negotiation')}
<p class='note'>Money I must earn, hours I cannot exceed, people and practices I will not sacrifice, health limits.
Everything else in this worksheet has to fit around these.</p>
{rules(4)}

{h2(4, 'Faith &amp; the life underneath the work', 'The part no CV has a column for')}
<p class='note'>Career planning tends to assume the work is the point. Fill this in first if you want the rest of the sheet
to stay in proportion.</p>
<table class='rhythms'>
  <thead><tr><th style='width:22%'>Rhythm</th><th style='width:19%'>Honestly, right now</th><th style='width:26%'>What I want it to be</th><th style='width:33%'>What would actually make that possible</th></tr></thead>
  <tbody>
    <tr class='rowlbl'><td>Prayer</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Scripture / reading</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Church &amp; community</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Rest / sabbath</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Serving others</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Giving</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Silence, walks, being unproductive</td><td></td><td></td><td></td></tr>
  </tbody>
</table>
<div class='split'>
  <div>
    {q('Who knows the real state of things with me — not the update version?')}
    {rules(2)}
    {q('Where am I being asked to trust rather than to strive?')}
    {rules(2)}
  </div>
  <div>
    {q('What do I want my life with God to look like a year from now — described plainly, not piously?')}
    {rules(2)}
    {q('What am I trying to control that is not mine to carry?')}
    {rules(2)}
  </div>
</div>
{q('Where do faith and craft meet in my work — and where do they pull against each other?')}
{rules(2)}
{q('What would I refuse to make, or refuse to make it for? What am I FOR?')}
{rules(2)}
""")

# ── PAGE 2 — THE LADDER ───────────────────────────────────────────────────────
P.append(f"""
{h2(5, 'The ladder', 'Write the far one first, then work down. Each rung should make the one above it more likely.')}

<section class='rung'><h3>Five years out — autumn 2031</h3>
{q('Where do I live? What does a good Tuesday look like? What am I making, and who am I making it with? What pays for it?')}
{rules(4)}
</section>

<section class='rung'><h3>Two years out — autumn 2028, roughly eighteen months after graduation</h3>
{q('Three sentences. What is my title, or the honest description of what I do? What is on my reel or in my book? Who knows my name?')}
{rules(3)}
</section>

<section class='rung'><h3>Graduation — May 2027. What has to be TRUE by then?</h3>
{q('Portfolio, credits, relationships, savings, a place to live, a first job or the runway to look for one. Be specific enough to check off.')}
{table(['What must be true by May 2027', 'Why it matters', 'True yet? What is missing'], 6, ['38%','28%','34%'])}
</section>

<section class='rung'><h3>This academic year — September 2026 to May 2027</h3>
{q('No more than three goals. If everything is a goal, nothing is. Add how you will know each one is DONE, not "worked on."')}
{table(['Goal for the year', 'Done looks like…', 'First move', 'By when'], 3, ['32%','30%','24%','14%'])}
</section>

<section class='rung'><h3>This semester — through December 2026</h3>
{table(['What I will finish this semester', 'Which year-goal it serves', 'Deadline'], 5, ['46%','34%','20%'])}
</section>

<section class='rung split'>
  <div>
    <h3>This month</h3>
    {rules(4)}
  </div>
  <div>
    <h3>This week — three things, no more</h3>
    {checks(['', '', ''], cols=1)}
    {q('If the week goes sideways, which ONE of these still happens?')}
    {rules(1)}
  </div>
</section>

{h2(6, 'Reverse-plan one big goal', 'Pick the goal that scares you most and walk it backwards')}
{inline('The goal')}
<table class='reverse'>
  <thead><tr><th style='width:20%'>Working backwards</th><th style='width:52%'>What must already be done</th><th style='width:28%'>Who or what I need for it</th></tr></thead>
  <tbody>
    <tr class='rowlbl'><td>The goal itself</td><td></td><td></td></tr>
    <tr class='rowlbl'><td>One month before</td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Three months before</td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Six months before</td><td></td><td></td></tr>
    <tr class='rowlbl'><td>The very next step</td><td></td><td></td></tr>
  </tbody>
</table>
""")

# ── PAGE 3 — PIPELINE, MATERIALS, PEOPLE ──────────────────────────────────────
P.append(f"""
{h2(7, 'Grad school — entry Fall 2027', 'Most applications close between December 2026 and mid-January 2027. That is THIS semester.')}
<div class='split'>
  <div>
    {q('What do I want grad school to give me that two more years of working would not? Be concrete — training, time, a cohort, a credential, access, permission.')}
    {rules(3)}
  </div>
  <div>
    {q('What would make me decide NOT to go, or to defer a year? Name it now, before the deadlines start deciding for me.')}
    {rules(3)}
  </div>
</div>
<div class='keep'>{table(['Programme &amp; school', 'Deadline', 'What it wants (portfolio, samples, letters, test)', 'Fee', 'Waiver?', 'Sent'],
       7, ['24%','11%','35%','8%','9%','13%'])}</div>
<div class='split'>
  <div>
    <h3>Letters of recommendation</h3>
    <p class='note'>Ask at least six weeks out. Send each one the deadline, the programme, your résumé, and a reminder of what you did together.</p>
    {table(['Who', 'Asked?', 'Sent them my materials?', 'Due'], 4, ['34%','14%','32%','20%'])}
  </div>
  <div>
    <h3>What I have to make</h3>
    {checks(['Statement of purpose — first draft',
             'Statement rewritten for each school',
             'Portfolio / lookbook',
             'Writing sample — which script?',
             'Reel',
             'Transcripts requested',
             'CV updated',
             'Fee waivers checked'], cols=1)}
  </div>
</div>
<div class='split'>
  <div>
    {q('Money: tuition, aid, assistantships, teaching. What debt am I actually willing to take on — a number, not a feeling?')}
    {rules(3)}
  </div>
  <div>
    {q('If I do not go, or do not get in: what is my Fall 2027 instead? (This is a real plan, not a consolation prize.)')}
    {rules(3)}
  </div>
</div>
{inline('Statement drafted by', 'Letters requested by', 'Portfolio final by', 'Everything submitted by')}

{h2(8, 'The pipeline', 'Nothing happens without submitting, applying, or asking. Keep this page fed.')}
<p class='note'>Types: festival · internship · job · freelance gig · grant / fund · residency · fellowship · grad programme · open call.
A healthy pipeline has something in it every month, and most of it will be a no. That is the job.</p>
{table(['What', 'Type', 'Deadline', 'What it needs from me', 'Sent?', 'Result'],
       14, ['24%','12%','12%','30%','8%','14%'])}
{inline('Number out this month', 'Target per month', 'Next deadline that scares me')}

{h2(9, 'Materials audit', 'The stuff that speaks when you are not in the room')}
<table class='audit'>
  <thead><tr><th style='width:26%'>Piece</th><th style='width:12%'>Exists?</th><th style='width:16%'>Last updated</th><th style='width:46%'>What would make it stronger — and when I'll do it</th></tr></thead>
  <tbody>
    <tr class='rowlbl'><td>Costume resume</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Film &amp; writing resume</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>General resume</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>CV</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>kayleerenaud.com</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Costume portfolio / lookbook</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Directing reel</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Writing samples — which scripts?</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Business cards / NFC</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Instagram &amp; socials</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Letters of recommendation</td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Other</td><td></td><td></td><td></td></tr>
  </tbody>
</table>

{h2(10, 'People', 'Careers in this industry move through rooms, not applications')}
<p class='note'>Mentors, professors, supervisors, collaborators, the person one year ahead of you. Write the ask down — vague
check-ins fade, specific asks get answered. Then put a date on it.</p>
{table(['Name', 'How we know each other', 'Last real contact', 'What I would actually ask them for', 'When I reach out'],
       9, ['18%','22%','12%','32%','16%'])}
{q('Who do I owe a thank-you, an update, or an apology for going quiet?')}
{rules(2)}
{q('Who is doing the work I want to be doing in five years, that I have never spoken to? What would a first message say?')}
{rules(2)}
""")

# ── PAGE 4 — MONEY, TIME, SKILLS ──────────────────────────────────────────────
P.append(f"""
{h2(11, 'Money, plainly')}
<div class='split money'>
  <div>
    <h3>What I need</h3>
    {inline('Rent + bills / month', 'Food + transit / month')}
    {inline('Everything else / month', 'TOTAL I need / month')}
    {q('One-off costs coming (materials, festival fees, travel, gear, moving):')}
    {rules(3)}
  </div>
  <div>
    <h3>Where it comes from</h3>
    {table(['Source', '$ / month', 'Hours it costs', 'Reliable?'], 5, ['40%','18%','20%','22%'])}
    {inline('TOTAL in', 'Gap (+ / –)')}
  </div>
</div>
{q('If the gap is negative: what closes it — more hours, a rate rise, cutting something, or asking for help? Which of those am I avoiding, and why?')}
{rules(3)}
{q('What is my day rate for costume work? For film or video work? Have I ever said it out loud without apologising for it?')}
{rules(2)}

{h2(12, 'The week I want', 'Block the non-negotiables first, then the deep work, then the rest')}
<table class='week'>
  <thead><tr><th style='width:12%'></th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr></thead>
  <tbody>
    <tr class='rowlbl'><td>Morning</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Midday</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Afternoon</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
    <tr class='rowlbl'><td>Evening</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>
<div class='split'>
  <div>{q('What refills me (and how often do I actually do it?)')}{rules(2)}</div>
  <div>{q('What drains me fastest — and what is the early warning sign that I am running on empty?')}{rules(2)}</div>
</div>

{h2(13, 'Skills to build', 'Pick few. A half-learned skill is a hobby; a finished one is a credit.')}
{table(['Skill or craft', 'Why it matters to the goal', 'How I learn it (class, shop, project, person)', 'Cost', 'By when'],
       6, ['20%','26%','32%','10%','12%'])}
""")

# ── PAGE 5 — DECISIONS & REVIEW ───────────────────────────────────────────────
P.append(f"""
{h2(14, 'How I decide', 'Write the filter now, while nothing is at stake, so you can use it when something is')}
<div class='split'>
  <div>
    <h3>I say YES when…</h3>
    {rules(4)}
  </div>
  <div>
    <h3>I say NO when…</h3>
    {rules(4)}
  </div>
</div>
{q('My automatic no-s this year — the things I will stop being talked into:')}
{rules(2)}
{q('The last three things I said yes to. Would the filter above have let them through? Should it have?')}
{rules(3)}

{h2(15, 'The honest questions')}
{q('If I could only work in ONE lane for the next twelve months, which would I pick — and what does that tell me?')}
{rules(2)}
{q('What am I doing mostly because someone would be disappointed if I stopped?')}
{rules(2)}
{q('What would I attempt this year if I were certain no one would think it was arrogant?')}
{rules(2)}
{q('What am I afraid of? Underneath that, what am I actually afraid of?')}
{rules(2)}
<div class='split'>
  <div><h3>Fear</h3>{rules(3)}</div>
  <div><h3>What is actually true / what I would do about it</h3>{rules(3)}</div>
</div>
{q('At 30, looking back at this year — what would make me proud of it? What would make me wince?')}
{rules(3)}

{h2(16, 'Next fourteen days', 'The worksheet is worthless without this part')}
{table(['I will…', 'By (date)', 'Who knows I said so'], 3, ['56%','20%','24%'])}

{h2(17, 'Monthly check-in', 'Ten minutes, first of the month. Same five questions.')}
<p class='note'>1. What moved? &nbsp;·&nbsp; 2. What stalled, and honestly why? &nbsp;·&nbsp; 3. What did I say yes to that I should have declined?
&nbsp;·&nbsp; 4. What is the single most important thing for next month? &nbsp;·&nbsp; 5. Who do I need to talk to?</p>
{table(['Month', 'What moved', 'What stalled &amp; why', 'The one thing next month'],
       9, ['12%','30%','30%','28%'])}
{h2(18, 'Anything I am not ready to decide yet', 'Park it here rather than carrying it around')}
{rules(4)}
<p class='foot'>kayleerenaud.com · revisit this whole sheet at the end of each semester — Dec 2026, May 2027</p>
""")

pages_html = "".join(f"<div class='page'>{p}</div>" for p in P)

CSS = f"""
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
.page {{ }}   /* content flows continuously so no page is left half empty */

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
table.lanes td, table.reverse td, table.audit td {{ height:.29in; }}
table.week td {{ height:.42in; border-right:.5pt solid #d8d8d8; }}
table.week td:first-child {{ font-size:7.2pt; color:#444; background:#f4f2f0; }}

/* checkbox lists */
.checks {{ list-style:none; margin:.15em 0 .3em; padding:0; }}
.checks li {{ display:flex; align-items:center; gap:.12in; height:.27in;
  border-bottom:.5pt solid #b9b9b9; }}
.cb {{ flex:0 0 .13in; height:.13in; border:.8pt solid #777; }}

/* two-up blocks */
.split {{ display:flex; gap:.3in; }}
.split > div {{ flex:1; }}
.split.money > div:first-child {{ flex:.9; }}
.rung {{ break-inside:avoid; }}
table.lanes, table.week, table.reverse, table.rhythms {{ break-inside:avoid; }}
thead {{ display:table-header-group; }}   /* repeat headers when a table splits */
.split, .keep {{ break-inside:avoid; }}
.checks {{ break-inside:avoid; }}
.foot {{ margin-top:.5em; font-size:7pt; font-style:italic; color:#777; text-align:center; }}
"""

DOC = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{pages_html}</body></html>"

out = os.path.join(ROOT, 'public', 'planning', 'career-planning-worksheet.pdf')
os.makedirs(os.path.dirname(out), exist_ok=True)
doc = HTML(string=DOC, base_url=ROOT).render()
doc.write_pdf(out)
print(f"wrote {out}  ({os.path.getsize(out)//1024} KB, {len(doc.pages)} pages)")
