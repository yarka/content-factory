# Telegram Adapter

Публикация превью статьи в Telegram канал с очередью.

## Требования

- Telegram бот с токеном
- Канал, где бот — администратор
- `config/config.yaml` с секцией `telegram`

## Workflow

```
┌────────────────────┐
│  Generate preview  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│   Save to queue    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Schedule publish  │
└────────────────────┘
```

## Step 1: Generate Preview

Сгенерируй превью статьи:

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

Создай очередь постов (JSON файл или база):

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

Логика:
1. Найди последнюю дату в очереди
2. Следующий пост = последняя дата + 1 день
3. Добавь новый пост с `status: pending`

## Step 3: Scheduler

Нужен процесс для автоматической отправки. Варианты:

**macOS:** launchd
**Linux:** cron
**Cloud:** GitHub Actions

Пример скрипта отправки:

```python
import json
import requests
from datetime import date

def send_telegram(token, channel_id, html):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": channel_id,
        "text": html,
        "parse_mode": "HTML"
    }
    return requests.post(url, json=data)

# Load config, check queue, send if scheduled_date == today
```

## Пример превью

```html
<b>$87 в месяц на LLM — посмотрел логи и понял где дыра</b>

Pro-модель тратила 80% токенов на поиск. Разделил на два этапа — счёт упал до $35.

→ <a href="https://example.com/blog/post">Читать</a>
```

## Checklist

- [ ] Preview: 4-6 строк
- [ ] Есть `<b>` hook
- [ ] Есть `<a href>` ссылка
- [ ] Нет emoji и хештегов
- [ ] Дата публикации назначена
