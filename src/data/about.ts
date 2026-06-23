// ============================================================================
//  ABOUT PAGE CONTENT — all placeholder for now. Swap the text, photos, and
//  credits here; the layout + interactions pick them up automatically.
// ============================================================================

// The opening "title card" line (write like you talk — warm, a little intriguing).
export const hook = "Hi, I'm Kaylee — I make things that feel like a story.";

// Two short paragraphs. Personality first, credentials later.
// Wrap words in <em>…</em> to give them the handwritten emphasis font.
export const blurb: string[] = [
  "I've been a writer since before I could really type, back when I filled a <em>purple notebook</em> with wolf princesses and kids who lived in tunnels under the dry South Jersey lawns. The notebook eventually made room for a viewfinder and a sewing table, but it's all the same instinct: build a world, then make it somewhere worth staying.",
  "I make things mostly for kids and families, not because it's easier but because I remember needing stories that <em>trusted me</em>. I grew up between a houseful of siblings at my mom and stepdad's and an only-child life at my dad's, and I needed heroes to get me from one to the other. Kids can hold <em>grief and wonder</em> in the same frame without anyone explaining it to them, so that's who I make things for: my younger self, my siblings and little cousins, and the occasional grown-up who still remembers.",
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
      "<em>Together, I'm Pieces</em> · Honorable Mention, Fusion Film Festival · Official Selection, WinterFest",
      "<em>Like Mother</em> · Official Selection, Manhattan & Fusion Film Festivals",
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
