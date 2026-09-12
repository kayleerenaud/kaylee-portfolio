#!/usr/bin/env python3
"""THE WRITER'S EYE — EPISODE. One sheet per episode of television.

Not the film sheet with the word "film" swapped out. An episode has to work as
a unit and as a link in a chain, so this sheet asks different questions: what
machine generates episodes of this show, what job THIS one is doing, how the
strands touch, what the series refuses to let change, and — the honest one for
serialized TV — whether anything actually moved or the week was just occupied.

Act-structure questions are written to survive streaming shows that have no act
breaks: mark where the pressure rises and falls instead.

    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-writers-eye-episode.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worksheet_kit import *

JOBS = ['pilot', 'standalone / case of the week', 'mythology advance', 'bottle',
        'flashback / origin', 'character showcase', 'one-location farce',
        'table-setting', 'penultimate escalation', 'finale', 'reset',
        'crossover', 'format break', 'holiday / detour', 'premiere re-pilot']

SHAPES = ['escalating farce', 'slow burn', 'parallel rhyme', 'frame story', 'real time',
          'flashback braid', 'vignettes', 'circular', 'procedural A→Z', 'two-hander',
          'ensemble split', 'countdown']

P1 = f"""
{masthead('The Writer&rsquo;s Eye — Episode',
          'An episode has to work twice: as one unit, and as one link. Read it both ways.',
          ['Watched: ____________________',
           'Where: ____________________',
           'First time? &nbsp; □ yes &nbsp; □ rewatch'])}

{inline('Show', 'Season &amp; episode', 'Episode title', 'Written by')}
{inline('Directed by', 'Runtime', 'Where in the season', 'Network / platform')}

{h2(1, 'The machine', 'Before this episode — what makes a NEW episode of this show possible every week?')}
{rules(1)}
{split(q('What does every episode of this show owe the viewer, no matter what?') + rules(2),
       q('What does this show do that no other show would do with the same premise?') + rules(2))}

{h2(2, 'What job this episode is doing')}
{pick(JOBS, other='If it is doing several — which is it really doing?')}
{split(q('If someone skipped this episode, what exactly would they miss?') + rules(2),
       q('Could this have been the cold open of the next one instead? Be honest.') + rules(2))}

{h2(3, 'The strands', 'A, B, C and the runner — and whether they are actually about the same thing')}
{table(['', 'Whose it is', 'What happens', 'How it rhymes with A', 'Resolved / carried'],
       0, ['10%','16%','30%','28%','16%'], cls='tall',
       rowlbls=['A story', 'B story', 'C story', 'Runner / gag'])}
{split(q('Where do the strands touch — do they collide, or just alternate?') + rules(2),
       q('Which strand is the episode <em>actually</em> about?') + rules(2))}

{h2(4, 'Shape &amp; breaks')}
{note('Streaming shows often have no act breaks at all. If this one does not, mark where the pressure '
      'rises and falls anyway — the shape is there whether or not anyone sold advertising against it.')}
{strip(8, label='Cold open · act-outs · tag — or where I would have put them',
       ticks=['cold open','','','','','','','tag'], h='.36in')}
{pick(SHAPES, other='Or describe the shape in my own words')}
{table(['Break / turn', '≈ min', 'The hook on the way out', 'Did it earn the return?'],
       3, ['26%','8%','42%','24%'])}
"""

P2 = f"""
{h2(5, 'The serialization ledger', 'The honest question: did anything move, or was the week merely occupied?')}
{table(['Thread', 'Where it stood at the top', 'Where it stands at the end', 'How far did it really move?', 'Could it have waited?'],
       4, ['20%','22%','22%','20%','16%'], cls='tall')}

{h2(6, 'Character, in a small unit', 'A week is not much room — which is what makes it a good test')}
{table(['Character', 'What they wanted this week', 'What it cost them', 'Changed · or series-locked'],
       3, ['18%','30%','28%','24%'], cls='tall')}
{split(q('What is this show refusing to let change — and is that a strength or a cage?') + rules(2),
       q('Who got the least screen time, and did the episode miss them?') + rules(2))}

{h2(7, 'The rules of the show', 'Every show teaches you its laws in the first ten minutes and then lives by them')}
{table(['', 'The rule', 'Broken this week?', 'If so — did breaking it work?'],
       0, ['12%','40%','18%','30%'],
       rowlbls=['Rule 1', 'Rule 2', 'Rule 3'])}

{h2(8, 'Economy', 'Twenty-two minutes or fifty-eight, somebody fought over every one of them')}
{split(q('What earned its minutes:') + rules(2),
       q('What I would cut, and what I would spend the time on instead:') + rules(2))}

{h2(9, 'If I were in that room')}
{split(q('Pitch the next episode in one line:') + rules(2),
       q('The episode I would write for this show — and which character it belongs to:') + rules(2))}
{q('What would I put on the board for the end of this season?')}
{rules(1)}

{h2(10, 'Craft worth stealing')}
{table(['What they did', 'How it actually works', 'Where it fits in something of mine'],
       2, ['30%','36%','34%'], cls='tall')}

{pick(['steal', 'study', 'avoid'], label='Verdict')}
{q('The one thing I am taking into my own pages:')}
{rules(1)}
{foot('kayleerenaud.com &nbsp;·&nbsp; The Writer&rsquo;s Eye: Episode &nbsp;·&nbsp; prints front and back on one sheet &nbsp;·&nbsp; siblings: Film, The Costume Eye')}
"""

build([P1, P2], 'public/planning/writers-eye-episode-worksheet.pdf')
