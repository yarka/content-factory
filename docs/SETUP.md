# Установка

## Требования

- Claude Code (или другой AI-агент с поддержкой skills)
- Git

## Шаг 1: Создай репозиторий

```bash
# Через GitHub CLI
gh repo create my-blog-pipeline --template sereja-ris/blog-pipeline-template
cd my-blog-pipeline

# Или вручную
git clone https://github.com/sereja-ris/blog-pipeline-template my-blog-pipeline
cd my-blog-pipeline
rm -rf .git && git init
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

## Шаг 3: Для Telegram (опционально)

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

**Секреты:** Используй переменные окружения вместо токенов в файле:

```yaml
bot_token: ${TELEGRAM_BOT_TOKEN}
```

```bash
export TELEGRAM_BOT_TOKEN="your-token"
```

## Шаг 4: Проверь работу

В Claude Code:

```
напиши статью про автоматизацию публикаций
```

Агент должен:
1. Задать уточняющие вопросы
2. Провести research
3. Написать черновик
4. Прогнать через деаификацию
5. Сохранить/опубликовать через выбранный adapter

## Структура папок после установки

```
my-blog-pipeline/
├── config/
│   ├── config.example.yaml
│   └── config.yaml          ← твой конфиг (gitignored)
├── output/
│   └── posts/               ← сюда сохраняются статьи
├── skills/
│   └── ...
└── CLAUDE.md                ← symlink на skill.md
```

## Troubleshooting

### Skill не находится

Проверь что `CLAUDE.md` в корне репозитория:

```bash
ls -la CLAUDE.md
# Должен быть symlink на skills/blog-post/skill.md
```

### Telegram не отправляет

1. Проверь что бот — админ канала
2. Проверь токен: `curl "https://api.telegram.org/bot{TOKEN}/getMe"`
3. Проверь channel_id: для публичных — `@username`, для приватных — числовой ID

### Config не читается

```bash
# Проверь YAML синтаксис
python3 -c "import yaml; yaml.safe_load(open('config/config.yaml'))"
```
