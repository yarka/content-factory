# AI Content Factory

A personal AI pipeline for creating authentic content — not AI slop, but your voice through smart tools.

```
Idea → Pipeline → Draft → Publish
```

Works with Telegram and LinkedIn. Threads support in progress.

---

## How it works

Three layers:

**1. Channel DNA** — set up once. Describe your voice, audience, topics, share 10 posts you like. The system learns how you write and never forgets.

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

The deaify step runs 4 parallel critics that strip AI fingerprints: generic phrases, rhythm problems, missing specifics, outdated facts. Plus a web-search fact-check so nothing made up slips through.

---

## Quick start

### Requirements
- [Claude Code](https://claude.ai/code) (recommended) **or** [claude.ai](https://claude.ai) Pro
- Git + GitHub account

### Step 1: Fork this repo
Click **Fork** → get your own copy on GitHub.

### Step 2: Clone locally
```bash
git clone https://github.com/YOUR_USERNAME/content-factory.git
cd content-factory
```

### Step 3: Open in Claude Code
```bash
claude
```

### Step 4: Run setup
```
запусти setup
```

Claude asks 6 questions → fills `channel-dna.md` and `rules/writing-guide.md` with your voice.

### Step 5: Write your first post
```
I want to write about [your idea]
```

The pipeline runs automatically.

---

> **No Claude Code?** Create a Project on [claude.ai](https://claude.ai) → upload all files from the `rules/` folder + `channel-dna.template.md` → work directly in the browser. Rename the template to `channel-dna.md` and fill it in.

> **Using ChatGPT?** Same approach — create a Project, upload the same files, use the same triggers.

---

## Triggers

| Say this | What happens |
|----------|--------------|
| `запусти setup` | Onboarding — fills Channel DNA |
| `настрой linkedin` | LinkedIn DNA setup |
| `I want to write about X` | Full pipeline runs |
| `в телеграм` / `в linkedin` | Run specific adapter |
| `деаишь этот текст: ...` | Deaify only |

---

## Publishing to Telegram

Setup `config/config.yaml` (copy from `config/config.example.yaml`):

```yaml
telegram:
  staging:
    bot_token: YOUR_BOT_TOKEN
    channel_id: YOUR_STAGING_CHANNEL_ID
  production:
    bot_token: YOUR_BOT_TOKEN
    channel_id: YOUR_PRODUCTION_CHANNEL_ID
```

Then publish:
```bash
# Staging
python3 publish.py --env staging --file output/posts/YYYY-MM-DD-slug.md

# Production
python3 publish.py --env production --file output/posts/YYYY-MM-DD-slug.md
```

---

## File structure

```
├── CLAUDE.md                    # Entry point — triggers and instructions
├── channel-dna.template.md      # Template → copy to channel-dna.md and fill in
├── channel-dna.md               # Your channel DNA (gitignored — stays local)
├── channel-dna-linkedin.md      # LinkedIn DNA (gitignored — stays local)
├── publish.py                   # Telegram publishing (staging/production)
├── config/
│   ├── config.example.yaml      # Config template
│   └── config.yaml              # Your tokens (gitignored — stays local)
├── output/
│   └── posts/                   # Ready drafts (gitignored — stays local)
└── rules/
    ├── setup.md                 # Onboarding flow
    ├── core-pipeline.md         # Main pipeline
    ├── writing-guide.md         # Your voice and style (gitignored — stays local)
    ├── fact-check.md            # Fact verification rules
    ├── deaify-text.md           # 4 critics + anti-AI rules
    └── adapters/
        ├── telegram.md          # Telegram: HTML, RU, ≤1500 chars
        ├── linkedin.md          # LinkedIn: plain text, EN, 600–1200 chars
        └── threads.md           # Threads: plain text, ≤500 chars
```

**Personal files stay local.** The `.gitignore` excludes `channel-dna.md`, `writing-guide.md`, `config.yaml`, and all posts. Fork the repo → your DNA and drafts never leave your machine.

---

## Status

| Component | Status |
|-----------|--------|
| Telegram pipeline | ✅ Working |
| LinkedIn DNA + adapter | ✅ Working |
| Telegram publishing | ✅ Staging + Production |
| Onboarding (main channel) | ✅ Working |
| Platform Setup (LinkedIn, Threads) | ✅ Working |
| Threads adapter | 🔧 Template ready, API later |
| LinkedIn auto-publish | 📋 Roadmap |
| Analytics layer | 📋 Roadmap |

---

## Roadmap

**Threads API** — Meta Developer App, `auto_publish_text`.

**LinkedIn API** — OAuth 2.0, app review 1-2 weeks.

**Competitor Intelligence** — when stuck for ideas: scans what others in the niche are writing, suggests 5 angles.

**Analytics Layer** — logs every post, monthly report: what performs, which hooks work.

**Visuals** — cover images in consistent style via DALL-E / Playwright.

→ Full plan: `ROADMAP.md`

---

## Credits

- [content-factory](https://github.com/serejaris/content-factory) by Sereja Ris — original skeleton
- [Claude Code](https://claude.ai/code) — runtime
- [Exa MCP](https://exa.ai) — research and fact-check
- Telegram Bot API — publishing
