# HTML Slide Template Library

This folder is the slide-authoring and slide-generation reference for this repo.

It exists so an AI coding agent or a human can quickly build, update, and maintain standalone HTML slide decks.

## Start here

- Read [`020-system-guide.md`](020-system-guide.md) for the system rules and authoring priorities.
- Use [`100-basic.html`](100-basic.html) as the default standalone slide scaffold.
- Browse [`120-layouts/010-layout-catalog.md`](120-layouts/010-layout-catalog.md) for structural options.
- Use [`130-workflows/010-ai-workflow.md`](130-workflows/010-ai-workflow.md) for slide creation and maintenance workflow.
- Reuse token values from [`110-systems/100-light-default.html`](110-systems/100-light-default.html) or [`110-systems/110-dark-default.html`](110-systems/110-dark-default.html).

## Folder map

```
300-templates/
├── 010-overview.md
├── 020-system-guide.md
├── 100-basic.html
├── 110-systems/
│   ├── 010-token-reference.md
│   ├── 100-light-default.html
│   └── 110-dark-default.html
├── 120-layouts/
│   └── 010-layout-catalog.md
└── 130-workflows/
    ├── 010-ai-workflow.md
    ├── 020-output-contract.md
    ├── 030-deck-arcs.md
    └── 040-maintenance-context.md
```

## Default workflow

1. Clarify the audience, goal, and raw input.
2. Choose a deck arc from `130-workflows/030-deck-arcs.md`.
3. Pick light or dark tokens.
4. Pick a small set of layout shapes from the catalog.
5. Build the actual slides as standalone HTML files.
6. Output the deck in `500-output/` together with `deck-context.md`.
7. On later revisions, update both the slides and the context sidecar.
