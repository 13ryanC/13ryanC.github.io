#!/usr/bin/env bash
# -----------------------------------------------------------------
#  reflow-md.sh  —  Hugo-/Markdown re-formatter
#     • Keeps the front-matter block (between the first two '---')
#     • Flattens every paragraph to one physical line
#     • Inserts ONE blank line after sentence-ending punctuation
#       ( . ! ? — optionally wrapped in quotes/brackets) that is
#       followed by a capital letter or an opening quote
#
#  Usage:
#       reflow-md.sh  in.md      > out.md
#       reflow-md.sh  *.md       > merged.md
# -----------------------------------------------------------------

gawk -f - "$@" <<'AWK'
##############################################################################
# Phase 0 – copy the front-matter verbatim (line-by-line mode)               #
##############################################################################
BEGIN {
    RS    = "\n"      # start in normal line mode
    ORS   = "\n"
    fence = 0         # how many --- lines have we seen so far?
}

$0 == "---" {
    ++fence
    print
    if (fence == 2) {            # second fence ends the front-matter
        RS  = ""                 # paragraph mode: blank line = record sep
        ORS = ""                 # we will control spacing manually
    }
    next
}

# still inside front-matter?
fence < 2 { print; next }

##############################################################################
# Phase 1 – paragraph-wise processing                                        #
##############################################################################
{
    gsub(/\n+/, " ", $0)          # step 1: collapse internal newlines

    # step 2: add two NLs after real sentence boundaries
    #          ([.!?] + optional quotes/brackets)  +  space(s)  +  Capital/quote
    $0 = gensub(/([.!?]["'’”)\]]*)[[:space:]]+(["'“”‘’«»(\[]*[[:upper:]])/,
                "\\1\n\n\\2", "g", $0)

    sub(/[[:space:]]+$/, "", $0)  # trim trailing whitespace
    print $0 "\n\n"               # paragraph + one blank line
}
AWK
