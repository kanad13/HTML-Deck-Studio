# Deck Context Sidecar

Each generated deck should include a `deck-context.md` file.

Its job is to preserve enough context so that a future AI agent or human can update the deck in a later session without rediscovering the original reasoning from scratch.

## Why this exists

Decks evolve across sessions.

The HTML slides alone often do not explain:

- why the deck was created
- what audience it targeted
- what arc was chosen
- which design choices were intentional
- what constraints shaped the deck

That context should be saved with the deck.

## Required sections

A `deck-context.md` file should usually include:

### 1. Deck summary

- deck name
- date created
- date last updated
- purpose of the deck
- intended audience

### 2. Input summary

- source materials used
- prompt or brief summary
- assumptions made because information was missing

### 3. Narrative choices

- selected deck arc
- why that arc was chosen
- section structure used
- what was intentionally excluded

### 4. Design choices

- theme direction used
- layouts used and why
- notable visual constraints
- token or styling choices if relevant

### 5. Slide map

A short list of slide numbers with their role.

Example:

```
- slide01.html — opener
- slide02.html — agenda
- slide03.html — current state
- slide04.html — recommendation
```

### 6. Update notes

- what changed in each later revision
- why it changed
- unresolved questions or follow-ups

## Maintenance rule

When an agent updates a deck, it should update `deck-context.md` as part of the same change unless the user explicitly says not to.
