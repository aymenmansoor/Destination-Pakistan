# Destination Pakistan

A refined responsive travel website for exploring Pakistan’s destinations, landscapes, cultural heritage, and tour packages. The redesign keeps the original project’s identity, photographs, destination descriptions, package listings, and page filenames.

## What’s included

- A scrollable homepage with a photographic hero, overview, featured destinations, tour categories, gallery showcase, and enquiry links.
- Twelve destination guides and a destination index.
- Nine tour categories with the original package descriptions, durations, prices, and discounts.
- A 24-photo gallery with mountain, desert, and coastal filters.
- An about page with the original story and seven team profiles.
- A contact form that prepares an email draft or copies an enquiry; it does not send or store submissions.
- Responsive navigation, keyboard focus styles, a skip link, breadcrumbs, shared footer, descriptive image text, and reduced-motion support.
- Locally hosted Bootstrap 5.0.2: styles, navigation enhancements, and slideshow controls work without a CDN connection.

## Technologies

Plain HTML, CSS, JavaScript, and Bootstrap 5. No build tools, framework, database, or package installation is required. Fonts use the visitor’s system fonts: Georgia for display headings and Arial/Helvetica for body text.

## Run locally

From the repository directory, with Python 3 installed:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open your browser at localhost on port 8000. `index.html` is the homepage. `front.html` retains the same homepage for existing links and bookmarks. Use Ctrl+C in the terminal to stop the server.

A local web server is recommended instead of opening files directly: clipboard permissions and other browser APIs work more reliably over localhost. The site can also be served by a static hosting provider without a build step.

## Project structure

```text
Destination-Pakistan/
├── index.html                   # Default homepage
├── front.html                   # Original homepage route, retained
├── destination.html             # Destination directory
├── tour.html                    # Tour category directory
├── gallery.html                 # Photo gallery
├── about.html                   # Original story and team
├── contact.html                 # Email enquiry form
├── [destination pages].html     # 12 existing guides
├── [tour category pages].html   # 9 existing package categories
├── assets/
│   ├── css/site.css             # Entry point importing small CSS modules
│   ├── js/site.js               # Menu, filtering and enquiry enhancement
│   ├── js/carousels.js          # Automatic slideshows and motion preferences
│   ├── js/gallery.js            # Keyboard-accessible photo dialog
│   ├── js/motion.js             # Progressive scroll/filter animation
│   ├── favicon.svg
│   └── vendor/bootstrap/        # Bootstrap 5.0.2 and its MIT license
├── destinations/               # Original destination photographs
├── tour/                       # Original tour and team photographs
├── kashmir/                    # Mountain gallery photographs
├── desert/                     # Desert gallery photographs
├── Sea Side/                   # Coastal gallery photographs
├── styleh.css                  # Legacy stylesheet compatibility path
├── style2.css                  # Legacy gallery stylesheet compatibility path
├── AUDIT.md                    # Findings, content issues, and review notes
├── scripts/                    # Optional Python/Playwright QA tools
├── docs/FINAL.md                # Current screenshots, videos and QA evidence
├── docs/PREMIUM.md              # Previous refinement evidence
├── docs/REFINEMENT.md           # Earlier refinement review
└── .gitignore
```

Filenames containing spaces or capital letters remain unchanged to preserve existing routes. Keep their spelling and capitalization when linking to them. Images are kept in their original folders to avoid breaking references.

## Editing the website

Edit HTML content directly. `assets/css/site.css` imports styles organized by responsibility: base, navigation, homepage, cards, pages, slideshows, gallery/contact, footer, and responsive layouts. Palette variables live in `assets/css/base.css`. `photography.css` controls cinematic directories and shared destination frames; `editorial.css` controls package rows, homepage details, and Contact; `motion.css` defines restrained animations. Common navigation and footer markup is present in each page so the site needs no templating runtime. When changing navigation, update every page consistently. Keep `index.html` and `front.html` synchronized.

Bootstrap’s responsive `.row`, `.col-*`, and `.g-*` classes arrange cards. The shared CSS controls typography, image cropping, buttons, and page spacing. `assets/js/site.js` adds small interactions; ordinary links and all content remain available when JavaScript is disabled. Gallery filtering, the photo dialog, and clipboard copying require JavaScript. Without JavaScript, every gallery thumbnail links directly to its original photograph.

The directory slideshows advance approximately every five seconds. Hover over controls, visible keyboard focus, active pointer interaction, and hidden tabs pause them; autoplay resumes when those conditions end. Reduced-motion preferences disable autoplay while keeping arrows available. Passive pointer placement on photographs keeps playback running. Touching an arrow does not leave an indefinite focus pause. The module uses one timer per carousel and suppresses controls for one-image sliders. Gallery photographs can be opened in a native dialog with previous/next controls, arrow-key navigation, Escape to close, and focus returned to the selected thumbnail.

Bootstrap was downloaded from the project’s existing 5.0.2 URLs and checked against the original SHA-384 integrity hashes. The unmodified files are committed locally. Its license is included beside the files. No external font or icon library is required; social links have readable text labels.

## Enquiries and bookings

Package buttons link to `contact.html?tour=...` and prefill the subject. Required name, email, and message fields use browser validation. **Prepare email** reveals an **Open email draft** link. That link opens the visitor’s configured email application with a draft, which they must send themselves. **Copy enquiry** copies the text when the browser allows clipboard access. Nothing is automatically sent or persisted, and no booking or payment is created.

Without a configured email app, copy the enquiry into an email manually. Without JavaScript, the form uses a `mailto:` action; browser support varies, so the direct email link is also available.

## Known content limitations

- Khunjerab now has a visitor guide based on owner-supplied copy, with qualified seasonal/access advice. Independent source verification was blocked by the environment’s network policy (403 responses); no current crossing schedule, road condition, pricing, or availability is asserted.
- The placeholder phone number has been removed from Contact. The existing email and social links remain; a verified phone number can be added when supplied by the owner.
- Package prices, discounts, durations, and availability have not been independently verified. A notice asks visitors to confirm them before planning travel.
- The about page’s founder names and team co-founder names conflict. Original names and roles are preserved for owner review, rather than inventing replacements. See `AUDIT.md`.
- The original homepage’s “over two decades” experience claim is not corroborated by the about page; it is no longer promoted. The rest of the overview remains.
- Destination descriptions contain inherited historical, seasonal, access, and safety claims. They need editorial review before being relied on for current travel decisions.
- Social account ownership, responses from the listed email address, actual email delivery, and the rights to original photographs have not been verified.

## Final refinement

Both directory sliders remain wide but now have a 520px maximum height, approximately one-third shorter than the previous 760px design. Destination photos fill their intended containers without grey side bands; safe landscapes use 16:9 cropping, while subject-sensitive photos retain their natural ratio. All twelve guides share a title-before-image structure and source-width limits. Package categories use compact editorial rows with a smaller image share and prominent prices/durations. Contact uses the form alongside email and useful enquiry guidance; its filler photograph was removed.

The existing homepage hero and palette are preserved. Hero heading/subtitle/actions now fade and rise with 90ms staggering. Selected destination content, featured images, packages, team profiles and Contact blocks reveal on scroll. Navigation has animated underlines and mobile opening/closing; gallery changes interpolate positions and grid height, and the lightbox fades in. Hover/field/button feedback is restrained. Large destination hero photographs do not move. Content remains visible without JavaScript; reduced-motion changes cancel effects safely.

## Validation

The current refinement passed **954 local link/asset checks** and **252 Chromium page/width cases**: all 28 routes at 320, 375, 390, 576, 768, 991, 1024, 1440, and 1920 pixels. Checks include all heading levels, image loading/proportions, footer reachability, HTTP/JavaScript failures, and horizontal overflow. Every destination guide passed frame-filling/background/title-position checks at every width: 108 checks across twelve routes. Additional checks cover 28 landscape layouts, 28 layouts with a viewport equivalent to 200% zoom reflow, and eight representative pages with 200% text size. This is not a test of Chromium's native browser-zoom UI.

Real-time recordings observe three automatic transitions on both desktop directories, manual arrows/indicators and automatic recovery; mobile checks observe repeated touch autoplay and recovery after tapping an arrow. Additional checks cover equal-height previews, repeated initialization, active navigation, and normal/reduced-motion animations. Fourteen interaction groups passed, including real five-second autoplay at phone/tablet/desktop sizes, manual navigation, hover/focus pause and resume, reduced motion, mobile navigation, filters, dialog keyboard behavior, validation, clipboard copying, and prepared email links. Eleven additional recording/motion/proportion checks passed, plus 21 guide/category animation checks and two rapid-filter/live-preference checks. Desktop and mobile WebM recordings, actual animation events and before/after screenshots are included in `docs/final/`. Axe-core 4.10.3 reported zero WCAG 2/2.1 A/AA violations in 56 page/width cases; automated accessibility checks do not establish full accessibility conformance.

Visual review used rendered phone, tablet, and desktop captures of all pages, with representative full-page inspection and before/after evidence in [the final refinement review](docs/FINAL.md). Physical devices, screen readers, other browsers, native browser zoom, external mail applications, actual email delivery, and social-account ownership remain untested.

To reproduce the browser checks, install Playwright in a separate development environment (not required to run the website), keep the local server running, and use:

```sh
python3 -m pip install playwright
python3 -m playwright install chromium ffmpeg
python3 scripts/check_pages.py
python3 scripts/check_interactions.py
python3 scripts/check_final.py
python3 scripts/check_motion_pages.py
```

The scripts use installed system Chromium when available, otherwise Playwright's browser. Results and screenshots go to ignored `.qa-output/`; `--base-url` and `--output` can override defaults. The recording check requires Playwright FFmpeg; this environment used the installed system FFmpeg through a QA-only cache. The axe scan was a separate QA run, not a runtime dependency. Static screenshots disable animation to capture completed layouts; the recordings and motion scripts verify normal animation and reduced motion separately.

## Upload to GitHub

The final refinement is provided on `codex/destination-pakistan-redesign` with explicit owner approval to commit and push. Download this development branch to obtain the refined site and review evidence. `main` is unchanged; no deployment has been performed.

To download from GitHub, select that branch on the repository page, then choose **Code → Download ZIP**. Extract the archive and follow the local run instructions above.

If you downloaded the ZIP, it intentionally excludes Git history. Extract it, then copy the contents of its `Destination-Pakistan` folder into your existing repository clone. Include the `.gitignore` file and leave the clone’s `.git` directory intact. Do not nest another `Destination-Pakistan` folder inside your repository. The steps below run from that clone.

1. Review the website and outstanding content questions in `AUDIT.md`.
2. Check changes with `git status` and `git diff`.
3. When satisfied, stage the intended files with `git add .` and create your own commit.
4. Push to your repository using your authenticated Git client.
5. For GitHub Pages, choose the desired branch and root folder in the repository’s Pages settings. No build command is needed.

Review your remote and branch before pushing. Keep credentials out of source files. The `.gitignore` excludes local secrets, editor files, logs, test outputs, and dependency caches.
