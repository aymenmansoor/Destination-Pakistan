# Development checks

These optional tools run in a separate Python verification environment. They are not required to view or host the website.

Install Python packages `playwright` and `lxml`, then install Playwright Chromium with `python3 -m playwright install chromium`. The scripts use system Chromium when available. Start a local web server from the project root before running:

```sh
python3 scripts/check_pages.py
python3 scripts/check_interactions.py
python3 scripts/check_design.py
python3 scripts/check_motion_pages.py
```

These checks cover local page references, responsive layouts, image loading, slideshow controls, gallery interactions, enquiry drafts, and motion preferences. `check_final.py` additionally records desktop and mobile interactions and requires Playwright FFmpeg (`python3 -m playwright install ffmpeg`).

Each script accepts `--base-url` and `--output`. Generated results default to ignored `.qa-output/`. Automated checks supplement visual inspection and do not verify external email delivery or current travel information.
