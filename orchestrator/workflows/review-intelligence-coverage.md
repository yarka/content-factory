---
description: Review Intelligence Coverage - summarizes the saved intelligence quality gate before strategy
globs:
  - "**/*.md"
  - "**/*.yaml"
---

# Review Intelligence Coverage

Use this when the user says `review intelligence coverage` or wants to know whether the research is strong enough.

## Workflow

1. Read `intelligence/accounts/<account-slug>/coverage-report.yaml`.
2. Read `intelligence/accounts/<account-slug>/research-report.md`.
3. Summarize:
   - overall status
   - strong areas
   - weak areas
   - missing source families or strategies
   - whether manual enrichment is recommended

## Output

Return:
- readiness status
- strongest signals
- weakest gaps
- whether strategy should run next
