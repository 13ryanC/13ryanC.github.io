---
date: "2025-06-30"
title: "(Part 1.1) Personal Notes on the Foundations of Reinforcement Learning"
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

## P₀ Core RL Semantics: the RL Problem Statement & the MDP Formalism

### 0.1 Problem Statement

> *Reinforcement Learning* studies how an **agent** ought to choose **actions** from observations so as to maximise a long‑term notion of reward when the **dynamics** of the environment are unknown.

### 0.2 Markov Decision Process: Definition 0.1

A (discounted, finite) **MDP** is the tuple

$$
\mathcal M=\bigl\langle\mathcal S,\mathcal A,P,R,\gamma\bigr\rangle
$$

with

1. finite **state set** $\mathcal S$;
2. finite **action set** $\mathcal A$;
3. **transition kernel** $P:\mathcal S\times\mathcal A\to\Delta(\mathcal S)$,
    $P(s'|s,a)=\Pr\{S_{t+1}=s'\mid S_t=s,\,A_t=a\}$;
4. **reward function** $R:\mathcal S\times\mathcal A\to\mathbb R$ (possibly stochastic; we absorb any noise into an augmented state);
5. **discount factor** $\gamma\in[0,1)$.

### 0.3 Trajectories & Return

A **trajectory** is the random sequence $\tau=(S_0,A_0,R_0,S_1,\dots)$.
The **discounted return** is

$$
G_0(\tau)=\sum_{t=0}^\infty \gamma^{t} R_t .
$$

### 0.4 Why “Markov”?

The state is *sufficient* in the sense that

$$
\Pr\{S_{t+1}=s'\mid S_0,\dots,S_t=s,A_t=a\}=P(s'|s,a),
$$

i.e. the conditional distribution of next state depends only on the current state–action pair.

---

## P₁ Policies, Value Functions, and Optimality

### 1.1 Policies

| Class                           | Formal Definition                                                                                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **History‑dependent (general)** | A policy is a sequence $\{\pi_t\}_{t\ge0}$ where each $\pi_t$ is a measurable map $\mathcal H_t\!\to\!\Delta(\mathcal A)$ with $\mathcal H_t$ the set of all length‑$t$ histories. |
| **Markov / stationary**         | A single measurable function $\pi:\mathcal S\to\Delta(\mathcal A)$.                                                                                                                |
| **Deterministic stationary**    | The special case $\pi(s)\in\mathcal A$.                                                                                                                                            |

### 1.2 Value Functions

*State value*:

$$
V_\pi(s)=\mathbb E_\pi\!\left[\sum_{t=0}^{\infty}\gamma^{t}R_t\,\middle|\,S_0=s\right].
$$

*Action value*:

$$
Q_\pi(s,a)=\mathbb E_\pi\!\left[\sum_{t=0}^{\infty}\gamma^{t}R_t\,\middle|\,S_0=s,\,A_0=a\right].
$$

### 1.3 Bellman Operators

$$
(\mathcal T_\pi V)(s)=\sum_{a}\pi(a|s)\bigl(R(s,a)+\gamma\sum_{s'}P(s'|s,a)V(s')\bigr).
$$

$$
(\mathcal T_*V)(s)=\max_{a}\bigl(R(s,a)+\gamma\sum_{s'}P(s'|s,a)V(s')\bigr).
$$

Both operators are $\gamma$-contractions in $(\mathbb R^{|\mathcal S|},\|\cdot\|_\infty)$.

### 1.4 Fundamental Theorem of Finite Discounted MDPs

**Theorem 1.1 (Howard, Bellman).**
There exists an optimal deterministic stationary policy $\pi^*$ satisfying

$$
V_{\pi^\ast}(s)=V^{\ast} (s)=\max_{\pi}V_\pi(s),\qquad\forall s\in\mathcal S.
$$

*Proof Sketch.*
Because $\mathcal T^{\ast}$ is a contraction, Banach’s fixed‑point theorem yields a unique $V^{\ast}$ such that $V^{\ast}=\mathcal T^{\ast}V^{\ast}$.

Selecting $\pi^{\ast}(s)\in\arg\max_a\bigl(R(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V^{\ast}(s')\bigr)$ gives a greedy deterministic policy.
One verifies $\mathcal T_{\pi^{\ast}}V^{\ast}= \mathcal T^{\ast} V^{\ast} = V^{\ast}$, so $V_{\pi^{\ast}}=V^{\ast}$. ∎

---

## P₂ Discounting & Horizon Analysis

### 2.1 Why Discount?

*Convergence* (guarantees $\sum_{t}\gamma^t|R_t|$ is finite);
*Time preference*;
*Regularisation* (weights recent rewards more heavily).

### 2.2 Effective Horizon (ε‑truncation)

Let $\epsilon>0$.  Choose

$$
T_\epsilon \;=\;\left\lceil\frac{\log\epsilon}{\log\gamma}\right\rceil
\quad(\text{since }\gamma^{T_\epsilon}\le\epsilon).
$$

Then

$$
\Bigl|\,\sum_{t>T_\epsilon}\gamma^{t}R_t\,\Bigr|\;\le\;\epsilon\,\frac{R_{\max}}{1-\gamma}.
$$

### 2.3 Comparison with Average‑Reward Criterion

Average reward
$\rho_\pi=\lim_{T\to\infty}\frac1T\sum_{t=0}^{T-1}\mathbb E[R_t]$
requires communicating MDPs and ergodicity assumptions; cycles may render $\rho_\pi$ undefined.  Discounting avoids these pitfalls while approximating long horizons when $\gamma$ is close to 1.

---

## P₃ Landscape: Planning, Batch RL, Online RL

| Paradigm               | Given                               | Unknown                     | Core Difficulty                                                        |
| ---------------------- | ----------------------------------- | --------------------------- | ---------------------------------------------------------------------- |
| **Planning**           | Full $P,R$                          | –                           | Purely computational: e.g. value iteration, A\*.                       |
| **Batch / Offline RL** | Dataset $\mathcal D=\{(s,a,r,s')\}$ | Live interaction disallowed | Off‑policy evaluation, distribution shift, uncertainty quantification. |
| **Online RL**          | None (beyond state & action sets)   | $P,R$                       | Exploration–exploitation trade‑off; sample efficiency.                 |

All three ultimately reduce to (approximate) policy optimisation in an MDP.

---

## P₄ Probability & Measure‑Theory Foundations

### 4.1 Probability Spaces

A triple $(\Omega,\mathcal F,\mathbb P)$.
*Random variable* $X:(\Omega,\mathcal F)\to(\mathcal X,\mathcal B(\mathcal X))$.

### 4.2 Ionescu‑Tulcea Theorem

Given a measurable initial distribution and a sequence of stochastic kernels, there exists a unique measure on the infinite product space yielding those marginals.  **Application:** the trajectory distribution induced by $\pi$ and $P$.

### 4.3 Concentration Inequalities

Hoeffding, Bernstein, Azuma; used for high‑probability regret bounds.

### 4.4 Central Limit Theorem (CLT)

For i.i.d. mean‑$\mu$, variance‑$\sigma^2$ variables $X_i$,

$$
\frac{\sqrt n(\bar X_n-\mu)}{\sigma}\;{\xrightarrow{\;d\;}}\;\mathcal N(0,1).
$$

---

## P₅ Computational Foundations

### 5.1 Model of Computation

Classical single‑tape deterministic Turing machine defines *time* and *space* costs.

### 5.2 Complexity Measures

*Time complexity* $T(\varepsilon,|\mathcal S|,|\mathcal A|)$ : cost to compute an $\varepsilon$-optimal policy;
*Sample complexity*: number of transitions required to estimate $V_\pi$ within $\varepsilon$.

### 5.3 Lower Bounds

Any algorithm needs $\Omega\!\bigl(\frac{|\mathcal S||\mathcal A|}{(1-\gamma)^3\varepsilon^2}\bigr)$ samples to estimate $V_\pi$ with additive error $\varepsilon$ (Kearns & Singh, 2002).

---

## P₆ Optimisation & Function Approximation

### 6.1 Inner‑Product Spaces

Let $L^2(\mathcal S,\mu)$ with inner product $\langle f,g\rangle=\sum_s\mu(s)f(s)g(s)$.

### 6.2 Gradient Descent

For differentiable $J(\theta)$, iterate

$$
\theta_{k+1}=\theta_k-\eta_k\nabla_\theta J(\theta_k).
$$

### 6.3 Linear Function Approximation

Approximate $V_\theta(s)=\phi(s)^\top\theta$.
**Projected Bellman Equation**: find $\theta$ such that
$V_\theta=\Pi_{\Phi}\mathcal T_\pi V_\theta$
with $\Pi_\Phi$ the $L^2$-projection onto span $\Phi$.

### 6.4 Convergence Theorem (Tsitsiklis & Van Roy)

Under i.i.d. sampling, diminishing step sizes, and feature matrix full rank, TD(0) with linear approximation converges w\.p. 1 to the unique fixed point of the projected Bellman equation.

---

## P₇ Exploration Principles

### 7.1 Exploration–Exploitation Dilemma

Agent must gather information (explore) while maximising reward (exploit).

### 7.2 Optimism in the Face of Uncertainty (OFU)

Maintain confidence sets $\mathcal P_t$ for transition models; pick policy optimal for the most favourable model in $\mathcal P_t$.

> **Theorem 7.1 (UCB‑VI Regret Bound).**
> In a finite‑horizon MDP with horizon $H$ and diameter $D$, OFU algorithms achieve regret
>
> $$
> \tilde O\bigl(H\sqrt{|\mathcal S||\mathcal A|T}\bigr).
> $$

*Sketch.* Uses Azuma–Hoeffding to bound optimism error; recursion via Bellman equations.

### 7.3 Posterior Sampling (Bayesian)

Sample $P_t\sim\text{Posterior}(P|\,\text{data})$, act greedily in sampled MDP.  Thompson‑sampling–like guarantees yield identical $\tilde O\bigl(H\sqrt{|\mathcal S||\mathcal A|T}\bigr)$ Bayesian regret.

---

## P₈ Key Inequalities & Convex Analysis

### 8.1 Cauchy–Schwarz

$|\langle x,y\rangle|\le\|x\|\,\|y\|$.

### 8.2 Jensen

For convex $\varphi$ and random $X$: $\varphi(\mathbb E[X])\le\mathbb E[\varphi(X)]$.

### 8.3 Bregman Divergence

For strictly convex differentiable $F$:
$D_F(p,q)=F(p)-F(q)-\langle\nabla F(q),p-q\rangle$.
Used to analyse mirror‑descent‑type RL updates.

### 8.4 Convex Hull & Carathéodory

Any point in $\text{conv}(A)\subset\mathbb R^d$ is a convex combination of at most $d\!+\!1$ points of $A$.  Tightens state‑aggregation proofs.

---

## P₉ Broader Stochastic‑Environment Context

### 9.1 Beyond MDPs

*Partially Observable MDPs* (POMDPs) drop the full‑state observability assumption.
*Non‑stationary environments* $P_t$, $R_t$ vary with $t$; require adaptive or meta‑learning techniques.

### 9.2 Why Noise Matters

* Real sensors yield stochastic observations even if the underlying system is deterministic.
* Robust control: compute policies that maximise worst‑case, CVaR, or percentile returns.

### 9.3 Open Research Threads

* Combining offline datasets with online fine‑tuning under covariate shift.
* Safe RL: guaranteeing constraint satisfaction with high probability.

---

## Concluding Roadmap

1. **Study P₀–P₂ in depth**: they form the semantic spine and give the main theorem that legitimises stationary optimal policies.
2. **Branch to P₄ for formal measure‑theoretic underpinnings** as soon as proofs invoke σ‑algebras or kernels.
3. **Consult P₅–P₆** when implementing or analysing algorithms.
4. **Use P₇ and P₈** to tighten performance guarantees.
5. **Return to P₉** for advanced projects that press against the MDP boundary.

Each cluster can now be fleshed out with worked examples, code snippets, and empirical case studies as your personal notes mature.
