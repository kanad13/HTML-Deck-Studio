# Output Contract

This file defines the required output contract for generated decks.

## Output location

Generated slide decks belong in `500-output/`.

Use one subfolder per deck.

Example:

```
500-output/
└─ project-update-q3/
   ├─ slide01.html
   ├─ slide02.html
   ├─ slide03.html
   └─ deck-context.md
```

Do not place long-lived generated decks directly at the root of `500-output/` unless the user explicitly asks for a flat output.

## Required deck files

Every generated deck should usually include:

- `slide01.html`, `slide02.html`, `slide03.html`, ...
- `deck-context.md`

Optional:

- supporting local assets stored in a deck-local subfolder such as `assets/`

## Slide naming

- Use zero padded numbering: `slide01.html`, `slide02.html`, `slide03.html`
- keep numbering contiguous
- Prefer stable names so future edits do not reorder the entire deck unnecessarily

## Slide contract

Each slide must be a standalone HTML document.

Each slide should include:

- `<!DOCTYPE html>`
- `<html lang="...">`
- charset and viewport metadata
- a meaningful `<title>`
- inline CSS
- slide markup
- optional `<aside class="notes">`

## Deck consistency rules

Within one deck:

- keep one primary theme direction unless the user asks otherwise
- reuse a small set of layouts rather than changing layout on every slide
- keep typography, spacing, and card treatments consistent
- prefer content clarity over decorative density

## Default generation assumptions

Unless the user says otherwise:

- create a deck subfolder inside `500-output/`
- use standalone HTML slides
- use `300-templates/100-basic.html` as the base scaffold
- choose layouts from `300-templates/120-layouts/010-layout-catalog.md`
- write a `deck-context.md` file alongside the slides

## Update behavior

When updating an existing deck:

- preserve existing numbering when practical
- edit in place when only small changes are needed
- add new slides by extending the sequence
- update `deck-context.md` to record why changes were made
