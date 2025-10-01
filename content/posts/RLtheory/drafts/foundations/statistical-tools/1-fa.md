---
_build:
  render: never
  list: never

date: "2025-07-10"
title: "(2.1) Function Approximation Architectures (Linear, Kernel, Neural)"
summary: "Function Approximation Architectures (Linear, Kernel, Neural)"
lastmod: "2025-07-10"
category: "Notes"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# Function Approximation

Previous analysis reveals that no online planner can satisfy three desirable properties for all Markov Decision Processes (MDPs) defined on general state spaces: 1) achieving a guaranteed fraction of the optimal value, 2) having a per-state runtime polynomial in the horizon \(H\) and the number of actions, and 3) having no dependence on the cardinality of the state space.

As computational efficiency is non-negotiable for practical applications, we must relax the first requirement: universal performance guarantees across all possible MDPs. This is achieved by restricting the class of MDPs a planner is expected to solve. However, rather than excluding certain MDPs outright, we provide the planner with a "hint" about the MDP's structure. The planner is only required to perform well if the hint is correct. Since the hints are general, for any given MDP, a corresponding correct hint exists.

Three tensions motivate function approximation:

1. **Performance** ≥ a fixed fraction of \(v^\*\)  
2. **Runtime per decision** poly\((H,|A|)\)  
3. **State‑space independence**  

Impossibility results (see (4.1) § 5.1) show all three cannot hold simultaneously for general MDPs.  
We keep 2 & 3 and instead supply *hints*—low‑dimensional representations in which the planner is guaranteed to succeed.  Formal definitions of hints, realizability, and approximate realizability now live in (1.1) § 2.2–2.3.
 

### **Hints on Value Functions**

The hints we consider posit that the value functions of an MDP are compressible. Specifically, we assume that either the optimal value function or the value functions of all policies can be accurately represented within a low-dimensional function space.

**Key idea: compressible value functions**
If either \(v^\*\) or \(\lbrace v^\pi\rbrace_{\pi}\) sits (exactly or approximately) in a \(d\)‑dimensional subspace, planning cost can scale with \(d\) instead of \(|S|\).  See (1.2) § 1.1 for the precise performance/approximation trade‑off theorem; the constructive algorithms are in (1.3) § 2–3.
 

Consider an MDP where the state space \(S\) is a subset of a Euclidean space (e.g., an interval on the real line) and the optimal value function \(v^*\) is a smooth, slowly varying function. Such functions can be well-approximated by a linear combination of a few fixed basis functions, such as polynomials or Fourier basis elements. The objective is to design a planner whose runtime depends on the number of these basis functions, rather than the (potentially infinite) number of states. Given such an approximation of \(v^*\), an agent can derive an effective policy through one-step lookahead computations using a simulator.

### **Linear Function Approximation**

**Linear features: (1.1) § 2.2**
A feature map \(\phi:S\to\mathbb R^{d}\) induces the subspace \(\mathcal F_\phi\). Assumptions A1 – A2 (\(v^\*\)‑ and universal‑realizability) and their \(\epsilon\)‑relaxed versions are stated & proved there.

To formalize this, we begin by defining the components of the MDP within a measure-theoretic framework. Let the state space \((S, \mathcal{B}(S))\) and action space \((A, \mathcal{B}(A))\) be **standard Borel spaces**.

A hint is provided through a set of \(d\) **Borel-measurable** basis functions, \(\phi_1, \dots, \phi_d: S \to \mathbb{R}\). These are collected into a single measurable **feature map** \(\phi: S \to \mathbb{R}^d\), where \(\phi(s) = (\phi_1(s), \dots, \phi_d(s))^\top\).

These features define a \(d\)-dimensional subspace, denoted \(\mathcal{F}_\phi\), within the Banach space of all bounded, measurable functions on the state space, \(B(S)\). A function \(f \in B(S)\) belongs to this subspace if it can be expressed as a linear combination of the basis functions:
$$\mathcal{F}_\phi = \{f: S \to \mathbb{R} \mid \exists \theta \in \mathbb{R}^d \text{ s.t. } f(s) = \langle \phi(s), \theta \rangle \text{ for all } s \in S\}$$
This subspace \(\mathcal{F}_\phi\) is the set of all functions representable by our chosen features.

#### **Typical Hints**

The hint connects the MDP's structure to the feature map \(\phi\). The following are standard assumptions.

**Assumption A1 (\(v^*\)-realizability):** The MDP \(M\) and feature map \(\phi\) are such that the optimal value function \(v^*\) is an element of the subspace \(\mathcal{F}_\phi\).
* Note that \(v^*(s) := \sup_{\pi} v_\pi(s)\), where the supremum is over all policy kernels \(\pi(da|s)\). The measurability of \(v^*\) is guaranteed because \(S\) is a standard Borel space.

**Assumption A2 (Universal Value Function Realizability):** For any stationary policy \(\pi\)—defined as a probability kernel from \((S, \mathcal{B}(S))\) to \((A, \mathcal{B}(A))\)—the corresponding state-value function \(v^\pi\) lies in \(\mathcal{F}_\phi\).
* The function \(v^\pi\) is the unique fixed point of the Bellman expectation operator \(T_\pi: B(S) \to B(S)\), where \((T_\pi v)(s) := \int_A \pi(da|s) (r(s,a) + \gamma \int_S v(s') p(ds'|s,a))\).

These assumptions are often relaxed to allow for approximation errors. Using the supremum norm \(\|f\|_\infty = \sup_{s \in S} |f(s)|\) on the space \(B(S)\), we define approximate realizability for some \(\epsilon \ge 0\) as:
$$v \in_\epsilon \mathcal{F}_\phi \quad \iff \quad \inf_{f \in \mathcal{F}_\phi} \|f - v\|_\infty \le \epsilon$$
This leads to the following relaxed assumptions:

**Assumption A1\(_\epsilon\) (Approximate \(v^*\)-realizability):** The MDP \(M\) and feature map \(\phi\) are such that \(v^* \in_\epsilon \mathcal{F}_\phi\).

**Assumption A2\(_\epsilon\) (Approximate Universal Realizability):** For any policy \(\pi\), its value function \(v^\pi\) satisfies \(v^\pi \in_\epsilon \mathcal{F}_\phi\).

#### **Action-Value Hints**

Alternatively, hints can be defined over state-action pairs. Let \(\phi: S \times A \to \mathbb{R}^d\) be a measurable function on the product space \((S \times A, \mathcal{B}(S) \otimes \mathcal{B}(A))\). The corresponding function space \(\mathcal{F}_\phi\) is a subspace of \(B(S \times A)\).

**Assumption B1 (\(q^*\)-realizability):** The optimal action-value function \(q^* \in B(S \times A)\) is an element of \(\mathcal{F}_\phi\).

**Assumption B2 (Universal Action-Value Realizability):** For any policy \(\pi\), its action-value function \(q^\pi \in B(S \times A)\) is an element of \(\mathcal{F}_\phi\).

These can be similarly relaxed to approximate versions, **B1\(_\epsilon\)** and **B2\(_\epsilon\)**.

### Kernel Function Approximation

Kernel methods generalize linear function approximation by implicitly using a high-dimensional feature map. The core idea is to replace the explicit feature map \(\phi(s)\) with a **kernel function** \(k: S \times S \to \mathbb{R}\), which computes an inner product in a high-dimensional feature space without ever instantiating the feature vectors.

This is formalized through a **Reproducing Kernel Hilbert Space (RKHS)**, denoted \(\mathcal{H}_k\). An RKHS is a Hilbert space of functions where all point evaluations are bounded linear functionals. For every kernel \(k\) that is symmetric and positive definite, there exists a unique RKHS \(\mathcal{H}_k\) for which \(k\) is the reproducing kernel.

The function space for approximation is now this RKHS, \(\mathcal{F}_k = \mathcal{H}_k\). By the Representer Theorem, any function \(f \in \mathcal{H}_k\) that minimizes a regularized empirical risk can be written as:
$$f(s) = \sum_{i=1}^N \alpha_i k(s_i, s)$$
where \(\{s_i\}_{i=1}^N \subset S\) is a set of data points (or "support vectors") and \(\alpha_i \in \mathbb{R}\) are coefficients.

#### **Formal Requirements and Hints**

For this framework to be sound, the kernel function \(k(s, s')\) must be a **measurable function** on the product space \((S \times S, \mathcal{B}(S) \otimes \mathcal{B}(S))\). This ensures that all functions within the RKHS are also measurable and thus valid elements of \(B(S)\).

The structural hints are analogous to the linear case, but with the function space defined by the kernel.

**Assumption K1 (\(v^*\)-realizability):** The optimal value function \(v^*\) is an element of the RKHS \(\mathcal{H}_k\).

**Assumption K2 (Universal Realizability):** For any policy \(\pi\), its value function \(v^\pi\) is an element of the RKHS \(\mathcal{H}_k\).

Approximate versions **K1\(_\epsilon\)** and **K2\(_\epsilon\)** are defined accordingly, measuring the distance from a value function to the space \(\mathcal{H}_k\) in the supremum norm.

### Neural Function Approximation

Neural networks provide a powerful class of non-linear function approximators. A feed-forward neural network with \(L\) layers defines a function \(f: S \to \mathbb{R}\) by composing simpler functions:
$$f(s; \theta) = f_L( \dots f_2(f_1(s; \theta_1); \theta_2) \dots; \theta_L)$$
where \(\theta = (\theta_1, \dots, \theta_L)\) are the network parameters (weights and biases). Each layer typically consists of an affine transformation followed by a point-wise activation function \(\sigma(\cdot)\):
$$f_l(z; \theta_l) = \sigma(W_l z + b_l)$$

The function space \(\mathcal{F}_{NN}\) is the set of all functions representable by a given network architecture for all valid parameter vectors \(\theta\). Unlike the linear and kernel cases, this space is **not a linear subspace**, making its analysis significantly more complex.

#### **Formal Requirements and Hints**

For the resulting function \(f(s; \theta)\) to be a valid element of \(B(S)\), its measurability must be guaranteed. This is achieved by requiring the activation functions (e.g., ReLU, sigmoid, tanh) to be **Borel-measurable**. Since affine transformations are continuous (and thus measurable) and the composition of measurable functions is measurable, the entire network is a measurable function of the input state \(s\).

The realizability assumptions are stated in terms of the existence of a suitable parameter vector.

**Assumption N1 (\(v^*\)-realizability):** There exists a parameter vector \(\theta^*\) such that the optimal value function satisfies \(v^*(s) = f(s; \theta^*)\) for all \(s \in S\).

More practically, the approximate version is used:

**Assumption N1\(_\epsilon\) (Approximate \(v^*\)-realizability):** The optimal value function lies in the \(\epsilon\)-neighborhood of the function class, i.e., \(v^* \in_\epsilon \mathcal{F}_{NN}\). This means \(\inf_{\theta} \|v^* - f(\cdot; \theta)\|_\infty \le \epsilon\).

The non-convex nature of \(\mathcal{F}_{NN}\) and the non-linear dependence on \(\theta\) mean that finding the optimal parameters is a challenging optimization problem. Theoretical guarantees for reinforcement learning with neural networks often require stronger assumptions beyond simple realizability, such as assumptions on the optimization landscape or the network's Jacobian.


### **Notes**

#### **Where do features come from?**

A key motivation for linear function approximation comes from **low-rank MDPs**. In such an MDP, the transition kernel has a factored structure. Formally, we assume there exists a reference measure \(\lambda\) on \((S, \mathcal{B}(S))\) (e.g., the counting measure for discrete spaces or the Lebesgue measure for Euclidean spaces). The transition kernel \(p(ds'|s,a)\) is assumed to have a density with respect to \(\lambda\) that factorizes:
$$\frac{p(ds'|s,a)}{d\lambda} = \langle \phi(s,a), \nu(s') \rangle$$
for some measurable feature map \(\phi: S \times A \to \mathbb{R}^d\) and a vector of measurable functions \(\nu: S \to \mathbb{R}^d\). If the reward function \(r(s,a)\) also lies in the span of \(\phi(s,a)\), then it can be shown that the action-value function \(q^\pi\) for any policy \(\pi\) lies in the function space \(\mathcal{F}_\phi\).

One concrete example arises from dynamics with additive, state-independent noise. Consider a state space \(S \subseteq \mathbb{R}^p\) where the dynamics are given by:
$$S_{t+1} = f(S_t, A_t) + \eta_{t+1}$$
Here, \((\eta_t)_t\) is a sequence of i.i.d. random variables with a common density \(g\). The transition kernel takes the form \(p(ds'|s,a) = g(s' - f(s,a)) ds'\), where \(ds'\) denotes the Lebesgue measure. The state-independent nature of the noise introduces smoothness in the value functions, which can often be exploited by feature representations like Fourier bases.

#### **Nonlinear Function Approximation**

The most successful applications of function approximation utilize neural networks, which are a form of nonlinear approximation. A central question is whether planning algorithms can be designed independently of the specific function approximator used. By developing planners that are provably effective for *any* measurable feature map \(\phi\), we establish general principles that may extend to nonlinear settings. If, however, performant algorithms must exploit specific properties of the linear feature map, it serves as a warning that generalizing to nonlinear approximators may be complex. It is therefore a prudent research strategy to first understand the simpler, linear case.
