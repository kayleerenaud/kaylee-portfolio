// ============================================================================
//  ABOUT PAGE CONTENT — all placeholder for now. Swap the text, photos, and
//  credits here; the layout + interactions pick them up automatically.
// ============================================================================

// The opening "title card" line (write like you talk — warm, a little intriguing).
export const hook = "Hi, I'm Kaylee — I make things that feel like a story.";

// Two short paragraphs. Personality first, credentials later.
// Wrap words in <em>…</em> to give them the handwritten emphasis font.
export const blurb: string[] = [
  "Lorem ipsum — I'm a <em>multi-faceted artist</em> working across film, costume, and writing. I'm happiest somewhere between a sewing table, a viewfinder, and a half-filled notebook, chasing the moment a small idea turns into a <em>whole little world</em>.",
  "Lorem ipsum — I'm especially drawn to <em>stories made for kids</em>: the warmth, the wonder, the permission to be playful. Whether I'm stitching a costume, framing a shot, or writing a scene, I'm really doing the same thing — building somewhere you'd <em>want to spend an afternoon</em>.",
];

// Where you're based — shown as a filmic "on location" line in the title card.
export const basedIn = "New York, NY";

// Headshot frames — flips through these on load and lands on the LAST one
// (your professional shot). Replace with 4 real photos. Square-ish works best.
const me = (seed: string) => `https://picsum.photos/seed/${seed}/640/720`;
export const headshotFrames: string[] = [
  me('kr-me-laugh'),   // laughing
  me('kr-me-smile'),   // soft smile
  me('kr-me-tongue'),  // tongue out / playful
  me('kr-me-pro'),     // professional — lands here
];

// The three crafts, each with a doodle motif + a link into that section.
export const crafts = [
  { label: 'Film',    sketch: 'clapper', href: '/film/',    blurb: 'Moving pictures and the frames behind them.' },
  { label: 'Costume', sketch: 'thread',  href: '/costume/', blurb: 'Worlds you can wear, made by hand.' },
  { label: 'Writing', sketch: 'quill',   href: '/writing/', blurb: 'Words, scenes, and small wonders.' },
];

// End credits — Awards / Experience / Education. Keep entries short and real;
// "Title — where, year" reads cleanly in the credit roll.
export const credits: { heading: string; sketch: string; lines: string[] }[] = [
  {
    heading: 'Awards',
    sketch: 'laurel',
    lines: [
      'Best Short Film — Placeholder Festival, 2024',
      'Costume Design, Honorable Mention — Placeholder Awards, 2023',
      'Emerging Artist Grant — Placeholder Foundation, 2022',
    ],
  },
  {
    heading: 'Selected Experience',
    sketch: 'summit',
    lines: [
      'Costume Designer — Placeholder Production, 2023–24',
      'Writer / Director — "Placeholder" (short), 2023',
      'Wardrobe & Story Dept. — Placeholder Studio, 2021–22',
    ],
  },
  {
    heading: 'Education',
    sketch: 'gradcap',
    lines: [
      'BFA, Film & Media — Placeholder University, 2022',
      'Costume Construction — Placeholder Workshop, 2021',
    ],
  },
];
