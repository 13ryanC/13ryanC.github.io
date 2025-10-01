---
_build:
  render: never
  list: never

date: "2025-06-26"
title: "Some Intuition from lecture 1 of Casba's RL theory series"
summary: "errata"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### 0  Bandits as the "bedrock" of RL

> RL is the big brother of bandits and bandits serve as the bedrock foundation for RL

A multi-armed bandit (MAB) abstracts away state to isolate the exploration-exploitation trade-off. Every RL proof of sample-complexity lower bounds ultimately reduces to a bandit instance.

Bandits teach us:

1. Information constraints (you cannot observe counterfactual rewards)

2. Concentration tools (Azuma-Hoeffding, self-normalised martingales, Empirical Bernstein) that re-appear in RL with only minor tweaks.

3. The importance of model-free regret analysis (i.e., UCB, Thompson Sampling) before one can appreciate model-based planning.

RL is the big brother of bandits as it inherits all bandit difficulties plus credit assignment through time, partial observability, and compounding model errors.

### 1  Background & recommended reading

| Source                                                                   | Why it matters in Lecture 1                                                                                                            |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Lattimore & Szepesvári, *Bandit Algorithms*** — Ch. 2, 3, 5, 7, 26, 38 | Measure‑theoretic setup, lower‑bound techniques, and non‑asymptotic concentration inequalities.                                        |
| **Second course in probability** — Ch. 1, 3, 4, 5                        | σ‑fields, conditional expectation wrt histories, dominated convergence—used to justify interchange of limits in value‑function proofs. |
| **Szepesvári, *Algorithms for RL*** — App. A                             | A compressed “toolkit” of kernels, filtrations, measurable selection. Useful when the lecture skips eps–δ details.                     |
| **RL Theory Seminar series**                                             | Provides ongoing examples where the lecture’s abstract definitions get stress‑tested on current research problems.                     |

These sources supply (i) measure‑theoretic foundations, (ii) concentration inequalities, and (iii) notation that the lecture will assume without re‑deriving.

---

### 2  “Three circles” landscape of RL

Csaba sketches RL research as the intersection of three methodological areas:

| Circle                 | Core question                                                                                                                                 | Typical assumptions                                                                              | Example tasks                                                                            |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **Planning**           | Given a *known* model of the environment, how do we compute a near‑optimal policy efficiently?                                                | Full access to transition kernel \(P\) and reward function \(r\); focus on computational complexity. | Value‑iteration, policy‑iteration, linear programming; real‑time game‑tree search.       |
| **Batch (offline) RL** | With a fixed data set of transitions \((s,a,r,s')\) gathered *before* deployment, can we learn a policy that will perform well *when executed*? | No further interaction allowed; dataset may be off‑policy and biased.                            | Fitted Q‑evaluation, doubly‑robust methods, conservative policy iteration in healthcare. |
| **Online RL**          | While interacting with the environment, how should the agent trade off exploration vs. exploitation to maximise cumulative reward?            | Feedback is sequential and stochastic; regret or sample‑complexity is analysed.                  | UCB‑style algorithms, posterior sampling, deep RL with ε‑greedy exploration.             |


| Circle             | Dominant variable        | **Nuanced insight from Csaba**                                                                                                                     |
| ------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Planning           | **Computation time**     | “Even if the model is exact, naïve value‑iteration explodes in large state spaces.  Structure (e.g. factored MDPs, linear MDPs) is the only hope.” |
| Batch (offline) RL | **Risk of acting**       | “In medicine a single bad on‑policy trial can kill, so interaction is forbidden.  Offline RL must *certify* safety from a biased dataset.”         |
| Online RL          | **Data budget / regret** | “Exploration is *not* just dithering.  It is the *price* of learning a transferable model.”                                                        |

The three circles overlap on the formal *Markov Decision Process* abstraction:

> **MDP = (state space \(S\), action space \(A\), transition kernel \(P\), reward function \(r\), horizon/discount \(H\)/\(\gamma\)).**

Thus, ideas about *models*, *policies*, and *returns* are shared, even though the data‑access model (full, batch, or interactive) differs.

> Intersection = MDPs. Yet the analysis lens changes:
> planning → complexity theory,
> batch → statistical generalisation under confounding,
> online → adversarial or stochastic regret.

---

### 3  Formal reinforcement‑learning model (MDP)

| Symbol                              | Meaning                                                                     | Typical assumption in the lecture                                    |
| ----------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| \(S\)                                 | **State space**                                                             | Finite (to avoid topological/measurability pitfalls on a first pass) |
| \(A\)                                 | **Action space**                                                            | Finite                                                               |
| \(P(\,\cdot \mid s,a)\)               | **Transition kernel** – probability distribution over next state \(s' \in S\) | Stationary and Markovian                                             |
| \(r(s,a)\)                            | **Immediate reward**                                                        | Bounded, w\.l.o.g. \(r \in [0,1]\)                                     |
| \(\gamma\in[0,1)\) or \(H\in\mathbb N\) | **Discount factor** (infinite horizon) or **finite horizon** length         | The lecture mostly uses \(\gamma\) for algebraic convenience           |

> **MDP tuple:**
>
> $$
> \mathcal M = \langle S,\;A,\;P,\;r,\;\gamma\text{ or }H\rangle.
> $$

#### 3.1 Histories and policies

* **History at time \(t\):**

  $$
  H_t = (s_0,a_0,\dots,s_{t-1},a_{t-1},s_t)\in\mathcal H_t := (S\times A)^{t}\times S .
  $$
* **Policy:** a sequence of stochastic kernels

  $$
  \pi = (\pi_t)_{t\ge 0},\qquad  
  \pi_t : \mathcal H_t \;\longrightarrow\; \mathcal P(A),
  $$

  where \(\mathcal P(A)\) denotes the set of probability measures on \(A\).
  *If \(S,A\) are finite, \(\pi_t(H_t)\) is just a probability vector over \(A\).*
  Deterministic policies are the special case where \(\pi_t(H_t)\) puts all mass on one action.

#### 3.2 Trajectory distribution and return

A **trajectory** generated by \(\pi\) in \(\mathcal M\) is

$$
\tau = (s_0,a_0,r_0,s_1,a_1,r_1,\dots),
$$

with \(a_t\sim\pi_t(H_t)\), \(s_{t+1}\sim P(\cdot\mid s_t,a_t)\), and \(r_t = r(s_t,a_t)\).

| Return type              | Formula                                                                                                      | Comments                                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| **Discounted**           | \(G = \sum_{t=0}^{\infty} \gamma^{t} r_t\)                                                                     | Gives exponentially vanishing weight to future rewards; effective horizon \(\approx \tfrac{1}{1-\gamma}\). |
| **Finite‑horizon**       | \(G = \sum_{t=0}^{H-1} r_t\)                                                                                   | Equivalent to \(\gamma=1\) followed by truncation.                                                         |
| **Truncated discounted** | Stop after \(T=\lceil \tfrac{\ln(1/\varepsilon)}{1-\gamma}\rceil\) terms to incur at most \(\varepsilon\) error. |                                                                                                          |

**Value functions** under policy \(\pi\):

$$
V^\pi(s) = \mathbb E_\pi \bigl[G \mid s_0=s\bigr],\qquad  
Q^\pi(s,a)=\mathbb E_\pi \bigl[G \mid s_0=s,a_0=a\bigr].
$$

The optimal value and policy are \(V^{\ast} (s)= \sup_\pi V^{\pi}(s)\) and
\(\displaystyle \pi^{\ast} \in \arg\max_\pi V^{\pi}\) (existence is guaranteed in the finite case).

---

### 4  Key modelling choices & open questions

| Design choice                | Why it appears in the lecture                                                                | What happens if we change it?                                                                         |
| ---------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **State fully observed**     | Simplifies control and learning proofs; converts the problem to an MDP.                      | Partial observability ⇒ POMDPs. Optimal control is PSPACE‑hard; sample complexity explodes.           |
| **Finite \(S,A\)**             | Avoids measurable‑selection subtleties (choice of σ‑algebra, existence of Borel selectors).  | Continuous spaces need extra regularity (compactness, continuity of \(P,r\)) or function approximation. |
| **Stationary transitions**   | Makes Bellman equations well‑defined and allows dynamic‑programming arguments.               | Non‑stationary environments require regret or adaptation bounds.                                      |
| **Discounting (\(\gamma<1\))** | Ensures \(G<\infty\) and allows contraction‑mapping proofs. Acts as an *implicit regulariser*. | Average‑reward and undiscounted infinite‑horizon settings demand different bias‑span analyses.        |
| **Bounded rewards**          | Guarantees concentration inequalities with sub‑Gaussian tails.                               | Heavy‑tailed rewards necessitate robust variants.                                                     |

### Open research‑style questions highlighted by Csaba

* *Why this particular formulation?* Could alternative objectives (e.g. risk‑sensitive criteria, quantiles) be more appropriate in safety‑critical domains?
* *What models should we learn?* Minimal sufficient statistics vs. rich world‑models that transfer.
* *Can we act without access to true states?* Representation learning, belief‑state RL, state‑abstraction theory.
* *Measure‑theoretic edge cases:* Do optimal measurable policies always exist in general Borel spaces? Under what topological conditions?
* *Exploration vs. exploitation trade‑offs* differ sharply between the planning, batch, and online regimes of the Venn diagram.

---

## 5  Compact cheat‑sheet of core formulas

* **Bellman operator (discounted):**

  $$
  (\mathcal T V)(s)=\max_{a\in A}\Bigl[r(s,a)+\gamma\sum_{s'} P(s'\!\mid s,a)\,V(s')\Bigr].
  $$

  Contraction modulus: \(\gamma\). Fixed point \(V^*\) satisfies \(\mathcal T V^*=V^*\).

* **Regret (online RL):**

  $$
  \text{Regret}(T)=\sum_{t=0}^{T-1}\bigl(r(s_t,a^*_t)-r(s_t,a_t)\bigr),\qquad  
  a^*_t\in\arg\max_{a}Q^*(s_t,a).
  $$

* **Conservative policy improvement (batch RL):**
  Guarantee:

  $$
  V^{\pi_{\text{new}}}(s_0)\;\ge\; V^{\pi_{\text{beh}}}(s_0)\;-\;O\!\bigl(\widehat{\text{IPW‑error}}\bigr).
  $$

(These are not derived in Lecture 1 but set the stage for later sessions.)

---

## 5  Formal MDP: enriched commentary

1. **States \(S\).**  The lecture *assumes* full observability “to free up mental space.”
   *Open question:* *When can a learned representation \(\phi(s)\) replace \(s\) without sacrificing optimality?*
2. **Actions \(A\).**  Finite so that *measurable‑selection* theorems are not needed.  In continuous \(A\), existence of optimal deterministic policies may fail without continuity of \(r,P\).
3. **Transition kernel \(P\).**  Stationarity means “physics does not drift.”  Non‑stationary kernels turn the value operator from a contraction into a *moving* operator—fixed‑point theory no longer applies.
4. **Reward \(r\in[0,1]\).**  Boundedness ⇒ sub‑Gaussian tails.  If rewards are heavy‑tailed, concentration requires Catoni‑style robust means.
5. **Discount \(\gamma<1\).**

   *Implicit regularisation.*  The Lipschitz constant of the Bellman operator is \(\gamma\); making \(\gamma\) smaller shrinks the hypothesis class of value functions, improving generalisation in finite‑data regimes.

   *Effective horizon.*  To approximate an infinite sum within \(\varepsilon\):

   $$
   T(\varepsilon,\gamma)=\Bigl\lceil\tfrac{\ln(1/\varepsilon)}{1-\gamma}\Bigr\rceil.
   $$

---

## 6  Histories, policies, and *why randomisation matters*

* **History \(H_t\).**  Contains *exactly* what the agent has seen.  If the policy instead used only \(s_t\), it assumes the Markov property is correct.  When the modelling choice is wrong (POMDP), the dependence on *full history* is necessary to recover optimality.

* **Stochastic policies.**
  *Why randomise?*

  1. *Tie‑breaking* when \(Q^\pi(s,a)\) is flat.
  2. *Mixed strategies* are sometimes uniquely optimal (e.g. zero‑sum games, exploration incentives).
  3. *Algorithmic convenience*—gradient methods treat actions as soft samples, which makes the loss differentiable.

---

## 7  Distribution of returns → the “expectation” debate

Your raw notes asked:

> *“What does it mean to maximise the return when the return itself is a random variable?”*

* **Classical answer:** optimise the *expected* discounted sum \(V^\pi(s)\).
* **Critique:** expectation ignores risk.  Safety‑critical RL studies CVaR, variance‑penalised, or quantile criteria.
* **Lecture hint:** future sessions may show how expectation‑optimality can mask heavy‑tail failures (e.g. a high‑variance policy that *usually* wins but occasionally crashes).

---

## 8  Measure‑theoretic footnotes (why Csaba waves his hands—for now)

1. **Borel vs. universal measurability.**  An optimal policy measurable w\.r.t. the Borel σ‑algebra may *not* exist in general Polish spaces.  One needs analytic sets or Blackwell’s 1956 result.
2. **Axiom of choice pitfalls.**  Non‑measurable sets can break the existence of probability kernels.  Textbooks often slip in “assume all troublesome sets are jointly measurable”—practitioners silently accept finite \(S,A\).
3. **Weakening to “Terry’s Analysis I & II.”**  If one restricts to separable metric spaces and continuous kernels, measurable selection holds; the lecture promises to “extend power and expressivity” later.

---

## 9  Motivating questions Csaba emphasised for *future deep dives*

| Question                                             | Why it matters                                     | Potential deep‑dive technique                       |
| ---------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------- |
| *Why is learning essential for AI?*                  | Hard‑coded policies brittle to distribution shift. | PAC‑Bayesian transfer, representation learning.     |
| *Which models should we learn to be data‑efficient?* | Full dynamics vs. partial successor features.      | Structural MDPs, linear‑MDPs, bisimulation metrics. |
| *Can we excel without observing the true state?*     | Real‑world sensors are partial.                    | Predictive‑state representations, belief‑state RL.  |
| *How much history is “enough”?*                      | Balances memory/computation vs. optimality.        | Information bottleneck, causal state aggregation.   |

---

## 10  Cheat‑sheet (same formulas, with usage notes)

| Formula                                                        | When you will *actually* use it                                  |
| -------------------------------------------------------------- | ---------------------------------------------------------------- |
| \(V^\pi(s)=\mathbb E_\pi\bigl[\sum_{t\ge0}\gamma^tr_t\bigr]\)    | Baseline for policy‑gradient objectives.                         |
| \(\mathcal T V=\max_a\{r+\gamma P V\}\)                          | Contraction proof of value‑iteration convergence.                |
| \(T(\varepsilon,\gamma)\approx \frac{1}{\varepsilon(1-\gamma)}\) | How long Monte‑Carlo rollouts must be to estimate \(V^\pi\) to ±ε. |
| \(\text{Regret}(T)=\sum_{t=0}^{T-1}\bigl(r^*-r_t\bigr)\)         | Performance metric in online RL proofs.                          |

---

