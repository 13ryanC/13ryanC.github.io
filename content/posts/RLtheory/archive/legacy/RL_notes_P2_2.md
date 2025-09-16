---
date: "2025-06-30"
title: "(Part 2.2) Personal Notes on the Foundations of Reinforcement Learning"
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

Below is a **self‑contained compendium** arranged in the seven‑level hermeneutic order

$$
\boxed{𝒞_{1}\;\leᴴ\;𝒞_{2}\;\leᴴ\;\dots\;\leᴴ\;𝒞_{7}}
$$

so that every concept presupposes only material in earlier clusters.  Formal definitions appear in **blue boxes**, theorems in **green boxes**, and key proofs are sketched in compressed but complete form.  Wherever several viewpoints coexist, they are itemised explicitly.  All sets are finite unless stated Borel‑measurable, which lets us side‑step technicalities without losing generality.

---

## 𝒞₁ — Foundational MDP primitives

### 1.1 Probability space of trajectories

$$
(\Omega,\mathscr F,\mathbf P)=\left(S\times A\times\mathbb R\right)^{\infty},\qquad
\mathscr F=\sigma\!\bigl(\text{cylinder sets}\bigr).
$$

Random co‑ordinate projections give $S_t,A_t,R_{t+1}$.

---

### 1.2 **Definition (MDP)**

$$
\boxed{\mathcal M=(S,A,T,R,\gamma)},\qquad\gamma\in[0,1).
$$

* $S$: state space          \* $A$: action space
* $T(s,a,\cdot)$: transition kernel (probability measure on $S$).
* $R(s,a)$: reward, either deterministic or the mean of a bounded distribution.
* $\gamma$: discount factor ensuring $|G_t|<\infty$.

---

### 1.3 Histories & policies

*Full history* at time t:

$$
H_t=(S_0,A_0,R_1,\ldots,S_t).
$$

$$
\boxed{\pi_t(\,\cdot\mid H_t):A\to[0,1]}\quad
\text{is a policy kernel (measurable in }H_t\text{).}
$$

> **Memoryless / stationary**
> $\pi_t(\cdot\mid H_t)=\pi(\cdot\mid S_t)$.

### 1.4 Return

$$
G_t=\sum_{k=0}^{\infty}\gamma^{k}R_{t+k+1},
\qquad
|G_t|\le\frac{R_{\max}}{1-\gamma}.
$$

*Boundedness* follows from geometric summation plus bounded rewards.

---

## 𝒞₂ — Value‑centric objectives

### 2.1 **Definition (Value functions)**

$$
V^{\pi}(s) = \mathbf E^{\pi}_s [G_0],
$$

$$
Q^{\pi}(s,a)=\mathbf E^{\pi}_{s,a}[G_0].
$$

### 2.2 Optimality & ε‑optimality

$$
V^{\star}(s)=\sup_\pi V^{\pi}(s),\qquad
\pi\text{ is }\varepsilon\text{-optimal}\iff 
V^{\pi}(s)\ge V^{\star}(s)-\varepsilon\;\forall s.
$$

*Why “sup” not “max”* — the space of all history‑dependent policies is (uncountably) infinite; continuity does not guarantee an attained maximum but completeness of ℝ guarantees a supremum.

### 2.3 Initial‑state distribution is optional

For discounted tasks

$$
\mathbf E_{\mu_0}^\pi[G_0]
= (1-\gamma)\sum_{s,a}d^{\pi}_\gamma(s,a)R(s,a),
$$

so $\mu_0$ merely **rescales** the occupancy measure; optimisation is state‑wise.

---

## 𝒞₃ — Structural sufficiency: occupancy measures & Fundamental Theorem

### 3.1 **Definition (Discounted occupancy measure)**

$$
d_{\gamma}^{\pi} (s,a)  =  \mathbf{E}^{\pi} \bigl[\sum_{t=0}^{\infty} \gamma^{t} \mathbf{1} \lbrace S_t=s,A_t=a \rbrace \bigr]
$$

Properties

* total mass $=1/(1-\gamma)$;
* **linear value identity**
  $V^{\pi}(s_0)=\sum_{s,a}d^{\pi}_\gamma(s,a)R(s,a)$.

### 3.2 LP formulation

Maximise $\sum_{s,a}d(s,a)R(s,a)$ subject to linear **balance constraints**

$$
\sum_a d(s,a)-(1-\gamma)\mu_0(s)=
\gamma \sum_{s',a'}d(s',a')T(s',a',s),\quad d\ge0.
$$

Feasible set is a compact, convex polytope $𝒟$.

### 3.3 Extremal structure

**Lemma.** An extreme point of $𝒟$ corresponds to a **deterministic stationary** policy.

*Proof sketch.*
Eliminate $d$ to $(|S|\times|A|)$ variables.  Every basic feasible solution has at most $|S|$ non‑zero state‑action pairs ⇒ each state chooses exactly **one** action ⇒ deterministic & stationary.

---

### 3.4 **Fundamental Theorem (discounted MDPs)**

$$
\boxed{\exists\;\pi^\star\in A^{S}\text{ deterministic stationary with }V^{\pi^\star}=V^\star.}
$$

*Proof.* Objective is linear, so optimum is at an extreme point of $\mathcal{D}$ ⇒ deterministic stationary $\pi^{\ast}$ (Lemma). □

---

### 3.5 Memoryless ≠ Greedy

*Memoryless* merely means $\pi(s)$ depends only on $s$.
Greedy w.r.t $V$ means

$$
\pi(s)=\arg\max_{a} \lbrace R(s,a)+\gamma\sum_{s'}T(s,a,s')V(s') \rbrace.
$$

A memoryless policy can be non‑greedy if the argument is not evaluated on the value it induces.  **Example:** two‑state chain where π picks a sub‑optimum action consistently.

---

## 𝒞₄ — Computational mechanisms

### 4.1 Bellman operators

$$
(T^\pi V)(s)= R(s,\pi(s))+\gamma\!\!\sum_{s'}T(s,\pi(s),s')V(s'),\qquad
(T^\star V)(s)=\max_a\{R+\gamma \cdot T V\}.
$$

### 4.2 **Theorem (Contraction)**

$$
\|T^\star V_1-T^\star V_2\|_\infty\le\gamma\|V_1-V_2\|_\infty.
$$

*Proof.* Follows from max of affine maps and γ<1.

### 4.3 Value Iteration

```
V₀ arbitrary
repeat  V_{k+1} ← T★ V_k
until   ‖V_{k+1}−V_k‖∞ < ε(1−γ)/2γ
π_k(s)=argmax_a {...}
```

**Iteration bound**

$$
k\;\ge\;\frac{\log\!\bigl(\tfrac{2R_{\max}}{(1-\gamma)\varepsilon}\bigr)}
           {\log\!\bigl(\tfrac1\gamma\bigr)}.
$$

### 4.4 Policy enumeration complexity

$$
|\Pi_{\text{det‑stat}}|=|A|^{|S|},\qquad
|\Pi_{\text{full}}|\approx(|A|^{|S|})^{\mathbb N}\;\text{(uncountable)}.
$$

Policy‑iteration / VI avoid this blow‑up; nevertheless, exact optimal control for undiscounted infinite‑horizon is **PPAD‑complete** (Etessami & Yannakakis ’10).

---

### 4.5 Geometry of value space

Attainable value vectors form a **convex polytope** in $\mathbb R^{|S|}$.
Value Iteration traces a γ‑contractive trajectory that spirals onto the **upper surface** (Pareto‑optimal frontier).  For |S| = 3 one can visualise this as a 3‑D polyhedron; successive $T^\star$ images move the point outward until convergence at the extreme point representing π★.

---

## 𝒞₅ — Measure‑theoretic foundations

* **σ‑algebras** guarantee every infinite‑length event we care about (e.g. “visit s infinitely often”) is measurable.
* **Dominated convergence** lets us swap limit ↔ expectation when proving convergence of $G_t$.
* **Radon–Nikodym** derivatives underpin conditional values $V^{\pi}(s)=\mathbf E[G_t\mid S_t=s]$.

### St Petersburg paradox (why γ < 1)

With payoff $2^{N}$ on first heads,
$\mathbf E[2^{N}]=\infty$.  Discounting with γ<½ yields finite expectation
$\sum_{n\ge0}γ^{n}2^{n}<\infty$.  This motivates insisting on γ<1 or bounded horizon.

### Weak vs. strong Markov

* **Strong Markov property**: state at a stopping time τ is independent of past given $S_\tau$.
* **Weak Markov**: independence only for fixed times.
  Strong ⇒ Weak ⇒ sufficiency of stationary policies; equality holds for time‑homogeneous kernels.

---

## 𝒞₆ — Horizon & reward variants

| Setting                   | Policy form                                    | Bellman equation                      | Issues                                          |
| ------------------------- | ---------------------------------------------- | ------------------------------------- | ----------------------------------------------- |
| Finite horizon T          | time‑indexed πₜ(s)                             | backward recursion over t             | Stationarity lost.                              |
| Undiscounted total reward | stationary π may suffice but $G_t$ may diverge | no contraction ⇒ different algorithms | Requires positive recurrence or absorbing goal. |
| Average reward            | stationary π, bias functions h(s)              | $ρ + h(s) = \max_a[R + \sum T h]$     | Needs gain‑bias VI or relative‑value PI.        |

**Goal states & deadlines**
Augment state with clock $t$ or absorbing “terminal”; Markov property restored, algorithms unchanged.

---

## 𝒞₇ — Meta‑model reflections

### Brittleness & Robust MDPs

Introduce an **ambiguity set**

$$
\mathcal T=\{\,\tilde T:\| \tilde T - T\|_1\le \delta \,\}.
$$

Robust value solves

$$
V(s)=\max_a\min_{\tilde T\in\mathcal T}
\bigl\{R(s,a)+\gamma\sum_{s'}\tilde T(s,a,s')V(s')\bigr\}.
$$

### Leaky abstraction

Hidden variables violate Markov; remedy via **feature engineering** or **POMDPs**.
Non‑stationary exploration policies used during learning purposely break optimal‑stationary dogma.

### Time‑outs & soft deadlines

*Hard* — add clock dimension.
*Soft* — reward shaping $R'(s,a)=R(s,a)-\lambda$ each step imposes implicit discount.

### Non‑memoryless policies with unmatched value profile

Example: 2‑state MDP where π¹ alternates actions (depends on parity of t), achieving identical V★ but *state‑wise* returns unmatched by any stationary policy at intermediate horizons; underscores why we *define* policies broadly before proving sufficiency.

---

## Closing synthesis

The lattice

$$
𝒞_{1}\to𝒞_{2}\to𝒞_{3}\to𝒞_{4}\to𝒞_{5}\to𝒞_{6}\to𝒞_{7}
$$

first **builds the syntax** of MDPs, then **semantics of preference**, discovers a **structural theorem** that shrinks the search space, develops **algorithms** exploiting that structure, erects the **measure‑theoretic scaffolding** needed for infinite trajectories, surveys **alternative objective framings**, and finally reflects on **model robustness and abstraction limits**.  Each idea is justified, formally defined, and embedded in its proper interpretive stratum, completing the requested comprehensive passage.
