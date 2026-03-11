# Intelligence Workspace

This workspace stores reusable intelligence contracts outside of the strategy layer.

`intelligence/accounts/<account-slug>/` is the local-only workspace for discovery artifacts.
It feeds an approved intelligence snapshot into the strategist workflow.

## Workspace contract

Each account workspace should contain:

```text
intelligence/accounts/<account-slug>/
├── source-config.yaml
├── manual-context.md
├── discovered-sources.yaml
├── evidence-log.yaml
└── intelligence-snapshot.yaml
```

Use templates from `intelligence/templates/` when creating a new account.

## Runtime rules

- Treat `source-config.yaml` as the machine-readable discovery input.
- Treat `manual-context.md` as optional enrichment and hypothesis input.
- Treat `discovered-sources.yaml` as the candidate universe of accounts, sites, and discussion spaces.
- Treat `evidence-log.yaml` as the normalized evidence ledger with stable IDs.
- Treat `intelligence-snapshot.yaml` as the approved upstream input for strategy synthesis.

## Search strategies

The module preserves four search strategies as distinct labels:
- Direct competitor discovery
- Adjacent analog discovery
- Audience pain discovery
- Winning-content discovery

## Source tiers

Tier 1:
- LinkedIn
- Reddit
- websites/blogs

Tier 2 extensions:
- YouTube
- Instagram
- X
- newsletters
- comments/community signals

## Recommended commands

- `run intelligence` -> run `intelligence/workflows/discovery.md`
- `refresh intelligence` -> run `intelligence/workflows/refresh.md`
- `linkedin strategy` -> run `strategy/workflows/linkedin-strategist.md` using the approved intelligence snapshot
