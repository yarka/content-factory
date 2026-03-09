# AI Content Factory

A personal AI pipeline for creating authentic content — not AI slop, but your voice through smart tools.

```
Idea → Pipeline → Draft → Publish
```

Works with Telegram and LinkedIn.

---

## System architecture

Four layers. Two are live, two are on the roadmap.

```
┌─────────────────────────────────────────┐
│  Intelligence Layer        [roadmap]    │
│  Scans trends, competitors, top posts   │
│  in your niche via Exa AI               │
└────────────────────┬────────────────────┘
                     ↓
┌────────────────────▼────────────────────┐
│  Strategy Layer            [live]       │
│  ICP → Offer → Content Pillars          │
│  → 30-day plan → Ongoing review         │
└────────────────────┬────────────────────┘
                     ↓
┌────────────────────▼────────────────────┐
│  Content Layer             [live]       │
│  Idea → Pipeline → Adapter → Publish    │
└────────────────────┬────────────────────┘
                     ↓
┌────────────────────▼────────────────────┐
│  Analytics Layer           [roadmap]    │
│  Tracks what hooks work, what topics    │
│  convert → feeds back into strategy     │
└─────────────────────────────────────────┘
```

**The key piece: Channel DNA.** One config file captures the company's voice, audience, tone, and format. Every agent reads this file first — that's how you scale without losing authenticity. Swap the file, you have a different brand.

---

## How it works

The Content Layer has three components:

**1. Channel DNA** — set up once. Your voice, audience, topics. The system learns how you write and never forgets.

**2. Core Pipeline** — platform-agnostic engine:
Questions → Research → Write → Fact-check → Deaify

**3. Adapters** — one draft, formatted for each platform:

```
     Channel DNA + Writing Guide
               │
               ▼
     ┌─────────────────────┐
     │    Core Pipeline    │
     │  Questions          │
     │  Research           │  ← Exa MCP or your references
     │  Write              │  ← 3 hook options + draft
     │  Fact-check         │  ← web search, flags ✅⚠️❌
     │  Deaify             │  ← 4 parallel critics
     └──────────┬──────────┘
                │
     ┌──────────▼──────────┐
     │   Choose adapter    │
     └──┬──────────────┬───┘
        │              │
        ▼              ▼
   Telegram        LinkedIn
   RU, HTML        EN, plain
   ≤1500 chars     600–1200 chars
```

One piece of truth → two platforms → two languages → different style for each.

The deaify step runs 4 parallel critics that strip AI fingerprints: generic phrases, rhythm problems, missing specifics, outdated facts.

---

## How setup works

Run `setup linkedin` — Claude asks you 6 questions and builds your DNA file:

| Step | Question |
|------|----------|
| 1. Goal | What are you building on LinkedIn — leads, reputation, network? |
| 2. Language | English / Russian / both? |
| 3. Audience | Who reads you there — role, company size, context? |
| 4. Voice | How do you want to sound — vs your main channel? |
| 5. References | Share 3–5 posts you like (not yours). What resonates? |
| 6. Format | Length, hashtags, emojis? |

Output: `channel-dna-linkedin.md` — stays local, never pushed to git.

---

## Quick start

**Requirements:** [Claude Code](https://claude.ai/code) · Git

```bash
git clone https://github.com/YOUR_USERNAME/content-factory.git
cd content-factory
claude
```

Then:
```
setup linkedin        → LinkedIn DNA setup (English)
запусти setup         → Main channel setup (Telegram)
```

Claude asks questions → fills your DNA → you're ready to write.

**No Claude Code?** Create a Project on [claude.ai](https://claude.ai) → upload all files from `rules/` → work in the browser.

---

## Triggers

| Say this | What happens |
|----------|--------------|
| `setup linkedin` | LinkedIn DNA setup |
| `запусти setup` | Main channel (Telegram) setup |
| `I want to write about X` | Full pipeline runs |
| `в телеграм` / `в linkedin` | Run specific adapter |
| `деаишь этот текст: ...` | Deaify only |

---

## Publishing to Telegram

Copy `config/config.example.yaml` → `config/config.yaml`, fill in your tokens:

```yaml
telegram:
  staging:
    bot_token: YOUR_BOT_TOKEN
    channel_id: YOUR_STAGING_CHANNEL_ID
  production:
    bot_token: YOUR_BOT_TOKEN
    channel_id: YOUR_PRODUCTION_CHANNEL_ID
```

```bash
python3 publish.py --env staging --file output/posts/YYYY-MM-DD-slug.md
python3 publish.py --env production --file output/posts/YYYY-MM-DD-slug.md
```

---

## File structure

```
├── channel-dna.md               # Your Telegram DNA (gitignored)
├── channel-dna-linkedin.md      # Your LinkedIn DNA (gitignored)
├── rules/
│   ├── setup.md                 # Onboarding flow
│   ├── core-pipeline.md         # Main pipeline
│   ├── writing-guide.md         # Your voice (gitignored)
│   ├── deaify-text.md           # 4 critics + anti-AI rules
│   └── adapters/
│       ├── telegram.md          # Telegram: HTML, RU, ≤1500 chars
│       └── linkedin.md          # LinkedIn: plain text, EN, 600–1200 chars
├── publish.py                   # Telegram publishing
└── output/posts/                # Ready drafts (gitignored)
```

**Personal files stay local.** Fork the repo → your DNA and drafts never leave your machine.
