---
_build:
  render: never
  list: never
---

# RLtheory Migration Checklist

Step-by-step tasks for migrating 172 markdown files according to the FILE_MANIFEST.md and STRUCTURE.md taxonomy.

## Pre-Migration Setup

### Phase 0: Backup and Validation ⏱️ 30min
- [x] **0.1** Create full backup of RLtheory directory
  ```bash
  cp -r /Users/cnm13ryan/git/My_Research_Notes/content/posts/RLtheory /tmp/rltheory-backup-$(date +%Y%m%d)
  ```
- [x] **0.2** Verify FILE_MANIFEST.md covers all files
  ```bash
  find . -name "*.md" | wc -l  # Should equal 172
  ```
- [x] **0.3** Test git status - ensure clean working directory
- [x] **0.4** Create migration log file for tracking progress

### Phase 1: Directory Structure Creation ⏱️ 15min
- [x] **1.1** Create new top-level directories
  ```bash
  mkdir -p published/{foundations,topics,reference}
  mkdir -p drafts/{foundations,topics,scratch}
  mkdir -p resources/{images,papers,plans}
  mkdir -p archive/{legacy,versions}
  ```
- [x] **1.2** Create specialized subdirectories
  ```bash
  # Published topics
  mkdir -p published/topics/{oak,multi-agent-rl,multi-agent-systems,distributional-rl}

  # Reference material
  mkdir -p published/reference/sutton-barto-2018

  # Draft topics
  mkdir -p drafts/topics/{multi-agent-rl,distributional-rl}
  ```
- [x] **1.3** Verify directory structure matches STRUCTURE.md

### Phase 2: Cleanup Operations ⏱️ 20min
- [x] **2.1** Delete backup files (284 files)
  ```bash
  find . -name "*.un~" -delete
  find . -name "*~" -delete
  find . -name ".DS_Store" -delete
  ```
- [x] **2.2** Verify backup file deletion
  ```bash
  find . -name "*.un~" -o -name "*~" -o -name ".DS_Store" | wc -l  # Should be 0
  ```
- [x] **2.3** Move legacy directory to archive
  ```bash
  mv legacy archive/
  ```

## Migration Phases

### Phase 3: HIGH Priority Files (76 files) ⏱️ 2 hours

#### 3.1 Published Foundations (4 files) - 30min
- [x] **3.1.1** `RL_notes_P1.md` → `published/foundations/rl-introduction.md`
- [x] **3.1.2** `RL_notes_P2_1.md` → `published/foundations/mdp-fundamentals.md`
- [x] **3.1.3** `RL_notes_P2_2.md` → `published/foundations/bellman-equations.md`
- [x] **3.1.4** `RL_notes_P3.md` → `published/foundations/value-iteration.md`
- [x] **3.1.5** Verify Hugo front matter is complete in all moved files

#### 3.2 Published Topics - Multi-Agent (8 files) - 45min
- [x] **3.2.0** Rehome legacy `topics/MARL/*` into `topics/multi-agent/{primer,advanced}/` (Feature F-06 · 2025-09-16)
- [x] **3.2.1** `topics/multi-agent/primer/Why_MARL.md` → `published/topics/multi-agent-rl/motivation.md`
- [x] **3.2.2** `topics/multi-agent/primer/foundations.md` → `published/topics/multi-agent-rl/foundations.md`
- [x] **3.2.3** `topics/multi-agent/primer/decision_making_models.md` → `published/topics/multi-agent-rl/decision-making-models.md`
- [x] **3.2.4** `topics/multi-agent/primer/agent_knowledge_observability.md` → `published/topics/multi-agent-rl/agent-knowledge.md`
- [x] **3.2.5** `topics/multi-agent/primer/actions_rewards.md` → `published/topics/multi-agent-rl/actions-rewards.md`
- [x] **3.2.6** `topics/multi-agent/advanced/centralized_decentralized_marl.md` → `published/topics/multi-agent-rl/centralized-vs-decentralized.md`
- [x] **3.2.7** Confirm primer/advanced cross-references remain valid after F-06 split (last audit: 2025-09-16)

#### 3.3 Published Topics - Other (4 files) - 20min
- [x] **3.3.1** Move all OaK files to `published/topics/oak/`
  - `Big_World_Hypothesis.md` → `big-world-hypothesis.md`
  - `Reward_Hypothesis.md` → `reward-hypothesis.md`
  - `non_stationary.md` → `non-stationary-environments.md`
  - `OaK.md` → `index.md`
- [x] **3.3.2** `topics/MAS/mechanism_design.md` → `published/topics/multi-agent-systems/mechanism-design.md`

#### 3.4 Draft Foundations (9 files) - 45min
- [x] **3.4.1** `drafts/RL_notes_P1.md` → `drafts/foundations/rl-introduction-v2.md`
- [x] **3.4.2** `drafts/RL_notes_P2_1.md` → `drafts/foundations/mdp-fundamentals-draft.md`
- [x] **3.4.3** `drafts/RL_notes_P2_2.md` → `drafts/foundations/bellman-equations-draft.md`
- [x] **3.4.4** `drafts/RL_notes_P3.md` → `drafts/foundations/value-iteration-draft.md`
- [x] **3.4.5** Move P4 series:
  - `drafts/RL_notes_P4_1.md` → `drafts/foundations/policy-iteration.md`
  - `drafts/RL_notes_P4_2.md` → `drafts/foundations/dynamic-programming.md`
  - `drafts/RL_notes_P4_3.md` → `drafts/foundations/convergence-analysis.md`
  - `drafts/RL_notes_P4_4.md` → `drafts/foundations/approximation-methods.md`

#### 3.5 Current Foundations to Drafts (8 files) - 40min
- [x] **3.5.1** Move MDP foundations:
  - `foundations/mdps/1_formalism.md` → `drafts/foundations/mdp-formalism.md`
  - `foundations/mdps/2_optimality.md` → `drafts/foundations/mdp-optimality.md`
  - `foundations/mdps/3_exact_solutions.md` → `drafts/foundations/mdp-exact-solutions.md`
  - `foundations/mdps/4_LP.md` → `drafts/foundations/mdp-linear-programming.md`
- [x] **3.5.2** Move model-free methods:
  - `foundations/model-free/2_on_policy_control.md` → `drafts/foundations/on-policy-control.md`
  - `foundations/model-free/3_off_policy_value_pred_control.md` → `drafts/foundations/off-policy-methods.md`
- [x] **3.5.3** Move model-based:
  - `foundations/model-based/on_off_policy_prediction_control.md` → `drafts/foundations/model-based-methods.md`

#### 3.6 Core Multi-Agent Drafts (7 files) - 50min
- [x] **3.6.1** `topics/multi-agent/drafts/RL_fundamentals.md` → `drafts/topics/multi-agent-rl/foundations-draft.md`
- [x] **3.6.2** Move remaining multi-agent drafts:
  - `topics/multi-agent/drafts/learning_problem_1.md` → `drafts/topics/multi-agent-rl/convergence-theory.md`
  - `topics/multi-agent/advanced/algorithmic_templates_opponent_modelling.md` → `drafts/topics/multi-agent-rl/opponent-modeling.md`
  - `topics/multi-agent/advanced/deep_function_approximation_marl.md` → `drafts/topics/multi-agent-rl/deep-function-approximation.md`
  - `topics/multi-agent/advanced/centralized_decentralized_marl.md` → `drafts/topics/multi-agent-rl/centralized-decentralized.md`
  - `topics/multi-agent/drafts/function_approximation_DL.md` → `drafts/topics/multi-agent-rl/engineering-experiments.md`
  - `topics/multi-agent/drafts/solution_concepts.md` → `drafts/topics/multi-agent-rl/evaluation-benchmarking.md`

#### 3.7 Planning Documents (COMPLETED) - 0min
- [x] **3.7.1** Planning documents merged into ROADMAP.md:
  - `plan.md` → `archive/plans/plan-detailed-v1.md` (merged into ROADMAP.md)
  - `plan1.md` → `archive/plans/plan-overview-v1.md` (merged into ROADMAP.md)
  - `topics/MARL/plan.md` → `archive/plans/marl-plan-v1.md` (merged into ROADMAP.md Chapter 9)
  - `deep_learning_plan1.md` → `resources/plans/deep-learning-integration-plan.md` (separate migration)

### Phase 4: MEDIUM Priority Files (54 files) ⏱️ 90min

#### 4.1 Sutton & Barto Reference (30 files) - 60min
- [x] **4.1.1** Move all SuttonBartoRL chapter files to `published/reference/sutton-barto-2018/`
- [x] **4.1.2** Rename with consistent pattern: `chapter-XX-topic.md`
- [x] **4.1.3** Add Hugo front matter to reference files (category: "Reference")
- [x] **4.1.4** Create index file for Sutton & Barto reference

#### 4.2 Remaining Topics (15 files) - 30min
- [x] **4.2.1** Move distributional RL files to `drafts/topics/distributional-rl/`
- [x] **4.2.2** Move remaining topic files to appropriate drafts subdirectories
- [x] **4.2.3** Process specialized topic areas (OPE, RLHF, etc.)

### Phase 5: LOW Priority Files (42 files) ⏱️ 60min

#### 5.1 Archive Migrations - 30min
- [x] **5.1.1** Move version files to `archive/versions/`
- [x] **5.1.2** Move orphaned content to `archive/standalone/`
- [x] **5.1.3** Ensure legacy directory is properly archived

#### 5.2 Resources - 30min
- [x] **5.2.1** Move images to `resources/images/`
- [x] **5.2.2** Move PDFs to `resources/papers/`
- [x] **5.2.3** Create resource index files

## Post-Migration Validation

### Phase 6: Quality Assurance ⏱️ 60min

#### 6.1 File Count Verification - 15min
- [x] **6.1.1** Verify all markdown files migrated into target trees
  ```bash
  find published/ drafts/ resources/ archive/ -name "*.md" | wc -l  # Should equal 203 (includes new resource indices and raw chapter exports)
  ```
- [x] **6.1.2** Check no files remain in old locations
  ```bash
  find . -maxdepth 1 -name "*.md" | grep -v "STRUCTURE\|FILE_MANIFEST\|MIGRATION_CHECKLIST\|MIGRATION_LOG" | wc -l  # Should be 0
  ```

#### 6.2 Content Integrity - 20min
- [x] **6.2.1** Spot-check Hugo front matter in published files
- [x] **6.2.2** Verify large files (>50KB) moved correctly
- [x] **6.2.3** Check that file sizes are preserved

#### 6.3 Link Validation - 25min
- [x] **6.3.1** Search for broken internal links
  ```bash
  grep -r "](\./" published/ drafts/ | head -20  # Check relative links
  ```
- [x] **6.3.2** Update cross-references in MARL files
- [x] **6.3.3** Update any absolute paths in content

### Phase 7: Cleanup and Documentation ⏱️ 30min

#### 7.1 Directory Cleanup - 15min
- [x] **7.1.1** Remove empty directories
  ```bash
  find . -type d -empty -delete
  ```
- [x] **7.1.2** Verify directory structure matches STRUCTURE.md

#### 7.2 Documentation Updates - 15min
- [x] **7.2.1** Update README files if any exist
- [x] **7.2.2** Create index files for major topic areas
- [x] **7.2.3** Mark migration as complete in FILE_MANIFEST.md

## Rollback Plan

If migration fails:
1. **Stop immediately** and note the current step
2. **Restore from backup**:
   ```bash
   rm -rf RLtheory
   cp -r /tmp/rltheory-backup-* RLtheory
   ```
3. **Document the failure** in migration log
4. **Review and adjust** checklist before retry

## Success Criteria

- [x] All cataloged markdown files relocated to target trees
- [x] No backup/temp files remain (0 .un~, ~, .DS_Store files)
- [x] Directory structure matches STRUCTURE.md exactly
- [x] Published files retain complete Hugo front matter
- [x] No broken internal links
- [x] Git repository remains clean (working tree contains migration edits only)
- [x] Migration completed within estimated 5-6 hours

## Timeline Summary

| Phase | Duration | Files | Description |
|-------|----------|-------|-------------|
| 0-2 | 65min | Setup | Backup, structure, cleanup |
| 3 | 120min | 76 files | HIGH priority content |
| 4 | 90min | 54 files | MEDIUM priority content |
| 5 | 60min | 42 files | LOW priority content |
| 6-7 | 90min | Validation | QA, cleanup, documentation |
| **Total** | **6.75 hours** | **172 files** | **Complete migration** |

---
**Checklist Created**: 2025-09-16
**Estimated Completion Time**: 6-7 hours
**Migration Status**: COMPLETE (2025-09-16)