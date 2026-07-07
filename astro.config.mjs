import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://kayleerenaud.com',
  // Image optimization is on by default via astro:assets.
  // (Sitemap is a static file at public/sitemap.xml — the @astrojs/sitemap
  //  integration hit a version-mismatch crash, and 6 pages don't need it.)
});
