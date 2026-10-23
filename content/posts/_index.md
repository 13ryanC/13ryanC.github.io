---
title: "Writing"
description: "Essays, explainers and post-mortems. Informal and not peer reviewed."
summary: "Essays, explainers and post-mortems."

# Pages below are not ready for readers (drafts, deprecated or superseded
# versions, untitled scratch notes). They are left out of every listing
# (Writing, homepage, search, tags, sitemap) and marked noindex, but
# still render at their URLs so existing links keep working.
# To hide a single post instead, add `build: {list: never}` to its front matter.
cascade:
  - build:
      list: never
    params:
      robotsNoIndex: true
    target:
      path: "{/posts/**/drafts/**,/posts/blog/ip_deprecated,/posts/blog/ip_drafting,/posts/blog/ip_with_pending_results,/posts/blog/retracted_*,/posts/blog/linkedinmessage,/posts/blog/problems,/posts/blog/why_multi_awarding_winning_dangerous,/posts/blog/mts,/posts/blog/mvsc,/posts/blog/reduce_compute/**,/posts/idea-to-software/prompt,/posts/idea-to-software/**/chatgpt,/posts/idea-to-software/parnas/content,/posts/idea-to-software/parnas/slug,/posts/mechinterp/sdl,/posts/reckless/**}"

  # Finished posts hidden from listings by choice (31 pages). They still render
  # at their URLs and stay indexable. Delete this block to list them again.
  #   - 5 posts: RLHF failings, quant books, VCs, LLM training field notes,
  #     pre-training feasibility
  #   - 15 Parnas software-engineering posts dated 2025-10-18
  #   - 11 bird posts dated 2025-10-13
  - build:
      list: never
    target:
      path: "{/posts/blog/rlhf_failings,/posts/blog/quant_books,/posts/blog/vc,/posts/blog/llms,/posts/thoughts_pre_training,/posts/idea-to-software/parnas/2025-10-18-*,/posts/blog/birds/*}"
---

{{< browse-links >}}
