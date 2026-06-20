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
  tagline: 'Film · Costume · Writing',

  // Where the contact form delivers (Formspree form ID).
  formspreeId: 'xojzgpdg',

  // Direct email shown on the contact page as a fallback.
  // (Once you own kayleerenaud.com you can switch this to hello@kayleerenaud.com.)
  email: 'kayleeerenaud@gmail.com',

  // Social links. Empty string = hidden.
  social: {
    instagram: 'https://www.instagram.com/the.miss.kaylee/',
    youtube: 'https://www.youtube.com/@the.miss.kaylee',
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

// Feminine cinematic palette on charcoal; rose thread ties the map together.
export const pages: PageDef[] = [
  { slug: '',        label: 'Home',    teaser: 'Start here.',           accent: '#d98a9e', tone: 196.00 },
  { slug: 'about',   label: 'About',   teaser: 'Get to know me.',         accent: '#b58ac0', tone: 220.00 },
  { slug: 'film',    label: 'Film',    teaser: 'My moving pictures.',     accent: '#8a72c2', tone: 174.61 },
  { slug: 'costume', label: 'Costume', teaser: 'Other bodies in motion.', accent: '#c8688e', tone: 261.63 },
  { slug: 'writing', label: 'Writing', teaser: 'Words and worlds collide!', accent: '#d6926e', tone: 207.65 },
  { slug: 'contact', label: 'Contact', teaser: "Let's make something.", accent: '#df8b93', tone: 246.94 },
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
