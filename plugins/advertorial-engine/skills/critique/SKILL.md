---
description: Critique an EXISTING advertorial or listicle landing page against the advertorial-engine methodology. Locates the page on the market-sophistication × awareness grid, names its archetype, scores it against the structural guardrails and the pre-delivery self-check (format, structural ranges, interface texture, offer/proof mechanics, strategy coherence), and returns a ranked diagnosis — observed vs expected, the rule violated, and the smallest fix per failure. Use when the user already has a page (their own draft, a competitor's, or anything in the wild) and wants a methodology-grounded diagnosis, NOT a rewrite.
---

# advertorial-engine: critique

You are running the **critique** entry-point of the advertorial-engine plugin.
It is the reverse of `generate`: given a page that already exists, you diagnose,
score, and recommend. **You do NOT write replacement copy** — no headline, no
paragraphs, no copy doc. The deliverable is a diagnosis.

Paths use `${CLAUDE_PLUGIN_ROOT}` (the directory containing
`.claude-plugin/plugin.json`); if unset, resolve relative to it.

## Step 1 — Collect the inputs

You need two things:
- **The page** — pasted copy, a COPYDOC v1 file, an HTML/text dump, or a URL's
  readable text. A fragment is fine; say what is missing.
- **Minimal market context** — at least what the product is and who it targets.
  Without this, sophistication/awareness classification is impossible; ask once
  for the missing half (if the user gave the page but no context, or context
  but no page).

## Step 2 — Parse the page into structure

Using the metric contract in
`${CLAUDE_PLUGIN_ROOT}/output/copy-doc-format.md`, extract the observable
structure: format (advertorial vs listicle), body word count, section/H2 count
(and numbered-item count for listicles), image count and cadence, CTA count and
first-CTA depth (word offset of the first CTA ÷ total), testimonial count,
persona (byline/date/disclosure present?), offer construction (discount-led vs
guarantee-led, price choreography, scarcity hardware), and the presence of page
furniture (sale banner, sticky bar, buy-box, review wall, FAQ, footer shell).
Report these as the observed feature set.

## Step 3 — Locate it on the grid and name the archetype

Using `${CLAUDE_PLUGIN_ROOT}/references/schwartz-mapping.md`, infer the market
sophistication stage (1–5) and the awareness level the page is built for, each
with one line of evidence from the copy. Then name its archetype from
`${CLAUDE_PLUGIN_ROOT}/references/structure-archetypes.md` (e.g. ADV-1
offer-page hybrid, LIS-2 conquest listicle). If it is a malformed hybrid, say
which archetypes it straddles.

## Step 4 — Score

Run the page against, in order:
1. `${CLAUDE_PLUGIN_ROOT}/qa/self-check.md` — all five sections (format lint;
   structural ranges for the identified archetype; the hostile-expert
   discriminator read + texture gates; leakage/assumption audit; strategy
   coherence). This is the primary rubric.
2. The STRUCTURAL GUARDRAILS table in
   `${CLAUDE_PLUGIN_ROOT}/references/structure-archetypes.md` — the format-level
   hard rails.
3. `${CLAUDE_PLUGIN_ROOT}/references/writing-mechanics.md` and
   `${CLAUDE_PLUGIN_ROOT}/references/persuasion-elements.md` — load the sections
   relevant to what the page contains, to judge tense-role architecture, rhythm/
   interface texture, offer architecture, claim posture, proof stack, numbers
   doctrine, guarantee framing, and CTA economy against the expected behavior.

Judge **coherence against the page's OWN declared/inferred strategy**, not
against a different archetype's rules — a stage-5 identity editorial is not
failed for lacking a stage-3 promise lead.

## Deliverable — a diagnosis, ranked

1. **Verdict line** — identified format + archetype + grid position
   (sophistication stage, awareness level), and a one-line overall read.
2. **Observed feature set** — the Step-2 metrics in a compact block.
3. **What's working** — the dimensions that pass, briefly.
4. **Ranked failures** — most damaging first. For each: the dimension, the
   OBSERVED value/behavior vs the EXPECTED (with the rule/reference it comes
   from), and the SMALLEST fix that would resolve it. Prefer specific,
   countable observations ("first CTA at 62% depth; offer-page hybrids place it
   in the top 10%") over vibes.
5. **Strategic note** — if the page is mis-targeted (wrong archetype for its
   traffic, wrong lead for its sophistication), name the reposition; this is the
   highest-leverage finding when present.

## Hard rules

- **No rewrite.** Diagnose and recommend; do not produce replacement copy,
  copy docs, or rendered HTML. (If the user wants the fix built, point them to
  `generate`.)
- Score against the methodology, not personal taste; cite the reference rule
  behind each failure.
- Corpus isolation: never name the methodology's source brands/niches in the
  diagnosis.

## Sibling commands

- `generate` — build the corrected page once the diagnosis is agreed.
- `strategize` — get the target strategy the page should have been built to.
