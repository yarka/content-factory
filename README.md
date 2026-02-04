# Blog Pipeline

Модульный pipeline для написания статей через AI-агентов.

**Работает с:** Claude Code, Cursor, Windsurf, GitHub Copilot, Aider и другими.

```
Questions → Research → Write → Deaify → Publish
```

## Что это

5-фазный воркфлоу для создания блог-постов:

1. **Questions** — уточняющие вопросы (угол, аудитория, takeaway)
2. **Research** — поиск источников через web search
3. **Write** — черновик 600+ слов с ASCII диаграммой
4. **Deaify** — 4 параллельных критика убирают AI-отпечатки
5. **Publish** — адаптер для Telegram, файла или своего сервиса

## Quick Start

```bash
# 1. Клонируй
git clone https://github.com/serejaris/blog-pipeline-template
cd blog-pipeline-template

# 2. Настрой конфиг
cp config/config.example.yaml config/config.yaml

# 3. Открой в своём AI-инструменте и скажи:
# "напиши статью про X"
```

## Совместимость

| Tool | Entry Point | Rules Location |
|------|-------------|----------------|
| **Claude Code** | `CLAUDE.md` | `rules/` |
| **Cursor** | `.cursor/rules/*.mdc` | symlinks → `rules/` |
| **Windsurf** | `.windsurf/rules/*.md` | symlinks → `rules/` |
| **Any AGENTS.md** | `AGENTS.md` | → symlink to `CLAUDE.md` |

Все инструменты читают один и тот же контент — `rules/` папка является canonical source.

## Структура

```
├── CLAUDE.md                   # Entry point (canonical)
├── AGENTS.md → CLAUDE.md       # Universal standard (symlink)
│
├── rules/                      # 📁 CANONICAL SOURCE
│   ├── blog-post.md           # Main 5-phase workflow
│   ├── deaify-text.md         # 4 parallel critics
│   ├── writing-guide.md       # Style, hooks, rhythm
│   ├── ai-terms-ru.md         # AI terms glossary
│   └── publish/
│       ├── publish.md         # Adapter router
│       └── adapters/
│           ├── telegram.md
│           ├── file-only.md
│           └── custom.md
│
├── .cursor/rules/              # Cursor (symlinks)
├── .windsurf/rules/            # Windsurf (symlinks)
│
├── config/
│   └── config.example.yaml
│
└── docs/
    ├── SETUP.md
    ├── CUSTOMIZATION.md
    └── ADAPTERS.md
```

## Адаптеры

| Adapter | Что делает |
|---------|------------|
| `telegram` | Очередь + scheduler для Telegram канала |
| `file-only` | Сохраняет markdown в папку |
| `custom` | Шаблон для своего сервиса |

Выбор в `config/config.yaml`:

```yaml
output:
  adapter: file-only  # telegram | file-only | custom
  output_dir: output/posts
```

## Документация

- [Установка](docs/SETUP.md)
- [Кастомизация](docs/CUSTOMIZATION.md)
- [Свои адаптеры](docs/ADAPTERS.md)

## Standards

- [AGENTS.md](https://agents.md) — universal open standard (60k+ projects)
- [Cursor Rules](https://docs.cursor.com/context/rules-for-ai) — `.cursor/rules/*.mdc`
- [Windsurf Rules](https://docs.windsurf.com) — `.windsurf/rules/*.md`

## Референс

Статья: [Пайплайн для блог-постов](https://sereja.tech/blog/blog-post-pipeline)

## License

MIT
