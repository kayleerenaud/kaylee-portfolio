// ============================================================================
//  COSTUME CONTENT — projects shown as "oak tags" on a rail. Clicking a tag
//  opens an in-page plate overlay (✕ to close) with each piece's imagery + note.
//
//  Each Project = one production (or paper project). Each Piece is a costume
//  "look" with whatever images exist:
//     final?     finished costume photo  (omit for paper / unrealized projects)
//     rendering? the design illustration
//     progress?  1–3 in-progress / construction photos
//     swatches?  flats / technicals / fabric swatches (optional)
//     caption?   the written note that travels with the piece (preview → full)
//
//  kind: 'realized' = has production photos; 'paper' = design-only (renderings).
//
//  ▸ IMAGES are Kaylee's real photos (from the Drive drop). The card cover is the
//    file she marked *_COVER (or the first look when there was none).
//  ▸ TEXT is still to come: company / director / role / year / blurb / per-piece
//    captions are left blank on purpose. Empty fields simply don't render, so the
//    page looks clean until Kaylee sends the copy. (See the message thread for the
//    fill-in template.)
// ============================================================================

export type Piece = {
  caption?: string;
  final?: string;
  rendering?: string;
  progress?: string[];
  swatches?: string[];
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
    show: 'Knights of the Old Republic', company: 'Studio 70', director: '', role: 'Costume Director', year: '', kind: 'realized',
    pieces: [
      { final: im('kotor', 'cover') },                          // *_COVER → card cover
      { final: im('kotor', 'look-1') },
      { final: im('kotor', 'look-2') },
      { final: im('kotor', 'look-3') },
      { final: im('kotor', 'look-4') },
      { final: im('kotor', 'look-5') },
      { final: im('kotor', 'look-6') },
      { final: im('kotor', 'look-7') },
    ],
  },

  // ---- As You Like It (realized) -------------------------------------------
  {
    id: 'as-you-like-it',
    show: 'As You Like It', company: '', director: '', role: '', year: '', kind: 'realized',
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

  // ---- Peter and the Starcatcher — thesis / paper (renderings) --------------
  {
    id: 'peter-starcatcher',
    show: 'Peter and the Starcatcher', company: '', director: '', role: '', year: '', kind: 'paper',
    pieces: [
      { rendering: im('peter-starcatcher', 'teacher') },        // *_COVER → card cover
      { rendering: im('peter-starcatcher', 'peter-act1') },
      { rendering: im('peter-starcatcher', 'peter-act2') },
      { rendering: im('peter-starcatcher', 'mermaid-molly-rendering'),
        progress: [im('peter-starcatcher', 'mermaid-molly-build')],
        swatches: [im('peter-starcatcher', 'mermaid-molly-technicals')] },
      { rendering: im('peter-starcatcher', 'molly-nightgown') },
      { rendering: im('peter-starcatcher', 'black-stache') },
      { rendering: im('peter-starcatcher', 'alf') },
      { rendering: im('peter-starcatcher', 'grempkin') },
      { rendering: im('peter-starcatcher', 'fighting-prawn') },
    ],
  },

  // ---- Billiards (realized) ------------------------------------------------
  {
    id: 'billiards',
    show: 'Billiards', company: '', director: '', role: '', year: '', kind: 'realized',
    pieces: [
      { final: im('billiards', 'look-1') },                     // no COVER file → first look
      { final: im('billiards', 'look-2') },
      { final: im('billiards', 'look-3') },
      { final: im('billiards', 'look-4') },
    ],
  },

  // ---- Weightless (realized) -----------------------------------------------
  {
    id: 'weightless',
    show: 'Weightless', company: '', director: '', role: 'Costume Designer', year: '', kind: 'realized',
    pieces: [
      { final: im('weightless', 'cover') },                     // *_COVER → card cover
      { final: im('weightless', 'look-1') },
      { final: im('weightless', 'look-2') },
      { final: im('weightless', 'look-3') },
    ],
  },

  // ---- Like Mother — film (realized) ---------------------------------------
  {
    id: 'like-mother',
    show: 'Like Mother', company: '', director: '', role: 'Costume Designer', year: '', kind: 'realized',
    pieces: [
      { final: im('like-mother', 'look-1') },                   // no COVER file → first look
      { final: im('like-mother', 'look-2') },
      { final: im('like-mother', 'look-3') },
    ],
  },

  // ---- Renderings — paper (illustration) -----------------------------------
  {
    id: 'rendering-study',
    show: 'Renderings', company: 'Independent', director: '', role: 'Illustrator / Designer', year: '', kind: 'paper',
    pieces: [
      { rendering: im('rendering-study', 'queen-elizabeth') },  // no COVER file → strongest plate
      { rendering: im('rendering-study', 'cirkus-ringmaster') },
      { rendering: im('rendering-study', 'cirkus-clown') },
      { rendering: im('rendering-study', 'cirkus-balancing-act') },
      { rendering: im('rendering-study', 'matching-set-sketch'),
        swatches: [im('rendering-study', 'matching-set-technical')] },
      { rendering: im('rendering-study', 'temasek-kit') },
      { rendering: im('rendering-study', 'temasek-frenchie') },
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
};
