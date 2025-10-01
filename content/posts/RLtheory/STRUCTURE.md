---
_build:
  render: never
  list: never
---

# RLtheory Directory Structure

This document defines the canonical directory taxonomy for organizing all reinforcement learning theory content.

## Top-Level Directory Structure

```
published/           # Ready-to-publish content with complete Hugo front matter
├── foundations/     # Core RL concepts and mathematical foundations
├── topics/          # Advanced topics and specialized areas
└── reference/       # External material summaries (books, papers)

drafts/             # Work-in-progress content
├── foundations/    # Draft foundational content
├── topics/         # Draft topic content
└── scratch/        # Quick notes and temporary work

resources/          # Supporting materials
├── images/         # All image files (PNG, JPG, diagrams)
├── papers/         # PDF papers and documents
└── plans/          # Planning and roadmap documents

archive/            # Historical content and backups
├── legacy/         # Old versions and deprecated content
└── versions/       # Previous iterations of content
```

## Content Categorization Rules

### Published Content (`published/`)
**Criteria:**
- Complete Hugo front matter (date, title, summary, category, author)
- Polished content ready for publication
- Proper mathematical notation and formatting
- Peer-reviewed or self-reviewed quality

**Examples:**
- `published/topics/multi-agent-rl/nash-equilibrium.md`
- `published/foundations/mdps/bellman-equations.md`

### Draft Content (`drafts/`)
**Criteria:**
- Work-in-progress content
- Missing or incomplete front matter
- Rough notes, partial sections, brainstorming
- Content undergoing active development

**Examples:**
- `drafts/topics/distributional-rl/quantile-regression.md`
- `drafts/scratch/idea-notes-2024-09-16.md`

### Resource Content (`resources/`)
**Images:** All visual content (PNG, JPG, SVG, diagrams)
- Use descriptive names: `bellman-backup-diagram.png` not `image1.png`
- Organize by topic: `resources/images/mdps/`, `resources/images/policy-gradients/`

**Papers:** PDF files and external documents
- Author-year format: `sutton-barto-2018-rl-introduction.pdf`
- Topic-based subdirectories: `resources/papers/multi-agent/`, `resources/papers/function-approximation/`

**Plans:** Planning documents, roadmaps, meta-content
- Clear descriptive names: `multi-agent-rl-learning-plan.md`
- Date prefixes for time-sensitive plans: `2024-09-rl-foundations-roadmap.md`

### Archive Content (`archive/`)
**Legacy:** Old versions and deprecated content
- Preserve original structure for reference
- Add deprecation notices in README files

**Versions:** Previous iterations of specific content
- Use version suffixes: `bellman-equations-v1.md`, `bellman-equations-v2.md`
- Include migration notes explaining changes

## Naming Conventions

### Directories
- Use kebab-case: `multi-agent-rl`, `value-iteration`
- Descriptive over abbreviated: `reinforcement-learning` not `rl`
- Consistent hierarchy: `foundations/` before `topics/`

### Files
- Use kebab-case for markdown files
- Descriptive names reflecting content: `policy-gradient-theorem.md`
- Avoid generic names: Use `temporal-difference-learning.md` not `notes.md`
- Series numbering: `foundations-mdp-1-definitions.md`, `foundations-mdp-2-value-functions.md`

### Hugo Front Matter Requirements (Published Content)
Required fields:
```yaml
---
date: "YYYY-MM-DD"
title: "Descriptive Title"
summary: "Brief description of content"
category: "Notes" | "Plan" | "Reference"
series: ["Series Name", "Subseries"]
author: "Author Name"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
lastmod: "YYYY-MM-DD" (when updated)
---
```

## Migration Mapping Strategy

### Current → Target Structure

**Root Level Files:**
- `RL_notes_P*.md` → `published/foundations/` (if complete) or `drafts/foundations/`
- `plan*.md` → `resources/plans/`
- `mdp.md`, `MDPs.md` → `published/foundations/mdps/`

**Current Directories:**
- `topics/` → `published/topics/` (content with front matter) + `drafts/topics/` (incomplete)
- `foundations/` → `published/foundations/` (reviewed content) + `drafts/foundations/` (WIP)
- `SuttonBartoRL/` → `published/reference/sutton-barto-2018/`
- `drafts/` → `archive/versions/` (old drafts) + `drafts/` (active work)
- `legacy/` → `archive/legacy/`
- `images/` → `resources/images/`

**Content Type Identification:**
1. **Has Hugo front matter** → `published/`
2. **Work in progress** → `drafts/`
3. **PDF/images** → `resources/`
4. **Old versions/backups** → `archive/`

## Success Criteria Checklist

- [ ] All content types have designated homes
- [ ] Clear rules for published vs. draft classification
- [ ] Consistent naming conventions established
- [ ] Migration path defined for each existing file
- [ ] Resource organization (images, PDFs) planned
- [ ] Archive strategy for legacy content defined
- [ ] Hugo front matter requirements documented

## Implementation Notes

This taxonomy prioritizes:
1. **Content maturity** (published vs. draft)
2. **Content type** (notes vs. resources vs. archive)
3. **Subject organization** (foundations vs. specialized topics)
4. **Discoverability** through consistent naming

The structure supports both content creation workflows and end-user navigation while maintaining clear boundaries between different content lifecycle stages.