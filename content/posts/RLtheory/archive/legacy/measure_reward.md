---
date: "2025-06-30"
title: "Occupancy Measure and Reward"
summary: "Occupancy Measure and Reward"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

**Step 2 – Plan & First Verifiable Step**

### Internal plan (concise)

| Sub-task                                                                                        | Tool | Checkpoint                  |
| ----------------------------------------------------------------------------------------------- | ---- | --------------------------- |
| A. Formally define an MDP and the *discounted state(-action) occupancy measure*.                | none | Math objects clearly stated |
| B. Derive a closed-form linear‐algebra expression for the occupancy measure.                    | none | μ^π formula obtained        |
| C. Show that the *value* of a policy is an inner product ⟨μ^π , r⟩ and prove the decomposition. | —    | Dot-product proved          |
| D. Make the “independence” argument precise: which terms depend on π,P vs. r.                   | —    | Dependence table            |
| E. (If requested) sketch implications for inverse RL & policy optimisation.                     | —    | Optional                    |

We will execute **Sub-task A** now.

---

### Sub-task A – Formal definitions

**Markov Decision Process (MDP).**
An MDP is the tuple
\((\mathcal S,\mathcal A,P,r,\gamma,\mu_0),\)
where

* \( \mathcal S\) finite (or countable) state set,
* \( \mathcal A\) finite action set,
* \(P(s'|s,a)=\Pr[S_{t+1}=s'\mid S_t=s,A_t=a]\) transition kernel,
* \(r:\mathcal S\times\mathcal A\to\mathbb R\) immediate reward,
* \(\gamma\in(0,1)\) discount factor,
* \(\mu_0\) initial-state distribution.

**Policy.**  A (stationary, stochastic) policy \(\pi(a|s)=\Pr[A_t=a\mid S_t=s]\).

---

#### Discounted *state–action* occupancy measure

For every policy π, define

$$
\mu^{\pi}(s,a)\;:=\;\mathbb E_{\pi}\!\left[\sum_{t=0}^{\infty}\gamma^{t}\,\mathbf 1\{S_t=s,\;A_t=a\}\right],
\tag{1}
$$

the expected *discounted* number of visits to pair \((s,a)\).

Equivalently, with initial distribution µ₀,

$$
\mu^{\pi}(s,a)=\sum_{t=0}^{\infty}\gamma^{t}\Pr_{\mu_0,\pi}(S_t=s,A_t=a).
$$

When rewards depend only on state (not action), the *state* occupancy measure \(d^{\pi}(s)=\sum_a\mu^{\pi}(s,a)\) is used.

Equation (1) depends **only** on \(\pi\) and \(P\); the reward function plays no role.  This “reward-free” quantity is what later lets us write the value as an inner product. ([rltheory.github.io][1])

---

### Progress

| Achieved                                                                                | Evidence          |
| --------------------------------------------------------------------------------------- | ----------------- |
| Defined MDP, policy, discount factor.                                                   | above             |
| Gave rigorous definition of discounted occupancy measure and noted reward-independence. | eq. (1), citation |

**Open issues for next step**

1. Derive a linear-algebra form: \( \boldsymbol\mu^{\pi} = (1-\gamma)\,\bigl(I-\gamma P_\pi\bigr)^{-1}\operatorname{diag}(\mu_0)\pi\).
2. Prove value decomposition \( J(π)=\sum_{s,a}\mu^{π}(s,a)r(s,a)=\langle \mu^{π},r\rangle\).
3. Summarise independence and practical uses.

Let me know if you want me to continue with derivation **B–C**, or adjust focus.

[1]: https://rltheory.github.io/lecture-notes/planning-in-mdps/lec2/?utm_source=chatgpt.com "2. The Fundamental Theorem - RL Theory"



### 1 Setup and notation

| Symbol                                            | Meaning                                        | Dimensions (finite)                    |             |
| ------------------------------------------------- | ---------------------------------------------- | -------------------------------------- | ----------- |
| \(\mathcal S=\{1,\dots,n\}\)                        | state set                                      | \(n\)                                    |             |
| \(\mathcal A=\{1,\dots,m\}\)                        | action set                                     | \(m\)                                    |             |
| \(P_a\in\mathbb R^{n\times n}\)                     | \(P_a[s,s']\!:=\Pr(S_{t+1}=s'\mid S_t=s,A_t=a)\) | transition under action \(a\)            |             |
| (\pi(a                                            | s))                                            | stationary policy                      | —           |
| (P\_\pi=\sum\_{a} \operatorname{diag}!\bigl(\pi(a | \cdot)\bigr),P\_a)                             | state‑to‑state kernel induced by \(\pi\) | \(n\times n\) |
| \(\mu_0\in\Delta(\mathcal S)\)                      | row vector of initial‑state probabilities      | \(1\times n\)                            |             |
| \(r\in\mathbb R^{nm}\)                              | reward vector *flattened* over \((s,a)\)         | \(1\times nm\)                           |             |
| \(\gamma\in(0,1)\)                                  | discount factor                                | —                                      |             |

We use **row vectors** throughout so that probabilities evolve by *right‑multiplication*.

---

### 2 Discounted occupancy measures

**State visitation (row) vector**

$$
d_\gamma^{\pi} \;:=\;\sum_{t=0}^{\infty}\gamma^{t}\,\mu_0 P_\pi^{\,t}
\tag{1}
$$

and the **state–action occupancy**

$$
\mu^{\pi}(s,a)\;=\;d_\gamma^{\pi}(s)\,\pi(a|s)\quad\Longrightarrow\quad
\mu^{\pi}=d_\gamma^{\pi}\,\Pi,
\tag{2}
$$

where \(\Pi\in\mathbb R^{n\times nm}\) has entries
\(\Pi[s,(s,a)]=\pi(a|s)\).

---

### 3 Closed‑form solution for \(d_\gamma^{\pi}\)

Because \(\rho_{t+1}:=\rho_tP_\pi\) with \(\rho_0=\mu_0\), summation in (1) gives a geometric series:

$$
d_\gamma^{\pi}
  \;=\;\mu_0\sum_{t=0}^{\infty}(\gamma P_\pi)^{t}
  \;=\;\mu_0\bigl(I-\gamma P_\pi\bigr)^{-1},
\tag{3}
$$

since \(\| \gamma P_\pi\|_\infty\le\gamma<1\) implies \(I-\gamma P_\pi\) is nonsingular. This is the *reward‑free* part—it depends **only** on \(\mu_0,\pi,P\).&#x20;

A frequently used *probability* version rescales (3):

$$
\underbrace{(1-\gamma)\,d_\gamma^{\pi}}_{\displaystyle d^{\pi}}
\in\Delta(\mathcal S),\qquad
d^{\pi}=\!(1-\gamma)\mu_0(I-\gamma P_\pi)^{-1}.
\tag{4}
$$

---

### 4 Value as an inner product

For any starting distribution \(\mu_0\), the **discounted return** of policy \(\pi\) is

$$
J(\pi)
=\mathbb E_{\mu_0,\pi}\!\left[\sum_{t=0}^{\infty}\gamma^{t}r(S_t,A_t)\right].
$$

Insert an indicator, exchange expectation/sum, and recognise (2):

$$
\begin{aligned}
J(\pi)
&=\sum_{s,a} r(s,a)\sum_{t=0}^{\infty}\gamma^{t}
      \Pr_{\mu_0,\pi}(S_t=s,A_t=a) \\[2pt]
&=\sum_{s,a} r(s,a)\,\mu^{\pi}(s,a)
 =\;\langle \mu^{\pi},\,r\rangle.
\end{aligned}
\tag{5}
$$

Equation (5) is the **alignment** statement: value equals the inner product between the *geometry* (where the policy visits) and the *semantics* (how good those visits are). ([rltheory.github.io][1])

---

### 5 Summary of dependence

| Quantity                                 | Depends on \(P,\,\pi\)             | Depends on \(r\)   |
| ---------------------------------------- | -------------------------------- | ---------------- |
| Occupancy \(d_\gamma^{\pi},\mu^{\pi}\)     | **Yes** — via (3) & (2)          | **No**           |
| Value \(J(\pi)=\langle\mu^{\pi},r\rangle\) | indirectly (through \(\mu^{\pi}\)) | **Yes** — linear |

The factorisation \(J(\pi)=\langle\mu^{\pi},r\rangle\) underlies:

* **Inverse RL** – solve for \(r\) that explains observed \(\mu^{\pi}\).
* **Policy search / gradients** – optimise \(\pi\) while holding \(r\) fixed (policy‑gradient theorem expresses \(\nabla_\theta J\) via \(\mu^{\pi}\)).
* **Reward‑agnostic evaluation** – one can estimate \(\mu^{\pi}\) once, then plug in many candidate reward vectors without new roll‑outs.

All of these exploit the *independence* delineated above.

[1]: https://rltheory.github.io/lecture-notes/planning-in-mdps/lec2/ "The Fundamental Theorem | RL Theory"
