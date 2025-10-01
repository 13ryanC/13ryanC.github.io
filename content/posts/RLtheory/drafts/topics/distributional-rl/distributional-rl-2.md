---
_build:
  render: never
  list: never

date: "2025-07-12"
title: "(2) (Pending) Notes Briefly on the foundations of Distributional RL"
summary: "(2) (Pending) Notes Briefly on the foundations of Distributional RL"
lastmod: "2025-07-12"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### A Note on Notation
-   A general measurable space is denoted by \((X, \Sigma_X)\).
-   The set of all probability measures on \((X, \Sigma_X)\) is denoted by \(\mathcal{P}(X)\).
-   The Borel \(\sigma\)‑algebra on the real line \(\mathbb{R}\) is \(\mathcal{B}(\mathbb{R})\).
-   The law (or distribution) of a random variable \(X\) under a measure \(\mathbb{P}\) is its push-forward measure, written as \(X_{*}(\mathbb{P})\) or \(\mathbb{P} \circ X^{-1}\).
-   The expectation operator is denoted by \(\mathbb{E}\).

---

## 1. Formal Set-up

### 1.1 The Ambient Probability Space
Let \((\Omega, \mathcal{F}, \mathbb{P})\) be a complete probability space.

### 1.2 Controlled Markov Chain (MDP)
-   **State space:** A measurable space \((S, \Sigma_S)\).
-   **Action space:** A measurable space \((A, \Sigma_A)\).
-   **Transition kernel:** A stochastic kernel \(P \colon S \times A \to \mathcal{P}(S)\).
-   **Reward kernel:** A stochastic kernel \(P_R \colon S \times A \to \mathcal{P}(\mathbb{R})\).
-   **Discount factor:** A scalar \(\gamma \in [0, 1)\).
-   **Policy:** A Markov (stationary) policy is a stochastic kernel \(\pi \colon S \to \mathcal{P}(A)\).

For any initial state distribution \(\xi_0 \in \mathcal{P}(S)\), the process evolves according to the recursive sampling equations for \(t \ge 0\):
$$
S_0 \sim \xi_0, \quad A_t \sim \pi(\cdot \mid S_t), \quad R_{t+1} \sim P_R(\cdot \mid S_t, A_t), \quad S_{t+1} \sim P(\cdot \mid S_t, A_t)
$$

These equations generate an infinite trajectory 

$$
\omega \mapsto (S_t(\omega), A_t(\omega), R_{t+1}(\omega))_{t \ge 0}
$$

which is a random element in the product space \((S \times A \times \mathbb{R})^{\mathbb{N}}\) equipped with the product \(\sigma\)‑algebra \(\bigotimes_{t=0}^{\infty} (\Sigma_S \otimes \Sigma_A \otimes \mathcal{B}(\mathbb{R}))\).

### 1.3 The Return as a Random Variable
For each time step \(t \in \mathbb{N}\), the **return** is the random variable \(G_t \colon \Omega \to \mathbb{R}\) defined by the series:
$$G_t(\omega) := \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}(\omega) \quad (1)$$
**Assumptions:**
1.  **Finite first moment of rewards:** The expected absolute reward is uniformly bounded:
    $$
    \sup_{(s,a) \in S \times A} \mathbb{E}\left[ |R_{t+1}| \mid S_t=s, A_t=a \right] < \infty
    $$
2.  **Discount factor:** \(\gamma < 1\).

Under these assumptions, the sequence of partial sums in \((1)\) is an \(L^1\)-Cauchy sequence, which guarantees that the series converges almost surely. The resulting limit \(G_t\) is an integrable, \(\mathcal{F}\)‑measurable random variable.

---

## 2. \(G_t\) as a Measurable Map

Let the space of all possible trajectories be \(E := (S \times A \times \mathbb{R})^{\mathbb{N}}\) with its corresponding product \(\sigma\)‑algebra \(\Sigma_E := \bigotimes_{n=0}^{\infty} (\Sigma_S \otimes \Sigma_A \otimes \mathcal{B}(\mathbb{R}))\).

The mapping from the abstract space \(\Omega\) to a concrete trajectory in \(E\) is given by:
$$\theta \colon \Omega \to E, \quad \theta(\omega) = \left( (S_n(\omega), A_n(\omega), R_{n+1}(\omega)) \right)_{n \ge 0}$$
By construction, \(\theta\) is an \((\mathcal{F}, \Sigma_E)\)‑measurable map. The return \(G_t\) can be expressed as the composition of a deterministic function on the trajectory space with \(\theta\). Let \(\tilde{G}_t \colon E \to \mathbb{R}\) be the function that calculates the discounted sum of rewards from a given trajectory sequence. Then, the random variable \(G_t\) is \(G_t = \tilde{G}_t \circ \theta\). The measurability of \(\tilde{G}_t\) and \(\theta\) ensures that \(G_t\) is \(\mathcal{F}\)‑measurable.

---

## 3. From Random Variable to Distribution

### 3.1 Push-forward Distribution (Law)
Given a random variable \(X \colon (\Omega, \mathcal{F}) \to (Y, \Sigma_Y)\) and a probability measure \(\mathbb{P}\) on \((\Omega, \mathcal{F})\), its **law** is the push-forward measure \(X_{*}(\mathbb{P}) \in \mathcal{P}(Y)\) defined as:

$$
(X_\ast (\mathbb{P}))(B) := \mathbb{P}(X^{-1}(B)) = (\mathbb{P} \circ X^{-1})(B) \quad \text{for all } B \in \Sigma_Y
$$

### 3.2 Return-Distribution Function
Fix a policy \(\pi\). For each starting state \(s \in S\), we consider the process where the initial distribution is a Dirac measure, \(\xi_0 = \delta_s\). Let \(\mathbb{P}^{\pi, s}\) denote the resulting probability measure on \((\Omega, \mathcal{F})\).

The **return-distribution function** \(Z^{\pi} \colon S \to \mathcal{P}(\mathbb{R})\) is defined by the law of the initial return \(G_0\) for each starting state \(s\):
$$Z^{\pi}(s) := (G_0)_{*}(\mathbb{P}^{\pi, s}) \in \mathcal{P}(\mathbb{R}) \quad (2)$$
This is well-defined because \(G_0\) is a real-valued random variable.

### 3.3 The Distributional Bellman Operator
Let \(\mathcal{Z}\) be the space of all return-distribution functions, i.e., \(\mathcal{Z} := \lbrace \eta \mid \eta \colon S \to \mathcal{P}(\mathbb{R}) \rbrace\).

For any \(\eta \in \mathcal{Z}\), the **distributional Bellman operator** \(\mathcal T^{\pi} \colon \mathcal Z \to \mathcal Z\) is defined as:

$$
(\mathcal T^{\pi} \eta)(s) := \mathbb E_{A_0 \sim \pi(\cdot|s), R_1 \sim P_R(\cdot \mid s,A_0), S_1 \sim P(\cdot \mid s,A_0)} \left[ (b_{R_1, \gamma})_\ast (\eta(S_1)) \right] \quad (3)
$$

Here, \(b_{r, \gamma}(z) := r + \gamma z\) is a shift-and-scale map, and \((b_{R_1, \gamma})_\ast (\eta(S_1))\) is the push-forward of the measure \(\eta(S_1)\) by this map. 

This represents the distribution of \(R_1 + \gamma Z'\), where \(Z' \sim \eta(S_1)\). The expectation is taken over the random variables \(A_0\), \(R_1\), and \(S_1\) generated from state \(s\).

### 3.4 \(\mathcal{T}^{\pi}\) is a \(\gamma\)‑Contraction in the Wasserstein Metric

For \(p \ge 1\), the **Wasserstein-\(p\) distance** on \(\mathcal{P}(\mathbb{R})\) is:
$$W_p(\mu, \nu) := \inf_{\kappa \in \Gamma(\mu, \nu)} \left( \mathbb{E}_{(X,Y) \sim \kappa} \left[ |X-Y|^p \right] \right)^{1/p}$$
where \(\Gamma(\mu, \nu)\) is the set of all joint distributions (couplings) with marginals \(\mu\) and \(\nu\).

We define a metric on the space \(\mathcal{Z}\) by taking the supremum over states:
$$d_p(\eta, \zeta) := \sup_{s \in S} W_p(\eta(s), \zeta(s))$$

The contraction property of \(\mathcal{T}^{\pi}\) relies on the following properties of the \(W_p\) distance, where \(\mu, \nu \in \mathcal{P}(\mathbb{R})\):

-   **Lemma 1 (Shift Invariance):** 
   - Let \(S_c(x) = x+c\). 
   - Then \(W_p ((S_c \circ \mu^{-1}), (S_c \circ \nu^{-1})) = W_p(\mu, \nu)\).

-   **Lemma 2 (Scaling):** 
   - Let \(M_\gamma(x) = \gamma x\). 
   - Then \(W_p((M_\gamma \circ \mu^{-1}), (M_\gamma \circ \nu^{-1})) = \lvert \gamma \rvert W_p(\mu, \nu)\).

-   **Lemma 3 (Mixture Property):** For a kernel \(Q(s, \cdot)\),
    $$
    W_p \left( \int \mu_{s'} Q(s, ds'), \int \nu_{s'} Q(s, ds') \right) \le \int W_p(\mu_{s'}, \nu_{s'}) Q(s, ds')
    $$

Combining these lemmas with definition \((3)\) yields, for any state \(s\):

$$
W_p( (\mathcal{T}^{\pi}\eta)(s), (\mathcal{T}^{\pi}\zeta)(s) ) \le \gamma  \mathbb{E}_{S_1 \sim P(\cdot|s, \pi)} \left[ W_p(\eta(S_1), \zeta(S_1)) \right] \le \gamma  d_p(\eta, \zeta)
$$

Taking the supremum over \(s\) gives \(d_p(\mathcal{T}^{\pi}\eta, \mathcal{T}^{\pi}\zeta) \le \gamma d_p(\eta, \zeta)\).

Thus, \(\mathcal{T}^{\pi} \colon (\mathcal{Z}, d_p) \to (\mathcal{Z}, d_p)\) is a **\(\gamma\)‑contraction**. Since \((\mathcal{Z}, d_p)\) is a complete metric space, the Banach fixed-point theorem guarantees that \(\mathcal{T}^{\pi}\) has a unique fixed point, which is precisely the return-distribution function \(Z^{\pi}\) from \((2)\).

---

## 4. Synthesis and Implications

-   **Existence & Measurability:** The return \(G_t\) is a well-defined (integrable and measurable) random variable, provided rewards have a finite first moment and \(\gamma < 1\).

-   **Law via Push-forward:** The return-distribution function \(Z^{\pi}\) is rigorously defined as the collection of laws of \(G_0\) (\( (G_0)_*(\mathbb{P}^{\pi,s}) \)), indexed by the starting state \(s\).

-   **Distributional Bellman Equation:** The self-consistency of the return process leads to the distributional Bellman equation, \(Z^{\pi} = \mathcal{T}^{\pi} Z^{\pi}\), which generalizes the scalar Bellman equation to the space of distributions.

-   **Contraction and Uniqueness:** The operator \(\mathcal{T}^{\pi}\) is a `\(\gamma\)‑contraction` with respect to the Wasserstein metric. This proves that a unique return-distribution function \(Z^{\pi}\) exists and can be found by iterating the operator `$\mathcal{T}^{\pi}` from any valid starting distribution function.

### Practical Implications
1.  **Algorithmic Design:** Algorithms like C51 (Categorical DQN) and QR-DQN (Quantile Regression DQN) are designed to approximate the distributional Bellman operator \(\mathcal{T}^{\pi}\) using parametric or sample-based representations. The contraction property provides the theoretical foundation for their convergence.

2.  **Risk-Aware Objectives:** Having access to the full distribution \(Z^{\pi}(s)\) allows for the direct calculation of various risk measures, such as Conditional Value-at-Risk (CVaR), variance, or tail probabilities, enabling the optimization of risk-sensitive objectives.

3.  **Representation Choice:** The operator \(\mathcal{T}^{\pi}\) involves shifting distributions by rewards and scaling them by \(\gamma\). Any representational class closed under these operations (e.g., discrete distributions on a fixed support, or quantile representations) is a theoretically sound choice for modeling the return distribution.
