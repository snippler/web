CSS = r"""
/* ============================================================
   Lev Markhasin — personal site
   Palette : paper / graphite ink / prussian accent
   Type    : Newsreader (display) · IBM Plex Sans (text) · IBM Plex Mono (data)
   ============================================================ */

:root {
  color-scheme: light;

  --ground:      #fcfcfd;
  --surface:     #ffffff;
  --surface-2:   #f4f5f7;
  --ink:         #13171c;
  --ink-soft:    #3b434c;
  --muted:       #626b76;
  --line:        #e1e5ea;
  --line-strong: #c9d0d8;
  --accent:      #1c4e6b;
  --accent-hi:   #17627f;
  --accent-soft: #e9f1f6;

  --f-display: "Newsreader", "Iowan Old Style", Georgia, "Times New Roman", serif;
  --f-text:    "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --f-mono:    "IBM Plex Mono", ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;

  --shell: 61rem;
  --r: 4px;
}

@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    color-scheme: dark;
    --ground:      #0e1114;
    --surface:     #151a20;
    --surface-2:   #1b2128;
    --ink:         #e9edf1;
    --ink-soft:    #c3cbd4;
    --muted:       #96a1ac;
    --line:        #232a32;
    --line-strong: #39434e;
    --accent:      #8cc0de;
    --accent-hi:   #a9d4ec;
    --accent-soft: #15242f;
  }
}

:root[data-theme="dark"] {
  color-scheme: dark;
  --ground:      #0e1114;
  --surface:     #151a20;
  --surface-2:   #1b2128;
  --ink:         #e9edf1;
  --ink-soft:    #c3cbd4;
  --muted:       #96a1ac;
  --line:        #232a32;
  --line-strong: #39434e;
  --accent:      #8cc0de;
  --accent-hi:   #a9d4ec;
  --accent-soft: #15242f;
}

*, *::before, *::after { box-sizing: border-box; }

figure, blockquote { margin: 0; }
h1, h2, h3, p, dl, dd { margin: 0; }

html { -webkit-text-size-adjust: 100%; }

body {
  margin: 0;
  background: var(--ground);
  color: var(--ink);
  font-family: var(--f-text);
  font-size: 1rem;
  line-height: 1.65;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

img { max-width: 100%; display: block; }

a { color: var(--accent); text-decoration-color: color-mix(in srgb, var(--accent) 35%, transparent); text-underline-offset: 2px; }
a:hover { color: var(--accent-hi); text-decoration-color: currentColor; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 2px; }

/* ----------------------------------------------------------------- shell */
.shell {
  width: 100%;
  max-width: var(--shell);
  margin-inline: auto;
  padding-inline: 20px;
}

section { padding-block: 4.5rem; }
section + section { border-top: 1px solid var(--line); }

/* ------------------------------------------------------------------- nav */
.nav {
  position: sticky;
  top: env(safe-area-inset-top, 0px);
  z-index: 20;
  background: color-mix(in srgb, var(--ground) 88%, transparent);
  backdrop-filter: saturate(140%) blur(10px);
  border-bottom: 1px solid var(--line);
}
.nav-in {
  display: flex;
  align-items: center;
  gap: 1.1rem;
  min-height: 52px;
}
.nav-name {
  font-family: var(--f-display);
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: 0.01em;
  margin-right: auto;
  color: var(--ink);
  text-decoration: none;
}
.nav a.nav-link {
  font-family: var(--f-mono);
  font-size: 0.75rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--muted);
  text-decoration: none;
}
.nav a.nav-link:hover { color: var(--ink); }

@media (max-width: 640px) {
  .nav-name { display: none; }
  .nav-in { gap: 0.9rem; justify-content: flex-start; }
  .nav-in .theme-btn { margin-left: auto; }
}

.theme-btn {
  font: inherit;
  font-family: var(--f-mono);
  font-size: 0.7rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
  background: transparent;
  border: 1px solid var(--line-strong);
  border-radius: 999px;
  padding: 3px 10px;
  cursor: pointer;
}
.theme-btn:hover { color: var(--ink); border-color: var(--ink); }

/* ------------------------------------------------------------------ hero */
.hero { padding-block: 4rem 3.5rem; }
.hero-grid {
  display: grid;
  gap: 2.5rem;
  grid-template-columns: 1fr;
  align-items: start;
}
@media (min-width: 820px) {
  .hero-grid { grid-template-columns: minmax(0, 1fr) 15.5rem; gap: 3.5rem; }
}

.eyebrow {
  font-family: var(--f-mono);
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  margin: 0 0 1rem;
}

h1 {
  font-family: var(--f-display);
  font-weight: 500;
  font-size: clamp(2.5rem, 7vw, 3.9rem);
  line-height: 1.02;
  letter-spacing: -0.015em;
  margin: 0 0 0.6rem;
  text-wrap: balance;
}
.role {
  font-family: var(--f-display);
  font-style: italic;
  font-size: clamp(1.1rem, 2.6vw, 1.35rem);
  line-height: 1.35;
  color: var(--ink-soft);
  margin: 0 0 1.75rem;
  max-width: 46ch;
  text-wrap: balance;
}

.lede { max-width: 62ch; }
.lede p { margin: 0 0 1.1rem; color: var(--ink-soft); }
.lede p:last-child { margin-bottom: 0; }
.lede strong { color: var(--ink); font-weight: 600; }

.portrait {
  border: 1px solid var(--line);
  border-radius: var(--r);
  overflow: hidden;
  background: var(--surface-2);
  max-width: 15.5rem;
}
.portrait img { width: 100%; height: auto; }

/* ----------------------------------------------------------------- links */
.linkrow {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 2rem;
}
.linkrow a {
  font-family: var(--f-mono);
  font-size: 0.78rem;
  text-decoration: none;
  color: var(--ink-soft);
  border: 1px solid var(--line-strong);
  border-radius: 999px;
  padding: 5px 13px;
}
.linkrow a:hover { color: var(--accent); border-color: var(--accent); }

/* -------------------------------------------------------------- headings */
.sec-head { margin-bottom: 2.25rem; }
.sec-num {
  font-family: var(--f-mono);
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
  display: block;
  margin-bottom: 0.6rem;
}
h2 {
  font-family: var(--f-display);
  font-weight: 500;
  font-size: clamp(1.8rem, 4.4vw, 2.4rem);
  line-height: 1.1;
  letter-spacing: -0.012em;
  margin: 0 0 0.9rem;
  text-wrap: balance;
}
.sec-head p { margin: 0; max-width: 60ch; color: var(--ink-soft); }
.sec-head h2:last-child { margin-bottom: 0; }

/* ------------------------------------------------------------ trajectory */
.track { margin: 2.75rem 0 0; }
.track div {
  display: grid;
  grid-template-columns: 8.5rem minmax(0, 1fr);
  gap: 0 1.5rem;
  padding: 0.7rem 0;
  border-top: 1px solid var(--line);
  align-items: baseline;
}
.track div:last-child { border-bottom: 1px solid var(--line); }
.track dt {
  font-family: var(--f-mono);
  font-size: 0.78rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}
.track dd { margin: 0; }
.track dd em { font-style: normal; color: var(--muted); }
@media (max-width: 560px) {
  .track div { grid-template-columns: 1fr; gap: 0.1rem; }
}

/* ---------------------------------------------------------------- filter */
.filter {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 1.75rem;
}
.filter button {
  font-family: var(--f-mono);
  font-size: 0.72rem;
  letter-spacing: 0.02em;
  color: var(--muted);
  background: transparent;
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 4px 12px;
  cursor: pointer;
}
.filter button:hover { color: var(--ink); border-color: var(--line-strong); }
.filter button[aria-pressed="true"] {
  color: var(--accent);
  border-color: var(--accent);
  background: var(--accent-soft);
}
.filter .count { opacity: 0.6; margin-left: 0.4em; font-variant-numeric: tabular-nums; }

/* ----------------------------------------------------------------- lists */
.rows { border-top: 1px solid var(--line); }

.row {
  display: grid;
  grid-template-columns: 9.5rem minmax(0, 1fr);
  gap: 0 1.5rem;
  padding: 1.1rem 0;
  border-bottom: 1px solid var(--line);
}
@media (max-width: 680px) {
  .row { grid-template-columns: 1fr; gap: 0.35rem; }
}

.row-meta {
  font-family: var(--f-mono);
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}
.row-meta a { color: var(--muted); text-decoration: none; border-bottom: 1px solid var(--line-strong); }
.row-meta a:hover { color: var(--accent); border-color: var(--accent); }
.row-meta .yr { display: block; color: var(--ink-soft); }
.row-meta .tag { display: block; margin-top: 0.15rem; font-size: 0.68rem; letter-spacing: 0.06em; text-transform: uppercase; }

.row-title {
  font-family: var(--f-display);
  font-size: 1.12rem;
  font-weight: 500;
  line-height: 1.3;
  margin: 0 0 0.25rem;
  color: var(--ink);
  text-wrap: pretty;
}
.row-title a { color: inherit; text-decoration: none; background-image: linear-gradient(currentColor, currentColor); background-size: 0% 1px; background-repeat: no-repeat; background-position: 0 92%; transition: background-size 0.22s ease; }
.row-title a:hover { background-size: 100% 1px; color: var(--accent); }

.row-sub { margin: 0; font-size: 0.9rem; color: var(--muted); line-height: 1.55; }
.row-sub .me { color: var(--ink); font-weight: 600; }
.row-venue { font-style: italic; }

.chips { display: flex; flex-wrap: wrap; gap: 0.35rem; margin-top: 0.5rem; }
.chips a {
  font-family: var(--f-mono);
  font-size: 0.68rem;
  letter-spacing: 0.03em;
  text-decoration: none;
  color: var(--muted);
  border: 1px solid var(--line);
  border-radius: 3px;
  padding: 1px 7px;
}
.chips a:hover { color: var(--accent); border-color: var(--accent); }

.hidden-row { display: none; }

/* ---------------------------------------------------------------- footer */
footer {
  border-top: 1px solid var(--line);
  padding-block: 2.5rem 3.5rem;
  font-size: 0.85rem;
  color: var(--muted);
}
footer .foot-in { display: flex; flex-wrap: wrap; gap: 1rem 2rem; justify-content: space-between; }
footer p { margin: 0; }
footer .foot-links { display: flex; flex-wrap: wrap; gap: 1.1rem; }
footer a { font-family: var(--f-mono); font-size: 0.78rem; text-decoration: none; }
footer a:hover { text-decoration: underline; }

@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
"""
