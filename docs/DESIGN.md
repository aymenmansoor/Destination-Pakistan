# Requested design refinement review

Incremental work on top of `77f3079` on `codex/destination-pakistan-redesign`. No reset or revert. The owner explicitly approved committing and pushing this iteration to the existing development branch.

## Design changes

| Area | Result |
| --- | --- |
| Tour and destination directories | Matching 1,050px maximum-width, 380px desktop-height sliders, 10px corners, 32px captions and a 30px gap to the cards. Lighter bottom overlay, centered arrows and existing indicators. |
| Twelve destination guides | Warm-ivory heading, breadcrumbs, destination label, serif title and contextual introduction; 1,050px photograph and two-thirds/one-third copy/sidebar layout, stacked on phones. Rounded photo corners and compact beige enquiry card. |
| Saral | A 2.4:1 desktop composition retains the lake, mountain scenery and reflection. |
| Nine package categories | Three columns on large desktops (1200px+), two at 768–1199px and one below 768px; 200px top photos, equal-height cards within each row and aligned enquiry buttons. Original package text and commercial values preserved. |
| Contact | Clean transparent heading and two-column form/email/guidance layout; white form, green top accent and closer field spacing. Existing draft/copy behavior and active green Contact link preserved. |
| Homepage / gallery / About | Hero, content and working gallery/About design preserved. Homepage preview frames are equally sized landscapes; existing filters, descriptive captions, lightbox and team framing remain. |
| Motion | Preserved hero stagger, scroll reveals, menu motion, slider/caption transitions, gallery interpolation and lightbox fade. Added gentle package-card lift/shadow; large guide photos remain stationary. No animation library added. |

**All twelve guides use the shared wide-content design.** Seven scenic photos use a 2.4–2.5:1 desktop crop; Khunjerab, Kalash, Mushkpuri, Rakaposhi and Tolipeer keep natural ratios to protect people, livestock and tents. These are the permitted subject-sensitive exceptions, rather than forced panoramic crops. Phones use a gentler 16:9 scenic frame. No filler side bands or distorted images were detected.

## Screenshots

Before images were captured from an isolated read-only export of `77f3079`; after images show this refinement. Static captures disable animations to show completed layouts.

| Page / width | Before | After |
| --- | --- | --- |
| index · 375px | [Before](design/before/index-375.png) | [After](design/after/index-375.png) |
| index · 768px | [Before](design/before/index-768.png) | [After](design/after/index-768.png) |
| index · 1440px | [Before](design/before/index-1440.png) | [After](design/after/index-1440.png) |
| tour · 375px | [Before](design/before/tour-375.png) | [After](design/after/tour-375.png) |
| tour · 768px | [Before](design/before/tour-768.png) | [After](design/after/tour-768.png) |
| tour · 1440px | [Before](design/before/tour-1440.png) | [After](design/after/tour-1440.png) |
| destination · 375px | [Before](design/before/destination-375.png) | [After](design/after/destination-375.png) |
| destination · 768px | [Before](design/before/destination-768.png) | [After](design/after/destination-768.png) |
| destination · 1440px | [Before](design/before/destination-1440.png) | [After](design/after/destination-1440.png) |
| saral · 375px | [Before](design/before/saral-375.png) | [After](design/after/saral-375.png) |
| saral · 768px | [Before](design/before/saral-768.png) | [After](design/after/saral-768.png) |
| saral · 1440px | [Before](design/before/saral-1440.png) | [After](design/after/saral-1440.png) |
| Mushkpuri · 375px | [Before](design/before/Mushkpuri-375.png) | [After](design/after/Mushkpuri-375.png) |
| Mushkpuri · 768px | [Before](design/before/Mushkpuri-768.png) | [After](design/after/Mushkpuri-768.png) |
| Mushkpuri · 1440px | [Before](design/before/Mushkpuri-1440.png) | [After](design/after/Mushkpuri-1440.png) |
| khunjerab · 375px | [Before](design/before/khunjerab-375.png) | [After](design/after/khunjerab-375.png) |
| khunjerab · 768px | [Before](design/before/khunjerab-768.png) | [After](design/after/khunjerab-768.png) |
| khunjerab · 1440px | [Before](design/before/khunjerab-1440.png) | [After](design/after/khunjerab-1440.png) |
| treking · 375px | [Before](design/before/treking-375.png) | [After](design/after/treking-375.png) |
| treking · 768px | [Before](design/before/treking-768.png) | [After](design/after/treking-768.png) |
| treking · 1440px | [Before](design/before/treking-1440.png) | [After](design/after/treking-1440.png) |
| safarie · 375px | [Before](design/before/safarie-375.png) | [After](design/after/safarie-375.png) |
| safarie · 768px | [Before](design/before/safarie-768.png) | [After](design/after/safarie-768.png) |
| safarie · 1440px | [Before](design/before/safarie-1440.png) | [After](design/after/safarie-1440.png) |
| contact · 375px | [Before](design/before/contact-375.png) | [After](design/after/contact-375.png) |
| contact · 768px | [Before](design/before/contact-768.png) | [After](design/after/contact-768.png) |
| contact · 1440px | [Before](design/before/contact-1440.png) | [After](design/after/contact-1440.png) |

[Gallery](design/after/gallery-1440.png) · [About](design/after/about-1440.png)

Visual review sheets include every guide, category and page at all three representative widths:

- 375px: [12 guides](design/guides-375.jpg) · [9 categories](design/categories-375.jpg) · [28 page viewports](design/pages-375.jpg)
- 768px: [12 guides](design/guides-768.jpg) · [9 categories](design/categories-768.jpg) · [28 page viewports](design/pages-768.jpg)
- 1440px: [12 guides](design/guides-1440.jpg) · [9 categories](design/categories-1440.jpg) · [28 page viewports](design/pages-1440.jpg)

## Actual browser checks

- **954 local references and 252 page/width cases**, all 28 pages at 320, 375, 390, 576, 768, 991, 1024, 1440 and 1920px. No detected missing images, distorted renders, clipped headings, horizontal overflow, HTTP errors or JavaScript/console errors. The extra 576/991px checks supplement the seven requested widths. All heading levels were measured and visually reviewed.
- **108 guide frame/title checks** at all nine widths. **161 design cases** at the seven requested widths check all twelve guide headers, photo widths/content split, nine package grids/200px images/button alignment, both slider proportions and unchanged package text. Additional checks verify equal homepage preview heights, clean Contact heading and real hover/reduced-motion changes.
- **14 interaction groups** passed, including real autoplay/manual controls/pause/resume, keyboard and touch behavior, reduced motion/live preferences, menu/skip link, gallery filters/dialog keys/focus containment/return, enquiry prefill/validation/preparation/copy/reset and no-JavaScript fallbacks.
- **21 guide/category entrance checks plus two rapid-filter/live-preference checks** passed. **11 recording/motion checks** observed three real automatic transitions on each desktop slideshow, manual arrows/indicators and recovery, mobile autoplay/taps/menu, hero/scroll/hover/gallery/dialog animation and reduced motion.
- **56 stable axe-core 4.10.3 WCAG 2/2.1 A/AA scans** (28 pages at 375/1440px) reported zero violations after entrances completed. Automated scans do not establish full accessibility conformance.
- All 28 landscape and viewport-equivalent 200% zoom-reflow cases passed, as did eleven representative doubled-text cases. Native browser zoom was not tested.

[Layout/headings/guide evidence](design/layout-results.json) · [Design and preserved-package checks](design/design-results.json) · [Interactions](design/interaction-results.json) · [Guide/category motion](design/motion-pages-results.json) · [Accessibility](design/accessibility-results.json)

The main matrix preceded the final price-spacing/overlay polish; the design checks and captures were rerun after those adjustments, and the 56 accessibility scans were repeated. A timing-sensitive menu assertion was changed to observe actual Web Animations API creation/timing instead of depending on an animation still running when an input call returns. No site behavior was disabled to make checks pass.

## Recorded animation evidence

[Desktop browser recording](design/desktop-motion.webm) · [Mobile browser recording](design/mobile-motion.webm) · [Observed events](design/final-results.json)

The recorded hero was sampled mid-entrance at opacity 0.219353 with a 14px vertical offset; heading, subtitle and action animation starts were separately observed at approximately 623ms, 684ms, 782ms. Recordings use actual Chromium frames and real timers, not CSS-class inspection. They include hero/title/subtitle/action entrances, scrolling, hover, repeated automatic/manual slides, gallery reflow/lightbox and menu/reduced-motion behavior. Playwright used installed system FFmpeg through a QA-only browser cache; no runtime dependency was added. Reproduce with the commands in README; run recording checks separately from heavy screenshot work for a smooth capture.

## Modified files

Source changes are the twelve guide HTML files, `assets/css/photography.css`, `assets/css/editorial.css`, `assets/css/motion.css`, the proportion/recording assertions in `scripts/check_final.py`, and new `scripts/check_design.py`. README, AUDIT and this review/evidence directory are updated. The nine category HTML files receive the shared CSS grid without markup or content changes. Directory, homepage, About, Contact and gallery markup is unchanged; their requested visual refinements use shared CSS. [Exact changed-file list](design/changed-files.txt).

## Unresolved content and image limitations

All 108 used photograph sources were reviewed in thumbnail sheets and new rendered layouts; original files are unchanged. Some package sources are low-resolution; Hunza’s 800px guide image may look soft at the requested width. CSS cannot recover detail. Watermarks remain in originals. Safari photos show mountain transport scenes rather than confirming the advertised desert/wildlife/jungle activities. Repeated imagery, foreign Great Wall/cactus/red-rock/Joshua-tree scenes, precise locations, usage rights and portrait identity matches require owner review. No unrelated replacement stock images or unverified place labels were added. [Image dimension inventory](design/image-inventory.json) and AUDIT record these limits.

Prices, discounts, durations, availability, inherited destination/access/history claims and social/email ownership remain unverified. Khunjerab retains owner-supplied copy, not independently researched facts. The new introductions summarize existing guide subjects and visible scenes without adding current travel promises. Physical devices, screen readers, other browsers, native zoom and external email delivery were not tested.

This refinement is provided on `codex/destination-pakistan-redesign` with explicit owner approval to commit and push. The branch ZIP includes the website and review evidence. No merge into `main` or deployment was performed.
