---
description: Core pipeline — от идеи до готового черновика. Платформо-независимый.
globs:
  - "**/*.md"
---

# Core Pipeline

Ядро контент-завода. Производит core draft в авторском голосе.
Платформа не важна на этом этапе — только идея и голос.

## Phase 0: Strategy Brief Handoff

Если пользователь приходит не с сырой идеей, а с готовым артефактом из strategy layer:

- Прочитай selected strategy post brief из `strategy/accounts/<account-slug>/content-plan.yaml`
- Прочитай image brief для этого поста
- Прочитай approved strategy constraints из того же brief
- Прочитай supporting evidence из `intelligence/accounts/<account-slug>/intelligence-snapshot.yaml`

В этом режиме:
- не придумывай заново стратегию поста
- используй brief как source of truth для угла, proof asset и soft CTA
- задавай только вопросы на заполнение пробелов, если не хватает фактов или деталей сцены

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Phase 1:   │ ──▶ │  Phase 2:   │ ──▶ │  Phase 3:   │
│  Questions  │     │  Research   │     │  Write      │
└─────────────┘     └─────────────┘     └─────────────┘
                                              │
          ┌─────────────┐                     │
          │  Phase 4:   │ ◀───────────────────┘
          │  Fact-check │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │  Phase 5:   │
          │   Deaify    │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐     ┌─────────────┐
          │  Core Draft │ ──▶ │  Adapter    │
          │   готов     │     │  (выбрать)  │
          └─────────────┘     └─────────────┘
```

**Всегда читай `content/channel-dna.md` перед запуском.**

## Workflow Mode

Read `config/config.yaml` when available and check `content.workflow_mode`.

Allowed modes:
- `human_in_the_loop`
- `fully_automatic`

Default to `human_in_the_loop` when the config is missing.

If `human_in_the_loop` is enabled:
- do a Depth Check before hooks when the idea is still forming
- ask for the author's angle, concrete example, or proof asset when those are missing
- prefer short checkpoints over guessing

If `fully_automatic` is enabled:
- ask only when a factual gap would make the draft misleading
- otherwise synthesize from the brief, research, and saved context directly

---

## Phase 1: Questions

Получи идею. Задай максимум 3 уточняющих вопроса.

**Всегда:**
1. **Угол** — что конкретно хочешь сказать? какая мысль?
2. **Контекст** — личный опыт? инсайт? реакция на что-то?

**Если нужно:**
3. **Платформа** — куда публикуем? (Telegram / LinkedIn / Threads / все)

Если работаешь из strategy brief:
- не спрашивай угол заново, возьми его из brief
- сфокусируй вопросы на missing specifics: цифры, сцена, доказательства, фактические детали

Если платформа не указана — спроси. Это нужно для адаптера на выходе.

Если `human_in_the_loop` включён:
- не перескакивай сразу к хукам, если мысль ещё сырая
- сначала помоги автору докрутить angle, proof и сцену
- веди процесс как editor, а не как blind generator

---

### Depth Check (перед заголовком)

Если идея пришла как голосовой поток, набросок или мысль не до конца оформлена — задай до 3 уточняющих вопросов перед тем как генерировать заголовки:

**Триггеры для Depth Check:**
- Идея — поток мыслей без чёткого вывода
- Несколько тем смешаны в одном сообщении
- Есть событие, но не понятно зачем это читателю

**Вопросы (выбери те что нужны, не все сразу):**
- **Вывод:** "Если бы пост был одним предложением — что бы это было?"
- **Деталь:** "Есть конкретный момент, реплика или сцена которую точно хочешь в посте?"
- **Ощущение:** "Что читатель должен почувствовать после? 'Я не один' / 'хочу попробовать' / 'задумался'?"

⛔ СТОП. Не генерируй заголовки пока не получил ответы.

Если `fully_automatic` включён и brief already has:
- clear angle
- proof asset
- supporting evidence

то Depth Check можно пропустить.

---

## Phase 2: Research

Сразу спроси:
> "Есть материалы/ссылки по теме или ищем сами?"

### Режим A: Авто-поиск
```
Найди контекст для поста на тему: {тема}

1. Web search: 2-3 источника (факты, цифры, кейсы)
2. Один конкретный пример или историю
3. Проверь актуальность (текущий год)

Верни: 3-5 ключевых фактов с источниками. НЕ черновик.
```

### Режим B: Референсы
```
Прочитай предоставленные материалы.
Извлеки: ключевые факты, цитаты, нераскрытый угол.
НЕ черновик — только сырьё.
```

### Режим C: Из головы
Личный опыт без внешних фактов → пропусти research,
спроси конкретные детали: что произошло, цифры, вывод.

### Режим D: Strategy Evidence
Если post brief уже выбран:
- используй supporting evidence из intelligence snapshot как research baseline
- добирай только недостающие факты
- сохрани approved strategy constraints и image brief в контексте до конца пайплайна

---

## Phase 3: Write — Core Draft

### Шаг 3.1: Заголовок (3 варианта)

```
Придумай 3 варианта заголовка.

Типы (`content/writing-guide.md`):
- Zinger: короткий удар ("Кодер выживет. Менеджер — нет.")
- First-Person: личный ("Мой запасной план — делать массаж.")
- Question: вопрос-боль ("Если завтра без работы — чем займёшься?")
- Scene: картинка момента

Правила: макс. 8 слов, без точки в конце, интригует — не объясняет.

Покажи 3 варианта и спроси: "Какой берём? Или предложи свой."

⛔ СТОП. Не пиши черновик пока не получил ответ с выбором заголовка.
```

### Шаг 3.2: Core Draft

```
Напиши core draft.

Заголовок: {выбранный}
Контекст: {Phase 1}
Сырьё: {Phase 2}

Читай: `content/channel-dna.md` + `content/writing-guide.md`

ПРАВИЛА CORE DRAFT:
- Язык: русский (адаптер сам переведёт если нужно)
- Длина: сколько нужно идее — не думай про платформу
- Структура: Заголовок → Тело → Финал
- Тон: голос автора из `content/writing-guide.md`
- Включи все детали, факты, личные моменты — адаптер уберёт лишнее

Верни ТОЛЬКО текст. Без комментариев.
```

---

## Phase 4: Fact-check

Прочитай `content/workflows/fact-check.md`.

Если пост содержит внешние факты — проверь через Exa MCP или WebFetch.
Если личная история / мнение — напиши "Fact-check: пропущен" и иди дальше.

---

## Phase 5: Deaify

Прочитай `content/workflows/deaify-text.md`. Прогони core draft через 4 критиков.

После deaify → **Core Draft готов**.

## Phase 5.5: Quality Report

После черновика не молчи о качестве.

Всегда коротко сообщай:
- был ли `fact-check`
- был ли `deaify`
- what changed after critic pass
- остались ли сомнения или слабые места

Формат короткий:
- `Fact-check: ...`
- `Deaify: ...`
- `What changed: ...`

Даже если правок мало, дай пользователю явный сигнал, что текст прошёл quality pass.

---

## Phase 6: Выбор адаптера

Спроси если платформа ещё не выбрана:
> "Для какой площадки готовим? Telegram / LinkedIn / Threads / все три?"

Запусти нужный адаптер из `content/workflows/adapters/`:

| Платформа | Файл | Язык | Формат |
|-----------|------|------|--------|
| Telegram | `content/workflows/adapters/telegram.md` | RU | HTML, до 1500 символов |
| LinkedIn | `content/workflows/adapters/linkedin.md` | EN | plain text, до 3000 символов |
| Threads | `content/workflows/adapters/threads.md` | RU/EN | plain text, до 500 символов |

Если выбраны несколько — запусти адаптеры последовательно.

---

## Phase 7: Save

After the user approves the final post — save it automatically to `content/accounts/<account-slug>/posts/YYYY-MM-DD-slug.md`.

Use the active pilot account slug when the post came from strategy/orchestrator.
If the account slug is still unknown, ask once before saving.

Do not ask for save confirmation. Just save and confirm: "Saved to content/accounts/<account-slug>/posts/YYYY-MM-DD-slug.md"

Slug: short English kebab-case summary of the topic (e.g. `founders-competitor-agent-linkedin`).

## Phase 8: Proactive Next Step

After save, do not stop passively.

Recommend the next best action in this order:
1. generate/refine LinkedIn visual
2. review final text once with visual context
3. publish

Return:
- saved path
- recommended next step
- why this is the best move now
- 1-3 concrete options the user can take immediately

---

## Checklist

- [ ] content/channel-dna.md прочитан
- [ ] Phase 1: идея + угол + платформа
- [ ] Phase 2: режим выбран, сырьё собрано
- [ ] Phase 3.1: заголовок выбран
- [ ] Phase 3.2: core draft написан
- [ ] Phase 4: fact-check пройден
- [ ] Phase 5: deaify пройден
- [ ] Phase 5.5: quality report показан пользователю
- [ ] Phase 6: адаптер запущен
- [ ] Phase 7: сохранён в content/accounts/<account-slug>/posts/
- [ ] Phase 8: рекомендован следующий шаг
