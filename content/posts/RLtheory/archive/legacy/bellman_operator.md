---
date: "2025-06-30"
title: "Bellman Optimal Operator"
summary: "Wandering"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### 1.  Setting and Notation

Let

* **S** be a (finite or countable) set of states.
* **A** the set of actions (possibly state–dependent, but we suppress that for clarity).
* \(P(\,s' \mid s,a)\) the transition kernel.
* \(R(s,a)\in\mathbb{R}\) the expected one‑step reward.
* \(0\le\gamma<1\) the discount factor.

A *value function* is any bounded mapping \(V:S\to\mathbb{R}\).  Endow the space \(\mathcal{V}= \{V:\|V\|_\infty<\infty\}\) with the supremum norm \(\|V\|_\infty=\max_{s\in S}|V(s)|\).

---

### 2.  Bellman Operators

| Symbol                                         | Definition                                                                                | Fixed‑point                        |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------- |
| **Policy evaluation operator** \((T^{\pi}V)(s)\) | \( = R(s,\pi(s)) + \gamma\sum_{s'}P(s' \mid s,\pi(s))\,V(s')\)                              | \(V^\pi\) (value under policy \(\pi\)) |
| **Optimal (control) operator** **\(T^{*}\)**     | \( (T^{*}V)(s) = \max_{a\in A}\Bigl[ R(s,a) + \gamma\sum_{s'}P(s' \mid s,a)\,V(s') \Bigr]\) | \(V^{*}\) (optimal value)            |

The user’s question concerns **\(T^{*}\)**, usually called the **Bellman optimality operator** or **Bellman optimal operator**.

---

### 3.  Formal Properties of \(T^{*}\)

| Property                          | Statement                                                                                                         | Sketch of proof / intuition                                                                                                   |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Monotone**                      | \(V\le W \;\Longrightarrow\; T^{*}V \le T^{*}W\).                                                                   | Immediate because max and expectation preserve order.                                                                         |
| **γ‑Contraction**                 | \(\|T^{*}V - T^{*}W\|_\infty \le \gamma\,\|V-W\|_\infty\).                                                          | For each state the difference is bounded by \(\gamma\) times the sup difference of \(V,W\); take the max.                         |
| **Unique fixed point**            | There exists a single \(V^{*}\) such that \(T^{*}V^{*}=V^{*}\).                                                       | Banach fixed‑point theorem → uniqueness because \(T^{*}\) is a contraction on a complete space.                                 |
| **Optimality of the fixed point** | \(V^{*}(s)=\sup_{\pi}V^{\pi}(s)\) for all \(s\).                                                                      | Classical dynamic‑programming argument: greedy w\.r.t. \(V^{*}\) attains the supremum.                                          |
| **Value‑iteration convergence**   | Starting with any \(V_{0}\in\mathcal{V}\),   \(V_{k+1}=T^{*}V_{k}\) satisfies \(V_{k}\xrightarrow[k\to\infty]{}V^{*}\). | Repeated application of a γ‑contraction converges geometrically: \(\|V_{k}-V^{*}\|_\infty\le\gamma^{k}\|V_{0}-V^{*}\|_\infty\). |

*Consequences.*

1. **Algorithmic:**   Value iteration and many modern reinforcement‑learning methods (e.g., DQN, fitted Q‑iteration) are nothing more than approximate fixed‑point solvers for \(T^{*}\).
2. **Stability:**   Because \(T^{*}\) is a contraction, small approximation errors do not snowball—crucial for function‑approximation proofs.

---

### 4.  Extension to Action‑Value Functions

Define \(Q:S\times A\to\mathbb{R}\) and norm \(\|Q\|_\infty\).
The **optimal \(Q\)-operator**

$$
(\mathcal{T}^{*}Q)(s,a)=R(s,a)+\gamma\sum_{s'}P(s'\mid s,a)\,\max_{a'}Q(s',a')
$$

shares the same monotonicity and contraction properties, with unique fixed point \(Q^{*}\).  Policy greedy w\.r.t. \(Q^{*}\) is optimal.

---

### 5.  Assumptions & When They Fail

| Assumption      | Why needed                                        | What if violated                                                                                                                                                                  |
| --------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \(0\le\gamma<1\)  | Guarantees contraction.                           | For \(\gamma=1\) (undiscounted) on infinite‑horizon‑total‑reward problems, \(T^{*}\) is *not* a contraction; extra conditions (e.g., proper policies in episodic tasks) are required. |
| Bounded rewards | Completeness of \((\mathcal{V},\|\cdot\|_\infty)\). | Unbounded rewards can break Banach’s theorem; use weighted norms or other techniques.                                                                                             |

---

### 6.  Alternate Viewpoints

*Functional Analysis* \(T^{*}\) is a **non‑expansive maximal monotone operator**; its fixed point is the unique minimal element of the set \(\{V\mid V\ge T^{*}V\}\).

*Control Theory* \(T^{*}\) encodes the one‑step *Generalized Policy Iteration* map; solving \(T^{*}V=V\) is equivalent to the Hamilton‑Jacobi–Bellman equation in continuous spaces.

*Computer Science* \(T^{*}\) is the semiring “tropical” dynamic‑programming operator: \(\max\) plays the role of addition, \(+\) plays multiplication.

---

### 7.  Typical Pitfalls & Practical Remedies

| Pitfall                                       | Effect                                                                                   | Remedy                                                                                          |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Function approximation error accumulation** | With non‑linear approximators \(T^{*}\) may no longer be a contraction on parameter space. | Use *projected* Bellman operators, regularisation, or policy‑gradient alternatives.             |
| **Overestimation bias** (in \(Q\)-based RL)     | The inner \(\max\) in \(\mathcal{T}^{*}\) yields upward‑biased estimates when \(Q\) is noisy.  | Double Q‑learning, robust Bellman operators.                                                    |
| **γ close to 1**                              | Contraction factor ≈ 1 → slow convergence.                                               | Use acceleration (Anderson, extrapolation), multi‑step returns, or “contracting trace” methods. |

---

### 8.  Minimal Working Example (hand‑computed)

Two‑state MDP, actions {a,b}, γ=0.9.
\(R(s_1,a)=1\), \(R(s_1,b)=0\), \(R(s_2,\cdot)=0\).
All actions deterministically keep you in the same state.

1. Start \(V_{0} \equiv 0\).
2. Apply \(T^{*}\):

$$
(T^{*}V_{0})(s_1)=\max\{1+0.9\cdot0,\;0\}=1,\qquad
(T^{*}V_{0})(s_2)=0.
$$

3. Next iteration gives \(V_{2}(s_1)=1+0.9\cdot1=1.9\), etc.
4. Limit \(V^{*}(s_1)=\frac{1}{1-0.9}=10\); \(V^{*}(s_2)=0\).

---

### 9.  Summary

The **Bellman optimal operator** \(T^{*}\) maps any bounded value function to the value of acting optimally *for just the next step and then following \(V\)*.  It is

* **order‑preserving**,
* a **γ‑contraction** under the sup‑norm (when \(0\le\gamma<1\)), with
* a **unique fixed point** \(V^{*}\) that equals the optimal value function,

and serves as the theoretical and algorithmic cornerstone of dynamic programming and modern reinforcement learning.
