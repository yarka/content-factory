# Strategy Workspace

This workspace stores reusable strategy artifacts outside of `content/channel-dna-linkedin.md`.

`content/channel-dna-linkedin.md` stays the voice/platform contract.
`intelligence/accounts/<account-slug>/` stores discovery artifacts and normalized evidence.
`strategy/accounts/<account-slug>/` stores synthesis outputs and refresh reports.

## Workspace contract

Each account workspace should contain:

```text
strategy/accounts/<account-slug>/
├── account-profile.yaml
├── manual-context.md
├── content-plan.yaml
├── strategy-pack.md
└── refresh-report.md
```

Use templates from `strategy/templates/` when creating a new account.

## Runtime rules

- Treat `account-profile.yaml` as the machine-readable business brief.
- Treat `manual-context.md` as optional strategy notes, not a discovery source of truth.
- Treat `intelligence/accounts/<account-slug>/intelligence-snapshot.yaml` as the approved intelligence snapshot.
- Treat `content-plan.yaml` as the approved source for post briefs and image briefs.
- Treat `refresh-report.md` as a delta report only. Never silently overwrite approved strategy.

## Recommended commands

- `run intelligence` -> run `intelligence/workflows/discovery.md`
- `refresh intelligence` -> run `intelligence/workflows/refresh.md`
- `linkedin strategy` -> run `strategy/workflows/linkedin-strategist.md`
- `refresh linkedin strategy` -> run `strategy/workflows/refresh.md`
- `write from strategy brief` -> run `content/workflows/core-pipeline.md` using a selected brief from `content-plan.yaml`
