---
_build:
  render: never
  list: never

date: "2025-06-30"
title: "(Part 1.2) Personal Notes on the Foundations of Reinforcement Learning"
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


## A – Paradigms, Purposes, and Design Tensions

*(Context precedes formalism)*

### A 1 Why RL Exists

* **Unknown world.** Neither the transition kernel \(P\) nor reward law \(R\) is known *a priori*.
* **Stochastic world.** \(P(\cdot\mid s,a)\) is a probability measure, so outcomes are genuinely random.
* **Exploration.** Because the agent’s data are self‑generated, it must *spend* reward to gather information; otherwise identifiability fails:

> **Identifiability Barrier.**
> If two MDPs differ *only* in the transition from a state–action pair never visited by the learner, no algorithm can be optimal in both. (Proof: the learner’s trajectory distribution is identical in the two environments, so it cannot tell them apart.)

### A 2 Three Operational Modes

| Mode                   | Information pattern   | Main hazard                      |
| ---------------------- | --------------------- | -------------------------------- |
| **Planning**           | Perfect model offline | Exponential state blow‑up        |
| **Batch / Offline RL** | Fixed logged data     | Distributional shift; safety     |
| **Online RL**          | Live interaction      | Exploration–exploitation dilemma |

These modes trade *sample cost*, *risk*, and *computation*.
Designers also choose among **objective formulations**:

* **Discounted‑return** \(G_\gamma=\sum_{t=0}^{\infty}\gamma^{t}r_t\)
* **Average‑reward** \(\limsup_{T\to\infty}T^{-1}\sum_{t<T}r_t\)
* **Episodic finite horizon**, **risk‑sensitive** (CVaR), **adversarial** (min–max)

and among **meta‑learning** criteria (“good policy family across many MDPs”, formalised via PAC‑Bayesian bounds or worst‑case regret).

---

## B – Core Markov Machinery

*(Formal grammar of sequential decision‑making)*

### B 1 Primitives

$$
M=(S,A,P,R,\gamma),\quad
0<\gamma<1,\quad
P:S\times A\to\Delta(S),\;
R:S\times A\to\mathbb R_{\text{bdd}}.
$$

### B 2 Closed‑Loop Dynamics

A **policy** is a measurable kernel \(\pi:H_t\to\Delta(A)\) where \(H_t\) is the history.
Together, \(\pi\) and \(P\) form a **product Markov chain** on \(S\):

$$
\tilde P^{\pi}(s'|s)=\sum_{a}\pi(a|s)P(s'|s,a).
$$

### B 3 Scalar‑valued Control

*Return* \(G_t=\sum_{k=0}^{\infty}\gamma^{k}r_{t+k}\).
*Value functions*

$$
V^{\pi}(s)=\mathbb E[G_0\mid s_0=s;\pi],\qquad
Q^{\pi}(s,a)=\mathbb E[G_0\mid s_0=s,a_0=a;\pi].
$$

> **Fundamental Theorem (finite, discounted).**
> (a) The Bellman *optimal* operator
> \((T^\star V)(s)=\max_{a}\{R(s,a)+\gamma\sum_{s'}P(s'|s,a)V(s')\}\)
> is a \(\gamma\)-contraction; its unique fixed point is \(V^\star\).
> (b) Any greedy deterministic *stationary* policy \(\pi^\star(s)\in\arg\max_a[\dots]\) achieves \(V^\star\).

*(Proof: Banach fixed‑point + monotonicity arguments.)*

**Geometry.** Because deterministic policies are vertices of the simplex \(\Delta(A)\), maximising an affine objective over \(\Delta(A)\) attains its optimum at a vertex—hence deterministic suffices.

### B 4 Distributional Control (NEW layer)

Treat the *entire distribution* \(F^{\pi}_s\) of \(G_0\).
The **distributional Bellman operator**

$$
(\mathcal T_D F)(s)=\mathcal L\bigl[r(s,a)+\gamma G'\bigr],\quad
a\sim\pi(\cdot|s),\;G'\sim F(\cdot|s') 
$$

is a contraction in the Wasserstein metric \(W_p\).
Optimality may be taken under first‑order stochastic dominance, CVaR dominance, or minimal \(W_p\).

Discounting now doubles as a **regulariser**: smaller \(\gamma\) strengthens the contraction (biases long‑term value, reduces variance).

---

## C – Measure‑Theoretic Foundations

*(Making the integrals legal)*

1. **σ‑algebra \(\mathcal S\)** on \(S\); Borel if \(S\subset\mathbb R^d\).
2. **Push‑forward measure.** For measurable \(f:(\Omega,\mathcal F)\to(S,\mathcal S)\) and probability \(\mathbb P\) on \(\Omega\), the *law* of \(f\) is \(f_\mathbb P(B)=\mathbb P(f^{-1}(B))\).
3. **Probability kernel** \(K:X\times\mathcal Y\to[0,1]\).
4. **History σ‑algebra** \(\mathcal H_t=\sigma(s_0,a_0,\dots,s_t)\); general policies require \(\pi:(H_t,\mathcal H_t)\to\Delta(A)\) to be measurable.

> **Ionescu–Tulcea.**
> Given an initial measure \(\mu_0\) and a sequence of kernels \(K_t\), there is a unique trajectory measure \(\mathbb P\) on \(S^{\mathbb N}\) consistent with them.

Consequences: expectations in all Bellman operators are well‑defined even for continuous \(S\).

### C 1 Sampling Bounds

*Hoeffding.* For bounded independent \(X_i\),

$$
\Pr\{|\bar X-\mathbb E\bar X|>\varepsilon\}\le2\exp\!(-2N\varepsilon^2/(b-a)^2).
$$

*CLT & Berry–Esseen* link deviation bounds to Gaussian approximation, underpinning confidence intervals in value‑estimation.

---

## D – Optimisation & Analytical Muscle

* **Hilbert space primer.** Inner product \(\langle\cdot,\cdot\rangle\) ⇒ norm \(\|\cdot\|\) ⇒ Cauchy–Schwarz.
* **Convex analysis** (separating hyperplane, Fenchel duality) ⇒ proof that deterministic policy vertices are optimal.
* **Bregman divergence** \(D_\phi\) generalises Euclidean distance; choosing \(\phi\)=negative entropy yields KL and **mirror descent**—basis of natural‑policy gradient.

> **Mirror‑Descent Rate.**
> If \(f\) is \(L\)-smooth and \(\phi\) 1‑strongly convex, step‑size \(\eta_k=\eta/\sqrt{k}\) gives
> \(f(x_k)-f^\star=O(L\|x_0-x^\star\|^2/\sqrt{k})\).

* **Gradient descent** with constant \(\eta<2/L\) on convex \(f\) yields \(f(x_k)-f^\star\le O(1/k)\).
* **Functional approximation.** Parameterised \(V_\theta\) or \(\pi_\theta\) inserted into these schemes; Bregman tools control approximation bias.

---

## E – Computational Perspective

### E 1 Decision‑problem formalism

*Succinct MDP* = MDP where \(P\) is encoded by a Boolean circuit.
*Value Decision Problem (VDP)* “Is \(V^\star_T(s)\ge\beta\)?”

> **PSPACE‑Completeness.**
> VDP reduces from True‑Quantified‑Boolean‑Formula; dynamic programming uses polynomial space, so VDP ∈ PSPACE and is PSPACE‑hard.

### E 2 Statistical–Computational Gap

Even when **sample complexity** is polynomial (via Cluster C concentration), computing an ε‑optimal policy may be PSPACE‑complete.
Structural restrictions—factored transitions, low treewidth—yield *PTAS* but break in the worst‑case.

---

## Global Hermeneutic Ordering (≤ᴴ) Recap

1. **A (Context)**: motivations, modes, trade‑offs, alternative objectives.
2. **B (System)**: MDP primitives → scalar Bellman theory → distributional layer; γ as regulariser.
3. **C (Foundation)**: measurable spaces, kernels, history σ‑algebras, Ionescu–Tulcea, concentration ↔ CLT.
4. **D (Tools)**: geometry, convexity, Bregman & inequalities, descent rates, approximation.
5. **E (Meta‑limits)**: computational complexity, runtime–sample tension, necessity of heuristics.

Edges are *partial*, not total: measure theory (C) can precede or follow scalar MDPs (B) depending on whether finiteness is assumed; distributional optimality orders are themselves nested lattices.

---

### Reading Tips

*Follow the arrows.* Start with A if you need **motivation**, jump to B for **formal syntax**, consult C whenever you wonder “is that integral legal?”, invoke D for **algorithmic proofs**, and read E to appreciate why your elegant algorithm may still take the age of the universe in the worst case.
