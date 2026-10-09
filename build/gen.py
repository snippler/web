# -*- coding: utf-8 -*-
import os, html
import data as D
from styles import CSS

OUT = "/home/aloy/Documents/Website/site"
ART = os.environ.get("ART_OUT", "")
os.makedirs(OUT, exist_ok=True)
if ART: os.makedirs(ART, exist_ok=True)

E = html.escape

# ------------------------------------------------------------------ patents
CAT_LABEL = dict(D.CATS)
CAT_COUNT = {}
for p in D.PATENTS:
    CAT_COUNT[p["cat"]] = CAT_COUNT.get(p["cat"], 0) + 1

def patent_row(p):
    gp = "https://patents.google.com/patent/%s/en" % p["id"]
    status = "granted %s" % p["grant"][:4] if p["grant"] else "published %s" % p["pub"][:4]
    note = '<p class="row-sub">%s</p>' % E(p["note"]) if p["note"] else \
           '<p class="row-sub">Abstract not published in the search index.</p>'
    return (
      '<article class="row" data-cat="%s">'
        '<div class="row-meta">'
          '<span class="yr">filed %s</span>'
          '<a href="%s" target="_blank" rel="noopener">%s</a>'
          '<span class="tag">%s</span>'
        '</div>'
        '<div>'
          '<h3 class="row-title"><a href="%s" target="_blank" rel="noopener">%s</a></h3>'
          '%s'
          '<p class="row-sub" style="margin-top:.35rem;font-size:.8rem">%s · %s</p>'
        '</div>'
      '</article>'
    ) % (p["cat"], p["pri"][:4], gp, p["id"], CAT_LABEL[p["cat"]], gp, E(p["title"]), note, E(p["asg"]), status)

patent_filter = ['<button type="button" aria-pressed="true" data-cat="all">All<span class="count">%d</span></button>' % len(D.PATENTS)]
for key, label in D.CATS:
    patent_filter.append('<button type="button" aria-pressed="false" data-cat="%s">%s<span class="count">%d</span></button>'
                         % (key, label, CAT_COUNT[key]))

# ------------------------------------------------------------- publications
def authors_html(names):
    out = []
    for n in names:
        out.append('<span class="me">%s</span>' % E(n) if n == "Lev Markhasin" else E(n))
    return ", ".join(out)

def pub_row(p):
    primary = ("https://doi.org/" + p["doi"]) if p["doi"] else \
              ("https://arxiv.org/abs/" + p["arxiv"]) if p["arxiv"] else None
    title = E(p["title"])
    if primary:
        title = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (primary, title)
    chips = []
    if p["doi"]:
        chips.append('<a href="https://doi.org/%s" target="_blank" rel="noopener">DOI</a>' % p["doi"])
    if p["arxiv"]:
        chips.append('<a href="https://arxiv.org/abs/%s" target="_blank" rel="noopener">arXiv:%s</a>' % (p["arxiv"], p["arxiv"]))
    venue = '<span class="row-venue">%s</span>' % E(p["venue"])
    if p["detail"]:
        venue += " · " + E(p["detail"])
    kind_label = "AI &amp; computer vision" if p["kind"] == "ai" else "Mathematics"
    return (
      '<article class="row" data-cat="%s">'
        '<div class="row-meta"><span class="yr">%s</span><span class="tag">%s</span></div>'
        '<div>'
          '<h3 class="row-title">%s</h3>'
          '<p class="row-sub">%s</p>'
          '<p class="row-sub">%s</p>'
          '<div class="chips">%s</div>'
        '</div>'
      '</article>'
    ) % (p["kind"], p["year"], kind_label, title, authors_html(p["authors"]), venue, "".join(chips))

n_ai = sum(1 for p in D.PUBS if p["kind"] == "ai")
n_math = len(D.PUBS) - n_ai
pub_filter = [
  '<button type="button" aria-pressed="true" data-cat="all">All<span class="count">%d</span></button>' % len(D.PUBS),
  '<button type="button" aria-pressed="false" data-cat="ai">AI &amp; computer vision<span class="count">%d</span></button>' % n_ai,
  '<button type="button" aria-pressed="false" data-cat="math">Mathematics<span class="count">%d</span></button>' % n_math,
]

# -------------------------------------------------------------------- page
HEAD_LINKS = (
  '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
  '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
  '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
  'family=IBM+Plex+Mono:wght@400;500&'
  'family=IBM+Plex+Sans:wght@400;500;600&'
  'family=Newsreader:ital,opsz,wght@0,6..72,400..600;1,6..72,400&display=swap">'
)

SCRIPT = r"""
<script>
(function () {
  document.querySelectorAll("[data-filterset]").forEach(function (group) {
    var list = document.getElementById(group.dataset.filterset);
    if (!list) return;
    group.addEventListener("click", function (e) {
      var btn = e.target.closest("button[data-cat]");
      if (!btn) return;
      var want = btn.dataset.cat;
      group.querySelectorAll("button[data-cat]").forEach(function (b) {
        b.setAttribute("aria-pressed", String(b === btn));
      });
      list.querySelectorAll(".row").forEach(function (row) {
        row.classList.toggle("hidden-row", want !== "all" && row.dataset.cat !== want);
      });
    });
  });

  var root = document.documentElement,
      btn = document.getElementById("theme-btn");
  function label() {
    var dark = root.getAttribute("data-theme") === "dark" ||
      (!root.hasAttribute("data-theme") && window.matchMedia("(prefers-color-scheme: dark)").matches);
    btn.textContent = dark ? "Light" : "Dark";
  }
  try {
    var saved = localStorage.getItem("lm-theme");
    if (saved === "dark" || saved === "light") root.setAttribute("data-theme", saved);
  } catch (err) {}
  label();
  btn.addEventListener("click", function () {
    var dark = root.getAttribute("data-theme") === "dark" ||
      (!root.hasAttribute("data-theme") && window.matchMedia("(prefers-color-scheme: dark)").matches);
    var next = dark ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("lm-theme", next); } catch (err) {}
    label();
  });
})();
</script>
"""

BODY = """
<header class="nav">
  <div class="shell nav-in">
    <a class="nav-name" href="#top">Lev Markhasin</a>
    <a class="nav-link" href="#about">About</a>
    <a class="nav-link" href="#publications">Publications</a>
    <a class="nav-link" href="#patents">Patents</a>
    <button class="theme-btn" id="theme-btn" type="button">Dark</button>
  </div>
</header>

<main id="top">

<section class="hero" id="about">
  <div class="shell">
    <div class="hero-grid">
      <div>
        <h1>Dr. Lev Markhasin</h1>
        <p class="role">AI Engineer | Imaging World Models | Robotics</p>
        <div class="lede">
          <p>Senior AI expert and Team Leader with proven track record of excellence in the
             semiconductor industry with a focus on Edge AI, Generative AI and Agentic
             workflows. <strong>+15 years of experience</strong> at international scale
             including people management, project management, technical leadership, strategy,
             technology development and academic research. 49
             <a href="https://patents.google.com/?inventor=lev+markhasin&amp;oq=lev+markhasin" target="_blank" rel="noopener">patents</a>
             filed and 17 research
             <a href="https://scholar.google.com/citations?user=_mWX1EAAAAAJ&amp;hl=en&amp;oi=sra" target="_blank" rel="noopener">papers</a>
             published. A versatile problem-solver who thrives in fast-paced, cross-functional
             teams and multi-cultural environments. Innovation and success recognized by
             <strong>fast-track promotion</strong>, awards and rapidly increased
             responsibilities.</p>
        </div>

        <div class="linkrow">
          <a href="https://scholar.google.com/citations?user=_mWX1EAAAAAJ&amp;hl=en" target="_blank" rel="noopener">Google Scholar</a>
          <a href="https://patents.google.com/?inventor=lev+markhasin" target="_blank" rel="noopener">Google Patents</a>
        </div>
      </div>

      <figure class="portrait">
        <picture>
          <source srcset="lev-markhasin.webp" type="image/webp">
          <img src="lev-markhasin.jpg" width="667" height="1000" alt="Portrait of Lev Markhasin">
        </picture>
      </figure>
    </div>

    <dl class="track">
      <div><dt>2026&ndash;</dt><dd>Founder &mdash; <em>stealth</em></dd></div>
      <div><dt>2015&ndash;2026</dt><dd>Engineer to Team Leader, AI &mdash; <em>Sony Semiconductor Solutions, Stuttgart</em></dd></div>
      <div><dt>2013&ndash;2015</dt><dd>Researcher &mdash; <em>University of Stuttgart</em></dd></div>
      <div><dt>2009&ndash;2012</dt><dd>Researcher &mdash; <em>Friedrich Schiller University Jena</em></dd></div>
    </dl>

  </div>
</section>

<section id="publications">
  <div class="shell">
    <div class="sec-head">
      <h2>Publications</h2>
    </div>

    <div class="filter" data-filterset="pub-list">__PUB_FILTER__</div>
    <div class="rows" id="pub-list">__PUB_ROWS__</div>
  </div>
</section>

<section id="patents">
  <div class="shell">
    <div class="sec-head">
      <h2>Patents</h2>
    </div>

    <div class="filter" data-filterset="patent-list">__PATENT_FILTER__</div>
    <div class="rows" id="patent-list">__PATENT_ROWS__</div>
  </div>
</section>

</main>

<footer>
  <div class="shell foot-in">
    <p>&copy; __YEAR__ Lev Markhasin</p>
    <div class="foot-links">
      <a href="https://scholar.google.com/citations?user=_mWX1EAAAAAJ&amp;hl=en" target="_blank" rel="noopener">Scholar</a>
      <a href="https://patents.google.com/?inventor=lev+markhasin" target="_blank" rel="noopener">Patents</a>
    </div>
  </div>
</footer>
"""

body = (BODY
    .replace("__PATENT_FILTER__", "".join(patent_filter))
    .replace("__PATENT_ROWS__",   "".join(patent_row(p) for p in D.PATENTS))
    .replace("__PUB_FILTER__",    "".join(pub_filter))
    .replace("__PUB_ROWS__",      "".join(pub_row(p) for p in D.PUBS))
    .replace("__YEAR__", "2026"))

TITLE = "Lev Markhasin"
DESC  = ("Lev Markhasin \u2014 formerly AI team leader at Sony Semiconductor Solutions, "
         "now building a new company. Patents, publications and a short introduction.")

# ------------------------------------------------------------ standalone site
full = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title>
<meta name="description" content="%s">
<meta name="author" content="Lev Markhasin">
<meta property="og:type" content="profile">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:image" content="lev-markhasin.jpg">
<meta name="twitter:card" content="summary_large_image">
%s
<link rel="stylesheet" href="styles.css">
</head>
<body>
%s%s</body>
</html>
""" % (TITLE, DESC, TITLE, DESC, HEAD_LINKS, body, SCRIPT)

open(os.path.join(OUT, "index.html"), "w").write(full)
open(os.path.join(OUT, "styles.css"), "w").write(CSS.lstrip())

# ------------------------------------------------------------------ artifact
art = "<title>%s</title>\n%s\n<link rel=\"stylesheet\" href=\"styles.css\">\n%s%s" % (
    TITLE, HEAD_LINKS, body, SCRIPT)
if ART:
    open(os.path.join(ART, "index.html"), "w").write(art)
    open(os.path.join(ART, "styles.css"), "w").write(CSS.lstrip())

print("site/index.html  %6d bytes" % len(full))
print("site/styles.css  %6d bytes" % len(CSS))
if ART: print("artifact page    %6d bytes" % len(art))
