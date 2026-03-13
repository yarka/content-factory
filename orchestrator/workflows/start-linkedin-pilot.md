---
description: LinkedIn Pilot Orchestrator - guides the user through onboarding, intelligence, coverage review, strategy, and content handoff
globs:
  - "**/*.md"
  - "**/*.yaml"
---

# Start LinkedIn Pilot

Language rule: detect the language the user writes in and respond in that language throughout the workflow.

This is the guided entrypoint for the LinkedIn pilot. It should feel like a manager flow, not a loose list of commands.
The orchestrator should behave proactively: recommend the next move, explain why this is the best move now, and keep the user moving instead of waiting passively for commands.

## Workflow

1. Check whether a valid business brief already exists in:
   - `strategy/accounts/<account-slug>/account-profile.yaml`
   - `intelligence/accounts/<account-slug>/source-config.yaml`
2. If the brief is incomplete, collect the missing business brief fields before running anything else.
3. Before running research, collect the user's unique advantage and human context when missing:
   - operator or founder background
   - mission
   - values
   - worldview about how change should happen inside a team or company
   - public proof points they are comfortable using in content
4. Ask for optional private/manual sources such as Upwork exports, reference post dumps, or sales notes.
5. Save the user's unique angle and values into the account profile and manual context before running research.
6. run `intelligence` using the saved source config and manual context.
7. Review the saved coverage report and research report.
8. If coverage is weak, return a warning, explain the gaps, and propose manual enrichment.
9. If the user wants to continue despite the warning, say that `linkedin strategy` will be built with warning context.
10. If coverage is strong enough, run `linkedin strategy`.
11. Summarize the strongest briefs and offer `write from strategy brief` as the next step.

## Rules

- Do not expect the user to know module commands ahead of time.
- Always point the user to the saved artifacts after each phase.
- Treat `coverage-report.yaml` as the quality gate.
- Treat `research-report.md` as the primary human-readable research file.
- Treat the user's mission, values, and unique operator background as first-class strategy inputs, not optional fluff.
- If the brief is missing critical fields, set the status to `blocked_missing_brief`.
- If coverage is weak but usable, set the status to `warning_needs_enrichment`.
- If coverage is strong, set the status to `ready_for_strategy`.

## Output

Return:
- current pilot status
- which artifact to review now
- whether the next step is manual enrichment, linkedin strategy, or write from strategy brief
- recommended next step
- why this is the best move now
- 1-3 concrete options the user can take immediately
