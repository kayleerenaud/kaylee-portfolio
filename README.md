# Kaylee Renaud — Portfolio

A fast, content-first portfolio built with [Astro](https://astro.build).

## Run it locally

```bash
npm install      # first time only
npm run dev      # start a local preview at http://localhost:4321
```

`npm run build` makes the production version in `dist/`.

## Where to change things (no deep coding needed)

| I want to change… | Edit this file |
|---|---|
| My brand/name, tagline, email, social links | `src/config/site.ts` |
| The order of pages / the top menu / the "Next →" tour | `pages` array in `src/config/site.ts` |
| Photos + captions in a gallery | `src/data/galleries.ts` |
| My YouTube videos | `videos` in `src/data/galleries.ts` |
| The About blurb | `src/pages/about.astro` |
| Colors & fonts (the whole look) | the variables at the top of `src/styles/global.css` |

## Pages

Home · About · Photography · Costume · Writing · Video · Contact —
each ends with a "Next →" link that follows the order in `src/config/site.ts`.

## Contact form setup (one-time)

1. Make a free account at [formspree.io](https://formspree.io) and create a form.
2. Copy the form ID (looks like `xyzabcd`).
3. Paste it into `formspreeId` in `src/config/site.ts`.

Submissions then email you **and** are stored in your Formspree dashboard, capturing
the sender's name, email, phone, topic, and message.

## Adding real images

For now, galleries use placeholder images. To use your own:
- Drop files into `public/images/` and reference them as `/images/yourphoto.jpg` in
  `src/data/galleries.ts`, **or**
- (Better quality/perf) we'll move them into `src/assets/` and switch to Astro's
  optimized `<Image>` component — ping Claude when you're ready.

## Still to come (the "full Kayleeverse")

- Blog page (markdown posts)
- Kid-friendly audio "web stories" (image + audio click-through player)
