#!/usr/bin/env bash
set -euo pipefail
OWNER="${1:-MuhamedZanabal}"
REPO="${2:-bahrain-brick-assets}"
VISIBILITY="${3:-private}"

if command -v gh >/dev/null 2>&1; then
  gh auth status
  gh repo create "$OWNER/$REPO" --"$VISIBILITY" --source=. --remote=origin --push
else
  cat >&2 <<EOF
GitHub CLI is not installed. Create an empty repository named $OWNER/$REPO, then run:
  git remote add origin https://github.com/$OWNER/$REPO.git
  git push -u origin main
  git push -u origin work/bahrain-brick-complete-asset-system-v1
EOF
  exit 2
fi
