---
description: Continue LinkedIn Pilot - resumes the guided pilot flow from saved artifacts and status
globs:
  - "**/*.md"
  - "**/*.yaml"
---

# Continue LinkedIn Pilot

Use this when the user says `continue linkedin pilot`, asks what to do next, or wants to resume after adding sources or reviewing reports.

## Workflow

1. Read `orchestrator/accounts/<account-slug>/pilot-status.yaml` if it exists.
2. Read the linked `coverage-report.yaml`, `research-report.md`, and `intelligence-snapshot.yaml`.
3. If status is `blocked_missing_brief`, continue gathering missing business brief fields.
4. If status is `warning_needs_enrichment`, propose the highest-leverage manual enrichment or rerun intelligence.
5. If status is `ready_for_strategy` and strategy artifacts do not exist, run `linkedin strategy`.
6. If strategy artifacts already exist, recommend the strongest brief and offer `write from strategy brief`.

## Output

Return:
- the saved status
- what changed since the last phase
- the best next action
