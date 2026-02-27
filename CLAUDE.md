# Контент-завод

Персональный AI-пайплайн для создания аутентичного контента.

```
Идея → Core Pipeline → Adapter → Publish
```

---

## Как использовать

**Первый запуск:**
> "запусти setup" — онбординг, заполняет channel-dna.md

**Написать пост:**
> Просто скажи идею → pipeline запустится сам

**Только deaify:**
> "деаишь этот текст: ..."

---

## Архитектура

```
         channel-dna.md
         writing-guide.md
               │
               ▼
     ┌─────────────────────┐
     │    Core Pipeline    │
     │  Questions          │
     │  Research           │  ← Авто (Exa) или референсы
     │  Write              │  ← Заголовок + core draft
     │  Fact-check         │  ← Exa MCP / WebFetch
     │  Deaify             │  ← 4 параллельных критика
     └──────────┬──────────┘
                │
     ┌──────────▼──────────┐
     │   Выбор адаптера    │
     └──┬────────┬────┬────┘
        │        │         │
        ▼        ▼         ▼
   Telegram  LinkedIn   Threads
   RU, HTML  EN, plain  RU, 500
   до 1500   до 3000    символов
```

**Ядро одно. Адаптеры разные.**

---

## Skills

| Trigger | Файл | Что делает |
|---------|------|------------|
| "setup", "настрой канал" | `rules/setup.md` | Онбординг основного канала |
| "настрой linkedin", "setup linkedin" | `rules/setup.md` → Platform Setup | Онбординг LinkedIn DNA |
| "настрой threads", "setup threads" | `rules/setup.md` → Platform Setup | Онбординг Threads DNA |
| идея для поста, "напиши пост" | `rules/core-pipeline.md` | Полный pipeline |
| "в телеграм", "telegram" | `rules/adapters/telegram.md` | Telegram адаптер |
| "в linkedin" | `rules/adapters/linkedin.md` | LinkedIn адаптер (читает channel-dna-linkedin.md) |
| "в threads" | `rules/adapters/threads.md` | Threads адаптер (короткий) |
| "деаишь", "humanize" | `rules/deaify-text.md` | Только deaify |
| "напиши статью", длинный формат | `rules/blog-post.md` | Оригинальный pipeline |

---

## Файлы

| Файл | Назначение |
|------|------------|
| `channel-dna.md` | ДНК основного канала (Telegram) |
| `channel-dna-linkedin.md` | ДНК LinkedIn — цель, язык, голос, референсы |
| `channel-dna-{platform}.md` | ДНК для каждой новой платформы |
| `rules/writing-guide.md` | Стиль и голос автора |
| `rules/core-pipeline.md` | Основной pipeline |
| `rules/fact-check.md` | Проверка фактов |
| `rules/deaify-text.md` | 4 параллельных критика |
| `rules/adapters/telegram.md` | Telegram: HTML, RU, до 1500 |
| `rules/adapters/linkedin.md` | LinkedIn: plain text, EN, до 3000 |
| `rules/adapters/threads.md` | Threads: plain text, до 500 |
| `rules/setup.md` | Онбординг |
| `publish.py` | Публикация (staging/production) |
| `config/config.yaml` | Токены и окружения |
| `output/posts/` | Готовые черновики |

---

## Правила

- Читай `channel-dna.md` перед каждым постом
- Не выдумывай факты — спроси или оставь плейсхолдер
- Deaify обязателен для каждого поста
- Тире только короткие (–)
