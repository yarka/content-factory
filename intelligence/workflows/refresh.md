---
description: Intelligence Refresh - reruns discovery and updates the approved intelligence snapshot without changing strategy artifacts directly
globs:
  - "**/*.md"
  - "**/*.yaml"
---

# Intelligence Refresh

Use this when the user says `refresh intelligence`, `rerun discovery`, or asks what changed in the source landscape.

Always read first:
1. `intelligence/accounts/<account-slug>/source-config.yaml`
2. `intelligence/accounts/<account-slug>/discovered-sources.yaml`
3. `intelligence/accounts/<account-slug>/evidence-log.yaml`
4. `intelligence/accounts/<account-slug>/intelligence-snapshot.yaml`
5. `intelligence/accounts/<account-slug>/manual-context.md`

## Workflow

1. rerun the four search strategies using the current source config
2. compare against the previous snapshot and previous evidence log
3. update discovered sources, evidence log, intelligence snapshot, coverage report, and research report
4. record any fallback to adjacent analogs when direct competitor discovery is weak
5. create or update a refresh report in the intelligence workspace
6. save the refreshed artifacts before returning the delta summary

## Rules

- compare against the previous snapshot before summarizing change
- preserve stable evidence IDs when the same evidence persists
- keep fallback notes explicit
- prefer `Exa MCP` for public discovery and record `web_search` if fallback was required
- Do not update strategy artifacts directly
- write a refresh report that can be reviewed before the strategist refresh runs
- keep the readiness status up to date when coverage improves or degrades

## Output

Return:
- what changed
- whether fallback behavior was used
- whether the strategist should be rerun next
