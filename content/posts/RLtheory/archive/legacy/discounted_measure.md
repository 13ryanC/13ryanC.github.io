---
_build:
  render: never
  list: never

date: "2025-06-30"
title: "Discounted Occupancy Meaure affect initial state visitation"
summary: "Discounted Occupancy Meaure affect initial state visitation"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### Internal plan — subtasks & checkpoints

1. **Formal definition**
   Write the discounted (normalized) state‑occupancy measure ‎\(d_{\mu}^{\pi}\) and isolate the term coming from the first time‑step. ✔︎ **(do now)**
2. **Relative weight analysis**
   Show that the initial‑state contribution is exactly \(1-\gamma\). Examine the limits \( \gamma\!\to\!0\) and \( \gamma\!\to\!1\). *pending*
3. **Concrete example**
   Compute a two‑state MDP illustrating how the mass on \(t=0\) shrinks as \( \gamma\) grows. *pending*
4. **Implications for algorithms**
   Explain why policy‑gradient, imitation‑learning and off‑policy evaluation methods that use discounted occupancies effectively “forget” the start state when \( \gamma\) is near 1. *pending*
5. **Residual questions / tests**
   Note open issues (average‑reward setting, episodic tasks, horizon truncation). *pending*

---

## Step 1 – Definition and decomposition (verifiable)

For an infinite‑horizon discounted Markov Decision Process with discount factor \(0<\gamma<1\), an initial state distribution \(\mu\), and a policy \(\pi\), the **discounted state‑occupancy measure** is

$$
d_{\mu}^{\pi}(s)\;=\;(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}\; \Pr_{\mu}^{\pi}(S_{t}=s).
$$

* It is a probability distribution over states because \((1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}=1\).
* Splitting off the first term (\(t=0\)) gives

$$
d_{\mu}^{\pi}(s) \;=\; (1-\gamma)\,\mu(s) \;+\; (1-\gamma)\sum_{t=1}^{\infty}\gamma^{t}\Pr_{\mu}^{\pi}(S_{t}=s).
$$

Hence **the discounted share coming directly from the initial state is exactly \((1-\gamma)\mu(s)\)**. Everything else—weighted by an additional factor \(\gamma^{t}\)—comes from later visits. The formula and its use as a “weighted stationary distribution” appear in standard RL texts and lecture notes ([rltheory.github.io][1]).

---

### Progress

* Verified that the initial‑state term in \(d_{\mu}^{\pi}\) is \((1-\gamma)\mu(s)\); this immediately shows how the discount factor governs the importance of the start distribution.
* Open issues: quantify how that importance decays with \(\gamma\); build an example; discuss algorithmic implications.

[1]: https://rltheory.github.io/lecture-notes/planning-in-mdps/lec2/ "The Fundamental Theorem | RL Theory"


---


### Step 2 – Quantifying the decay of the initial‑state share as \(\gamma\!\uparrow\!1\)

---

#### 1.  Exact fraction of mass on \(t=0\)

From the definition

$$
d_{\mu}^{\pi}(s)=(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}\Pr_{\mu}^{\pi}(S_t=s)\; ,\qquad 0<\gamma<1, 
$$

the **weight placed on the first time‑step** is

$$
w_0 \;=\; (1-\gamma)\mu(s), 
$$

while the combined weight of all later visits is

$$
\sum_{t=1}^{\infty}w_t \;=\;\gamma.  
$$

Hence the **global fraction** of the discounted occupancy coming directly from the start distribution is

$$
\boxed{\;\textstyle\frac{\text{init.~mass}}{\text{total mass}} \;=\;1-\gamma\;}
$$

and the **ratio** of initial to later visits is

$$
\frac{w_0}{\sum_{t\ge1}w_t}\;=\;\frac{1-\gamma}{\gamma}.
$$

(The formula for \(d_{\mu}^{\pi}\) is standard .)

---

#### 2.  How fast does it shrink?

| \(\gamma\) | Init. share \(1-\gamma\) | Ratio \( \frac{1-\gamma}{\gamma}\) | Steps until 95 % of mass seen\(^\dagger\) |
| -------- | ---------------------- | -------------------------------- | --------------------------------------- |
| 0.50     | 0.50                   | 1.00                             |  4                                      |
| 0.80     | 0.20                   | 0.25                             |  13                                     |
| 0.90     | 0.10                   | 0.11                             |  28                                     |
| 0.95     | 0.05                   | 0.05                             |  58                                     |
| 0.99     | 0.01                   | 0.01                             |  298                                    |

\(^\dagger\)For an infinite‑horizon chain, the smallest \(k\) such that \(\sum_{t=0}^{k}\!w_t \ge 0.95\) is
\(k = \lceil\log(0.05)/\log\gamma\rceil-1\).

Observations:

* **Linear decay in \(1-\gamma\).** Every extra “9” in \( \gamma\) knocks the initial share down by an order of magnitude.
* **Geometric half‑life.** The per‑step weights satisfy \(w_{t+1}/w_t=\gamma\). The time to halve any weight is

  $$
  t_{1/2}=\frac{\ln 0.5}{\ln\gamma}.
  $$
* **Practical horizon.** With \(\gamma=0.99\), fewer than 1 % of visits come from the start state; 95 % of the discounted mass lies within the first \~300 steps.

---

#### 3.  Differential view

The derivative

$$
\frac{\mathrm{d}}{\mathrm{d}\gamma}(1-\gamma)=-1
$$

is constant, but the **relative** sensitivity diverges as \(\gamma\to1\):

$$
\frac{\mathrm{d}}{\mathrm{d}\gamma}\log(1-\gamma)= -\frac{1}{1-\gamma}\;\longrightarrow\;-\infty.
$$

So near 1, tiny changes in \( \gamma\) produce disproportionately large changes in how much the initial distribution matters.

---

### Progress

* Derived closed‑form expressions for the initial‑mass share and its ratio to future visits.
* Quantified decay with numeric examples, half‑life, and 95 % horizon.
* **Open next tasks:** craft a concrete two‑state MDP illustration; discuss consequences for gradient‑based, imitation, and off‑policy algorithms; examine episodic vs. average‑reward settings.

---


### Step 3 – Concrete two‑state MDP example

---

#### Minimal MDP

| element                | value                                    |
| ---------------------- | ---------------------------------------- |
| **States**             | \(S=\{A,B\}\)                              |
| **Start distribution** | \(\mu(A)=1,\;\mu(B)=0\)                    |
| **Transitions**        | \(P(A\!\to\!B)=1,\;P(B\!\to\!B)=1\)        |
| **Actions / rewards**  | Irrelevant here (any fixed policy works) |

*Intuition*: you begin in \(A\), move to \(B\) on the first step, and then stay there forever.

---

#### Discounted occupancy

Let \(d_{\mu}^{\pi}\) be the discounted state‑occupancy measure

$$
d_{\mu}^{\pi}(s)=(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}\Pr(S_t=s).
$$

Because \(A\) is visited only at \(t=0\):

$$
d(A)=(1-\gamma)\mu(A)=1-\gamma,
\qquad
d(B)=(1-\gamma)\sum_{t=1}^{\infty}\gamma^{t}= \gamma.
$$

Hence **every choice of \(\gamma\) splits the mass as**

$$
\boxed{d(A)=1-\gamma,\; d(B)=\gamma}.
$$

---

#### Numeric illustration

| \(\gamma\) | Init‑state mass \(d(A)\) | Later‑state mass \(d(B)\) |
| -------- | ---------------------- | ----------------------- |
| 0.50     | 0.50                   | 0.50                    |
| 0.80     | 0.20                   | 0.80                    |
| 0.90     | 0.10                   | 0.90                    |
| 0.95     | 0.05                   | 0.95                    |
| 0.99     | 0.01                   | 0.99                    |

*Observations*

* The initial state’s share falls **linearly with \(1-\gamma\)**—exactly the trend quantified in Step 2.
* When \(\gamma=0.99\), 99 % of the discounted visitation ignores the start state.
* Because \(A\) is never revisited, this example shows the **maximal possible decay**; in richer MDPs later returns can raise \(d(A)\), but the first‑step contribution is always exactly \(1-\gamma\).

---

### Progress

* Constructed and analyzed a two‑state MDP whose discounted occupancy cleanly splits into \((1-\gamma,\gamma)\).
* Demonstrated numerically how the initial‑state share shrinks as \(\gamma\!\to\!1\), concretely matching the general formulas from Step 2.
* **Open next tasks:** (i) discuss implications for learning algorithms that rely on \(d_{\mu}^{\pi}\); (ii) outline residual issues (finite horizons, average‑reward setting, horizon truncation).

---



### Step 4 – Implications of the \((1-\gamma)\) front‑loading on algorithms that **sample or optimize through the discounted occupancy measure** \(d_{\mu}^{\pi}\)

The following three classes of methods all integrate (or match) expectations w\.r.t.
\(d_{\mu}^{\pi}(s,a)=(1-\gamma)\!\sum_{t\ge0}\gamma^{t}\Pr_{\mu}^{\pi}(S_t=s,\,A_t=a)\).
Because the *first* term is \((1-\gamma)\mu(s)\pi(a|s)\), any component of their objective, gradient or loss that depends **only on the start distribution** is attenuated in direct proportion to \(1-\gamma\).

---

#### 4‑A.  **Policy‑gradient & actor–critic methods**

* **Gradient formula:** $\nabla_{\theta}J(\pi_{\theta})=\frac{1}{1-\gamma}\;
  \mathbb{E}_{(s,a)\sim d_{\mu}^{\pi_{\theta}}}\!\bigl[\nabla_{\theta}\log\pi_{\theta}(a|s)\,Q^{\pi}(s,a)\bigr] , $
  derived in modern lecture notes ([rltheory.github.io][1]).

  * The pre‑factor \(1/(1-\gamma)\) *multiplies* the expectation, but the integrand at time \(t=0\) still carries the small weight \(1-\gamma\).
  * **Effect:** when \(\gamma\to1\), the gradient signal from start states is \(O(1)\) *smaller* than the signal from the stationary part of the trajectory. Early decisions therefore adapt slowly; learning is “myopic” toward the long‑run distribution.
  * **Variance blow‑up:** The expected trajectory length under geometric termination is \(1/(1-\gamma)\). This cancels the front factor in expectation, but the *variance* of Monte‑Carlo gradient estimators grows as \(1/(1-\gamma)\), so large \(\gamma\) both down‑weights start states and inflates gradient noise.

**Mitigations.**

* Use a smaller \(\gamma\) for tasks where the initial configuration matters (robot resets, games with crucial openings).
* Keep \(\gamma\) high but add a *time‑dependent* baseline or *advantage shaping* that explicitly boosts early‑step signal.
* In episodic problems, let \(\gamma=1\) inside an episode and average returns over finite horizon \(H\); this restores equal weighting while preserving convergence theory.

---

#### 4‑B.  **Imitation‑learning by discounted occupancy matching (GAIL, AIRL, etc.)**

GAIL minimises an \(f\)-divergence between the expert occupancy \(\rho_{E}\) and the learner occupancy \(\rho_{\pi}\) with \(\rho(s,a)=\pi(a|s)\sum_{t}\gamma^{t}\Pr(S_t=s)\) .

* **Asymmetry:** mismatches at \(t=0\) are penalised only by \(1-\gamma\). A learner can reproduce the expert’s *long‑run* behaviour while ignoring subtle differences in the opening moves.
* **Observed failure modes:**

  * Agents that start in the wrong lane but quickly merge into expert‑like traffic flows.
  * Dexterous manipulation policies that fumble the initial grasp yet look expert once the object is secured.
* **Practical fixes:**

  1. **Horizon‑sweeping weights** — replace \(\gamma^{t}\) with a hand‑tuned schedule (e.g. \(\gamma\le0.95\) for the first 10 steps, then \(\gamma=0.99\)).
  2. **Un‑discounted occupancy matching** for the first \(k\) steps (equivalent to multiplying by \((1-\gamma)^{-1}\) for \(t<k\)).
  3. Combine GAIL with *behaviour cloning* pre‑training, which fits the *one‑step* distribution that is free of the \((1-\gamma)\) factor.

---

#### 4‑C.  **Off‑policy evaluation (Monte‑Carlo / IS and doubly‑robust variants)**

Per‑decision importance sampling estimates each discounted reward term
\((1-\gamma)\gamma^{t}\rho_{0:t-1}\,R_{t+1}\) ([pages.cs.wisc.edu][2]).

* **Bias toward later rewards:** the same \((1-\gamma)\) that suppresses start‑state visitation also suppresses the weight on *early* rewards in the return. Near \(\gamma=1\) most of the estimator’s mass (and variance) comes from rewards \(t\gg0\).
* **Sensitivity to start‑distribution mismatch diminishes:** if two policies differ only at the first few steps, their value‑difference is proportional to \(1-\gamma\). High‑\(\gamma\) OPE will therefore seem to agree even when the policies behave very differently at the outset.
* **Variance considerations:** because trajectory lengths scale as \(1/(1-\gamma)\), the product of IS weights can explode, but much of that variance sits in the *tail* of the trajectory—again leaving initial‑state information statistically impoverished.

**Diagnostics & remedies.**

* Run *discount‑aware IS*: truncate after \(k\approx\lceil\log(1-\alpha)/\log\gamma\rceil\) steps so that \(\alpha\) fraction of the discounted mass is captured (e.g.\ \(k\approx300\) for \(\gamma=0.99,\alpha=0.95\)).
* Evaluate with several \(\gamma\) values; a large swing in estimates as \(\gamma\) varies is a sign that early‑episode differences matter.

---

#### 4‑D.  **Cross‑cutting advice**

| Situation                                                         | Symptom under high \(\gamma\)                          | Simple counter‑measure                                                   |
| ----------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------ |
| Policy‑gradient stalls in early‑game tactics                      | Gradient norm small for \(t=0\) states                 | Lower \(\gamma\) or add curriculum that re‑starts from later states        |
| GAIL policy copies expert only after “settling in”                | Low discriminator loss, but poor first‑move accuracy | Pre‑train with BC; anneal \(\gamma\) upward during training                |
| OPE shows tiny value gap between two visibly different strategies | Estimates stable but wrong in practice               | Use finite‑horizon evaluation or clip IS weights before \(k\)-step horizon |

---

### Progress

* Mapped the \((1-\gamma)\) attenuation onto **three widely‑used algorithm families** and explained concrete failure modes.
* Provided quantitative or bibliographically‑supported mitigation tactics for each family.
* **Open issues for future steps:**

  1. Episodic *finite‑horizon* tasks, where discounting is an artefact—should one simply set \(\gamma=1\)?
  2. Average‑reward (\(\gamma=1\), \(\beta\)-mixing) formulations that bypass the problem but require different theory and baselines.

[1]: https://rltheory.github.io/lecture-notes/planning-in-mdps/lec16/ "Policy gradients | RL Theory"
[2]: https://pages.cs.wisc.edu/~jphanna/teaching/2022fall_cs839/documents/lec7-monte-carlo-II.pdf "lec7-monte-carlo-II"
