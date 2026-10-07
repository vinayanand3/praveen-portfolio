# Praveen Mangalagiri — Portfolio

Single-page portfolio for a Design Release, NPI & Launch Engineer / Technical Program Manager.

`index.html` is self-contained: the headshot, the carousel images and the resume PDF are embedded as data URIs, so the page works when opened directly or hosted as a static site (GitHub Pages, Netlify, Vercel).

## Structure

```
index.html            The site (open in a browser)
assets/img/           Web-ready images (also embedded in index.html)
source/images/        Original images used to build the composites
source/resume/        Resume (PDF + DOCX)
tools/                Scripts that build the carousel composite images
notes/                Research and resume/LinkedIn strategy
```

## Rebuilding a composite image

Requires Python 3 with Pillow and NumPy. Run from the repo root:

```bash
python3 tools/compose_nissan.py
```

The scripts write to `assets/img/`. After regenerating an image, re-embed it in `index.html` (the carousel `<img src="data:...">`).
