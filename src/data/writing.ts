// ============================================================================
//  WRITING — one piece per format. Each is a notebook "leaf": a tag, a title,
//  a one-line logline, a short teaser, and a doodle (drawn on scroll) evocative
//  of the story. Swap the placeholder copy + doodle names for the real pieces.
//  sketch: any name from the Sketch component's library
//          (e.g. clapper, spotlight, tv, book — or send your own line art).
// ============================================================================
export type Piece = {
  tag: string;
  title: string;
  logline: string;
  teaser: string;      // short — shown on the notebook page
  synopsis: string;    // longer — shown in the click-through overlay
  sketch: string;
};

const ph =
  'Full synopsis goes here. A few paragraphs that walk through the world, the characters, and the emotional arc without spoiling the ending — the version you would hand a producer or a director. Replace this placeholder with the real synopsis.\n\nA second paragraph can carry the themes, the tone, and what makes it unmistakably yours. The drawing to the side acts as the script’s cover illustration.';

export const pieces: Piece[] = [
  {
    tag: 'Film',
    title: 'Untitled Film',
    logline: 'Logline — one vivid sentence that promises the whole movie.',
    teaser:
      'A short teaser paragraph lives here — a taste of the world, the voice, and the heart of it, without giving the ending away. Two or three sentences is plenty.',
    synopsis: ph,
    sketch: 'clapper',
  },
  {
    tag: 'Stage',
    title: 'Untitled Play',
    logline: 'Logline — the play in a single, intriguing breath.',
    teaser:
      'A short teaser paragraph for the stage piece. Set the room, the tension, the question the audience leans toward. Keep it warm and specific.',
    synopsis: ph,
    sketch: 'mask',
  },
  {
    tag: 'Pilot',
    title: 'Untitled Pilot',
    logline: 'Logline — the series engine in one line.',
    teaser:
      'A short teaser paragraph for the TV pilot — who we follow, the world they move through, and why we would tune in next week.',
    synopsis: ph,
    sketch: 'tv',
  },
  {
    tag: 'Prose',
    title: 'Untitled Story',
    logline: 'Logline — the short story or book, distilled to a sentence.',
    teaser:
      'A short teaser paragraph for the prose piece. A line or two of the actual voice can shine here — let the reader hear how you write.',
    synopsis: ph,
    sketch: 'book',
  },
];
