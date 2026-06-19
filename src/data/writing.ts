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
  teaser: string;
  sketch: string;
};

export const pieces: Piece[] = [
  {
    tag: 'Film',
    title: 'Untitled Film',
    logline: 'Logline — one vivid sentence that promises the whole movie.',
    teaser:
      'A short teaser paragraph lives here — a taste of the world, the voice, and the heart of it, without giving the ending away. Two or three sentences is plenty. Replace with the real thing.',
    sketch: 'clapper',
  },
  {
    tag: 'Stage',
    title: 'Untitled Play',
    logline: 'Logline — the play in a single, intriguing breath.',
    teaser:
      'A short teaser paragraph for the stage piece. Set the room, the tension, the question the audience leans toward. Keep it warm and specific. Placeholder copy for now.',
    sketch: 'spotlight',
  },
  {
    tag: 'Pilot',
    title: 'Untitled Pilot',
    logline: 'Logline — the series engine in one line.',
    teaser:
      'A short teaser paragraph for the TV pilot — who we follow, the world they move through, and why we would tune in next week. Placeholder until the real logline + teaser arrive.',
    sketch: 'tv',
  },
  {
    tag: 'Prose',
    title: 'Untitled Story',
    logline: 'Logline — the short story or book, distilled to a sentence.',
    teaser:
      'A short teaser paragraph for the prose piece. A line or two of the actual voice can shine here — let the reader hear how you write. Placeholder text for now.',
    sketch: 'book',
  },
];
