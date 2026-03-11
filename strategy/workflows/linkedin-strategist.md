---
description: LinkedIn Strategist - consumes an approved intelligence snapshot and turns it into strategy pack, content plan, and image briefs
globs:
  - "**/*.md"
  - "**/*.yaml"
---

# LinkedIn Strategist

Language rule: detect the language the user writes in and respond in that language throughout the workflow.

This workflow creates strategy outputs from an approved upstream intelligence snapshot before the content pipeline starts writing posts.

## Inputs

Always read first:
1. `strategy/accounts/<account-slug>/account-profile.yaml` - the business brief
2. `intelligence/accounts/<account-slug>/intelligence-snapshot.yaml` - the approved intelligence snapshot
3. `content/channel-dna-linkedin.md` - voice and platform contract
4. `content/writing-guide.md` - author voice if available
5. `strategy/README.md` - workspace rules

If the account workspace does not exist, create it from `strategy/templates/`.

## Workflow

### Phase 1: Read the business brief

- Read the business brief and extract the offer, audience, proof assets, goal type, and CTA constraints.
- Read the approved intelligence snapshot and treat it as the only discovery input.
- Confirm the primary platform is LinkedIn.
- Keep `content/channel-dna-linkedin.md` as the voice contract, not the strategy database.

### Phase 2: Read Pattern Library and competitor universe

Read the approved Pattern Library and competitor universe from the intelligence snapshot:
- hook types
- body structures
- CTA styles
- topic clusters
- funnel roles
- discussion language

If signals conflict, prefer trust-building patterns and soft CTA styles for trust-and-audience accounts.

### Phase 3: Build Strategy Pack

Use the account profile, LinkedIn DNA, and Pattern Library to write the Strategy Pack:
- positioning statement
- audience lens
- competitor gap map
- funnel and content model
- 3-5 pillars
- CTA rules
- posting cadence

Do not copy competitor phrasing. Translate patterns into the account's own angle.

### Phase 4: Build 30-Day Plan

Generate a 30-Day Plan with 12-16 LinkedIn post briefs.

Each brief must include:
- funnel stage
- pillar tag
- hook direction
- proof asset
- soft CTA style
- supporting evidence IDs
- strategy constraints

### Phase 5: Build Image Briefs

For every post brief, generate Image Briefs with:
- visual angle
- composition direction
- text overlay guidance
- style constraints
- no-go list

No final image generation in this workflow.

### Phase 6: Save all artifacts

Save all artifacts to:
- `strategy/accounts/<account-slug>/account-profile.yaml`
- `strategy/accounts/<account-slug>/content-plan.yaml`
- `strategy/accounts/<account-slug>/strategy-pack.md`

## Guardrails

- Do not perform source discovery in this workflow.
- Use the approved intelligence snapshot as the upstream source of truth.
- Avoid hard-sell CTA drift if the account goal is trust and audience.
- If the intelligence snapshot is weak, flag it and stop short of inventing evidence.

## Output

Return a concise summary:
- what the approved intelligence snapshot suggests
- where artifacts were saved
- which 2-3 briefs are strongest to write next
