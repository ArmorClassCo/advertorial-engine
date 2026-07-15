# Copy-Doc Format v1 (FROZEN)

The canonical deliverable format for every generated page and every normalized corpus
page. The skill (Phase 3) must adopt this verbatim as `output/copy-doc-format.md`
(byte-identical — Gate 5 checks). `eval/fingerprint` parses this format; `eval/normalizer`
emits it from raw corpus pages.

A copy doc is a UTF-8 markdown file with three zones:

## Zone 1 — Sentinel + strategy header

Line 1 is exactly:

```
<!-- COPYDOC v1 -->
```

Then a fenced strategy header (declares strategy; stripped before discriminator lineups
and ignored by fingerprint word counts):

```
===STRATEGY===
format: advertorial | listicle
archetype: <archetype name from the skill's taxonomy>
market_sophistication: <1-5>
awareness_level: <unaware | problem-aware | solution-aware | product-aware | most-aware>
lead_type: <short label, e.g. story-lead / promise-lead / identification-lead / secret-lead>
cta_strategy: <short description of CTA count, placement pattern, phrasing class>
image_budget: <integer — planned number of image slots>
voice: <narrator persona, person, tense plan in one line>
brand: <brand name>
product: <product name>
===END STRATEGY===
```

All ten keys are required, one per line, `key: value`, in any order.

## Zone 2 — Body

Everything after `===END STRATEGY===` is the page body, top-to-bottom in reading order.

1. **Headline** — exactly one H1: `# <headline text>`.
2. **Persona block** (optional, immediately after H1, any subset, one per line):
   ```
   BYLINE: <author name and optional role>
   DATE: <display date>
   DISCLOSURE: <verbatim disclosure label, e.g. ADVERTORIAL, Advertisement, Sponsored>
   ```
3. **Section headings** — H2 (`##`) for major sections. Listicle items MUST be H2s
   beginning with the item number: `## 1. <item title>` (or `## 1) <title>`). H3 (`###`)
   allowed for sub-points.
4. **Paragraphs** — plain markdown text.
5. **Testimonials** — markdown blockquotes; attribution after an em/en dash or hyphen,
   optionally with a detail clause:
   ```
   > I stopped hiding my hands within three weeks. — Maren K., verified buyer
   ```
6. **Image slots** — a fenced block, all seven lines required, at the exact position the
   image appears in the page flow:
   ```
   [IMAGE]
   subject: <what the image shows>
   composition: <framing/shot type>
   style: <photographic/illustrative mood>
   aspect_ratio: <e.g. 4:3, 1:1, 16:9, 3:4>
   placement_rationale: <why the image sits at this point in the flow>
   text_correlation: <the specific claim in adjacent copy this image supports>
   caption: <displayed caption text, or "none">
   [/IMAGE]
   ```
7. **CTA slots** — a fenced block at the exact position the call-to-action appears:
   ```
   [CTA]
   type: button | link | banner
   text: <the displayed CTA text>
   target_note: <where it leads, e.g. product page / checkout>
   [/CTA]
   ```
8. **Horizontal rules** (`---`) may separate major movements; ignored by metrics.

## Zone 3 — none

Nothing after the last body element. No appendices, no notes to the client, no
meta-commentary. Rationale lives only inside the strategy header and the structured
fields above.

## Lineup view (defined here so it is frozen)

For discriminator lineups, a copy doc is reduced to its **lineup view** by the
normalizer's `--lineup` mode, identically for real-normalized and generated docs:

- Drop Zone 1 entirely (sentinel + strategy header).
- Keep headline, persona block lines, headings, paragraphs, blockquotes, `---`.
- Replace each `[IMAGE]...[/IMAGE]` block with two lines:
  `[IMAGE: <subject cleaned: lowercased; filename-like tokens, digit/underscore
  tokens removed; truncated to 8 words>]` (just `[IMAGE]` if nothing survives
  cleaning) and, if caption ≠ none, `[CAPTION: <caption text>]`.
- Replace each `[CTA]...[/CTA]` block with one line: `[BUTTON: <text>]`.
- Strip all URLs and markdown link targets (keep link text).

## Parsing rules for metrics (frozen contract)

- Body word count = whitespace-separated tokens in paragraphs, headings, blockquotes,
  captions, CTA text — excluding structured field labels and non-caption image fields.
- Section count = number of H2 headings.
- Listicle item count = number of H2 headings starting with an integer + `.` or `)`.
- Image count = number of `[IMAGE]` blocks; caption present iff caption field ≠ "none".
- CTA count = number of `[CTA]` blocks; first-CTA depth = body words preceding the first
  block ÷ total body words.
- Byline/date/disclosure present = corresponding persona line exists.
- Testimonial = blockquote containing an attribution dash.
