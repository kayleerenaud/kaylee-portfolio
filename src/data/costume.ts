// ============================================================================
//  COSTUME CONTENT — projects shown as "oak tags" on a rail. Clicking a tag
//  opens an in-page plate overlay (✕ to close) with each piece's final +
//  rendering + progress, all flexible per piece.
//
//  Each Project = one production (or paper project). Each Piece is a costume
//  "look" with whatever images exist:
//     final?     finished costume photo  (omit for paper / unrealized projects)
//     rendering? the design illustration
//     progress?  1–3 in-progress / construction photos
//     swatches?  flat photos of fabric swatches (optional; only if you have them)
//     caption    the written note that travels with the piece (preview → full)
//
//  kind: 'realized' = has production photos; 'paper' = design-only (thesis, etc.)
// ============================================================================

export type Piece = {
  caption: string;
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

const ph = (seed: string, w: number, h: number) => `https://picsum.photos/seed/${seed}/${w}/${h}`;
const fin = (s: string) => ph(s, 840, 1140);   // finished costume (portrait)
const ren = (s: string) => ph(s, 780, 1060);   // rendering / illustration
const pro = (s: string) => ph(s, 780, 1000);   // progress / construction

export const projects: Project[] = [
  {
    id: 'tempest',
    show: 'The Tempest', company: 'Placeholder Theatre Co.', director: 'Dir. Placeholder', role: 'Costume Designer', year: '2024', kind: 'realized',
    blurb: 'Lorem ipsum — a storm-tossed island world. Placeholder note about the design concept and palette.',
    pieces: [
      { caption: 'Prospero — Act I. Lorem ipsum about the build: hand-dyed silk, layered for movement. The full note expands here.', final: fin('cos-temp-1f'), rendering: ren('cos-temp-1r'), progress: [pro('cos-temp-1p1'), pro('cos-temp-1p2')] },
      { caption: 'Ariel — the spirit look. Lorem ipsum on the airy construction and harness.', final: fin('cos-temp-2f'), rendering: ren('cos-temp-2r'), progress: [pro('cos-temp-2p1')] },
      { caption: 'Caliban. Lorem ipsum — texture study and distressing.', final: fin('cos-temp-3f'), rendering: ren('cos-temp-3r') },
    ],
  },
  {
    id: 'little-shop',
    show: 'Little Shop of Horrors', company: 'Placeholder Playhouse', director: 'Dir. Placeholder', role: 'Costume Designer', year: '2023', kind: 'realized',
    pieces: [
      { caption: 'Audrey — the iconic dress. Lorem ipsum about silhouette and fittings.', final: fin('cos-ls-1f'), rendering: ren('cos-ls-1r'), progress: [pro('cos-ls-1p1'), pro('cos-ls-1p2')] },
      { caption: 'Seymour. Lorem ipsum — thrifted-and-altered approach.', final: fin('cos-ls-2f'), progress: [pro('cos-ls-2p1')] },
    ],
  },
  {
    id: 'dolls-house',
    show: "A Doll's House", company: 'Placeholder Rep', director: 'Dir. Placeholder', role: 'Associate Costume Designer', year: '2023', kind: 'realized',
    pieces: [
      { caption: 'Nora — Act III. Lorem ipsum on period tailoring and trim.', final: fin('cos-dh-1f'), rendering: ren('cos-dh-1r') },
      { caption: 'Torvald. Lorem ipsum — placeholder note.', final: fin('cos-dh-2f'), rendering: ren('cos-dh-2r'), progress: [pro('cos-dh-2p1')] },
    ],
  },
  {
    id: 'hadestown',
    show: 'Hadestown', company: 'Placeholder Regional', director: 'Dir. Placeholder', role: 'Costume Designer', year: '2022', kind: 'realized',
    pieces: [
      { caption: 'Persephone. Lorem ipsum — seasonal color story.', final: fin('cos-had-1f'), rendering: ren('cos-had-1r'), progress: [pro('cos-had-1p1')] },
      { caption: 'The Fates. Lorem ipsum — placeholder.', final: fin('cos-had-2f'), rendering: ren('cos-had-2r') },
    ],
  },
  {
    id: 'thesis',
    show: 'Thesis Project', company: 'Placeholder University', director: 'Dir. Placeholder (concept)', role: 'Designer', year: '2024', kind: 'paper',
    blurb: 'A paper project — designed in full, never produced. Lorem ipsum about the world and research.',
    pieces: [
      { caption: 'Lead — rendering & research. Lorem ipsum on the concept and references.', rendering: ren('cos-th-1r'), progress: [pro('cos-th-1p1'), pro('cos-th-1p2')] },
      { caption: 'Ensemble study. Lorem ipsum — silhouette exploration.', rendering: ren('cos-th-2r') },
      { caption: 'Antagonist. Lorem ipsum — palette and texture notes.', rendering: ren('cos-th-3r'), progress: [pro('cos-th-3p1')] },
    ],
  },
  {
    id: 'rendering-study',
    show: 'Rendering & Swatch Study', company: 'Independent', director: '—', role: 'Illustrator / Designer', year: '2023', kind: 'paper',
    blurb: 'A pure design exercise in rendering and fabric study. Lorem ipsum.',
    pieces: [
      { caption: 'Watercolor figure study. Lorem ipsum on technique.', rendering: ren('cos-rs-1r') },
      { caption: 'Textile rendering. Lorem ipsum — rendering fabric drape and sheen.', rendering: ren('cos-rs-2r') },
      { caption: 'Gouache plate. Lorem ipsum — placeholder.', rendering: ren('cos-rs-3r') },
    ],
  },
];

// the 7th tag — shows you're actively working
export const upcoming = {
  show: 'Upcoming Production',
  company: 'Placeholder Company',
  director: 'Dir. Placeholder',
  role: 'Costume Designer',
  date: 'Spring 2026',
};
