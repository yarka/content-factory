# Blog Post Pipeline

Модульный pipeline для написания статей через AI-агентов.

```
Questions → Research → Write → Deaify → Publish
```

## Skills

| Skill | File | Trigger |
|-------|------|---------|
| **blog-post** | `rules/blog-post.md` | "напиши статью", "блог", "пост" |
| **deaify-text** | `rules/deaify-text.md` | "убери аишность", "деаишь", "humanize" |
| **publish** | `rules/publish/publish.md` | "опубликуй", "publish" |

## Quick Start

Для написания статьи прочитай `rules/blog-post.md` и следуй 5-фазному workflow:

1. **Questions** — угол, аудитория, takeaway
2. **Research** — web search, 3+ источников
3. **Write** — черновик 600+ слов
4. **Deaify** — 4 критика убирают AI-отпечатки
5. **Publish** — adapter из config

## Supporting Files

| File | Purpose |
|------|---------|
| `rules/writing-guide.md` | Стиль, хуки, ритм |
| `rules/ai-terms-ru.md` | AI терминология на русском |
| `rules/publish/adapters/` | Telegram, file-only, custom |
| `config/config.yaml` | Настройки output adapter |

## Config

Скопируй `config/config.example.yaml` → `config/config.yaml`:

```yaml
output:
  adapter: file-only  # telegram | file-only | custom
  output_dir: output/posts
```

## Reference

- [Статья о пайплайне](https://sereja.tech/blog/blog-post-pipeline)
- [AGENTS.md standard](https://agents.md)
