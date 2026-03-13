---
description: LinkedIn Strategy Refresh - consumes refreshed intelligence and proposes delta updates without overwriting the approved strategy
globs:
  - "**/*.md"
  - "**/*.yaml"
---

# LinkedIn Strategy Refresh

Use this when the user says `refresh linkedin strategy`, `weekly refresh`, or asks what changed in the niche.

Always read first:
1. `strategy/accounts/<account-slug>/account-profile.yaml`
2. `intelligence/accounts/<account-slug>/intelligence-snapshot.yaml`
3. `strategy/accounts/<account-slug>/content-plan.yaml`
4. `strategy/accounts/<account-slug>/strategy-pack.md`
5. `content/channel-dna-linkedin.md`

## Workflow

1. rerun intelligence discovery via `intelligence/workflows/refresh.md` before updating any strategy conclusion
2. compare against the previous snapshot and note net-new competitors, hook shifts, CTA changes, or topic changes
3. read the refreshed intelligence snapshot with fresh evidence IDs and date metadata
4. draft a Refresh Delta report with recommended adds/removals for the content plan
5. note whether pillars, CTA guidance, or cadence should change

## Refresh Delta rules

- Title the report `Refresh Delta`
- Include a section for recommended adds/removals
- Include a section for strategy impact
- Do not silently overwrite approved strategy or content plans
- If the refresh only changes evidence, say so explicitly

## Output

Return:
- what changed
- whether the strategy should change
- which briefs to add, pause, or rewrite
