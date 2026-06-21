# HTML Deck Studio

**Portable presentations. No accounts. No servers. Files stay local.**

## The Problem

Presentation tools are built backward. The tool is the center. Your slides live inside it. You're stuck with what it can do, how it renders, and what happens when it changes.

You want to:

- Embed a custom visualization? The tool doesn't support it.
- Version your slides in Git? Export, upload, hope the format stays compatible.
- Use an AI agent to generate slides? You get proprietary markup that needs manual fixing.
- Export to PDF? It doesn't match what you saw on screen.
- Reuse slide components across multiple decks? Copy-paste and maintain separately.

Five years later, the tool might be gone or behind a paywall, and your files are trapped.

## The Solution

HTML Deck Studio inverts that. Your slides are HTML files. The files are the center. The tools are interchangeable.

- **Present** using a lightweight browser-based viewer
- **Generate** decks with AI using a stable template system
- **Export** to PDF using a simple Python script
- **Version** everything in Git like code
- **Embed** anything that renders in a browser—D3, Mermaid, React, live data

![](./400-assets/100.png)

In this repository, you'll find:

- A presentation viewer that provides navigation, notes, overview, and fullscreen
- An AI-assisted workflow for generating and updating HTML slide decks with stable templates and token-based theming
- A PDF export tool that converts your HTML slides to full-bleed 16:9 PDFs for sharing or printing

The viewer is a single HTML file. No installation. No build step. No lock-in.

## Three Ways to Use It

### 1. Just Present a Deck

Open [HTML Slides Viewer](./100-viewer.html) in a browser, select a folder of `.html` slides, and present. Arrow keys navigate. Press `O` for overview, `N` for notes, `Z` for fullscreen. Works offline, any machine.

### 2. Generate Decks with AI

Give a coding agent the [Templates Folder](./300-templates/) folder as context. It creates clean HTML slides following stable conventions. Regenerate whenever content changes. Token-based theming keeps your branding intact.

### 3. Export to PDF

Convert a slide folder to PDF for sharing or printing:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 600-tools/requirements/pdf.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python 600-tools/export_pdf.py my-deck --out my-deck.pdf
```

## Who This Is For

**Developers who want to version-control presentations**

Your slides are source files. Commit them. Diff them. Merge them. Use branches for major revisions.

**People working with AI agents**

Agents understand code and conventions. Give them the template system, ask them to generate slides, and get clean, regenerable HTML without proprietary format friction.

**Presenters with custom content needs**

Embed D3 visualizations, Mermaid charts, live data feeds, or interactive components. The full power of HTML, CSS, and JavaScript.

**Anyone who wants to own their files**

HTML files work in any browser. PDFs work everywhere. No vendor lock-in. No proprietary format rot.

## Key Features

- **No installation required** for normal use. The viewer is a single HTML file.
- **Works offline.** Present anywhere without internet or server dependencies.
- **Portable files.** HTML slides, CSS styling, and assets in a simple folder structure.
- **Version control friendly.** Plain text HTML diffs, branches, merges, and history.
- **Sandboxed presentation.** Slides render in iframes separate from the viewer.
- **Speaker notes built in.** Extract and display without executing slide code.
- **Presenter window support.** Press `P` to open notes on one monitor, slides on another.
- **AI-friendly templating.** Stable structure for agents to generate and regenerate decks.
- **Token-based theming.** Regenerate slide content without losing customization.
- **Optional PDF export.** Renders in Chromium for pixel-perfect full-bleed output.

## Repository Map

Core folders:

- [`100-viewer.html`](./100-viewer.html) - the presentation viewer (single file, no dependencies).
- [`150-docs/`](./150-docs/) - documentation, guides, and reference material.
- [`200-demos/`](./200-demos/) - a reference demo deck built to the current slide contract.
- [`300-templates/`](./300-templates/) - AI authoring system, token references, layout catalog, and output contracts.
- [`500-output/`](./500-output/) - recommended location for generated decks.
- [`600-tools/`](./600-tools/) - validation, smoke tests, CI helpers, and optional PDF export tooling.

## Documentation

Start here:

- [`150-docs/100-user-guide.md`](./150-docs/100-user-guide.md) - how to open, present, and navigate decks.
- [`150-docs/110-pdf-export.md`](./150-docs/110-pdf-export.md) - setup and export commands.
- [`150-docs/120-security-model.md`](./150-docs/120-security-model.md) - privacy boundaries and file handling.
- [`150-docs/130-development-and-tests.md`](./150-docs/130-development-and-tests.md) - maintenance, checks, and CI.

For AI-assisted deck creation, see [`300-templates`](./300-templates/010-overview.md) and the guides within.

## Quick Start

### Present a Deck

1. Open [`100-viewer.html`](./100-viewer.html) in a modern browser.
2. Click **Choose Folder**.
3. Select a folder containing slide files (`slide0100.html`, `slide0200.html`, etc.).
4. Navigate with arrow keys, `O` for overview, `N` for notes, `Z` for fullscreen.

### Generate a Deck With AI

1. Review [`300-templates/010-overview.md`](./300-templates/010-overview.md) and [`300-templates/020-system-guide.md`](./300-templates/020-system-guide.md).
2. Give those to a coding agent as context.
3. Ask the agent to generate a deck in [`500-output/<deck-name>/`](./500-output/).
4. Open the generated `slide0100.html` onwards in the viewer.

### Export to PDF

```bash
.venv/bin/python 600-tools/export_pdf.py 500-output/my-deck --out my-deck.pdf
```

See [`150-docs/110-pdf-export.md`](./150-docs/110-pdf-export.md) for full setup and options.

## Security and Privacy

The viewer is designed for local-first use.

- Selected files are read by the browser only after you choose them.
- Files are represented with temporary object URLs; old ones are revoked when you load a new deck.
- Slides render in sandboxed iframes separate from the viewer.
- The viewer does not upload your files.

For details, see [`150-docs/120-security-model.md`](./150-docs/120-security-model.md).

## Development

Run standard checks before committing:

```bash
python3 600-tools/run_checks.py
```

Run the full browser suite when development dependencies are installed:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r 600-tools/requirements/dev.txt
.venv/bin/python -m playwright install chromium
python3 600-tools/run_checks.py --browser
```

See [`150-docs/130-development-and-tests.md`](./150-docs/130-development-and-tests.md) for more.

## Why This Exists

Most presentation tools lock you into a single system. HTML Deck Studio optimizes for your files instead.

Files that are:

- **Portable.** They work in any browser, forever.
- **Versionable.** Diffs, branches, and history like code.
- **Generatable.** AI agents understand the structure.
- **Extensible.** Full power of HTML, CSS, and JavaScript.
- **Yours.** No vendor, no lock-in, no proprietary format.

This matters because presentations accumulate. Every deck is an asset. Those assets should belong completely to you.
