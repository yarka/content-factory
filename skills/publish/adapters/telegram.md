# Telegram Adapter

Публикация превью статьи в Telegram канал с очередью.

## Требования

- Telegram бот с токеном
- Канал, где бот — администратор
- `config/config.yaml` с секцией `telegram`

## Workflow

```
┌────────────────────┐
│  Generate preview  │  ← Task(haiku)
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   Save to queue    │  ← queue.json или база
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Schedule publish  │  ← cron/launchd/Actions
└────────────────────┘
```

## Step 1: Generate Preview

Используй Task(model: haiku) для генерации превью:

```
Напиши превью статьи для Telegram канала.

URL: {url статьи}

ФОРМАТ (строго):
<b>Hook — цепляющая фраза про боль/результат</b>

Тезис — что получит читатель, 1-2 предложения.

→ <a href="URL">Читать</a>

ПРАВИЛА:
- МАКСИМУМ 5 строк (hook + 1-2 предложения + ссылка)
- HTML теги: <b> для заголовка, <a href="..."> для ссылки
- НИКАКИХ emoji, хештегов, markdown
- Личный тон (я сделал, я понял)

Верни ТОЛЬКО готовый HTML текст.
```

## Step 2: Save to Queue

Создай очередь постов. Простейший вариант — JSON файл:

```json
{
  "queue": [
    {
      "id": "uuid",
      "html": "<b>Hook</b>\n\nТезис.\n\n→ <a href=\"url\">Читать</a>",
      "scheduled_date": "2026-01-20",
      "status": "pending"
    }
  ]
}
```

Логика добавления:
1. Найди последнюю дату в очереди
2. Следующий пост = последняя дата + 1 день
3. Добавь новый пост с `status: pending`

## Step 3: Scheduler

Нужен процесс, который запускается по расписанию и отправляет посты.

### Варианты реализации

**macOS (launchd):**
```xml
<!-- ~/Library/LaunchAgents/com.blog.scheduler.plist -->
<plist>
  <dict>
    <key>Label</key>
    <string>com.blog.scheduler</string>
    <key>ProgramArguments</key>
    <array>
      <string>/usr/bin/python3</string>
      <string>/path/to/scheduler.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
      <key>Hour</key>
      <integer>19</integer>
      <key>Minute</key>
      <integer>0</integer>
    </dict>
  </dict>
</plist>
```

**Linux (cron):**
```
0 19 * * * python3 /path/to/scheduler.py
```

**GitHub Actions:**
```yaml
on:
  schedule:
    - cron: '0 16 * * *'  # UTC = 19:00 MSK
jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python3 scheduler.py
```

## Скрипт отправки

Агент должен создать скрипт примерно такого вида:

```python
import json
import requests
from datetime import date

def send_telegram(token, channel_id, html):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": channel_id,
        "text": html,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    return requests.post(url, json=data)

def main():
    # Load config
    with open("config/config.yaml") as f:
        config = yaml.safe_load(f)

    # Load queue
    with open("queue.json") as f:
        queue = json.load(f)

    today = date.today().isoformat()

    for post in queue["queue"]:
        if post["scheduled_date"] == today and post["status"] == "pending":
            send_telegram(
                config["telegram"]["bot_token"],
                config["telegram"]["channel_id"],
                post["html"]
            )
            post["status"] = "sent"

    # Save updated queue
    with open("queue.json", "w") as f:
        json.dump(queue, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
```

## Формат превью (пример)

```html
<b>$87 в месяц на LLM — посмотрел логи и понял где дыра</b>

Pro-модель тратила 80% токенов на поиск в JSON. Разделил на два этапа — Flash ищет, Pro пишет. Счёт упал до $35.

→ <a href="https://example.com/blog/two-stage-ai-pipeline">Читать</a>
```

## Checklist

- [ ] Preview: 4-6 строк
- [ ] Есть `<b>` hook
- [ ] Есть `<a href>` ссылка
- [ ] Нет emoji
- [ ] Нет хештегов
- [ ] Нет markdown (`**`, `#`)
- [ ] Дата публикации назначена
