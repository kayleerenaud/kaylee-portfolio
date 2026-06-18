// ============================================================================
//  SITE CONFIG — the single source of truth for the whole site.
//  Change your brand name, links, page order, section colors, or audio motifs
//  here and it updates everywhere (header, titles, footer "Next →" tour, the
//  scroll-driven color + sound moods). No need to touch any other file.
// ============================================================================

export const site = {
  // Your brand / artist name. Shows in the header, browser tab, and footer.
  brand: 'Kaylee Renaud',

  // A short tagline shown on the home page + in search results.
  tagline: 'Film · Costume · Writing · Visual Storytelling',

  // Where the contact form delivers. See src/pages/contact.astro for setup.
  // Paste your Formspree form ID here once you create a (free) account.
  formspreeId: 'YOUR_FORM_ID',

  // Direct email shown on the contact page as a fallback.
  email: 'hello@kayleerenaud.com',

  // Social links. Empty string = hidden.
  social: {
    instagram: 'https://www.instagram.com/the.miss.kaylee/',
    youtube: 'https://www.youtube.com/@kayleerenaud',
  },
} as const;

// ----------------------------------------------------------------------------
//  PAGES — controls the top nav, the "Next →" guided tour, AND each section's
//  "mood": the accent color it paints the site with and the audio motif it
//  plays as you arrive. Reorder this array to reorder the whole story.
//
//    slug    : url path; '' = home
//    label   : nav + link text
//    teaser  : shown next to the "Next →" link at the bottom of the prior page
//    accent  : the section's signature color (drives links, highlights, motion)
//    tone    : base note (Hz) for the optional ambient pad that plays on arrival
//    inNav   : false = keep out of the top bar but still in the story flow
// ----------------------------------------------------------------------------
export type PageDef = {
  slug: string;
  label: string;
  teaser?: string;
  accent: string;
  tone: number;
  inNav?: boolean;
};

export const pages: PageDef[] = [
  { slug: '',        label: 'Home',    teaser: 'Start here.',           accent: '#b4654a', tone: 196.00 },
  { slug: 'about',   label: 'About',   teaser: 'A little about me.',    accent: '#6b7f6e', tone: 220.00 },
  { slug: 'film',    label: 'Film',    teaser: 'Moving pictures.',      accent: '#4a6178', tone: 174.61 },
  { slug: 'costume', label: 'Costume', teaser: 'Made by hand.',         accent: '#8a5a78', tone: 261.63 },
  { slug: 'writing', label: 'Writing', teaser: 'Words and worlds.',     accent: '#9a7b4f', tone: 207.65 },
  { slug: 'contact', label: 'Contact', teaser: "Let's make something.", accent: '#4f7a72', tone: 246.94 },
];

export function pageHref(slug: string) {
  return slug === '' ? '/' : `/${slug}/`;
}

export function getPage(slug: string): PageDef {
  return pages.find((p) => p.slug === slug) ?? pages[0];
}

// Given the current page slug, return the next page in the tour (wraps around).
export function nextPage(currentSlug: string): PageDef {
  const i = pages.findIndex((p) => p.slug === currentSlug);
  return pages[(i + 1) % pages.length];
}
