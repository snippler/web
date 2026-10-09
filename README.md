# markhasin.com

Static personal site. No framework, no build dependencies beyond Python 3.

    site/            <- this is the only thing you deploy
      index.html
      styles.css
      lev-markhasin.jpg / .webp
    build/           <- optional generator; do NOT deploy
      data.py        <- the publication and patent lists live here
      styles.py      <- the stylesheet
      gen.py         <- writes site/index.html and site/styles.css

## Updating

Either edit `site/index.html` directly (it is plain, readable HTML), or edit
`build/data.py` and regenerate:

    cd build && python3 gen.py

## Deploying

Serve the `site/` directory at the domain root. Everything is relative, so it
works from any subpath or straight off the filesystem.

- GitHub Pages: push the repo, set Pages source to `/site`.
- Netlify / Cloudflare Pages: publish directory = `site`, no build command.
- Plain hosting: upload the four files in `site/`.

Local check:

    python3 -m http.server -d site 8000

## Privacy note

`CV_Markhasin.pdf` and `CV_Markhasin.tex` in the repository root contain a home
address and mobile number. They are deliberately outside `site/` and are not
linked from the page. Keep them out of whatever you deploy — if you host this
from a public Git repo, put them in `.gitignore` or move them elsewhere.
