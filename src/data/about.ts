// ============================================================================
//  ABOUT PAGE CONTENT — all placeholder for now. Swap the text, photos, and
//  credits here; the layout + interactions pick them up automatically.
// ============================================================================

// The opening "title card" line (write like you talk — warm, a little intriguing).
export const hook = "Hi, I'm Kaylee — I make things that feel like a story.";

// Two short paragraphs. Personality first, credentials later.
export const blurb: string[] = [
  "Lorem ipsum — I'm a multi-faceted artist working across film, costume, and writing. I'm happiest somewhere between a sewing table, a viewfinder, and a half-filled notebook, chasing the moment a small idea turns into a whole little world.",
  "Lorem ipsum — I'm especially drawn to stories made for kids: the warmth, the wonder, the permission to be playful. Whether I'm stitching a costume, framing a shot, or writing a scene, I'm really doing the same thing — building somewhere you'd want to spend an afternoon.",
];

// Where you're based (a map-pin doodle draws itself next to this).
export const basedIn = "Based in Los Angeles, California";

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
export const credits: { heading: string; lines: string[] }[] = [
  {
    heading: 'Awards',
    lines: [
      'Best Short Film — Placeholder Festival, 2024',
      'Costume Design, Honorable Mention — Placeholder Awards, 2023',
      'Emerging Artist Grant — Placeholder Foundation, 2022',
    ],
  },
  {
    heading: 'Selected Experience',
    lines: [
      'Costume Designer — Placeholder Production, 2023–24',
      'Writer / Director — "Placeholder" (short), 2023',
      'Wardrobe & Story Dept. — Placeholder Studio, 2021–22',
    ],
  },
  {
    heading: 'Education',
    lines: [
      'BFA, Film & Media — Placeholder University, 2022',
      'Costume Construction — Placeholder Workshop, 2021',
    ],
  },
];
