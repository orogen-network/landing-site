#!/usr/bin/env node
// Walks dist/ produced by `astro build`, verifies that every <a href="...">
// local link resolves to a static file in dist/. External (http(s)://,
// mailto:) links are skipped.
//
// Usage:   node scripts/lint-links.mjs
// Exits non-zero on broken links.

import { readdirSync, readFileSync, statSync, existsSync } from "node:fs";
import { dirname, join, resolve, relative } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const dist = resolve(here, "..", "dist");

if (!existsSync(dist)) {
  console.error(`dist/ does not exist at ${dist}. Run 'npm run build' first.`);
  process.exit(1);
}

const ALLOWED_PLACEHOLDER_HASHES = new Set();

function walk(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    const st = statSync(p);
    if (st.isDirectory()) walk(p, acc);
    else acc.push(p);
  }
  return acc;
}

const files = walk(dist);
const htmlFiles = files.filter((f) => f.endsWith(".html"));

const hrefRe = /\shref\s*=\s*"([^"#?][^"]*)"/g;
const hashOnlyHrefRe = /\shref\s*=\s*"(#[^"]+)"/g;

let broken = 0;
let checked = 0;

function resolveLocal(href, fromFile) {
  // strip query / fragment
  const clean = href.split("#")[0].split("?")[0];
  if (!clean) return null; // pure-fragment handled separately

  if (
    clean.startsWith("http://") ||
    clean.startsWith("https://") ||
    clean.startsWith("mailto:") ||
    clean.startsWith("tel:") ||
    clean.startsWith("data:")
  ) {
    return null;
  }

  let target;
  if (clean.startsWith("/")) {
    target = join(dist, clean);
  } else {
    target = join(dirname(fromFile), clean);
  }

  // Astro `build.format: "file"` produces /how-it-works.html for /how-it-works.
  // Prefer the .html sibling when it exists, even if a directory with the
  // same name also exists (the directory may simply hold static assets).
  if (existsSync(`${target}.html`)) return `${target}.html`;
  if (existsSync(target)) {
    const st = statSync(target);
    if (st.isDirectory()) {
      const idx = join(target, "index.html");
      if (existsSync(idx)) return idx;
      return null;
    }
    return target;
  }
  return null;
}

for (const file of htmlFiles) {
  const body = readFileSync(file, "utf8");
  // ordinary local links
  for (const m of body.matchAll(hrefRe)) {
    const href = m[1];
    if (
      href.startsWith("http://") ||
      href.startsWith("https://") ||
      href.startsWith("mailto:") ||
      href.startsWith("tel:") ||
      href.startsWith("data:")
    ) {
      continue;
    }
    checked++;
    const resolved = resolveLocal(href, file);
    if (!resolved) {
      broken++;
      console.error(
        `BROKEN: ${relative(dist, file)} -> ${href}`,
      );
    }
  }
  // pure-hash anchors — allow the known placeholders, ignore others (in-page anchors)
  for (const m of body.matchAll(hashOnlyHrefRe)) {
    const href = m[1];
    if (ALLOWED_PLACEHOLDER_HASHES.has(href)) continue;
    // in-page anchor; we do not enforce id-presence in this lint pass
  }
}

if (broken > 0) {
  console.error(`\n${broken} broken local link(s) across ${htmlFiles.length} HTML files.`);
  process.exit(1);
} else {
  console.log(
    `ok: ${checked} local link(s) checked across ${htmlFiles.length} HTML files. all resolved.`,
  );
}
