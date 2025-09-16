---
date: "2025-07-18"
title: "(1.4) The Linear Programming Formulation of MDPs"
summary: "The Linear Programming Formulation of MDPs"
lastmod: "2025-07-18"
category: "Notes"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# 1. Introduction and Setting

The reinforcement learning problem can be elegantly reframed as a **linear program**, converting the non-linear problem of policy search into a convex optimization problem with linear constraints. This formulation moves the focus from the recursive structure of value functions to a holistic, flow-based view provided by **state occupancy measures**.

## 1.1 Mathematical Setting

**State and Action Spaces**: $(S,\mathcal{B}(S))$ and $(A,\mathcal{B}(A))$ are standard Borel spaces.

**Dynamics**: Given by a probability kernel
$$P(\cdot\mid s,a) := \kappa_S(\cdot|s,a), \quad (s,a) \in S \times A$$

**Reward Function**: Expected one-step reward
$$r(s,a) := \int_{S \times \mathbb{R}} r' \kappa(ds'dr' \mid s,a), \quad |r| \leq R_{\max} < \infty$$

**Parameters**: 
- Discount factor $\gamma \in (0,1)$
- Initial distribution $\mu_0 \in \mathcal{P}(S)$
- Assumption: $(1-\gamma)^{-1}R_{\max} < \infty$ ensures all value functions are bounded

**Notation**:
- $\mathcal{M}_b(S)$ = bounded, real-valued, $\mathcal{B}(S)$-measurable functions
- $\mathcal{M}_+(S \times A)$ = finite, non-negative measures on $S \times A$

# 2. The Primal Linear Program

## 2.1 Bellman Optimality and Half-Spaces

For $v \in \mathcal M_b(S)$, define the Bellman operator difference:

$$
g_{s,a}(v) := r(s,a) + \gamma \int_S v(s') P(ds'|s,a) - v(s)
$$

Bellman optimality requires $g_{s,a}(V_*) \leq 0$ with equality for optimal actions. Each pair $(s,a)$ induces a closed half-space:

$$
H_{s,a}^+ := \{v \in \mathcal M_b(S) \mid g_{s,a}(v) \leq 0\}
$$

## 2.2 Primal Formulation: Optimizing Value Functions

The primal LP seeks the pointwise infimum of the intersection $\bigcap_{s,a} H_{s,a}^+$ by minimizing a strictly positive linear functional:

$$\boxed{
\begin{aligned}
\text{(P)} \quad \min_{v \in \mathcal M_b(S)} &\quad (1-\gamma) \int_S v(s) \mu_0(ds) \newline
\text{subject to} &\quad g_{s,a}(v) \leq 0 \quad \forall (s,a) \in S \times A
\end{aligned}
}$$

**Interpretation**: 
- **Variables**: A function $v(\cdot)$ representing a value function
- **Constraints**: Bellman optimality inequalities for all state-action pairs
- **Feasible region**: Bounded supersolutions of the Bellman equation
- **Objective**: Pushes $v$ down until no component can be reduced without violating constraints

## 2.3 Finite State-Action Case

For finite $S$ and $A$, this becomes:
$$\text{minimize} \quad \sum_{s \in S} \mu_0(s) v(s)$$
subject to:
$$v(s) \geq r(s,a) + \gamma \sum_{s' \in S} p(s'|s,a) v(s') \quad \forall s \in S, a \in A$$

# 3. The Dual Linear Program

## 3.1 Lagrangian Formulation

Attaching non-negative multipliers $\xi \in \mathcal M_+(S \times A)$:

$$
\mathcal L (v,\xi) = (1-\gamma) \int v d\mu_0 + \int_{S \times A} [r + \gamma P v - v(s)] \xi(dsda)
$$

## 3.2 Flow Balance Constraints

Setting the Fréchet derivative in $v$ to zero yields the **flow balance condition**: for all measurable $B \subseteq S$,
$$(1-\gamma) \mu_0(B) = \int_{B \times A} \xi(dsda) - \gamma \int_{S \times A} P(B|s,a) \xi(dsda) \tag{F}$$

This characterizes **discounted state-action occupancy measures**:

$$
\xi(B \times C) = (1-\gamma) \mathbb E_{\mu_0}^\pi \left[ \sum_{t \geq 0} \gamma^t \mathbf 1_{\{S_t \in B, A_t \in C\}} \right]
$$

## 3.3 Dual Formulation: Optimizing Occupancy Measures

$$\boxed{
\begin{aligned}
\text{(D)} \quad \max_{\xi \in \mathcal M_+(S \times A)} &\quad \int_{S \times A} r(s,a) \xi(dsda) \newline
\text{subject to} &\quad \xi \text{ satisfies flow balance (F)}
\end{aligned}
}$$

**Interpretation**:
- **Variables**: A measure $\xi$ representing discounted occupancy
- **Objective**: Total expected discounted reward, linear in the measure
- **Constraints**: Flow conservation ensuring consistency with dynamics

## 3.4 Finite State-Action Case

For finite spaces, find $\rho \in \mathbb{R}^{|S| \times |A|}$ that:
$$\text{maximize} \quad \sum_{s,a} \rho(s,a) r(s,a)$$
subject to:
1. **Flow conservation**: $\sum_a \rho(s',a) - \gamma \sum_{s,a} p(s'|s,a) \rho(s,a) = \mu_0(s') \quad \forall s' \in S$
2. **Non-negativity**: $\rho(s,a) \geq 0 \quad \forall s,a$

# 4. Optimality and Duality

## 4.1 Complementary Slackness

For primal-dual optimal solutions $(v^\ast, \xi^\ast)$:

$$
g_{s,a}(v^\ast) \xi^\ast (dsda) = 0 \quad \text{as measures on } S \times A
$$

**Interpretation**: Every state-action pair visited with positive measure is Bellman-tight (greedy).

## 4.2 Strong Duality

The optimal values of both programs are equal:
$$\max_{\xi} \int r d\xi = \min_v \int v d\mu_0 = J(\pi^*)$$

This provides elegant symmetry:
- **Primal**: Directly optimizes over policies (via occupancy measures) to maximize rewards
- **Dual**: Finds the tightest upper bound on the Bellman equation, yielding the optimal value function

## 4.3 Policy Recovery

From the optimal occupancy measure $\xi^\ast$, recover the optimal policy:

$$
\pi^\ast (a \mid s) = \frac{\xi^\ast (s,a)}{\sum_{a'} \xi^\ast (s,a')}
$$

If the denominator is zero for some state $s$, that state is unreachable under the optimal policy.

## 5. Geometric Interpretation

**Primal Feasible Set**: Intersection of infinitely many closed half-spaces in the Banach lattice $\mathcal{M}_b(S)$; convex and upward-closed.

**Extreme Points**: Correspond to deterministic stationary policies under standard continuity assumptions.

**Policy Iteration**: Pivoting between actions corresponds to moving along edges of this infinite-dimensional polyhedron.

# 6. Computational Complexity

| Approach | Comments |
|----------|----------|
| **Policy Iteration** | Solves linear Fredholm equations; finite convergence for finite spaces |
| **Interior-Point Methods** | $\tilde{O}(\sqrt{N})$ iterations where $N$ = sampled constraints |
| **First-Order Primal-Dual** | $O(\varepsilon^{-2})$ complexity for $\varepsilon$-optimal solutions |

# 7. Extensions and Variants

| Setting | Primal Variables | Constraints | Dual Variables |
|---------|------------------|-------------|----------------|
| **Average-Reward** | Bias function $h$, gain $\rho$ | Stationary flow balance | Stationary distribution |
| **Finite Horizon** | Stage-wise $v_t$ | Block-triangular flow | Stage-wise occupancies $\xi_t$ |
| **Constrained MDP** | Same $v$ | Flow + cost budgets | Lagrange multipliers |
| **Robust MDP** | $v$ + model slacks | Semi-infinite constraints | Adversarial model selection |

# 8. Key Insights

1. **Primal LP (P)** searches over value functions in an infinite-dimensional, upward-closed polyhedron defined by Bellman half-spaces.

2. **Dual LP (D)** searches over discounted occupancy measures with probabilistic flow conservation as the sole constraint.

3. **Complementary slackness** provides algebraic justification for policy improvement rules and modern actor-critic algorithms by equating positive occupancy with Bellman-tightness.

4. This formulation converts the non-linear policy search problem into a convex optimization problem with linear constraints, enabling the use of efficient, well-understood solvers.

5. The duality between value functions and occupancy measures provides deep theoretical insights and forms the basis for advanced reinforcement learning algorithms, including apprenticeship learning and robust MDPs.
