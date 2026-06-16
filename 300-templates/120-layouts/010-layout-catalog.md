# Layout Catalog

This file shows the main layout shapes available to build real standalone slides.

Use these as structural patterns, not as complete files.

Do not copy a snippet directly into output and call it done. A generated slide must still be a complete standalone HTML
document with inline token definitions, inline CSS that consumes those tokens, slide markup, and optional speaker notes.

## Shared notes

- Build the final result as a full standalone HTML slide.
- Use tokens from the system files.
- Add `aside.notes` only when useful.
- Keep only the structure that helps the slide communicate clearly.
- Add the CSS required to make the selected layout render correctly at 16:9 desktop presentation size and narrow mobile
  widths.
- Keep hardcoded colour values in the token definition section. Layout CSS should consume token names.
- Check text fit, contrast, and hierarchy after content is inserted. The snippets below are not text-fit guarantees.

## 010 classic-title

Regions: eyebrow, title, subtitle, meta, notes

```html
<main class="slide layout-classic-title">
  <section class="content stack-center">
    <p class="eyebrow">Section label</p>
    <h1>Primary slide message</h1>
    <div class="accent-line"></div>
    <p class="subtitle">Optional subtitle or framing statement.</p>
    <p class="meta">Presenter - Organization - Date</p>
    <aside class="notes">Presenter notes.</aside>
  </section>
</main>
```

## 020 title-body

Regions: tag, title, divider, body, list, notes

```html
<main class="slide layout-title-body">
  <section class="content prose block">
    <p class="tag">Context</p>
    <h1>Slide title</h1>
    <hr class="divider" />
    <p class="body">A short framing paragraph.</p>
    <ul class="body-list">
      <li>Key point one</li>
      <li>Key point two</li>
      <li>Key point three</li>
    </ul>
    <aside class="notes">Presenter notes.</aside>
  </section>
</main>
```

## 030 split-diagram-text

Regions: diagram-panel, text-panel, eyebrow, title, subtitle

```html
<main class="slide layout-split-diagram">
  <section class="split two-column">
    <div class="diagram-panel">Diagram or visual block.</div>
    <div class="text-panel">
      <p class="eyebrow">Framework</p>
      <h1>Explain the visual.</h1>
      <p class="subtitle">Supporting narrative.</p>
    </div>
  </section>
</main>
```

## 040 image-focus

Regions: image-frame, caption-panel, title, body

```html
<main class="slide layout-image-focus">
  <figure class="image-stage">
    <div class="image-frame">Image area.</div>
    <figcaption class="caption-panel">
      <h1>Caption title</h1>
      <p>Short supporting explanation.</p>
    </figcaption>
  </figure>
</main>
```

## 050 three-column

Regions: eyebrow, title, cards[3]

```html
<main class="slide layout-three-column">
  <header>
    <p class="eyebrow">Overview</p>
    <h1>Three supporting pillars</h1>
  </header>
  <section class="grid three-up">
    <article class="card">
      <h2>One</h2>
      <p>Detail.</p>
    </article>
    <article class="card">
      <h2>Two</h2>
      <p>Detail.</p>
    </article>
    <article class="card">
      <h2>Three</h2>
      <p>Detail.</p>
    </article>
  </section>
</main>
```

## 060 big-quote

Regions: quote-mark, quote-text, quote-meta

```html
<main class="slide layout-big-quote">
  <blockquote class="quote-block">
    <p class="quote-mark">"</p>
    <p class="quote-text">A memorable statement.</p>
    <footer class="quote-meta">Name - Role</footer>
  </blockquote>
</main>
```

## 070 stats-grid

Regions: title, metric-cards

```html
<main class="slide layout-stats-grid">
  <header>
    <h1>The numbers tell the story</h1>
  </header>
  <section class="grid three-up">
    <article class="metric-card">
      <div class="metric-value">4.2x</div>
      <div class="metric-label">Faster delivery</div>
    </article>
    <article class="metric-card">
      <div class="metric-value">83%</div>
      <div class="metric-label">Cost reduction</div>
    </article>
    <article class="metric-card">
      <div class="metric-value">99.9%</div>
      <div class="metric-label">Uptime</div>
    </article>
  </section>
</main>
```

## 080 section-header

Regions: accent-bar, eyebrow, title, subtitle

```html
<main class="slide layout-section-header">
  <section class="section-banner">
    <div class="accent-bar"></div>
    <div>
      <p class="eyebrow">Section</p>
      <h1>Section title</h1>
      <p class="subtitle">Optional transition statement.</p>
    </div>
  </section>
</main>
```

## 090 agenda

Regions: title, agenda-list, index, label

```html
<main class="slide layout-agenda">
  <header><h1>Agenda</h1></header>
  <ol class="agenda-list">
    <li>
      <span class="index">01</span><span class="label">Introduction</span>
    </li>
    <li><span class="index">02</span><span class="label">Findings</span></li>
    <li><span class="index">03</span><span class="label">Decision</span></li>
  </ol>
</main>
```

## 100 comparison

Regions: title, option-a, option-b

```html
<main class="slide layout-comparison">
  <header><h1>Compare two options</h1></header>
  <section class="grid two-up comparison-columns">
    <article class="card option-a">
      <h2>Option A</h2>
      <p>Characteristics.</p>
    </article>
    <article class="card option-b">
      <h2>Option B</h2>
      <p>Characteristics.</p>
    </article>
  </section>
</main>
```

## 110 timeline

Regions: title, milestone-list, milestone

```html
<main class="slide layout-timeline">
  <header><h1>Timeline</h1></header>
  <section class="timeline">
    <article class="milestone">
      <h2>Q1</h2>
      <p>Milestone detail.</p>
    </article>
    <article class="milestone">
      <h2>Q2</h2>
      <p>Milestone detail.</p>
    </article>
    <article class="milestone">
      <h2>Q3</h2>
      <p>Milestone detail.</p>
    </article>
  </section>
</main>
```

## 120 code-snippet

Regions: title, subtitle, window-bar, code-block

```html
<main class="slide layout-code-snippet">
  <header>
    <h1>Code example</h1>
    <p class="subtitle">Optional explanation.</p>
  </header>
  <section class="code-window">
    <div class="window-bar">file.ts</div>
    <pre><code>// code block</code></pre>
  </section>
</main>
```

## 130 image-overlay

Regions: image-stage, overlay-card, eyebrow, title, subtitle

```html
<main class="slide layout-image-overlay">
  <section class="image-overlay-stage">
    <div class="image-stage">Image area.</div>
    <article class="overlay-card">
      <p class="eyebrow">Highlight</p>
      <h1>Overlay headline</h1>
      <p class="subtitle">Overlay summary.</p>
    </article>
  </section>
</main>
```

## 140 grid-cards

Regions: title, cards[4]

```html
<main class="slide layout-grid-cards">
  <header><h1>Capability grid</h1></header>
  <section class="grid four-up">
    <article class="card">A</article>
    <article class="card">B</article>
    <article class="card">C</article>
    <article class="card">D</article>
  </section>
</main>
```

## 150 consulting-split

Regions: left-rail, callout, right-panel, evidence-list

```html
<main class="slide layout-consulting-split">
  <section class="split consulting-layout">
    <aside class="left-rail">
      <p class="eyebrow">Finding 03</p>
      <h1>Key messages</h1>
      <div class="callout">Short so-what statement.</div>
    </aside>
    <section class="right-panel">
      <h2>Supporting evidence</h2>
      <ol class="evidence-list">
        <li>Evidence point</li>
        <li>Evidence point</li>
        <li>Evidence point</li>
      </ol>
    </section>
  </section>
</main>
```

## 160 bold-statement

Regions: statement-block, title, accent-underline

```html
<main class="slide layout-bold-statement">
  <section class="statement-block">
    <h1>One sharp statement.</h1>
    <div class="accent-underline"></div>
  </section>
</main>
```

## 170 data-table

Regions: title, subtitle, table-wrap, table

```html
<main class="slide layout-data-table">
  <header>
    <h1>Scorecard</h1>
    <p class="subtitle">Updated weekly.</p>
  </header>
  <section class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Initiative</th>
          <th>Owner</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Example</td>
          <td>Name</td>
          <td>On track</td>
        </tr>
      </tbody>
    </table>
  </section>
</main>
```

## 180 split-bands

Regions: band-top, band-bottom

```html
<main class="slide layout-split-bands">
  <section class="band-top"><h1>Top band headline</h1></section>
  <section class="band-bottom"><p>Supporting content.</p></section>
</main>
```

## 190 sidebar-accent

Regions: sidebar, content-panel, title, body

```html
<main class="slide layout-sidebar-accent">
  <section class="sidebar-layout">
    <aside class="sidebar">Sidebar label.</aside>
    <section class="content-panel">
      <h1>Main content</h1>
      <p>Supporting narrative.</p>
    </section>
  </section>
</main>
```

## 200 gradient-glass

Regions: gradient-stage, glass-card, title, body

```html
<main class="slide layout-gradient-glass">
  <section class="gradient-stage">
    <article class="glass-card">
      <h1>Premium visual treatment</h1>
      <p>Glassmorphism or layered card content.</p>
    </article>
  </section>
</main>
```

## 210 diagonal-split

Regions: diagonal-left, diagonal-right

```html
<main class="slide layout-diagonal-split">
  <section class="diagonal-shell">
    <div class="diagonal-left"><h1>Left concept</h1></div>
    <div class="diagonal-right"><p>Right concept.</p></div>
  </section>
</main>
```

## 220 top-accent-band

Regions: top-band, band-stripe, content-panel

```html
<main class="slide layout-top-accent-band">
  <header class="top-band">
    <div class="band-stripe"></div>
    <h1>Headline</h1>
  </header>
  <section class="content-panel">
    <p>Body content.</p>
  </section>
</main>
```

## 230 minimal-typography

Regions: minimal-shell, accent-dot, title, subtitle

```html
<main class="slide layout-minimal-typography">
  <section class="minimal-shell">
    <div class="accent-dot"></div>
    <h1>Minimal message</h1>
    <p class="subtitle">Very sparse supporting text.</p>
  </section>
</main>
```

## 240 pyramid

Regions: title, pyramid, tier-1, tier-2, tier-3

```html
<main class="slide layout-pyramid">
  <header><h1>Hierarchy</h1></header>
  <section class="pyramid">
    <div class="tier tier-1">Top</div>
    <div class="tier tier-2">Middle</div>
    <div class="tier tier-3">Base</div>
  </section>
</main>
```

## 250 full-bleed-solid

Regions: full-bleed-stage, title, subtitle

```html
<main class="slide layout-full-bleed-solid">
  <section class="full-bleed-stage">
    <h1>Large centered message</h1>
    <p class="subtitle">Optional support line.</p>
  </section>
</main>
```
