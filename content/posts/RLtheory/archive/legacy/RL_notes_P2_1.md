---
date: "2025-06-30"
title: "(Part 2.1) Personal Notes on the Foundations of Reinforcement Learning"
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

Below each cluster **𝒞ₖ** appears in the hermeneutic order
$𝒞_{1}\leᴴ𝒞_{2}\leᴴ\dots\leᴴ𝒞_{7}$.
Every section supplies (i) formal definitions, (ii) explanatory prose, and (iii) proofs or rigorous arguments where they are called for.

---

## 𝒞₁ — Foundational MDP primitives

### 1.1 Probability space of trajectories

Let $(\Omega ,\mathscr F ,\mathbf P)$ be a probability space.
A **trajectory** (sample path) is an element

$$
\omega=(s_{0},a_{0},r_{1},s_{1},a_{1},r_{2},\dots)\in\Omega .
$$

Cylinder sets generate the σ‑algebra $\mathscr F$; this ensures every finite prefix event is measurable.
The random variables $S_{t},A_{t},R_{t+1}$ (state, action, reward) are coordinate projections on Ω.

### 1.2 MDP tuple

A **Markov Decision Process** is

$$
\mathcal M=(S,A,T,R,\gamma),\quad\gamma\in[0,1).
$$

| symbol   | meaning               | assumptions                                                                          |
| -------- | --------------------- | ------------------------------------------------------------------------------------ |
| $S$      | **state space**       | finite, or a Borel space for measure‑theoretic formalisms.                           |
| $A$      | **action space**      | finite / Borel, independent of s (for simplicity).                                   |
| $T$      | **transition kernel** | $T(s,a,\cdot)$ is a probability measure on $S$.                                      |
| $R$      | **reward function**   | Either deterministic $R:S\times A\to\mathbb R$ or bounded measurable $r\sim R(s,a)$. |
| $\gamma$ | **discount factor**   | guarantees finiteness of infinite sums.                                              |

### 1.3 Histories and policies

*Full history* at time t: $H_{t}=(S_{0},A_{0},R_{1},\dots,S_{t})$.
A **policy** is a family of stochastic kernels

$$
\pi_t(\,\cdot\mid H_t): A\longrightarrow[0,1],\qquad t=0,1,\dots
$$

with measurability in $H_t$.
A policy is **memoryless / stationary** if $\pi_t(\cdot\mid H_t)=\pi(\cdot\mid S_t)$ for all t.

> *Why keep full‑history policies?* They form the largest decision class compatible with perfect recall. Only later (𝒞₃) do we prove that we may restrict to stationary policies **without loss of optimality** under the Markov property.

### 1.4 Return

For bounded rewards, the **discounted return** is

$$
G_t=\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1},\qquad |G_t|\le\frac{R_{\max}}{1-\gamma}.
$$

Its measurability follows from dominated convergence and the finiteness supplied by $\gamma<1$.

---

## 𝒞₂ — Value‑centric objectives

### 2.1 Value functions

$$
V^{\pi}(s)\;=\;\mathbf E^{\pi}_s[G_0],\qquad
Q^{\pi}(s,a)\;=\;\mathbf E^{\pi}_{s,a}[G_0].
$$

### 2.2 Optimality

$$
V^{\star}(s)=\sup_{\pi}V^{\pi}(s),\qquad
Q^{\star}(s,a)=\sup_{\pi}Q^{\pi}(s,a).
$$

*Sup* is used because, on infinite policy spaces, a maximum may fail to exist; completeness of $\mathbb R$ ensures the supremum always does.

### 2.3 ε‑optimality

A policy $\pi$ is **ε‑optimal** if

$$
V^{\pi}(s)\ge V^{\star}(s)-\varepsilon,\quad\forall s\in S.
$$

Practical algorithms usually terminate once this criterion is met because the computational effort of closing the last ε‑gap can be exponential in log (1/ε).

---

## 𝒞₃ — Structural sufficiency: occupancy measures & the Fundamental Theorem

### 3.1 Discounted occupancy measure

For a policy $\pi$ define


$$
d_{\gamma}^{\pi} (s,a)  =  \mathbf{E}^{\pi} \bigl[\sum_{t=0}^{\infty} \gamma^{t} \mathbf{1} \lbrace S_t=s,A_t=a \rbrace \bigr]
$$

Properties:

* $d^{\pi}_{\gamma}$ is a **probability sub‑measure** (total mass $1/(1-\gamma)$).
* **Linear value identity**

  $$
  V^{\pi}(s_0)=\sum_{s,a}d^{\pi}_{\gamma}(s,a)\,R(s,a).
  $$

### 3.2 Linear‑program view

Optimising V can be written

$$
\max_{d\in\mathbb R^{|S||A|}}
\sum_{s,a}d(s,a)R(s,a)
\text{ s.t. }
\sum_{a}d(s,a)-(1-\gamma)\mu_0(s)=
\gamma\sum_{s',a'}d(s',a')T(s',a',s),\;d\ge0.
$$

Extreme points of this polytope correspond one‑to‑one with **deterministic stationary policies**.
Hence any optimiser is achieved at an extreme point → **stationary deterministic π★ exists**.

### 3.3 Fundamental Theorem of discounted MDPs

> **Theorem (Puterman, 1994).**
> For a discounted MDP with finite S, A and bounded rewards, there exists a deterministic stationary policy π★ such that $V^{π★}=V^\star$.

*Proof sketch.*

1. Feasible set of occupancy measures is compact convex.
2. Objective is linear; maximum is attained at an extreme point.
3. Extreme points induce deterministic stationary policies as argued above. ∎

Corollary: to find an ε‑optimal policy it suffices to search the much smaller space $A^{|S|}$ instead of the huge history‑dependent space.

---

## 𝒞₄ — Computational mechanisms

### 4.1 Bellman optimality operator

$$
T^{\star}V(s)=\max_{a\in A} \lbrace R(s,a)+\gamma\sum_{s'}T(s,a,s')V(s') \rbrace.
$$

### 4.2 Bellman optimality equation

$V^{\star}=T^{\star}V^{\star}$.

*Proof.*
For any V set

$$
T^{\pi}V(s)=R(s,\pi(s))+\gamma\sum_{s'}T(s,\pi(s),s')V(s').
$$

$T^{\star}V=\sup_{\pi}T^{\pi}V$.
Applying $T^{\star}$ to $V^{\star}$ yields the same value because $V^{\star}$ already dominates every $T^{\pi}V^{\star}$; conversely $V^{\star}$ must satisfy it by definition of sup. ∎

### 4.3 Contraction property

$$
\|T^{\star}V_1-T^{\star}V_2\|_\infty\le\gamma\|V_1-V_2\|_\infty.
$$

Hence $T^{\star}$ is a γ‑contraction on $(\mathbb R^{|S|},\|\cdot\|_\infty)$.

### 4.4 Value Iteration

```
initialise V₀ arbitrarily
repeat
    V_{k+1} ← T★ V_k
until ‖V_{k+1}−V_k‖∞ < ε(1−γ)/2γ
return greedy policy π_k(s)=argmax_a {…}
```

*Convergence.* By Banach’s fixed‑point theorem, $V_k\to V^{\star}$ at **geometric rate** γ.
Stopping rule above guarantees ε‑optimality of the returned greedy policy.

---

## 𝒞₅ — Measure‑theoretic foundations

Why can’t we “sweep measure theory under the rug”?

* We need σ‑algebras so that **events about infinitely many time steps** remain measurable; e.g. “the process visits state 0 infinitely often.”
* Conditional expectations $\mathbf E[G_t\mid S_t=s]$ are Radon–Nikodym derivatives that require measurable sets.
* Without dominated convergence, proofs of the interchange of limit and expectation in $G_t$ would be invalid; paradoxes such as the Saint‑Petersburg game (infinite mean) arise.

Takeaway: **probabilistic soundness** of MDP analysis hinges on these foundations, even though algorithms can usually be presented without them.

---

## 𝒞₆ — Horizon & reward variants

| Setting                   | Objective                                         | Notable differences & pitfalls                                                                                            |
| ------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Finite horizon T**      | $G_0=\sum_{t=0}^{T-1} R_{t+1}$                    | Optimal policies are *time‑dependent* but still memoryless in S.                                                          |
| **Undiscounted infinite** | $\sum_{t=0}^{\infty}R_{t+1}$                      | May diverge; extra assumptions (positive recurrent Markov chain, bounded rewards) or artificial “goal states” are needed. |
| **Average reward**        | $\lim_{N\to\infty}\frac1N\sum_{t=0}^{N-1}R_{t+1}$ | Stationary optimal policies still exist but Bellman equation uses bias functions; value iteration must be modified.       |
| **St Petersburg paradox** | Payoff $2^{N}$ at stopping time N                 | Shows *expectation* can be infinite → discounting restores finiteness.                                                    |

---

## 𝒞₇ — Meta‑model reflections

* **Brittleness of optimality.** A policy can be optimal w\.r.t. an assumed $T,R$ yet fragile under slight model misspecification; robust MDP frameworks (e.g. ambiguity sets over T) enlarge the decision space to mitigate this.
* **Leaky abstraction.** Real systems may violate the Markov property (hidden variables, delayed effects). Practitioners add state features or switch to POMDPs rather than abandon the framework.
* **Deadlines & time‑outs.** Hard horizons break stationarity; one designs augmented states $(s,t)$ with a ticking clock to restore the Markov property.
* **Policy stationarity in practice.** Even when theory guarantees a stationary optimal π★, non‑stationary heuristics (e.g. exploration schedules) are vital during learning phases. Understanding where the abstraction departs from reality guides algorithmic choices.

---

### Closing remarks

The seven clusters supply a **graded hermeneutic scaffold**:

1. *Primitive syntax* of MDPs →
2. *Semantics of preference* (values) →
3. *Structural theorems* simplifying the search space →
4. *Algorithms* exploiting those theorems →
5. *Mathematical legitimation* for infinite objects →
6. *Alternative framings* and their hazards →
7. *Critical reflection* on modelling commitments.

Each level presupposes the earlier ones, satisfying the requested partial order ≤ᴴ.
