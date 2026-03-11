# Publish Module

This module owns delivery and distribution.

It is responsible for:
- publish routing
- publish adapters
- Telegram delivery
- LinkedIn delivery

## Inputs

- approved post artifact from `output/posts/`
- `config/config.yaml`

## Outputs

- published post on the target platform
- delivery status and preview confirmation

## Entry points

- `publish/workflows/publish.md`
- `publish/publish.py`
- `publish/publish_linkedin.py`
