// ============================================================================
//  CONTENT — placeholder images + captions for each gallery.
//  Replace the picsum.photos URLs with your real images and write your real
//  captions here. (Later we'll move real photos into src/assets/ for automatic
//  optimization — for now these remote placeholders just let you see the flow.)
//
//  Each item: { src, alt, caption }
//    src     = image URL (or /images/... once you add real files to /public)
//    alt     = plain description for accessibility / screen readers
//    caption = the FULL caption. A short preview shows lower-left on the
//              thumbnail; the whole thing expands in the enlarged lightbox view.
// ============================================================================
import type { GalleryItem } from '../components/Gallery.astro';

const ph = (seed: string) => `https://picsum.photos/seed/${seed}/900/1125`;        // portrait
const phL = (seed: string) => `https://picsum.photos/seed/${seed}/1280/720`;       // landscape (16:9)

// FILM — stills from set / behind-the-scenes. (Moving pieces live in `videos`.)
//   edge = the film-strip "edge print": project name + date for that frame.
//   Landscape placeholders so the enlarged view opens horizontal, like real
//   widescreen film stills. (Upload landscape stills to match.)
export const filmStills: GalleryItem[] = [
  { src: '/film/collateral-calamity-1.jpg', alt: 'Four young adults peek warily around a stone corner on a New York street', edge: 'Collateral Calamity · 2024', caption: "Four accomplices, one terrible plan. The crew peeks around a corner to check the coast in Collateral Calamity, my 2024 short comedy about an eclectic group of young adults trying to hide a body in New York City. What could possibly go wrong? Original music by me." },
  { src: '/film/collateral-calamity-2.jpg', alt: 'A low-angle shot of characters wrestling something on a Manhattan stoop', edge: 'Collateral Calamity · 2024', caption: "Everything that can go sideways, does. A scramble on the stoop from Collateral Calamity (2024), a short comedy I wrote and scored myself." },
  { src: '/film/dinners-ready-1.jpg', alt: 'Black-and-white close-up of a curly-haired boy with a wary, downcast expression', edge: "Dinner's Ready! · 2024", caption: "A son caught in his father's temper. Dinner's Ready! (2024) is a narrative short that asks what happens when we let our own agenda consume us. This close-up holds the boy's fear in the moment before everything boils over." },
  { src: '/film/dinners-ready-2.jpg', alt: 'Black-and-white kitchen scene with a father, a son eating, and a mother', edge: "Dinner's Ready! · 2024", caption: "After the storm, a thaw. Father, son, and mother back in the kitchen in Dinner's Ready! (2024), where an apology and an offer to cook together turns a hard night into a shared one." },
  { src: phL('kr-film-5'), alt: 'Placeholder film still 5', edge: 'Project Three · 2023', caption: 'Lorem ipsum — practical lighting test, deep shadows.' },
  { src: phL('kr-film-6'), alt: 'Placeholder film still 6', edge: 'Project Three · 2023', caption: 'Lorem ipsum — final frame before the cut to black.' },
];

export const costume: GalleryItem[] = [
  { src: ph('kr-costume-1'), alt: 'Placeholder costume 1', caption: 'Lorem ipsum — hand-stitched bodice, boned and lined. The full process note expands here: fabric choices, fittings, and the reference that started it.' },
  { src: ph('kr-costume-2'), alt: 'Placeholder costume 2', caption: 'Lorem ipsum — detail of the beadwork at the collar.' },
  { src: ph('kr-costume-3'), alt: 'Placeholder costume 3', caption: 'Lorem ipsum — the full look, photographed on set.' },
  { src: ph('kr-costume-4'), alt: 'Placeholder costume 4', caption: 'Lorem ipsum — fabric study and draping test.' },
];

// Writing pieces use a "cover" image that opens to the full text in the lightbox.
export const writing: GalleryItem[] = [
  { src: ph('kr-writing-1'), alt: 'Cover for a written piece 1', caption: 'Title of piece — Lorem ipsum dolor sit amet. The short excerpt previews lower-left; the full short piece (or a longer excerpt) expands in the enlarged view so a reader can read it in place.' },
  { src: ph('kr-writing-2'), alt: 'Cover for a written piece 2', caption: 'Title of piece — Lorem ipsum, a short excerpt here.' },
  { src: ph('kr-writing-3'), alt: 'Cover for a written piece 3', caption: 'Title of piece — Lorem ipsum, a short excerpt here.' },
];

// Photos of Kaylee for the About page.
export const aboutPhotos: GalleryItem[] = [
  { src: ph('kr-me-1'), alt: 'Photo of Kaylee 1', caption: '' },
  { src: ph('kr-me-2'), alt: 'Photo of Kaylee 2', caption: '' },
  { src: ph('kr-me-3'), alt: 'Photo of Kaylee 3', caption: '' },
];

// The "Coming Soon" slide at the end of the Film stills strip (movie-trailer
// style). Fill in your upcoming film's title, your role, and the date.
export const upcomingFilm = {
  title: 'Untitled Comedy',
  role: 'Writer / Director',
  date: 'Narrative · In Production 2026',
};

// Video projects — YouTube video IDs (the part after watch?v= or youtu.be/).
//   meta = optional small line under the title (form · festival recognition)
export const videos = [
  {
    id: 'Qm7khPLbYsw',
    title: "Together, I'm Pieces",
    meta: 'Documentary · Honorable Mention, Fusion Film Festival 2026 · Official Selection, WinterFest 2025',
    blurb:
      "An auto-documentary. I sit down with my three parents to ask how they raised me across the political and religious spectrum, and kept love at the center. No tables were flipped in the making of this film.",
  },
  {
    id: 's1aRxygTD6s',
    title: 'Spirit Temple No. 7',
    meta: 'Documentary · Artist portrait',
    blurb:
      "I follow two artists to the furthest edge of New York City, where they're raising a temple out of driftwood and coastal trash. Somewhere between the tide line and the offering, we meet the spirit himself: Chris.",
  },
  {
    id: 'uAGjuZFWCis',
    title: 'Elli',
    meta: 'Documentary · Archival short',
    blurb:
      "A short archival portrait of Elli, a concentration camp survivor, told in the words of her daughter Dianna, and voiced by me: Dianna's granddaughter, and Elli's great-granddaughter. Three generations carry a single voice.",
  },
];
