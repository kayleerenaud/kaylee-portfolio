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

export const pieces: Piece[] = [
  {
    tag: 'Feature Film',
    title: 'India',
    logline:
      "In the wake of her father's early death, a young girl takes her goldfish where her father always promised to take her, The Grand Canyon, despite the pursuit of her tormented uncle and high-strung mother.",
    teaser:
      "India is eight and full of plans. Her dad is gone, nobody has time to take her anywhere, and her goldfish has spent his whole life staring out a window, so she decides the two of them are long overdue for an adventure. She sets off across Arizona toward the Grand Canyon, and somewhere along the way the fish becomes a friend who walks and talks right beside her. Trailing behind are the two grown-ups who love her most, trying to catch up before she gets there.",
    synopsis:
      "Flagstaff, Arizona, 2008. Eight-year-old India has just lost her father, and she is not taking it quietly. She is restless and stubborn and hungry for the kind of adventures he used to promise her, and her mom, Luciana, is too worn out to give her any. So India takes matters into her own small hands. Her pet goldfish has spent his entire life watching the world go by from a bowl on the dresser, and she decides he deserves to see something wonderful before it's too late. Destination: the Grand Canyon.\n\nShe sneaks onto a city bus with the fishbowl in her lap, and as the miles roll by, her imagination fills in the rest. The goldfish becomes a companion, a man in shimmering gold who bickers and daydreams right alongside her, and who looks a little more like her father at every stop. Along the way there are ghost towns, magic jelly beans, a candy man, and a boy named Rocket who is almost certainly lying about his name. Meanwhile Luciana and India's gentle, rattled uncle Marcello are chasing her across the state, each of them slowly learning how to love a person without holding on so tightly it hurts. India is a warm and funny film about grief and imagination, and about a little girl who just wants to give her goldfish, and herself, one real adventure.",
    sketch: 'goldfish',
  },
];
