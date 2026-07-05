// ============================================================================
//  ABOUT PAGE CONTENT — all placeholder for now. Swap the text, photos, and
//  credits here; the layout + interactions pick them up automatically.
// ============================================================================

// The opening "title card" line (write like you talk — warm, a little intriguing).
export const hook = "Hi, I'm Kaylee — I make things that feel like a story.";

// Two short paragraphs. Personality first, credentials later.
// Wrap words in <em>…</em> to give them the handwritten emphasis font.
export const blurb: string[] = [
  "I plotted out my first play with untrained pointer fingers, clicking away slowly on the chunky keys of my family's PC. I must have been eight, certainly no younger than seven, and I had never seen a play let alone been trained to write one, but no one corrected me (or my spelling), so I let my imagination run wild. What began as a fantastical escape became my way of processing the world.",
  "Today, I'm a New York-based artist and writer drawn to character-driven stories and mixed media, with an enduring love of storytelling for young audiences. Across theater, marketing, live production, and wardrobe, I have contributed to two feature films, over twenty stage productions, and thirty short films. But whether I'm writing a script, sewing a costume, or framing a shot, it's the same work, and I'm glad you're here to see some of it.",
];

// Where you're based — shown as a filmic "on location" line in the title card.
export const basedIn = "New York, NY";

// Headshot frames — flips through these on load and lands on the LAST one.
// Kaylee's real photos; the file she marked "land_on_this" (pic4 → me-4) is last.
export const headshotFrames: string[] = [
  '/about/me-1.jpg',
  '/about/me-2.jpg',
  '/about/me-3.jpg',
  '/about/me-4.jpg',   // "land_on_this" — the frame it settles on
];

// The three crafts, each with a doodle motif + a link into that section.
export const crafts = [
  { label: 'Film',    sketch: 'clapper', href: '/film/',    blurb: "Documentary · Narrative · Children's media" },
  { label: 'Costume', sketch: 'mannequin', href: '/costume/', blurb: 'Research · Design · Illustration · Construction' },
  { label: 'Writing', sketch: 'quill',   href: '/writing/', blurb: 'Family-centered stories for stage & screen' },
];

// End credits — Awards / Experience / Education. Keep entries short and real;
// "Title — where, year" reads cleanly in the credit roll.
export const credits: { heading: string; sketch: string; entries: { title: string; detail?: string }[] }[] = [
  {
    heading: 'Awards & Selections',
    sketch: 'laurel',
    entries: [
      { title: "<em>Together, I'm Pieces</em> <span class='credit-role'>Director</span>", detail: 'Honorable Mention, Fusion Film Festival · Official Selection, WinterFest' },
      { title: "<em>Like Mother</em> <span class='credit-role'>Costume Designer</span>", detail: 'Official Selection, Manhattan & Fusion Film Festival' },
    ],
  },
  {
    heading: 'Selected Experience',
    sketch: 'summit',
    entries: [
      { title: 'Writer & Director', detail: "<em>Schmoopy</em>, <em>Elli</em>, <em>Spirit Temple No. 7</em>" },
      { title: 'Costume Designer', detail: '<em>Eurydice</em> (NYU Tisch ETW), <em>Weightless</em>' },
      { title: 'Costume Director', detail: '<em>Knights of the Old Republic</em>, Studio 70' },
      { title: 'Development Intern', detail: 'Jean Doumanian Productions, NYC' },
    ],
  },
  {
    heading: 'Education',
    sketch: 'gradcap',
    entries: [
      { title: 'BFA, Film & Television', detail: 'NYU Tisch School of the Arts · 2027' },
      { title: 'Additional Concentrations', detail: 'Costume Design & Dance' },
      { title: 'Developing the Dramatic Script', detail: 'Florence, Italy' },
      { title: 'Storytelling', detail: 'Athens, Greece' },
    ],
  },
];
