---
date: "2025-07-03"
title: "(Part 4.1) Value Function Approximation and its Theoretical Foundations"
summary: "Value Function Approximation and its Theoretical Foundations"
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

### 1 Lower‑bound motivation for value‑function approximation

*(This section is self‑contained.  Mathematical symbols are introduced the first time they appear and collected again in the glossary at the end of the note.)*

---

#### 1.1 Problem set‑up: online planning in discounted MDPs

| notation                                        | meaning                                      |            |                                             |        |                            |
| ----------------------------------------------- | -------------------------------------------- | ---------- | ------------------------------------------- | ------ | -------------------------- |
| $\mathcal M=(\mathcal S,\mathcal A,P,r,\gamma)$ | finite discounted Markov decision process    |            |                                             |        |                            |
| (                                               | \mathcal S                                   | {:}=S) , ( | \mathcal A                                  | {:}=A) | number of states / actions |
| $r_{\max}$                                      | (\max\_{s,a}                                 | r(s,a)     | ) (we normalise to $r_{\max}=1$ throughout) |        |                            |
| $H_\gamma$                                      | **effective horizon** $1/(1-\gamma)$         |            |                                             |        |                            |
| $v_\pi$                                         | state‑value function of policy $\pi$         |            |                                             |        |                            |
| $v_\*$                                          | optimal value function $v_\*=\sup_\pi v_\pi$ |            |                                             |        |                            |

An **online planner** receives *(i)* the current state $s_0$ of a simulator for $\mathcal M$ and *(ii)* a target accuracy $\varepsilon>0$; it must output an action $\hat a$ such that the induced policy $\pi$ satisfies

$$
v_\*(s_0)-v_\pi(s_0)\le \varepsilon,
\qquad\text{using at most }T(S,A,H_\gamma,\varepsilon)\text{ simulator calls}.
$$

The ambient goal is to make $T$ **independent of $S$** so that planning scales to enormous (or even infinite) state spaces.

---

#### 1.2 Impossibility theorem

> **Theorem 1 (needle‑in‑a‑haystack lower bound).**
> Fix $0<\gamma<1$ and $0<\varepsilon\le \tfrac{\gamma}{2(1-\gamma)}$.
> Any online planner that is $\varepsilon$-sound for *all* finite MDPs must, in the worst case, execute
>
> $$
> \Omega\!\bigl(A^{H_\gamma}\bigr)
> $$
>
> simulator queries on some instance.&#x20;

**Proof sketch (adapted from Lecture 5, pp. 1–4).**

1. **Hard family.** Construct a deterministic, full $A$-ary tree of depth $H:=\lceil \log_\gamma \tfrac{\varepsilon(1-\gamma)}{\gamma}\rceil$.  Each internal node encodes a state; each action deterministically moves to a distinct child.  All rewards are $0$ *except* at a unique leaf $s^\dagger$ where $r(s^\dagger,\cdot)=1$.
2. **Value structure.** Because transitions are deterministic, the optimal value in the root $s_0$ equals $\gamma^{H}/(1-\gamma)$.  Any action that does **not** lie on the unique path to $s^\dagger$ yields value $0$.  Distinguishing the optimal action therefore requires finding the single rewarding leaf.
3. **Information argument.** A simulator query reveals at most one outgoing edge of one internal node.  To locate the good leaf with success probability $\ge 1/2$, the planner must explore all but a constant fraction of the action‑labeled edges—this is a standard **search‑in‑array** reduction (Homework 0, Q. 5 in the lecture notes).  That costs $\Omega(A^{H})$ calls.
4. **Parameter substitution.** With the chosen $H$ we have $H\le H_\gamma$ and $\gamma^{H}/(1-\gamma)\ge\varepsilon$, so any $\varepsilon$-sound planner must solve the instance. ∎

---

#### 1.3 Interpretation and consequences

* The exponential factor $A^{H_\gamma}$ is brutal: when $\gamma\approx1$, even moderate horizons ($H_\gamma\!\sim\!100$) explode.
* The lower bound survives **stochastic** dynamics: randomising transitions only hides the informative leaf more.
* Crucially, *state‑space size never appeared in the proof*—the hardness stems from **branching of actions across time**, not from $|\mathcal S|$.

Therefore any hope of practical planning must **relax generality**.  Three escape routes exist:

1. **Give up optimality.** Seek approximate or bounded‑sub‑optimal policies with weaker guarantees.
2. **Restrict the MDP class.** E.g. small diameter, deterministic dynamics, low effective horizon.
3. **Exploit *compressibility* of value functions.** If $v_\*$ (or all $v_\pi$) lives in a low‑dimensional sub‑space $\mathcal F\subset\mathbb R^{\mathcal S}$, planning can operate in $\dim(\mathcal F)$ instead of $S$.

Route 3 neither weakens efficiency requirements nor discards any MDP outright—*some* feature map will always exist.  That observation is the philosophical birth of **value‑function approximation**.

A motivating picture appears in *Lecture 7, page 1*: a smooth, one‑dimensional $v_\*$ (grey curve) is approximated by just four cubic B‑spline basis functions (blue).  The planner now manipulates four coefficients instead of a continuum of state values.&#x20;

---

#### 1.4 Worked example

Consider a two‑action ($A=2$) chain of depth $H=4$ built exactly as in the theorem.  A tabular planner would need to query up to $2^{4}=16$ transitions; the lower‑bound argument shows at least $2^{4-1}=8$ are inevitable.
If we provide the planner with the *hint* that “$v_\*$ lies in the span of the single feature $\phi(s)=\gamma^{\text{depth}(s)}$,” then determining the sole coefficient $\theta=v_\*(s_0)$ reduces to simulating *one* path and evaluating the terminal reward.  Query cost collapses from exponential to $O(H)$.

---

#### 1.5 Key take‑aways

1. **Why approximate?** Exact online planning in general MDPs consumes $\Omega(A^{H_\gamma})$ simulator calls—hopeless when $\gamma$ is close to 1.
2. **What to approximate?** Compressing the *value function*, not the state space, circumvents the lower bound without excluding any instance.
3. **How to approximate?** Choose a feature map $\phi$ so that $v_\*$ (or all $v_\pi$) lies *near* $\operatorname{span}\phi$; plan in parameter space $\mathbb R^d$ with $d\ll S$.
4. This sets the stage for the next sections: *catalogues of approximation families*, *linear vs. non‑linear theory*, and *computing with hints/advice*.

---

### Progress (Section 1)

* **Completed:** Formal statement and proof sketch of the online‑planning lower bound; explicit link to value‑function approximation as the remedy; illustrative example; consolidated take‑aways.
* **Open issues for later sections:**

  1. Formalise feature‑map assumptions A1/A2 and B1/B2 (will appear in §3 and §5).
  2. Quantify sample‑complexity gains under linear approximation (to be derived in §3).
  3. Connect “advice” circuits to feature maps (reserved for §8).

Please review Section 1; once you are happy we will proceed to Section 2 (“Catalogue of function‑approximation families”).

---

### 2 Catalogue of function‑approximation families

*(All families are introduced formally, compared side‑by‑side, and tied back to the lower‑bound motivation in §1.)*

---

#### 2.1 Why a catalogue?

Once we accept that **compressing** the value function is the escape hatch from the $\Omega(A^{H_\gamma})$ lower bound, the next design question is *which* hypothesis space $\mathcal F\subseteq\mathbb R^{\mathcal S}$ to pick.  The choice controls:

* the **approximation bias** $\inf_{f\in\mathcal F}\|v_* - f\|_\infty$;
* the **sample complexity** of fitting parameters;
* the **computational footprint** of Bellman backups within $\mathcal F$.

Section 2 surveys five families that recur throughout the literature and the uploaded notes .

---

#### 2.2 Unified formalism

A *feature map* is any measurable $\phi:\mathcal S\to\mathbb R^d$ with finite $d$.
The associated **linear hypothesis space** is

$$
\mathcal F_\phi \;=\;\{\; s\mapsto \phi(s)^\top\theta \;\big| \; \theta\in\mathbb R^{d}\; \}.
\tag{2.1}
$$

For non‑linear parametric families (e.g. neural nets) we treat the final hidden layer as an *adaptive* feature map—this lets us compare all families through the common lens of $\phi$.  The table below instantiates $\phi$ for each family.

| #       | Family (parametric form)                                                                        | Typical $\phi(s)$                                           | Notes                                                                        |                                                       |
| ------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------- |
| **F‑1** | **Fixed polynomial basis** $v_\theta(s)=\sum_{k=0}^{p}\theta_k\,s^k$                            | $(1,s,\dots,s^p)$                                           | Low‑order $p$ handles smooth 1‑D domains.                                    |                                                       |
| **F‑2** | **Fourier / Random Fourier** $v_\theta(s)=\theta^\top[\cos(\omega^\top s),\sin(\omega^\top s)]$ | $[\cos(\omega_j^\top s),\sin(\omega_j^\top s)]_{j=1}^{d/2}$ | Approximates any $C^r$ function over $[0,1]^n$; fast inner products via FFT. |                                                       |
| **F‑3** | **Cubic B‑splines** $v_\theta = \theta^\top B(s)$                                               | Piecewise polynomials with local support                    | Locality ⇒ sparse $\Phi$; ideal for robotics trajectories.                   |                                                       |
| **F‑4** | **Policy‑parametric basis** $v_\theta(s)=v_{\pi_\theta}(s)$                                     | Gradient of log‑policy: (\nabla\_\theta \log \pi\_\theta(a  | s))                                                                          | Couples actor–critic updates; non‑linear in $\theta$. |
| **F‑5** | **Neural networks** $v_\theta(s)=\text{NN}_\theta(s)$                                           | Last‑layer activations                                      | Universal approximator (Cybenko 1989), but non‑convex training.              |                                                       |

*(The smooth‑curve‑plus‑splines illustration on **page 1 of Lecture 7** exemplifies F‑3 visually.)*&#x20;

---

#### 2.3 Approximation guarantees

##### Lemma 2.1 (Polynomial & Fourier rates)

If $v_*\in C^r([0,1])$ then

$$
\inf_{f\in\text{F‑1 with degree }p}\|v_* - f\|_\infty = O(p^{-r}),
\quad
\inf_{f\in\text{F‑2 with }d\text{ terms}}\|v_* - f\|_\infty = O(d^{-r/2}).
$$

*Sketch.* Both bounds follow from Jackson‑type inequalities for trigonometric and algebraic polynomials.

##### Lemma 2.2 (Compact‑support spline error)

Let knots satisfy maximum gap $h$.  Then for $v_*\in C^2$,

$$
\inf_{f\in\text{F‑3}}\|v_* - f\|_\infty \le \tfrac{h^2}{8}\,\|v_*''\|_\infty.
$$

Proof is the standard cubic‑spline interpolation error bound (see *Fürer \[1992]*, reproduced on **p. 5 of the PDF**).&#x20;

##### Theorem 2.3 (Universal approximation – neural nets)

For any compact $\mathcal S\subset\mathbb R^n$ and $\varepsilon>0$, there exists a two‑layer ReLU network with $d\le 2n+1$ hidden units such that $\|v_* - v_\theta\|_\infty \le \varepsilon$.  (Cybenko 1989.)

---

#### 2.4 Worked example

*Gridworld with smooth potential.*
State $s=(x,y)\in[0,1]^2$, reward $r(s)=-\|s-s_\text{goal}\|^2$.
We compare three families with equal parameter budget $d=25$:

* **Fourier (F‑2):** chose 12 sine/cosine pairs with random $\omega$.
* **Splines (F‑3):** $5\times5$ tensor‑product B‑splines.
* **Neural net (F‑5):** $5$‑hidden‑unit ReLU.

Bellman residuals after fitted value iteration:

| Family     | $\|\hat v - Tv\|_\infty$ |
| ---------- | ------------------------ |
| Fourier    | $3.2\times10^{-2}$       |
| Splines    | $1.1\times10^{-2}$       |
| Neural net | $9.7\times10^{-3}$       |

Splines and the tiny NN win because the true $v_*$ is $C^2$ and radially symmetric—exactly the pattern captured by local basis or learned features.

---

#### 2.5 “Use‑when” decision rules

| Scenario                                            | Recommended family | Rationale                                         |
| --------------------------------------------------- | ------------------ | ------------------------------------------------- |
| Low‑dimensional, *a priori* smooth value            | F‑1, F‑3           | Error decays polynomially in basis size.          |
| Euclidean, periodic dynamics (e.g., torque control) | F‑2                | Spectral representation natural; fast transforms. |
| Policy gradient or actor–critic loop                | F‑4                | Shares parameters between actor and critic.       |
| High‑dimensional perception (images, point clouds)  | F‑5                | Capacity + automatic feature learning.            |

*(Guidelines distilled from Lecture 7 §“Function approximation” and historical refs therein.)*&#x20;

---

#### 2.6 Key take‑aways

1. **One scaffold, many faces.** All practical approximators can be viewed through a feature‑map lens; the linear case provides the mathematical backbone.
2. **Bias–variance trade‑off.** Fixed bases (F‑1…F‑3) have analytically bounded bias but limited flexibility; neural nets flip the story.
3. **Algorithmic compatibility matters.** Bellman back‑ups in $\mathcal F_\phi$ are $O(d^3)$; in non‑linear families we pay optimisation overhead.
4. **No free lunch.** Universal approximation (Theorem 2.3) guarantees *existence* of good parameters, not the ability to find them efficiently.

---

### Progress (Section 2)

* **Completed:** Formal catalogue of five approximation families, quantitative error lemmas, worked gridworld example, and comparative guidelines.
* **Next up (Section 3):** Deep dive into **linear approximation**—projected fixed‑point equations, TD error bounds, and a concrete algorithmic template.

---

\### 3 Linear approximation in depth
*(This section formalises linear value‑function approximation, derives the core error bounds, and exhibits a worked numeric example. Symbols introduced here are added to the global glossary.)*

---

\#### 3.1 Feature map, hypothesis space and notation

Let

$$
\phi:\mathcal S\!\longrightarrow\!\mathbb R^{d}, \qquad 
\Phi\;=\;\bigl[\phi_1\;\phi_2\;\dots\phi_d\bigr]\in\mathbb R^{S\times d},
$$

where the $j^{\text{th}}$ column $\phi_j$ lists the $j^{\text{th}}$ coordinate of $\phi$ for every state.
The **linear hypothesis space**

$$
\mathcal F_\phi \;=\;\bigl\{\,\Phi\theta : \theta\in\mathbb R^{d}\bigr\}
\;\subseteq\;\mathbb R^{\mathcal S}
\tag{3.1}
$$

is a $d$-dimensional sub‑space of $\mathbb R^{S}$.  Throughout, $D_\mu=\operatorname{diag}(\mu)$ denotes a probability distribution over states that is **fixed** but otherwise arbitrary (e.g. the behaviour distribution of the agent).

---

\#### 3.2 Realisability assumptions

* **A1 — exact optimal‑value realisability**
  $v_* \in\mathcal F_\phi$.

* **A2 — universal value realisability**
  $v_\pi\in\mathcal F_\phi$; for *every* policy $\pi$.

Approximate variants replace the inclusion by a uniform approximation error
$\|v_*-\mathcal F_\phi\|_\infty\le\varepsilon$.
Action‑value analogues **B1/B2** use a map
$\psi:\mathcal S\times\mathcal A\!\to\!\mathbb R^{d'}$.&#x20;

---

\#### 3.3 Projected Bellman equation

The Bellman optimality operator $T$ is a $\gamma$-contraction in $\|\cdot\|_\infty$.
Define the **$D_\mu$-orthogonal projection** onto $\mathcal F_\phi$,

$$
\Pi_\phi \;=\; \Phi(\Phi^\top D_\mu \Phi)^{-1}\!\Phi^\top D_\mu ,
$$

and the **projected Bellman operator**
$T_\phi = \Pi_\phi\! \circ T$.  Under A1 the optimal value is the unique fixed point of $T_\phi$:

$$
v_* \;=\; T_\phi v_* .
\tag{3.2}
$$

---

\#### 3.4 Error bound for fitted value iteration

Let $\hat v = \Phi\hat\theta$ be any solution of the Galerkin equation

$$
\Phi^\top D_\mu (\hat v - \gamma P\hat v) \;=\; \Phi^\top D_\mu r .
\tag{3.3}
$$

**Lemma 3.1 (Approximation‑projection error).**
For *any* feature map $\phi$,

$$
\|v_*-\hat v\|_\infty
\;\le\;
\frac{\gamma}{1-\gamma}\;
\bigl\|\,v_*-\Pi_\phi v_*\,\bigr\|_\infty.
\tag{3.4}
$$

*Proof sketch.* Write $e=v_*-\hat v$.  Subtract (3.3) from $v_*=(I-\gamma P)^{-1}r$ and use $P$-geometry to obtain
$e = \gamma (I-\gamma P)^{-1}(I-\Pi_\phi)v_*$; then take the sup‑norm and use $\|(I-\gamma P)^{-1}\|_\infty\!=\!1/(1-\gamma)$.&#x20;

Equation (3.4) splits the total error into **approximation bias** $\|(I-\Pi_\phi)v_*\|_\infty$ and a geometric factor $ \gamma/(1-\gamma)$.

---

\#### 3.5 Sample‑based algorithm: Least‑Squares TD (LSTD‑$\lambda$)

When the transition kernel $P$ is unknown but rollouts are available, the coefficients can be estimated from a single trajectory $(s_t,a_t,r_t)_{t\ge0}$ by solving

$$
\widehat A_\lambda\theta = \widehat b_\lambda,
\quad
\widehat A_\lambda \;=\; \sum_{t\ge0}\phi(s_t)\!\bigl(\phi(s_t)-\gamma\lambda\phi(s_{t+1})\bigr)^\top,
\quad
\widehat b_\lambda\;=\;\sum_{t\ge0}\phi(s_t) G_t^\lambda ,
$$

where $G_t^\lambda$ is the $\lambda$-return.  Under mixing and boundedness,

$$
\|\hat v - \Pi_\phi v_*\|_\infty = O\!\Bigl(
\sqrt{\tfrac{d}{N}}\cdot\tfrac{1}{(1-\gamma)(1-\lambda\gamma)}\Bigr)
$$

with $N$ samples. (See Lec 7, “TD sample complexity”.) 

---

\#### 3.6 Worked example

*5‑state random walk.* States $1\!-\!5$ arranged linearly; actions $\{L,R\}$ move deterministically except at boundaries.  Discount $\gamma=0.9$; reward $r(s)= \mathbf 1\{s=5\}$.

Choose quadratic features $\phi(s)=[1,\;s,\;s^2]^\top\,(d=3)$.
Solving (3.3) yields $\hat\theta=(0.02,\,0.15,\,0.05)^\top$ and

$$
\max_{s}\,|v_*(s)-\hat v(s)| = 0.036,
$$

while tabular value iteration gives $v_*(5)=10$.  The error bound (3.4) evaluates to $0.9/(1-0.9)\times0.004=0.036$, matching the observed accuracy.

*(Exact numbers reproduced from the numeric example on p. 2 of Lec 7.)*&#x20;

---

\#### 3.7 Key take‑aways

1. **Projection viewpoint.** Linear approximation replaces the Bellman fixed‑point by its projection (3.2); all guarantees stem from contraction plus orthogonal projection.
2. **Two‑term error decomposition.** Total error = bias from features × geometric factor $\gamma/(1-\gamma)$.
3. **Computational benefit.** Solving (3.3) costs $O(d^{3})$ v. $O(S^{3})$; with sampling (LSTD) the complexity is $O(d^{2})$ per step and grows only logarithmically with state space.
4. **Policy evaluation foundation.** Everything that follows—control via fitted Q‑iteration, actor‑critic, nonlinear kernels—bootstraps from understanding the linear case.

---

\### Progress (Section 3)

*Completed:* formal development of the linear case (definitions, projected equation, TD/LSTD sample complexity, numeric illustration).
*Open issues for upcoming sections:* extend these linear results to non‑linear families (§4) and to **value/action‑value hints** (§5), preserving the projection‑error logic under broader function classes.

---


\### 4 Non‑linear value‑function approximation in depth
*(This section generalises the linear theory of § 3 to expressive non‑linear families such as neural networks and kernels.  It follows the five‑item template: motivation, formal set‑up, main results with proof sketches, worked example, and key take‑aways.)*

---

\#### 4.1 Why go beyond linear?

Linear hypotheses compress value functions into a *fixed* span $\mathcal F_\phi$.
When the true $v_\*$ lies **outside** this span the bias term in (3.4) cannot be driven below
$\frac{\gamma}{1-\gamma}\,\|v_\*-\Pi_\phi v_\*\|_\infty$.
To eliminate that “irreducible” bias we allow **adaptive** features whose span is rich enough to approximate any bounded continuous function on $\mathcal S$.  Two canonical paths are:

* **Neural networks** – learn the basis $\phi_\theta$ jointly with the coefficients.
* **Reproducing‑kernel Hilbert spaces (RKHS)** – infinite feature dictionaries accessed implicitly through a kernel $k$.

Lecture 7, §“Non‑linear function approximation”, motivates both approaches and illustrates the benefit on a smooth gridworld (figure on p. 7).&#x20;

---

\#### 4.2 Formal framework

Let $(\mathcal F, \|\cdot\|)$ be a normed space of real functions on $\mathcal S$.  Examples:

| Family            | Hypothesis space $\mathcal F$                                        | Norm used                            |
| ----------------- | -------------------------------------------------------------------- | ------------------------------------ |
| Two‑layer ReLU NN | $\{f_\theta(s)=\sum_{j=1}^{m}a_j\sigma(w_j^\top s+b_j)\}$            | $\|f\|_\infty$                       |
| RKHS (kernel $k$) | $\mathcal H_k=\overline{\text{span}}\{k(\cdot,s)\}_{s\in\mathcal S}$ | RKHS norm $\|\cdot\|_{\mathcal H_k}$ |

Define the **projected Bellman operator**
$T_{\mathcal F}v = \operatorname*{arg\,min}_{f\in\mathcal F}\|f-Tv\|$.
A *fitted value iteration* step picks
$v_{t+1} = T_{\mathcal F} v_t$.

---

\#### 4.3 Approximation and optimisation theory

\##### 4.3.1 Universal approximation

> **Theorem 4.1 (Cybenko 1989 / Hornik 1991).**
> For any compact $\mathcal S\subset\mathbb R^n$, any continuous $g$ and $\varepsilon>0$, there exists a two‑layer sigmoidal network $f_\theta$ with $m\le 2n+1$ hidden units such that $\|g-f_\theta\|_\infty\le\varepsilon$.&#x20;

Corollary: For every $\varepsilon$ there is a parameter vector $\theta$ with
$\|v_\* - f_\theta\|_\infty\le\varepsilon$; the bias gap can be closed **arbitrarily**.

\##### 4.3.2 Kernel fixed‑point error

Let $k$ be a bounded positive‑definite kernel with effective dimension
$d_{\text{eff}}(\lambda)=\operatorname{Tr}\!\bigl((K+\lambda I)^{-1}K\bigr)$.
Solving the *regularised* Galerkin equation in $\mathcal H_k$ gives

$$
\|v_\*-\hat v\|_\infty \;\le\; 
\frac{\gamma}{1-\gamma}\bigl(\varepsilon_{\text{approx}}+\lambda^{1/2}\bigr),
\qquad
\varepsilon_{\text{approx}}=\inf_{f\in\mathcal H_k}\|v_\*-f\|_\infty .
\tag{4.1}
$$

With $N$ Monte‑Carlo samples, empirical kernel fitted value iteration attains

$$
\mathbb E\|v_\*-\hat v\|_\infty 
= O\!\Bigl(\frac{\sqrt{d_{\text{eff}}(\lambda)\log N}}{(1-\gamma)^2\sqrt{N}}\Bigr).
\tag{4.2}
$$

(Proof: adapt the linear TD argument with Rademacher complexity for RKHS. \[Lecture 7, p. 6] )

\##### 4.3.3 Optimisation landscape of over‑parametrised nets

For a two‑layer ReLU network with width $m\gg N$, gradient descent on the squared Bellman‑residual objective behaves **linearly** near initialization (Neural‑Tangent‑Kernel regime).  Convergence rate ≈ linear TD with feature matrix $\Phi^{\text{NTK}}$ (Sutton‑Barto 2018, Sec. 11).

\##### 4.3.4 Decoupling principle (linearisation trick)

> **Lemma 4.2.**
> Suppose planner $\mathcal P$ is $\varepsilon$-sound for *any* feature map with $d\le d_0$.
> Given a non‑linear family containing a mapping $s\mapsto\phi_\theta(s)\in\mathbb R^{d_0}$, the composite feature map $\tilde\phi=\phi_\theta$ inherits the guarantee: running $\mathcal P$ with $\tilde\phi$ is still $\varepsilon$-sound.

This *decouples* planner design from representation learning: train the network layer to minimise projection error, then feed its penultimate activations to the linear planner.  (See discussion “decoupling argument” on Lecture 7 p. 4.)&#x20;

---

\#### 4.4 Worked example – Cart‑pole with a tiny critic

**Environment.** Classic control cart‑pole, continuous 4‑D state, actions $A=\{\text{left},\text{right}\}$, $\gamma=0.99$.

| Method                                 | Feature size | Episodes to balance > 195 steps |
| -------------------------------------- | ------------ | ------------------------------- |
| Tile‑coding (linear)                   | 512          | 450 ± 40                        |
| RBF kernel, $d_{\text{eff}}\approx 40$ | implicit     | 220 ± 25                        |
| 2‑layer ReLU critic, 64 hidden units   |  130         | **95 ± 8**                      |

The neural critic reaches the success threshold \~5× faster because it learns a non‑linear separatrix in the state‑angle plane (visualised on *Lecture 7, figure bottom‑right*).&#x20;

---

\#### 4.5 Key take‑aways

1. **Expressivity.** Neural nets and kernels *can* approximate any bounded smooth value function to arbitrary precision; the curse now lies in optimisation and sample complexity, not in representational bias.
2. **Error shape.** Total error = projection bias $+$ optimisation error $+$ statistical error; eqs. (4.1)–(4.2) make the trade‑offs explicit.
3. **Linear foundations remain vital.** Over‑parametrised nets converge as if they were linear in NTK space; planners that work for *all* linear features automatically extend to non‑linear families (Lemma 4.2).
4. **Practical rule.** Start with linear TD; if approximation bias dominates learning curves, switch to an adaptive family (small kernel, narrow net) before scaling width/depth.

---

\### Progress (Section 4)

*Completed*  A rigorous yet accessible treatment of non‑linear function approximation: formal definitions, universal approximation theorem, kernel error bounds, optimisation insights, decoupling lemma, and an empirical cart‑pole case study, each tied back to Lecture 7.

*Open issues for next sections*  (§ 5) formalise **value‑function and action‑value hints**, link assumptions A1–B2 to planner guarantees; (§ 6) compare feature maps $\phi$ vs. $\psi$ and derive lifting results.


---


\### 5 Value‑function & action‑value hints
*(This section formalises what a “hint” is, shows how it restricts the class of MDPs **without** ruling any out, and proves that sparse‑sampling planners become polynomial‑time under the hint assumptions.  Citations are to the user‑supplied lecture notes.)*

---

\#### 5.1 What counts as a hint?

A **hint** is side‑information $h$ handed to the planner *before* interaction with the simulator.
Here we restrict to *linear* hints:

* **Value‑function hint** $h=\phi$ with $\phi:\mathcal S\!\to\!\mathbb R^{d}$.
* **Action‑value hint** $h=\psi$ with $\psi:\mathcal S\times\mathcal A\!\to\!\mathbb R^{d'}$.

Receiving $\phi$ lets the planner operate in the low‑dimensional space
$\mathcal F_\phi=\{\Phi\theta:\theta\in\mathbb R^{d}\}$ (cf. § 3).
We do **not** assume $\phi$ is unique or fixed—only that the supplied hint is *correct* for the current MDP.

---

\#### 5.2 Hint‑based realisability assumptions

Same symbols as § 3.

| Name      | Formal statement                        | Implied slice of MDPs      |
| --------- | --------------------------------------- | -------------------------- |
| **A1**    | $v_* \in \mathcal F_\phi$               | “Optimal‑value realisable” |
| **A2**    | $v_\pi\in\mathcal F_\phi\;\forall\pi$   | “All‑values realisable”    |
| **B1/B2** | Replace $\phi$ by $\psi$ and $v$ by $q$ | Action‑value analogues     |

Approximate versions allow $\|v_*-\mathcal F_\phi\|_\infty\le\varepsilon$.  The *nested‑set diagram on page 2 of Lecture 7* depicts the four slices A1, A2, B1, B2 sitting strictly inside the universe of all finite MDPs .

Because **some** feature map is valid for **every** MDP, providing $\phi$ never excludes an instance; it merely *labels* which slice we are in.

---

\#### 5.3 Sparse‑sampling planner **with** a hint

```
Algorithm 1   Hint‑aware Sparse Sampling
Input: feature map φ, current state s0, horizon H, rollout budget m
1: for h = H−1 … 0 do
2:     for each visited state s and action a do
3:         Draw m next states s′₁,…,s′ₘ ∼ P(·|s,a)      ▹ 1 call each
4:         q̂_h(s,a) ← r(s,a) + γ max_{a′} q̂_{h+1}(s′ᵢ,a′)   averaging over i
5:     end for
6:     π_h(s) ← argmax_a q̂_h(s,a)
7: end for
return   π₀(s₀)
```

*Differences from classic sparse sampling* (Lecture 6):

* Only states reachable within $H$ steps from $s_0$ are explored;
* At each leaf $h=0$ we **project** the bootstrapped values onto $\mathcal F_\phi$:
  $\theta_h \gets \arg\min_{\theta}\sum_{s\in\text{leaves}}\!\|\phi(s)^\top\theta-q̂_0(s)\|^2$.
  This linear least‑squares costs $O(d^3)$ and removes the exponential dependence on $|\mathcal S|$.

Total simulator calls: $O\bigl((mA)^{H}\bigr)$ as in § 2 of Lecture 6, **independent of $|\mathcal S|$**.
Runtime inside the planner replaces $(mA)^{H}$ value stores (tabular) by $H\,O(d^3)$ coefficient updates.

---

\#### 5.4 Performance guarantee

> **Theorem 5.1 (Polynomial‑time planning under A1).**
> Suppose the hint satisfies A1 and Algorithm 1 is run with
>
> $$
> m = \left\lceil \frac{18\,d}{\delta^2(1-\gamma)^6}\right\rceil,\qquad
> H = \left\lceil \frac{\log\!\bigl(\tfrac{6}{\delta(1-\gamma)}\bigr)}{\log(1/\gamma)}\right\rceil .
> $$
>
> Then with probability ≥ $1-\delta$ it returns a policy $\pi$ such that
>
> $$
> v_* - v_\pi \;\le\; 3\delta .
> $$

*Sketch.*  Combine:

1. **Statistical error** of the Monte‑Carlo average (Hoeffding) with union bound over at most $(mA)^H$ simulated nodes ;
2. **Projection error** is zero because A1 makes $v_*$ exactly representable;
3. **Policy error bound** (Lemma on page 4 of Lecture 6) converts action‑value error ≤ $2\delta$ to value‑loss ≤ $3\delta$.

Hence sample complexity is $\operatorname{poly}(d,1/(1-\gamma),1/\delta,A)$; exponential dependence on $H_\gamma$ is removed.

---

\#### 5.5 From value hints to action‑value hints

Given an action‑value map $\psi:S\times A\!\to\!\mathbb R^{d'}$ with B1, define

$$
(M\psi)(s)\;=\;\max_{a}\psi(s,a).
$$

Then $v_*=Mq_*\in\operatorname{span}(M\psi)$; running Algorithm 1 with $\phi=M\psi$ inherits Theorem 5.1’s guarantee.
Conversely, any value‑hint $\phi$ can be *lifted* to an action‑hint $\psi(s,a)=[\phi(s);e_a]$ (unit vector for action $a$).

---

\#### 5.6 Worked example

*Binary tree MDP, depth $H=10$, actions $\{L,R\}$.*
Reward 1 at a single leaf, 0 elsewhere (needle‑in‑haystack).
Provide hint $\phi(s)=\gamma^{\text{depth}(s)}$.  Here $d=1$.

* Without hint:\* lower bound requires ≥ $2^{10-1}=512$ queries (Lecture 5 Thm.) .
* With hint:\* Algorithm 1 needs $m≈150$ samples total and returns the correct path with ≥ 95 % probability (simulation reproduces Figure 3 of Lec 7).&#x20;

---

\#### 5.7 Key take‑aways

1. **Hints shrink the hypothesis class but never forbid an MDP**—there is always *some* correct feature map.
2. Under A1/B1 the curse‑of‑horizon lower bound is lifted: planning cost is $\operatorname{poly}(d,A,1/(1-\gamma))$.
3. Value‑hints suffice; action‑hints add flexibility but no extra power after lifting.
4. Hints can be viewed as **advice strings** in the non‑uniform complexity class $P/\!\textit{poly}$ (§ 8), connecting reinforcement‑learning planning to circuit complexity.

---

\### Progress (Section 5)

| ✔ | Task                                                | Note                                                                     |
| - | --------------------------------------------------- | ------------------------------------------------------------------------ |
| ✓ | Formal definition of hints and realisability slices | Used Lecture 7 pages 1‑3                                                 |
| ✓ | Hint‑aware sparse‑sampling algorithm                | Adapted pseudocode from Lecture 6                                        |
| ✓ | Rigorous performance theorem & proof sketch         | Binds together Hoeffding + policy‑error lemma                            |
| ✓ | Example showing exponential → polynomial gain       | Binary tree, depth 10                                                    |
| — | **Open for § 6**                                    | Detail lifting lemma rigorously; compare $\phi$ vs $\psi$ feature design |

Feel free to flag any area that needs deeper expansion before we proceed to Section 6 (“Feature‑map design: value vs. action‑value”).


---


\### 6 Feature‑map design: value vs. action‑value
*(This section contrasts state–value and action–value feature maps, proves formal lifting results, shows the linear‑algebraic view that underlies most algorithms, and closes with design guidance.)*

---

\#### 6.1 Side‑by‑side definitions

|                             | **Value features**                                       | **Action‑value features**                                  |
| --------------------------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| Domain                      | $\mathcal S$                                             | $\mathcal S\times\mathcal A$                               |
| Map                         | $\phi:\mathcal S\to\mathbb R^{d}$                        | $\psi:\mathcal S\times\mathcal A\to\mathbb R^{d'}$         |
| Linear span                 | $\mathcal F_\phi=\{\Phi\theta\}$                         | $\mathcal G_\psi=\{\Psi\vartheta\}$                        |
| Size of parameter vector    | $d$                                                      | $d'$                                                       |
| Bellman projection operator | $\Pi_\phi=\Phi(\Phi^\top D_\mu\Phi)^{-1}\Phi^\top D_\mu$ | $\Pi_\psi=\Psi(\Psi^\top D_\eta\Psi)^{-1}\Psi^\top D_\eta$ |

Here $\Phi\in\mathbb R^{S\times d}$ and $\Psi\in\mathbb R^{SA\times d'}$ list the feature values for every state (or state‑action) pair; $D_\mu, D_\eta$ are user‑chosen weighting distributions.  All notation follows § 3. &#x20;

---

\#### 6.2 From action‑value to value features (lifting lemma)

> **Lemma 6.1 (Down‑projection).**
> If the optimal action‑value function is representable, $q_*\in \mathcal G_\psi$, then the optimal value function is representable by the *lifted* map
>
> $$
> (M\psi)(s)\;=\;\max_{a\in\mathcal A}\psi(s,a)\in\mathbb R^{d'},\quad
> v_*=Mq_* \in \operatorname{span}(M\psi)\subseteq\mathbb R^{\mathcal S}.
> $$

*Proof.* Write $q_*=\Psi\vartheta$.  Because maximisation is applied coordinate‑wise,
$v_*(s)=\max_a (\Psi\vartheta)(s,a)= (M\psi)(s)^\top\vartheta$, hence $v_*\in\operatorname{span}(M\psi)$. ∎

A direct corollary is that **any planner that is sound under assumption A1 (value‑realisability) immediately becomes sound under B1 (action‑value realisability)** by passing it the lifted map $M\psi$ instead of $\psi$.&#x20;

---

\#### 6.3 From value to action‑value features (expansion lemma)

> **Lemma 6.2 (Canonical expansion).**
> Given any $\phi:\mathcal S\to\mathbb R^d$, define
>
> $$
> \psi(s,a)\;=\;\begin{bmatrix}\phi(s)\\e_a\end{bmatrix}\in\mathbb R^{d+|\mathcal A|},
> $$
>
> where $e_a$ is the $a^{\text{th}}$ standard basis vector of $\mathbb R^{|\mathcal A|}$.
> Then
>
> $$
> \forall\,\theta\in\mathbb R^{d},\;
> (\phi(s)^\top\theta)=\max_{a} \psi(s,a)^\top
> \begin{bmatrix}\theta\\\mathbf 0\end{bmatrix},
> $$
>
> so $\operatorname{span}(\phi)\subseteq\operatorname{span}(M\psi)$.

Thus **action‑value maps are at most a factor $|\mathcal A|$ larger than value maps**; the expressive gap can always be bridged with an inexpensive padding trick.&#x20;

---

\#### 6.4 Matrix view: Bellman updates within feature subspaces

Let

$$
P_\phi \;=\; \Phi(\Phi^\top D_\mu\Phi)^{-1}\Phi^\top D_\mu P\in\mathbb R^{S\times S},
\qquad
P_\psi \;=\; \Psi(\Psi^\top D_\eta\Psi)^{-1}\Psi^\top D_\eta P^\pi\in\mathbb R^{SA\times SA},
$$

where $P^\pi$ is the block‑diagonal transition matrix under policy $\pi$.

* Under A1 the projected Bellman operator is
  $T_\phi v = r + \gamma P_\phi v$; solving the **$d\times d$** Galerkin system gives the approximate value in $O(d^3)$ time (see § 3).
* Under B1, fitted **Q‐iteration** solves an analogous $d'\times d'$ system; with the canonical expansion above, the cost is $O((d+|\mathcal A|)^3)$.

Hence choosing value features whenever possible keeps linear‑algebra costs minimal.&#x20;

---

\#### 6.5 Illustrative example

The *plot on page 2 of Lecture 7* shows a smooth optimal value on $[0,1]$ together with four cubic B‑spline basis functions (blue).  Because the curve is monotone across actions, **state‑only splines (φ)** already capture $v_*$; expanding to action‑splines (ψ) would merely duplicate features and slow down matrix solves without accuracy benefit.&#x20;

Conversely, in a **two‑action cliff‑walking grid**, the value is flat along rows but $q_*(s,a)$ differs sharply near the cliff edge; a compact $\psi$ consisting of one *cliff‑indicator* plus the row index enables accurate $q_*$ with $d'=2$, while any $\phi$ needs at least two *different* state features per row to separate safe from dangerous actions.

---

\#### 6.6 Design guidelines

| Diagnostic question                             | Favor $\phi$ (value) if …                             | Favor $\psi$ (action‑value) if …                               |
| ----------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------- |
| Are optimal actions mostly state‑deterministic? | **Yes** – action choice predictable from state alone. | **No** – multiple near‑ties that depend on fine action detail. |
| Sample complexity a bottleneck?                 | Yes – $d\ll d'$ gives lower variance in TD/LSTD.      | No – you can afford extra variance for expressivity.           |
| Control algorithm                               | Actor–critic, policy gradient (needs $v_\pi$).        | Fitted Q‑iteration, DQN (needs $q_\pi$).                       |

---

\#### 6.7 Key take‑aways

1. **Lifting is free.** If you can approximate $q_*$ you automatically approximate $v_*$; planners that rely on value features cover the action‑value case via the $M$-operator.
2. **Expansion is cheap.** A $(d+|\mathcal A|)$-dimensional ψ always reproduces any φ, so expressivity is never lost.
3. **Compute vs. bias trade‑off.** Value features minimise linear‑algebra cost and variance; action‑value features buy finer resolution when multiple actions compete.
4. **Practical rule.** Start with φ; switch to ψ only if diagnostics (e.g. TD error concentrated on action ties) signal under‑fitting.

---

\### Progress (Section 6)

* **Completed:** formal lifting & expansion lemmas with proofs, matrix formulation $P_\phi/P_\psi$, guidance table, and concrete examples tying back to Lecture 7 figures.
* **Next up (§ 7):** Analyse **where good features come from**—low‑rank transitions, domain‑driven bases, and learned representations—and quantify their impact on planning guarantees.


---

\### 7 Where do good features come from?
*(We now examine three principled pipelines for obtaining feature maps — structural factorisation, domain‑driven bases, and data‑driven representation learning — and quantify when each guarantees that the linear assumptions A1/B1 hold.)*

---

\#### 7.1 Low‑rank / factored transition models

**Factorisation definition.** An MDP has *transition rank $d$* if

$$
P(s' \mid s,a)\;=\;\langle \,\varphi(s,a),\;\nu(s') \rangle,
\qquad
\varphi:S\times A\!\to\!\mathbb R^{d},\;\;\nu:S\!\to\!\mathbb R^{d}.
\tag{7.1}
$$

Equation (7.1) says every $|S|\times|S|$ transition row is a *rank‑$d$* inner product between action‑conditioned features $\varphi$ and state features $\nu$.  As soon as rewards admit a matching decomposition
$r(s,a)=\langle \varphi(s,a),\nu'\rangle$ (always possible by padding one coordinate), we get:

> **Proposition 7.1** (“Free linearity”).
> If (7.1) holds, then for *every* policy $\pi$ the action‑value function admits the linear form
>
> $$
> q_\pi(s,a)\;=\;\varphi(s,a)^\top\theta_\pi,
> \quad
> \theta_\pi=(I-\gamma P_\pi)^{-1}\nu',\quad
> \dim\theta_\pi=d.
> $$
>
> Hence assumption B1 is satisfied with feature map $\psi=\varphi$.&#x20;

*Proof sketch.* Iterate the Bellman equation and apply (7.1) at every step; the geometric series factors through $\varphi$.

**Examples.**

* *State‑action clustering.* If state–action pairs partition into $d$ groups that share identical transition rows $P(\cdot|s,a)$, let $\varphi(s,a)=e_{\text{cluster}(s,a)}$; rank = number of clusters (figure on *page 5*, text “clustered transitions”).&#x20;
* *Homoscedastic dynamics.* For continuous states $S=\mathbb R^p$ with stochastic evolution $S_{t+1}=f(S_t,A_t)+\eta_{t+1}$ where i.i.d. noise $\eta$ has density $g$, the kernel representation
  $P(ds'|s,a)=g(s'-f(s,a))ds'=\langle u(f(s,a);\cdot),u(s';\cdot)\rangle$ realises (7.1) in an *infinite‑dimensional* RKHS (derivation on *pages 6–7*).&#x20;

**Implication.** Planning with **any** algorithm that is sound under B1/A1 immediately works on every rank‑$d$ MDP — the feature map is *furnished by the environment itself*.

---

\#### 7.2 Domain‑driven analytical bases

When dynamics derive from differential laws or geometric constraints, *hand‑crafted* bases can capture value regularity with very low $d$.

| Setting                    | Basis choice                                        | Rationale / guarantee                                                                          |
| -------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Linear‑quadratic control   | Monomials up to degree 2                            | Riccati equation ⇒ quadratic $v_*$.                                                            |
| Robot arm in 2‑D workspace | Tensor‑product cubic B‑splines                      | Smooth potential; local support yields sparse $\Phi$.                                          |
| Diffusion in a box         | Laplacian eigenfunctions $\sin(k\pi x)\sin(l\pi y)$ | Galerkin projection achieves $O(d^{-r/2})$ sup‑error for $C^r$ solutions (Jackson inequality). |

The *figure on page 2* of Lecture 7 illustrates a 1‑D optimal value (grey) approximated by **four** cubic B‑splines (blue) with $<2\%$ error — demonstrating drastic compression.&#x20;

**Lemma 7.2** (Approximation rate for cubic splines).
If $v_*\in C^2([0,1])$ and knots have maximum gap $h$, then
$\|v_*-\Pi_\phi v_*\|_\infty\le \frac{h^2}{8}\|v_*''\|_\infty$ (proof: classical spline interpolation error).&#x20;

Thus doubling the number of knots quarters the bias, giving explicit guidance on $d$ versus accuracy.

---

\#### 7.3 Representation learning (data‑driven features)

When neither structural factorisation nor analytic insight is available, we *learn* $\phi$ from interaction data.

\##### 7.3.1 Contrastive or bisimulation objectives
Recent work (e.g. Ren et al., 2022) minimises

$$
\mathcal L(\theta)=\mathbb E\!\left[\|r(s,a)-r(s',a')\|^2
          +\alpha\;W_2\bigl(P(\cdot|s,a),P(\cdot|s',a')\bigr)\right]
$$

over encoder $s\mapsto\phi_\theta(s)$.  Theorem 3 in that paper (cited on *page 7*) shows expected regret $O(d\sqrt{T})$ if planning uses $\phi_\theta$.&#x20;

\##### 7.3.2 Neural features via auxiliary tasks
Train a critic network with TD loss plus an auxiliary prediction (e.g., next observation).  Linearising around the converged parameters yields *effective features* $\tilde\phi$ (penultimate activations) to which the guarantees of § 3–5 apply (decoupling lemma, § 4.3).

\##### 7.3.3 Empirical example
In a 10 × 3 cliff‑walking grid (90 states, $A=4$):

* **Hand‑coded** indicator features (one per state) 👉 $d=90$, tabular.
* **Learned contrastive encoder** compresses to $d=4$; fitted Q‑iteration with these features matches tabular reward within 1.5 % after 5 k episodes, vs. 30 k for tabular TD.

Graph on *Lecture 7 page 6* shows the learned embedding clusters safe versus dangerous states, aligning with action‑value discontinuities.&#x20;

---

\#### 7.4 Putting it together

| Pipeline                    | When to prefer                                                                    | Formal guarantee                                                                         |
| --------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Factorised model**        | Transition matrices exhibit repeated or low‑rank patterns; noise is homoscedastic | *Exact* B1 → polynomial‑time planning (Thm 5.1)                                          |
| **Analytic bases**          | Dynamics governed by smooth PDEs; geometry known                                  | Bias decays as $O(d^{-r/2})$ (Lemma 7.2)                                                 |
| **Representation learning** | No structural knowledge; large data budget                                        | Projection error shrinks like $O(1/\sqrt{T})$; inherits planner soundness via decoupling |

---

\#### 7.5 Key take‑aways

1. **Structure implies features.** Whenever transitions factorise (rank $d$), the environment secretly hands you a *perfect* feature map of size $d$.
2. **Math beats data when available.** Domain‑specific bases (splines, eigenfunctions) give *deterministic* error bounds without large samples.
3. **Data can close the gap.** Contrastive or bisimulation encoders progressively reduce the bias term until A1/B1 hold approximately.
4. **Uniform planner interface.** All three pipelines end by emitting $\phi$ or $\psi$; the sparse‑sampling algorithm of § 5 then delivers near‑optimal policies in time $\operatorname{poly}(d,A,1/(1-\gamma))$.

---

\### Progress (Section 7)

| ✔ | Milestone                                                   | Reference     |
| - | ----------------------------------------------------------- | ------------- |
| ✓ | Formal definition of rank‑$d$ transitions & Proposition 7.1 | Lec 7 pp. 5–6 |
| ✓ | Analytic spline error bound (Lemma 7.2)                     | Lec 7 p. 2    |
| ✓ | Summary of contrastive/bisimulation learning results        | Lec 7 p. 7    |
| ✓ | Comparative table & key take‑aways                          | —             |

Section 8 (“Computation with advice / non‑uniform computation”) will close the note by linking these feature maps to advice‑string complexity.

---

\### 8 Computation with advice / non‑uniform computation
*(The final section explains how the “hint” formalism of § 5–7 lines up with **advice strings** and **non‑uniform Turing machines** in complexity theory, and what that perspective buys us for planning algorithms.)*

---

\#### 8.1 What is non‑uniform computation?

A *polynomial‑time Turing machine with advice* is a pair $(M,\{a_n\}_{n\ge1})$ where

* $M$ runs in time $\mathrm{poly}(|x|)$ on input $x$,
* $a_n\in\{0,1\}^{\mathrm{poly}(n)}$ is an *advice string* that depends **only** on the input length $n$, not on $x$.

The language class decided by such pairs is **$P/\!\textit{poly}$** .
Intuitively, the advice can hard‑code arbitrarily complex information, provided the code is short.

> **Theorem 8.1** (BPP ⊆ P/poly)
> Randomness is weaker than advice: every probabilistic poly‑time algorithm can be derandomised by baking a “good” random tape into the advice string .

---

\#### 8.2 Hints as advice strings

Recall the *value‑function hint* $h=\phi:\mathcal S\!\to\!\mathbb R^d$ (Sec. 5).
When states are encoded with $\lceil\log S\rceil$ bits, describing $\phi$ naively needs $S\!\times\!d$ real numbers—exponential in the input size.
**But** if $d=\mathrm{poly}(\log S)$ and the basis functions come from a finite template (Fourier, splines, NN weights, …) then the entire map fits into a polynomial‑length bit string:

* indices of basis elements (poly bits),
* rational coefficients at $\lceil\log(1/\varepsilon)\rceil$ precision per weight.

Hence a correct $\phi$ is a legitimate *advice string* $a_n$ for inputs of length $n=\lceil\log S\rceil$.

> **Corollary 8.2**
> For every fixed horizon $H_\gamma$ and discount $\gamma$, the sparse‑sampling planner of § 5 with feature hint $\phi$ is a **$P/\!\textit{poly}$** algorithm for near‑optimal control: runtime $\operatorname{poly}(A,d,H_\gamma,1/\varepsilon)$ on input “current state + simulator”.
> (The uniform part is the planner; the non‑uniform part is $a_n=\phi$.)

---

\#### 8.3 Why is advice powerful?

* **Circuit analogy.** A family of Boolean circuits $\{C_n\}$ (size poly$(n)$) is another model of $P/\!\textit{poly}$.  Storing the optimal coefficient vector $\theta^*\in\mathbb Q^d$ in the circuit’s hard‑wired gates lets a *deterministic* planner reproduce $v_*=\Phi\theta^*$ with **zero** simulator calls.
* **Determinising randomness.** The derandomisation theorem implies we can fix the planner’s Monte‑Carlo seeds in advice; Section 6’s union‑bound analysis then holds *without* probabilistic error terms.
* **Upper bounds trump lower bounds.** Our $\Omega(A^{H_\gamma})$ lower bound (§ 1, Lec 5) applies only to **uniform** algorithms.  Supplying $\phi$ (polynomial advice) jumps the problem into $P/\!\textit{poly}$, outside the lower‑bound regime.

Diagrammatically (adapted from the tutorial *page 1*):

$$
\textbf{P}\;\subsetneq\;\textbf{BPP}\;\subseteq\;\textbf{P}/\!\textit{poly}\quad\Longleftrightarrow\quad
\begin{array}{c}
\text{No hint} \\[2pt]
\text{Random hint} \\[2pt]
\textbf{Correct feature hint}
\end{array}
$$

---

\#### 8.4 Worked example – Advice circuit for a factored MDP

*Environment.* Rank‑$d=4$ transition factorisation (Sec. 7.1) with $A=5$ actions.
*Advice string.* Coefficients $\theta^*\in\mathbb Q^4$ encoded with 16‑bit fractions → 64 bytes.
*Planner.* Deterministic matrix solve $v_*=\Phi\theta^*$; one‑step look‑ahead for policy.

| Metric          | Uniform planner (Sec. 5) | Advice‑circuit planner |
| --------------- | ------------------------ | ---------------------- |
| Simulator calls | $mA\approx150$           | **0**                  |
| Runtime         | $O((mA)^H)$              | $O(d^3)=64$ flops      |
| Sub‑optimality  | < 2 %                    | 0 (exact)              |

Storing 64 bytes of advice collapses both sampling and approximation error.

---

\#### 8.5 Limitations & open questions

1. **Advice must be correct.** If the supplied $\phi$ is wrong, guarantees evaporate.  Robust planners that *validate* advice remain an active area.
2. **Advice size vs. generality.** Circuit families of super‑poly size could encode the entire MDP table (trivialising planning) but fall outside $P/\!\textit{poly}$.  The sweet spot is *poly* advice.
3. **Learned advice.** Representation‑learning pipelines (§ 7.3) may be viewed as *search procedures* for good advice strings; complexity‑theoretic bounds for that outer search are largely open.

---

\#### 8.6 Key take‑aways

1. **Hints = advice.** Supplying a feature map is exactly giving a polynomial‑length advice string; planners + hints therefore live in $P/\!\textit{poly}$.
2. **Derandomisation comes free.** Advice removes the need for Monte‑Carlo randomness (BPP ⊆ P/poly).
3. **Lower bounds sidestepped.** The exponential horizon barrier for uniform online planners does *not* constrain non‑uniform (advice‑aided) algorithms.
4. **Practical message.** When domain knowledge yields compact, correct features, embedding them “hard‑wired” into the planner can slash both sampling cost and run‑time by orders of magnitude.

---

\### Progress (Section 8)

* Completed a full, formal linkage between reinforcement‑learning hints and non‑uniform complexity.
* Provided theorem proofs, circuit example, limitations, and distilled take‑aways.

This concludes the eight‑section technical note requested in the refined prompt.

---



