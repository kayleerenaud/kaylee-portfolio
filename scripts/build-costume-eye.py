#!/usr/bin/env python3
"""THE COSTUME EYE — a one-page watching log, one sheet per film.

Print twenty and keep them by the couch. The point is not to review the film;
it is to build the habit of reading costume as story before the dialogue does
the work. Follows public/planning/worksheet-format-spec.md.

    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-costume-eye.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worksheet_kit import *

PAGE = f"""
{masthead('The Costume Eye',
          'One film per sheet. Read the clothes as story — not as shopping.',
          ['Watched: ____________________',
           'Where: ____________________',
           'First time? &nbsp; □ yes &nbsp; □ rewatch'])}

{inline('Film', 'Year', 'Director', 'Costume designer')}

{h2(1, 'The palette', 'Fill each box with pencil or paint, then name where it lives in the film')}
{swatches(6, h='.44in')}
{q('Which colour belongs to whom — and what happens the first time someone wears somebody else&rsquo;s?')}
{rules(1)}

{h2(2, 'What the clothes said before anyone spoke')}
<table class='tall'>
  <thead><tr>
    <th style='width:15%'>Character</th>
    <th style='width:20%'>Silhouette &amp; line</th>
    <th style='width:14%'>Palette</th>
    <th style='width:21%'>Fabric, weight, texture</th>
    <th style='width:30%'>What it reveals — and hides</th>
  </tr></thead>
  <tbody>
    <tr><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td><td></td><td></td></tr>
  </tbody>
</table>

{h2(3, 'What changed, and what refused to')}
{table(['Scene or beat', 'What changed on the body', 'The story reason for it'],
       3, ['26%','34%','40%'])}
{split(q('Who changes the <em>least</em>? What is that stillness doing?') + rules(1),
       q('A garment that outlives its owner — passed on, borrowed, stolen, inherited?') + rules(1))}

{h2(4, 'Craft &amp; money', 'Every costume department is solving a budget in public')}
{table(['', 'What I actually saw', 'Would I have solved it that way?'],
       0, ['25%','45%','30%'], cls='tall',
       rowlbls=['Where the money went',
                'Where they hid that it didn&rsquo;t — repeats, doubles, backs never seen',
                'Ageing, dyeing, breakdown — what was done to the cloth',
                'Period as researched, or period as remembered?'])}

{h2(5, 'The one garment I would steal')}
{split(sketch('1.0in', 'Sketch it'),
       q('What it is, and why it works:') + rules(2)
       + q('The one thing I would have done differently in this whole film:') + rules(1))}

{pick(['steal', 'study', 'avoid'], label='Verdict — this film goes in the')}
{q('One sentence I want to carry into my own work:')}
{rules(1)}
{foot('kayleerenaud.com &nbsp;·&nbsp; The Costume Eye &nbsp;·&nbsp; print more when you run out')}
"""

build([PAGE], 'public/planning/costume-eye-worksheet.pdf')
