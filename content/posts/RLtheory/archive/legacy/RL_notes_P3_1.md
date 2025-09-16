---
date: "2025-06-30"
title: "(Part 3.1) Personal Notes on the Foundations of Reinforcement Learning"
summary: "Aim to provide more insight on RL foundations for beginners"
category: "Tutorial"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
sources:
  - title: "Lecture 1 (2022-01-05)"
    url: "http://www.youtube.com/watch?v=rjwxqcVrVws"
  - title: "Lecture 1 (2021-01-12)"
    url: "http://www.youtube.com/watch?v=0oJmSULoj3I"
---

## Organising principle: the hermeneutic lattice ≤ᴴ

Eight **clusters** $C_1\!\prec C_2\!\prec\cdots\!\prec C_8$ form a **partial order of plausibility**: each cluster supplies the minimal conceptual ground on which every later cluster relies.  Arrows point strictly forward unless otherwise stated.

```
C₁ → C₂ → C₃ → C₄ → C₅ → C₆ → C₈
                ↘︎         ↘︎
                  C₇ ───────┘
```

---

### C₁ Primitive ingredients of a finite Markov Decision Process (MDP)

| symbol                | definition                                               | notes                                                                      |   |                                             |
| --------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------- | - | ------------------------------------------- |
| $S$                   | finite set of **states**                                 | (                                                                          | S | <\infty) needed for algorithmic complexity. |
| $A(s)\subseteq A$     | finite set of **actions** available in state $s$         | Heterogeneous action sets allowed.                                         |   |                                             |
| $P_{sa s'}$           | **transition kernel**: $\Pr[s_{t+1}=s'\mid s_t=s,a_t=a]$ | $\sum_{s'}P_{sa s'}=1$.                                                    |   |                                             |
| $R(s,a)$              | expected **one‑step reward**                             | Rewards may be unbounded, but most theorems require $\|R\|_\infty<\infty$. |   |                                             |
| $\gamma\in[0,1)$      | **discount factor**                                      | Defines *effective horizon* $H_\gamma:=1/(1-\gamma)$.                      |   |                                             |
| $\pi_t(a\!\mid\!h_t)$ | **general policy** (history‑dependent stochastic)        | History $h_t=(s_0,a_0,\dots,s_t)$.                                         |   |                                             |
| $\pi(a\!\mid\!s)$     | **memoryless policy**                                    | Uses current state only.                                                   |   |                                             |
| $\mu:S\to A$          | **deterministic memoryless policy**                      | Single action per state.                                                   |   |                                             |

*Dependency rationale:* Without $(S,A,P,R,\gamma)$ no value, theorem, or algorithm can be stated.

---

### C₂ Value‑oriented abstractions

| name                              | formula                                                              | key properties                                       |
| --------------------------------- | -------------------------------------------------------------------- | ---------------------------------------------------- |
| **Return**                        | $G_t=\sum_{k\ge0}\gamma^k R(s_{t+k},a_{t+k})$                        | Finite a.s. when $\gamma<1$ & $\|R\|_\infty<\infty$. |
| **Value of π**                    | $v^{\pi} = (I-\gamma P^{\pi})^{-1}R^{\pi}$                           | Solves linear system.                                |
| **Action value**                  | $q^{\pi}(s,a)=R(s,a)+\gamma\sum_{s'}P_{sa s'}v^{\pi}(s')$            | —                                                    |
| **Policy‑evaluation operator**    | $T^{\pi}v = R^{\pi}+\gamma P^{\pi}v$                                 | γ‑contraction; affine.                               |
| **Deterministic‑action operator** | $T^{(a)}v := R^{(a)} + \gamma P^{(a)}v$                              | $T=\max_{a}T^{(a)}$.                                 |
| **Bellman optimality operator**   | $Tv(s)=\max_a T^{(a)}v(s)$                                           | γ‑contraction in $\|\cdot\|_\infty$.                 |
| **Greedy operator**               | $Gv(s)=\arg\max_{a}T^{(a)}v(s)$                                      | Set‑valued if ties.                                  |
| **Policy‑improvement map**        | $I(\pi)=Gv^{\pi}$                                                    | Guarantees monotone value increase.                  |
| **Value‑difference identity**     | $v^{\pi'}-v^{\pi}=(I-\gamma P^{\pi'})^{-1}(T^{\pi'}v^{\pi}-v^{\pi})$ | Basis for continuity bounds.                         |
| **Monotonicity**                  | $v\le w\Rightarrow T^{\pi}v\le T^{\pi}w$ & $Tv\le Tw$                | —                                                    |

**∞‑norm “bottleneck” (formal proof sketch).**
For any vectors $v,w$,

$$
|Tv(s)-Tw(s)|=\bigl|\max_a f_a-\max_a g_a\bigr|
\le\max_a |f_a-g_a|
\le \gamma\|v-w\|_\infty,
$$

where $f_a:=T^{(a)}v(s)$.  The crucial *max–max* inequality fails in p‑norms $p<\infty$.

---

### C₃ Fixed‑point & sufficiency theorems

1. **Banach fixed‑point theorem** (metric contraction).
   *Exceptions:* fails when β ≥ 1, metric space incomplete, or reward unbounded → no complete normed space.

2. **Contraction of $T$.** $T$ is a γ‑contraction in ∞‑norm.

3. **Fundamental theorem of MDPs.**
   A deterministic memoryless policy $\mu^{\*}$ achieves the optimum: $v^{\mu^{\*}}=v^{\*}$.
   *Dynamic‑programming viewpoint:* Bellman’s principle of optimality implies that local greedy choices in every state suffice for global optimality.

---

### C₄ Planning algorithms

| step                            | algorithm                                                      | pseudocode & notes                                                                                                                                  |   |                         |   |           |
| ------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | - | ----------------------- | - | --------- |
| **Policy Evaluation (PE)**      | solve $(I-\gamma P^{\pi})v=R^{\pi}$.                           | Gaussian elimination O(                                                                                                                             | S | ³) or iterative sweeps. |   |           |
| **Value Iteration (VI)**        | repeat $v_{k+1}=Tv_k$.                                         | *Purpose:* simplest DP scheme producing ε‑optimal policies **without** linear solves.  Stop when $\|v_{k+1}-v_k\|_\infty\le \frac{ε(1-\gamma)}{2}$. |   |                         |   |           |
| **Policy Improvement (Greedy)** | $\pi_{k+1}=Gv_k$.                                              | Tie‑break deterministically.                                                                                                                        |   |                         |   |           |
| **Policy Iteration (PI)**       | loop PE → Greedy until policy stable.                          | Each sweep strictly improves value; ≤                                                                                                               | A | ^{                      | S | } sweeps. |
| **n‑step VI / finite horizon**  | perform $n$ iterations of $T$.                                 | With horizon $T$, **early stopping:** no additional benefit after $T$ sweeps.                                                                       |   |                         |   |           |
| **Backward induction**          | start at $v_T=0$; for $t=T-1\dots0$ compute $v_t=T_t v_{t+1}$. | Equivalent to finite‑horizon VI.                                                                                                                    |   |                         |   |           |
| **Simplified PI**               | drop high‑precision PE once policy stabilises to save work.    | —                                                                                                                                                   |   |                         |   |           |

---

### C₅ Convergence & error analysis

| result                          | statement                                                                                          |   |    |   |                                  |
| ------------------------------- | -------------------------------------------------------------------------------------------------- | - | -- | - | -------------------------------- |
| **Effective horizon**           | $H_\gamma=1/(1-\gamma)$.                                                                           |   |    |   |                                  |
| **VI convergence**              | $\|v_k-v^{\*}\|_\infty\le\gamma^k\|v_0-v^{\*}\|_\infty$.                                           |   |    |   |                                  |
| **Absolute‑error runtime (VI)** | $k\ge H_\gamma\ln(1/ε)$.                                                                           |   |    |   |                                  |
| **Relative‑error runtime**      | require $\|v_k-v^{\*}\|_\infty\le ε\|v^{\*}\|_\infty$: extra additive $\ln\|v^{\*}\|_\infty$ term. |   |    |   |                                  |
| **Policy error bound**          | $\|v^{Gv}-v^{\*}\|_\infty\le \frac{2\gamma}{1-\gamma}\|v-v^{\*}\|_\infty$.                         |   |    |   |                                  |
| **Finite termination of PI**    | ≤                                                                                                  | A | ^{ | S | } greedy sweeps; often far less. |
| **Normalization / span trick**  | set $\tilde v=v-\min_s v(s)$ ⇒ spans bounded by rewards.                                           |   |    |   |                                  |
| **Mixing‑rate viewpoint**       | replace $1/(1-\gamma)$ with span($v^{\*}$) in “easy” instances.                                    |   |    |   |                                  |

---

### C₆ Computational complexity & bounds

| category                              | bound / notion                                                                                                                                                                     |   |                                                      |   |                                  |   |                          |   |       |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ---------------------------------------------------- | - | -------------------------------- | - | ------------------------ | - | ----- |
| **Algorithm‑independent lower bound** | Ω(                                                                                                                                                                                 | S | ²                                                    | A | ) just to *read* $(P,R)$.        |   |                          |   |       |
| **VI upper bound**                    | (O(                                                                                                                                                                                | S | ^2                                                   | A | ,H\_\gamma\ln(1/ε))) scalar ops. |   |                          |   |       |
| **PI upper bound**                    | worst case (O(                                                                                                                                                                     | A | ^{                                                   | S | },                               | S | ^3)); typical (\tilde O( | S | ^3)). |
| **Best‑case trivial scenario**        | if $R,P$ independent of actions ⇒ *any* policy is optimal ⇒ only input scan required.                                                                                              |   |                                                      |   |                                  |   |                          |   |       |
| **Δ‑dependence**                      | VI runtime grows with $\ln(1/ε)$; PI’s *exact* optimality bound has no ε.                                                                                                          |   |                                                      |   |                                  |   |                          |   |       |
| **Horizon notation**                  | $H_{\gamma,ε}=\lceil\ln(1/ε)/(1-\gamma)\rceil$; instance‑optimal $H^{\*}_{\gamma,ε}$.  Analyses enforce $H\ge H_{\gamma,ε}$, stronger than the necessary $H\ge H^{\*}_{\gamma,ε}$. |   |                                                      |   |                                  |   |                          |   |       |
| **Instance‑dependent vs worst‑case**  | “hot” instances (γ→1, span↑) vs span‑bounded “easy” cases.                                                                                                                         |   |                                                      |   |                                  |   |                          |   |       |
| **Model of computation**              | bit‑model introduces log factors (matrix condition numbers).                                                                                                                       |   |                                                      |   |                                  |   |                          |   |       |
| **Hardness frontier**                 | no proof yet that PI can be forced to >poly(                                                                                                                                       | S | ) iterations; matching upper‑lower gaps remain open. |   |                                  |   |                          |   |       |

---

### C₇ Geometric & analytical views

* **Value‑function polytope**

  $$
    \mathcal V=\operatorname{conv}\{v^{\mu}:\mu\text{ deterministic}\}\subset\mathbb R^{|S|}.
  $$

* **VI as projection** onto the monotone half‑space $\{v\le Tv\}$; each step shrinks the ∞‑distance to $v^{\*}$.

* **PI as alternating projections** between affine subspaces $\{v=T^{\pi}v\}$ (policy evaluation) and facets of $\mathcal V$ (greedy improvement).

* **Geometric proof of sufficiency**: extreme points of $\mathcal V$ correspond exactly to deterministic policies; optimal point lies on at least one facet ⇒ some deterministic policy is optimal.

---

### C₈ Open questions & research frontiers

| problem                                            | current status                                                   | why it matters                                    |                                              |                                                   |                             |                                               |
| -------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------- | ------------------------------------------------- | --------------------------- | --------------------------------------------- |
| **PI worst‑case iterations**                       | exponential gap unproved; candidate hard instances sparse.       | Separates complexity classes of DP algorithms.    |                                              |                                                   |                             |                                               |
| **Span‑adaptive planning**                         | theory hints at span(v\*) replacing $1/(1-\gamma)$.              | Could yield PTAS for “easy” MDPs.                 |                                              |                                                   |                             |                                               |
| **Accuracy‑free algorithms**                       | goal: poly(                                                      | S                                                 | ,                                            | A                                                 | ,log input) without ε term. | Mirrors breakthroughs in LP & interior‑point. |
| **Fast evaluation via fast matrix multiplication** | theoretical O(                                                   | S                                                 | ^{ω}) (ω≈2.37) but impractical for sparse P. | Would shift PI’s “expensive iteration” narrative. |                             |                                               |
| **Average‑reward counterparts**                    | need span‑norm contractions; open rates.                         | Extends discounted techniques to ergodic control. |                                              |                                                   |                             |                                               |
| **Instance‑dependent lower bounds**                | techniques from communication complexity only partially adapted. | Precise hardness = sharper algorithmic focus.     |                                              |                                                   |                             |                                               |

---

## Inter‑cluster cheat‑sheet (where to look)

| question                                                          | answer location                |
| ----------------------------------------------------------------- | ------------------------------ |
| “What exactly **is** the Fundamental Theorem and its proof idea?” | C₃ (items 2–3)                 |
| “How does **Value Iteration** terminate within ε?”                | C₄ (VI) + C₅ (VI convergence)  |
| “Why does **Policy Iteration** avoid ε in its bound?”             | C₄ (PI) + C₆ (Δ‑independence)  |
| “Where does the factor 1/(1‑γ) come from?”                        | C₅ (effective horizon)         |
| “What if I only need a *relative*‑error value?”                   | C₅ (relative‑error runtime)    |
| “Can deterministic policies ever be sub‑optimal?”                 | No – see C₃ (Fundamental Thm.) |
| “What is the geometric picture behind all this?”                  | C₇                             |

---

## Suggested next steps for the curious practitioner

1. **Hands‑on sanity** – Code VI & PI on 20‑state random MDPs; verify C₅’s error curves and C₆’s runtime formulas.
2. **Visual insight** – Plot the 2‑state value polytope and animate VI vs PI (cluster C₇).
3. **Research play** – Try designing an MDP where PI needs super‑polynomial sweeps (C₈.1); test against existing heuristics.
4. **Algorithm engineering** – Implement span‑normalised VI; compare to vanilla VI when γ≈0.995.

Feel free to request **proof details**, **empirical notebooks**, or **additional geometric diagrams** on any sub‑topic.
