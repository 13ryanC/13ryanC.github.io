---
_build:
  render: never
  list: never

date: "2025-07-11"
title: "Distributional RL"
summary: "Distributional RL"
lastmod: "2025-07-11"
category: "Notes"
series: ["RL Theory", "RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

## Fundamental Distinction between classical RL and distributional RL

| Aspect                  | **Classical RL**                                                                                                                          | **Distributional RL**                                                                                                                                |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Quantity modelled**   | **Expected return** \(\displaystyle V^\pi(x)=\mathbb{E}\bigl[G^\pi \mid X{=}x\bigr]\) – a single scalar per state (or state–action pair). | **Return *distribution*** \(\displaystyle \mathcal{G}^\pi(x)=\text{Law}\bigl[G^\pi \mid X{=}x\bigr]\) – a full probability law (infinite‑dimensional). |
| **Bellman relation**    | Scalar Bellman equation.                                                                                                                  | *Distributional* Bellman equation \(G^\pi(x)\overset{D}{=}R+\gamma G^\pi(X')\).                                                                   |
| **Objective implied**   | Maximise expectation → *risk‑neutral* policy.                                                                                             | Can optimise arbitrary risk functionals of \(\mathcal{G}\) (variance, CVaR, etc.) → *risk‑sensitive / robust* policies.                                |
| **Error metric**        | \(L^1\)/\(L^2\) norm between scalars.                                                                                                         | Probability metrics between distributions (Wasserstein, KL, Cramér).                                                                                 |
| **Representation**      | A table or function approximator for \(V\) or \(Q\).                                                                                          | A parametric family for \(\mathcal{G}\) (categorical “C51”, quantile “QR‑DQN”, mixture models, particles).                                             |
| **Learning difficulty** | Single target per sample.                                                                                                                 | Target *distribution* must be projected/approximated → heavier computation, stability issues.                                                        |

## How the difference Manifests Across Workflows


| Workflow                                                                                        | Classical recipe                                                                                | Distributional analogue                                                                                                                         | Added value / new issues                                                                                                                                               |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Offline planning** (full model known; dynamic programming, policy iteration, value iteration) | Iterate **Bellman expectation operator** until convergence.                                     | **Distributional Dynamic Programming (DDP)** – iterate distributional Bellman operator, then compute risk‑aware or expectation policies.        | Yields *entire* future‑return law for each state, enabling post‑hoc evaluation of multiple risk criteria without re‑planning.                                          |
| **Online planning** (look‑ahead search such as MCTS, Dyna, model‑predictive control)            | Roll‑outs/back‑ups use mean returns; bandit criteria balance exploration/exploitation on means. | Roll‑outs/back‑ups propagate distributions (e.g., histogram MCTS, quantile tree‑search); bandit logic can use stochastic‑dominance or CVaR‑UCB. | More informative uncertainty estimates improve risk‑aware decision making and better guide exploration in stochastic domains (e.g., games with heavy‑tailed pay‑offs). |
| **Batch / fitted RL** (learn value function from a fixed dataset)                               | Fitted‑Q iteration, LSPI, Neural FQI.                                                           | Distributional FQI: fit a distribution model per state–action, then project distributional Bellman target (e.g., quantile regression loss).     | Captures aleatoric variance present in logged data; downstream policy can optimise different risk profiles without re‑training.                                        |
| **Incremental / TD learning**                                                                   | TD(λ), Q‑learning update a scalar.                                                              | Categorical TD, Quantile TD (QR‑DQN), Implicit Quantile Networks: update the whole distribution per step.                                       | Extra hyper‑parameters (support range, number of quantiles), sensitivity to projection bias and probability metric choice.                                             |


# Motivation

## Expectation hides critical structure

### Why “the mean can mislead”

Formally, let the *return* be the random variable \(G = \sum_{t=0}^{T-1} \gamma^{t} R_t\) with law \(\mathcal G\) on \(\mathbb R\).

The expectation operator \(\mathbb E\) is **many‑to‑one**.

In other words, different distributions that share the same mean collapse to the same value estimate \(V = \mathbb E[G]\).  

Whenever the *shape* of \(\mathcal G\) (variance, skew, multimodality, tail mass) drives good decisions, the scalar \(V\) becomes a lossy—and potentially dangerous—summary.  

Figure 1.2 of the chapter visualises this problem: after 15 rounds of Kuhn poker the agent’s expected gain is £+0.6, yet the most likely outcome is still bankruptcy.

---

### Problem archetypes where expectation hides critical structure

| #     | Archetype (diagnostic pattern)                                                    | Why the mean fails                                                                                                          | Real‑world or benchmark examples                                                                                                                                                                     |
| ----- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Binary‑extreme outcomes** (high‑probability loss vs. low‑probability windfall). | Mean sits between two modes and suggests “mild profit” although *most* trajectories are bad.                                | • Gambling & lotteries • Early‑stage drug discovery (rare blockbuster hit) • Exploration‑heavy RL domains such as *Montezuma’s Revenge* where ≥90 % roll‑outs score 0 but rare ones score very high. |
| **2** | **Catastrophe‑vs‑nominal operation** (safety‑critical control).                   | A tiny crash probability adds a large negative tail; \(\mathbb E[G]\) can still be positive, masking fatal risk.              | • Autonomous driving or drone flight (0.1 % collision rate) • Robotic manipulation near fragile objects • Nuclear power shutdown policies.                                                           |
| **3** | **Heavy‑tailed cost or reward** (power‑law or Lévy statistics).                   | Variance is infinite or huge; the sample mean converges slowly and underestimates risk.                                     | • High‑frequency trading P\&L • Network traffic surges causing queue overflow • Insurance claim sizes.                                                                                               |
| **4** | **Threshold or draw‑down constraints** (ruin barriers).                           | Decision quality depends on staying above a wealth/energy/health barrier, a property of the lower tail, not the mean.       | • Portfolio management with Value‑at‑Risk limits • Battery‑powered robot that must not deplete charge mid‑mission • Inventory control with stock‑out penalties.                                      |
| **5** | **Multi‑modal strategy pay‑offs** (non‑convex return landscape).                  | Averaging distinct modes gives a value that no single policy ever achieves; policy ranking becomes unreliable.              | • Poker variants (Figure 1.2) • Multi‑agent coordination tasks with “win together / lose together” outcomes • Curriculum‑learning environments with disparate sub‑tasks.                             |
| **6** | **Asymmetric loss functions** (utility ≠ identity).                               | When the user’s utility \(u(\cdot)\) is convex or concave, maximising \(\mathbb E[G]\) ≠ maximising \(\mathbb E[u(G)]\).          | • Risk‑averse health‑care dosing (quadratic penalty for overdosing) • Risk‑seeking advertising bids (concave gain for clicks).                                                                       |
| **7** | **Sparse‑reward or rare‑event learning**.                                         | Expectation is near zero for long stretches, providing almost no learning signal even though informative tail events exist. | • Goal‑conditioned robotic pick‑and‑place • Hard‑exploration Atari games • Cyber‑security intrusion detection.                                                                                       |

---

### How to Recognize Risk-Sensitive Tasks in Practice

| Indicator in Data/Model | Interpretation |
|-------------------------|----------------|
| Histogram or kernel density of returns shows multiple modes, heavy skew, or fat tails | Direct evidence that the mean is unrepresentative |
| Empirical variance or CVaR (Conditional Value-at-Risk) is large relative to E[G] | Tail behavior dominates utility |
| Small policy tweaks change higher-order moments (probability of failure) while leaving the mean nearly unchanged | Performance depends on distribution shape |
| Domain requirements mention "safety", "risk", "guarantees", "worst-case", "draw-down", "tail-probability" | Stakeholders already care about risk-sensitive criteria |

---

### Why distributional RL addresses these archetypes

1. **Tail‑aware optimisation** – Policies can be chosen to minimise CVaR, variance, or crash probability directly once \(\mathcal G\) is learned.

2. **Rich exploration signals** – High quantiles or entropy of \(\mathcal G\) guide curiosity toward rare but valuable states.

3. **One‑shot re‑use** – A single learned distribution supports multiple downstream utilities without retraining (e.g., switching from risk‑neutral to risk‑averse planning).

---

### Practical checklist before modelling only the mean

| Question                                                                               | If answer is “yes”, consider distributional RL |
| -------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Could a low‑probability event have large positive *or* catastrophic impact?            |                                                |
| Does the task include hard constraints or safety margins?                              |                                                |
| Are rewards sparse / highly skewed?                                                    |                                                |
| Will different stakeholders evaluate the same policy under different risk preferences? |                                                |

---

### Key takeaway

Whenever the **variance, tails, or multimodality** of future returns influence good decisions—as in the poker histogram on page 4—**expectation alone is an information bottleneck**.  

Such problems are common in finance, safety‑critical robotics, heavy‑tailed operational domains, and sparse‑reward exploration.  

Modelling the **full return distribution** is not a luxury; it is the correct state variable for rational, risk‑aware decision making.

## What are risk-aware objectives and why they are cheap? 

In reinforcement learning we usually optimise the **expected return**

$$
J_{\text{exp}}(\pi) = \mathbb E[G^\pi], \qquad G^\pi = \sum_{t=0}^{T-1} \gamma^{t}R_t
$$

which implicitly treats all variability in the random return \(G^\pi\) as irrelevant.

A **risk‑aware (or risk‑sensitive) objective** replaces the plain expectation by a *functional* \(\rho : \mathcal P (\mathbb R) \to \mathbb R\) that scores **the entire return distribution \(\mathcal G^\pi\)**:

$$
J_{\rho}(\pi)=\rho\bigl(\mathcal G^\pi\bigr).
$$

Typical choices of \(\rho\) emphasise *tail events*, *dispersion* or *asymmetry*:

| Risk functional \(\rho\)              | Formal definition                            | Captures                                      |
| ----------------------------------- | -------------------------------------------- | --------------------------------------------- |
| **Variance‑penalised mean**         | \(\mathbb E[G]-\lambda\text{Var}[G]\)        | Trade‑off accuracy vs. volatility             |
| **Value‑at‑Risk (VaR\(_\alpha\))**    | \(\inf\{z:\Pr(G\le z)\ge\alpha\}\)             | Worst loss not exceeded with prob. \(1-\alpha\) |
| **Conditional VaR / CVaR\(_\alpha\)** | \(\mathbb E[G \mid G\le\text{VAR}_\alpha]\)    | Expected loss *inside* the tail               |
| **Entropic risk**                   | \(-\frac{1}{\eta}\log \mathbb E[e^{-\eta G}]\) | Exponential utility, robust to model error    |
| **Sharpe‑like ratios**              | \(\frac{\mathbb E[G]}{\sqrt{\text{Var}[G]}}\)  | Risk‑adjusted performance                     |

All of these depend on higher‑order statistics (variance, quantiles, cumulants) that the scalar \(V^\pi=\mathbb E[G]\) cannot supply. 

The chapter explicitly motivates such objectives under the banner of *risk‑sensitive reinforcement learning* .

---

### 2  Why do they become *cheap* once you learn the distribution?

| Stage                           | Classical RL (mean only)                                                                                                               | Distributional RL                                                                                                                          |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Learning**                    | Train a value‑function approximator for \(V^\pi\).                                                                                       | Train a model \(\hat{\mathcal G}^\pi\) (categorical, quantile, mixture, …) that outputs the *full* return distribution.                      |
| **Switch to a new risk metric** | **Re‑learn** or fine‑tune because \(V^\pi\) lacks tails; must approximate \(\rho\) indirectly by shaping rewards or redefining TD targets. | **No retraining:** compute \(\rho(\hat{\mathcal G}^\pi)\) by closed‑form formula or a small Monte‑Carlo sample from the stored distribution. |
| **Per‑state cost**              | Extra simulation or network forward passes; sometimes impossible (e.g. CVaR needs quantiles you never estimated).                      | \(O(K)\) arithmetic where \(K\) = number of atoms/quantiles (usually 50–200).                                                                  |
| **Policy improvement**          | Need brand‑new loss/objective; may destabilise training.                                                                               | Plug \(\rho(\hat{\mathcal G}^\pi)\) into the \(\arg\max\) step; gradients flow through the same network.                                       |

**Key intuition:** 

* Learning \(\hat{\mathcal G}^\pi\) is the “expensive” part (it subsumes learning the mean). 

* *Any* coherent risk measure is then a *post‑processing* of that distribution—just a few tensor operations on the output layer. 

* The authors remark that “knowledge of the return function allows us to define behaviours that depend on the full distribution of returns – what is called risk‑sensitive reinforcement learning".

---

### 3  Illustrative examples of the “cheapness”

| Domain                   | Distribution learned once                            | Cheap risk queries afterwards                                              |
| ------------------------ | ---------------------------------------------------- | -------------------------------------------------------------------------- |
| **Autonomous drone**     | Histogram of future altitude loss during manoeuvres. | • Probability of crash < 0 m? </br> • CVaR of worst 1 % drop?                    |
| **Portfolio RL**         | Quantile network for monthly P\&L.                   | • Sharpe ratio </br> • 99 % VaR </br> • Prob. draw‑down > 10 %                         |
| **Game‑playing (Atari)** | C51 distribution over cumulative score.              | • Expected score (for leader‑board) </br> • Variance (for curriculum difficulty) |

Each query is a *constant‑time* reduction over the stored support/probability vectors.

---

### 4  When *isn’t* it cheap?

1. **Representation too coarse.** If the support range is badly truncated or too few quantiles are used, tail estimates become noisy; risk measures lose fidelity.
2. **Epistemic uncertainty dominates.** A pointwise return distribution does not express *model uncertainty*; additional Bayesian layers are needed.
3. **High‑dimensional action selection.** Computing \(\rho(\mathcal G^{\pi}(s,a))\) for thousands of continuous actions may still be costly; actor‑critic architectures alleviate this with a separate policy network.

---

### 5  Take‑aways for practitioners

* **Learn the distribution once, buy many objectives for free.** Budget your compute for accurate distributional learning; the marginal cost of risk metrics is negligible.
* **Match representation ↔ risk measure.** CVaR and VaR require accurate *tail* quantiles → prefer quantile networks; entropic risk needs support outside the clipped range → widen categorical support.
* **Debug with multiple functionals.** During development monitor mean, std, CVaR simultaneously; discrepancies often uncover representation or exploration issues early.

---

> **Bottom line.**
> *Risk‑aware objectives* evaluate policies through functionals (variance, CVaR, entropy …) of the return distribution. In **Distributional RL** these objectives are *cheap* because the costly part—learning \(\mathcal G^\pi\)—is shared, and each new risk criterion reduces to a lightweight computation over already‑predicted atoms or quantiles.&#x20;


## Good unified view of stochasticity?

### A.  Exact theory — does the abstraction subsume classical RL?

#### 1  Set‑up and notation

*Finite discounted MDP* \(M=(\mathcal X,\mathcal A,P,R,\gamma)\) with \(\gamma\in(0,1)\).

For a stationary policy \(\pi\):

* **Return random variable**

  $$
    G^\pi_{x,a}=\sum_{t=0}^{\infty}\gamma^{t}R_t,\quad
           R_t\sim R(X_t,A_t), \quad 
           X_{t+1} \sim P(\cdot\mid X_t,A_t), \quad
           A_t\sim\pi(\cdot\mid X_t)
  $$

* **Return distribution** \(\mathcal Z^\pi_{x,a} = \mathbb P (G^\pi_{x,a}) = \text{Law}(G^\pi_{x,a}) \in \mathcal P_1(\mathbb R)\) (probability measures with finite first moment).

* **Expectation functional**  \(\mathbb E:\mathcal P_1(\mathbb R)\to\mathbb R, \mathbb E[\mathcal Z]=\displaystyle\int zd\mathcal Z(z)\).

---

### 2  Distributional Bellman operator and contraction

Define

$$
(\mathcal{T}^\pi \mathcal{Z})_{x,a}
$$

$$
= \text{Law} (R(x,a) + \gamma \mathcal Z_{X',A'}
$$

$$
X'\sim P(\cdot \mid x,a), \quad A' \sim \pi (\cdot \mid X')
$$

**Theorem 1 (Bellemare‑Dabney‑Munos 2017).**

For any \(p \ge 1\) the operator \(\mathcal T^\pi\) is a \(\gamma\)-contraction in the \(p\)-Wasserstein metric \(W_p\):

$$
W_p \bigl(\mathcal T^\pi \mathcal Z,\mathcal T^\pi \mathcal Z'\bigr)
\le \gamma W_p(\mathcal Z,\mathcal Z')
$$

Hence a unique fixed point \(\mathcal Z^{\pi^\ast}\) exists.

> *Why this matters.*  If the abstraction were “leaky”, we would lack an operator on distributions with the same fundamental Banach‑fixed‑point guarantee that underpins Bellman’s equation.  The theorem gives us parity.

---

### 3  Expectation collapses back to the classical value function

Take expectations on both sides of the distributional fixed‑point equation:

$$
\mathcal Z^{\pi^\ast}_{x,a} 
$$

$$
\overset{D}{=} R(x,a) + \gamma \mathcal Z^{\pi^\ast}_{X',A'}
$$

$$
V^\pi (x,a) := \mathbb E[\mathcal Z^{\pi^\ast}_{x,a}] 
$$

$$
= \mathbb E \bigl[R(x,a) \bigr] + \gamma \mathbb E_{P,\pi} \bigl[V^\pi (X',A') \bigr],
$$

which is exactly the **scalar Bellman expectation equation**.

Therefore

> **Proposition 1.** *The expectation functional is a surjective homomorphism from the space of distributional fixed points onto the space of classical value functions.*

**Consequence.** Distributional RL *strictly contains* classical RL: every classical solution arises as the mean of **one and only one** return distribution, while the reverse is not true.

---

### 4  Risk functionals and unified stochasticity

Because \(\mathcal Z^{\pi*}\) is learned once, any coherent risk functional
\(\rho:\mathcal P_1(\mathbb R)\to\mathbb R\) (e.g., variance, CVaR\(_\alpha\), entropic risk)
is *just a post‑processing step*:

$$
J_\rho(\pi)=\rho\bigl(\mathcal Z^{\pi*}\bigr).
$$

This single abstraction therefore unifies:

* **Risk‑neutral control** (\(\rho=\mathbb E\)) ⇒ classical RL.
* **Risk‑sensitive / robust control** (non‑linear \(\rho\)).
* **Exploration‑driven objectives** (use quantiles, entropy of \(\mathcal Z\), etc.).

Hence the modelling space is closed under all objectives that depend *only* on the law of \(G^\pi\). This is the sense in which distributional RL gives a “unified view of stochasticity”.

---

### 5  Caveat: the optimality operator

For control, define

$$
(\mathcal T\mathcal Z)_{x,a} 
$$

$$
=\text{Law}\left(R(x,a)+\gamma\mathcal Z_{X',a^\star(X')}\right),
\quad a^\star(x')\in\arg\max_{a'}\mathbb E[\mathcal Z_{x',a'}].
$$

Bellemare et al. showed:

* **Theorem 2.**  \(\mathcal T\) *is not* a contraction in any integral probability metric – even though its *mean* counterpart \(T\) *is* a \(\gamma\)-contraction.&#x20;

This *instability* does **not** break the abstraction (the mean is still preserved), but it **does** mean that additional assumptions (e.g., unique optimal policy) or algorithmic tweaks are required for guaranteed convergence in the control setting. Instability at the distribution level, therefore, is the **first place where the abstraction can leak** if we are careless.

---

### B.  Approximate / algorithmic layer — where leaks can appear

| Source of approximation                                     | Possible leak                                                                                 | Known mitigations                                                                                                                                                    |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Projection of targets** (e.g. C51 categorical projection) | Mean of projected distribution ≠ true mean ⇒ scalar Bellman equation no longer holds exactly. | Use *mean‑preserving* projections (Cramér, quantile regression) or add a correction term.                                                                            |
| **Finite support or too few quantiles**                     | Tail risk understated; risk functionals mis‑estimated.                                        | Dynamic support expansion; heteroscedastic quantile spacing.                                                                                                         |
| **Control‑stage instability**                               | Iterates may oscillate in Wasserstein metric although means converge.                         | Perturbations such as *one‑step distributional RL* (Achab 2020), entropy regularisation, or proving convergence under unique‑optimal‑policy assumption. ([arXiv][1]) |

**Take‑away:**  At the *exact* (tabular, infinite‑precision) level distributional RL is a sound, non‑leaky super‑abstraction of classical RL.  *Leaks only arise after we add finite‑dimensional representations or greedy control steps.*  These leaks are well‑understood and can be plugged with appropriate projections, metrics, or regularisation.


> **Mathematically, distributional RL is a *good* abstraction that fully contains classical RL; its leaks stem from practical approximations rather than conceptual unsoundness.**

[1]: https://arxiv.org/pdf/2304.14421?utm_source=chatgpt.com "[PDF] One-Step Distributional Reinforcement Learning - arXiv"


## Classical vs Distributional Reinforcement Learning: A Comparative Analysis

### 1. What each paradigm *learns*

| Paradigm | Formal prediction target | Canonical notation | Governing Bellman relation |
|----------|--------------------------|-------------------|---------------------------|
| **Classical / expectation‑based RL** | **Scalar expected return**<br>$$V^{\pi}(x) = \mathbb{E}\left[\sum_{t \geq 0}\gamma^{t}R_t \mid X_0=x,\pi\right]$$ | $$V^{\pi}:\mathcal{X} \to \mathbb{R}$$ | $$V^{\pi}(x) = \mathbb{E}[R + \gamma V^{\pi}(X') \mid X = x]$$ |
| **Distributional RL** | **Full return distribution**<br>$$\mathcal{Z}^{\pi}(x) = \text{Law}\left(\sum_{t \geq 0}\gamma^{t}R_t \mid X_0=x,\pi\right)$$ | $$\mathcal{Z}^{\pi}:\mathcal{X} \to \mathcal{P}_1(\mathbb{R})$$<br>(probability measures with finite first moment) | $$G^{\pi}(x) \overset{D}{=} R + \gamma G^{\pi}(X')$$<br>(distributional Bellman eq.) |

*Taking the expectation functional \(\mathbb{E}\) of \(\mathcal{Z}^{\pi}\) collapses it **exactly** to \(V^{\pi}\); hence distributional RL strictly subsumes classical RL*.

---

### 2. How we **measure** learning accuracy

| Layer | Classical RL | Distributional RL |
|-------|-------------|------------------|
| **Norm / metric on predictions** | Vector norms on \(\mathbb{R}\) |\(\mathcal{X}\)|}$<br><br>• Mean‑Squared Error (MSE) or Root MSE:<br>  \(\lVert \hat{V} - V^{\pi}\rVert_2\)<br><br>• Mean‑Absolute Error (MAE):<br>  \(\lVert \hat{V} - V^{\pi}\rVert_1\) | **Probability metrics** on \(\mathcal{P}_1(\mathbb{R})\)<br><br>• 1‑Wasserstein distance:<br>  \(W_1(\hat{\mathcal{Z}},\mathcal{Z}^{\pi})\) ([arXiv][1])<br><br>• Cramér/energy distance:<br>  \(\ell_2^2=\int (F_{\hat{Z}}-F_Z)^2dz\) ([arXiv][2])<br><br>• KL divergence / cross‑entropy<br>  (for categorical supports) |
| **Typical loss used in TD update** | Squared TD‑error:<br><br>\((r+\gamma\hat{V}(s')-\hat{V}(s))^2\) | • **Categorical C51** – cross‑entropy between projected target pmf and current pmf ([arXiv][1])<br><br>• **Quantile / IQN** – quantile‑regression (pinball) loss:<br>  \(\rho_{\tau}(u)=u(\tau-\mathbf{1}_{u<0})\)<br>  summed over quantile levels ([arXiv][3]) |
| **Convergence guarantees** | Bellman expectation operator is a \(\gamma\)-contraction in \(L_{\infty}\) | Policy‑evaluation operator is a \(\gamma\)-contraction in \(W_p\) (p‑Wasserstein) ([arXiv][1])<br><br>Control case demands extra care (no contraction) |
| **Error diagnosed in practice** | **RMSVE** over a held‑out state set<br><br>(true values computed via Monte‑Carlo or dynamic programming) ([incompleteideas.net][4]) | **Average \(W_1\)** or **Cramér distance** over states<br><br>Sometimes Earth‑Mover's distance on sampled returns<br><br>For categorical nets: negative log‑likelihood of atoms |

---

### Formal definitions of key probability metrics

**Wasserstein‑\(p\):**
$$W_p(\mu,\nu) = \left(\inf_{\gamma \in \Gamma(\mu,\nu)} \int |x-y|^p  d\gamma(x,y)\right)^{1/p}$$

**Cramér distance** (Rowland et al., 2018):
$$\ell_2^2(\mu,\nu) = \int_{-\infty}^{\infty} (F_{\mu}(z) - F_{\nu}(z))^2  dz$$
where \(F_{\mu}\) is the cumulative‑distribution function. Both metrics metrise weak convergence when first moments are finite.

**Quantile (pinball) loss** (Dabney et al., 2018):

$$
\mathcal L (\theta) = \frac{1}{K} \sum_{i=1}^K (\tau_i - \mathbf 1_{u_i < 0}) u_i, \quad u_i = z^{\text{target}} - \hat{z}_{\theta}^{(i)}
$$

---

## 3. Illustrative micro‑example

| Toy MDP | Classical estimate | Distributional estimate |
|---------|-------------------|------------------------|
| **One‑step coin**: reward \(+5\) w.p. \(0.1\), else \(-1\). | \(V = 0.1 \times 5 + 0.9 \times (-1) = -0.4\) | $$\mathcal{Z} = \begin{cases} +5 & p=0.1\\ -1 & p=0.9 \end{cases}$$ |
| **Error if learner predicts 0** | Absolute value error \(= 0.4\) | Wasserstein‑1 error \(= 0.1 \times |5-0| + 0.9 \times |-1-0| = 1.4\) |
| **Insight** | Scalar error small; agent believes near‑neutral outcome. | Probability metric reveals heavy left‑tail (risk of \(-1\)) and right‑tail (rare \(+5\)). |

A learner optimising only MSE might deem its prediction (\(\approx 0\)) "close", whereas any reasonable \(W_1\)‑based metric flags a large miss in tail mass—mirroring the *Kuhn‑poker* tri‑modal example on *page 4* of the chapter.

---

## 4. Standard evaluation protocols in the literature

| Setting | Classical baseline | Distributional counterpart |
|---------|-------------------|---------------------------|
| **Tabular policy evaluation** | Compute RMSVE against exact dynamic‑programming \(V^{\pi}\). | Compute average \(W_1\) (or Cramér) between learned \(\hat{\mathcal{Z}}\) and analytic \(\mathcal{Z}^{\pi}\) (possible on small chains). |
| **Atari 2600 (Deep RL)** | Report mean human‑normalised score of DQN variants (Mnih et al.). | C51/QR‑DQN report *same* score **plus** distributional diagnostics (average KL or \(W_1\) on held‑out roll‑outs) ([arXiv][1], [arXiv][5]). |
| **Risk‑aware control tasks** | Evaluate CVaR of total reward computed via Monte‑Carlo. | Measure CVaR directly from predicted distributions; also test pinball loss convergence (Dabney 2018) ([arXiv][3]). |

---

## 5. Assumptions you should state explicitly

1. **Finite first moment** of returns (\(\mathbb{E}[|G|] < \infty\)) so \(W_1\) and expectations are well‑defined.
2. **Stationary dynamics** for contraction proofs; non‑stationarity (e.g., opponents learning) breaks guarantees but distributions often remain informative.
3. **Projection bias**: practical algorithms approximate \(\mathcal{Z}\) on finite supports (C51) or a finite set of quantiles; accuracy of risk metrics hinges on the chosen representation ([arXiv][2]).

---

## 6. Key references

* Bellemare, Dabney & Munos, **"A Distributional Perspective on RL"** (C51, Wasserstein contraction) ([arXiv][1])
* Dabney et al., **"Distributional RL with Quantile Regression"** (QR‑DQN) ([arXiv][5])
* Dabney et al., **"Implicit Quantile Networks"** (IQN; continuous quantile set) ([arXiv][3])
* Rowland et al., **"Analysis of Categorical Distributional RL"** (Cramér distance) ([arXiv][2])
* Sutton & Barto, **"Reinforcement Learning: An Introduction"** (2nd ed.) – canonical treatment of expectation‑based RL and RMSVE evaluation ([incompleteideas.net][4])

---

## **Take‑away**

*Classical RL* evaluates **how close a single number per state** is to the true mean return, usually with squared‑error norms.

*Distributional RL* judges **how close an entire probability law** is to the true return distribution, requiring probability metrics (Wasserstein, Cramér, KL) and tailored losses (cross‑entropy, quantile regression).

The richer target subsumes the scalar case and unlocks direct, "cheap" access to risk‑aware criteria—but demands more expressive losses, careful projections, and metrics that respect distributional geometry.

---

[1]: https://arxiv.org/abs/1707.06887?utm_source=chatgpt.com "A Distributional Perspective on Reinforcement Learning"
[2]: https://arxiv.org/abs/1802.08163?utm_source=chatgpt.com "An Analysis of Categorical Distributional Reinforcement Learning"
[3]: https://arxiv.org/abs/1806.06923?utm_source=chatgpt.com "Implicit Quantile Networks for Distributional Reinforcement Learning"
[4]: https://incompleteideas.net/book/bookdraft2018jan1.pdf?utm_source=chatgpt.com "[PDF] Reinforcement Learning: An Introduction ****Complete Draft****"
[5]: https://arxiv.org/abs/1710.10044?utm_source=chatgpt.com "Distributional Reinforcement Learning with Quantile Regression"


## Brief Summary of Trade-offs

| Advantage of distributional view                                                                        | Corresponding cost / caveat                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Can design **safer** or **risk‑seeking** agents; identify catastrophic‑tail events.                     | Requires choosing a **representation** and **probability metric**; poor choices harm convergence.           |
| Provides richer feedback for **exploration** (e.g., optimistic sampling on high quantiles).             | **Bootstrapping instability** stronger; must align projection with SGD‑friendly losses.                     |
| Post‑hoc policy evaluation over many utility functions.                                                 | Higher memory/compute (store tens‑to‑hundreds of atoms or quantiles instead of one scalar).                 |
| Potentially faster learning when the *shape* of reward distribution conveys signal (multi‑modal tasks). | Benefits diminish if environment is almost deterministic; gains depend on quality of distribution estimate. |


## When to Prefer Each Paradigm


| Scenario                                                                              | Classical RL sufficient? | Distributional RL recommended?           |
| ------------------------------------------------------------------------------------- | ------------------------ | ---------------------------------------- |
| Deterministic control or variance‑irrelevant tasks.                                   | ✓                        | –                                        |
| Finance, energy markets, safety‑critical robotics, games with high‑variance pay‑offs. | –                        | ✓                                        |
| Compute‑constrained embedded systems.                                                 | ✓                        | – (unless catastrophic‑risk critical)    |
| Multi‑objective or late‑binding utility (utility chosen after learning).              | –                        | ✓ (learn once, evaluate many objectives) |


### 4. **Distributional RL**

Instead of the scalar value \(V^\pi(s)\), learn the **return distribution** \(Z^\pi(s)\).

* Bellemare et al. proved a **Wasserstein contraction** of the distributional Bellman operator, guaranteeing convergence of categorical or quantile approximations ([arXiv][7]).
* A full monograph (MIT Press, 2023) collects theory tying distributional learning to risk‑sensitive control and representation learning ([distributional-rl.org][8]).

Significance: just as approximation theory broadened our view from function value to function class, distributional analysis broadens RL from expectation to full stochastic predictions, fundamentally changing stability and learning speed.

---


[7]: https://arxiv.org/abs/1707.06887?utm_source=chatgpt.com "A Distributional Perspective on Reinforcement Learning"
[8]: https://www.distributional-rl.org/?utm_source=chatgpt.com "Distributional Reinforcement Learning"
