---
_build:
  render: never
  list: never
---

# Front Matter & Heading Standards for RLtheory

Documentation of standardized front matter and heading hierarchy requirements for all markdown files in the RLtheory directory.

## Standard Front Matter Format

All markdown files should include the following standardized front matter:

```yaml
---
date: "YYYY-MM-DD"
title: "Descriptive Title"
summary: "Brief description of content"
lastmod: "YYYY-MM-DD"
category: Notes|Plan|Reference
series: ["RL Theory", "Subtopic"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---
```

### Required Fields
- **date**: Creation date in ISO 8601 format (YYYY-MM-DD)
- **title**: Descriptive title matching the document's main heading
- **summary**: Brief 1-2 sentence description of content
- **category**: One of: `Notes`, `Plan`, `Reference`
- **series**: Array of series classifications
- **author**: Content author name

### Recommended Fields
- **lastmod**: Last modification date in ISO 8601 format
- **hero**: Hero image path (standardized to `/assets/images/hero3.png`)
- **image**: Card image path (standardized to `/assets/images/card3.png`)

## Category Standardization

### Valid Categories
- **Notes**: General educational content, tutorials, explanations
- **Plan**: Planning documents, roadmaps, curriculum guides
- **Reference**: Reference materials, taxonomies, external content summaries

### Migration Rules
- `"Tutorial"` → `Notes`
- `"Taxonomy"` → `Reference`
- Remove quotes around category values
- Standardize to unquoted format

## Series Standardization

### Standard Series Values
- **["RL Theory"]**: Core reinforcement learning theory content
- **["RL Theory", "RL Topics"]**: Advanced RL topics
- **["SuttonBarto"]**: Sutton & Barto textbook summaries
- **["MARL"]**: Multi-agent reinforcement learning
- **["MAS"]**: Multi-agent systems
- **["DL Theory"]**: Deep learning theory
- **["Continual Learning"]**: Continual/lifelong learning topics

## Author Field Standards

### Standard Format
```yaml
author: "Bryan Chan"
```

### Common Fixes Applied
- Remove "Author:" prefix: `"Author: Bryan Chan"` → `"Bryan Chan"`
- Standardize non-standard authors: `"ChatGPT"` → `"Bryan Chan"`

## Heading Hierarchy Standards

### Standard Hierarchy
1. **# Document Title** - Should match front matter title
2. **## Major Sections** - Main content sections
3. **### Subsections** - Detailed subsections within major sections
4. **#### Details** - Use sparingly for very specific details

### Rules
- Files must start with `#` (document title) or `##` (major section)
- Never start with `###` or deeper levels
- Don't skip heading levels (e.g., `#` followed by `###`)
- Avoid headings deeper than `####`

### Template Structure
```markdown
---
title: "Document Title"
---

# Document Title
[Brief introduction]

## 1. Major Section
[Content]

### 1.1 Subsection
[Content]

#### 1.1.1 Detail Level (use sparingly)
[Content]

## 2. Next Major Section
[Content]
```

## Validation Script

Use the validation script to check compliance:

```bash
python scripts/validate_frontmatter.py --verbose
```

### Automatic Fixes
The script can automatically fix:
- Category formatting and standardization
- Author prefix removal
- Missing `lastmod` fields
- Standard image paths
- Common title typos

Run with `--fix` flag:
```bash
python scripts/validate_frontmatter.py --fix
```

## Common Issues Fixed

### Front Matter Issues
1. **Category Quotes**: `"Notes"` → `Notes`
2. **Tutorial Category**: `"Tutorial"` → `Notes`
3. **Author Prefix**: `"Author: Bryan Chan"` → `"Bryan Chan"`
4. **Non-standard Authors**: `"ChatGPT"` → `"Bryan Chan"`
5. **Missing Fields**: Added `lastmod`, `hero`, `image` fields
6. **Title Typos**: Fixed "Traeat" → "Treat"

### Heading Issues
1. **Improper Start Levels**: Files starting with `###` fixed to proper hierarchy
2. **Missing Document Titles**: Added `#` titles matching front matter
3. **Skipped Levels**: Fixed `#` → `###` sequences
4. **Inconsistent Numbering**: Standardized subsection numbering

## Files Modified

### High Priority Fixes Applied
- `RL_notes_P3.md`: Fixed typo, category, and images
- `MDPs.md`: Changed category from "Taxonomy" to "Reference"
- `deep_learning_plan1.md`: Removed author prefix
- `topics/PAC-MDP.md`: Added document title, fixed heading hierarchy

### Systematic Changes
- Standardized category values across ~120 files
- Added missing `lastmod` fields where needed
- Normalized author fields
- Fixed heading hierarchy violations in topics files

## Best Practices

### Creating New Content
1. Use the standard front matter template
2. Start with document title (`#`) matching front matter
3. Use logical heading hierarchy
4. Choose appropriate category and series
5. Run validation script before committing

### Editing Existing Content
1. Preserve existing custom fields when possible
2. Update `lastmod` field when making significant changes
3. Maintain consistent heading levels
4. Validate changes with script

---

**Last Updated**: 2025-09-16
**Validation Script**: `scripts/validate_frontmatter.py`
**Status**: Standards implemented and enforced