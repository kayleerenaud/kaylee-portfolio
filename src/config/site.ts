// ============================================================================
//  SITE CONFIG — the single source of truth for the whole site.
//  Change your brand name, links, or page order here and it updates everywhere
//  (header, page titles, footer, the "Next →" tour). No need to touch any
//  other file for these.
// ============================================================================

export const site = {
  // Your brand / artist name. Shows in the header, browser tab, and footer.
  // If you ever rebrand (or change your name), edit ONLY this line.
  brand: 'Kaylee Renaud',

  // A short tagline shown on the home page + in search results.
  tagline: 'Photographer · Costume Maker · Writer · Storyteller',

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
//  PAGE ORDER — controls both the top nav bar AND the "Next →" guided tour
//  at the bottom of each page. Reorder this array to reorder the whole site.
//  `inNav: false` keeps a page out of the top bar but still in the flow.
// ----------------------------------------------------------------------------
export type PageDef = {
  slug: string;       // url path; '' = home
  label: string;      // nav + link text
  teaser?: string;    // shown next to the "Next →" link at the bottom
  inNav?: boolean;
};

export const pages: PageDef[] = [
  { slug: '',            label: 'Home',        teaser: 'Start here.' },
  { slug: 'about',       label: 'About',       teaser: 'A little about me.' },
  { slug: 'photography', label: 'Photography', teaser: 'Light, people, places.' },
  { slug: 'costume',     label: 'Costume',     teaser: 'Things made by hand.' },
  { slug: 'writing',     label: 'Writing',     teaser: 'Words and worlds.' },
  { slug: 'film',        label: 'Video',       teaser: 'Moving pictures.' },
  { slug: 'contact',     label: 'Contact',     teaser: "Let's talk." },
];

export function pageHref(slug: string) {
  return slug === '' ? '/' : `/${slug}/`;
}

// Given the current page slug, return the next page in the tour (wraps around).
export function nextPage(currentSlug: string): PageDef {
  const i = pages.findIndex((p) => p.slug === currentSlug);
  return pages[(i + 1) % pages.length];
}
