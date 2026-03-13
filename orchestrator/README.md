# Orchestrator Workspace

This module is the guided entrypoint for the LinkedIn pilot flow.

It does not replace the underlying modules. It routes the user through:

```text
business brief -> intelligence -> coverage review -> strategy -> content
```

## Workspace contract

Each pilot workspace may contain:

```text
orchestrator/accounts/<account-slug>/
└── pilot-status.yaml
```

Use templates from `orchestrator/templates/` when creating a new account workspace.

`pilot-status.yaml` is the persisted state for the guided flow. On the same machine, a new session should resume from this file instead of relying on chat memory.

## Responsibilities

- collect or validate the business brief
- ask for optional private/manual sources
- run the intelligence module
- review `coverage-report.yaml` and `research-report.md`
- decide whether the flow is `ready_for_strategy`, `warning_needs_enrichment`, or `blocked_missing_brief`
- hand off to `strategy` when appropriate
- suggest the next brief to write in `content`
- proactively recommend the highest-leverage next step and explain the reason instead of waiting for the user to guess the flow
- after post approval, push the user toward visual generation and publish instead of ending at text
- recompute the next step from saved artifacts and publication state instead of trusting a stale `next_action`

## Recommended commands

- `start linkedin pilot` -> run `orchestrator/workflows/start-linkedin-pilot.md`
- `continue linkedin pilot` -> run `orchestrator/workflows/continue-linkedin-pilot.md`
- `review intelligence coverage` -> review the saved intelligence quality gate artifacts
