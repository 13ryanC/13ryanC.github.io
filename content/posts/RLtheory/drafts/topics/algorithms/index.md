---
_build:
  render: never
  list: never

date: "2025-09-16"
title: "Algorithms Module"
summary: "Core RL algorithms from tabular to function approximation"
lastmod: "2025-09-16"
category: "Notes"
series: ["RL Theory", "RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# Algorithms Module

This module covers the essential algorithms that form the backbone of reinforcement learning, from classical tabular methods to modern function approximation approaches.

## Learning Progression

### 1. Tabular Methods (Sutton-Barto Foundations)
- **sutto-barto/** - Classical RL algorithms
  - **Monte Carlo Methods** (`MC_methods.md`)
    - First-visit and every-visit MC
    - MC prediction and control
    - Importance sampling

  - **Temporal Difference Learning** (`TD_learning.md`)
    - TD(0), SARSA, Q-learning
    - On-policy vs off-policy methods
    - Bootstrapping concepts

  - **N-Step Bootstrapping** (`n_step_bootstrapping.md`)
    - Bridging MC and TD methods
    - N-step TD prediction and control
    - Forward and backward views

  - **Eligibility Traces** (`eligibility_traces.md`)
    - TD(λ) algorithms
    - Trace-based updates
    - Implementation considerations

### 2. Function Approximation
- Value function approximation
- Policy gradient methods (see Advanced module)
- Deep RL algorithms (see Advanced module)

## Prerequisites
- **Foundations Module** completed
- Understanding of MDPs and Bellman equations
- Basic programming concepts

## Next Steps
After mastering these algorithms, consider:
- **Theory Module** - Understanding convergence guarantees
- **Advanced Module** - Policy gradients and modern methods
- **Applications Module** - Practical implementation considerations

## Key Concepts
1. **Prediction vs Control**: Learning value functions vs finding optimal policies
2. **On-policy vs Off-policy**: Learning from the policy being improved vs learning from different policies
3. **Bootstrapping**: Using estimates to update estimates
4. **Exploration vs Exploitation**: Balancing learning and performance

## Implementation Notes
- Start with tabular implementations before moving to function approximation
- Understand the bias-variance tradeoffs in different methods
- Pay attention to convergence conditions and practical considerations