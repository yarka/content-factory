---
name: publish
description: Публикация готовой статьи через выбранный adapter. Читает config/config.yaml и направляет к нужному output. Триггеры — "опубликуй", "publish"
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

```bash
cat config/config.yaml
```

Найди поле `output.adapter`. Возможные значения:
- `telegram` — очередь в Telegram канал
- `file-only` — сохранить в папку
- `custom` — пользовательский adapter

## Step 2: Load Adapter

В зависимости от значения `output.adapter`, прочитай соответствующий файл:

| Adapter | File |
|---------|------|
| telegram | `skills/publish/adapters/telegram.md` |
| file-only | `skills/publish/adapters/file-only.md` |
| custom | `skills/publish/adapters/custom.md` |

## Step 3: Execute Adapter

Следуй инструкциям из загруженного adapter файла.

## Config Structure

```yaml
output:
  adapter: telegram  # telegram | file-only | custom
  output_dir: output/posts  # для file-only

telegram:
  bot_token: ${TELEGRAM_BOT_TOKEN}
  channel_id: "@mychannel"
  schedule_time: "19:00"
  timezone: "Europe/Moscow"
```

## Validation

Перед публикацией проверь:
- [ ] Config файл существует и читается
- [ ] Adapter value валидный
- [ ] Для telegram: токен и channel_id заданы
- [ ] Для file-only: output_dir существует или создаётся

## Fallback

Если конфиг не найден или adapter не указан — используй `file-only` по умолчанию.
