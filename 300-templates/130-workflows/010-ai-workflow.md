# AI Slide Workflow

This folder defines how an AI coding agent should create, update, and maintain slide decks in this repo.

## Scope

Use this workflow for personal HTML slide generation in this repo.

This is not a corporate multi-user design system. It is a lightweight, local-first slide workflow for a single user who may return across multiple sessions.

## Workflow set

- [`010-ai-workflow.md`](010-ai-workflow.md) — end-to-end creation and maintenance workflow
- [`020-output-contract.md`](020-output-contract.md) — required output files and naming rules
- [`030-deck-arcs.md`](030-deck-arcs.md) — reusable deck arc patterns based on communication best practices
- [`040-maintenance-context.md`](040-maintenance-context.md) — deck context sidecar file for future updates

## Creation workflow

### 1. Understand the task

Before creating slides, determine:

- who the audience is
- what outcome the deck should achieve
- what source material is available
- whether the deck is informative, persuasive, analytical, explanatory, or mixed
- what constraints exist for length, tone, and theme

If important information is missing, state assumptions clearly in `deck-context.md`.

### 2. Shape the deck before writing slides

Before writing any HTML:

- choose a deck arc from [`030-deck-arcs.md`](030-deck-arcs.md)
- define the section flow
- decide roughly how many slides are needed
- assign one communication job to each slide

Do not start from decorative layout choices.

Start from message, audience, and arc.

### 3. Choose system ingredients

- use [`../100-basic.html`](../100-basic.html) as the default scaffold
- choose a theme direction from [`110-systems/`]
- choose a small number of layouts from [`120-layouts/`]
- prefer reuse over novelty

### 4. Generate output

- write the deck into `500-output/` following [`020-output-contract.md`](020-output-contract.md)
- create standalone HTML slides
- create `deck-context.md`
- keep slides scannable and locally editable

## Maintenance workflow

When updating an existing deck:

### 1. Read before editing

Review:

- existing slide files
- `deck-context.md`
- the user's requested changes

### 2. Preserve intent where possible

Try to preserve:

- the existing arc unless the user wants a reframing
- the current numbering unless renumbering is truly needed
- the visual system unless the user wants a redesign

### 3. Record change context

Update `deck-context.md` with:

- what changed
- why it changed
- what assumptions were introduced
- any unresolved follow-up items

## Authoring priorities

When trade-offs appear, prefer this order:

1. message clarity
2. audience fit
3. coherent arc
4. slide readability
5. deck consistency
6. visual refinement

## Anti-patterns

Avoid these failure modes:

- choosing layouts before understanding the content
- using a different visual style on every slide
- overfilling slides with report text
- inventing unsupported facts to complete a narrative
- updating slides without updating context
- treating layouts as rigid templates instead of communication tools
