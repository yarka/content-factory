---
description: LinkedIn visual workflow - builds a reference board, visual DNA, and one rendered editorial card
globs:
  - "**/*.md"
  - "**/*.yaml"
  - "**/*.html"
---

# LinkedIn Visual Workflow

Use this after an approved LinkedIn post artifact exists.

## Inputs

Always read first:
1. approved post artifact from `content/accounts/<account-slug>/posts/YYYY-MM-DD-slug.md`
2. optional strategy image brief from `strategy/accounts/<account-slug>/content-plan.yaml`
3. `content/accounts/<account-slug>/visual-reference-board.md`
4. `content/accounts/<account-slug>/visual-dna.md`
5. `content/templates/linkedin-visual-card.html`

## Rules

- Start from a manual reference pack, not vibes.
- Do not lock a color/style direction before references exist.
- If no manual reference pack exists yet, ask the user for 3-10 references and stop after saving `visual-reference-board.md`.
- The first V1 output is one single-image editorial card for LinkedIn.
- No carousel generation in this workflow.
- No AI image model in this workflow.

## Workflow

### Phase 1: Reference Intake

Ask the user for a manual reference pack:
- 3-10 visual references
- what feels right
- what feels cringe
- any existing brand or banner cues worth preserving

Save a structured summary to:
`content/accounts/<account-slug>/visual-reference-board.md`

### Phase 2: Visual DNA

Once references exist, synthesize:
- palette direction
- typography direction
- composition rules
- texture/background rules
- text overlay rules
- what to never do

Save it to:
`content/accounts/<account-slug>/visual-dna.md`

### Phase 3: Render Card

Render one LinkedIn visual card from:
- the approved post artifact
- the optional image brief
- the approved visual DNA

Save the PNG to:
`content/accounts/<account-slug>/visuals/linkedin/YYYY-MM-DD-slug.png`

Use the HTML/CSS editorial card template as the base renderer.

## Output

Return:
- whether references were missing or approved
- where `visual-reference-board.md` was saved
- where `visual-dna.md` was saved
- where the rendered PNG was saved
- whether the next best step is review-with-visual or publish
