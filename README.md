# AI Content Factory

A modular AI content system for turning business context into publishable content without losing voice.

```
Setup -> Orchestrator -> Intelligence -> Strategy -> Content -> Publish
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
│  Orchestrator Module     [live]         │
│  Guided pilot flow and handoff          │
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

**2. Orchestrator**
- Guides the user through the pilot flow, quality gates, and module handoffs.
- Canonical entrypoints:
  - `orchestrator/workflows/start-linkedin-pilot.md`
  - `orchestrator/workflows/continue-linkedin-pilot.md`
  - `orchestrator/workflows/review-intelligence-coverage.md`

**3. Intelligence**
- Discovers sources, normalizes evidence, and writes approved snapshots.
- Canonical entrypoints:
  - `intelligence/workflows/discovery.md`
  - `intelligence/workflows/refresh.md`

**4. Strategy**
- Consumes approved intelligence snapshots and emits plans/briefs.
- Canonical entrypoints:
  - `strategy/workflows/linkedin-strategist.md`
  - `strategy/workflows/refresh.md`

**5. Content**
- Owns DNA, writing guide, core pipeline, fact-check, deaify, and platform adapters.
- Canonical entrypoints:
  - `content/workflows/core-pipeline.md`
  - `content/workflows/blog-post.md`
  - `content/workflows/telegram-post.md`
  - `content/workflows/adapters/*.md`

**6. Publish**
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
start linkedin pilot       -> guided pilot flow from brief to research to strategy handoff
setup linkedin             -> bootstrap LinkedIn DNA only
run intelligence           -> build and save discovered sources + evidence log + snapshot + quality reports
linkedin strategy          -> build strategy pack + 30-day plan from snapshot
write from strategy brief  -> write a post from an approved brief
linkedin visual           -> build reference board / visual DNA / one LinkedIn card
```

Publishing examples:

```bash
python3 publish/publish.py --env staging --file content/accounts/<account-slug>/posts/YYYY-MM-DD-slug.md
python3 publish/publish.py --env production --file content/accounts/<account-slug>/posts/YYYY-MM-DD-slug.md
python3 publish/publish_linkedin.py --file content/accounts/<account-slug>/posts/YYYY-MM-DD-slug.md
```

## Triggers

| Say this | What happens |
|----------|--------------|
| `start linkedin pilot` | Run the guided pilot orchestrator |
| `continue linkedin pilot` | Resume the guided pilot from saved status |
| `review intelligence coverage` | Review saved coverage and research reports |
| `setup linkedin` | Run setup bootstrap for LinkedIn DNA |
| `run intelligence` | Build and save discovered sources, evidence log, intelligence snapshot, and quality reports |
| `refresh intelligence` | Refresh and save discovery artifacts and snapshot |
| `linkedin strategy` | Build strategy pack, content plan, and image briefs |
| `refresh linkedin strategy` | Recompute strategy deltas from refreshed intelligence |
| `I want to write about X` | Run the content pipeline from an idea |
| `write from strategy brief` | Run the content pipeline from a saved brief |
| `linkedin visual` | Build LinkedIn visual artifacts from references and an approved post |
| `в телеграм` / `в linkedin` | Run the relevant content adapter |
| `деаишь этот текст: ...` | Run de-AI-fy only |
| `publish` | Route to the publish module |

## File Structure

```text
├── content/
│   ├── README.md
│   ├── accounts/              # local, gitignored
│   ├── channel-dna.md
│   ├── channel-dna-linkedin.md
│   ├── channel-dna.template.md
│   ├── writing-guide.md
│   ├── writing-guide.template.md
│   ├── ai-terms-ru.md
│   ├── templates/
│   └── workflows/
├── orchestrator/
│   ├── README.md
│   ├── accounts/              # local, gitignored
│   ├── templates/
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
```

## Local Artifact Policy

- `content/channel-dna*.md`, `content/writing-guide.md`, and `content/accounts/*` are local and gitignored.
- `intelligence/accounts/*`, `strategy/accounts/*`, and `orchestrator/accounts/*` are local and gitignored.
- Tracked files are templates, workflows, docs, and tests.
- These local account workspaces are also how the system persists progress between sessions on the same machine. The main resume file for the guided flow is `orchestrator/accounts/<account-slug>/pilot-status.yaml`.

## No-Claude fallback

If you work outside Claude Code, upload the module workflows you need instead of the old flat `rules/` folder.
