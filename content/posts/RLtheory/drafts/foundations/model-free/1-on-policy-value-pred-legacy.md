---
date: "2025-07-09"
title: "(3.1 legacy) On-Policy Value Prediction (MC, TD-lambda, LSTD)"
summary: "On-Policy Value Prediction (MC, TD-lambda, LSTD)"
lastmod: "2025-07-09"
category: "Notes"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

* **3.1. On-Policy Value Prediction (MC, TD(\(\lambda\)), LSTD)**
    * 3.1.1. Monte-Carlo (MC) Prediction: First-visit, Every-visit, and Incremental Updates
    * 3.1.2. Temporal-Difference (TD) Learning: TD(0), Bias-Variance Trade-offs
    * 3.1.3. Multi-Step TD and the \(\lambda\)-Return: TD(\(\lambda\)) and Eligibility Traces (GAE)
    * 3.1.4. Least-Squares Temporal Difference (LSTD) and Batch Methods





---

## 3  On‑Policy Value Prediction under a Measure‑Theoretic MDP

Throughout let

* \((S,\mathcal B(S))\) and \((A,\mathcal B(A))\) be **standard Borel spaces**;
* \(\kappa(ds'dr'\mid s,a)\) the *unified* transition‑reward **kernel**;
* \(\pi(da\mid s)\) a stationary **policy kernel**;
* \(\gamma\in[0,1)\) the discount;
* \(\mu\) an initial state distribution.

By the Ionescu–Tulcea theorem there is a unique process measure
\(\mathbb P_{\mu}^{\pi}\) on the trajectory space \(H=(S\times A)^{\mathbb N}\) satisfying the Markov property and strong Markov property described in § 1.7 of the attachment.&#x20;

> We write expectations \(\mathbb E_\mu^\pi[\cdot]\) and conditional expectations \(\mathbb E_\mu^\pi[\cdot\mid\mathcal F_t]\) with respect to this measure, where \(\mathcal F_t=\sigma(S_0,A_0,\dots,S_t)\).

---

### 3.1  Value Functions as Integrals

Define the **discounted return** random variable

$$
G_t(\omega) =\sum_{k=0}^{\infty}\gamma^k R_{t+k+1}(\omega) \quad\omega\in H,
$$

which is integrable because rewards are assumed bounded (hence dominated convergence applies). The **state‑value function** is the map

$$
v_\pi(s)=\mathbb E_\mu^\pi\bigl[G_t\mid S_t=s\bigr]
           =T_\pi v_\pi(s),
$$

where the **Bellman operator**

$$
(T_\pi f)(s)=
\int_A\pi(da\mid s)
\int_{S\times\mathbb R}\bigl[r'+\gamma f(s')\bigr]
\kappa(ds'dr'\mid s,a)
$$

is a **Markov operator** in the sense of Definition 1.6.3.

Because \(T_\pi\) is a \(\gamma\)-contraction on \((\mathcal B_\infty(S), \lVert \cdot \rVert_\infty)\), \(v_\pi\) is its unique fixed point.

---

### 3.2  Monte‑Carlo (MC) Policy Evaluation

**Estimator.**  For any measurable state set \(B\in\mathcal B(S)\) define the first visit time

$$
\tau_B :=\inf \lbrace t\ge 0 : S_t\in B \rbrace.
$$

Sampling \(m\) i.i.d. trajectories \(\omega^{(i)}\sim\mathbb P_\mu^\pi\), the *first‑visit* MC estimator is

$$
\widehat v_m(s)=\frac1{m}\sum_{i=1}^{m} G_{\tau_{\{s\}}}(\omega^{(i)}).
$$

Because \(\lbrace G_{\tau_{\{s\}}} \rbrace_{i=1}^m\) are i.i.d. integrable random variables with mean \(v_\pi(s)\), the strong law of large numbers yields almost‑sure convergence \(\widehat v_m(s)\to v_\pi(s)\).

**Incremental update (Robbins–Monro).**  Let \(k_s\) count the visits of \(s\).  The online recursion

$$
V_{k_s+1}(s)=V_{k_s}(s)+\alpha_{k_s}(G_s-V_{k_s}(s)),
\quad
\alpha_{k_s}=\frac{1}{k_s+1},
$$

performs stochastic gradient descent on the mean‑squared error
\(\tfrac12\mathbb E_\mu^\pi[(V(s)-G_s)^2]\).

*Measure‑theoretic note.*  \(G_s\) is \(\mathcal F_\infty\)-measurable and integrable; the update is \(\mathcal F_t\)-adapted, so the Robbins–Monro theorem applies on the canonical probability space \((H,\mathcal F,\mathbb P_\mu^\pi)\).

---

### 3.3  One‑Step Temporal Difference: TD(0)

Define the **TD error** random variable

$$
\delta_t = R_{t+1}+\gamma V_t(S_{t+1})-V_t(S_t),
$$

which is \(\mathcal F_{t+1}\)-measurable.  The *TD(0)* update

$$
V_{t+1}(S_t)=V_t(S_t)+\alpha_t\delta_t
$$

is a stochastic approximation of the projected fixed‑point equation
\(V = \Pi T_\pi V\) (with respect to the state‑occupancy inner product).
Conditioning on \(\mathcal F_t\),

$$
\mathbb E_\mu^\pi[\delta_t\mid\mathcal F_t]
= (T_\pi V_t)(S_t) - V_t(S_t),
$$

so the expected update equals one step of the Bellman operator, yielding convergence to \(v_\pi\) when \(\sum_t\alpha_t=\infty\) and \(\sum_t\alpha_t^2<\infty\).

*Bias–variance.*  Relative to MC, TD(0) replaces the unbiased target \(G_t\) by the conditional expectation \(\mathbb E[G_t\mid \mathcal F_{t+1}]\); this introduces **bias** that vanishes as \(V_t\to v_\pi\) while reducing variance from \(O((1-\gamma)^{-2})\) to \(O(1)\).

---

### 3.4  Multi‑Step Returns and the \(\lambda\)‑Return

For \(n\ge 1\) define the **n‑step return**

$$
G_t^{(n)} = \sum_{k=0}^{n-1}\gamma^{k}R_{t+k+1}
           +\gamma^{n}V_t(S_{t+n}).
$$

Each \(G_t^{(n)}\) is \(\mathcal F_{t+n}\)-measurable.  Choosing random horizon \(N\sim\text{Geom}(1-\lambda)\) independent of the trajectory and setting

$$
G_t^{(\lambda)} := (1-\lambda)\sum_{n=1}^\infty \lambda^{n-1}G_t^{(n)},
$$

yields the **λ‑return** \(G_t^{(\lambda)}\) whose conditional expectation equals \(T_\pi V_t\).  The backward‑view implementation employs the **eligibility trace**

$$
Z_{t} = \gamma\lambda Z_{t-1} + \nabla_\theta v_\theta(S_t)
$$

so that the semi‑gradient update

$$
\theta_{t+1}= \theta_t + \alpha_t \delta_t Z_t
$$

achieves forward–backward equivalence in \(L^2(\rho_\pi)\).

---

### 3.5  Least‑Squares Temporal Difference (LSTD)

Fix a linear architecture \(v_\theta(s)=\phi(s)^\top\theta\) with bounded features.  Under \(\rho_\pi\) (the discounted state‑occupancy measure) define the matrices

$$
A := \mathbb E_{\rho_\pi}\bigl[\phi(S_t)\bigl(\phi(S_t)-\gamma\phi(S_{t+1})\bigr)^\top\bigr],
\qquad
b := \mathbb E_{\rho_\pi}\bigl[R_{t+1}\phi(S_t)\bigr].
$$

Both expectations are Lebesgue integrals over \(H\) w\.r.t.\ \(\mathbb P_\mu^\pi\).  The **projected Bellman equation** \(A\theta=b\) is solved in closed form by

$$
\hat\theta_{\text{LSTD}} = A^{-1}b,
$$

provided \(A\) is non‑singular (true whenever the features are linearly independent on \(\operatorname{supp}\rho_\pi\)).  Empirically \(A,b\) are approximated by trajectory sums; by the strong law the estimates converge almost surely to the true moments.

> **Interpretation.** LSTD performs an explicit *Galerkin projection* of the fixed‑point equation onto the span of \(\phi\), minimising the mean‑squared Bellman error in \(L^2(\rho_\pi)\).

---

### 3.6  Summary of Measure‑Theoretic Guarantees

| Algorithm | Target random variable        | Measurability / Integrability                       | Convergence theorem      |
| --------- | ----------------------------- | --------------------------------------------------- | ------------------------ |
| MC        | \(G_{\tau_{\{s\}}}\)            | \(G_t\in L^1(H,\mathcal F,\mathbb P_\mu^\pi)\)        | LLN ⇒ \(V(s)\to v_\pi(s)\) |
| TD(0)     | \(R_{t+1}+\gamma V_t(S_{t+1})\) | \(\delta_t\in L^1\) and \(\mathcal F_{t+1}\)-measurable | Robbins–Monro a.s. conv. |
| TD(λ)     | \(G_t^{(\lambda)}\)             | integrable by boundedness and geometric weighting   | Same as TD(0) on traces  |
| LSTD      | moments \(A,b\)                 | expectations exist under \(\rho_\pi\)                 | Continuous‑mapping + LLN |

The key technical enabler for all results is the **regular conditional probability** guaranteed by the standard‑Borel assumption, ensuring that conditional expectations and kernels such as \(p\), \(\pi\) and \(\kappa\) are well‑defined measurable maps.&#x20;

---

### 3.7  Practical Implications

* **Choosing a prediction method** becomes a question of balancing finite‑sample bias (0 for MC, small for TD) against variance (large for MC, small for TD) *given the same underlying probability space*.
* **Eligibility traces and λ** provide a *continuum* of estimators indexed by the distribution of the random horizon \(N\), each rigorously integrable thanks to the dominated convergence theorem.
* **Batch least‑squares** (LSTD, LSPI) are justified as *empirical‑risk minimisers* over \(L^2(\rho_\pi)\), with statistical guarantees following directly from uniform law‑of‑large‑numbers arguments on standard Borel spaces.

Thus, the entire toolbox of on‑policy value prediction can be seen as progressively more sophisticated ways of estimating the same Lebesgue integral \(v_\pi(s)=\mathbb E_\mu^\pi[G_t\mid S_t=s]\) on the canonical probability space generated by an MDP.
