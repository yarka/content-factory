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

Write three artifacts:
- `discovered-sources.yaml`
- `evidence-log.yaml`
- `intelligence-snapshot.yaml`

Every evidence record must keep:
- stable evidence ID
- source family
- source type
- strategy type
- entity ID
- URL
- summary
- confidence
- discussion language

## Guardrails

- Do not collapse the four search strategies into one undifferentiated list.
- If direct competitors are weak, fall back to adjacent analogs and record the fallback.
- Keep Tier 1 coverage explicit even if Tier 2 sources are mentioned.
- Do not write strategy artifacts in this workflow.

## Output

Return:
- what entities were discovered
- which sources produced the strongest evidence
- where the approved intelligence snapshot was saved
