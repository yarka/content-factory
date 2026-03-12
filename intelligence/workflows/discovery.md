---
description: Intelligence Discovery - builds a normalized intelligence snapshot from tiered sources and four search strategies
globs:
  - "**/*.md"
  - "**/*.yaml"
---

# Intelligence Discovery

Language rule: detect the language the user writes in and respond in that language throughout the workflow.

This module is upstream from strategy. It is responsible for discovery, normalization, and evidence synthesis only.

## Inputs

Always read first:
1. `intelligence/accounts/<account-slug>/source-config.yaml`
2. `intelligence/accounts/<account-slug>/manual-context.md`
3. `content/channel-dna-linkedin.md` when LinkedIn is the primary platform
4. `intelligence/README.md`

If the account workspace does not exist, create it from `intelligence/templates/`.

## Quality bar

Use the `Practical V1` quality bar for initial strategy work:
- target `12-15 discovered entities`
- target `25-40 evidence records`
- preserve all four search strategies
- cover at least 3 source families
- aim for `4+` direct competitors when available
- aim for `4+` adjacent analogs
- aim for `8+` buyer pain signals
- aim for `8+` winning content examples

If the pass misses the quality bar, mark the saved outputs as `warning_needs_enrichment` instead of pretending the research is complete.

## Discovery engine

- `Exa MCP` is the preferred discovery engine for public-web discovery when available.
- `web search` is the Web search fallback when `Exa MCP` is unavailable in the runtime.
- Record the actual acquisition mode used in `discovered-sources.yaml` and `evidence-log.yaml`.
- Keep source family and acquisition mode separate. Example: `source_family: reddit`, `acquisition_mode: exa_mcp`.

## Tier 1 sources

Use Tier 1 sources first:
- LinkedIn
- Reddit
- websites/blogs

Treat discussion language from comments, replies, and thread dynamics as a first-class signal in the evidence model.

## Tier 2 extensions

Keep these as extension seams unless the user explicitly supplies them:
- YouTube
- Instagram
- X
- newsletters
- comments/community signals outside Tier 1

## Four search strategies

### Direct competitor discovery

- Find direct competitors that share the offer, audience, or funnel shape.
- Save them to `discovered-sources.yaml` with `strategy_type: direct_competitor_discovery`.

### Adjacent analog discovery

- Find adjacent analogs when the direct competitor set is thin or low-confidence.
- Preserve these as a separate strategy label instead of mixing them into direct competitors.

### Audience pain discovery

- Search Reddit and other discussion-heavy sources for recurring audience pain language.
- Capture the pain phrases, objections, and language patterns in normalized evidence.

### Winning-content discovery

- Find content examples that perform well for the topic, angle, or funnel role.
- Preserve why the content matters: hook pattern, proof format, CTA style, or discussion response.

## Normalization

Write five artifacts:
- `discovered-sources.yaml`
- `evidence-log.yaml`
- `intelligence-snapshot.yaml`
- `coverage-report.yaml`
- `research-report.md`

Always save the discovery artifacts to the account workspace before returning a summary in chat.
If an external dataset is used, preserve its source metadata in the saved artifacts instead of keeping it only in the narrative response.

Every evidence record must keep:
- stable evidence ID
- source family
- source type
 - source origin
 - acquisition mode
 - strategy type
 - entity ID
 - URL
 - summary
- confidence
- discussion language

After normalization:
1. dedupe and cluster similar evidence
2. compute coverage by strategy and source family
3. compute confidence summary and cross-source agreement
4. assign one readiness status:
   - `ready_for_strategy`
   - `warning_needs_enrichment`
   - `blocked_missing_brief`
5. save both `coverage-report.yaml` and `research-report.md`

## Guardrails

- Do not collapse the four search strategies into one undifferentiated list.
- If direct competitors are weak, fall back to adjacent analogs and record the fallback.
- Keep Tier 1 coverage explicit even if Tier 2 sources are mentioned.
- Do not write strategy artifacts in this workflow.
- If coverage is weak, do not say `research complete`.
- Return a warning, enumerate what is missing, and propose manual enrichment.
- LinkedIn-native evidence is desirable but not a hard blocker when cross-source coverage is strong.

## Output

Return:
- what entities were discovered
- which sources produced the strongest evidence
- where the approved intelligence snapshot was saved
- where `coverage-report.yaml` and `research-report.md` were saved
