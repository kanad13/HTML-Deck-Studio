# Slide System Guide

This file is the main instruction set for building slides from `300-templates`.

## What the system is

The system separates four things:

- **tokens** - colours, spacing, radius, shadow, typography variables
- **layouts** - structural arrangements of content regions
- **deck workflows** - how decks are created, updated, and documented across sessions
- **slides** - real standalone HTML files with actual content

## What this system is for

This is a personal HTML slide system for AI-assisted deck creation and maintenance.

It is not a corporate multi-user design system.

The normal workflow is:

1. give an AI coding agent the repo and source material
2. ask it to create or update a deck
3. generate standalone slide files in `500-output/`
4. keep a `deck-context.md` file beside the slides so future sessions retain context

## Rules that matter

- Keep each slide as a standalone HTML file.
- Use the token names from [`110-systems/010-token-reference.md`](110-systems/010-token-reference.md).
- Choose layout structure based on content and communication need first.
- Adjust token values to express theme and visual tone once the content structure is right.
- Reuse a small number of layouts within one deck.
- Update deck context when a deck is created or materially changed.

## Normal workflow

1. Determine audience, purpose, and available input.
2. Choose a deck arc from [`130-workflows/030-deck-arcs.md`](130-workflows/030-deck-arcs.md).
3. Use [`100-basic.html`](100-basic.html) as the default scaffold.
4. Select fitting structures from [`120-layouts/010-layout-catalog.md`](120-layouts/010-layout-catalog.md).
5. Copy needed token values from the light or dark default system.
6. Build the slides as full HTML documents.
7. Output them following [`130-workflows/020-output-contract.md`](130-workflows/020-output-contract.md).
8. Write or update `deck-context.md` using [`130-workflows/040-maintenance-context.md`](130-workflows/040-maintenance-context.md).

## Required token contract

### Minimum tokens for most slides

- `--surface-0`
- `--surface-1`
- `--surface-2`
- `--text-primary`
- `--text-secondary`
- `--border`
- `--brand-primary`
- `--space-1` to `--space-8`
- `--radius-sm` to `--radius-xl`
- `--shadow-soft`

### Extended tokens for richer slides

#### Additional brand

- `--brand-secondary`
- `--brand-tertiary`
- `--brand-quaternary`

#### Semantic

- `--success`
- `--warning`
- `--danger`
- `--info`

#### Chart

- `--chart-1`
- `--chart-2`
- `--chart-3`
- `--chart-4`
- `--chart-5`
- `--chart-6`

## Slide file expectations

A real slide file should usually include:

- `<!DOCTYPE html>`
- `lang`
- charset and viewport metadata
- inline token definitions
- `<style>` that consumes those tokens
- `<slide markup>`
- optional `<aside class="notes">`

## Deck-level expectations

A real deck should usually have:

- a coherent arc
- a limited set of repeated layout patterns
- an opener and a close or clear final implication
- titles that make slide purpose obvious
- `deck-context.md` documenting why the deck was built

## Simple quality check

Before considering a slide or deck done:

- the deck arc fits the audience and task
- each slide has one clear communication job
- tokens are used consistently
- layout choice follows content need rather than decoration
- the deck does not rely on random hardcoded colours across components
- hierarchy is obvious
- slides are readable without zooming in
- output files follow the output contract
