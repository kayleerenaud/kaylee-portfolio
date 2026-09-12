#!/usr/bin/env python3
"""DEVOTIONS — one passage per sheet. A reflection sheet for working through a book.

Two design commitments that shape everything:

  1. OBSERVATION IS PROTECTED. The sheet will not let you reach application until
     you have said what the text actually says. The most common failure in
     devotional journaling is skipping straight to "what does this mean to me,"
     and a worksheet is exactly the wrong place to make that easy.

  2. GENRE CHANGES THE QUESTIONS. A psalm is not asking to be obeyed the way a
     command is; a narrative is not always endorsing what it reports. The genre
     row near the top is not decoration — it tells you which questions apply.

There is also a section for the days when nothing lands. A sheet that cannot
record a dry day quietly teaches you to fake one.

    PYTHONPATH=/data/home/.local/lib/python3.12/site-packages \
      python3 scripts/build-devotions.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worksheet_kit import *

GENRES = ['narrative', 'law', 'psalm / poetry', 'wisdom', 'prophecy', 'gospel',
          'parable', 'epistle', 'apocalyptic', 'genealogy / list', 'song', 'prayer']

STORY = ['creation', 'the fall', 'Abraham', 'exodus', 'law &amp; covenant',
         'wilderness', 'the land', 'kings', 'prophets', 'exile', 'return',
         'the life of Christ', 'cross &amp; resurrection', 'the church', 'new creation']

P1 = f"""
{masthead('Devotions',
          'One passage per sheet. Stay in what it says before you ask what it means to you.',
          ['Date: ____________________',
           'Passage: ____________________',
           'Translation: ____________________'])}

{inline('Book', 'Where I am in it', 'How long I sat with it', 'Read it aloud? &nbsp; □')}

{h2(1, 'Before I read', 'Not to arrive calm — to notice what I brought, so I can tell it apart from what I find')}
{split(q('What I am carrying in — distracted, angry, numb, rushed, hopeful, nothing much:') + rules(1),
       q('A prayer before reading, one line:') + rules(1))}

{h2(2, 'What it actually says', 'Stay here longer than feels necessary. Everything below is only as good as this part.')}
{pick(GENRES, other='Or — what kind of writing is this?')}
{note('The genre decides which questions apply. A psalm is not asking to be obeyed the way a command is. '
      'A narrative is not always endorsing what it reports. Wisdom describes how things generally go, not '
      'what God has promised you personally. Read accordingly.')}
{q('Retell the passage in my own words, in three sentences. No interpretation yet — just what happens, or what is claimed.')}
{rules(3)}
{split(q('What repeats? What contrasts? Where does it turn — the <em>but</em>, <em>therefore</em>, <em>so that</em>, <em>because</em>?') + rules(2),
       q('What surprised me, or is not how I would have written it?') + rules(2))}
{q('What I do not understand. Leave it as a question — do not resolve it just to fill the line.')}
{rules(2)}

{h2(3, 'The ring around it', 'A verse lifted out of its paragraph will say almost anything you want')}
{split(q('What happens immediately before and after?') + rules(2),
       q('Who wrote it, to whom, and what were they actually dealing with?') + rules(2))}
{pick(STORY, other='Where this sits in the whole story')}
"""

P2 = f"""
{h2(4, 'What it shows about God', 'Before it is about me. This is the question that is easiest to skip.')}
{split(q('About God — Father, Son, Spirit. What is he like here? What does he do, want, refuse, promise?') + rules(3),
       q('About people, including me. What are we like here — and is the passage describing us or commanding us?') + rules(3))}
{q('Where is Christ in this passage — directly, by promise, by pattern, or by contrast? If the honest answer is &ldquo;not obviously,&rdquo; write that.')}
{rules(2)}

{h2(5, 'The verse I am taking with me')}
{linedbox(3, label='Reference: ____________________',
          note_='Write it out by hand. Copying is slower than reading, and that is the entire point.')}

{h2(6, 'What it asks of me', 'Not application in the abstract — a person, a place, and a week')}
{table(['What this asks of me', 'Where exactly — who, when, this week', 'By when', '✓'],
       3, ['34%','40%','18%','8%'], cls='tall')}
{split(q('What is the honest resistance? What here do I not want to do?') + rules(3),
       q('What would change this week if I actually believed this passage?') + rules(3))}

{h2(7, 'Prayer', 'Use the passage&rsquo;s own words where you can — it is better at this than I am')}
{table(['', 'In my own words', 'Words from the passage'], 0, ['16%','48%','36%'], cls='tall vgrid',
       rowlbls=['Adore', 'Confess', 'Thank', 'Ask'])}
{inline('Still praying for — and since when', 'Answered — and when')}

{h2(8, 'Honest, and unfinished', 'Dry days are not failed days. A sheet that cannot record one will teach me to fake it.')}
{q('If nothing landed today, say it plainly — what was it like to sit here anyway?')}
{rules(2)}
{table(['A question I am carrying', 'Where I might look — commentary, person, cross-reference', 'Asked?'],
       2, ['34%','52%','14%'])}
{split(q('One thing from this I want to tell someone this week — and who:') + rules(2),
       q('The thread so far — what has this book been doing across the last few sittings?') + rules(2))}
{h2(9, 'Next sitting', 'So the stack stays a book and not a pile of good mornings')}
{inline('Next passage', 'When', 'One thing to reread first')}
{foot('kayleerenaud.com &nbsp;·&nbsp; Devotions &nbsp;·&nbsp; one sheet per sitting &nbsp;·&nbsp; keep them in order and the book reads back')}
"""

build([P1, P2], 'public/planning/devotions-worksheet.pdf')
