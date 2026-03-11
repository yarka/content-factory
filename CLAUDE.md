# Контент-завод

Модульный AI-пайплайн:

```
Setup -> Intelligence -> Strategy -> Content -> Publish
```

## Архитектура

```
content/channel-dna-linkedin.md
intelligence/accounts/*
         │
         ▼
┌─────────────────────┐
│ Intelligence Module │
│ Discovery           │
│ Evidence            │
│ Snapshot            │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  Strategy Module    │
│  Positioning        │
│  30-Day Plan        │
│  Briefs             │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│   Content Module    │
│   Pipeline          │
│   Fact-check        │
│   Deaify            │
│   Adapters          │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│   Publish Module    │
│   Router            │
│   Delivery          │
└─────────────────────┘
```

## Триггеры

| Trigger | Файл | Что делает |
|---------|------|------------|
| `setup`, `setup linkedin`, `настрой канал` | `setup/bootstrap.md` | Bootstrap локального конфига и DNA |
| `run intelligence` | `intelligence/workflows/discovery.md` | Строит discovered sources, evidence log и approved snapshot |
| `refresh intelligence` | `intelligence/workflows/refresh.md` | Обновляет discovery artifacts и snapshot |
| `linkedin strategy` | `strategy/workflows/linkedin-strategist.md` | Читает approved snapshot и строит strategy pack, plan, briefs |
| `refresh linkedin strategy` | `strategy/workflows/refresh.md` | Строит strategy delta без silent overwrite |
| идея для поста, `напиши пост` | `content/workflows/core-pipeline.md` | Полный content pipeline |
| `write from strategy brief` | `content/workflows/core-pipeline.md` | Пишет пост из сохранённого brief |
| `в телеграм`, `telegram` | `content/workflows/adapters/telegram.md` | Telegram адаптер |
| `в linkedin` | `content/workflows/adapters/linkedin.md` | LinkedIn адаптер |
| `в threads` | `content/workflows/adapters/threads.md` | Threads адаптер |
| `деаишь`, `humanize` | `content/workflows/deaify-text.md` | Только de-AI-fy |
| `publish` | `publish/workflows/publish.md` | Роутинг в publish adapters |

## Модули

| Путь | Назначение |
|------|------------|
| `content/` | DNA, writing guide, ai terms, pipeline, QA, adapters |
| `intelligence/` | discovery, evidence, snapshots |
| `strategy/` | synthesis, planning, refresh |
| `publish/` | delivery, publish adapters, scripts |
| `setup/` | bootstrap layer |
| `config/config.yaml` | токены и окружения |
| `output/posts/` | готовые артефакты для публикации |

## Правила

- `content` отвечает только за создание контента
- `publish` отвечает только за доставку
- `strategy` не делает discovery, а читает approved snapshot
- `intelligence` не пишет контент и не обновляет strategy artifacts напрямую
- Читай `content/channel-dna.md` перед каждым постом
- Не выдумывай факты — проверяй или ставь плейсхолдер
