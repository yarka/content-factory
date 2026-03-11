# AI Content Factory

A modular AI content system for turning business context into publishable content without losing voice.

```
Setup -> Intelligence -> Strategy -> Content -> Publish
```

Works with Telegram and LinkedIn today. The repo is organized by module, not by a flat rule dump.

## Architecture

```
┌─────────────────────────────────────────┐
│  Setup Layer             [live]         │
│  Bootstrap DNA and local workspaces     │
└────────────────────┬────────────────────┘
                     ↓
┌────────────────────▼────────────────────┐
│  Intelligence Module     [live]         │
│  Discovery -> Evidence -> Snapshot      │
│  Tier 1: LinkedIn, Reddit, blogs        │
└────────────────────┬────────────────────┘
                     ↓
┌────────────────────▼────────────────────┐
│  Strategy Module         [live]         │
│  Snapshot -> Positioning -> Plan        │
│  -> Briefs -> Refresh Delta             │
└────────────────────┬────────────────────┘
                     ↓
┌────────────────────▼────────────────────┐
│  Content Module          [live]         │
│  DNA -> Pipeline -> QA -> Adapters      │
└────────────────────┬────────────────────┘
                     ↓
┌────────────────────▼────────────────────┐
│  Publish Module          [live]         │
│  Routing -> Platform delivery           │
└─────────────────────────────────────────┘
```

## Modules

**1. Setup**
- Bootstrap local DNA, writing guide, and platform-specific context.
- Canonical entrypoint: `setup/bootstrap.md`

**2. Intelligence**
- Discovers sources, normalizes evidence, and writes approved snapshots.
- Canonical entrypoints:
  - `intelligence/workflows/discovery.md`
  - `intelligence/workflows/refresh.md`

**3. Strategy**
- Consumes approved intelligence snapshots and emits plans/briefs.
- Canonical entrypoints:
  - `strategy/workflows/linkedin-strategist.md`
  - `strategy/workflows/refresh.md`

**4. Content**
- Owns DNA, writing guide, core pipeline, fact-check, deaify, and platform adapters.
- Canonical entrypoints:
  - `content/workflows/core-pipeline.md`
  - `content/workflows/blog-post.md`
  - `content/workflows/telegram-post.md`
  - `content/workflows/adapters/*.md`

**5. Publish**
- Owns publish routing, adapters, and delivery scripts.
- Canonical entrypoints:
  - `publish/workflows/publish.md`
  - `publish/publish.py`
  - `publish/publish_linkedin.py`

## Quick Start

**Requirements:** Claude Code, Git, Python 3

```bash
git clone https://github.com/YOUR_USERNAME/content-factory.git
cd content-factory
claude
```

Then:

```text
setup linkedin             -> bootstrap LinkedIn DNA
run intelligence           -> build discovered sources + evidence log + snapshot
linkedin strategy          -> build strategy pack + 30-day plan from snapshot
write from strategy brief  -> write a post from an approved brief
```

Publishing examples:

```bash
python3 publish/publish.py --env staging --file output/posts/YYYY-MM-DD-slug.md
python3 publish/publish.py --env production --file output/posts/YYYY-MM-DD-slug.md
python3 publish/publish_linkedin.py --file output/posts/YYYY-MM-DD-slug.md
```

## Triggers

| Say this | What happens |
|----------|--------------|
| `setup linkedin` | Run setup bootstrap for LinkedIn DNA |
| `run intelligence` | Build discovered sources, evidence log, and intelligence snapshot |
| `refresh intelligence` | Refresh discovery artifacts and snapshot |
| `linkedin strategy` | Build strategy pack, content plan, and image briefs |
| `refresh linkedin strategy` | Recompute strategy deltas from refreshed intelligence |
| `I want to write about X` | Run the content pipeline from an idea |
| `write from strategy brief` | Run the content pipeline from a saved brief |
| `в телеграм` / `в linkedin` | Run the relevant content adapter |
| `деаишь этот текст: ...` | Run de-AI-fy only |
| `publish` | Route to the publish module |

## File Structure

```text
├── content/
│   ├── README.md
│   ├── channel-dna.md
│   ├── channel-dna-linkedin.md
│   ├── channel-dna.template.md
│   ├── writing-guide.md
│   ├── writing-guide.template.md
│   ├── ai-terms-ru.md
│   └── workflows/
├── intelligence/
│   ├── README.md
│   ├── accounts/              # local, gitignored
│   ├── templates/
│   └── workflows/
├── strategy/
│   ├── README.md
│   ├── accounts/              # local, gitignored
│   ├── templates/
│   └── workflows/
├── publish/
│   ├── README.md
│   ├── publish.py
│   ├── publish_linkedin.py
│   └── workflows/
├── setup/
│   ├── README.md
│   └── bootstrap.md
├── config/
└── output/posts/
```

## Local Artifact Policy

- `content/channel-dna*.md` and `content/writing-guide.md` are local and gitignored.
- `intelligence/accounts/*` and `strategy/accounts/*` are local and gitignored.
- Tracked files are templates, workflows, docs, and tests.

## No-Claude fallback

If you work outside Claude Code, upload the module workflows you need instead of the old flat `rules/` folder.
