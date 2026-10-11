# Final refinement review

Targeted corrections to the existing development branch. Before screenshots represent `026535a`; after screenshots represent this local refinement. The owner approved committing and pushing this refinement to the existing development branch. No merge into `main` or deployment was performed.

## Audit and changes

| Issue | Root cause and correction |
| --- | --- |
| Directory sliders dominated the desktop viewport | Their height reached 760px. Both now use `clamp(300px, 36vw, 520px)` with a separate phone rule. At 1440px, height is approximately 518px, a 32% reduction. First-row cards enter the viewport about 240px earlier. Titles, arrows, indicators and 750ms transitions remain. |
| Grey destination-photo side bands | A full-width grey flex frame surrounded a narrower image using `contain` and a fixed height. Shared frames now fit their photographs, have no background filler, and use 16:9 cover for appropriate landscapes. Photos with people, livestock or foreground tents use their natural ratio to preserve subjects. Native-width limits remain. |
| Destination title/photo alignment | All twelve guides use the same title-before-image structure, typography and spacing. The real browser measured title placement and image/frame boundaries at every tested width. |
| Oversized package imagery | Rows formerly allocated over half their width and at least 280px height to imagery. Nine categories now use a roughly one-third image/two-thirds text split, a 280px image-height limit, compact body spacing and clear metadata; phone layouts stack. All package text and values are unchanged. |
| Contact filler photograph | Removed the unrelated night scene. The right column now leads with the existing email, practical trip-detail guidance and the email-draft workflow. No contact details, backend or booking capability were invented. |
| Motion was too limited to be apparent | Previous observation targeted a few headings and frames. Actual staggered hero fades, selected content/profile/package/photograph reveals, hover zoom, animated menu opening/closing, sliding captions, gallery position/height interpolation and lightbox fades are now implemented and browser-tested. Large destination hero photos do not move. |

The homepage hero design, palette, route names, gallery content, Khunjerab copy, original photograph files, team biographies and enquiry functionality were preserved. Hover/focus feedback is about 200–220ms; reveals are 550ms; hero entrances are 600ms with 90ms staggering; slider movement is 750ms. Content stays visible without JavaScript and reduced-motion preferences suppress animation. Body-text reveals use movement at full opacity; the requested hero entrance uses a short fade.

## Screen recordings and reproducible evidence

- [Desktop recording · 68 seconds](final/desktop-motion.webm): hero stagger, scrolling/hover, both directory sliders over multiple automatic transitions, manual arrows/indicators, gallery reflow/lightbox and representative page entrances.
- [Mobile recording · 21 seconds](final/mobile-motion.webm): menu opening/closing, repeated touch autoplay, arrow recovery and reduced-motion behavior.
- [Recorded animation/slider events](final/final-results.json) include a hero sample with opacity 0.219 and a 14px upward offset during its entrance, plus three distinct hero animation starts. These are browser observations rather than initialization-only checks.
- [All-guide/category motion checks](final/motion-pages-results.json) cover twelve guides, nine package pages, rapid gallery switching and live motion-preference changes.

The recordings are real-time Chromium captures. Download/open WebM files if the file viewer cannot play them. Playwright recording uses FFmpeg; this environment used its installed system binary through a QA-only cache. No runtime dependency was added to the site.

## Before and after

All seven requested comparison pages are included at phone, tablet and desktop widths. Open each image to inspect the full page.

| Page and width | Before | After |
| --- | --- | --- |
| tour · 375px | [Before](final/before/tour-375.png) | [After](final/after/tour-375.png) |
| tour · 768px | [Before](final/before/tour-768.png) | [After](final/after/tour-768.png) |
| tour · 1440px | [Before](final/before/tour-1440.png) | [After](final/after/tour-1440.png) |
| destination · 375px | [Before](final/before/destination-375.png) | [After](final/after/destination-375.png) |
| destination · 768px | [Before](final/before/destination-768.png) | [After](final/after/destination-768.png) |
| destination · 1440px | [Before](final/before/destination-1440.png) | [After](final/after/destination-1440.png) |
| khunjerab · 375px | [Before](final/before/khunjerab-375.png) | [After](final/after/khunjerab-375.png) |
| khunjerab · 768px | [Before](final/before/khunjerab-768.png) | [After](final/after/khunjerab-768.png) |
| khunjerab · 1440px | [Before](final/before/khunjerab-1440.png) | [After](final/after/khunjerab-1440.png) |
| Mushkpuri · 375px | [Before](final/before/Mushkpuri-375.png) | [After](final/after/Mushkpuri-375.png) |
| Mushkpuri · 768px | [Before](final/before/Mushkpuri-768.png) | [After](final/after/Mushkpuri-768.png) |
| Mushkpuri · 1440px | [Before](final/before/Mushkpuri-1440.png) | [After](final/after/Mushkpuri-1440.png) |
| treking · 375px | [Before](final/before/treking-375.png) | [After](final/after/treking-375.png) |
| treking · 768px | [Before](final/before/treking-768.png) | [After](final/after/treking-768.png) |
| treking · 1440px | [Before](final/before/treking-1440.png) | [After](final/after/treking-1440.png) |
| contact · 375px | [Before](final/before/contact-375.png) | [After](final/after/contact-375.png) |
| contact · 768px | [Before](final/before/contact-768.png) | [After](final/after/contact-768.png) |
| contact · 1440px | [Before](final/before/contact-1440.png) | [After](final/after/contact-1440.png) |
| index · 375px | [Before](final/before/index-375.png) | [After](final/after/index-375.png) |
| index · 768px | [Before](final/before/index-768.png) | [After](final/after/index-768.png) |
| index · 1440px | [Before](final/before/index-1440.png) | [After](final/after/index-1440.png) |

## Browser QA actually executed

- 954 local link/asset/fragment checks; 252 page/width cases: every one of 28 pages at 320, 375, 390, 576, 768, 991, 1024, 1440 and 1920px. The extra 991px breakpoint supplements the eight requested widths. No detected HTTP errors, broken/distorted images, JavaScript errors, heading clipping or horizontal overflow.
- **108 destination frame/title checks across all twelve routes**: image and intended frame boundaries match, frame background is transparent, and the destination title precedes the image. Grey filler bands are gone at all tested sizes.
- 28 landscape layouts, 28 viewport-equivalent 200% zoom-reflow checks and eight doubled-text checks passed. Native browser zoom itself was not tested.
- Fourteen focused interaction groups passed, including autoplay/manual arrows, hover/focus pause and resume, reduced motion, one-image controls, menu/skip link, gallery filters/dialog keyboard behavior, required/invalid fields, enquiry prefill/preparation/copy/reset and no-JavaScript fallbacks.
- Eleven recording/proportion/motion checks passed, including three actual automatic transitions on each desktop directory, manual indicators/arrows and recovery, touch autoplay, hover effects, gallery interpolation, lightbox fade and reduced motion.
- Twenty-one guide/category animation checks and two rapid-filter/live-preference checks passed. No large-guide-photo animations were detected.
- Axe-core 4.10.3 found zero WCAG 2/2.1 A/AA violations in 56 stable page/width cases. Scans waited for entrance animations to finish. This does not establish full accessibility conformance.
- All 28 rendered pages were visually reviewed in phone/tablet/desktop contact sheets; the seven comparison pages have full-page captures. The 108 used photograph sources were reviewed in thumbnail sheets for subjects, watermarks, resolution and provenance concerns.

Machine-readable results are linked above and in [layout results](final/layout-results.json), [interaction results](final/interaction-results.json), and [accessibility results](final/accessibility-results.json). Reproducible scripts live in `scripts/`. [Changed file list](final/changed-files.txt) identifies source and review artifacts.

## Remaining limitations

Original low-resolution photographs remain a constraint. Watermarks from Pakistan Travel Places and other photographers are preserved in the originals. `tour/china.jpg` depicts the Great Wall and is retained for the original Overland category; gallery red-rock/cactus/Joshua-tree images may depict locations outside Pakistan. Precise locations, ownership, usage rights and team-portrait identities are not verified. No new Pakistani place names or unrelated stock photographs were substituted.

Khunjerab remains based on owner-supplied copy because independent research access was previously blocked. Current guide facts, prices/availability, conflicting founder names and email/social ownership still need owner confirmation. Physical devices, screen readers, non-Chromium browsers, native zoom controls and actual external email delivery were not tested.

The final refinement is provided on `codex/destination-pakistan-redesign` with explicit owner approval to commit and push. The before screenshots represent `026535a`; `main` is unchanged.
