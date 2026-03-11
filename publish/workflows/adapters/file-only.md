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

Формат имени: `{date}-{slug}.md`

Пример: `2026-01-20-my-first-post.md`

Файл содержит:
1. Frontmatter (title, date, description, tags)
2. Полный текст статьи

## Step 3: Confirm

Сообщи пользователю:
- Путь к файлу
- Размер в словах
- Следующие шаги (git commit если нужно)

## Пример вывода

```
Статья сохранена: output/posts/2026-01-20-my-first-post.md
Размер: 847 слов

Следующие шаги:
- git add output/ && git commit -m "feat(blog): add post"
```
