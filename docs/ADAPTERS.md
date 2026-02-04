# Написание адаптеров

Как создать свой adapter для публикации.

## Архитектура

```
skills/publish/
├── skill.md            ← Router (читает config, выбирает adapter)
└── adapters/
    ├── telegram.md     ← Adapter 1
    ├── file-only.md    ← Adapter 2
    ├── custom.md       ← Шаблон
    └── your-adapter.md ← Твой adapter
```

Router читает `output.adapter` из конфига и загружает соответствующий файл.

## Структура адаптера

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
  ...
```

## Workflow

```
Диаграмма шагов
```

## Step 1: {Action}

Инструкции для агента.

## Step 2: {Action}

...

## Checklist

- [ ] Validation 1
- [ ] Validation 2
```

## Примеры

### Ghost CMS

```markdown
# Ghost Adapter

Публикация в Ghost CMS.

## Требования

- Ghost Admin API key
- Ghost URL

## Config

```yaml
ghost:
  url: https://blog.example.com
  admin_key: ${GHOST_ADMIN_KEY}
```

## Workflow

1. Конвертировать markdown в mobiledoc
2. POST к Ghost Admin API
3. Вернуть URL опубликованного поста

## Step 1: Convert to Mobiledoc

Ghost использует mobiledoc формат. Простейший вариант — card с markdown:

```json
{
  "version": "0.3.1",
  "markups": [],
  "atoms": [],
  "cards": [["markdown", {"markdown": "...content..."}]],
  "sections": [[10, 0]]
}
```

## Step 2: Create Post

```python
import jwt
import requests

def create_ghost_post(url, admin_key, title, content, status="draft"):
    id, secret = admin_key.split(":")

    token = jwt.encode(
        {"iat": int(time.time()), "exp": int(time.time()) + 300, "aud": "/admin/"},
        bytes.fromhex(secret),
        algorithm="HS256",
        headers={"kid": id}
    )

    mobiledoc = {
        "version": "0.3.1",
        "markups": [],
        "atoms": [],
        "cards": [["markdown", {"markdown": content}]],
        "sections": [[10, 0]]
    }

    response = requests.post(
        f"{url}/ghost/api/admin/posts/",
        headers={"Authorization": f"Ghost {token}"},
        json={"posts": [{"title": title, "mobiledoc": json.dumps(mobiledoc), "status": status}]}
    )

    return response.json()["posts"][0]["url"]
```

## Checklist

- [ ] Admin key настроен
- [ ] URL доступен
- [ ] Статус: draft или publish
```

### Notion

```markdown
# Notion Adapter

Создание страницы в Notion database.

## Требования

- Notion integration token
- Database ID с нужными properties

## Config

```yaml
notion:
  token: ${NOTION_TOKEN}
  database_id: "abc123..."
```

## Workflow

1. Конвертировать markdown в Notion blocks
2. Создать страницу через API
3. Вернуть URL страницы

## Step 1: Convert to Blocks

Notion API принимает blocks, не markdown. Используй библиотеку или конвертируй вручную:

```python
def markdown_to_notion_blocks(md_content):
    blocks = []
    for line in md_content.split("\n"):
        if line.startswith("# "):
            blocks.append({"type": "heading_1", "heading_1": {"rich_text": [{"text": {"content": line[2:]}}]}})
        elif line.startswith("## "):
            blocks.append({"type": "heading_2", "heading_2": {"rich_text": [{"text": {"content": line[3:]}}]}})
        else:
            blocks.append({"type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": line}}]}})
    return blocks
```

## Step 2: Create Page

```python
import requests

def create_notion_page(token, database_id, title, blocks):
    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        },
        json={
            "parent": {"database_id": database_id},
            "properties": {"Name": {"title": [{"text": {"content": title}}]}},
            "children": blocks
        }
    )
    return response.json()["url"]
```

## Checklist

- [ ] Integration добавлена к database
- [ ] Database имеет property "Name" (title)
```

### Medium

```markdown
# Medium Adapter

Публикация на Medium через API.

## Требования

- Medium integration token
- Publication ID (опционально)

## Config

```yaml
medium:
  token: ${MEDIUM_TOKEN}
  publication_id: "optional"  # для публикации в publication
```

## Step 1: Get User ID

```python
response = requests.get(
    "https://api.medium.com/v1/me",
    headers={"Authorization": f"Bearer {token}"}
)
user_id = response.json()["data"]["id"]
```

## Step 2: Create Post

```python
response = requests.post(
    f"https://api.medium.com/v1/users/{user_id}/posts",
    headers={"Authorization": f"Bearer {token}"},
    json={
        "title": title,
        "contentFormat": "markdown",
        "content": content,
        "publishStatus": "draft"  # или "public"
    }
)
return response.json()["data"]["url"]
```
```

## Регистрация

После создания файла `adapters/your-adapter.md`:

```yaml
output:
  adapter: your-adapter
```

Router автоматически найдёт и загрузит твой adapter.

## Best Practices

1. **Validation** — проверяй конфиг перед использованием
2. **Errors** — обрабатывай ошибки API, показывай понятные сообщения
3. **Secrets** — используй `${ENV_VAR}` вместо hardcoded токенов
4. **Draft first** — по умолчанию создавай draft, не publish
5. **Return URL** — всегда возвращай URL созданного контента
