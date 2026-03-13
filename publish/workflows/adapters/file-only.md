# File-Only Adapter

Простое сохранение статьи в per-account workspace. Без внешних сервисов.

## Требования

- Папка для контент-артефактов (канонически `content/accounts/<account-slug>/posts/`)

## Workflow

```
┌────────────────────┐
│ Create artifact    │
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
mkdir -p content/accounts/<account-slug>/posts
```

Или путь из `config.yaml`:
```yaml
output:
  adapter: file-only
  output_dir: content/accounts/<account-slug>/posts
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
Статья сохранена: content/accounts/<account-slug>/posts/2026-01-20-my-first-post.md
Размер: 847 слов

Следующие шаги:
- git add content/accounts/<account-slug>/posts/ && git commit -m "feat(blog): add post"
```
