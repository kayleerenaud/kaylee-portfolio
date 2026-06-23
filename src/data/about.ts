// ============================================================================
//  ABOUT PAGE CONTENT — all placeholder for now. Swap the text, photos, and
//  credits here; the layout + interactions pick them up automatically.
// ============================================================================

// The opening "title card" line (write like you talk — warm, a little intriguing).
export const hook = "Hi, I'm Kaylee — I make things that feel like a story.";

// Two short paragraphs. Personality first, credentials later.
// Wrap words in <em>…</em> to give them the handwritten emphasis font.
export const blurb: string[] = [
  "I've been writing since before I could properly type, filling a purple notebook with wolf princesses and children who lived in tunnels beneath the dry South Jersey lawns. That notebook eventually made room for a viewfinder and a sewing table, but the instinct never changed: I build worlds, and I try to make them places worth staying.",
  "I work mostly for kids and families, not because it's easier but because I remember needing stories that trusted me. I grew up moving between two very different households, leaning on the heroes I found in books and films to carry me from one to the other. Children can hold grief and wonder in the same frame without needing it explained, and that is who I make things for: my younger self, my younger siblings and cousins, and the grown-ups who still remember being that kid. Whether I'm writing a script, sewing a costume, or framing a shot, it's the same work, and I'm glad you're here to see some of it.",
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
  { label: 'Film',    sketch: 'clapper', href: '/film/',    blurb: "Documentary · Narrative · Children's media" },
  { label: 'Costume', sketch: 'mannequin', href: '/costume/', blurb: 'Research · Design · Illustration · Construction' },
  { label: 'Writing', sketch: 'quill',   href: '/writing/', blurb: 'Family-centered stories for stage & screen' },
];

// End credits — Awards / Experience / Education. Keep entries short and real;
// "Title — where, year" reads cleanly in the credit roll.
export const credits: { heading: string; sketch: string; lines: string[] }[] = [
  {
    heading: 'Awards & Selections',
    sketch: 'laurel',
    lines: [
      "<em>Together, I'm Pieces</em>",
      "Honorable Mention, Fusion Film Festival · Official Selection, WinterFest",
      "<em>Like Mother</em>",
      "Official Selection, Manhattan & Fusion Festivals",
    ],
  },
  {
    heading: 'Selected Experience',
    sketch: 'summit',
    lines: [
      "Writer & Director · <em>Schmoopy</em>, <em>Together, I'm Pieces</em>, <em>Spirit Temple No. 7</em>",
      "Costume Designer · <em>Eurydice</em> (NYU Tisch ETW), <em>Weightless</em>",
      "Costume Director · <em>Knights of the Old Republic</em>, Studio 70",
      "Development Intern · Jean Doumanian Productions, NYC",
    ],
  },
  {
    heading: 'Education',
    sketch: 'gradcap',
    lines: [
      "BFA, Film & Television · NYU Tisch School of the Arts, 2027",
      "Additional Concentrations · Costume Design & Dance",
      "Developing the Dramatic Script · Florence, Italy",
      "Storytelling · Athens, Greece",
    ],
  },
];
