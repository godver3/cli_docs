# Clyde Documentation

MkDocs + Material theme documentation site.

## Local preview

```bash
pip install mkdocs-material
mkdocs serve
```

Then open http://localhost:8000

## Build

```bash
mkdocs build
```

## Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

## Structure

```
cli/
  mkdocs.yml              # Site config
  docs/
    index.md              # Home page
    installation/
      index.md            # Installation overview
      docker.md           # Docker guide
      windows.md          # Windows guide
      unraid.md           # Unraid guide
      updating.md         # Updating guide
    assets/
      screenshots/        # Add your screenshots here
        installation/     # Screenshots for install pages
      images/             # Logo, favicon
```

## Logo and Favicon

Drop your logo and favicon into `docs/assets/images/`:

- `docs/assets/images/logo.svg` — site logo (shown in top-left nav bar)
- `docs/assets/images/favicon.png` — browser tab icon, recommended 32×32px

Then uncomment these two lines in `mkdocs.yml`:
```yaml
logo: assets/images/logo.svg
favicon: assets/images/favicon.png
```
And remove (or comment out) the `icon: logo:` line below them.

## Screenshots

Screenshots are referenced as placeholders throughout the docs.
Drop your real screenshots into `docs/assets/screenshots/` matching the filenames used in the markdown files.

All installation screenshots go in: `docs/assets/screenshots/installation/`
