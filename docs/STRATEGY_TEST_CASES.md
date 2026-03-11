# LinkedIn Strategist V1 Test Cases

Use this checklist when validating a new account workspace or refreshing an existing one.

## Acceptance checklist

1. Business-brief-only happy path
   Input only `account-profile.yaml` and no competitor list.
   Expected: strategy pack and 30-day plan are produced from the approved intelligence snapshot.

2. Manual enrichment merge
   Add notes, reference posts, or UVP analysis to `manual-context.md`.
   Expected: outputs preserve discovered signals and visibly reflect manual enrichment.

3. Weak competitor discovery
   Use a narrow or weak niche brief.
   Expected: strategist falls back to adjacent analogs, flags confidence, and still produces a usable strategy pack.

4. Conflicting competitor patterns
   Include evidence with both hard-sell and trust-first patterns.
   Expected: trust-and-audience accounts prefer soft CTA patterns.

5. Reusable-core validation
   Run the workflow on a second hypothetical business.
   Expected: artifacts still fit the same templates and rule flow.

6. Content handoff
   Pick one post brief from `content-plan.yaml`.
   Expected: `content/workflows/core-pipeline.md` can write from that brief without extra strategic guessing.

7. Image-brief quality
   Review every `image_brief`.
   Expected: each has concept, composition direction, text overlay guidance, style constraints, and a no-go list.

8. Refresh behavior
   Run `refresh linkedin strategy` after changing evidence.
   Expected: a `Refresh Delta` report is created from the refreshed intelligence snapshot and approved strategy is not silently replaced.

9. Guardrails
   Review strategy pack and briefs.
   Expected: no hard-sell CTA drift, no generic AI-slop pillars, no ignored lead magnet, no conflict with LinkedIn DNA voice.
