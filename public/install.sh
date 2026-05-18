#!/usr/bin/env bash
# Orogen wallet-cli installer (Linux x86-64).
# Verifies the SHA-256 from the published SHA256SUMS and installs to ~/.local/bin/wallet-cli.
#
# TRUST MODEL — READ BEFORE PIPING TO sh.
# This installer fetches the tarball + SHA256SUMS from the SAME origin and
# verifies `sha256sum -c`. That defends against in-transit corruption and
# random-CDN tampering, but NOT against a compromise of the origin itself
# (orogen.network) — an attacker with write access to public/downloads/
# can replace both files coherently and the check will still pass.
#
# For high-assurance / production-operator use:
#   - Verify the binary against the foundation release key
#     (https://orogen.network/keys/release.pub) BEFORE running it.
#   - Cross-check the GitHub Release SHA256SUMS at
#     https://github.com/orogen-network/chain-node/releases — these are
#     attested by GitHub's audit log and require multi-party push access.
#
# TODO: ship a detached signature (`SHA256SUMS.asc` via the foundation key,
# or sigstore `*.sig` + `*.pem`) alongside the tarball and have this script
# verify it with a pinned public key embedded below. Tracked in
# security-audit/fixes-05-frontends.md (Fix 6).

set -euo pipefail

VERSION="${OROGEN_VERSION:-0.1.0}"
BASE="${OROGEN_BASE_URL:-https://orogen.network/downloads}"
PREFIX="${OROGEN_PREFIX:-$HOME/.local}"
ARTIFACT="wallet-cli-linux-x64-${VERSION}.tar.gz"

cat <<'BANNER' >&2
─────────────────────────────────────────────────────────────────────────
  Orogen wallet-cli installer
  Trust model: SHA-256 against same-origin SHA256SUMS (transport-only).
  Foundation-signed releases (.sig) verification is COMING; for now,
  high-assurance users should verify the binary signature manually
  against the public key at https://orogen.network/keys/release.pub.
─────────────────────────────────────────────────────────────────────────
BANNER

mkdir -p "$PREFIX/bin"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
cd "$tmp"

echo "→ downloading $BASE/$ARTIFACT"
curl -fsSL "$BASE/$ARTIFACT" -o "$ARTIFACT"
curl -fsSL "$BASE/SHA256SUMS" -o SHA256SUMS

echo "→ verifying SHA-256 (same-origin checksum — see TRUST MODEL above)"
grep " $ARTIFACT$" SHA256SUMS | sha256sum -c -

echo "→ extracting + installing to $PREFIX/bin/wallet-cli"
tar -xzf "$ARTIFACT"
install -m 0755 "wallet-cli-linux-x64-${VERSION}/wallet-cli" "$PREFIX/bin/wallet-cli"

echo
echo "Installed wallet-cli $VERSION to $PREFIX/bin/wallet-cli"
echo "Add $PREFIX/bin to your PATH if it's not already."
echo "Try: wallet-cli --help"
