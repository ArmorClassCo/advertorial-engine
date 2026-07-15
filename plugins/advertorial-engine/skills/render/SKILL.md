---
description: Render an existing COPYDOC v1 copy doc into a styled HTML preview using the advertorial-engine renderer. Use when the user already has a copy doc (from generate, or hand-written to the COPYDOC v1 spec) and just wants the browser preview — the strategy card, persona row, annotated image-slot placeholders, CTA buttons, and testimonial pulls — without re-running intake, strategy, or writing.
---

# advertorial-engine: render

You are running the **render** entry-point of the advertorial-engine plugin. It
is a thin wrapper around the standalone renderer: COPYDOC v1 markdown in, styled
preview HTML out. No intake, no strategy, no writing.

Paths use `${CLAUDE_PLUGIN_ROOT}` (the directory containing
`.claude-plugin/plugin.json`); if unset, resolve relative to it.

## Steps

1. **Get the copy doc.** Take the path to a COPYDOC v1 file. If the user pasted
   the copy doc inline instead of giving a path, write it to a file first (e.g.
   `./copy-doc.md`), then render that.
2. **Sanity-check the format** (optional but recommended). The renderer expects
   the COPYDOC v1 shape defined in
   `${CLAUDE_PLUGIN_ROOT}/output/copy-doc-format.md`: line 1 `<!-- COPYDOC v1 -->`,
   a `===STRATEGY===`…`===END STRATEGY===` header, then the body with `[IMAGE]`
   / `[CTA]` blocks. If the input clearly is not COPYDOC v1, say so — the
   renderer will still run but the preview will be sparse.
3. **Render:**
   ```
   python3 ${CLAUDE_PLUGIN_ROOT}/output/html-renderer/render.py <copy-doc.md> [-o <out.html>]
   ```
   The positional argument is the input copy doc; `-o/--out` is optional and
   defaults to the input path with `.md` replaced by `.html`. The script is
   stdlib-only (no dependencies) and prints `wrote <path>`.
4. **Report** the output HTML path back to the user. Do not modify the copy doc
   or the rendered HTML by hand.

## Notes

- The renderer shows the strategy header as a collapsible card for internal
  review — mention that it can be deleted from the HTML before sharing
  externally.
- This command does not judge or change the copy. For a quality read use
  `critique`; to (re)write use `generate`.

## Sibling commands

- `generate` — produce a copy doc from a brief (it renders as its last step).
- `critique` — diagnose an existing page.
- `strategize` — strategy brief only.
