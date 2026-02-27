# AI Content Factory

Персональная система создания аутентичного контента с AI.
Не AI-слоп. Твой голос — через умные инструменты.

```
Идея (1 мин) → Pipeline (10 мин) → Правки (5 мин) → Пост
```

Работает для Telegram и LinkedIn. Готовится: Threads.

---

## 🚀 Быстрый старт (для участников воркшопа)

### Что нужно заранее
- Аккаунт на [GitHub](https://github.com) — для форка репо
- Аккаунт на [claude.ai](https://claude.ai) (Pro) **или** [ChatGPT](https://chatgpt.com)
- [Claude Code](https://claude.ai/code) — если хочешь работать через терминал

### Шаг 1: Форкни этот репозиторий
Нажми **Fork** в правом верхнем углу → получишь копию в своём GitHub-аккаунте.

### Шаг 2: Клонируй к себе
```bash
git clone https://github.com/ТВОЙ_USERNAME/content-factory.git
cd content-factory
```

### Шаг 3: Открой в Claude Code
```bash
claude
```

### Шаг 4: Запусти настройку
```
запусти setup
```

Claude задаст 6 вопросов → заполнит `channel-dna.md` и `rules/writing-guide.md` под твой голос.

### Шаг 5: Напиши первый пост
```
хочу написать про [твоя идея]
```

Pipeline запустится сам.

---

> **Нет Claude Code?** Создай Project в [claude.ai](https://claude.ai) → загрузи файлы из папки `rules/` и оба `channel-dna*.md` → работай прямо в браузере.

> **Используешь ChatGPT?** Создай Project → загрузи те же файлы → используй те же триггеры.

---

## Что это

Контент-завод — это не "попроси ChatGPT написать пост".

Это система в три слоя:

**1. Channel DNA** — один раз описываешь голос, аудиторию, рубрики.
Система знает как ты пишешь. Не нужно объяснять каждый раз.

**2. Core Pipeline** — платформо-независимое ядро:
Questions → Research → Write → Fact-check → Deaify

**3. Адаптеры** — каждая платформа получает свою версию из одного черновика:

```
         Channel DNA
         Writing Guide
               │
               ▼
     ┌─────────────────────┐
     │    Core Pipeline    │
     │  Questions          │
     │  Research           │  ← Exa MCP или твои референсы
     │  Write              │  ← 3 варианта хука + черновик
     │  Fact-check         │  ← веб-поиск, флаги ✅⚠️❌
     │  Deaify             │  ← 4 параллельных критика
     └──────────┬──────────┘
                │
     ┌──────────▼──────────┐
     │   Выбор адаптера    │
     └──┬──────────────┬───┘
        │              │
        ▼              ▼
   Telegram        LinkedIn
   RU, HTML        EN, plain
   до 1500         600-1200
```

**Ядро одно. Адаптеры разные.**

---

## Как запустить

### Первый раз — настройка канала

```
"запусти setup"
```

Claude анализирует твой канал, задаёт 6 вопросов, заполняет `channel-dna.md` и `rules/writing-guide.md`.
После — система знает твой голос.

### Новая платформа — отдельный DNA

```
"настрой linkedin"
"настрой threads"
```

Для каждой платформы свой онбординг: цель, язык, аудитория, референсы, голос.
Создаёт `channel-dna-{platform}.md`.

### Написать пост

```
"хочу написать про X"
```

Pipeline запускается сам. Задаст максимум 3 вопроса, всё остальное сделает.

### Адаптировать под платформу

```
"в телеграм"
"в linkedin"
"в threads"
```

### Опубликовать в Telegram

```bash
# Тест
python3 publish.py --file output/posts/дата-slug.md

# Продакшн
python3 publish.py --file output/posts/дата-slug.md --env production
```

---

## Pipeline — детально

| Фаза | Что делает |
|------|------------|
| **Questions** | Уточняет идею, угол, контекст (макс. 3 вопроса) |
| **Research** | Авто-поиск через Exa MCP или читает твои референсы |
| **Write** | 3 варианта хука → выбираешь → пишет черновик в твоём голосе |
| **Fact-check** | Проверяет каждый факт, флагает ✅⚠️❌❓ |
| **Deaify** | 4 критика параллельно: клише, ритм, конкретность, факты |
| **Adapter** | Форматирует под платформу: HTML/plain, длина, тон |

---

## Адаптеры

### Telegram
- Язык: русский
- Формат: HTML (`<b>`, `<a href>`)
- Длина: 200–1500 символов
- Тире: только короткие (–)
- Публикация: `publish.py`

### LinkedIn
- Язык: английский
- Формат: plain text
- Длина: 600–1200 символов (ёмко, не растягивать)
- Без хэштегов, без эмодзи
- Мягкий CTA — вопрос или наблюдение
- Голос: 80% бизнес-инсайт, 20% личная история
- DNA: `channel-dna-linkedin.md`

### Threads (в разработке)
- Длина: до 500 символов
- Авто-выжимка из основного поста

---

## Файловая структура

```
├── CLAUDE.md                    # Главный вход — триггеры и инструкции
├── channel-dna.md               # DNA основного канала (Telegram)
├── channel-dna-linkedin.md      # DNA LinkedIn
├── publish.py                   # Публикация в Telegram (staging/production)
├── config/
│   └── config.yaml              # Токены (не в git)
├── output/
│   ├── posts/                   # Готовые черновики
│   └── analytics/               # Будущее: лог постов и паттерны
└── rules/
    ├── setup.md                 # Онбординг (канал + платформы)
    ├── core-pipeline.md         # Основной pipeline
    ├── fact-check.md            # Проверка фактов
    ├── deaify-text.md           # 4 критика + правило тире
    ├── writing-guide.md         # Голос и стиль автора
    └── adapters/
        ├── telegram.md          # Telegram адаптер
        ├── linkedin.md          # LinkedIn адаптер
        └── threads.md           # Threads адаптер (шаблон)
```

---

## Статус

| Компонент | Статус |
|-----------|--------|
| Telegram pipeline | ✅ Работает |
| LinkedIn DNA + адаптер | ✅ Настроен |
| Публикация в Telegram | ✅ Staging + Production |
| Onboarding (основной канал) | ✅ Работает |
| Platform Setup (новые платформы) | ✅ Работает |
| Threads адаптер | 🔧 Шаблон готов, API позже |
| Competitor Intelligence | 📋 В roadmap |
| Analytics Layer | 📋 В roadmap |

---

## Что дальше

**Threads API** — Meta Developer App, `auto_publish_text`, самообслуживание.

**LinkedIn API** — OAuth 2.0, ревью приложения 1-2 недели.

**Competitor Intelligence** — когда нет идей: сканирует что пишут авторы в нише, предлагает 5 углов.

**Analytics Layer** — логирует каждый пост, раз в месяц показывает паттерны: что заходит, какие хуки работают.

**Картинки** — обложки в едином стиле через DALL-E / Playwright.

**Карусели** — длинный пост → 5-7 карточек для LinkedIn и Threads.

→ Полный план: `ROADMAP.md`

---

## В основе

- [blog-pipeline-template](https://github.com/serejaris/blog-pipeline-template) by Серёжа Рис — скелет пайплайна
- Claude Code — среда выполнения
- Exa MCP — research и fact-check
- Telegram Bot API — публикация
