# Kaylee Renaud — Portfolio

A fast, content-first, **interactive** portfolio built with [Astro](https://astro.build).
The whole site ships ~1.7 kB of gzipped JavaScript, so it loads instantly and the
scroll never lags behind the story.

## Run it locally

```bash
npm install      # first time only
npm run dev      # local preview at http://localhost:4321
```

`npm run build` makes the production version in `dist/`.

## The story layer (what makes it interactive)

As you scroll, the site tells a story instead of just listing work:

- **Mood shifts** — each section has its own accent color (set in `src/config/site.ts`).
  As a section reaches the center of the screen, the whole site eases to that color.
- **Ambient sound** — a subtle tone fades in when you tap the speaker button
  (lower-right) and *changes pitch per section*. It's procedural for now (no audio
  files needed) and off by default; swap in real audio later, see below.
- **Reveal on scroll** — text and images ease in the instant they enter view.
  Triggered by scroll *position*, never a timed fade — so there's no dissolve that
  outlasts your scroll. Respects "reduce motion" system settings.
- **Scroll-progress hairline** in the active accent color, top of the page.
- **Guided "Next →" tour** at the bottom of every page, following the page order.

## Galleries & captions

Each image shows a **short caption preview** in its lower-left corner. Click/tap to
**enlarge** — the caption expands to its **full length**, and you can **toggle through
every image** in that gallery with the on-screen arrows, your keyboard ← →, or a swipe
on mobile. Esc or tap-outside closes.

## Where to change things (no deep coding needed)

| I want to change… | Edit this file |
|---|---|
| My brand/name, tagline, email, social links | `src/config/site.ts` |
| Page order / top menu / "Next →" tour | `pages` array in `src/config/site.ts` |
| A section's accent color or ambient tone | `accent` / `tone` in that `pages` entry |
| Photos + captions in a gallery | `src/data/galleries.ts` |
| My YouTube videos / film stills | `videos` / `filmStills` in `src/data/galleries.ts` |
| The About blurb | `src/pages/about.astro` |
| Colors & fonts (the base look) | the variables at the top of `src/styles/global.css` |

## Pages

Home · About · Film · Costume · Writing · Contact —
each ends with a "Next →" link that follows the order in `src/config/site.ts`.

## Contact form setup (one-time)

1. Make a free account at [formspree.io](https://formspree.io) and create a form.
2. Copy the form ID (looks like `xyzabcd`).
3. Paste it into `formspreeId` in `src/config/site.ts`.

Submissions then email you **and** are stored in your Formspree dashboard.

## Adding real images

For now, galleries use placeholder images. To use your own:
- Drop files into `public/images/` and reference them as `/images/yourphoto.jpg` in
  `src/data/galleries.ts`, **or**
- (Better quality/perf) we'll move them into `src/assets/` and switch to Astro's
  optimized `<Image>` component — ping Claude when you're ready.

## Swapping the procedural sound for real audio

The ambient pad is generated in the browser (`src/components/Atmosphere.astro`). To use
real audio clips instead, add `/audio/*.mp3` files and point each section at one — ask
Claude to wire the `data-audio` path and we'll crossfade between real tracks per section.

## Still to come (the "full Kayleeverse")

- **In-page admin** — a password-protected editor to change captions/upload images in
  the browser (needs a small database + auth; this scaffold is structured for it).
- Blog page (markdown posts).
- Kid-friendly audio "web stories" (image + audio click-through player).
