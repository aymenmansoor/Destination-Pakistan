# Corrections against the eight references

Both reference batches were applied together on top of `94cd590`. The owner approved committing and pushing this iteration to the existing development branch; no merge or deployment was performed.

## Visual comparison

| Reference | Correction and visual review |
| --- | --- |
| Image 1 · Tour Packages | Restored beige introduction, terracotta label and shared left alignment for heading, centered rounded slideshow and three-column cards. Existing 1,050 × 380px desktop slider and 30px card gap retained. |
| Image 2 · Destinations | Matching beige introduction and aligned slideshow/cards; the existing autumn Hunza photograph now opens the slideshow, matching the reference. The dusk photo remains as a fourth slide with its own indicator. Original card images and links retained. |
| Image 3 · Tour categories | All nine use beige introductions, visible terracotta labels, cream confirmation notices and ivory card bodies. Existing three/two/one-column grids and package values unchanged. |
| Image 4 · Guides | All twelve share a rounded wide main photograph, ivory background, readable article and compact cream sidebar. The 1,050px desktop frames use 2.4:1; phones use 16:9. |
| Image 5 · Khunjerab | Removed its taller natural-ratio exception; same photograph frame, article typography, spacing and sidebar as Saral and the other guides. Original group photo preserved. |
| Image 6 · Extra headings | Removed the three repetitive Khunjerab article headings and oversized lead style. Every guide retains its main title and all article paragraphs. Related navigation remains with an understated label. |
| Image 7 · Article/sidebar | Larger left article and smaller right cream card (two-thirds/one-third after the 32px gap), rounded border and green enquiry action. Sidebar stacks beneath the article below 768px. |
| Images 7–8 · Background | Shared beige `#eee9dd` replaces pale green in gallery/soft-section backgrounds. The homepage overview now uses the same beige; ivory main backgrounds, cream panels, terracotta labels and green actions remain. |

The supplied references were compared visually with the rendered desktop, tablet and phone pages, not only with source code. Original photograph files are unchanged. Wide frames intentionally crop their top/bottom edges; subject-specific positions were reviewed, and each guide main photo opens its complete original with a pointer or keyboard. No replacement stock images, generic descriptions, changed package values or new travel claims were introduced.

## Screenshots

| Page | Phone · 375px | Tablet · 768px | Desktop · 1440px |
| --- | --- | --- | --- |
| tour | [View](references/tour-375.png) | [View](references/tour-768.png) | [View](references/tour-1440.png) |
| destination | [View](references/destination-375.png) | [View](references/destination-768.png) | [View](references/destination-1440.png) |
| wild | [View](references/wild-375.png) | [View](references/wild-768.png) | [View](references/wild-1440.png) |
| saral | [View](references/saral-375.png) | [View](references/saral-768.png) | [View](references/saral-1440.png) |
| khunjerab | [View](references/khunjerab-375.png) | [View](references/khunjerab-768.png) | [View](references/khunjerab-1440.png) |
| gallery | [View](references/gallery-375.png) | [View](references/gallery-768.png) | [View](references/gallery-1440.png) |
| index | [View](references/index-375.png) | [View](references/index-768.png) | [View](references/index-1440.png) |

All-guide and all-page review sheets:

- 375px: [All twelve guides](references/guides-375.jpg) · [All 28 page viewports](references/pages-375.jpg)
- 768px: [All twelve guides](references/guides-768.jpg) · [All 28 page viewports](references/pages-768.jpg)
- 1440px: [All twelve guides](references/guides-1440.jpg) · [All 28 page viewports](references/pages-1440.jpg)

## Checks actually executed

- 968 current local link/asset/fragment checks. All 28 pages rendered at nine widths (320, 375, 390, 576, 768, 991, 1024, 1440 and 1920px): **252 cases**, zero detected layout/image/heading failures, HTTP errors or JavaScript/console errors. All twelve guide frame/title positions passed at every width (**108 cases**). Landscape and viewport-equivalent 200% zoom reflow passed on all 28 pages, plus eleven representative doubled-text checks.
- **161 shared-design cases** at seven widths: twelve guide titles/cream headers, same photo ratio/width, uncropped-photo links and article/sidebar split; nine package grids/image heights/button alignment and unchanged card text; matching sliders. Theme, Contact, homepage preview and real card hover/reduced-motion behavior were also checked.
- **14 interaction groups** observed actual five-second autoplay/manual controls/pause/resume, keyboard/touch behavior, reduced motion, menu/skip link, gallery filtering/dialog keyboard/focus behavior, contact enquiry validation/draft/copy/reset and no-JavaScript fallbacks.
- **21 guide/category reveal checks plus two rapid-filter/live-motion checks** observed real animation events. **11 recording checks** observed repeated autoplay, manual arrows/indicators, hover/scroll/menu/lightbox/filter motion and reduced motion. [Desktop recording](references/desktop-motion.webm) · [Mobile recording](references/mobile-motion.webm) · [Recorded events](references/final-results.json).
- All twelve complete-original photo links were opened using the keyboard and decoded successfully. Guide paragraph text and photo-source sequences were compared against HEAD and are unchanged; all nine category HTML files are unchanged.
- **56 stable axe-core WCAG 2/2.1 A/AA scans** (all pages at 375/1440px) found zero violations. Two final homepage palette follow-ups and two final Destinations slide follow-ups also found zero. Automated checks do not establish full accessibility conformance.

The main matrix preceded the final homepage shade and Destinations opening-photo adjustment. The homepage received palette/accessibility follow-ups; Destinations was checked again at all nine widths with all four indicators and fresh screenshots, and the real-recording suite was rerun. Source formatting and diff checks passed.

[Layout/guide results](references/layout-results.json) · [Design results](references/design-results.json) · [Interactions](references/interaction-results.json) · [Guide/category motion](references/motion-pages-results.json) · [Original-photo keyboard links](references/original-photo-results.json) · [Accessibility](references/accessibility-results.json) · [Destinations follow-up](references/destination-followup.json)

## Modified files and affected pages

Modified source: the twelve destination guide HTML files, `destination.html`, `assets/css/base.css`, `assets/css/home.css`, `assets/css/photography.css`, `assets/css/editorial.css`, and the shared-design assertions in `scripts/check_design.py`. README and AUDIT are updated. Tour Packages, all nine category pages, gallery and selected homepage sections receive their corrections through shared CSS. Routes, original photographs, package values and JavaScript modules are preserved. [Exact changed-file inventory](references/changed-files.txt).

## Remaining limits

Original low-resolution assets, watermarks, unverified image locations/rights and inherited commercial/content claims remain documented in AUDIT. Khunjerab retains owner-supplied information rather than independently verified research. Physical devices, non-Chromium browsers, screen readers, native zoom and actual external email delivery were not tested. The contact form prepares/copies an enquiry; it does not submit to a server.

This iteration is provided on `codex/destination-pakistan-redesign` with explicit owner approval. Its ZIP includes the current corrections and browser evidence; `main` is unchanged.
