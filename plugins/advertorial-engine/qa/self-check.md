# Pre-Delivery Self-Check

Run every generated page through all five checks before delivering. These mirror the
evaluation gates the methodology was validated against.

## 1. Format lint (mechanical)

- [ ] Line 1 is exactly `<!-- COPYDOC v1 -->`
- [ ] Strategy header present with ALL TEN keys (format, archetype,
      market_sophistication, awareness_level, lead_type, cta_strategy, image_budget,
      voice, brand, product)
- [ ] Exactly one H1
- [ ] Every `[IMAGE]` block has all seven fields filled: subject, composition, style,
      aspect_ratio, placement_rationale, text_correlation, caption (use `caption: none`
      when the corpus pattern applies — see image-system: captions are usually adjacent
      styled paragraphs, not caption fields)
- [ ] Every `[CTA]` block has type, text, target_note
- [ ] Listicle items are H2s beginning with the number (`## 1. …`)
- [ ] Renders without error: `python3 output/html-renderer/render.py <doc.md>`

## 2. Structural ranges (mechanical sanity)

Compare the draft against its DECLARED archetype's proven ranges. If outside a range,
either fix the draft or justify in the strategy header's cta_strategy/voice notes.

| archetype | words | sections (H2) | images (cadence w/img) | CTAs | first-CTA depth | testimonials | stat mentions |
|---|---|---|---|---|---|---|---|
| personal-story advertorial | 1,800–4,900 (med ~2,600) | 9–20 | 25–90 (≈35–60) | 8–16 | ≤5% (very early) | 7–14 | 12–30 |
| editorial/mechanism advertorial | 1,100–3,600 (med ~1,700) | 10–24 | 20–60 (≈30–65) | 5–12 | ≤10% | 0–8 (brand-dependent) | 10–30 |
| visual-panel advertorial | 700–1,000 | 8–14 | 30–45 (≈20–25) | 4–12 | ≤10% | 4–10 | 6–14 |
| numbered listicle | 760–2,150 (med ~1,300) | items 8–12 | 2–39 (≈60–120) | 1–4 | late (≥40%, usually post-list) or mid-list breaks | 0–2 | 4–16 |
| visual/hybrid listicle | 600–1,200 | 2–6 numbered + panels | 4–45 | 1–3 | late | 0–3 | 2–8 |

Persona rules: advertorials — NO byline/date (brand-story voice). Listicles — byline
AND "Last Updated" date expected (editorial frame). Disclosure labels: rare in the
proven corpus; include only when the client's compliance context requires or requests
editorial-disguise hardening.

## 3. Discriminator self-test (read as a hostile expert)

Read the full draft as a media buyer who has seen 10,000 pages. Kill it if:
- [ ] Any claim could be pasted onto a competitor's product unchanged (not specific)
- [ ] Paragraph rhythm is uniform (real pages alternate 1-line punches with 2–3
      sentence blocks)
- [ ] The mechanism is a benefit restated, not a cause ("works deeper" ≠ mechanism)
- [ ] Testimonials sound like the narrator (vary length, punctuation, competence;
      platform-chrome review dumps, not aphoristic pull-quotes; never a uniform
      "— X., verified customer" pattern)
- [ ] Numbers are round everywhere (real proof uses 2,148 reviews, 78%, 52.21%)
- [ ] Every image subject reads like art direction (subjects are terse page-grade
      tags; direction lives in composition/style)
- [ ] No concrete named scenes (stairs, car door, 3 a.m., mirror) — triggers must be
      somatic and specific
- [ ] The offer appears with no price choreography (anchor → cut → why-the-discount)

**Texture gates (mechanical — count them):**
- [ ] Median paragraph ≤14 words; ≥15% of body blocks ≤6 words
- [ ] At least one %-off token AND concrete currency amounts in the offer zone
- [ ] ONE short all-caps CTA string repeated verbatim (4–10×); no em dashes in
      any button text; urgency microcopy under buttons
- [ ] Sale banner + countdown token; stock counter; buy-box price rows present
- [ ] Review-wall zone with star row + count line; FAQ stub (offer hybrids)
- [ ] Footer shell present: links line, © line, category disclaimer paragraph
- [ ] ZERO brackets/placeholders/production vocabulary anywhere in the copy doc
      (no "[ASSUMED", "TBD", "placeholder", "client-supplied", "buy-box", "carousel")
- [ ] Any "Last Updated"/byline date is a plausible PAST date, not today
- [ ] No number, name, quote, or pet phrase reused from the references' examples
- [ ] All invented specifics derived via the entropy rule (no defaults like
      stock 41–43, no round review counts, no reused dates)
- [ ] No banned constructions (TLDR+emoji, per-day cost punchline, mirror
      aphorism, "We call it…" naming beat unless deliberately chosen once)
- [ ] If the brief gave no offer economics: NO absolute prices — discount-only,
      availability-gated offer hardware

## 4. Leakage & assumption audit

- [ ] Zero references to the methodology's source brands/niches — the page contains
      ONLY this client's brand, product, audience
- [ ] Every fact not present in the client's context is marked `[ASSUMED: …]` at
      intake, and assumptions were listed for the client
- [ ] All scarcity/urgency devices used are ones the client confirmed truthful

## 5. Strategy coherence

- [ ] Declared sophistication stage matches the lead: stages 1–2 → direct promise;
      stage 3 → new mechanism; stage 4 → bigger/differentiated mechanism +
      mechanism-of-failure of rivals; stage 5 → identity/experience lead over claims
- [ ] Declared awareness matches the hook: problem-aware opens on the felt problem;
      solution-aware opens on the differentiator; product-aware opens on offer/proof
- [ ] CTA depth matches format rules (advertorial: early + escalating; listicle:
      after the argument has been built, or as mid-list breaks)
- [ ] Image budget matches the archetype cadence and every image lands a specific
      adjacent claim (check each text_correlation field is a claim, not a theme)
