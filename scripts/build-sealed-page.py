#!/usr/bin/env python3
"""THE SEALED PAGE — fill the left column now, seal it, open it on a written date.

DELIBERATE RULE BEND (spec §1 brief): the house brief calls these "working
documents, not keepsakes — cross things out." This one IS a keepsake, so two
rules are bent on purpose rather than by accident:
  · rows are .36in (`table.taller`) not .245in, because it will be re-read;
  · the letter blocks get generous ruled space instead of maximum density.
Everything else — greyscale, hairlines, EB Garamond, Letter — is unchanged.
Print it on heavier paper than the rest of the family.

    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-sealed-page.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worksheet_kit import *

NOWTHEN = ['', 'Now', 'Then']
W = ['34%','33%','33%']

P1 = f"""
{masthead('The Sealed Page',
          'Fill the left column in one sitting. Fold it, seal it, write the opening date on the outside.',
          ['Sealed on: ____________________',
           'To be opened: ____________________',
           'Witnessed by: ____________________'])}

{note('<b>How to use it.</b> Left column tonight, in one pass — do not draft, do not improve, do not reread. '
      'Then put it in an envelope and write the opening date where you will see it. On that day, fill the right '
      'column <b>in a different pen</b>, and only then read what you wrote. The whole value of this sheet is that '
      'you cannot edit the first column later.')}

{h2(1, 'Where I actually am', 'Facts, not reflections. These are the ones that will have quietly changed.')}
{table(NOWTHEN, 0, W, cls='taller vgrid', rowlbls=[
  'The city, the neighbourhood, and who I live with',
  'What a normal Tuesday looks like',
  'What is on my nightstand',
  'The last thing I finished making',
  'What I actually reach for in my closet',
  'Who I have seen most this week',
  'What I am reading, and whether I am enjoying it',
  'The song I have played into the ground',
  'What is in my bag right now',
  'My day rate, if someone asked me today',
  'The last thing that made me laugh out loud'])}

{h2(2, 'In progress', 'The unfinished things — the ones a year will either resolve or expose')}
{table(NOWTHEN, 0, W, cls='taller vgrid', rowlbls=[
  'The project I am most afraid of',
  'The thing I am avoiding, and why',
  'What I am waiting to hear about',
  'The prayer I keep repeating',
  'What I would change about my work if I could',
  'Who I am becoming, in three words'])}
"""

P2 = f"""
{h2(3, 'Predictions', 'Make them falsifiable. A prediction you cannot be wrong about is a mood.')}
{note('Good seeds: where I will be living · what I will have heard back about, and the answer · what I will '
      'have finished · what I will still be putting off · a person I have not met yet · something I am sure of '
      'today that I will find funny.')}
{table(['I predict that…', 'Sure? 1–5', 'What actually happened', '✓ / ✗'],
       9, ['44%','10%','38%','8%'], cls='tall vgrid')}

{h2(4, 'What I hope has NOT changed')}
{table(['', 'Name it now', 'Still true? What did it cost to keep?'], 0, ['26%','34%','40%'], cls='taller vgrid',
       rowlbls=['A person', 'A habit or rhythm', 'Something I believe',
                'Something about how I work', 'Something small and stupid I love'])}

{h2(5, 'A letter', 'To whoever opens this — who is, inconveniently, you')}
{split(h3('Written on the day it was sealed')
       + note('Tell her what today was actually like. Not the summary — the texture.')
       + rules(11),
       h3('Written on the day it was opened')
       + note('Different pen. Answer her.')
       + rules(11))}

{h2(6, 'For the record', 'Small, dateable, and the first thing memory gets wrong')}
{split(h3('Three things I am grateful for today') + rules(3),
       h3('Three things that annoyed me today') + rules(3),
       h3('Three people I would call right now') + rules(3))}

{inline('Opened on', 'Where I was', 'Who was with me')}
{foot('kayleerenaud.com &nbsp;·&nbsp; The Sealed Page &nbsp;·&nbsp; do not open early — it only works once')}
"""

build([P1, P2], 'public/planning/sealed-page-worksheet.pdf')
