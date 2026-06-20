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
  { src: phL('kr-film-1'), alt: 'Placeholder film still 1', edge: 'Project One · 2024', caption: 'Lorem ipsum — opening frame, golden hour on location. The full caption can run several sentences and will expand here when enlarged, telling the story behind the shot.' },
  { src: phL('kr-film-2'), alt: 'Placeholder film still 2', edge: 'Project One · 2024', caption: 'Lorem ipsum — close on the lead during the third act. Replace with the real story of this frame.' },
  { src: phL('kr-film-3'), alt: 'Placeholder film still 3', edge: 'Project Two · 2023', caption: 'Lorem ipsum — wide establishing shot, quiet morning light.' },
  { src: phL('kr-film-4'), alt: 'Placeholder film still 4', edge: 'Project Two · 2023', caption: 'Lorem ipsum — behind the scenes, blocking the dolly move.' },
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
      "An auto-documentary. I sit down with my three parents to ask how they raised me across the political and religious spectrum, and kept love at the center. A portrait of a family that agrees on almost nothing except each other.",
  },
  {
    id: 's1aRxygTD6s',
    title: 'Spirit Temple No. 7',
    meta: 'Documentary',
    blurb:
      "I follow two artists to the furthest edge of New York City, where they're raising a temple out of driftwood and coastal trash. Somewhere between the tide line and the offering, we meet the spirit himself: Chris.",
  },
  {
    id: 'uAGjuZFWCis',
    title: 'Elli',
    meta: 'Documentary · Archival short',
    blurb:
      "A short archival portrait of Elli, a concentration camp survivor, told in the words of her daughter Dianna, and voiced by me: Dianna's granddaughter, and Elli's great-granddaughter. Three generations carrying a single voice.",
  },
];
