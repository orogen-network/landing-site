#!/usr/bin/env -S uv run --with markdown --with weasyprint python3
"""Build the OROG MiCA-compliant crypto-asset white paper PDF.

Source:  landing-site/content/whitepaper-mica.md
Output:  landing-site/public/downloads/orogen-mica-whitepaper.pdf

This is the regulatory white paper required under Regulation (EU) 2023/1114
(MiCA) Title II Articles 6, 8 and 9 — distinct from the technical white paper
produced by build-whitepaper.py.

Usage: uv run --with markdown --with weasyprint python3 build-mica-whitepaper.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import markdown
from weasyprint import HTML

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "landing-site" / "content" / "whitepaper-mica.md"
OUT = REPO / "landing-site" / "public" / "downloads" / "orogen-mica-whitepaper.pdf"

CSS = """
@page {
  size: A4;
  margin: 2.5cm 2cm 2.8cm 2cm;
  @bottom-left { content: "OROG · MiCA white paper · v0.1 (draft)"; font-size: 8.5pt; color: #64748b; }
  @bottom-right { content: counter(page) " / " counter(pages); font-size: 8.5pt; color: #64748b; }
}
@page :first { @bottom-left { content: none; } @bottom-right { content: none; } }

body { font-family: "Inter", "Helvetica", "Arial", sans-serif; font-size: 10.5pt; line-height: 1.5; color: #111; }

h1 { font-size: 22pt; color: #0c4a6e; border-bottom: 2px solid #0c4a6e; padding-bottom: 4pt; margin-top: 22pt; page-break-after: avoid; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 15pt; color: #155e75; margin-top: 18pt; page-break-after: avoid; }
h3 { font-size: 12.5pt; color: #164e63; margin-top: 14pt; page-break-after: avoid; }
h4 { font-size: 11pt; color: #1e293b; margin-top: 10pt; page-break-after: avoid; }

p, li { hyphens: auto; text-align: justify; }
strong { color: #0f172a; }
em { color: #334155; }

pre, code { font-family: "JetBrains Mono", "Menlo", "Consolas", monospace; font-size: 8.5pt; }
pre { background: #f1f5f9; padding: 8pt; border-left: 3px solid #0891b2; border-radius: 3px; page-break-inside: avoid; white-space: pre-wrap; }
code { background: #f1f5f9; padding: 1pt 3pt; border-radius: 2px; }

table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 9.5pt; page-break-inside: avoid; }
table th, table td { border: 1px solid #cbd5e1; padding: 4pt 6pt; text-align: left; vertical-align: top; }
table th { background: #e2e8f0; font-weight: 600; }

hr { border: 0; border-top: 1px dashed #94a3b8; margin: 18pt 0; }
blockquote { border-left: 3px solid #cbd5e1; padding-left: 10pt; color: #334155; margin: 8pt 0; }

.cover {
  text-align: center;
  page-break-after: always;
  padding-top: 18%;
  height: 86vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.cover .top { }
.cover h1 { font-size: 44pt; border: none; color: #0c4a6e; margin: 0; }
.cover .sub { font-size: 14pt; color: #334155; margin-top: 18pt; }
.cover .tag { font-size: 11pt; color: #475569; margin-top: 8pt; }
.cover .meta { font-size: 9.5pt; color: #64748b; line-height: 1.6; }
.cover .legal { font-size: 8.5pt; color: #64748b; max-width: 16cm; margin: 0 auto; line-height: 1.45; }
"""

COVER = """
<div class="cover">
  <div class="top">
    <div style="font-size:10.5pt;color:#475569;letter-spacing:0.18em;text-transform:uppercase;">Crypto-asset white paper</div>
    <h1 style="margin-top:18pt;">OROG</h1>
    <div class="sub">Orogen Network Token</div>
    <div class="tag">Verifiable LLM inference, anchored to physical work.</div>
    <div class="meta" style="margin-top:36pt;">
      Issued under Regulation (EU) 2023/1114 (MiCA)<br>
      Title II, Articles 6, 8 and 9<br>
      Form: crypto-asset other than ART or EMT<br><br>
      Version v0.1 (draft) — May 2026<br>
      <code>orogen.network</code><br>
      <code>github.com/orogen-network</code>
    </div>
  </div>
  <div class="legal">
    This crypto-asset white paper has not been approved by any competent authority
    in any Member State of the European Union. The offeror of the crypto-asset
    is solely responsible for the content of this crypto-asset white paper.
  </div>
</div>
"""


def main() -> int:
    if not SRC.exists():
        sys.stderr.write(f"source not found at {SRC}\n")
        return 1

    body_md = SRC.read_text()
    body_html = markdown.markdown(
        body_md,
        extensions=["fenced_code", "tables", "sane_lists", "attr_list", "footnotes"],
    )

    html_doc = (
        f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
        f'<title>OROG — MiCA crypto-asset white paper</title>'
        f'<style>{CSS}</style></head>'
        f'<body>{COVER}{body_html}</body></html>'
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=html_doc, base_url=str(REPO)).write_pdf(OUT)
    size_kb = OUT.stat().st_size // 1024
    sys.stdout.write(f"wrote {OUT} ({size_kb} KB)\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
