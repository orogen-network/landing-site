#!/usr/bin/env -S uv run --with markdown --with weasyprint python3
"""Build the Orogen technical whitepaper PDF.

Source: landing-site/content/whitepaper.md (hand-authored, versioned).
Output: landing-site/public/downloads/orogen-whitepaper.pdf

Usage:
    cd landing-site
    uv run --with markdown --with weasyprint python3 scripts/build-whitepaper.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "content" / "whitepaper.md"
OUT = REPO / "public" / "downloads" / "orogen-whitepaper.pdf"

CSS = """
@page { size: A4; margin: 2.5cm 2cm 2.5cm 2cm; @bottom-center { content: "Orogen Whitepaper · " counter(page) " / " counter(pages); font-size: 9pt; color: #666; } }
body { font-family: "Inter", "Helvetica", "Arial", sans-serif; font-size: 10.5pt; line-height: 1.45; color: #111; }
h1 { font-size: 22pt; color: #0c4a6e; border-bottom: 2px solid #0c4a6e; padding-bottom: 4pt; margin-top: 18pt; page-break-after: avoid; }
h2 { font-size: 16pt; color: #155e75; margin-top: 14pt; page-break-after: avoid; }
h3 { font-size: 13pt; color: #164e63; margin-top: 12pt; page-break-after: avoid; }
h4 { font-size: 11pt; color: #1e293b; margin-top: 10pt; page-break-after: avoid; }
p, li { hyphens: auto; }
pre, code { font-family: "JetBrains Mono", "Menlo", "Consolas", monospace; font-size: 8.5pt; }
pre { background: #f1f5f9; padding: 8pt; border-left: 3px solid #0891b2; border-radius: 3px; page-break-inside: avoid; white-space: pre-wrap; }
code { background: #f1f5f9; padding: 1pt 3pt; border-radius: 2px; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9pt; page-break-inside: avoid; }
table th, table td { border: 1px solid #cbd5e1; padding: 4pt 6pt; text-align: left; vertical-align: top; }
table th { background: #e2e8f0; font-weight: 600; }
hr { border: 0; border-top: 1px dashed #94a3b8; margin: 16pt 0; }
.cover { text-align: center; page-break-after: always; padding-top: 30%; }
.cover h1 { font-size: 48pt; border: none; color: #0c4a6e; }
.cover .tag { font-size: 14pt; color: #475569; margin-top: 8pt; }
.cover .meta { font-size: 10pt; color: #64748b; margin-top: 60pt; }
.toc { page-break-after: always; }
.toc h1 { font-size: 22pt; border-bottom: 2px solid #0c4a6e; padding-bottom: 4pt; }
.toc ol { list-style: none; padding-left: 0; margin: 0; }
.toc ol.h3 { padding-left: 1.6em; color: #475569; font-size: 10pt; margin-top: 2pt; margin-bottom: 4pt; }
.toc li { margin: 3pt 0; }
"""


HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$")


def build_toc(md_text: str) -> str:
    """Build a contents block from the document's H2 and H3 headings.

    The cover-block H1 ("Orogen") is intentionally skipped.
    """
    sections: list[tuple[int, str]] = []
    in_code = False
    for line in md_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group(1))
        if level == 1:
            # The document has a single H1 (title); skip it.
            continue
        if level in (2, 3):
            sections.append((level, m.group(2)))

    lines: list[str] = ['<div class="toc">', "<h1>Contents</h1>", '<ol class="h2">']
    open_h3 = False
    for level, title in sections:
        if level == 2:
            if open_h3:
                lines.append("</ol></li>")
                open_h3 = False
            lines.append(f"<li>{title}")
        else:  # level == 3
            if not open_h3:
                lines.append('<ol class="h3">')
                open_h3 = True
            lines.append(f"<li>{title}</li>")
    if open_h3:
        lines.append("</ol></li>")
    else:
        # Close the last <li> opened for an H2 with no H3 children.
        pass
    # Close any dangling <li> from the last H2 that had no H3 children.
    # Simpler: walk lines and close orphan <li> by replacing trailing pattern.
    lines.append("</ol></div>")
    html = "\n".join(lines)
    # Close any <li> that lacks an explicit close before the next <li> or </ol>.
    # weasyprint tolerates unclosed <li>, but tidy it anyway.
    html = html.replace("<li>", "<li>").replace("</ol></li>\n<li>", "</ol></li>\n<li>")
    return html


def render_body_md(md_text: str) -> str:
    """Render the authored markdown to HTML, stripping the cover-block H1.

    The cover is rendered separately so the first content page starts with the
    abstract rather than a duplicated giant title.
    """
    # Drop the leading H1 ("# Orogen") and its immediate bold tagline so that
    # the cover page provides the visual title, not the body.
    lines = md_text.splitlines()
    out: list[str] = []
    seen_first_h1 = False
    skipping = False
    for line in lines:
        if not seen_first_h1 and line.startswith("# "):
            seen_first_h1 = True
            skipping = True
            continue
        if skipping:
            # Skip the boilerplate lines under the H1 until the first H2.
            if line.startswith("## "):
                skipping = False
            else:
                continue
        out.append(line)
    return markdown.markdown(
        "\n".join(out),
        extensions=["fenced_code", "tables", "sane_lists", "attr_list"],
    )


def main() -> int:
    if not SOURCE.exists():
        sys.stderr.write(f"whitepaper source not found at {SOURCE}\n")
        return 1

    md_text = SOURCE.read_text()

    cover = """
<div class="cover">
  <h1>Orogen</h1>
  <div class="tag">Verifiable LLM inference, anchored to physical work.</div>
  <div class="meta">Whitepaper v0.1 — Forge testnet edition<br>
    OROG · orogen.network<br>
    github.com/orogen-network
  </div>
</div>
"""

    toc = build_toc(md_text)
    body = render_body_md(md_text)

    html_doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>Orogen Whitepaper</title>
<style>{CSS}</style></head><body>{cover}{toc}{body}</body></html>"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html_doc, base_url=str(REPO)).write_pdf(OUT)
    size_kb = OUT.stat().st_size // 1024
    sys.stdout.write(f"wrote {OUT} ({size_kb} KB)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
