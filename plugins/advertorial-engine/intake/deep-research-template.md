# Deep-Research Prompt Template

When context is minimal, fill the parameters below and hand this prompt to a
deep-research agent (or a human researcher). Its output document feeds the
generation workflow directly: each REQUIRED SECTION below maps 1:1 to checklist
items in intake/context-checklist.md.

Parameters: `{{brand}}`, `{{product}}`, `{{product_category}}`, `{{audience}}`,
`{{price_point}}`, `{{traffic_source}}`, `{{competitor_urls}}` (optional),
`{{known_claims}}` (optional).

---

## PROMPT (copy from here)

You are researching the market for **{{product}}** by **{{brand}}**, a
{{product_category}} aimed at {{audience}}, expected to sell at {{price_point}}
via {{traffic_source}} traffic. Known claims/context so far: {{known_claims}}.

Produce a research document with EXACTLY these sections, in this order. Where you
cannot verify something, say so explicitly rather than inventing.

### 1. MARKET SOPHISTICATION EVIDENCE
How long has this category been sold to this audience? List the dominant claims and
mechanisms competitors lead with today (quote real ad/page headlines where possible,
with sources). Which claims appear so often they are wallpaper? Estimate the
Schwartz sophistication stage (1–5) and justify in 3 sentences.

### 2. AWARENESS DISTRIBUTION
For {{traffic_source}} traffic in this category: what does the typical prospect
already know? Classify the realistic awareness level(s) (unaware / problem-aware /
solution-aware / product-aware / most-aware) and say which single level the landing
page should be built for.

### 3. COMPETITOR ANGLE MAP
5–8 current competitor landing pages or ads ({{competitor_urls}} plus what you
find): for each — the angle in one line, the lead type, the proof they use, the
offer construction. Mark which angles feel exhausted.

### 4. AUDIENCE LANGUAGE & TRIGGER MOMENTS
The audience's own words for the problem (forums, reviews, social comments —
quote and cite). The 3–5 concrete scenes where the problem hurts most. How they
explain past product failures to themselves.

### 5. MECHANISM RESEARCH
The strongest scientifically-grounded explanation for WHY {{product}}'s approach
works, in consumer language. Equally important: the mechanism-of-failure story —
why the familiar alternatives disappoint. Cite sources for every scientific claim
and flag confidence levels.

### 6. PROOF INVENTORY
Everything usable as proof: review counts/ratings across platforms, notable
testimonials (verbatim, with source), studies on the ingredients/components with
the citable numbers, experts associated with the brand or category, before/after
material that exists publicly.

### 7. OBJECTION MAP
The top 6–10 reasons prospects in this category do NOT buy (price, skepticism,
past failures, safety, shipping, partner approval…), each with evidence it is a
real objection, ranked by how often it appears.

### 8. OFFER & COMPLIANCE NOTES
Typical price/bundle/guarantee constructions that work in this category; the
claim-compliance rules that constrain copy (category-specific regulated terms,
required disclaimers); any platform policies of {{traffic_source}} that affect
angle choice.

Deliver as a single markdown document with the section headings above verbatim.
