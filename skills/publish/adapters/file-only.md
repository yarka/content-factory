# File-Only Adapter

Простое сохранение статьи в папку. Без внешних сервисов.

## Требования

- Папка для output (по умолчанию `output/posts`)

## Workflow

```
┌────────────────────┐
│   Create output    │
│    directory       │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Save markdown     │
│   with metadata    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Confirm to user   │
└────────────────────┘
```

## Step 1: Create Directory

```bash
mkdir -p output/posts
```

Или путь из `config.yaml`:
```yaml
output:
  adapter: file-only
  output_dir: output/posts
```

## Step 2: Save File

Формат имени файла: `{date}-{slug}.md`

Пример: `2026-01-20-my-first-post.md`

Файл содержит:
1. Frontmatter (title, date, description, tags)
2. Полный текст статьи

## Step 3: Confirm

Сообщи пользователю:
- Путь к сохранённому файлу
- Размер в словах
- Напомни про git commit если нужно

## Пример

```
Статья сохранена: output/posts/2026-01-20-my-first-post.md
Размер: 847 слов

Следующие шаги:
- Проверь статью: cat output/posts/2026-01-20-my-first-post.md
- Закоммить: git add output/ && git commit -m "feat(blog): add my-first-post"
```
