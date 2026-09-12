#!/usr/bin/env python3
"""STORY PLANNING — for a story that does not exist yet, or one that is refusing to work.

Form-agnostic on purpose: feature, pilot, short, short story, novel, play. It
tests structure by IRREVERSIBILITY rather than by act numbers, asks you to draw
the shape before naming it, and includes a design column no other story
worksheet has — because the person filling it in dresses characters for a
living and wardrobe is the fastest character document there is.

    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-story-planning.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worksheet_kit import *

FORMS = ['feature', 'TV pilot — half hour', 'TV pilot — hour', 'limited series',
         'short film', 'short story', 'novel', 'play', 'comic', 'audio']

SHAPES = ['three-act', 'kishōtenketsu', 'jo-ha-kyū', 'two-hander / duel',
          'rival accounts', 'braided ensemble', 'circular / return', 'odyssey',
          'slice of life', 'mosaic of vignettes', 'frame story', 'reverse chronology',
          'daisy chain', 'nested', 'one continuous day', 'procedural', 'drifting']

P1 = f"""
{masthead('Story Planning',
          'For a story that does not exist yet — or one that is refusing to work. Answer badly first.',
          ['Working title: ____________________',
           'Draft: __________ &nbsp; Date: __________',
           'Kaylee Renaud'])}

{h2(1, 'The form', 'Decide this early — it changes every other answer on the sheet')}
{pick(FORMS, other='Something else — name it')}
{split(q('Why this form and not the one next to it? What can it do that the others cannot?') + rules(2),
       q('Target length, and the closest thing to it that already exists:') + rules(2))}

{h2(2, 'The seed', 'Do not make it sound good yet. Making it sound good is how ideas get lost.')}
{split(q('The image, line, or moment that will not leave me alone:') + rules(3),
       q('Where it came from — and what I am actually trying to work out by writing it:') + rules(3))}
{q('Now say what it is about <em>badly</em>, in one ugly sentence. Leave the ugly sentence on the page.')}
{rules(2)}

{h2(3, 'The ladder', 'Same story at five altitudes. If two rungs disagree, that is the note.')}
{table(['', 'Written out', 'Does it match the rung above?'], 0, ['24%','54%','22%'], cls='taller',
       rowlbls=['One sentence',
                'One paragraph',
                'The question it asks',
                'The argument it makes',
                'The promise of the genre — what does someone expect walking in?'])}

{h2(4, 'Whose story is it?', 'The test: take each one out. Whose story is still standing?')}
{table(['Character', 'Wants (says out loud)', 'Needs (does not know)', 'Would never do', 'Does it anyway when…', 'What it costs'],
       5, ['14%','18%','18%','16%','18%','16%'], cls='tall')}
"""

P2 = f"""
{h2(5, 'The shape', 'Draw it before you name it. The name is only useful if the drawing came first.')}
{split(sketch('1.7in', 'Draw the shape of the story — a line, a spiral, a braid, a circle, a staircase'),
       note('Tick anything that fits what you drew. Cross out what nearly fits. If nothing does, the '
            'sheet is wrong and the drawing is right — describe it in your own words instead.')
       + pick(SHAPES, other='In my own words'))}

{h2(6, 'Turns, by what cannot be undone', 'Not act breaks — irreversibility. That is the only structural test that survives every form.')}
{note('If nothing became impossible to undo, it was an event, not a turn. A story with two real turns and '
      'six events is the most common thing wrong with a draft.')}
{table(['#', 'Roughly where', 'What happens', 'What can never be undone after this', 'Who caused it'],
       7, ['5%','15%','30%','32%','18%'])}
{split(q('Which turn am I least sure of — and what am I avoiding by leaving it vague?') + rules(2),
       q('Which turn happens <em>to</em> the protagonist rather than <em>because</em> of them? Is that a problem?') + rules(2))}

{h2(7, 'Promises &amp; payoffs', 'The first tenth of anything is a contract')}
{table(['The promise made early', 'Where it is paid', 'Paid · subverted · dropped'],
       5, ['40%','36%','24%'])}

{h2(8, 'The ending, written now', 'Even if it changes. Especially if it changes.')}
{split(q('The last image or last line, written today:') + rules(4),
       q('The second-to-last beat — the one that makes the last one land:') + rules(4))}
{q('Does the opening promise this ending? If not, which of the two is wrong — and which am I more attached to?')}
{rules(2)}
"""

P3 = f"""
{h2(9, 'The world and its rules')}
{table(['', 'The rule', 'What it costs to break it', 'Who breaks it, and when'],
       0, ['12%','34%','26%','28%'], cls='tall',
       rowlbls=['Rule 1', 'Rule 2', 'Rule 3'])}
{split(q('What does this world let me say that the real one will not?') + rules(2),
       q('What is ordinary here that would be strange to us — and how do I show it without explaining it?') + rules(2))}

{h2(10, 'What the story believes', 'Theme, without being embarrassed about it')}
{split(q('What the story believes, in plain words:') + rules(2)
       + q('Who carries that belief — and do they know they are carrying it?') + rules(2),
       q('The strongest possible case for the opposite:') + rules(2)
       + q('Who carries <em>that</em> — and honestly, are they a straw man?') + rules(2))}

{h2(11, 'The design column', 'You dress people for a living. Put it in the outline, not the prep.')}
{note('Wardrobe is the fastest character document there is — it says want, class, era, self-image and '
      'self-deception before a line of dialogue. Writing it now will change the scenes you plan.')}
{table(['Character', 'First look', 'Last look', 'What changed — and the moment the audience notices'],
       4, ['16%','24%','24%','36%'], cls='tall')}
{swatches(6, caption='The palette of the whole thing — fill each box, then name it', h='.44in')}
{split(q('The one image this whole story is built around:') + rules(2),
       q('What does the audience see before anyone says anything?') + rules(2))}

{h2(12, 'What I need to know', 'Research, but only the kind that changes a scene')}
{table(['What I need to know', 'Who or what would tell me', 'By when', '✓'],
       4, ['36%','38%','18%','8%'])}
"""

P4 = f"""
{keep(h2(13, 'The ladder of scenes', 'One row per scene or sequence. The last column is the honest one.')
     + note('Fill the middle columns fast and the last column slowly. Any row where the honest answer to '
            '&ldquo;why can it not be cut&rdquo; is &ldquo;because I like it&rdquo; is a row to look at twice.')
     + table(['#', 'Where / when', 'Who', 'What happens', 'What CHANGES', 'Why it cannot be cut'],
             20, ['4%','16%','14%','26%','22%','18%']))}

{h2(14, 'What I already know is broken', 'Park it here. Do not fix it now — naming it is the whole job today.')}
{rules(4)}

{h2(15, 'The next fourteen days', 'A plan that ends here is a daydream with a table')}
{table(['I will…', 'By (date)', 'Who knows I said so'], 3, ['56%','20%','24%'])}
{foot('kayleerenaud.com &nbsp;·&nbsp; Story Planning &nbsp;·&nbsp; companion sheets: The Writer&rsquo;s Eye (Film · Episode), The Costume Eye')}
"""

build([P1, P2, P3, P4], 'public/planning/story-planning-worksheet.pdf')
