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
├── intelligence-snapshot.yaml
├── coverage-report.yaml
└── research-report.md
```

Use templates from `intelligence/templates/` when creating a new account.
Discovery artifacts are saved by default after every `run intelligence` or `refresh intelligence` pass.

## Runtime rules

- Treat `source-config.yaml` as the machine-readable discovery input.
- Treat `manual-context.md` as optional enrichment and hypothesis input.
- Treat `discovered-sources.yaml` as the candidate universe of accounts, sites, and discussion spaces.
- Treat `evidence-log.yaml` as the normalized evidence ledger with stable IDs.
- Treat `intelligence-snapshot.yaml` as the approved upstream input for strategy synthesis.
- Treat `coverage-report.yaml` as the quality gate for readiness and gaps.
- Treat `research-report.md` as the primary human-readable research output.
- Treat `external_data_sources` in `source-config.yaml` as supported private or manually curated datasets.
- Treat manual competitor research as a first-class strategic input when it is saved as a `manual_competitor_research_pack`.

## Quality gate

Use a `Practical V1` quality bar for initial strategy work:
- `12-15 discovered entities`
- `25-40 evidence records`
- coverage across all four search strategies
- at least 3 source families
- aim for `4+` direct competitors when available
- aim for `4+` adjacent analogs
- aim for `8+` buyer pain signals
- aim for `8+` winning content examples

Valid readiness statuses:
- `ready_for_strategy`
- `warning_needs_enrichment`
- `blocked_missing_brief`

LinkedIn-native coverage is desirable but not a hard blocker if broader cross-source coverage is strong.

## Discovery engines

- `Exa MCP` is the preferred discovery engine for public web research when it is available in the runtime.
- `web search` is the fallback discovery engine when `Exa MCP` is unavailable.
- The acquisition tool should be recorded separately from the source family so the same source can later be gathered by a connector or manual import.

## External data sources

Use `external_data_sources` for non-public-web inputs that still belong in discovery.

Example source types:
- `private_market_signal`
- `manual_competitor_export`
- `manual_competitor_research_pack`
- `crm_win_loss_notes`

Example origins:
- `upwork_manual_export`
- `sales_call_notes`
- `manual_research_dump`
- `founder_manual_research`

Manual competitor research can include:
- profile links
- screenshots
- positioning notes
- funnel observations
- featured section breakdowns
- lead magnet breakdowns
- what to copy vs what to reject

The strategist should be able to turn this manual competitor research into:
- packaging patterns worth adapting
- patterns to reject because they break authenticity
- profile and featured recommendations
- content-series implications

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

- `start linkedin pilot` -> run `orchestrator/workflows/start-linkedin-pilot.md`
- `continue linkedin pilot` -> run `orchestrator/workflows/continue-linkedin-pilot.md`
- `review intelligence coverage` -> review `coverage-report.yaml` and `research-report.md`
- `run intelligence` -> run `intelligence/workflows/discovery.md`
- `refresh intelligence` -> run `intelligence/workflows/refresh.md`
- `linkedin strategy` -> run `strategy/workflows/linkedin-strategist.md` using the approved intelligence snapshot
