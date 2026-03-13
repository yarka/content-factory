---
description: Publish router - reads config and routes to adapter
---

# Publish Router

Роутер для публикации статей. Читает конфиг и направляет к нужному adapter.

## Workflow

```
┌────────────────────┐
│  Read config.yaml  │
└─────────┬──────────┘
          │
          ▼
    Which adapter?
    ┌─────┼─────┐
    │     │     │
    ▼     ▼     ▼
telegram file  custom
    │     │     │
    ▼     ▼     ▼
 adapters/   adapters/   adapters/
telegram.md file-only.md custom.md
```

## Step 1: Read Config

Прочитай `config/config.yaml` и найди поле `output.adapter`:

```yaml
output:
  adapter: file-only  # telegram | file-only | custom
```

## Step 2: Load Adapter

| Adapter | File |
|---------|------|
| telegram | `publish/workflows/adapters/telegram.md` |
| file-only | `publish/workflows/adapters/file-only.md` |
| custom | `publish/workflows/adapters/custom.md` |

## Step 3: Execute Adapter

Прочитай соответствующий adapter файл и следуй инструкциям.

## Artifact Input

Canonical input artifact:
- `content/accounts/<account-slug>/posts/YYYY-MM-DD-slug.md`

The publish layer accepts any explicit `--file` path, but the repo should treat the per-account content workspace as the primary source of approved posts.

## Validation

Перед публикацией проверь:
- [ ] Config файл существует и читается
- [ ] Adapter value валидный
- [ ] Для telegram: токен и channel_id заданы
- [ ] Для file-only: output_dir существует

## Fallback

Если конфиг не найден — используй `file-only` по умолчанию.
