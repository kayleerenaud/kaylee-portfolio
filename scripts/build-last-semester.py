#!/usr/bin/env python3
"""LAST SEMESTER — the expiring list. September 2026 → May 2027.

Not a bucket list of things that would be nice. A list of things that STOP
BEING POSSIBLE when the student ID stops working and the people scatter.
The whole sheet expires, which is the point.

    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-last-semester.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worksheet_kit import *

P1 = f"""
{masthead('Last Semester',
          'Everything that stops being possible in May. Not what would be nice — what expires.',
          ['Kaylee Renaud &nbsp;·&nbsp; NYU Film &amp; TV',
           'Filled in: ____________________',
           'Expires: May 2027'])}

{inline('Today', 'Graduation day', 'Weeks left — count them', 'Weeks I&rsquo;ll be on a show')}

{h2(1, 'The expiry test', 'The only entry rule: it gets harder, costlier, or impossible once the ID stops working')}
{note('Studio and shop access · equipment checkout · the library · free and student-priced tickets · '
      'professors&rsquo; office hours · being cheap to say yes to · the people who are only here until May. '
      'If it will be exactly as available in 2028, it does not belong on this page — put it on a different list.')}
{table(['What', 'Why it expires', 'What it takes (time, money, an ask)', 'When', '✓'],
       9, ['28%','22%','32%','13%','5%'])}

{h2(2, 'The city, while it is the one I live in')}
{note('Bias toward what New York does that nowhere else does, and toward things that need a particular '
      'season or a particular person. Write the borough — it is how you will actually plan the day.')}
{table(['What / where', 'Borough', 'Who with', 'Season it needs', 'Cost', '✓'],
       11, ['32%','13%','19%','16%','13%','7%'])}
"""

P2 = f"""
{h2(3, 'People who scatter', 'The ones you assume you will keep seeing')}
{note('After May, everyone becomes a plane ticket. Write the thing you always said you would do together, '
      'and put a real date on it — the vague version does not survive graduation.')}
{table(['Who', 'Where they go after May', 'The thing we always said we&rsquo;d do', 'By when', '✓'],
       8, ['18%','22%','38%','16%','6%'])}

{h2(4, 'Rooms I can still get into', 'Being a student is a door that closes quietly')}
{note('Sets, shops, crews, classes you are not enrolled in, someone&rsquo;s thesis, a designer who will let a '
      'student shadow. You are cheap to say yes to right now, and that is leverage. Spend it.')}
{table(['The room', 'Who opens it', 'What I ask for, in one sentence', 'Asked?', 'Result'],
       6, ['22%','18%','36%','10%','14%'])}

{h2(5, 'One per month', 'The forcing function — everything above stays a wish without this table')}
{table(['', 'The one thing that happens this month', 'With whom', '✓'],
       0, ['13%','54%','26%','7%'], cls='tall',
       rowlbls=['Sept 2026','October','November','December','January 2027',
                'February','March','April','May — last one'])}

{h2(6, 'Small, free, and near', 'So the sheet is not only made of ambitious days')}
{split(h3('Costs nothing') + rules(3),
       h3('Alone, on purpose') + rules(3),
       h3('An hour or less') + rules(3))}

{h2(7, 'Last times worth noticing')}
{note('Most last times happen without anyone announcing them — the last time you walk out of that building, '
      'the last fitting in that shop, the last late train home with those people. Name the ones you want to be awake for.')}
{rules(2)}

{h2(8, 'What I will not get to — and I am at peace with it')}
{note('Write this one honestly. A list this size is only usable if something is allowed to be cut.')}
{rules(2)}
{foot('kayleerenaud.com &nbsp;·&nbsp; Last Semester &nbsp;·&nbsp; this sheet expires in May 2027 — that is the feature')}
"""

build([P1, P2], 'public/planning/last-semester-worksheet.pdf')
