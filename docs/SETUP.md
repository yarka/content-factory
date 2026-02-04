# Установка

## Требования

- AI-агент: Claude Code, Cursor, Windsurf, Copilot, или другой
- Git

## Шаг 1: Клонируй репозиторий

```bash
git clone https://github.com/serejaris/blog-pipeline-template my-blog-pipeline
cd my-blog-pipeline
```

## Шаг 2: Настрой конфиг

```bash
cp config/config.example.yaml config/config.yaml
```

Минимальный конфиг для старта:

```yaml
output:
  adapter: file-only
  output_dir: output/posts

content:
  min_words: 600
  require_diagram: true
  language: ru
```

## Шаг 3: Открой в своём инструменте

### Claude Code

```bash
cd my-blog-pipeline
claude
# "напиши статью про X"
```

Claude Code автоматически прочитает `CLAUDE.md`.

### Cursor

Открой папку в Cursor — он автоматически прочитает `.cursor/rules/*.mdc`.

### Windsurf

Открой папку в Windsurf — он автоматически прочитает `.windsurf/rules/*.md`.

### Другие инструменты

Любой инструмент, поддерживающий `AGENTS.md`, прочитает его (symlink на `CLAUDE.md`).

## Шаг 4: Для Telegram (опционально)

1. Создай бота через [@BotFather](https://t.me/BotFather)
2. Добавь бота админом в канал
3. Заполни `config.yaml`:

```yaml
output:
  adapter: telegram

telegram:
  bot_token: "123456:ABC-DEF..."
  channel_id: "@mychannel"
  schedule_time: "19:00"
  timezone: "Europe/Moscow"
```

## Структура после установки

```
my-blog-pipeline/
├── CLAUDE.md                   # Entry point
├── AGENTS.md → CLAUDE.md       # Universal (symlink)
│
├── rules/                      # Canonical source
│   ├── blog-post.md
│   ├── deaify-text.md
│   └── ...
│
├── .cursor/rules/              # Cursor symlinks
├── .windsurf/rules/            # Windsurf symlinks
│
├── config/
│   ├── config.example.yaml
│   └── config.yaml             # ← твой конфиг (gitignored)
│
└── output/posts/               # ← сюда сохраняются статьи
```

## Troubleshooting

### Symlinks не работают (Windows)

На Windows symlinks могут не работать. Скопируй файлы вручную:

```bash
# Для Cursor
cp rules/*.md .cursor/rules/
# Переименуй в .mdc если нужно

# Для Windsurf
cp rules/*.md .windsurf/rules/
```

### Правила не подхватываются

Проверь что файлы на месте:

```bash
ls -la CLAUDE.md AGENTS.md
ls -la rules/
ls -la .cursor/rules/ .windsurf/rules/
```

### Telegram не отправляет

1. Проверь что бот — админ канала
2. Проверь токен: `curl "https://api.telegram.org/bot{TOKEN}/getMe"`
3. Проверь channel_id: для публичных — `@username`, для приватных — числовой ID
