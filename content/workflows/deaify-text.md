---
description: Remove AI fingerprints from text using 4 parallel critics
globs:
  - "**/*.md"
---

# De-AI-fy Text

Убирает AI-отпечатки из текста через параллельных критиков и итеративное переписывание.

## When to Use

- Текст "звучит как AI написал"
- Ровный ритм, предсказуемая структура
- Шаблонные фразы без конкретики
- Нет авторского голоса
- Технический контент с версиями, датами (нужна проверка фактов)

## Visual Output Format

When running critics, output this block BEFORE showing results:

```
◆ Agent 1: AI Pattern Detector  — running...
◆ Agent 2: Rhythm Analyzer      — running...
◆ Agent 3: Specificity Checker  — running...
◆ Agent 4: Fact Checker         — running...

✓ Agent 1: AI Pattern Detector  — done
✓ Agent 2: Rhythm Analyzer      — done
✓ Agent 3: Specificity Checker  — done
✓ Agent 4: Fact Checker         — done
```

Then show Results block:

```
─────────────
  Results
─────────────
  ✗ Agent 1: AI Pattern Detector — 3 issue(s) found
       → "exact flagged phrase"
  ✓ Agent 2: Rhythm Analyzer     — clean
  ✗ Agent 3: Specificity Checker — 2 issue(s) found
       → "no personal voice"
       → "no concrete examples"
  ✓ Agent 4: Fact Checker        — clean

  ⚠️  5 issue(s) flagged. Rewriting...
─────────────
```

Then proceed with the rewrite.

---

## Core Pattern

```
┌──────────────┐
│  Read text   │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────────────────────────┐
│           Launch 4 PARALLEL critics              │
├────────────┬────────────┬────────────┬───────────┤
│ Critic A   │ Critic B   │ Critic C   │ Critic D  │
│ Generic    │ Rhythm     │ Missing    │ Fact      │
│ phrases    │ problems   │ specifics  │ checker   │
└─────┬──────┴─────┬──────┴─────┬──────┴─────┬─────┘
      │            │            │            │
      │            │            │            ▼
      │            │            │    Web verify flagged
      │            │            │            │
      ▼            ▼            ▼            ▼
┌──────────────────────────────────────────────────┐
│              Aggregate critiques                 │
└──────────────────────┬───────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────┐
│           Rewrite with constraints               │
└──────────────────────┬───────────────────────────┘
                       │
                       ▼
              Shorter or same length?
                 │           │
               yes          no
                 │           │
                 ▼           ▼
              Done       Cut bloat → Done
```

---

## Critic Prompts

**Запусти все 4 критика параллельно** (в отдельных чатах/subagents или последовательно если параллельность недоступна):

### Critic A — Generic Detector

```
Find AI-typical phrases in this text:
- "важно понимать", "следует отметить", "в заключение"
- "Это не X — это Y" dramatic contrasts as conclusions
- "Если не разбираешься в X" — generic audience segmentation
- "не магия, система" / "не инструмент, подход" — empty slogans
- Generic future claims: "будущее за X", "скоро всё изменится" — without personal angle
- "Это не мотивашка" / "Это не совет — это наблюдение" — meta-disclaimer, никто так не говорит
- "N часов в неделю — не X, а Y" — productivity-tip формат, звучит как лайфхак-канал
- Sentences without specific names/numbers/dates
- Abstract claims without examples

Output: numbered list with exact quotes and line references.
```

### Critic B — Rhythm Analyzer

```
Analyze text rhythm:
- Find 3+ consecutive sentences of similar length
- Find paragraphs where all sentences start similarly
- Check burstiness: ratio of shortest to longest sentence

EXCEPTION: Do NOT flag sequential/step lists.
These help readers scan. Only flag lists where structure adds no value.

Output: specific locations that need rhythm variation.
```

### Critic C — Specificity Checker

```
Where could author add:
- Personal experience ("I tried this and...")
- Specific number or statistic
- Name/company/date reference
- Opinion marker ("я думаю", "по-моему")

Output: 3-5 specific suggestions with WHERE to insert.
```

### Critic D — Fact Checker

```
Extract all verifiable claims from this text:
- Software/model versions (GPT-4, Claude 3, Gemini 2.0)
- Release dates and timelines
- Company names, product names, tool names
- Statistics, percentages, numbers

For each claim, flag if:
- Model/version might be outdated (AI models older than 6 months)
- Date doesn't match current year context
- Tool/product might be deprecated or renamed
- Statistic seems made up (round numbers, no source)

Output: numbered list of claims that need web verification.
Format: "[CLAIM]: {exact quote}" + "[FLAG]: {why suspicious}"
```

---

## Fact Verification Step

**После Critic D — проверь каждый flagged claim через web search:**

```
Для каждого claim:
  Web search: "{product/model name} latest version 2026"

  Сравни claim с результатами.
  Если устарело: предоставь актуальное значение.
```

---

## Rewriter Constraints

После агрегации критик, перепиши с HARD RULES:

1. **Length cap:** Output ≤ original word count
2. **Vary sentence length:** Mix 3-word and 20-word sentences
3. **Kill generic phrases:** Replace every flagged phrase
4. **Add ONE personal touch:** "Я видел как...", "Помню когда..."
5. **Break one grammar rule:** Start with "И" or "Но", use fragment
6. **Тире:** заменить все длинные тире (—) на короткие (–). Всегда, без исключений.

---

## What to PRESERVE

- **Sequential/step lists** — "Как это работает", numbered workflows
- **Code examples** — don't touch
- **Technical specs** — configs, commands, file paths
- **Comparisons** — if author compares alternatives, keep structure

**Rule:** If a list helps reader skip prose and get the gist — keep it.

---

## Anti-Patterns

| Don't | Why |
|-------|-----|
| Expand text | AI loves adding "context" — resist |
| Add drama endings | "И это меняет всё." = AI fingerprint |
| Delete useful lists | Sequential steps help scanning |
| Rewrite intro last | Intro sets human tone — do first |

---

## Red Flags — You're Adding AI

- Output longer than input
- "Но факт в том, что..."
- "И вот почему это важно"
- All paragraphs same length
- Ending with rhetorical question
- "Если не разбираешься в X — начни с Y" (patronizing segmentation)
- "X – это не подписка. Это инструмент." (dramatic contrast as punchline)
- "будущее за теми кто..." (generic prophecy)
- Any slogan that sounds good but says nothing specific

---

## Quick Reference

| AI Pattern | Human Fix |
|------------|-----------|
| Even paragraphs | 1 sentence, then 5, then 2 |
| "Важно отметить" | Delete or replace with specific |
| No dates/names | Add one real reference |
| Abstract claim | Add "например" with concrete case |
| Drama ending | Cut last sentence, end earlier |
| "Если не разбираешься" | Cut or replace with what YOU did instead |
| "X – это не Y. Это Z." | Show, don't declare. Add concrete example |
| "будущее за X" without personal | "Я ставлю на X потому что..." |
| Empty slogan ("не магия, система") | Replace with the actual mechanic or cut |

---

## Personal touch examples

- ✅ "Я сам перестал заходить на tailwindcss.com"
- ✅ "По-моему, первый вариант самый реальный"
- ❌ "Многие эксперты считают" (generic)
- ❌ "Это важно для индустрии" (abstract)
