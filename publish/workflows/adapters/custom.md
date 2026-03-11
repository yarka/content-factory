# Custom Adapter Template

Шаблон для создания собственного adapter.

## Структура

Создай файл `publish/workflows/adapters/{your-adapter}.md`:

```markdown
# {Adapter Name}

Описание.

## Требования

- Что нужно для работы
- API ключи, токены

## Config

```yaml
your_adapter:
  api_key: ${YOUR_API_KEY}
```

## Workflow

(диаграмма шагов)

## Step 1: {Action}

Инструкции.

## Step 2: {Action}

...

## Checklist

- [ ] Validation 1
- [ ] Validation 2
```

## Примеры

### Ghost CMS

```yaml
ghost:
  url: https://blog.example.com
  admin_key: ${GHOST_ADMIN_KEY}
```

1. Конвертировать markdown в mobiledoc
2. POST к Ghost Admin API
3. Вернуть URL

### Notion

```yaml
notion:
  token: ${NOTION_TOKEN}
  database_id: "abc123..."
```

1. Конвертировать markdown в Notion blocks
2. POST /v1/pages
3. Вернуть URL страницы

### WordPress

```yaml
wordpress:
  url: https://your-site.com
  username: admin
  app_password: ${WP_APP_PASSWORD}
```

1. Конвертировать markdown в HTML
2. POST /wp-json/wp/v2/posts
3. Установить status: draft или publish

## Регистрация

После создания файла, добавь в `config/config.yaml`:

```yaml
output:
  adapter: your-adapter
```

Router найдёт `adapters/your-adapter.md`.
