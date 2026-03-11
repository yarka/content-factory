# Content Module

This module owns content creation.

It is responsible for:
- channel DNA
- writing guide
- AI terminology guidance
- core drafting pipeline
- fact-check
- de-AI-fy quality pass
- platform adapters

## Inputs

- raw idea, references, or approved strategy brief
- `strategy/accounts/<account-slug>/content-plan.yaml`
- `intelligence/accounts/<account-slug>/intelligence-snapshot.yaml`

## Outputs

- approved final post artifact in `output/posts/`
- platform-adapted content ready for publish

## Entry points

- `content/workflows/core-pipeline.md`
- `content/workflows/blog-post.md`
- `content/workflows/telegram-post.md`
- `content/workflows/adapters/*.md`
