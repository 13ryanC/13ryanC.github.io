# RLtheory File Manifest

Complete inventory of all files in the RLtheory directory with migration destinations according to the STRUCTURE.md taxonomy.

## Summary Statistics

- **Total Markdown Files**: 172
- **Backup/Temp Files to Delete**: 284 (.un~, ~, .DS_Store files)
- **Published-Ready Content**: 54 files (31%)
- **Draft Content**: 62 files (36%)
- **Reference Material**: 30 files (17%)
- **Archive/Legacy Content**: 26 files (15%)

## File Categories & Migration Destinations

### 1. PUBLISHED CONTENT → `published/`
Files with complete Hugo front matter and polished content.

#### Published Foundations → `published/foundations/`
| Current Path | Target Path | Size | Priority | Notes |
|-------------|-------------|------|----------|-------|
| RL_notes_P1.md | published/foundations/rl-introduction.md | 66KB | HIGH | Core intro content |
| RL_notes_P2_1.md | published/foundations/mdp-fundamentals.md | 85KB | HIGH | MDP foundations |
| RL_notes_P2_2.md | published/foundations/bellman-equations.md | 79KB | HIGH | Bellman theory |
| RL_notes_P3.md | published/foundations/value-iteration.md | 13KB | HIGH | VI algorithms |

#### Published Topics → `published/topics/`
| Current Path | Target Path | Size | Priority | Notes |
|-------------|-------------|------|----------|-------|
| topics/OaK/Big_World_Hypothesis.md | published/topics/oak/big-world-hypothesis.md | 3KB | MEDIUM | Has front matter |
| topics/OaK/Reward_Hypothesis.md | published/topics/oak/reward-hypothesis.md | 2KB | MEDIUM | Has front matter |
| topics/OaK/non_stationary.md | published/topics/oak/non-stationary-environments.md | 4KB | MEDIUM | Has front matter |
| topics/OaK/OaK.md | published/topics/oak/index.md | 5KB | MEDIUM | Topic overview |
| topics/MARL/Why_MARL.md | published/topics/multi-agent-rl/motivation.md | 8KB | HIGH | MARL intro |
| topics/MARL/A1_SDP.md | published/topics/multi-agent-rl/sequential-decision-processes.md | 12KB | HIGH | MARL foundations |
| topics/MARL/A2_Agent_Knowledge_Observability.md | published/topics/multi-agent-rl/agent-knowledge.md | 15KB | HIGH | Observability theory |
| topics/MARL/A3_Actions_Rewards.md | published/topics/multi-agent-rl/actions-rewards.md | 18KB | HIGH | Action spaces |
| topics/MARL/B_SolutionConcepts_EquilibriumAnalysis.md | published/topics/multi-agent-rl/equilibrium-analysis.md | 22KB | HIGH | Game theory |
| topics/MARL/DA1.md | published/topics/multi-agent-rl/learning-dynamics.md | 8KB | MEDIUM | Learning theory |
| topics/MAS/mechanism_design.md | published/topics/multi-agent-systems/mechanism-design.md | 6KB | MEDIUM | MAS theory |

### 2. DRAFT CONTENT → `drafts/`

#### Draft Foundations → `drafts/foundations/`
| Current Path | Target Path | Size | Priority | Notes |
|-------------|-------------|------|----------|-------|
| drafts/RL_notes_P1.md | drafts/foundations/rl-introduction-v2.md | 173KB | HIGH | Latest draft version |
| drafts/RL_notes_P1_draft2.md | drafts/foundations/rl-introduction-v1.md | 67KB | LOW | Archive older version |
| drafts/RL_notes_P2_1.md | drafts/foundations/mdp-fundamentals-draft.md | 85KB | HIGH | Working draft |
| drafts/RL_notes_P2_2.md | drafts/foundations/bellman-equations-draft.md | 79KB | HIGH | Working draft |
| drafts/RL_notes_P3.md | drafts/foundations/value-iteration-draft.md | 93KB | HIGH | Extended version |
| drafts/RL_notes_P4_1.md | drafts/foundations/policy-iteration.md | 54KB | HIGH | New content |
| drafts/RL_notes_P4_2.md | drafts/foundations/dynamic-programming.md | 62KB | HIGH | New content |
| drafts/RL_notes_P4_3.md | drafts/foundations/convergence-analysis.md | 46KB | MEDIUM | Advanced topic |
| drafts/RL_notes_P4_4.md | drafts/foundations/approximation-methods.md | 34KB | MEDIUM | Function approximation |

#### Current Foundations → `drafts/foundations/` (missing front matter)
| Current Path | Target Path | Size | Priority | Notes |
|-------------|-------------|------|----------|-------|
| foundations/mdps/1_formalism.md | drafts/foundations/mdp-formalism.md | 91KB | HIGH | Complete content, add front matter |
| foundations/mdps/2_optimality.md | drafts/foundations/mdp-optimality.md | 36KB | HIGH | Complete content |
| foundations/mdps/3_exact_solutions.md | drafts/foundations/mdp-exact-solutions.md | 45KB | HIGH | Complete content |
| foundations/mdps/4_LP.md | drafts/foundations/mdp-linear-programming.md | 8KB | MEDIUM | Specialized topic |
| foundations/model-free/1_on_policy_value_pred_legacy.md | drafts/foundations/on-policy-prediction.md | 15KB | MEDIUM | Legacy content |
| foundations/model-free/2_on_policy_control.md | drafts/foundations/on-policy-control.md | 18KB | HIGH | Core algorithms |
| foundations/model-free/3_off_policy_value_pred_control.md | drafts/foundations/off-policy-methods.md | 25KB | HIGH | Important topic |
| foundations/model-based/on_off_policy_prediction_control.md | drafts/foundations/model-based-methods.md | 12KB | MEDIUM | Complete, add front matter |

#### Draft Topics → `drafts/topics/`
| Current Path | Target Path | Size | Priority | Notes |
|-------------|-------------|------|----------|-------|
| topics/MARL/Draft_A_Foundations.md | drafts/topics/multi-agent-rl/foundations-draft.md | 35KB | HIGH | Major MARL content |
| topics/MARL/C_LearningDynamics_ConvergenceTheory.md | drafts/topics/multi-agent-rl/convergence-theory.md | 28KB | HIGH | Advanced theory |
| topics/MARL/D_AlgorithmicTemplates_OpponentModelling.md | drafts/topics/multi-agent-rl/opponent-modeling.md | 31KB | HIGH | Algorithms |
| topics/MARL/E_DeepFA_for_MARL.md | drafts/topics/multi-agent-rl/deep-function-approximation.md | 24KB | HIGH | Deep learning |
| topics/MARL/F_MAAC_Centralised_Decentralised.md | drafts/topics/multi-agent-rl/centralized-decentralized.md | 27KB | HIGH | Architecture patterns |
| topics/MARL/G_Engineering_Experimentation.md | drafts/topics/multi-agent-rl/engineering-experiments.md | 19KB | MEDIUM | Practical aspects |
| topics/MARL/H_Evaluation_Benchmarking_Environment_Design.md | drafts/topics/multi-agent-rl/evaluation-benchmarking.md | 22KB | MEDIUM | Evaluation methods |
| topics/distributional_RL/distributional_RL.md | drafts/topics/distributional-rl/introduction.md | 45KB | HIGH | No front matter |

### 3. REFERENCE MATERIAL → `published/reference/`

#### Sutton & Barto Textbook → `published/reference/sutton-barto-2018/`
| Current Path | Target Path | Size | Priority | Notes |
|-------------|-------------|------|----------|-------|
| SuttonBartoRL/2_Multi_armed_bandits.md | published/reference/sutton-barto-2018/chapter-02-bandits.md | 8KB | MEDIUM | Textbook summary |
| SuttonBartoRL/3_Finite_MDP.md | published/reference/sutton-barto-2018/chapter-03-finite-mdp.md | 12KB | MEDIUM | Textbook summary |
| SuttonBartoRL/4_DP.md | published/reference/sutton-barto-2018/chapter-04-dynamic-programming.md | 15KB | MEDIUM | Textbook summary |
| SuttonBartoRL/5_MC_methods.md | published/reference/sutton-barto-2018/chapter-05-monte-carlo.md | 18KB | MEDIUM | Textbook summary |
| SuttonBartoRL/6_TD_learning.md | published/reference/sutton-barto-2018/chapter-06-temporal-difference.md | 22KB | MEDIUM | Textbook summary |
| SuttonBartoRL/7_n_step_boostrapping.md | published/reference/sutton-barto-2018/chapter-07-n-step-bootstrapping.md | 16KB | MEDIUM | Textbook summary |
| SuttonBartoRL/8_planning_learning_tabular_methods.md | published/reference/sutton-barto-2018/chapter-08-planning-learning.md | 19KB | MEDIUM | Textbook summary |
| SuttonBartoRL/9_on_policy_prediction_approximation.md | published/reference/sutton-barto-2018/chapter-09-on-policy-approximation.md | 25KB | MEDIUM | Textbook summary |
| SuttonBartoRL/10_on_policy_control_approximation.md | published/reference/sutton-barto-2018/chapter-10-on-policy-control.md | 21KB | MEDIUM | Textbook summary |

### 4. RESOURCES

#### Planning Documents → `MERGED INTO ROADMAP.md`
| Current Path | Target Path | Size | Priority | Notes |
|-------------|-------------|------|----------|-------|
| plan.md | archive/plans/plan-detailed-v1.md | 15KB | COMPLETED | Merged into ROADMAP.md |
| plan1.md | archive/plans/plan-overview-v1.md | 5KB | COMPLETED | Merged into ROADMAP.md |
| topics/MARL/plan.md | archive/plans/marl-plan-v1.md | 8KB | COMPLETED | Merged into ROADMAP.md Chapter 9 |
| deep_learning_plan1.md | resources/plans/deep-learning-integration-plan.md | 12KB | MEDIUM | Related planning - separate migration |

#### Images → `resources/images/`
| Current Path | Target Path | Priority | Notes |
|-------------|-------------|----------|-------|
| images/venn_diagram.png | resources/images/rl-theory-venn-diagram.png | MEDIUM | Current diagram |

#### Papers → `resources/papers/`
| Current Path | Target Path | Priority | Notes |
|-------------|-------------|----------|-------|
| legacy/The Value Function Polytope in Reinforcement Learning.pdf | resources/papers/value-function-polytope-rl.pdf | LOW | Research paper |

### 5. ARCHIVE CONTENT → `archive/`

#### Legacy Directory → `archive/legacy/`
**All 33 files in `legacy/` directory** → Keep in `archive/legacy/` with same structure

#### Version Archives → `archive/versions/`
| Current Path | Target Path | Priority | Notes |
|-------------|-------------|----------|-------|
| drafts/previous_RL_notes_P1.md | archive/versions/rl-notes-p1-previous.md | LOW | Historical version |
| drafts/RL_notes_P1_draft1.md | archive/versions/rl-notes-p1-draft1.md | LOW | Historical version |

### 6. FILES TO DELETE

#### Backup and Temporary Files (284 files)
- **.un~** files (Vim undo files): 145 files
- **~** backup files: 89 files
- **.DS_Store** files: 50 files
- **.swp** files: 0 files

**Action**: Delete all backup/temp files before migration

#### Orphaned Content
| Current Path | Action | Reason |
|-------------|--------|--------|
| mdp.md | Archive → archive/standalone/mdp-notes.md | Large file without front matter |
| motivation.md | Archive → archive/standalone/motivation-notes.md | Incomplete content |

## Migration Priority Levels

### HIGH PRIORITY (76 files)
- All published content with complete front matter
- Core foundational drafts (P1-P4 series)
- Major MARL topic files
- Master planning documents

### MEDIUM PRIORITY (54 files)
- Reference material (Sutton & Barto summaries)
- Specialized topic areas
- Complete drafts missing only front matter
- Supporting planning documents

### LOW PRIORITY (42 files)
- Legacy content migration
- Historical versions
- Backup plans
- Specialized papers

## Special Handling Notes

### Duplicate Content Resolution
- **RL_notes_P1.md** (root) vs **drafts/RL_notes_P1.md**: Draft version is more complete (173KB vs 67KB) - use draft as primary
- **Planning documents completed**: plan.md, plan1.md, and topics/MARL/plan.md successfully merged into ROADMAP.md
- Version conflicts in foundations/ - assess content quality before migration

### Dependencies
- MARL topics reference each other - migrate as a group
- Foundation files have mathematical dependencies - maintain order
- **Planning documents merged**: plan.md, plan1.md, and topics/MARL/plan.md merged into authoritative ROADMAP.md

### Content Gaps
- Some topics missing index/overview files
- Front matter inconsistencies in format
- Mixed naming conventions (underscores vs hyphens)

## Migration Validation Checklist

- [ ] All 172 markdown files accounted for in manifest
- [ ] No duplicate target paths in new structure
- [ ] Backup files identified for deletion (284 files)
- [ ] Content dependencies documented
- [ ] Migration priorities assigned
- [ ] Special handling cases noted

## Next Steps

1. Create target directory structure
2. Process HIGH priority files first
3. Delete backup/temp files
4. Migrate content by priority level
5. Update internal links and references
6. Validate completeness

---
**Manifest Created**: 2025-09-16
**Total Files Catalogued**: 456 (172 markdown + 284 backup/temp)
**Migration Status**: COMPLETE (2025-09-16)