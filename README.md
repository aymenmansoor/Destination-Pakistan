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
├── docs/DESIGN.md               # Current design review and browser evidence
├── docs/FINAL.md                # Previous refinement evidence
├── docs/PREMIUM.md              # Previous refinement evidence
├── docs/REFINEMENT.md           # Earlier refinement review
└── .gitignore
```

Filenames containing spaces or capital letters remain unchanged to preserve existing routes. Keep their spelling and capitalization when linking to them. Images are kept in their original folders to avoid breaking references.

## Editing the website

Edit HTML content directly. `assets/css/site.css` imports styles organized by responsibility: base, navigation, homepage, cards, pages, slideshows, gallery/contact, footer, and responsive layouts. Palette variables live in `assets/css/base.css`. `photography.css` controls cinematic directories and shared destination frames; `editorial.css` controls package grids, homepage details, and Contact; `motion.css` defines restrained animations. Common navigation and footer markup is present in each page so the site needs no templating runtime. When changing navigation, update every page consistently. Keep `index.html` and `front.html` synchronized.

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

## Current design refinement

Both directory sliders share a centered 1,050px maximum width, 380px desktop height, 10px corners, lower-left 32px captions and a 30px gap before the cards. Their five-second autoplay, arrows, indicators, keyboard handling and reduced-motion behavior are preserved.

All twelve guides now share warm-ivory headings, breadcrumbs, a destination label and a concise introduction. Their main photographs span the 1,050px content area without filler bands. Seven scenic photographs use a 2.4–2.5:1 desktop frame; five subject-sensitive photographs keep their natural ratio to protect people, livestock and tents. Phones use a gentler landscape crop. Main copy and the compact beige enquiry card split two-thirds/one-third above the mobile breakpoint. Existing low-resolution files remain a quality limitation; see the photo review in [AUDIT.md](AUDIT.md).

All nine package categories use three-column card grids on large desktops, two columns on tablets and one on phones. Cards have 200px photographs, aligned enquiry buttons and restrained hover lift/shadow/zoom. Original descriptions, durations, prices and discounts are unchanged and remain subject to confirmation. The homepage hero, gallery filters/lightbox and About content are preserved. The homepage gallery preview uses equal landscape frames. Contact retains its clean form/email/guidance layout, white form and green active navigation button, with tighter field spacing.

Existing hero stagger, content reveals, menu transitions, slider captions, gallery interpolation and lightbox fades continue to work. Large guide photographs do not animate. Content remains visible without JavaScript and motion preferences suppress effects. [Review screenshots, recordings, modified files and remaining limitations](docs/DESIGN.md).

## Validation

The current refinement passed **954 local references and 252 Chromium page/width cases**: all 28 pages at 320, 375, 390, 576, 768, 991, 1024, 1440 and 1920px. No detected broken/distorted images, clipped headings, horizontal overflow, HTTP errors or JavaScript/console errors. All twelve guide frames/title positions passed at all nine widths (108 checks). Additional landscape, viewport-equivalent 200% zoom reflow and representative doubled-text checks passed.

The design-specific script passed **161 cases** across the seven requested widths, verifying all twelve guide headings, photo widths and content splits, all nine category grids/image heights/button alignment, both compact sliders and unchanged package text. It also checked equal homepage gallery heights, clean Contact headings and actual card-hover/reduced-motion behavior. Interaction scripts passed 14 groups, 21 guide/category reveal checks and two rapid-filter/live-preference checks. Real desktop/mobile recordings demonstrate hero/scroll/menu/hover/gallery motion and repeated automatic/manual slide transitions. Axe-core 4.10.3 found zero WCAG 2/2.1 A/AA violations in 56 stable page/width scans; this does not establish full accessibility conformance.

[Current screenshots, recordings and results](docs/DESIGN.md) include phone/tablet/desktop comparisons, every guide/category in visual review sheets and the changed-file list. Physical devices, screen readers, other browsers, native browser zoom, external mail applications, actual email delivery and social-account ownership remain untested.

To reproduce the browser checks, use a separate QA environment, keep the local server running, and run:

```sh
python3 -m pip install playwright lxml
python3 -m playwright install chromium ffmpeg
python3 scripts/check_pages.py
python3 scripts/check_interactions.py
python3 scripts/check_design.py
python3 scripts/check_final.py
python3 scripts/check_motion_pages.py
```

Scripts use installed system Chromium when available. Results go to ignored `.qa-output/`; `--base-url` and `--output` can override defaults. Recording requires Playwright FFmpeg; this environment used system FFmpeg through a QA-only cache. Axe was a separate QA run, not a runtime dependency. Static screenshots capture completed layouts; recordings and motion scripts test normal motion and reduced motion separately.

## Upload to GitHub

The newest design refinement is provided on `codex/destination-pakistan-redesign` with explicit owner approval to commit and push. Download this development branch for the refined website, screenshots and browser evidence. `main` is unchanged; nothing has been deployed.

To download from GitHub, select that branch on the repository page, then choose **Code → Download ZIP**. Extract the archive and follow the local run instructions above.

If you downloaded the ZIP, it intentionally excludes Git history. Extract it, then copy the contents of its `Destination-Pakistan` folder into your existing repository clone. Include the `.gitignore` file and leave the clone’s `.git` directory intact. Do not nest another `Destination-Pakistan` folder inside your repository. The steps below run from that clone.

1. Review the website and outstanding content questions in `AUDIT.md`.
2. Check changes with `git status` and `git diff`.
3. When satisfied, stage the intended files with `git add .` and create your own commit.
4. Push to your repository using your authenticated Git client.
5. For GitHub Pages, choose the desired branch and root folder in the repository’s Pages settings. No build command is needed.

Review your remote and branch before pushing. Keep credentials out of source files. The `.gitignore` excludes local secrets, editor files, logs, test outputs, and dependency caches.
