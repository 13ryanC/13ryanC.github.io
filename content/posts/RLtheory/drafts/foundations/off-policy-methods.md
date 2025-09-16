---
date: "2025-07-09"
title: "(3.3) Off-Policy Value Prediction and Control" 
summary: "Off-Policy Value Prediction and Control"
lastmod: "2025-07-09"
category: "Notes"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

## 3.3 Off‑Policy Value Prediction & Control — Measure‑Theoretic Re‑Formulation

> Throughout we adopt the formalism of Section 1 (“Mathematical Foundations: Measure‑theoretic set‑up”) in the attached notes. In particular
>
> * **State space** $(S,\mathcal B(S))$ and **action space** $(A,\mathcal B(A))$ are *standard Borel*.
> * A **policy** is a probability kernel $\pi: S\times\mathcal B(A)\to[0,1]$.
> * The **environment** is a unified kernel $\kappa(ds'dr'\mid s,a)$ on $S\times\mathbb R$.&#x20;

Let

$$
\mathbb P^{\mu}_{\mu_0}
:= \text{law of }(S_0,A_0,R_1,S_1,\ldots)
$$

be the **process measure** induced by an *initial* distribution $\mu_0$ on $S$, a **behaviour policy** $\mu$ and the kernel $\kappa$ (Ionescu–Tulcea Thm. 1.7.3) .
For any *target* policy $\pi$ we wish to compute—or learn to maximise—the value

$$
v_\pi(s)=\mathbb E^{\pi}_{\delta_s}\bigl[G_0\bigr],\qquad 
G_t=\sum_{k=0}^\infty\gamma^{k}R_{t+k+1}, \gamma\in[0,1).
$$

Because data arrive under $\mu\neq\pi$, we face a **distribution‑shift** problem; all subsequent algorithms are ways to estimate (or optimise) $v_\pi$ using samples distributed according to $\mathbb P^{\mu}_{\mu_0}$.

---

### 3.3.1 Q‑Learning — Pathwise Definition and Contraction

*Bellman‑optimality operator.*
For any bounded measurable $q:S\times A\to\mathbb R$

$$
(T^\*q)(s,a):= \int_{S\times\mathbb R}\bigl[r'+\gamma\sup_{a'}q(s',a')\bigr]\kappa(ds'dr'\mid s,a).
$$

$T^\*$ is a $\gamma$-contraction on $(\mathbb L_\infty,\|\cdot\|_\infty)$; hence there is a unique fixed‑point $q^\*$.

*Stochastic approximation viewpoint.*
Let $(S_t,A_t,R_{t+1},S_{t+1})$ be sampled under $\mu$.
Define the **semi‑martingale update**

$$
Q_{t+1}(S_t,A_t)
=Q_t(S_t,A_t)
\alpha_t\bigl[R_{t+1}+\gamma\max_{a'}Q_t(S_{t+1},a')-Q_t(S_t,A_t)\bigr].
$$

Under the Robbins–Monro step‑size conditions and **adequate support** (every $(s,a)$ visited infinitely often a.s.), the O.D.E. method shows $Q_t\to q^\*$ a.s. because the mean field is $T^\*Q-Q$ and inherits the contraction.

*Maximisation bias.*
The sample max $\max_{a'}Q_t(S_{t+1},a')$ is a *biased* estimator of $\sup_{a'}\mathbb E[Q_t(S_{t+1},a')]$ whenever $Q_t$ is noisy. This motivates Double‑Q variants.

---

### 3.3.2 Double Q‑Learning — Bias Cancellation

Maintain two estimates $Q^{(1)},Q^{(2)}$.
At each step flip an unbiased coin $I_t\in\{1,2\}$:

$$
Q^{(I_t)}\gets Q^{(I_t)}
\alpha_t\bigl[R_{t+1}
\gammaQ^{(J_t)}\bigl(S_{t+1},\arg\max_{a'}Q^{(I_t)}(S_{t+1},a')\bigr)
-Q^{(I_t)}(S_t,A_t)\bigr],
$$

with $J_t=3-I_t$.
The action for bootstrapping is chosen by one estimate and *evaluated* by the other, making the target an *unbiased* estimator of $T^\*Q$ in expectation; convergence mirrors the single‑Q case but without systematic overestimation.

---

### 3.3.3 Importance Sampling — Radon–Nikodym Weights

For any finite horizon $T$,

$$
\frac{d\mathbb P^{\pi}_{\mu_0}}{d\mathbb P^{\mu}_{\mu_0}}
\bigl(S_{0:T},A_{0:T-1}\bigr)
=\prod_{t=0}^{T-1}\rho_t,\qquad
\rho_t:=\frac{\pi(A_t\mid S_t)}{\mu(A_t\mid S_t)}.
$$

Thus for any integrable path functional $F$

$$
\mathbb E^{\pi}_{\mu_0}[F]=
\mathbb E^{\mu}_{\mu_0}\Bigl[\Bigl(\prod_{t=0}^{T-1}\rho_t\Bigr)F\Bigr].
$$

*High variance* stems from the product of ratios; modern algorithms substitute **per‑step** weights $c_t=f(\rho_t)\le\rho_t$ that truncate large importance ratios while introducing controlled bias.

---

### 3.3.4 Safe & Efficient Off‑Policy TD

#### (a) Retrace$(\lambda)$

Define truncated traces

$$
c_t := \lambda\min\bigl(1,\bar\rho_t\bigr),\qquad
\bar\rho_t = \frac{\pi(A_t\mid S_t)}{\mu(A_t\mid S_t)}, \lambda\in[0,1].
$$

The multi‑step target for $q$ is

$$
G_t^{\text{Retrace}} =
Q(S_t,A_t)+\sum_{n=0}^{\infty}\gamma^{n}\bigl(\prod_{k=1}^{n}c_{t+k-1}\bigr)
\delta_{t+n},
\quad
\delta_k:=R_{k+1}+\gamma\mathbb E_\pi Q(S_{k+1},\cdot)-Q(S_k,A_k).
$$

Bias is bounded by $1-\lambda$; variance is finite even with unbounded ratios.

#### (b) V‑trace (IMPALA)

Same idea but the state‑value version:   $v$-targets use truncated $c_t$ for bootstrapping and separate coefficients $b_t=\min(1,\bar\rho_t)$ inside the TD error.

#### (c) Emphatic TD (ETD$(\lambda)$)

Constructs *state‑dependent* emphatic weights $m_t$ that solve a linear **occupancy‑ratio** recursion ensuring the expected update follows the true fixed‑point of off‑policy TD, stabilising learning even with radical policy mismatch.

---

### 3.3.5 Gradient‑TD Family — Stability with Function Approximation

When $q_\theta=\phi(s,a)^\top\theta$ (linear) or $q_\theta\approx$ NN, ordinary TD is no longer a stochastic approximation of a contraction; divergence (Baird’s counter‑example) is possible.

* **GTD2 / TDC** formulate the mean‑squared projected‑Bellman‑error
  $J(\theta)=\tfrac12\| \Pi_\mu(T_\pi q_\theta-q_\theta)\|_{\mu}^2$
  and perform *stochastic gradient* descent by introducing an auxiliary weight $w$.
  Updates are two‑time‑scale and provably converge under standard SA conditions.

* **True‑Gradient TD (GTD‑MBA, Saddle‑point TD, etc.)** extend the idea to non‑linear function classes by operating on the primal‑dual (min‑max) form of $J$.

These algorithms preserve stability because they track the gradient of a *convex* objective rather than the fixed‑point of a possibly non‑contractive operator—addressing the third element of Sutton’s “deadly triad”.&#x20;

---

### 3.3.6 Occupancy‑Measure Perspective on Off‑Policy Control

Denote the discounted **state‑action occupancy measure** of $\mu$ by

$$
\rho_{\mu_0}^\mu(C)=\mathbb E^{\mu}_{\mu_0}\Bigl[\sum_{t=0}^\infty\gamma^{t}\mathbf1_{(S_t,A_t)\in C}\Bigr].
$$

For any candidate greedy policy $g_Q(s)=\arg\max_a Q(s,a)$ we can estimate the performance gap

$$
J(g_Q)-J(\mu)=\int_{S\times A}\bigl[r(s,a)+\gamma\mathbb E Q(s',g_Q(s'))-Q(s,a)\bigr]
d\rho_{\mu_0}^{\mu}(s,a),
$$

using the same TD error that drives learning. Control therefore reduces to (i) consistent off‑policy *prediction* of $Q$ and (ii) periodic improvement via $g_Q$ or ε‑greedy variants. The measure‑theoretic foundation guarantees the integral is well‑defined because $\rho_{\mu_0}^{\mu}$ is a finite measure (Theorem 2.2.2).&#x20;

---

## Take‑aways

* Off‑policy methods reinterpret every trajectory produced by a *behaviour* kernel $\mu$ as a random element of the path space endowed with the measure $\mathbb P^{\mu}_{\mu_0}$.
* Importance sampling provides the Radon–Nikodym derivative needed to *transfer* expectations from $\mathbb P^{\mu}_{\mu_0}$ to $\mathbb P^{\pi}_{\mu_0}$, but incurs high variance.
* Trace truncation (Retrace, V‑trace) and emphatic weighting exploit the measurability of kernels to craft *biased‑but‑safe* estimators whose expectations remain correct fixed‑points.
* Gradient‑TD algorithms regain stability in the presence of function approximation by minimising a well‑defined convex objective in $\mathbb L_2(S\times A,\rho_\mu)$.

The measure‑theoretic framework supplies the **regular conditional probabilities**, **Markov operators**, and **occupancy measures** that make each of these steps rigorous across arbitrary (Polish) state–action spaces, lifting classical tabular arguments to the domains encountered in modern reinforcement‑learning theory and practice.
