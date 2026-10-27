#!/usr/bin/env bash
# Security regression checks on the built site. Run after `hugo`:
#   scripts/security-check.sh [public-dir]
# Exits non-zero if any check fails.
set -uo pipefail

DIR="${1:-public}"
fail=0

err() { echo "FAIL: $*"; fail=1; }

[ -d "$DIR" ] || { echo "no build output at $DIR"; exit 2; }

# 1. Every external <script src> must carry an SRI integrity hash.
missing=$(grep -rhoE '<script[^>]*src="?https?://[^>]*>' "$DIR" --include='*.html' \
  | grep -v 'integrity=' | sort -u)
[ -z "$missing" ] || err "external script without integrity:"$'\n'"$missing"

# 2. External script URLs must pin an exact version (no @latest, @3, @3.2).
floating=$(grep -rhoE '<script[^>]*src="?https?://[^ ">]+' "$DIR" --include='*.html' \
  | grep -oE 'https?://[^ ">]+' | grep -E '@latest|@[0-9]+(\.[0-9]+)?/' | sort -u)
[ -z "$floating" ] || err "external script with floating version:"$'\n'"$floating"

# 3. Scripts may only come from this site or jsDelivr.
origins=$(grep -rhoE '<script[^>]*src="?https?://[^/" >]+' "$DIR" --include='*.html' \
  | grep -oE 'https?://[^/" >]+$' | grep -viE '^https://(cdn\.jsdelivr\.net|13ryanc\.github\.io)$' | sort -u)
[ -z "$origins" ] || err "script from unexpected origin:"$'\n'"$origins"

# 4. Every page that ships a <head> must ship the CSP (Hugo's script-free
#    meta-refresh redirect stubs, e.g. page/1/, are exempt).
nocsp=$(grep -rLE 'http-equiv="?Content-Security-Policy' "$DIR" --include='*.html' \
  | xargs grep -lE '<head' 2>/dev/null | xargs grep -LE 'http-equiv="?refresh' 2>/dev/null | head -5)
[ -z "$nocsp" ] || err "page without CSP meta tag (first 5):"$'\n'"$nocsp"

# 5. No personal email or machine identifiers in published files.
pii=$(grep -rlIiE 'channokman16@|MacBook-Pro\.local|/Users/[a-z0-9]+/' "$DIR" | head -5)
[ -z "$pii" ] || err "personal identifier in published files:"$'\n'"$pii"

# 6. No obvious secrets in published files.
secrets=$(grep -rlIE 'AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9]{36}|github_pat_[A-Za-z0-9_]{20,}|sk-ant-[A-Za-z0-9-]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY' "$DIR" | head -5)
[ -z "$secrets" ] || err "possible secret in published files:"$'\n'"$secrets"

[ "$fail" -eq 0 ] && echo "security-check: all checks passed ($DIR)"
exit "$fail"
