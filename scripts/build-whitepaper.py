#!/usr/bin/env -S uv run --with markdown --with weasyprint python3
"""Build the Orogen whitepaper PDF from the plan + RFC specs + research dossier.

Usage: uv run --with markdown --with weasyprint python3 build-whitepaper.py
Output: landing-site/public/downloads/orogen-whitepaper.pdf
"""

from __future__ import annotations

import sys
from pathlib import Path

import markdown
from weasyprint import HTML

REPO = Path(__file__).resolve().parents[2]
PLAN = Path.home() / ".claude" / "plans" / "make-a-full-plan-groovy-gosling.md"
RFC_DIR = REPO / "chain-tooling-rust" / "specs"
OUT = REPO / "landing-site" / "public" / "downloads" / "orogen-whitepaper.pdf"

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
table th, table td { border: 1px solid #cbd5e1; padding: 4pt 6pt; text-align: left; }
table th { background: #e2e8f0; font-weight: 600; }
hr { border: 0; border-top: 1px dashed #94a3b8; margin: 16pt 0; }
.cover { text-align: center; page-break-after: always; padding-top: 30%; }
.cover h1 { font-size: 48pt; border: none; color: #0c4a6e; }
.cover .tag { font-size: 14pt; color: #475569; margin-top: 8pt; }
.cover .meta { font-size: 10pt; color: #64748b; margin-top: 60pt; }
.toc h1 { font-size: 22pt; border-bottom: 2px solid #0c4a6e; padding-bottom: 4pt; }
.toc ul { list-style: none; padding-left: 0; }
.toc li { margin: 3pt 0; font-size: 10.5pt; }
.toc li.deep { padding-left: 14pt; color: #475569; }
.cover, .toc { page-break-after: always; }
"""


def render_md(path: Path) -> str:
    text = path.read_text()
    return markdown.markdown(text, extensions=["fenced_code", "tables", "toc", "sane_lists", "attr_list"])


def main() -> int:
    if not PLAN.exists():
        sys.stderr.write(f"plan not found at {PLAN}\n")
        return 1
    if not RFC_DIR.exists():
        sys.stderr.write(f"RFC dir not found at {RFC_DIR}\n")
        return 1

    rfcs = sorted(RFC_DIR.glob("RFC-*.md"))
    if len(rfcs) != 10:
        sys.stderr.write(f"warn: expected 10 RFCs, found {len(rfcs)}\n")

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

    toc = """
<div class="toc">
<h1>Contents</h1>
<ul>
<li>Part I — Network architecture and rationale</li>
<li>Part II — Cross-team integration RFCs (1–10)</li>
<li class="deep">RFC-0001 — Signed response receipt format</li>
<li class="deep">RFC-0002 — Multi-vendor attestation report</li>
<li class="deep">RFC-0003 — Heartbeat schema</li>
<li class="deep">RFC-0004 — Batch settlement format</li>
<li class="deep">RFC-0005 — Slashing extrinsic ABI</li>
<li class="deep">RFC-0006 — Sampling randomness</li>
<li class="deep">RFC-0007 — Customer nonce protocol</li>
<li class="deep">RFC-0008 — Oracle feed</li>
<li class="deep">RFC-0009 — Operator registration</li>
<li class="deep">RFC-0010 — RPC endpoint contract</li>
</ul>
</div>
"""

    parts: list[str] = [cover, toc]
    parts.append("<h1>Part I — Network architecture and rationale</h1>")
    parts.append(render_md(PLAN))
    parts.append('<div style="page-break-before: always"></div>')
    parts.append("<h1>Part II — Cross-team integration RFCs</h1>")
    for rfc in rfcs:
        parts.append('<div style="page-break-before: always"></div>')
        parts.append(render_md(rfc))

    body = "\n".join(parts)
    # Reuse the brand name in copy; replace working "USEFUL" appearing in the plan history with bracketed note
    body = body.replace("USEFUL", "OROG")
    html_doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>Orogen Whitepaper</title>
<style>{CSS}</style></head><body>{body}</body></html>"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html_doc, base_url=str(REPO)).write_pdf(OUT)
    size_kb = OUT.stat().st_size // 1024
    sys.stdout.write(f"wrote {OUT} ({size_kb} KB)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
