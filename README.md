# Destination Pakistan

A responsive travel website for exploring Pakistan’s destinations, landscapes, cultural heritage, and tour packages. The redesign keeps the original project’s identity, photographs, destination descriptions, package listings, and page filenames.

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
│   ├── css/site.css             # Shared layout, components, responsive styles
│   ├── js/site.js               # Menu, gallery, slideshows, enquiry enhancement
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
└── .gitignore
```

Filenames containing spaces or capital letters remain unchanged to preserve existing routes. Keep their spelling and capitalization when linking to them. Images are kept in their original folders to avoid breaking references.

## Editing the website

Edit HTML content directly. Shared colors and component styles are in `assets/css/site.css`; its `:root` variables define the palette. Common navigation and footer markup is present in each page so the site needs no templating runtime. When changing navigation, update every page consistently. Keep `index.html` and `front.html` synchronized.

Bootstrap’s responsive `.row`, `.col-*`, and `.g-*` classes arrange cards. The shared CSS controls typography, image cropping, buttons, and page spacing. `assets/js/site.js` adds small interactions; ordinary links and all content remain available when JavaScript is disabled. Gallery filtering and clipboard copying require JavaScript.

Bootstrap was downloaded from the project’s existing 5.0.2 URLs and checked against the original SHA-384 integrity hashes. The unmodified files are committed locally. Its license is included beside the files. No external font or icon library is required; social links have readable text labels.

## Enquiries and bookings

Package buttons link to `contact.html?tour=...` and prefill the subject. Required name, email, and message fields use browser validation. **Prepare email** reveals an **Open email draft** link. That link opens the visitor’s configured email application with a draft, which they must send themselves. **Copy enquiry** copies the text when the browser allows clipboard access. Nothing is automatically sent or persisted, and no booking or payment is created.

Without a configured email app, copy the enquiry into an email manually. Without JavaScript, the form uses a `mailto:` action; browser support varies, so the direct email link is also available.

## Known content limitations

- The original Khunjerab page incorrectly duplicated Mushkpuri’s description and pictures. The Mushkpuri guide is preserved on its correct page; Khunjerab now uses an existing Khunjerab photograph and openly states that a verified guide is needed.
- The original phone number `+1234567890` appears to be a placeholder. It is retained with a warning; use the existing email address until the owner confirms a valid number.
- Package prices, discounts, durations, and availability have not been independently verified. A notice asks visitors to confirm them before planning travel.
- The about page’s founder names and team co-founder names conflict. Original names and roles are preserved for owner review, rather than inventing replacements. See `AUDIT.md`.
- The original homepage’s “over two decades” experience claim is not corroborated by the about page; it is no longer promoted. The rest of the overview remains.
- Destination descriptions contain inherited historical, seasonal, access, and safety claims. They need editorial review before being relied on for current travel decisions.
- Social account ownership, responses from the listed email address, actual email delivery, and the rights to original photographs have not been verified.

## Validation

The redesign was exercised in headless Chromium at 375, 768, and 1440 pixels across all 28 HTML pages (84 page/viewport combinations). Checks covered HTTP errors, loaded images, horizontal overflow, working navigation controls, gallery filters, slideshow controls, enquiry subject prefill, required-field validation, clipboard copying, and email-draft link preparation. Static checks verified local links, fragment targets, assets, unique IDs, and one main heading per page. Mobile navigation and full gallery content were also checked without JavaScript.

Preparing the email draft and its encoded mailto link was checked through the form handler; opening an external mail application and actual delivery were not tested. Social accounts were not tested. Physical devices, assistive technologies, and other browsers still need manual review. See `AUDIT.md` for the final review record.

For future edits, serve the site and review the homepage, destination directory, a destination guide, tour packages, gallery, about, and contact pages at phone and desktop sizes. Check the page footer is reachable and that changed links or images load.

## Upload to GitHub

The redesign is provided on the `codex/destination-pakistan-redesign` branch for review. The `main` branch is unchanged; no website deployment has been performed.

To download from GitHub, select that branch on the repository page, then choose **Code → Download ZIP**. Extract the archive and follow the local run instructions above.

If you downloaded the ZIP, it intentionally excludes Git history. Extract it, then copy the contents of its `Destination-Pakistan` folder into your existing repository clone. Include the `.gitignore` file and leave the clone’s `.git` directory intact. Do not nest another `Destination-Pakistan` folder inside your repository. The steps below run from that clone.

1. Review the website and outstanding content questions in `AUDIT.md`.
2. Check changes with `git status` and `git diff`.
3. When satisfied, stage the intended files with `git add .` and create your own commit.
4. Push to your repository using your authenticated Git client.
5. For GitHub Pages, choose the desired branch and root folder in the repository’s Pages settings. No build command is needed.

Review your remote and branch before pushing. Keep credentials out of source files. The `.gitignore` excludes local secrets, editor files, logs, test outputs, and dependency caches.
