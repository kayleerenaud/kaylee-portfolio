// ============================================================================
//  CONTENT — placeholder images + captions for each gallery.
//  Replace the picsum.photos URLs with your real images and write your real
//  captions here. (Later we'll move real photos into src/assets/ for automatic
//  optimization — for now these remote placeholders just let you see the flow.)
//
//  Each item: { src, alt, caption }
//    src     = image URL (or /images/... once you add real files to /public)
//    alt     = plain description for accessibility / screen readers
//    caption = the text shown lower-left on hover + in full in the lightbox
// ============================================================================
import type { GalleryItem } from '../components/Gallery.astro';

const ph = (seed: string) => `https://picsum.photos/seed/${seed}/900/1125`;

export const photography: GalleryItem[] = [
  { src: ph('kr-photo-1'), alt: 'Placeholder photograph 1', caption: 'Caption goes here — golden hour, downtown.' },
  { src: ph('kr-photo-2'), alt: 'Placeholder photograph 2', caption: 'Caption goes here — portrait study.' },
  { src: ph('kr-photo-3'), alt: 'Placeholder photograph 3', caption: 'Caption goes here — quiet morning.' },
  { src: ph('kr-photo-4'), alt: 'Placeholder photograph 4', caption: 'Caption goes here — texture & light.' },
  { src: ph('kr-photo-5'), alt: 'Placeholder photograph 5', caption: 'Caption goes here — on location.' },
  { src: ph('kr-photo-6'), alt: 'Placeholder photograph 6', caption: 'Caption goes here — candid.' },
];

export const costume: GalleryItem[] = [
  { src: ph('kr-costume-1'), alt: 'Placeholder costume 1', caption: 'Caption goes here — hand-stitched bodice.' },
  { src: ph('kr-costume-2'), alt: 'Placeholder costume 2', caption: 'Caption goes here — detail work.' },
  { src: ph('kr-costume-3'), alt: 'Placeholder costume 3', caption: 'Caption goes here — full look.' },
  { src: ph('kr-costume-4'), alt: 'Placeholder costume 4', caption: 'Caption goes here — fabric study.' },
];

// Writing pieces use a "cover" image that opens to the full text in the lightbox.
export const writing: GalleryItem[] = [
  { src: ph('kr-writing-1'), alt: 'Cover for a written piece 1', caption: 'Title of piece — short excerpt or the full short text can live here.' },
  { src: ph('kr-writing-2'), alt: 'Cover for a written piece 2', caption: 'Title of piece — short excerpt here.' },
  { src: ph('kr-writing-3'), alt: 'Cover for a written piece 3', caption: 'Title of piece — short excerpt here.' },
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
