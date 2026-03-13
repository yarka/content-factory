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
- local per-account post artifacts
- LinkedIn visual reference boards, visual DNA, and rendered cards

## Inputs

- raw idea, references, or approved strategy brief
- `strategy/accounts/<account-slug>/content-plan.yaml`
- `intelligence/accounts/<account-slug>/intelligence-snapshot.yaml`

## Outputs

- approved final post artifact in `content/accounts/<account-slug>/posts/`
- LinkedIn visual artifacts in `content/accounts/<account-slug>/visuals/`
- platform-adapted content ready for publish

## Workflow mode

`config/config.yaml` can set `content.workflow_mode`:
- `human_in_the_loop` for editor-style checkpoints before drafting
- `fully_automatic` for minimum-interruption generation from saved context

Default behavior is `human_in_the_loop`.

After each draft, the workflow should also return a short quality report:
- fact-check status
- deaify status
- what changed after critic pass

## Entry points

- `content/workflows/core-pipeline.md`
- `content/workflows/linkedin-visual.md`
- `content/workflows/blog-post.md`
- `content/workflows/telegram-post.md`
- `content/workflows/adapters/*.md`
