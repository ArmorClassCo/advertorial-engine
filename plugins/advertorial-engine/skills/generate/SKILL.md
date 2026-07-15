---
description: Generate proven-pattern direct-response advertorial and listicle landing pages for any brand — from intake through strategy declaration, copy doc, image specs, and HTML preview. Use when the user wants an advertorial, a listicle ("N reasons why…"), a native-style presell page, or a direct-response landing page written end to end; also when they only have a product idea and need to know what context to gather first.
---

# advertorial-engine: generate

You are running the **generate** entry-point of the advertorial-engine plugin.
It produces the two highest-performing direct-response page formats —
advertorials and listicles — using a methodology extracted from a corpus of
proven pages, weighted by advertising spend. Niche-agnostic: everything
specific to a client comes in through intake.

Paths below use `${CLAUDE_PLUGIN_ROOT}` (the directory containing
`.claude-plugin/plugin.json`). If it is not set in your environment, resolve
paths relative to that directory.

## Deliverable

A **copy doc** in COPYDOC v1 format (`${CLAUDE_PLUGIN_ROOT}/output/copy-doc-format.md`
— follow it exactly) plus an HTML preview rendered with
`${CLAUDE_PLUGIN_ROOT}/output/html-renderer/render.py`. The copy doc opens with
a strategy header that DECLARES the strategy (format, archetype, sophistication,
awareness, lead type, CTA strategy, image budget, voice, brand, product) before
any copy. Every image is a fully-specified slot (seven fields); every CTA is an
explicit block.

## Workflow

### Step 1 — Intake audit
Read the client brief. Check it against
`${CLAUDE_PLUGIN_ROOT}/intake/context-checklist.md` (14 categories; ★ items are
blocking). Sort into: PROVIDED / MISSING-blocking / MISSING-nice-to-have.

Route by coverage:
- **Full context** (all ★ present): continue to Step 2.
- **Partial context**: write out the missing items as concrete numbered
  questions for the client into a SIDECAR file (intake-questions.md — a
  required intermediate output). If the engagement allows waiting, stop and
  ask. If instructed to proceed anyway (or you cannot ask), continue: choose
  plausible CONCRETE values for every missing fact (prices, review counts,
  discount depth, dates, quotes) and record each assumption with its chosen
  value in the sidecar for client confirmation. The copy doc itself must be
  production-shaped: no brackets, no `[ASSUMED]`, no placeholders, no
  editorial annotations of any kind in the deliverable.
- **Minimal context** (little beyond a product name): do NOT guess a strategy.
  Emit TWO parallel deliverables and stop: (a)
  `${CLAUDE_PLUGIN_ROOT}/intake/deep-research-template.md` filled with what is
  known — for everything the web can answer; (b) the client question list
  covering the ★ items only the client can answer (their real offer economics,
  guarantee terms, funnel/traffic, cleared testimonials and assets, truthful
  urgency, founder story, voice rules). Research cannot discover the client's
  own business facts — always ship both.

### Step 2 — Strategy declaration (before any copy)
Using `${CLAUDE_PLUGIN_ROOT}/references/schwartz-mapping.md`:
1. Read the market sophistication stage (1–5) from the brief's competitive
   evidence. 2. Read the traffic's awareness level (assume problem-aware when
   unknown). 3. Select the archetype from the selector table (respect the
   client's requested format — advertorial vs listicle — and pick the archetype
   within that format). 4. Select lead type, proof density tier, CTA depth
   plan, and persona per the mapping rules. 5. Set the image budget from
   `${CLAUDE_PLUGIN_ROOT}/references/image-system.md` cadence for that archetype.
Write all ten strategy-header fields now. If the brief conflicts with the
mapping (e.g., requests a hero discount for cold unaware traffic), follow the
brief but note the tension in the cta_strategy field.

### Step 3 — Structure
Take the archetype's flow map and word budgets from
`${CLAUDE_PLUGIN_ROOT}/references/structure-archetypes.md`. Lay out the section
skeleton (H2s, item list for listicles, CTA positions, image-slot positions)
BEFORE writing prose. Enforce the STRUCTURAL GUARDRAILS table (format-level hard
rails: word count, CTA count and first-CTA depth, image cadence, testimonial
counts, byline/date/disclosure rules).

### Step 4 — Write
Apply `${CLAUDE_PLUGIN_ROOT}/references/writing-mechanics.md` (tense-role
architecture, person, rhythm, INTERFACE TEXTURE — fragments, chips, riders,
choppy register — production texture, specificity hygiene, headline device by
awareness, connective tissue, item anatomy) and
`${CLAUDE_PLUGIN_ROOT}/references/persuasion-elements.md` (discount-led offer
architecture, flat claim posture, proof stack order, numbers doctrine,
guarantee as support not headline, price choreography, CTA economy — one short
all-caps CTA string reused verbatim — enemy/absolution, identity layer at
stage 5). Include ALL page furniture from structure-archetypes (sale banner +
countdown, sticky-bar lines, buy-box with concrete prices, review-wall dump,
FAQ stub, footer shell). Facts come from the brief; missing values become
plausible concrete numbers logged in the sidecar — the copy doc never hedges
or brackets them. Invent all specifics fresh (no figures copied from the
references, nothing reused across documents, dates in the past).

### Step 5 — Image slots
Place image slots at their exact positions with all seven fields per
`${CLAUDE_PLUGIN_ROOT}/references/image-system.md` (subject, composition, style,
aspect_ratio, placement_rationale, text_correlation, caption — default
`caption: none`). Compose the standardized proof units (testimonial cards,
buy-box carousel, comparison table, diagrams for every coined term).

### Step 6 — Self-check, render, deliver
Run every item in `${CLAUDE_PLUGIN_ROOT}/qa/self-check.md` (format lint,
structural ranges, hostile-expert read, leakage/assumption audit, strategy
coherence). Fix failures. Render:
`python3 ${CLAUDE_PLUGIN_ROOT}/output/html-renderer/render.py <copy-doc.md>`.
Deliver: copy doc + HTML + (if partial context) the question/assumption list.

## Hard rules

1. Strategy header before copy — a page that can't declare its strategy is a
   guess, not a build.
2. Facts only from intake; assumptions marked `[ASSUMED]` in the sidecar (never
   in the copy doc); urgency devices only if the client confirmed them truthful.
3. Editorial-disguise elements (bylines, date lines, publication styling,
   "ADVERTORIAL" labels) follow the format rules in schwartz-mapping.md and the
   client's compliance context; final compliance sign-off is the operator's,
   not this skill's. Use invented persona names only — never a real person's
   name or likeness without documented authorization in the brief.
4. Corpus isolation: never mention the methodology's source brands or niches in
   client deliverables; examples/ exists for internal illustration only.
5. The copy-doc format spec is frozen — never alter
   `${CLAUDE_PLUGIN_ROOT}/output/copy-doc-format.md`.

## Package map

- `references/structure-archetypes.md` — 5 advertorial + 4 listicle flow maps,
  word budgets, structural guardrails
- `references/schwartz-mapping.md` — sophistication × awareness → archetype,
  lead, proof density, CTA depth, persona
- `references/writing-mechanics.md` — tense roles, voice, rhythm, headlines,
  item anatomy
- `references/image-system.md` — cadence, type-placement rules, proof units,
  seven-field guide
- `references/persuasion-elements.md` — proof stacks, numbers, urgency,
  guarantee, price, CTA system, enemy/identity
- `intake/context-checklist.md` — the 14 categories; degraded-context protocol
- `intake/deep-research-template.md` — parameterized research prompt
- `output/copy-doc-format.md` — COPYDOC v1 spec (frozen)
- `output/html-renderer/render.py` — preview renderer
- `qa/self-check.md` — pre-delivery checklist
- `examples/` — corpus-derived illustrations (internal only)

## Sibling commands

- `strategize` — Steps 1–2 only (strategy brief, no body copy).
- `critique` — diagnose an existing page (archetype + grid + ranked fixes).
- `render` — turn an existing copy doc into an HTML preview.
