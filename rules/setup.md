---
description: Onboarding — sets up DNA for the main channel or a new platform
globs:
  - "**/*.md"
---

# Setup — Onboarding

**Language rule: detect the language the user writes in and respond in that language throughout the entire setup.**

Sets up Channel DNA through a dialogue.
Works for the **main channel** (Telegram) and **new platforms** (LinkedIn, Threads, etc.).

**Ask questions one at a time. Wait for the answer before the next one.**

---

## Detect mode

If a platform is specified in the command (e.g. `setup linkedin`, `setup threads`) →
run **Platform Setup** (section below).

If no platform specified → run **Main Channel Setup**.

---

## Step 0: Existing channel or starting from scratch?

Ask:
> "Do you already have a channel or social media with content — or are we starting from scratch?"

**If from scratch** → skip this step, go to Step 1.

**If there's a channel** → ask:
> "Share the link — I'll try to look at what you have. Or just paste 5–10 posts you like right here."

Two analysis options:

**Option A: Telegram channel link**
- Try WebFetch on `https://t.me/s/{username}`
- If it works — read posts, form an impression:
  - Main topics, tone and voice
- Share briefly: "I see you write about X, Y. Tone is like this."
- If WebFetch fails (error or empty response) → go to Option B

**Option B: Posts manually**
- Say: "Can't reach the channel directly. Paste 5–10 of your posts here — I'll analyze your voice from them."
- After receiving posts — analyze voice (same parameters: topics, tone, hooks)

Result in both cases: understanding of voice and topics before starting questions.

---

## Step 1: Direction (looking forward)

> "If you looked at this channel in 6 months — what would you want to see? What would it be about, who reads it, what are you building through it?"

Write down: channel goal, audience, why this matters to the author.

---

## Step 2: Unique angle

> "There's a sea of AI content right now. What's yours — what can only you show from your experience? What angle do you have that others don't?"

Write down: author's unique positioning.

---

## Step 3: Content pillars

Based on answers from steps 1–2, **propose 4–6 pillars yourself**.
Don't ask an open question — formulate options and ask:

> "Based on what you've shared, I see these pillars:
> 1. [pillar] — [description]
> 2. [pillar] — [description]
> ...
> Does this feel right? Anything to remove / add / rename?"

Write final pillars to `channel-dna.md`.

---

## Step 4: Voice — your posts

> "Share 5–10 of your posts that you like or that performed well. Paste them right here — I'll analyze your voice."

After receiving posts — run deep voice analysis:

```
You are a professional linguistic stylist and expert in analyzing author's writing.

Your task: conduct a deep analysis of the provided text samples and create a detailed guide that will allow you to precisely reproduce the author's style in new social media posts.

Analyze and systematize the following aspects (write all features in one line after the aspect name, separated by semicolons):

Tone and style: {Conduct a detailed analysis of the emotional tone: formal/informal, serious/humorous, authoritative/humble. Identify the dominant emotional notes: inspiring, provocative, informative, critical, etc. Note rhetorical devices, metaphors, analogies used. Determine how the author positions themselves: as an expert, friend, mentor, researcher.}

Lexical features: {Analyze vocabulary: simple/complex, everyday/specialized, contemporary/classical. Identify characteristic marker words, set phrases, author's neologisms, idioms. Determine presence of professional terminology, foreign words, slang. Create a list of 10–15 words and expressions most characteristic of the author.}

Syntactic features: {Determine typical sentence length, structure and complexity. Analyze the ratio of simple to complex sentences. Note the use of introductory constructions, participial phrases. Identify characteristic syntactic devices: inversion, parallelism, ellipsis, rhetorical questions.}

Content structure: {Analyze the compositional structure: introduction, main part, conclusion. Identify typical text-opening techniques (hooks): question, provocation, story, statistics. Identify logical transitions between parts. Determine key closing elements: conclusion, call to action, rhetorical question. Describe how the main idea develops throughout the text.}

Formatting and visual presentation: {Analyze paragraph length and structure, use of bullet/numbered lists, quotes, text highlights. Determine typical number of sentences per paragraph. Note use of headings and subheadings. Analyze visual structuring of information.}

Spelling, punctuation and typography: {Note punctuation preferences: dashes, colons, parentheses, ellipses. Analyze formatting of quotes and dialogues. Determine if the author addresses the reader, and what form they use. Identify typographic preferences: quote style, dash type, list formatting.}

Stylistic devices and figures of speech: {Analyze use of metaphors, similes, epithets, hyperbole, irony and other devices. Identify presence of stories, personal examples, statistics, expert opinions. Determine the balance between emotional and factual content.}

Audience engagement: {Analyze how the author engages the reader: direct address, rhetorical questions, imperatives. Determine the degree of dialogic quality, personal communication feel. Identify ways empathy is shown, objections anticipated, trust built.}

Provide only the analysis result by the specified sections, without introductory explanations or comments. Your task is to create such a precise style guide that new text written from it would be indistinguishable from the author's original work.
```

Write the result to `rules/writing-guide.md` — in full, preserving all 8 sections.

---

## Step 5: Voice — references (optional)

> "Are there channels or authors whose style resonates with you? Share 2–3 posts you like — not to copy, but so I understand what resonates."

Write examples to `channel-dna.md` section "Reference channels".

---

## Step 6: Technical parameters

Ask in one message:
> "Last thing: post length (short up to 500 / medium up to 1500 / long?), emojis (yes/no/sometimes), hashtags?"

Write to `channel-dna.md` section "Post format".

---

## After onboarding (Main Channel)

Check that these are filled:
- [ ] `channel-dna.md` — goal, audience, unique angle, pillars, post examples, references, format
- [ ] `rules/writing-guide.md` — voice, hooks, post types, what to avoid

Tell the user:

```
Done. Channel DNA is set up.

Now to write a post — just share an idea.
I'll run the pipeline: Questions → Research → Write → Fact-check → Deaify → Draft.

Want to try right now?
```

---

## Platform Setup — Onboarding a new platform

Use when connecting LinkedIn, Threads, Instagram or another platform.

**Files:** `channel-dna-{platform}.md` (e.g. `channel-dna-linkedin.md`)

**Ask questions one at a time. Wait for the answer.**

---

### Step P0: Platform goal

> "Why {platform} in your content mix? What are you building there — audience, leads, personal brand, niche reputation?"

Write down: goal, KPI, time horizon.

---

### Step P1: Language

> "What language are we posting in on {platform}?
> A) English only
> B) Russian only
> C) Both — different content for different audiences"

Language affects everything: voice, hooks, audience. Write it down clearly.

---

### Step P2: Audience on this platform

> "Who reads you there specifically? Can differ from Telegram — different country, different context, different familiarity with you."

Write down: audience, context (cold/warm), what they care about.

---

### Step P3: Voice on this platform

> "How do you want to sound on {platform}? This can differ from Telegram.
> For example: more professional, shorter, with a different focus on business/personal.
> Or exactly the same — then say 'same voice'."

If "same voice" → use `rules/writing-guide.md` without changes.
If different → write differences to `channel-dna-{platform}.md`.

---

### Step P4: References on this platform

> "Share 3–5 posts you like specifically on {platform} — not yours, someone else's. Whose style resonates? You can just paste the text."

After receiving — analyze:
- What the structure has in common
- How they open and close
- Tone, length, use of white space

Write to `channel-dna-{platform}.md` section "References".

---

### Step P5: Your own examples (optional)

> "Have you posted anything on {platform} already? If there are posts that performed — share them, I'll analyze."

If none — skip.

---

### Step P6: Technical platform parameters

Share platform parameters (you know them), then ask:
> "For {platform} the optimal length is {X} characters. Hashtags — yes/no? Emojis?"

Write final parameters.

---

### After Platform Setup

Check what's filled in `channel-dna-{platform}.md`:
- [ ] Goal and KPI
- [ ] Language (clearly stated)
- [ ] Audience on the platform
- [ ] Voice / differences from main
- [ ] References (3–5 posts)
- [ ] Technical parameters

Tell the user:

```
Done. DNA for {platform} is set up.
File: channel-dna-{platform}.md

Now when you say "for {platform}" the adapter will read exactly this file.
Write a post — want to try?
```
