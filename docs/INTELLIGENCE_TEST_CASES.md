# Intelligence Module Test Cases

Use this checklist when validating the new `intelligence/` workspace.

## Acceptance checklist

1. Workspace contract
   Expected: tracked templates live in `intelligence/templates/`, account artifacts live in `intelligence/accounts/` and remain gitignored.

2. Business-brief-only happy path
   Input only `source-config.yaml` plus optional empty manual context.
   Expected: the workflow still creates discovered sources, evidence log, intelligence snapshot, coverage report, and research report.

3. Discovery artifacts are persisted automatically
   Expected: `run intelligence` saves `discovered-sources.yaml`, `evidence-log.yaml`, `intelligence-snapshot.yaml`, `coverage-report.yaml`, and `research-report.md` before reporting findings in chat.

4. Four search strategies stay distinct
   Expected: direct competitor discovery, adjacent analog discovery, audience pain discovery, and winning-content discovery are preserved as separate labels in the artifacts.

5. Tier 1 source sufficiency
   Expected: LinkedIn, Reddit, and websites/blogs are enough to produce a useful snapshot for the AI consulting pilot.

6. Practical V1 quality bar
   Expected: the pass targets at least `12-15` discovered entities, `25-40` evidence records, all four search strategies, and 3 source families.

7. Discovery engine fallback
   Expected: the workflow prefers `Exa MCP` when available and records `web_search` when it falls back.

8. Weak direct competitor discovery
   Expected: the module falls back to adjacent analogs and records the fallback explicitly.

9. Discussion language capture
   Expected: comment and thread language appears in normalized evidence, not only post summaries.

10. Coverage status and warning behavior
   Expected: weak passes are marked `warning_needs_enrichment`, not silently treated as complete.

11. External manual datasets
   Expected: `external_data_sources` such as `upwork_manual_export` can be referenced without copying raw files into the repo.

12. Reusable-core validation
   Expected: the same templates support a second business without contract changes.

13. Strategy handoff
   Expected: `strategy/workflows/linkedin-strategist.md` consumes the approved intelligence snapshot instead of running source discovery itself.
