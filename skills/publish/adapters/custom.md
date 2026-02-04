# Custom Adapter Template

Шаблон для создания собственного adapter.

## Структура

Создай файл `skills/publish/adapters/{your-adapter}.md` со следующей структурой:

```markdown
# {Adapter Name}

Описание что делает adapter.

## Требования

- Что нужно для работы
- API ключи, токены
- Внешние сервисы

## Workflow

```
Диаграмма шагов
```

## Step 1: {First Step}

Инструкции для агента.

## Step 2: {Second Step}

...

## Checklist

- [ ] Валидация 1
- [ ] Валидация 2
```

## Примеры адаптеров

### Ghost CMS

```markdown
# Ghost Adapter

Публикация в Ghost CMS через Admin API.

## Требования

- Ghost instance URL
- Admin API key

## Config

```yaml
ghost:
  url: https://your-blog.ghost.io
  admin_key: ${GHOST_ADMIN_KEY}
```

## Workflow

1. Конвертировать markdown в mobiledoc формат
2. POST /ghost/api/admin/posts/
3. Опционально: schedule публикации
```

### Notion

```markdown
# Notion Adapter

Создание страницы в Notion database.

## Требования

- Notion integration token
- Database ID

## Config

```yaml
notion:
  token: ${NOTION_TOKEN}
  database_id: "abc123..."
```

## Workflow

1. Конвертировать markdown в Notion blocks
2. POST /v1/pages
3. Добавить properties (title, date, tags)
```

### WordPress

```markdown
# WordPress Adapter

Публикация через WordPress REST API.

## Требования

- WordPress site URL
- Application password

## Config

```yaml
wordpress:
  url: https://your-site.com
  username: admin
  app_password: ${WP_APP_PASSWORD}
```

## Workflow

1. Конвертировать markdown в HTML
2. POST /wp-json/wp/v2/posts
3. Установить status: draft или publish
```

## Регистрация адаптера

После создания файла, добавь в `config/config.yaml`:

```yaml
output:
  adapter: your-adapter  # имя файла без .md
```

Router автоматически найдёт и загрузит `adapters/your-adapter.md`.
