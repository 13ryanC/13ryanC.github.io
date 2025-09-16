#!/usr/bin/env bash
# create_md_from_folder.sh
#
# Usage:
#   ./create_md_from_folder.sh /absolute/or/relative/path/to/target-folder
#
#   Given a target folder laid out as:
#     images/
#     <uuid>_content_list.json
#     <uuid>_origin.pdf
#     full.md
#     layout.json
#
#   the script will
#     1. copy full.md into the current working directory,
#     2. prepend the required YAML front-matter (with the folder’s name in the title),
#     3. rename the file to <target-folder-name>.md.
#
# Notes:
#   • Requires a POSIX-compatible shell with mktemp.
#   • Safe-guards are included for missing arguments and files.

set -euo pipefail

### 1. Validate input ##########################################################
if [[ $# -ne 1 ]]; then
  printf 'Usage: %s <target-folder>\n' "${0##*/}" >&2
  exit 1
fi

target_dir=$1
if [[ ! -d $target_dir ]]; then
  printf 'Error: "%s" is not a directory.\n' "$target_dir" >&2
  exit 1
fi

if [[ ! -f "$target_dir/full.md" ]]; then
  printf 'Error: "%s/full.md" not found.\n' "$target_dir" >&2
  exit 1
fi

### 2. Derive names ############################################################
folder_name=$(basename "$target_dir")              # e.g. my-paper-folder
outfile="${folder_name}.md"                        # e.g. my-paper-folder.md

# Extract the paper’s actual title from the first line of full.md.
# If that line starts with a Markdown “# ” heading, strip it.
paper_title=$(head -n 1 "$target_dir/full.md" | sed -e 's/^#\s*//')

### 3. Copy the source markdown ################################################
cp "$target_dir/full.md" "./$outfile"

### 4. Prepend the YAML front-matter ###########################################
tmp=$(mktemp)
cat <<EOF >"$tmp"
---
date: "$(date +%F)"
title: "${paper_title}"
summary: "errata"
category: Tutorial
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

EOF

cat "./$outfile" >>"$tmp"
mv "$tmp" "./$outfile"

printf 'Created: %s\n' "$(realpath "./$outfile")"
