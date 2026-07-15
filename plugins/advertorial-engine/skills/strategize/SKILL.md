---
description: Run the advertorial-engine methodology on a product brief and return a STRATEGY BRIEF only — market sophistication stage, prospect awareness, recommended archetype, lead type and promise/mechanism/identification allocation, proof-density requirement, CTA-depth plan, persona, and image budget — without writing any body copy. Use when the user wants the strategic decision (which page to build and why) but will write the copy themselves, or wants to approve the strategy before generation.
---

# advertorial-engine: strategize

You are running the **strategize** entry-point of the advertorial-engine
plugin. This is Steps 1–2 of the `generate` workflow run standalone: you
diagnose the market and DECLARE the strategy, then STOP. You do NOT write
headlines, body copy, image slots, CTA blocks, or a copy doc.

Paths use `${CLAUDE_PLUGIN_ROOT}` (the directory containing
`.claude-plugin/plugin.json`); if unset, resolve relative to it.

## Step 1 — Intake audit (same routing as generate)

Read the brief. Check it against
`${CLAUDE_PLUGIN_ROOT}/intake/context-checklist.md` (14 categories; ★ blocking).
Sort into PROVIDED / MISSING-blocking / MISSING-nice-to-have, then route:

- **Full context** (all ★ present): proceed to Step 2.
- **Partial context**: you can still declare a provisional strategy, but you
  MUST list the missing ★ items as concrete client questions and mark every
  strategic choice that depends on an assumed value (e.g. "sophistication stage
  assumes competitors run X — confirm"). Deliver the brief plus the question
  list.
- **Minimal context** (little beyond a product name): do NOT guess a strategy.
  Emit the two parallel intake deliverables and stop — (a)
  `${CLAUDE_PLUGIN_ROOT}/intake/deep-research-template.md` filled with what is
  known; (b) the client question list for the ★ facts only the client can
  answer. Say plainly that a strategy cannot be declared until those return.

## Step 2 — Strategy declaration

Using `${CLAUDE_PLUGIN_ROOT}/references/schwartz-mapping.md`:

1. **Sophistication stage (1–5)** — read it from the brief's competitive
   evidence; give the one-line evidence.
2. **Awareness level** — the level of the TRAFFIC this page will receive
   (assume problem-aware if unstated; say so).
3. **Archetype** — select from the selector table for the requested format
   (advertorial vs listicle), naming it with its code from
   `${CLAUDE_PLUGIN_ROOT}/references/structure-archetypes.md` (e.g. ADV-3
   mechanism editorial, LIS-1 trending listicle).
4. **Lead type + allocation** — the lead by stage, and the
   promise/mechanism/identification emphasis.
5. **Proof density** — the tier required by stage (which proof elements, roughly
   how many).
6. **CTA-depth plan** — first-CTA depth and cadence by awareness.
7. **Persona** — byline/date/disclosure rules for the format.
8. **Image budget** — the integer cadence for the archetype from
   `${CLAUDE_PLUGIN_ROOT}/references/image-system.md`.

## Deliverable

A readable strategy brief containing:

1. **Strategy header** — the ten COPYDOC v1 strategy-header fields with values
   (format, archetype, market_sophistication, awareness_level, lead_type,
   cta_strategy, image_budget, voice, brand, product), so it can be pasted
   straight into a `generate` run or a hand-written copy doc.
2. **Rationale** — one short paragraph per decision above, each citing the
   evidence or rule it follows. Where the brief conflicts with the mapping,
   follow the brief and flag the tension.
3. **Build notes** — the archetype's flow map and word budgets (from
   structure-archetypes) as a skeleton the writer will fill, and the proof/CTA/
   furniture requirements — described, NOT written out as copy.
4. If partial/minimal context: the client question list (and, for minimal, the
   filled research prompt).

## Hard rules

- **No body copy.** No headline text, no paragraphs, no testimonials, no
  `[IMAGE]` or `[CTA]` blocks, no rendered HTML. If you catch yourself writing a
  sentence a visitor would read, stop — that belongs to `generate`.
- Same corpus-isolation rule as generate: never name the methodology's source
  brands or niches in the deliverable.
- Facts and assumptions: strategy may rest on assumed market facts, but every
  assumption is labeled and, for client-only facts, routed to the question list.

## Sibling commands

- `generate` — take this strategy all the way to finished copy + HTML.
- `critique` — score an existing page against this same strategy engine.
