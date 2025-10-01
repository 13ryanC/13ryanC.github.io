---
_build:
  render: never
  list: never

date: "2025-09-16"
title: "Multi-Agent Module"
summary: "Multi-agent reinforcement learning foundations and advanced topics"
lastmod: "2025-09-16"
category: "Notes"
series: ["RL Theory", "RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# Multi-Agent Module

The multi-agent module now follows a two-track progression: a **Primer** that grounds learners in motivation and modeling basics, and an **Advanced** track focused on algorithmic templates, CTDE design, and deep learning techniques. Supporting materials (drafts, legacy content, images) remain available for historical context and future expansions.

## Tracks at a Glance

### 🔰 Primer (`primer/`)
- Entry point for MARL motivation, modeling assumptions, and environment mechanics
- Sequenced readings covering **Why MARL?**, **Foundations**, **Decision Making Models**, **Agent Knowledge & Observability**, and **Actions & Rewards**
- Provides links to supporting theory in the **Foundations** and **Algorithms** modules

### 🚀 Advanced (`advanced/`)
- Curated selection of CTDE patterns, deep function approximation strategies, and opponent modeling templates
- Assumes proficiency with policy gradients and distributional/value-based deep RL
- Bridges to formal guarantees in the **Theory** module and deployment case studies in **Applications**

## Learning Progression
1. Complete the **Primer** to establish shared vocabulary and conceptual models.
2. Revisit relevant **Foundations** chapters on sequential decision processes and MAS basics.
3. Engage with **Advanced** materials while cross-referencing theoretical results on equilibrium and convergence.
4. Explore drafts and legacy notes for deeper dives or historical perspectives.

## Cross-Module References
- **Foundations**: `../foundations/sequential_decision_processes.md`, `../foundations/MAS/mechanism_design.md`
- **Algorithms**: `../algorithms/sutto-barto/TD_learning.md` – baseline learning dynamics
- **Theory**: `../theory/solution_concepts_equilibrium.md`, `../theory/learning_dynamics_convergence.md`
- **Advanced**: `../advanced/policy_gradients.md`, `../advanced/entropy_regularised_RL.md`
- **Applications**: `../applications/engineering_experimentation.md`, `../applications/evaluation_benchmarking.md`

## Supporting Materials
- **drafts/** – Work-in-progress chapters capturing emerging research directions
- **legacy/** – Original MARL series retained for archival reference
- **images/** – Shared visual assets used across primer and advanced topics

## Next Actions for Contributors
- Align in-progress drafts with either `primer/` or `advanced/` subdirectories
- Update cross-links in downstream modules to target the new structure
- File issues for additional subsections (e.g., cooperative vs. competitive curricula, MARL benchmarks)

Last updated: September 16, 2025
