// ============================================================================
//  ABOUT PAGE CONTENT — all placeholder for now. Swap the text, photos, and
//  credits here; the layout + interactions pick them up automatically.
// ============================================================================

// The opening "title card" line (write like you talk — warm, a little intriguing).
export const hook = "Hi, I'm Kaylee — I make things that feel like a story.";

// Two short paragraphs. Personality first, credentials later.
// Wrap words in <em>…</em> to give them the handwritten emphasis font.
export const blurb: string[] = [
  "I'm a Brooklyn-based storyteller trained at NYU's Tisch School of the Arts, drawn to character-driven narratives and with an enduring love of creating for young audiences. I've contributed to two feature films (with a third in production), over thirty short films, and more than twenty stage productions, across film, theater, live production, and wardrobe.",
  "I'm a genre-hopping, formally playful artist who weaves handmade touches into intimate pieces. My training in film production, screenwriting, dance, and costume design shapes the holistic way I approach both my work and my collaborations.",
];

// Where you're based — shown as a filmic "on location" line in the title card.
export const basedIn = "Brooklyn, NY";

// Headshot frames — flips through these on load and lands on the LAST one.
// Candid lead-ins (in Kaylee's order), settling on the pro headshot.
export const headshotFrames: string[] = [
  '/about/lead-3.jpg',
  '/about/lead-4.jpg',
  '/about/lead-5.jpg',
  '/about/me-4.jpg',   // pro headshot — the frame it settles on
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
      { title: 'Costume Designer', detail: '<em>Eurydice</em> (NYU Tisch ETW), <em>Be All End All</em> (Playwrights Horizons), <em>Weightless</em>' },
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
