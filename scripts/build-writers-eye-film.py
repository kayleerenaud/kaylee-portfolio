#!/usr/bin/env python3
"""THE WRITER'S EYE — FILM. One page per film. Sibling of The Costume Eye.

Deliberately NOT a beat sheet. It never asks "where is the midpoint" — it asks
you to DESCRIBE the shape the film actually has, name the engine that kept you
watching, and test structure by irreversibility rather than by page count. The
shape list is a menu you tick from and can override, never a template to fill.

    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-writers-eye-film.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worksheet_kit import *

SHAPES = ['three-act', 'two-hander / duel', 'kishōtenketsu', 'jo-ha-kyū',
          'rival accounts (Rashomon)', 'braided ensemble', 'circular / return',
          'odyssey / picaresque', 'slice of life', 'mosaic of vignettes',
          'procedural', 'frame story', 'reverse chronology', 'daisy chain',
          'nested / recursive', 'one continuous day', 'drifting / plotless']

ENGINES = ['a question', 'a deadline', 'a want', 'a relationship', 'a mystery',
           'dread', 'the pleasure of company', 'a formal pattern', 'a voice',
           'a place', 'an argument', 'grief']

PAGE = f"""
{masthead('The Writer&rsquo;s Eye — Film',
          'Describe the shape it actually has. Do not check it against a template.',
          ['Watched: ____________________',
           'Where: ____________________',
           'First time? &nbsp; □ yes &nbsp; □ rewatch'])}

{inline('Film', 'Year', 'Written by', 'Directed by')}

{h2(1, 'After the fact', 'Write the logline you would write now, not the one on the poster')}
{rules(1)}
{split(q('The question the film is asking:') + rules(1),
       q('The answer it gives — or refuses to give:') + rules(1))}

{h2(2, 'The shape it actually has', 'Tick what fits, cross out what nearly fits, and write your own if none do')}
{pick(SHAPES, other='If none of these — describe the shape in your own words')}
{strip(10, label='Runtime — mark every turn you FELT, not every turn you can name',
       ticks=['start','10%','20%','30%','40%','50%','60%','70%','80%','end'], h='.36in')}
{table(['The turn', '≈ min', 'What became impossible to undo', 'Who caused it'],
       4, ['30%','8%','40%','22%'],
       head_note='The useful test is not act numbers — it is irreversibility. If nothing became '
                 'impossible to undo, it was an event, not a turn.')}

{h2(3, 'The engine', 'What actually kept me in the seat')}
{pick(ENGINES, other='Something else')}
{split(q('When did the engine change — and did I notice at the time?') + rules(1),
       q('What did the film promise in its first ten minutes?') + rules(1))}

{h2(4, 'People')}
{table(['Character', 'Wants', 'Needs (and does not know it)', 'Would never say out loud', 'Ends up'],
       3, ['16%','20%','24%','22%','18%'])}

{h2(5, 'One scene, taken apart', 'Pick the one you would show someone to explain the whole film')}
{inline('The scene', '≈ min', 'Power at the start', 'Power at the end')}
{split(q('What is the argument underneath the words? Nobody in a good scene is discussing what the scene is about.') + rules(3),
       q('Where does it start — how much did they trust us to skip? And how does it get out?') + rules(3))}
{q('What would be lost if it were cut entirely? If the answer is &ldquo;nothing much,&rdquo; say so — that is worth knowing too.')}
{rules(2)}

{h2(6, 'Language')}
{split(q('Three lines I would steal:') + rules(3),
       q('One line that did too much work — said out loud what the film had already shown:') + rules(1)
       + q('How does this dialogue differ from how people actually talk, and what does that buy?') + rules(2))}

{h2(7, 'Structure worth stealing', 'Move it from admiration into something I can use on a Tuesday')}
{table(['What they did', 'How it actually works', 'Where it fits in something of mine'],
       4, ['30%','36%','34%'], cls='tall')}

{h2(8, 'If I were rewriting it')}
{split(q('Where it lost me — and would I have solved that problem the same way?') + rules(3),
       q('What is the film secretly about, underneath what it says it is about?') + rules(3))}
{q('What would this be in another form — a pilot, a short story, a play, a half-hour? What breaks, and what gets better?')}
{rules(2)}

{h2(9, 'What this sends me to next')}
{table(['Title', 'Why — what I want to watch them do', '✓'], 3, ['32%','58%','10%'])}
{split(q('If I could ask the writer one question:') + rules(2),
       q('And one for the costume designer — cross-reference the other sheet:') + rules(2))}

{pick(['steal', 'study', 'avoid'], label='Verdict')}
{q('The one thing I am taking into my own pages:')}
{rules(1)}
{foot('kayleerenaud.com &nbsp;·&nbsp; The Writer&rsquo;s Eye: Film &nbsp;·&nbsp; prints front and back on one sheet &nbsp;·&nbsp; sibling: The Costume Eye')}
"""

build([PAGE], 'public/planning/writers-eye-film-worksheet.pdf')
