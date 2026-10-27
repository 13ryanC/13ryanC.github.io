#!/usr/bin/env bash
# Look up GitHub security advisories for every jsDelivr npm package pinned in
# the templates. Needs `gh` (authenticated, or GH_TOKEN set). Exits 1 if any
# pinned version has a known advisory.
set -euo pipefail
cd "$(dirname "$0")/.."

pkgs=$(grep -rhoE --include='*.html' 'cdn\.jsdelivr\.net/npm/[^/"]+@[0-9][^/"]*' layouts \
  | sed 's#cdn.jsdelivr.net/npm/##' | sort -u)
[ -n "$pkgs" ] || { echo "no pinned CDN packages found"; exit 0; }

found=0
for p in $pkgs; do
  hits=$(gh api "/advisories?ecosystem=npm&affects=$p&per_page=50" \
    --jq '.[] | "  \(.ghsa_id) \(.severity): \(.summary)"')
  if [ -n "$hits" ]; then
    echo "$p has known advisories:"; echo "$hits"; found=1
  else
    echo "$p: no known advisories"
  fi
done
exit "$found"
