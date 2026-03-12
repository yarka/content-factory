---
description: LinkedIn Pilot Orchestrator - guides the user through onboarding, intelligence, coverage review, strategy, and content handoff
globs:
  - "**/*.md"
  - "**/*.yaml"
---

# Start LinkedIn Pilot

Language rule: detect the language the user writes in and respond in that language throughout the workflow.

This is the guided entrypoint for the LinkedIn pilot. It should feel like a manager flow, not a loose list of commands.

## Workflow

1. Check whether a valid business brief already exists in:
   - `strategy/accounts/<account-slug>/account-profile.yaml`
   - `intelligence/accounts/<account-slug>/source-config.yaml`
2. If the brief is incomplete, collect the missing business brief fields before running anything else.
3. Ask for optional private/manual sources such as Upwork exports, reference post dumps, or sales notes.
4. run `intelligence` using the saved source config and manual context.
5. Review the saved coverage report and research report.
6. If coverage is weak, return a warning, explain the gaps, and propose manual enrichment.
7. If the user wants to continue despite the warning, say that `linkedin strategy` will be built with warning context.
8. If coverage is strong enough, run `linkedin strategy`.
9. Summarize the strongest briefs and offer `write from strategy brief` as the next step.

## Rules

- Do not expect the user to know module commands ahead of time.
- Always point the user to the saved artifacts after each phase.
- Treat `coverage-report.yaml` as the quality gate.
- Treat `research-report.md` as the primary human-readable research file.
- If the brief is missing critical fields, set the status to `blocked_missing_brief`.
- If coverage is weak but usable, set the status to `warning_needs_enrichment`.
- If coverage is strong, set the status to `ready_for_strategy`.

## Output

Return:
- current pilot status
- which artifact to review now
- whether the next step is manual enrichment, linkedin strategy, or write from strategy brief
