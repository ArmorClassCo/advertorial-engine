#!/usr/bin/env python3
"""COPYDOC v1 -> preview HTML renderer (self-contained, stdlib only).

Usage: python3 render.py <copy-doc.md> [-o out.html]

Renders the canonical copy doc as a styled editorial landing-page preview:
persona row under the headline, image slots as annotated placeholder frames
(subject / composition / caption visible), CTA blocks as buttons, testimonial
blockquotes styled as review pulls. The strategy header renders as a small
collapsible strategy card at the top (for internal review; delete it from the
HTML if sharing externally).
"""

import argparse
import html
import re
import sys

STRAT_START = "===STRATEGY==="
STRAT_END = "===END STRATEGY==="

CSS = """
:root { --ink:#1c1c1e; --muted:#6b6b70; --accent:#c0392b; --bg:#ffffff;
        --wash:#f6f5f2; --rule:#e4e2dc; }
* { box-sizing: border-box; }
body { margin:0; background:var(--wash); color:var(--ink);
       font:17px/1.65 Georgia, 'Times New Roman', serif; }
.page { max-width:720px; margin:0 auto; background:var(--bg);
        padding:28px 34px 60px; }
.strategy { font:12px/1.5 -apple-system, Helvetica, Arial, sans-serif;
            background:#fffbe8; border:1px solid #e8ddac; border-radius:6px;
            padding:10px 14px; margin-bottom:22px; color:#5b5326; }
.strategy summary { cursor:pointer; font-weight:700; }
.disclosure { font:11px/1 -apple-system, Helvetica, Arial, sans-serif;
              letter-spacing:.12em; text-transform:uppercase; color:var(--muted);
              border:1px solid var(--rule); display:inline-block;
              padding:4px 8px; margin-bottom:14px; }
h1 { font-size:34px; line-height:1.18; margin:6px 0 10px; letter-spacing:-.01em; }
.byline { font:13px/1.4 -apple-system, Helvetica, Arial, sans-serif;
          color:var(--muted); border-bottom:1px solid var(--rule);
          padding-bottom:14px; margin-bottom:22px; }
.byline b { color:var(--ink); }
h2 { font-size:24px; line-height:1.25; margin:34px 0 12px; }
h3 { font-size:19px; margin:26px 0 10px; }
p { margin:0 0 16px; }
blockquote { margin:22px 8px; padding:14px 18px; background:var(--wash);
             border-left:4px solid var(--accent); font-style:italic; }
.figure { margin:24px 0; border:1px dashed #b9b6ae; border-radius:8px;
          background:var(--wash); overflow:hidden; }
.figure .frame { display:flex; align-items:center; justify-content:center;
                 min-height:120px; padding:18px;
                 font:13px/1.5 -apple-system, Helvetica, Arial, sans-serif;
                 color:var(--muted); text-align:center; }
.figure .meta { font:11px/1.5 -apple-system, Helvetica, Arial, sans-serif;
                color:#8a877f; padding:8px 14px; border-top:1px dashed #d5d2c9; }
.figure .caption { font:13px/1.5 -apple-system, Helvetica, Arial, sans-serif;
                   color:var(--ink); padding:9px 14px 11px;
                   border-top:1px solid var(--rule); background:#fff; }
.cta { display:block; text-align:center; margin:26px 0; }
.cta a { display:inline-block; background:var(--accent); color:#fff;
         text-decoration:none; font:700 18px/1 -apple-system, Helvetica,
         Arial, sans-serif; padding:16px 34px; border-radius:8px;
         box-shadow:0 3px 0 #90291d; }
.cta .note { display:block; font:11px/1.6 -apple-system, Helvetica, Arial,
             sans-serif; color:var(--muted); margin-top:8px; }
hr { border:0; border-top:1px solid var(--rule); margin:34px 0; }
"""


def esc(s):
    return html.escape(s or "", quote=False)


def render(md_text):
    lines = md_text.splitlines()
    strategy, body, in_s, started = {}, [], False, False
    for ln in lines:
        s = ln.strip()
        if s == STRAT_START:
            in_s = True
            continue
        if s == STRAT_END:
            in_s = False
            started = True
            continue
        if in_s:
            m = re.match(r"^([a-z_]+)\s*:\s*(.*)$", s)
            if m:
                strategy[m.group(1)] = m.group(2)
            continue
        if s == "<!-- COPYDOC v1 -->":
            continue
        if started or not strategy:
            body.append(ln)

    out = []
    if strategy:
        rows = "".join(f"<div><b>{esc(k)}:</b> {esc(v)}</div>"
                       for k, v in strategy.items())
        out.append(f'<details class="strategy"><summary>STRATEGY '
                   f'DECLARATION</summary>{rows}</details>')

    persona = {"byline": None, "date": None, "disclosure": None}
    i = 0
    para = []

    def flush():
        nonlocal para
        if para:
            out.append(f"<p>{esc(' '.join(para))}</p>")
            para = []

    while i < len(body):
        s = body[i].strip()
        if not s:
            flush()
            i += 1
            continue
        if s == "---":
            flush()
            out.append("<hr>")
            i += 1
            continue
        if s.startswith("[IMAGE]"):
            flush()
            f = {}
            i += 1
            while i < len(body) and not body[i].strip().startswith("[/IMAGE]"):
                m = re.match(r"^([a-z_]+)\s*:\s*(.*)$", body[i].strip())
                if m:
                    f[m.group(1)] = m.group(2)
                i += 1
            i += 1
            cap = f.get("caption", "none")
            caph = (f'<div class="caption">{esc(cap)}</div>'
                    if cap and cap.lower() != "none" else "")
            out.append(
                '<div class="figure">'
                f'<div class="frame">[{esc(f.get("aspect_ratio", "?"))}] '
                f'{esc(f.get("subject", ""))}<br>'
                f'<i>{esc(f.get("composition", ""))} — '
                f'{esc(f.get("style", ""))}</i></div>'
                f'<div class="meta">supports: {esc(f.get("text_correlation", ""))}'
                f' · placement: {esc(f.get("placement_rationale", ""))}</div>'
                f"{caph}</div>")
            continue
        if s.startswith("[CTA]"):
            flush()
            f = {}
            i += 1
            while i < len(body) and not body[i].strip().startswith("[/CTA]"):
                m = re.match(r"^([a-z_]+)\s*:\s*(.*)$", body[i].strip())
                if m:
                    f[m.group(1)] = m.group(2)
                i += 1
            i += 1
            note = f.get("target_note", "")
            out.append(f'<div class="cta"><a href="#">{esc(f.get("text", "Learn More"))}'
                       f'</a>{f"<span class=<double>note</double>>{esc(note)}</span>" if note else ""}</div>'
                       .replace("<double>", '"').replace("</double>", '"'))
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            flush()
            lvl = len(m.group(1))
            if lvl == 1:
                out.append(f"<h1>{esc(m.group(2))}</h1>")
                # persona lines may follow immediately
                j = i + 1
                prow = []
                while j < len(body):
                    pm = re.match(r"^(BYLINE|DATE|DISCLOSURE)\s*:\s*(.*)$",
                                  body[j].strip())
                    if not pm:
                        break
                    persona[pm.group(1).lower()] = pm.group(2)
                    j += 1
                if persona["disclosure"]:
                    out.insert(len(out) - 1,
                               f'<div class="disclosure">{esc(persona["disclosure"])}</div>')
                if persona["byline"] or persona["date"]:
                    bits = []
                    if persona["byline"]:
                        bits.append(f"<b>{esc(persona['byline'])}</b>")
                    if persona["date"]:
                        bits.append(esc(persona["date"]))
                    out.append(f'<div class="byline">{" · ".join(bits)}</div>')
                i = j
                continue
            out.append(f"<h{min(lvl,3)}>{esc(m.group(2))}</h{min(lvl,3)}>")
            i += 1
            continue
        if s.startswith(">"):
            flush()
            q = [re.sub(r"^>\s?", "", s)]
            i += 1
            while i < len(body) and body[i].strip().startswith(">"):
                q.append(re.sub(r"^>\s?", "", body[i].strip()))
                i += 1
            out.append(f"<blockquote>{esc(' '.join(q))}</blockquote>")
            continue
        pm = re.match(r"^(BYLINE|DATE|DISCLOSURE)\s*:\s*(.*)$", s)
        if pm:  # persona line not directly under H1 — still render sensibly
            flush()
            persona[pm.group(1).lower()] = pm.group(2)
            out.append(f'<div class="byline"><b>{esc(pm.group(2))}</b></div>')
            i += 1
            continue
        para.append(s)
        i += 1
    flush()

    title = strategy.get("product", "Landing page preview")
    return ("<!doctype html><html><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width, initial-scale=1'>"
            f"<title>{esc(title)}</title><style>{CSS}</style></head>"
            f"<body><div class='page'>{''.join(out)}</div></body></html>")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("copydoc")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()
    with open(args.copydoc, encoding="utf-8") as f:
        html_out = render(f.read())
    out_path = args.out or re.sub(r"\.md$", "", args.copydoc) + ".html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
