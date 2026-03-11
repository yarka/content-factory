# Intelligence Module Test Cases

Use this checklist when validating the new `intelligence/` workspace.

## Acceptance checklist

1. Workspace contract
   Expected: tracked templates live in `intelligence/templates/`, account artifacts live in `intelligence/accounts/` and remain gitignored.

2. Business-brief-only happy path
   Input only `source-config.yaml` plus optional empty manual context.
   Expected: the workflow still creates discovered sources, evidence log, and intelligence snapshot.

3. Four search strategies stay distinct
   Expected: direct competitor discovery, adjacent analog discovery, audience pain discovery, and winning-content discovery are preserved as separate labels in the artifacts.

4. Tier 1 source sufficiency
   Expected: LinkedIn, Reddit, and websites/blogs are enough to produce a useful snapshot for the AI consulting pilot.

5. Weak direct competitor discovery
   Expected: the module falls back to adjacent analogs and records the fallback explicitly.

6. Discussion language capture
   Expected: comment and thread language appears in normalized evidence, not only post summaries.

7. Reusable-core validation
   Expected: the same templates support a second business without contract changes.

8. Strategy handoff
   Expected: `strategy/workflows/linkedin-strategist.md` consumes the approved intelligence snapshot instead of running source discovery itself.
