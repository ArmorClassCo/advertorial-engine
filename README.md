# advertorial-engine

A local Claude Code plugin that produces and diagnoses direct-response
**advertorial** and **listicle** landing pages, using a methodology
reverse-engineered from a corpus of 73 high-spend live pages (ads-weighted).
Niche-agnostic: everything client-specific enters through intake.

## Commands

| Command | What it does |
|---|---|
| `/advertorial-engine:generate` | Brief → finished COPYDOC v1 copy doc + seven-field image specs + HTML preview. Graceful intake degradation (full → generate; partial → generate + client questions; minimal → deep-research prompt + client questions, and stop). |
| `/advertorial-engine:strategize` | Brief → strategy declaration only (sophistication, awareness, archetype, lead, proof density, CTA plan, image budget) with rationale. **No body copy.** |
| `/advertorial-engine:critique` | Existing page → archetype + sophistication×awareness grid position + ranked failures (observed vs expected + the rule + the smallest fix). **No rewrite.** |
| `/advertorial-engine:render` | A COPYDOC v1 copy doc → styled HTML preview (thin wrapper over the renderer). |

## Structure

Four entry points under `skills/`, sharing one methodology layer:

- `references/` — structure archetypes, Schwartz mapping, writing mechanics,
  image system, persuasion elements (the reusable, niche-agnostic core).
- `intake/` — the 14-category context checklist + parameterized deep-research
  template.
- `output/` — the frozen COPYDOC v1 format spec + the standalone HTML renderer.
- `qa/` — the pre-delivery self-check (also the critique rubric).
- `examples/` — corpus-derived illustrations, **internal reference only** — the
  commands never emit them, and their niche language must not leak into client
  deliverables.

## Validation status

`generate` is the artifact validated by the project's five-gate evaluation
(fingerprint prediction, blind rebuild, transfer to disjoint niches, and
completeness lint all PASS; the discriminator-lineup gate FAIL is analyzed in
the repo's `FINAL-REPORT.md` and attributed to gate construction, not method).

`strategize`, `critique`, and `render` are **newer entry points** that reuse the
same validated reference layer but were verified only by lightweight end-to-end
checks (see the repo's `tests/`), not by the full gate suite. Treat their output
as methodology-grounded but not gate-certified — review before shipping.

## Note on editorial disguise

Fake bylines, datelines, and "advertorial" styling are proven structural
patterns and are available options here. Whether to use them, and all
compliance sign-off, is the operator's call (human-in-the-loop) — this plugin
does not decide it and never uses a real person's name or likeness without
authorization in the brief.
