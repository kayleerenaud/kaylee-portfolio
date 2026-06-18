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

const ph = (seed: string) => `https://picsum.photos/seed/${seed}/900/1125`;

// FILM — stills from set / behind-the-scenes. (Moving pieces live in `videos`.)
//   edge = the film-strip "edge print": project name + date for that frame.
export const filmStills: GalleryItem[] = [
  { src: ph('kr-film-1'), alt: 'Placeholder film still 1', edge: 'Project One · 2024', caption: 'Lorem ipsum — opening frame, golden hour on location. The full caption can run several sentences and will expand here when enlarged, telling the story behind the shot.' },
  { src: ph('kr-film-2'), alt: 'Placeholder film still 2', edge: 'Project One · 2024', caption: 'Lorem ipsum — close on the lead during the third act. Replace with the real story of this frame.' },
  { src: ph('kr-film-3'), alt: 'Placeholder film still 3', edge: 'Project Two · 2023', caption: 'Lorem ipsum — wide establishing shot, quiet morning light.' },
  { src: ph('kr-film-4'), alt: 'Placeholder film still 4', edge: 'Project Two · 2023', caption: 'Lorem ipsum — behind the scenes, blocking the dolly move.' },
  { src: ph('kr-film-5'), alt: 'Placeholder film still 5', edge: 'Project Three · 2023', caption: 'Lorem ipsum — practical lighting test, deep shadows.' },
  { src: ph('kr-film-6'), alt: 'Placeholder film still 6', edge: 'Project Three · 2023', caption: 'Lorem ipsum — final frame before the cut to black.' },
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

// Video projects — YouTube video IDs (the part after watch?v= or youtu.be/).
export const videos = [
  { id: 'dQw4w9WgXcQ', title: 'Project title — replace with your video', blurb: 'A sentence about this piece.' },
  { id: 'dQw4w9WgXcQ', title: 'Another project — replace me', blurb: 'A sentence about this piece.' },
];
