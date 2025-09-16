---
date: "2025-07-12"
title: "(3) Briefly on Distributional RL"
summary: "(3) Briefly on Distributional RL"
lastmod: "2025-07-12"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


By learning from experience, we mean learning from data in the form of sample interactions with the environment, instead of data from the MDP description of the environment.


| Facet                       | Formal characterisation                                                                                                                                | Implication                                                                              |                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Source of knowledge**     | A sequence of observed trajectories  $(X_t,A_t,R_t)_{t\ge 0}$ drawn from the real environment, *not* the transition kernel $P$ or reward function $R$. | The agent does **not** assume it knows $P(x' \mid x,a)$ or $R(x,a)$; it must infer value purely from data. |
| **Learning objective**      | Estimate functions of the *return random variable* $G^\pi(x)=\sum_{t\ge 0}\gamma^{t}R_t$ (mean, full distribution, risk measures…).                    | Puts statistical estimation (Monte‑Carlo, TD, CTD…) at the heart of RL.                  |                                                          |
| **Algorithmic consequence** | Use **incremental, sample‑based updates** (e.g.\ Monte‑Carlo estimate $V(x)\leftarrow(1-\alpha)V(x)+\alpha g$ or CTD rule Eq. 3.20).               | Scales to large or unknown MDPs; memory need not grow with state–action space.           |                                                          |
| **Practical benefit**       | Removes “often impractical if not infeasible” requirement of a complete model; enables real‑time, on‑policy learning.                                  | RL can be deployed in domains (robotics, finance) where only interactions are available. |                                                          |



### 1.  What is the **“MDP description of the environment”?**

A *finite* Markov Decision Process (MDP) is the tuple

$$
\mathcal{M}= \langle \mathcal{S},\mathcal{A},P,R,\gamma\rangle
$$

| Symbol           | Meaning                                                                  |                                                                                                                                  |
| ---------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| $\mathcal{S}$    | finite set of states                                                     |                                                                                                                                  |
| $\mathcal{A}$    | finite set of actions                                                    |                                                                                                                                  |
| (P(s'            | s,a))                                                                    | **transition model:** the probability that the environment will move to state $s'$ after the agent takes action $a$ in state $s$ |
| $R(s,a)$         | **reward function:** the expected one‑step reward received after $(s,a)$ |                                                                                                                                  |
| $\gamma\in[0,1)$ | discount factor                                                          |                                                                                                                                  |

Having *the MDP description* means the agent is given the *entire* transition matrix $P$ and reward function $R$ up front, so it can compute expectations exactly (e.g., via dynamic programming).

---

### 2. What is **“learning from experience”**?

*Experience* refers to *sampled interaction tuples*

$$
(s_t,a_t,r_{t+1},s_{t+1})
$$

that the agent actually observes while acting in the environment.
Learning from these samples means the agent uses *empirical* estimates—averages over what really happened—rather than *analytical* expectations that require $P$ and $R$.

*Example:*
To estimate a state value $V_\pi(s)=\mathbb{E}_\pi \big[\sum_{k=0}^\infty \gamma^k r_{t+k+1}\big \mid s_t=s \big]$

* **With the MDP description:** one plugs $P$ and $R$ into Bellman equations and solves them exactly.
* **From experience:** one runs the policy $\pi$, records many returns $G^{(i)}$ starting from $s$, and sets

$$
\hat V_\pi(s)=\frac1{N}\sum_{i=1}^{N} G^{(i)}
$$

---

### 3. Why is the distinction important?

| Aspect                 | Using the MDP description                                             | Learning from experience                                         |
| ---------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Knowledge required** | Full, exact model $P,R$                                               | None; the world is a black box                                   |
| **Computation**        | Often involves solving large linear systems (e.g., policy evaluation) | Incremental, sample‑based updates (MC or TD)                     |
| **Error source**       | Only numerical/approximation error                                    | *Estimation noise* due to finite samples                         |
| **Typical methods**    | Dynamic Programming (Policy Iteration, Value Iteration)               | Monte‑Carlo, TD(λ), Q‑learning, Policy Gradient, etc.            |
| **Scalability**        | Hard beyond small state spaces (curse of dimensionality)              | Scales to large or continuous spaces with function approximation |

Hence the quoted sentence simply says:

> *In reinforcement learning we usually **do not** assume the agent is given the transition and reward functions. Instead it must **infer good behaviour solely from the stream of (state, action, reward, next‑state) samples it experiences while interacting with the world***—just as a person or animal learns by trial and error rather than by reading the environment’s equations.

---

#### Common pitfalls and clarifications

1. **“Model‑free” vs. “model‑based”.**
   *Learning from experience* does **not** forbid the agent from **building** an internal model $\hat P, \hat R$ if it wishes—only that such a model must be *learned* from data rather than provided.

2. **On‑policy vs. off‑policy.**
   The experience stream may come from the same policy the agent ultimately wants to evaluate (on‑policy) or from another behaviour policy (off‑policy); both still count as learning from experience.

3. **Sample complexity matters.**
   Because the agent relies on finite samples, there is variance; techniques like bootstrapping (TD) and variance‑reduction baselines are used to trade bias for variance.

---

### Take‑away

> **Learning from experience** = “sample‑based” reinforcement learning
> **Learning from the MDP description** = “planning” with a known model

The former mirrors real‑world situations where the exact dynamics are unknown or too complex to write down, compelling the agent to discover effective behaviour by *doing* rather than by *being told*.




---

### Distributional RL algorithm — working definition

A **distributional reinforcement‑learning (RL) algorithm** is any learning procedure that, for each state (or state–action pair) $x$, maintains and incrementally updates an *estimate of the full probability distribution*

$$
\eta^{\pi}(x):=\mathcal{L}\Bigl(G^{\pi}(x)\Bigr),\qquad  
G^{\pi}(x)=\sum_{t=0}^{\infty}\gamma^{t}R_t,
$$

rather than just the scalar mean $V^{\pi}(x)=\mathbb E[G^{\pi}(x)]$. 

Here $G^{\pi}(x)$ is the (discounted) **return random variable** generated when policy $\pi$ starts from $x$.  

---

#### Essential building blocks

| Component                           | What it does                                                                                                                     | Typical design in Chapter 3                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Representation $\mathcal R$**     | Chooses a finite, tractable family of distributions to store in memory.                                                          | *Categorical grid*: probabilities over *m* evenly‑spaced support points Θ.        |
| **Projection operator $\Pi$**       | Maps an arbitrary target distribution to the representable family, preventing support explosion and guaranteeing bounded memory. | Mean‑preserving linear interpolation (Eq. 3.15).                                  |
| **Target constructor $\mathcal T$** | Forms a bootstrap target from the successor state(s).                                                                            | Push‑forward of the next‑state estimate by the affine map $z \mapsto r+\gamma z$. |
| **Stochastic update rule**          | Blends the current estimate with the projected target using a stepsize α.                                                        | $ \eta(x)\leftarrow (1-\alpha)\eta(x)+\alpha\Pi\mathcal T[\eta(x')]$.       |
| **Policy coupling (control)**       | Specifies how the chosen action affects the target.                                                                              | Greedy w\.r.t. the *mean* of η (distributional Q‑learning).                       |

Combined, these parts define an *algorithmic iteration* over distributions that converges (under standard stepsize schedules) to the fixed point $ \eta^\star = \Pi \mathcal T[\eta^\star]$.&#x20;

---

#### Canonical examples from the chapter

| Algorithm                                 | Prediction vs. control | Key formulae                                                                                       |
| ----------------------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------- |
| **Categorical Monte‑Carlo (CMC)**         | Prediction             | Stores episode return *g* and updates $ \eta(x)\leftarrow(1-\alpha)\eta(x)+\alpha\Pi\delta_g$. |
| **Categorical Temporal‑Difference (CTD)** | Prediction             | Uses one‑step bootstrap $ \Pi(b_{r,\gamma}) \eta(x')$ (Eq. 3.20).                               |
| **Categorical Q‑learning**                | Control                | Same target as CTD but with action $a^\star=\arg\max_a\mathbb E[Z],Z\sim\eta(x',a)$.             |

All three satisfy the definition because they **update probability vectors, not scalars**.&#x20;

---

#### How it differs from classical RL

* **Information retained** Expectation‑based TD collapses the return distribution to a single moment; distributional RL retains variance, skew, and tail risk.
* **Decision criteria** Once the full η is known, the agent can optimise quantiles, CVaR, or other risk‑sensitive objectives without re‑learning.
* **Empirical behaviour** Bootstrapping plus projection introduces *diffusion* (smoother but biased tails) – a phenomenon unique to distributional methods (Fig. 3.3).&#x20;

---


## 1 Formal setting – “Learning from experience”

> **Goal:** turn raw interaction data into an accurate estimate of some target functional $F$ of the return without knowing the MDP dynamics.

---

### 1.1 Environment and policy

An *episodic* Markov Decision Process (MDP) is $\mathcal M=(\mathcal X,\mathcal A, P, R, \gamma)$ with

* state space $\mathcal X$ (finite or measurable),
* action space $\mathcal A$,
* transition kernel $P(x'|x,a)$,
* reward law $R(\cdot|x,a)\subset\mathbb R$,
* discount $\gamma\in[0,1]$.

A **policy** $\pi:\mathcal X\to\mathcal P(\mathcal A)$ induces a *controlled Markov chain*

$$
(X_0,A_0,R_0,X_1,A_1,R_1,\dots)
$$

with
$\Pr(A_t=a|X_t=x)=\pi(a|x),\quad  
\Pr(X_{t+1}=x'|X_t=x,A_t=a)=P(x'|x,a),$
$\Pr(R_t\in \mathrm d r|X_t=x,A_t=a)=R(\mathrm d r|x,a).$

---

### 1.2 Return and target functional

The *return random variable* starting from state $x$ is

$$
G^\pi(x)=\sum_{t=0}^{\infty}\gamma^{t}R_t\text{with }X_0=x.
$$

Classical RL seeks $F[\eta^\pi(x)]$ with $\eta^\pi(x)=\mathcal L(G^\pi(x))$.

* **Value function:** $F(\eta)=\mathbb E_\eta[Z]$.
* **Distributional RL:** $F(\eta)=\eta$ (identity functional).
* **Risk‑sensitive:** $F(\eta)=\text{CVaR}_{\alpha}(\eta)$, etc.

---

### 1.3 Experience = data stream

We **do not** observe $(P,R)$.
Instead we receive **experience**

$$
\mathcal E=\bigl\{(X_k,A_k,R_k,X_{k+1})\bigr\}_{k\ge 0},
$$

i.i.d. only when the behaviour policy is fixed and the chain is rapidly mixed. Chapter 3 states this explicitly:

> “By learning from experience, we mean **from data rather than from the Markov decision‑process description of the environment** … ‘these data are taken from sample interactions’.”&#x20;

Define the filtration $\{\mathcal F_k\}$ with $\mathcal F_k=\sigma(\mathcal E_0,\dots,\mathcal E_{k-1})$.
An *incremental algorithm* is an $\mathcal F_k$-adapted process $\{\hat F_k\}$ updated after each transition.

---

### 1.4 Learning rule (generic)

Let $\alpha_k\in(0,1]$ be a step size.
Given a *target estimator* $T_k$ (measurable w\.r.t. the latest sample), the **stochastic‑approximation update** is

$$
\hat F_{k+1}(X_k)=(1-\alpha_k)\hat F_{k}(X_k)+\alpha_kT_k.
$$

Different choices of $T_k$ recover:

| Algorithm            | Target $T_k$                                                     | Notes                                        |
| -------------------- | ---------------------------------------------------------------- | -------------------------------------------- |
| Monte‑Carlo          | empirical return $G_k$ of the just‑finished episode              | unbiased, high variance                      |
| TD(0)                | $R_k+\gamma\hat V_k(X_{k+1})$                                    | bootstraps, biased but lower variance        |
| Categorical TD (CTD) | $\Pi^{\mathsf c}\bigl[b_{R_k,\gamma}\#\hat\eta_k(X_{k+1})\bigr]$ | distributional, projection Πᶜ preserves mean |

All fit the Robbins–Monro form
$\hat\theta_{k+1}=\hat\theta_k+\alpha_k\bigl(h(\hat\theta_k)+\xi_{k+1}\bigr)$
with noise $\xi_{k+1}:=T_k-\mathbb E[T_k|\mathcal F_k]$.

---

### 1.5 Objective definition (mean‑squared sense)

We say the algorithm **learns from experience** if

$$
\lim_{k\to\infty}\mathbb E\bigl[\lVert \hat F_k - F^\ast\rVert\bigr]=0,
$$

where $F^\ast$ is the true functional (e.g., $V^\pi$ or $\eta^\pi$).
Under standard SA conditions (stepsizes, bounded moments, ergodicity) this holds for MC, TD and CTD; see Chapter 6 for proofs, previewed on page 55 (incremental MC) and page 66 (CTD fixed point) .

---


## 2 Statistical estimators derived from experience

> **Focus of this step:** quantify the *bias*, *variance*, and asymptotic behaviour of the three canonical estimators that Chapter 3 builds on—Monte‑Carlo, TD(0), and Categorical TD—using tools from mathematical statistics and stochastic processes.

---

### 2.1 Monte‑Carlo (MC) estimator

Let the **return** random variable under policy π be

$$
G^\pi(x)=\sum_{t=0}^{\infty}\gamma^{t}R_t,\qquad X_0=x .
$$

Given an i.i.d. (or mixing) sample $g_1,\dots,g_K\sim\eta^{\pi}(x)$ (see Eq. 3.2–3.3) , the *sample‑mean*

$$
\widehat V_K(x)=\frac1K\sum_{k=1}^K g_k
$$

is an **unbiased** estimator of $V^{\pi}(x)=\mathbb E[G^\pi(x)]$ and attains

$$
\operatorname{Var}\bigl[\widehat V_K(x)\bigr]=\frac{\sigma^2(x)}{K},\qquad
\sigma^2(x):=\operatorname{Var}[G^\pi(x)].
$$

*Law of large numbers (LLN).* If the second moment is finite,

$$
\widehat V_K(x)\xrightarrow{a.s.}V^{\pi}(x)\qquad(K\to\infty).
$$

*Central limit theorem (CLT).* If $G^\pi(x)$ has variance σ²(x),

$$
\sqrt{K}\bigl(\widehat V_K(x)-V^{\pi}(x)\bigr)\xrightarrow{d}N(0,\sigma^2(x)).
$$

Thus MC is statistically **efficient** but each estimate uses an *entire episode*, giving high variance when returns are heavy‑tailed or horizons long.

---

### 2.2 TD(0) estimator

With sequential data $(X_k,R_k,X_{k+1})$ (Eq. 3.8) , TD(0) performs

$$
V_{k+1}(X_k)=V_k(X_k)+\alpha_k\Bigl(R_k+\gamma V_k(X_{k+1})-V_k(X_k)\Bigr)\tag{TD}
$$

(Eq. 3.9).  Denote the **TD target**

$$
T_k := R_k+\gamma V_k(X_{k+1}),\qquad \delta_k:=T_k-V_k(X_k).
$$

*Bias.* $\mathbb E[T_k\mid\mathcal F_k]=\mathcal B[V_k](X_k)$ where

$$
\mathcal B[V](x):=\mathbb E_\pi\bigl[R+\gamma V(X')\mid X=x\bigr].
$$

TD is *biased* until $V_k$ is close to the fixed point $V^{\pi}$.

*Variance.* Conditional variance

$$
\operatorname{Var}[T_k\mid\mathcal F_k]=\operatorname{Var}_\pi\bigl[R+\gamma V_k(X')\mid X_k\bigr]
$$

does **not** shrink with horizon – a major gain over MC.

*SA formulation.* Define θₖ the vector of values. TD equals Robbins–Monro

$$
\theta_{k+1}=\theta_k+\alpha_k\bigl(h(\theta_k)+\xi_{k+1}\bigr),
$$

with drift $h(\theta)=\mathbb E_\xi[T-\theta]$. Under the usual conditions (ergodic chain, $\sum_k\alpha_k=\infty,\ \sum_k\alpha_k^2<\infty$) TD converges w\.p.1 to $V^{\pi}$ .

*Asymptotic mean‑squared error.* For small constant α,

$$
\mathbb E\bigl[\lVert V_k-V^{\pi}\rVert^2\bigr]\approx
\frac{\alpha\sigma_{\text{TD}}^2}{2\lambda_{\min}}, 
$$

where λ\_min is the smallest positive eigenvalue of the Bellman operator’s Jacobian; see e.g. Bertsekas‑Tsitsiklis (1996).

---

### 2.3 Categorical Temporal‑Difference (CTD) estimator

CTD works in **measure space**: each state stores a probability vector

$$
p(x)=\bigl(p_1(x),\dots,p_m(x)\bigr)\quad\text{over support }\Theta=\{\theta_i\}.
$$

Update (Eq. 3.20) :

$$
p_i^{new}(x)=p_i(x)+\alpha
\Bigl(\sum_{j=1}^{m}\xi_{ij}(R_k)p_j(x')-p_i(x)\Bigr),\qquad
\xi_{ij}(r):=\text{projection weights}.
$$

#### Bias decomposition

Write $\mathcal P$ the **mean‑preserving projection** Πᶜ (Eq. 3.15).
The one‑step expectation becomes

$$
\mathbb E[p^{new}(x)\mid\mathcal F_k]=p(x)+\alpha\bigl(\mathcal P\mathcal T[p](x)-p(x)\bigr),
$$

with $\mathcal T$ the distributional Bellman operator

$$
\mathcal T[p](x)=\mathbb E_\pi\bigl[(b_{R,\gamma})\#p(X')\mid X=x\bigr].
$$

Hence the **fixed point** satisfies $p^\star=\mathcal P\mathcal T[p^\star]$.
Because $\mathcal P\neq \text{Id}$, *approximation bias* (called *diffusion* on p. 68) remains even after convergence.

#### Variance

Each update moves *at most two* bins due to Πᶜ’s linear interpolation; the per‑step covariance matrix has rank ≤ 2, bounding variance independent of m.

#### Convergence (sketch)

Under ergodicity and step‑size conditions the SA theorem extends to the **probability simplex**: CTD converges almost surely to the unique solution of $p=\mathcal P\mathcal T[p]$.  The proof mirrors classical TD but uses the Cramér metric to guarantee a positive‑definite Lyapunov function (see Chapter 4 remarks).

---

### 2.4 Comparative summary

| Estimator | Target noise var.      | Bias                    | Data needed per update         | Converges to                     |
| --------- | ---------------------- | ----------------------- | ------------------------------ | -------------------------------- |
| MC        | σ²(x) (can be huge)    | 0                       | full episode                   | $V^{\pi}$                        |
| TD        | bounded by reward var. | transient               | single transition              | $V^{\pi}$                        |
| CTD       | ≤ 2 × max p\_j(x)      | persistent (projection) | single transition + vector op. | $\mathcal P\mathcal T$-fixed pt. |

---

### Progress

* **New findings:** Derived exact bias/variance characterisations, embedded MC, TD, CTD in a unified stochastic‑approximation framework, and located CTD’s approximation bias in the projection operator.
* **Open issues for next step:**

  1. Provide explicit Robbins–Monro convergence theorem with assumptions.
  2. Give PAC‑style finite‑sample bounds (sample complexity).
  3. Analyse mean‑preservation formally and show that CTD still preserves $E[G]$.
  4. Illustrate error trade‑offs with a small numerical example.

Let me know if you’d like me to delve into any of these items or continue to the stochastic‑approximation proof and sample‑complexity bounds (Sub‑task 3).
