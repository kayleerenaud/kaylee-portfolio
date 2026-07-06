// ============================================================================
//  WRITING — one piece per format. Each is a notebook "leaf": a tag, a title,
//  a one-line logline, a genre/audience line, and a doodle (drawn on scroll).
//  The logline opens to the full synopsis in the click-through overlay.
//  sketch: any name from the Sketch component's library
//          (e.g. clapper, spotlight, tv, book — or send your own line art).
// ============================================================================
export type Piece = {
  tag: string;
  title: string;
  logline: string;      // shown on the leaf; opens to the synopsis
  audience: string;     // one line: genre + who it's for (e.g. "Comedy for adults")
  synopsis: string;     // longer — shown in the click-through overlay
  sketch: string;
};

export const pieces: Piece[] = [
  {
    tag: 'Feature Film',
    title: 'India',
    logline:
      "In the wake of her father's early death, a young girl takes her goldfish where her father always promised to take her, The Grand Canyon, despite the pursuit of her tormented uncle and high-strung mother.",
    audience: 'Magical realism for adults',
    synopsis:
      "Flagstaff, Arizona, 2008. Eight-year-old India has just lost her father, and she is not taking it quietly. She is restless and stubborn and hungry for the kind of adventures he used to promise her, and her mom, Luciana, is too worn out to give her any. So India takes matters into her own small hands. Her pet goldfish has spent his entire life watching the world go by from a bowl on the dresser, and she decides he deserves to see something wonderful before it's too late. Destination: the Grand Canyon.\n\nShe sneaks onto a city bus with the fishbowl in her lap, and the farther she gets from home, the more the journey takes on the color of her imagination, until an ordinary runaway's bus trip starts to feel like the grand adventure she has always wanted. Along the way there are ghost towns, magic jelly beans, a candy man, and a boy named Rocket who is almost certainly lying about his name. Meanwhile Luciana and India's gentle, rattled uncle Marcello are chasing her across the state, each of them slowly learning how to love a person without holding on so tightly it hurts. India is a warm and funny film about grief and imagination, and about a little girl who just wants to give her goldfish, and herself, one real adventure.",
    sketch: 'goldfish',
  },
  {
    tag: 'Animated Pilot',
    title: 'Riftgard',
    logline:
      "A restless young goddess accidentally tears open the door between the gods' world and the mortal one, and now she has to sneak down to earth and wrangle a menagerie of runaway myths back home before anyone finds out.",
    audience: 'Animated fantasy-adventure for kids 7+ (TV-Y7-FV)',
    synopsis:
      "Princess Erika of Asgard has a real gift for trouble, happiest when she's smuggling a magical cow into the royal library. Her brother Jorunn is the responsible one, the future king everyone watches, which leaves Erika free to make all the mischief she likes. Then one kind impulse backfires. Slipping into the stables to send a captured mortal boy home, she cracks open a portal to the human world, and a whole menagerie of myths stampedes through after him. Suddenly the beasts of legend are loose on earth, it's her fault, and nobody will take her seriously enough to help. So she steps through the rift to fix it herself.\n\nRiftgard is an animated fantasy-adventure about a girl caught between two worlds and the mortals who just might become her truest friends.",
    sketch: 'dragon',
  },
];
