# Examples

Two **synthetic, self-authored** copy docs illustrating the COPYDOC v1 output
format the plugin produces:

- `example-advertorial.md` — a personal-story / mechanism advertorial for a
  fictional sleep supplement.
- `example-listicle.md` — a numbered "reasons why" listicle for a fictional
  senior-dog mobility chew.

Both use invented brands in niches chosen to be generic illustrations. They are
reference material only — the plugin never emits them, and their language should
not be copied into client deliverables. Use them to see what a finished copy doc
looks like: the strategy header, persona block, section flow, seven-field image
slots, CTA blocks, and testimonial pulls.

To preview either one as HTML:

```
python3 ../output/html-renderer/render.py example-listicle.md -o /tmp/preview.html
```
