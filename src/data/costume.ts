// ============================================================================
//  COSTUME CONTENT — projects shown as "oak tags" on a rail. Clicking a tag
//  opens an in-page plate overlay (✕ to close) with each piece's imagery + note.
//
//  Each Project = one production (or paper project). Each Piece is a costume
//  "look" with whatever images exist:
//     name?      short heading over the plate (character / look name)
//     final?     finished costume photo  (omit for paper / unrealized projects)
//     closeups?  detail shots of the final
//     photos?    extra finished photos beside the final
//     rendering? the design illustration
//     renderings? extra renderings shown in the same plate
//     technicals? design / technical sheets
//     progress?  in-progress / construction photos
//     swatches?  fabric swatches
//     caption?   the written note that travels with the piece (preview → full)
//
//  kind: 'realized' = has production photos; 'paper' = design-only (renderings).
// ============================================================================

export type Piece = {
  name?: string;           // short heading over the plate (character / look name)
  caption?: string;
  final?: string;
  rendering?: string;
  renderings?: string[];   // extra renderings shown in the same plate
  technicals?: string[];   // design/technical sheets that pair with the final
  progress?: string[];
  swatches?: string[];
  photos?: string[];       // extra finished photos (shown beside the final)
  closeups?: string[];     // detail / close-up shots of the final
};

export type Project = {
  id: string;
  show: string;        // production name (handwritten on the tag)
  company: string;     // producing company
  director: string;
  role: string;        // your role / credit
  year: string;
  kind: 'realized' | 'paper';
  blurb?: string;
  pieces: Piece[];
};

// image path helper — files live in /public/costume/<id>/<file>.jpg
const im = (id: string, file: string) => `/costume/${id}/${file}.jpg`;

export const projects: Project[] = [
  // ---- Knights of the Old Republic — Studio 70 (realized) ------------------
  {
    id: 'kotor',
    show: 'Knights of the Old Republic', company: 'Studio 70', director: 'Austin Parenti', role: 'Costume Director', year: '2025–Present', kind: 'realized',
    blurb: 'Knights of the Old Republic is a fan-made feature film trilogy.',
    pieces: [
      // two Tusken Raider photos: wide full-body main + "Close Up" thumbnail
      { name: 'Tusken Raiders', caption: 'Boots and accessories designed and crafted by Kaylee Renaud.',
        final: im('kotor', 'look-2'), closeups: [im('kotor', 'cover')] },
      // The Engineer: lightsaber-standing final + its technical drawing
      { name: 'The Engineer',
        final: im('kotor', 'look-1'), technicals: [im('kotor', 'look-3')] },
      // Eli: bug-helmet final + its technical drawing
      { name: 'Eli', caption: 'Designed by Kaylee Renaud. Silicon pieces crafted by Walter Welsh.',
        final: im('kotor', 'look-7'), technicals: [im('kotor', 'look-4')] },
      // Lena technical drawing
      { name: 'Lena', caption: 'Designed by Kaylee Renaud, crafted by Marie Cosplay Shop.',
        technicals: [im('kotor', 'look-6')] },
      // Griff Vao technical drawing
      { name: 'Griff Vao',
        technicals: [im('kotor', 'griff-vao')] },
    ],
  },

  // ---- As You Like It — NYU Classical Studio (realized) --------------------
  {
    id: 'as-you-like-it',
    show: 'As You Like It', company: 'NYU Classical Studio', director: 'Daniel Spector', role: 'Associate Designer', year: '2026', kind: 'realized',
    blurb: 'As You Like It was performed in the round by fourteen players, who took on different roles each night.',
    pieces: [
      { final: im('as-you-like-it', 'cover') },                 // *_COVER → card cover
      { final: im('as-you-like-it', 'look-1') },
      { final: im('as-you-like-it', 'look-2') },
      { final: im('as-you-like-it', 'look-3') },
      { final: im('as-you-like-it', 'look-4') },
      { final: im('as-you-like-it', 'look-5') },
      { final: im('as-you-like-it', 'look-6') },
      { final: im('as-you-like-it', 'look-7') },
    ],
  },

  // ---- Peter and the Starcatcher — paper (renderings) ----------------------
  {
    id: 'peter-starcatcher',
    show: 'Peter and the Starcatcher', company: 'Costume Design III', director: '', role: 'Costume Designer', year: '2025', kind: 'paper',
    blurb: "A final project for Costume Design III, under the instruction of Orla Long. I've been in love with the play Peter and the Starcatcher by Rick Elice for years now, and this was my chance to bring it to life on paper!",
    pieces: [
      { rendering: im('peter-starcatcher', 'teacher') },   // *_COVER → card cover
      { rendering: im('peter-starcatcher', 'peter-act1') },
      { rendering: im('peter-starcatcher', 'peter-act2') },
      { caption: 'Designed by Kaylee Renaud. Crafted by Michelle Roy.',
        rendering: im('peter-starcatcher', 'mermaid-molly-rendering'),
        technicals: [im('peter-starcatcher', 'mermaid-molly-technicals')],
        progress: [im('peter-starcatcher', 'mermaid-molly-build')] },
      { rendering: im('peter-starcatcher', 'molly-nightgown') },
      { rendering: im('peter-starcatcher', 'black-stache') },
      { rendering: im('peter-starcatcher', 'alf') },
      { rendering: im('peter-starcatcher', 'grempkin') },
      { rendering: im('peter-starcatcher', 'fighting-prawn') },
    ],
  },

  // ---- Billiards — NYU Intermediate Narrative (realized) -------------------
  {
    id: 'billiards',
    show: 'Billiards', company: 'NYU Intermediate Narrative', director: 'Josh Li', role: 'Designer & Wardrobe', year: '2026', kind: 'realized',
    blurb: 'A recent graduate reconnects with his father, who has recently come to the U.S. from China, over a game of pool.',
    pieces: [
      { final: im('billiards', 'look-1') },                     // no COVER file → first look
      { final: im('billiards', 'look-2') },
      { final: im('billiards', 'look-3') },
      { final: im('billiards', 'look-4') },
    ],
  },

  // ---- Weightless — NYU Intermediate Narrative (realized) ------------------
  {
    id: 'weightless',
    show: 'Weightless', company: 'NYU Intermediate Narrative', director: 'Kevin Sherman', role: 'Costume Designer', year: '2026', kind: 'realized',
    blurb: 'Weightless takes place in the mind of a boy the moments after his passing, as he watches his parents respond to his death.',
    pieces: [
      { final: im('weightless', 'look-1') },                    // now first + card cover
      { final: im('weightless', 'cover') },
      { final: im('weightless', 'look-2') },
      { final: im('weightless', 'look-3') },
    ],
  },

  // ---- Like Mother — NYU Sight & Sound (realized) --------------------------
  {
    id: 'like-mother',
    show: 'Like Mother', company: 'NYU Sight & Sound: Filmmaking', director: 'Ziyan Zheng', role: 'Costume Designer', year: '2024', kind: 'realized',
    blurb: 'A collaborative narrative dance piece featuring Daijia Monae and Tianna Trenae from The Ailey School.',
    pieces: [
      { final: im('like-mother', 'look-3') },                   // cover (Kaylee's pick)
      { final: im('like-mother', 'look-1') },
      { final: im('like-mother', 'look-2') },
    ],
  },

  // ---- Renderings — paper (illustration) -----------------------------------
  {
    id: 'rendering-study',
    show: 'Renderings', company: 'Independent', director: '', role: 'Illustrator / Designer', year: '', kind: 'paper',
    pieces: [
      { name: 'Queen Elizabeth I', rendering: im('rendering-study', 'queen-elizabeth') },
      // Cirkus Kouzel — three renderings on one plate
      { name: 'Cirkus Kouzel',
        rendering: im('rendering-study', 'cirkus-clown'),
        renderings: [im('rendering-study', 'cirkus-ringmaster'), im('rendering-study', 'cirkus-balancing-act')] },
      { name: 'Matching Set',
        rendering: im('rendering-study', 'matching-set-sketch'),
        technicals: [im('rendering-study', 'matching-set-technical')] },
      { name: 'Temasek – Kit', rendering: im('rendering-study', 'temasek-kit') },
      { name: 'Temasek – Frenchie', rendering: im('rendering-study', 'temasek-frenchie') },
    ],
  },
];

// the trailing tag — an upcoming production (still a "coming soon" teaser)
export const upcoming = {
  show: 'Eurydice',
  company: 'NYU Tisch ETW',
  director: 'Dir. Elia Monte-Brown',
  role: 'Costume Designer',
  date: 'Fall 2026',
  note: 'Thank you to our Associate Z Wechsler and our Assistant Ollie Reece!',
};
