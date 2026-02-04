# Blog Pipeline Template

Модульный pipeline для написания статей через Claude Code.

```
Questions → Research → Write → Deaify → Publish
```

## Что это

5-фазный воркфлоу для создания блог-постов:

1. **Questions** — уточняющие вопросы (угол, аудитория, takeaway)
2. **Research** — поиск источников через Exa
3. **Write** — черновик 600+ слов с ASCII диаграммой
4. **Deaify** — 4 параллельных критика убирают AI-отпечатки
5. **Publish** — адаптер для Telegram, файла или своего сервиса

## Quick Start

```bash
# 1. Клонируй template
gh repo create my-blog-pipeline --template serejaris/blog-pipeline-template
cd my-blog-pipeline

# 2. Настрой конфиг
cp config/config.example.yaml config/config.yaml
# Отредактируй config.yaml под себя

# 3. Готово! Теперь в Claude Code:
# "напиши статью про X"
```

## Структура

```
├── skills/
│   ├── blog-post/           # Main skill (Phase 1-3)
│   │   ├── skill.md         # Workflow
│   │   ├── writing-guide.md # Стиль и хуки
│   │   └── ai-terms-ru.md   # AI терминология
│   │
│   ├── deaify-text/         # Phase 4
│   │   └── skill.md         # 4 параллельных критика
│   │
│   └── publish/             # Phase 5
│       ├── skill.md         # Router
│       └── adapters/
│           ├── telegram.md  # Telegram канал
│           ├── file-only.md # Просто файл
│           └── custom.md    # Шаблон своего
│
├── config/
│   └── config.example.yaml  # Шаблон конфига
│
└── docs/
    ├── SETUP.md             # Установка
    ├── CUSTOMIZATION.md     # Адаптация
    └── ADAPTERS.md          # Свои adapters
```

## Адаптеры

| Adapter | Что делает |
|---------|------------|
| `telegram` | Очередь + scheduler для Telegram канала |
| `file-only` | Сохраняет markdown в папку |
| `custom` | Шаблон для своего сервиса |

Выбор адаптера — в `config/config.yaml`:

```yaml
output:
  adapter: telegram  # или file-only
```

## Документация

- [Установка](docs/SETUP.md) — как настроить
- [Кастомизация](docs/CUSTOMIZATION.md) — как адаптировать под себя
- [Адаптеры](docs/ADAPTERS.md) — как писать свои

## Референс

Этот template сделан на основе статьи: [Пайплайн для блог-постов](https://sereja.tech/blog/blog-post-pipeline)

## License

MIT
