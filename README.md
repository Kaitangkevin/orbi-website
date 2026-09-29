# Orbi website

Bilingual product website for Orbi for Mac.

## Website content

- `dist/product.js`: product presentation and interactive demos
- `dist/pages.js`: download guide and about page
- `dist/app.js`: shared navigation and language preference
- `dist/style.css`: styling and responsive layouts
- `dist/assets/`: images
- `dist/downloads/Orbi-1.0.dmg`: downloadable installer

## Deployment

Pushing to `main` deploys `dist/` to GitHub Pages using GitHub Actions.
`scripts/build-pages.py` adjusts root-relative links for the Pages base path.
The source files keep their original paths for local previews and Sites hosting.
Only the generated `_site` directory is published, not repository metadata.

For a local preview: `python3 -m http.server 4173 --directory dist`.

The installer is currently unsigned with Apple Developer ID. See the download
page for first-launch guidance. This repository contains the website, not the
native application's source code.
