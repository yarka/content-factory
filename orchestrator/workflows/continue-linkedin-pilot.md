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
3. Do not trust a stale `next_action` blindly.
4. Always recompute the next step from the saved artifacts and `published_artifacts`.
5. If status is `blocked_missing_brief`, continue gathering missing business brief fields.
6. If status is `warning_needs_enrichment`, propose the highest-leverage manual enrichment or rerun intelligence.
7. If status is `ready_for_strategy` and strategy artifacts do not exist, run `linkedin strategy`.
8. If strategy artifacts already exist, recommend the strongest brief and offer `write from strategy brief`.
9. If an approved post artifact already exists, recommend `linkedin visual` before publish unless a visual already exists for that post.
10. If both a saved post artifact and a saved visual exist and `published_artifacts` confirms publication, move the next action forward to the strongest unwritten brief instead of staying on the previous post.
11. Update the pilot status so `last_completed_action`, `next_action`, `recommended_step_reason`, and `published_artifacts` reflect the current state.
12. Do not stop at "what do you want to do next?". Recommend the best next action, explain why it matters, and offer 1-3 concrete options the user can take immediately.

## Output

Return:
- the saved status
- what changed since the last phase
- the best next action
- recommended next step
- why it matters
- 1-3 concrete options the user can choose from now
