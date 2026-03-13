# Кастомизация

Как адаптировать pipeline под себя.

## Изменение стиля

### Writing Guide

Отредактируй `skills/blog-post/writing-guide.md`:

```markdown
## Author Voice

**Тон:**
- Твой стиль здесь
- ...
```

### Хуки и формулы

В том же файле — секции про хуки, ритм, intro.

### Терминология

Для английского контента — удали или замени `ai-terms-ru.md`.

## Изменение требований

### Длина статьи

В `config/config.yaml`:

```yaml
content:
  min_words: 800  # было 600
```

И в `skills/blog-post/skill.md` — обнови Phase 3 prompt.

### ASCII диаграммы

Отключить требование:

```yaml
content:
  require_diagram: false
```

### SEO лимиты

```yaml
seo:
  max_title_length: 70
  max_description_length: 200
```

## Добавление фаз

### Пример: Review фаза

Создай `skills/review/skill.md`:

```markdown
---
name: review
description: Ревью статьи перед публикацией
---

# Review

Чеклист перед публикацией:

1. Факты проверены
2. Ссылки работают
3. SEO в норме
...
```

Добавь в workflow `blog-post/skill.md`:

```
Phase 4: Deaify → Phase 4.5: Review → Phase 5: Publish
```

## Изменение деаификации

### Добавить критика

В `skills/deaify-text/skill.md` добавь Critic E:

```markdown
### Critic E — {Your Critic}
```
Find {specific patterns} in this text:
- Pattern 1
- Pattern 2

Output: numbered list with exact quotes.
```

И обнови diagram + "Launch ALL FIVE in parallel".

### Убрать критика

Удали соответствующий блок и обнови параллельный запуск.

## Локализация

### Перевод на английский

1. Переведи `writing-guide.md`
2. Удали или замени `ai-terms-ru.md`
3. Обнови промпты в `skill.md` — убери русские примеры
4. В `deaify-text/skill.md` замени русские AI-паттерны на английские:
   - "важно понимать" → "it's important to understand"
   - "следует отметить" → "it should be noted"

### Другой язык

Создай свой `ai-terms-{lang}.md` с терминологией.

## Интеграция с блог-платформой

### Hugo

В `config.yaml`:

```yaml
blog:
  base_url: https://your-site.com
  post_pattern: /blog/{slug}
  content_dir: content/blog  # куда сохранять
```

Обнови `file-only.md` adapter чтобы сохранял в `content_dir`.

### Jekyll

```yaml
blog:
  content_dir: _posts
  post_pattern: /{year}/{month}/{slug}
```

Формат имени файла: `{date}-{slug}.md`

### Другие SSG

Адаптируй под свою структуру — главное чтобы frontmatter совпадал.

## Git workflow

### Auto-commit после публикации

Добавь в `file-only.md` или создай `git-commit.md` adapter:

```markdown
## After Save

```bash
git add content/accounts/<account-slug>/posts/{slug}.md
git commit -m "feat(blog): add {title}"
git push
```
```

### Branch strategy

Создавай PR для каждой статьи:

```bash
git checkout -b post/{slug}
# ... generate post ...
git push -u origin post/{slug}
gh pr create --title "feat(blog): {title}"
```
