---
date: "2025-06-27"
title: "High and Low Road of RL"
summary: "Provide accessible landscape for RL beginners and practitioners alike"
category: "Tutorial"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

Below is a parallel “two‑road” map for **reinforcement learning (RL)** that mirrors the low‑road / high‑road distinction already used in Active Inference.  The same mathematics (Bellman optimality and its stochastic‑approximation algorithms) can be reached from two very different starting points.

---

## 1   Preliminaries — the common destination

| Construct                          | Formal sketch                                             | Intuition                                          |                                                     |                                                      |
| ---------------------------------- | --------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------- |
| **Markov decision process (MDP)**  | $\langle\!\mathcal S,\mathcal A,P,r,\gamma\rangle$; (P(s' | s,a)) and reward $r(s,a)$.                         | Minimal description of a sequential choice problem. |                                                      |
| **Return**                         | $G_t=\sum_{k=0}^{\infty}\gamma^{k} r_{t+k+1}$             | Discounted future utility.                         |                                                     |                                                      |
| **Value‑function / Q‑function**    | (V^\pi(s)=\mathbf E\_\pi\[G\_t                            | s\_t=s]), (Q^\pi(s,a)=\mathbf E\_\pi\[G\_t         | s\_t=s,a\_t=a])                                     | Long‑run usefulness of a state or state‑action pair. |
| **Bellman optimality**             | (V^\* (s)=\max\_{a}!\bigl\[r(s,a)+\gamma!\sum\_{s'}P(s'   | s,a)V^\*(s')\bigr])                                | A self‑consistency equation for optimal behaviour.  |                                                      |
| **Temporal‑difference (TD) error** | $\delta_t=r_{t+1}+\gamma V(s_{t+1})-V(s_t)$               | Instantaneous surprise; the basic learning signal. |                                                     |                                                      |

---

## 2   The **Low Road** — *Algorithmic / process theory*

1. **Start with associative learning**
   Early psychology (Rescorla‑Wagner) already used a delta‑rule very close to TD learning for Pavlovian conditioning.  Sutton & Barto extend this to sequential tasks by bootstrapping on later predictions. ([web.stanford.edu][1])

2. **Define mechanistic update rules**
   With a fixed learning rate $\alpha$, a tabular critic updates

   $$
   V_{t+1}(s_t)\;\leftarrow\;V_t(s_t)+\alpha\,\delta_t,
   $$

   while an actor updates its policy in the direction that would have made the just‑received reward more likely (actor–critic).  These are local, online and neurally plausible computations.

3. **Extend to action‑selection (control)**
   Q‑learning, SARSA, policy‑gradient and modern deep RL (DQN, PPO, SAC, …) are refinements of the same TD principle, differing only in how they represent the value function and stabilise updates.

4. **Neuroscientific mapping**
   Phasic firing of mid‑brain dopamine neurons quantitatively matches the TD error, providing biological evidence for the low‑road mechanism. ([pmc.ncbi.nlm.nih.gov][2])

5. **Outcome**
   *Reinforcement learning becomes a toolbox*: give me a reward signal and I can construct an algorithm (or hypothesise a circuit) that will learn to maximise it, even in high‑dimensional spaces.

> **Virtue:** Concreteness and implementability (works from fruit‑flies to AlphaStar).
> **Limitation:** Takes the reward function as *given*; offers little explanation of why maximising cumulative reward is a sensible goal in the first place.

---

## 3   The **High Road** — *Normative / decision‑theoretic*

1. **Axioms of rational preference → expected utility**
   The von Neumann–Morgenstern theorem shows that any agent whose preferences obey four simple axioms must behave **as if** maximising the expectation of a scalar utility function. ([en.wikipedia.org][3])

2. **Utility in time → sequential decision theory**
   Add (i) stationarity, (ii) conditional independence given the current state, and (iii) time‑consistent discounting, and the utility maximisation problem *reduces* to an MDP whose solution is **Bellman optimal control**. ([icml.cc][4])

3. **Unknown dynamics → learning ≡ reinforcement learning**
   If the transition matrix $P$ or reward function $r$ is unknown, the only way to approximate Bellman‑optimal action is to *interact* with the environment and learn value functions or policies from data.  That interactive estimation procedure *is* RL.

4. **Links to optimal control and information theory**
   In continuous time the Bellman recursion becomes the Hamilton‑Jacobi‑Bellman (HJB) partial differential equation—the fundamental equation of stochastic optimal control. ([proceedings.mlr.press][5])
   When the agent is **information‑limited**, a Lagrange multiplier on policy entropy turns the objective into *maximum‑entropy* (a.k.a. “soft”) RL and yields KL‑control and path‑integral solutions. ([bair.berkeley.edu][6], [ber666.github.io][7])

5. **Outcome**
   *Reinforcement learning is the rational strategy* for any bounded agent that must repeatedly choose under uncertainty and latent dynamics—no neural delta‑rule assumption required.

> **Virtue:** Explains *why* cumulative reward is the right quantity to optimise.
> **Limitation:** Abstract; by itself it does not tell you *how* to compute the policy, nor whether biological brains possess the needed function approximators.

---

## 4   Synoptic comparison

|                          | **Low Road (process)**                                 | **High Road (normative)**                                    |
| ------------------------ | ------------------------------------------------------ | ------------------------------------------------------------ |
| **Starting premise**     | The brain (or algorithm) updates values via TD errors. | Any rational agent must maximise expected utility over time. |
| **Primary question**     | *How* can an unknown MDP be solved incrementally?      | *Why* is return maximisation the correct objective?          |
| **Core constructs**      | TD error, Q‑learning, actor–critic, dopamine.          | VNM utility, Bellman optimality, HJB, soft‑RL.               |
| **Level of explanation** | Algorithmic / implementational (Marr level 2).         | Computational / rational (Marr level 1).                     |
| **Typical applications** | Engineering agents, modelling dopaminergic learning.   | Economics, game‑theory, control, bounded‑rational analysis.  |
| **Risk of circularity**  | Reward taken as axiomatic.                             | Relies on strict utility axioms & discounting assumptions.   |

---

## 5   Bridging the roads

* **Control‑as‑inference:** By exponentiating negative reward into a Boltzmann factor, one can *derive* soft‑RL algorithms from probabilistic inference—providing an algebraic bridge between the two roads and to Active Inference.
* **Evolutionary design:** Natural selection can be viewed as a higher‑level optimiser of reward structures; the low road then instantiates day‑to‑day learning, while the high road captures the long‑run logic of survival and competition.

---

## 6   Typical misunderstandings & empirical tests

| Misunderstanding                         | Diagnostic check                                                 | Falsifiable test                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| “RL must assume a dopamine‑like signal.” | Does the algorithm require a biologically local TD error?        | Compare success of Monte‑Carlo policy‑gradient (no critic) in silico.                 |
| “Utility theory is optional.”            | Does replacing the VNM axioms change which policies are optimal? | Alter the independence axiom; show that certainty equivalence fails.                  |
| “Soft‑RL is an ad‑hoc trick.”            | Is the objective the solution to a constrained optimisation?     | Vary the entropy‑temperature parameter β and measure exploration‑exploitation curves. |

---

### Further reading

* **Sutton & Barto — *Reinforcement Learning: An Introduction*, 2nd ed. (MIT Press, 2018)**: canonical low‑road algorithms. ([web.stanford.edu][1])
* **Todorov (2009), Kappen (2011), “Soft Q‑Learning” (Haarnoja et al., 2017)**: control‑as‑inference / high‑road extensions. ([bair.berkeley.edu][6], [ber666.github.io][7])
* **von Neumann & Morgenstern — *Theory of Games and Economic Behaviour* (1947)**: foundational utility axioms. ([en.wikipedia.org][3])

---

**Take‑home:**

> The **low road** to RL says “give me a numeric reward and I’ll show you a learning rule.”
> The **high road** says “here is why any rational, uncertainty‑facing agent *must* behave *as if* maximising that reward.”
> Combining both gives you agents that are *both* theoretically justified and practically realisable.

[1]: https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf?utm_source=chatgpt.com "[PDF] Reinforcement Learning: An Introduction - Stanford University"
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8107188/?utm_source=chatgpt.com "Dopamine signals as temporal difference errors: Recent advances"
[3]: https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Morgenstern_utility_theorem?utm_source=chatgpt.com "Von Neumann–Morgenstern utility theorem - Wikipedia"
[4]: https://icml.cc/media/icml-2022/Slides/16848.pdf?utm_source=chatgpt.com "[PDF] Utility Theory for Sequential Decision Making"
[5]: https://proceedings.mlr.press/v120/kim20b/kim20b.pdf?utm_source=chatgpt.com "[PDF] Hamilton-Jacobi-Bellman Equations for Q-Learning in Continuous ..."
[6]: https://bair.berkeley.edu/blog/2017/10/06/soft-q-learning/?utm_source=chatgpt.com "Learning Diverse Skills via Maximum Entropy Deep Reinforcement ..."
[7]: https://ber666.github.io/blog/2024/soft-RL-01/?utm_source=chatgpt.com "Maximum Entropy RL and Soft Q-Learning | Shibo Hao"


### Two Roads to the Same RL Summit

Reinforcement learning can be reached from **two complementary starting points**—an *algorithmic* (“low‑road”) and a *normative* (“high‑road”) perspective—yet both converge on the **Bellman optimality equations** that define rational, reward‑maximising behaviour in an MDP.

---

#### 1  Common peak (what both roads reach)

* **MDP:**  $\langle\mathcal S,\mathcal A,P,r,\gamma\rangle$
* **Return:**  $G_t=\sum_{k\ge0}\gamma^{k}r_{t+k+1}$
* **Optimality:**  $V^\*(s)=\max_a\bigl[r(s,a)+\gamma\sum_{s'}P(s'|s,a)V^\*(s')\bigr]$
* **Learning signal:**  TD‑error $\delta_t=r_{t+1}+\gamma V(s_{t+1})-V(s_t)$

---

#### 2  Low Road — *Process & implementation*

1. **Associative beginnings.**  Rescorla–Wagner’s delta‑rule → Sutton & Barto’s TD‑learning.
2. **Local updates.**  $V(s)\!\leftarrow\!V(s)+\alpha\,\delta$; actor‑critic nudges policy toward actions that would have raised reward.
3. **Scaling up.**  Q‑learning, SARSA, policy‑gradient; deep nets (DQN, PPO, SAC) supply function approximators and stabilisers.
4. **Biological anchor.**  Mid‑brain dopamine firing ≈ TD‑error, tying the math to neural circuitry.

*Virtue:* immediately runnable on robots or neurons.
*Limitation:* treats the reward signal itself as an unexplained given.

---

#### 3  High Road — *Theory & justification*

1. **Utility axioms.**  Von Neumann–Morgenstern ➜ “max expected scalar utility.”
2. **From utility to control.**  Time consistency + Markov property collapse sequential choice to an MDP solved by Bellman recursions.
3. **Unknown world?**  Interaction-driven estimation (i.e., RL) is *necessary* when $P$ or $r$ are hidden.
4. **Continuous & bounded variants.**  HJB equations for continuous time; entropy‑regularised (soft) RL emerges when information costs are penalised.

*Virtue:* explains *why* maximising discounted reward is rational and quantifies sample complexity & regret.
*Limitation:* abstract; provides guarantees but not practical trickery.

---

#### 4  Bridges and Interplay

* **Control‑as‑Inference:**  Exponentiating $-r$ into a Boltzmann factor reframes soft‑RL as Bayesian inference, algebraically uniting both roads.
* **Evolutionary layering:**  Natural selection may sculpt reward functions (high‑road logic) while individual brains run TD‑like low‑road updates day‑to‑day.
* **Research workflow:**  Theory bounds set the **target**, empirical design (à la *Experimentology*) tests which algorithms hit it in noisy, high‑dimensional worlds.

---

### Take‑away

*Low road:* “Here is a delta‑rule that *learns* from reward.”
*High road:* “Here is why any agent that endures *must* behave *as if* maximising that reward.”
Mastering both yields RL systems that are **provably sensible** *and* **operationally effective**—from fruit‑fly brains to flagship AIs.


Here is a fuller, more precise version that spells out what each “road” entails and why the two complement one another.

---

**I plan to explore reinforcement learning (RL) along two converging paths, echoing the “low‑road / high‑road” distinction used in active‑inference research.**

### ①  The *low road* — empirical craft and experimentation

*Purpose* Start with working code and data, iterate quickly, and build intuition by observing what actually learns.
*Core activities*

* **Design credible experiments.**  Pre‑register hypotheses, control for confounders, and report negative results—principles championed in Michael Frank’s *Experimentology* (#ref‑frank).
* **Implement and benchmark algorithms.**  Temporal‑difference learning, Q‑learning, policy‑gradient, deep actor–critic variants, hyper‑parameter sweeps, ablation studies.
* **Ensure reproducibility.**  Shared code, deterministic seeds, statistical power analyses, robust evaluation protocols (as systematised in *Empirical Design in RL*, Patterson et al. 2023).

The low road treats RL as an engineering discipline first: collect evidence, iterate, and let phenomena drive refinements.

### ②  The *high road* — normative theory and guarantees

*Purpose* Begin with first principles—optimality in Markov Decision Processes (MDPs) and regret or sample‑complexity bounds—and derive what an ideal learner should do.
*Core activities*

* **Formal problem statements.**  Define returns $J(\pi)=\mathbb E[\sum_t\gamma^t r_t]$, Bellman equations, value and policy optimality conditions.
* **Theoretical algorithms.**  Value‑iteration, policy‑iteration, linear‑quadratic regulators, upper‑confidence and Thompson‑sampling bandits—developed and analysed in Szepesvári’s *Algorithms for Reinforcement Learning* (#ref‑szepesvari) and Lattimore & Szepesvári’s *Bandit Algorithms*.
* **Provable properties.**  Convergence rates, PAC and minimax regret bounds, stability under function approximation—topics covered in the RL Theory seminar series (#ref‑rltheory).

The high road provides the mathematical yardsticks against which low‑road prototypes can be judged: “How fast *should* this learn?” “Is the policy near‑optimal with high probability?”

### ③  Why follow both roads?

* **Synergy.**  Theory suggests what is possible and what is futile; experiment tells us which theoretically sound ideas survive contact with high‑dimensional reality.
* **Robust progress.**  Aligning empirical protocols with theoretical insights minimises the risk of over‑claiming, under‑powering, or silently depending on lucky hyper‑parameters.

---

> **Revised passage**

> *I will approach reinforcement learning through two complementary strands.
> **Low road (empirical design).**  Guided by Michael Frank’s “experimentology,” I will practise rigorous, model‑driven experimental design: reproducible pipelines, careful hyper‑parameter searches, and transparent statistical analysis. This strand emphasises building and testing concrete algorithms—TD‑learning, deep actor–critic, etc.—and learning from the data they generate.
> **High road (theoretical foundations).**  In parallel, I will study the normative backbone of RL, using Csaba Szepesvári’s textbook, the Lattimore–Szepesvári bandit monograph, and the RL Theory seminars. These resources develop optimal‑control principles, Bellman equations, regret bounds, and sample‑complexity results that explain *why* and *how fast* well‑designed algorithms can succeed.
> By alternating between low‑road experimentation and high‑road theory, I aim to build algorithms that are both empirically trustworthy and provably sound.*


**Short answer — Mostly yes, but add two caveats**

| Road          | Your proposed exemplars                                                                | What they capture                                                                                                                                                                                                                               | Two caveats                                                                                                                                                                                                                                                                   |
| ------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Low road**  | Michael Frank’s *Experimentology* and Patterson et al. (2023) *Empirical Design in RL* | Hands-on craft of running RL studies: reliable protocols, hyper-parameter hygiene, statistical tests, replication, open science. ([experimentology.io][1], [arxiv.org][2])                                                                      | (i) “Low-road” in the active-inference sense is broader than *just* experimentation—it also includes the *algorithmic* toolbox (TD-learning, policy gradient, etc.). <br> (ii) Good experimentation is needed on the high road too (e.g. to test theory-inspired algorithms). |
| **High road** | Lattimore & Szepesvári’s *Bandit Algorithms* and the *RL Theory* notes                 | Normative, sample-complexity and regret analyses; Bellman equations, PAC and minimax rates, concentration inequalities—i.e. *why* and *how fast* RL should work. ([tor-lattimore.com][3], [rltheory.github.io][4], [rltheorybook.github.io][5]) | (i) Bandits are a special (stateless) case; full high-road RL covers MDPs, function approximation and control. <br> (ii) Theory alone does not prescribe *which* empirical design is best for testing new ideas—low-road craft still matters.                                 |

---

### How the mapping lines up with the original “two-roads” metaphor

1. **Starting assumptions**

   * Low-road RL begins with *working code and data*; questions are pragmatic (“Does this variant learn faster on Atari?”). That resonates with Experimentology’s emphasis on reproducible pipelines.
   * High-road RL begins with *axioms*—optimality in MDPs, regret minimisation in bandits—then derives limits and algorithms. That is exactly what the Szepesvári/Lattimore texts do.

2. **Convergence point**
   Both roads ought to meet at algorithms that are *empirically robust* **and** *theoretically grounded*—e.g. an actor-critic method whose step-size schedule is justified by convergence proofs *and* is benchmarked with the statistical discipline recommended by Experimentology.

3. **Why the distinction is useful**
   *Low-road* resources teach how to avoid false positives, tune baselines, and share artefacts.
   *High-road* resources tell you when a new idea can be expected to scale, what sample size is needed, and which performance curves are impossibly good.

---

### Two refinements to tighten your characterisation

1. **Include algorithmic practice in the low road.**
   Papers such as Sutton & Barto (1998) or Mnih et al. (2015) are as “low-road” as empirical-design guides because they define the concrete update rules experimentologists will benchmark. Treat Experimentology + algorithmic cookbooks as a single empirical-engineering strand.

2. **Stretch the high road beyond bandits.**
   Keep Lattimore–Szepesvári for foundational intuition, but pair it with texts that cover *function-approximation* and *partial observability* (e.g. Agarwal et al., 2024 survey on RL theory with deep networks). This matches the way the high road in active inference scales from physics to brains.

---

### Bottom line

Your pairing is **directionally correct**: Those references epitomise the practical (low-road) and theoretical (high-road) sensibilities in modern RL. Just remember:

* Low-road ≠ “experiments only” – it is *experiment-centred engineering* writ large.
* High-road ≠ “bandits only” – it is *normative theory for the whole RL spectrum*.

Framing your reading list this way will give newcomers a clear mental map while avoiding the trap of thinking that practice and theory live in separate silos.

[1]: https://experimentology.io/?utm_source=chatgpt.com "Experimentology"
[2]: https://arxiv.org/abs/2304.01315?utm_source=chatgpt.com "Empirical Design in Reinforcement Learning"
[3]: https://tor-lattimore.com/downloads/book/book.pdf?utm_source=chatgpt.com "[PDF] Bandit Algorithms - tor-lattimore.com"
[4]: https://rltheory.github.io/?utm_source=chatgpt.com "RL Theory: Home"
[5]: https://rltheorybook.github.io/?utm_source=chatgpt.com "Reinforcement Learning: Theory and Algorithms"


Below is one way to map **“low-road” vs “high-road”** perspectives onto reinforcement learning (RL).
The labels are borrowed from active-inference terminology; in mainstream RL literature the split is not named this way, but two complementary derivations do exist.

---

## 1 Framing the question

| Active-inference pattern                                                                          | Desired RL analogue                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Low road**: start with an *algorithmic* recipe (predictive coding) and work upward.             | Begin with concrete, trial-and-error learning algorithms (TD, Q-learning, policy-gradient) and then explain what problem they end up solving.                                                                                       |
| **High road**: start with a *normative* physical principle (self-organisation) and work downward. | Start with normative decision theory—*maximise expected cumulative reward in a Markov Decision Process (MDP)*—derive optimal-control equations, then show that RL algorithms approximate those equations when the model is unknown. |

---

## 2 The **low road** to RL — “learning first, theory later”

### 2.1 Start-point

*Animals (or robots) improve behaviour by trial and error.* Treat learning as on-line adjustment of “cached” value estimates without assuming a full model of the world. Sutton & Barto’s temporal-difference (TD) updating is the canonical example. ([web.stanford.edu][1], [gibberblot.github.io][2])

### 2.2 Essential moves

1. **Prediction-error rule**

   $$
   \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t),\qquad
   V(s_t) \leftarrow V(s_t) + \alpha\,\delta_t .
   $$

   Learns a value function from sampled transitions.

2. **Extend to action values** (Q-learning, SARSA) so that a greedy or stochastic policy can be extracted.

3. **Policy-gradient & actor–critic**
   Replace value lookup tables by differentiable function approximators and update policy parameters directly with ∇θ J(θ).

4. **Deep RL**
   Stack neural nets on top of these core update rules; still no explicit environment model is required.

### 2.3 Pay-off

*Engineering recipe.* Yields algorithms that are easy to implement in unknown or very large state spaces; matches dopamine-like error signals observed in biology. Optimal-control theory is not required to start programming.

---

## 3 The **high road** to RL — “decision theory first”

### 3.1 Start-point

*A perfectly rational agent in an MDP maximises expected discounted return*

$$
J(\pi)=\mathbb E_{p_\pi}\Bigl[\sum_{t=0}^\infty\gamma^{t} r_t\Bigr].
$$

Here the environment is defined by $(\mathcal S,\mathcal A,P,R,\gamma)$. ([neptune.ai][3])

### 3.2 Essential moves

1. **Bellman optimality principle**

   $$
   V^\*(s)=\max_{a}\,R(s,a)+\gamma\sum_{s'}P(s'|s,a)V^\*(s') .
   $$

   This gives the unique fixed-point solved by dynamic-programming methods. ([deeplearningwizard.com][4], [datacamp.com][5])

2. **Dynamic programming algorithms**
   *Value-iteration* and *policy-iteration* compute $V^\*$ and an optimal policy when $P$ and $R$ are known.

3. **Planning as trajectory optimisation**
   Continuous-time and continuous-state analogues lead to the Hamilton–Jacobi–Bellman equation and links with classical control.

4. **When the model is unknown**
   Show that the stochastic-approximation updates from the low road (TD, Q-learning, policy-gradient) perform *sample-based stochastic dynamic programming*, converging (under conditions) to the same Bellman fixed point.

### 3.3 Pay-off

*Normative clarity.* Connects RL to economics, game theory, and optimal-control guarantees; supplies proofs of optimality and convergence; guides the design of safe or risk-sensitive variants (e.g. entropy-regularised RL, SAC). ([arxiv.org][6])

---

## 4 How the two roads meet

| Aspect                 | Low-road view                                                           | High-road view                                                                                             | Interaction                                                                     |
| ---------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **What is learned?**   | Approximate value or policy via sampled TD errors.                      | The exact value function solving Bellman’s equations.                                                      | Low-road updates are unbiased Monte-Carlo estimators of high-road targets.      |
| **When useful?**       | Unknown or huge environments; fast, incremental updates.                | Small modelled tasks; formal analysis, safety, explainability.                                             | Combine both: use model learning (DYNA) or offline planning with sampled data.  |
| **Typical algorithms** | TD-learning, Q-learning, SARSA, policy-gradient, actor–critic, deep RL. | Value-iteration, policy-iteration, linear-quadratic regulator, dynamic programming, path-integral control. | Modern systems alternate between model-free (low) and model-based (high) steps. |

---

## 5 Mnemonic

**Low road** = “**Trial-and-error algorithms** first, then ask what they optimise.”
**High road** = “**Optimal-control principle** first, then engineer approximations.”

Both routes end at the same goal: behaviour that maximises long-term reward—just as the two roads of active inference converge on free-energy minimisation.

[1]: https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf?utm_source=chatgpt.com "[PDF] Reinforcement Learning: An Introduction - Stanford University"
[2]: https://gibberblot.github.io/rl-notes/single-agent/temporal-difference-learning.html?utm_source=chatgpt.com "Temporal difference reinforcement learning"
[3]: https://neptune.ai/blog/markov-decision-process-in-reinforcement-learning?utm_source=chatgpt.com "Markov Decision Process in Reinforcement Learning - Neptune.ai"
[4]: https://www.deeplearningwizard.com/deep_learning/deep_reinforcement_learning_pytorch/bellman_mdp/?utm_source=chatgpt.com "Markov Decision Processes (MDP) and Bellman Equations"
[5]: https://www.datacamp.com/tutorial/bellman-equation-reinforcement-learning?utm_source=chatgpt.com "Understanding the Bellman Equation in Reinforcement Learning"
[6]: https://arxiv.org/abs/1801.01290?utm_source=chatgpt.com "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor"
