import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/serverless';

// https://astro.build/config
export default defineConfig({
  site: 'https://kayleerenaud.com',
  output: 'server',
  adapter: vercel({
    webAnalytics: { enabled: true },
  }),
  // Image optimization is on by default via astro:assets.
  // (Sitemap is a static file at public/sitemap.xml — the @astrojs/sitemap
  //  integration hit a version-mismatch crash, and 6 pages don't need it.)
});
