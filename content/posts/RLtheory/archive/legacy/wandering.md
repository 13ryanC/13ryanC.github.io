---
_build:
  render: never
  list: never

date: "2025-06-30"
title: "Wandering"
summary: "Wandering"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

Below is a compact “concept map” followed by deep dives into each concept.  Throughout, I use the language of **reinforcement learning (RL)** and **statistical physics** because they supply a common mathematical substrate.

---

## 1. How the pieces fit together

| Concept                              | Core question it answers                                                          | Key variable(s)                                                 | Typical mathematical formalism                           | Critical link to the next concept                                                                                              |     |                                                                                                                                          |
| ------------------------------------ | --------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Wandering / physics of foraging**  | *How should an agent move in space when rewards (food) are sparse and uncertain?* | Step‑length distribution \(P(\ell)\), search cost, encounter rate | Random walks, Lévy flights, first‑passage time           | A **greedy** choice of the *next* step length converts the physical search into a policy‑selection problem.                    |     |                                                                                                                                          |
| **Greedy policy**                    | *Which action maximizes *immediate* expected reward?*                             | Action value \(Q(s,a)\)                                           | \(a^\*=\arg\max_{a} Q(s,a)\)                               | Eliminating future look‑ahead creates a **memoryless** (Markov) policy when the state already encodes all necessary history.   |     |                                                                                                                                          |
| **Memoryless policy**                | *Can the agent’s decision depend only on the current state?*                      | Transition kernel (P(s'                                         | s,a))                                                    | Markov decision process (MDP), policy (\pi(a                                                                                   | s)) | A memoryless policy is **optimal** only if the state suffices; when it doesn’t, the agent needs *curiosity* to probe hidden information. |
| **Curiosity (intrinsic motivation)** | *Why explore states that look unrewarding?*                                       | Information gain \(I\), novelty bonus \(\eta\)                      | Intrinsic reward \(r_t^{\text{int}} = \beta \cdot I(s_t)\) | Curiosity systematically tilts behaviour away from purely greedy choices, addressing the **exploration–exploitation dilemma**. |     |                                                                                                                                          |
| **Exploration–exploitation dilemma** | *How should the agent trade immediate reward for long‑term information?*          | Exploration coefficient \(\varepsilon\) or confidence bound \(c\)   | Multi‑armed bandit bounds, regret \(R_T\)                  | The *physics‑of‑foraging* view re‑emerges: balancing long Lévy‑like moves (exploration) with short local moves (exploitation). |     |                                                                                                                                          |

---

## 2. Detailed expositions

### 2.1 Wandering & the physics of foraging

**Problem statement.**  An organism searching for sparsely distributed patches faces a *first‑passage* problem: it must choose a trajectory that minimises the expected time until the next hit.

**Mathematical model.**

* **Random walk / Brownian motion:** step lengths are Gaussian with finite variance. Mean first‑passage time in 2‑D grows \(\sim r^2\).
* **Lévy flight (\(\alpha\)‑stable):** heavy‑tailed \(P(\ell)\propto |\ell|^{-(1+\alpha)}\) with \(1<\alpha\le 3\). Occasional very long jumps decorrelate successive visits, lowering encounter time when targets are sparse.

**Key result (Viswanathan et al., 1999).**  When targets are revisitable and sparse, \(\alpha\approx2\) minimises search time—the celebrated “optimal Lévy foraging”.
*When targets are depleted after visit or are clumped, Brownian (local) search may outperform.*

### 2.2 Greedy (myopic) policy

A *greedy* policy in RL chooses

$$
\pi_{\text{greedy}}(a|s)=\begin{cases}
1 & a=\arg\max_{a'} Q(s,a'),\\
0 & \text{else.}
\end{cases}
$$

It is optimal in a **deterministic** one‑step decision or in *bandits* where \(Q(s,a)\) is known exactly. However, in most sequential tasks it collapses exploration and can converge to a sub‑optimal local maximum.

### 2.3 Memoryless policy

A policy is *memoryless* (Markov) if

$$
\pi(a_t|s_t, s_{t-1},\dots)=\pi(a_t|s_t).
$$

If the state \(s_t\) already embeds the *entire* agent‑environment history relevant for future returns—i.e., the environment is an MDP—then an optimal policy can indeed be Markov (Bellman’s principle).

*But*: biological foragers rarely perceive a fully Markov state (e.g., odor plumes drift). A purely memoryless greedy rule therefore under‑explores hidden resources.

### 2.4 Curiosity (intrinsic rewards)

Curiosity formalises the drive to minimise prediction error or maximise information:

$$
r_t^{\text{int}} = \beta\,\bigl(\mathrm{KL}[P_\theta(s_{t+1}|h_t)||P_{\theta'}(s_{t+1}|h_t)]\bigr)
$$

where \(h_t\) is history, \(\theta\) the current model, and \(\beta\) a gain.

Algorithms:

* **Prediction‑error bonus** (Schmidhuber, 1991).
* **Information‑gain** or Bayesian surprise (Sun et al., 2011).
* **Random‑network distillation** (Burda et al., 2019) approximates novelty cheaply.

Curiosity supplies *intrinsic* reward so that acting greedily with respect to \(r_t^{\text{ext}}+r_t^{\text{int}}\) yields balanced exploration.

### 2.5 Exploration–exploitation dilemma

In **multi‑armed bandits** the goal is to minimise *regret*:

$$
R_T = \sum_{t=1}^{T}( \mu^\* - \mu_{a_t}),
$$

where \(\mu^\*\) is the best arm. Canonical algorithms:

* **\(\varepsilon\)-greedy**: explore uniformly with probability \(\varepsilon\).
* **UCB1**: choose \(a_t=\arg\max_a \bigl(\bar{\mu}_a + c\sqrt{\frac{\ln t}{n_a}}\bigr)\).
* **Thompson sampling**: sample \(Q\) from posterior and act greedily under that sample.

In spatial foraging the same dilemma manifests as the choice between *local exploitation* of a known patch and *global exploration* via longer moves (akin to a Lévy tail).

---

## 3. “Connecting‑the‑dots” narrative

1. **Spatial motion as a policy.**  A forager’s *wandering kernel* \(P(\ell)\) *is* its policy over step lengths. Choosing a Lévy exponent \(\alpha\) is equivalent to picking an *exploration parameter*.

2. **Greedy vs exploratory steps.**  A greedy policy corresponds to \(\alpha\to\infty\): the agent always makes small, exploitative moves that maximise the *immediate* hit probability.

3. **Role of memory.**  If prey positions change slowly and the agent has perfect spatial memory, a greedy memoryless policy can be optimal because the state “distance to nearest known food” suffices. Without memory or with non‑stationary resources, the agent must sample unvisited areas—hence curiosity.

4. **Curiosity as adaptive Lévy adjustment.**  Intrinsic‑motivation algorithms learn when uncertainty about the world model is high; this inflates the value of long steps, effectively lowering \(\alpha\) (heavier tail) and tilting behaviour toward exploration.

5. **Resolution of the dilemma.**  A principled solution (e.g., Bayesian RL) views the dilemma as optimal *sequential experimental design*: explore until the confidence interval on the best action shrinks below a utility margin, then exploit. In physical foraging, this translates to *alternate bursty search*—long jumps until a patch is detected, followed by small diffusive moves within the patch.

---

## 4. Practical implications & open questions

| Question                               | Current insight                                                                 | Open challenge                                                              |
| -------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| *When are Lévy flights truly optimal?* | Proven optimal for non‑depleting, sparse targets with re‑visitable patches.     | Heterogeneous landscapes and predator avoidance complicate the criterion.   |
| *How much memory is needed?*           | Theoretically, a single sufficient statistic (posterior over rewards) suffices. | Biological agents have finite memory—what compression do they actually use? |
| *Designing curious robots.*            | Prediction‑error bonuses yield human‑level performance in sparse‑reward games.  | Scaling to real‑world exploration where sensing is noisy and costly.        |

---

### Key take‑away

> **“Wandering” in space, “curiosity” in state space, and “exploration” in decision space are *formal siblings*: all are strategies for reducing uncertainty under resource constraints.**

A physics‑inspired Lévy search, an RL exploration bonus, or an \(\varepsilon\)-greedy bandit differ only in what *measure of uncertainty* they optimise and at what scale they operate. Understanding these correspondences allows researchers to transfer results—e.g., finite‑time regret bounds—from one domain to another, and helps biologists formalise animal movement, roboticists design search strategies, and data scientists tune RL algorithms.


### Internal plan → sub‑questions we must answer

1. **Formalise “wandering”** as an intrinsic objective in an *infinite‑horizon* MDP and explain why a *greedy, memory‑less* policy can become degenerate.
2. **Analyse pathology**: average‑reward RL can reward endless delay (procrastination, aimless motion).
3. **Instrumental‑convergence angle**: why an indefinitely‑living agent tends to keep *options open* and “just wander”.
4. **Finite‑horizon shock**: what changes, and can a previously aimless agent switch to optimal goal‑directed behaviour?
5. **Robust design tools**: hazard‑rate discounting, multi‑horizon critics, uncertain‑episode‑length RL.
6. **Open issues / tests**.

---

## 1 “Wandering” in an infinite‑horizon, average‑reward MDP

Let an MDP be \((\mathcal{S},\mathcal{A},P,r)\).  In *continuing* tasks we often optimise the **average reward**

$$
\rho^\pi \;=\;\lim_{T\to\infty}\frac1T\; \mathbb{E}_\pi\bigl[\textstyle\sum_{t=0}^{T-1} r(s_t,a_t)\bigr].
$$

*If \(r\equiv0\) until some rare target is reached*, every path has the same average reward (zero).  The **Fundamental Theorem of MDPs** then tells us that *some* deterministic, Markov (memory‑less) policy is optimal, but it need not be unique; any policy that never lowers \(\rho^\pi\) is “optimal” — including aimless Lévy‑flight wandering. ([rltheory.github.io][1], [era.library.ualberta.ca][2])

### Degeneracy

Because the objective is indifferent to **when** the first non‑zero reward arrives, *delaying carries no penalty*.  Computational models of procrastination make exactly this point: with flat average reward, agents rationally delay work or drift endlessly. ([pmc.ncbi.nlm.nih.gov][3], [2019.ccneuro.org][4])

---

## 2 Instrumental‑convergence view

Bostrom’s **instrumental convergence thesis** predicts that long‑lived agents adopt generic sub‑goals (keep options, gather resources, explore).  “Wandering” is one such sub‑goal: by keeping the state distribution broad the agent prevents premature commitment in a non‑stationary world.  Hence an intrinsic “curiosity” drive and an average‑reward objective can coincide. ([en.wikipedia.org][5])

---

## 3 Why the degeneracy disappears when the horizon becomes uncertain

If the agent learns that each step may be its **last** with hazard \(h\), the *true* optimisation problem is

$$
\mathbb{E}_\pi\!\Bigl[\sum_{t=0}^\infty (1-h)^t\,r_t\Bigr]
\;=\;
\mathbb{E}_\pi\!\Bigl[\sum_{t=0}^\infty \gamma^t r_t\Bigr], \quad
\gamma = 1-h.
$$

Bayesian uncertainty about \(h\) converts exponential to **hyperbolic discounting**, yielding finite effective horizons and breaking the symmetry that rewarded delay. ([researchgate.net][6], [openreview.net][7])
Modern RL papers exploit exactly this fact: learning several discount heads or directly learning hyperbolic value functions improves performance when episode lengths are random. ([arxiv.org][8], [ojs.aaai.org][9])

---

## 4 What if a hard deadline suddenly appears?

Add *time‑to‑deadline* \(d\) to the state and the MDP becomes finite‑horizon:

$$
V_t^{\pi}(s,d)=\max_{a}\bigl\{r(s,a)+\mathbb{E}[V_{t+1}^{\pi}(s',d-1)]\bigr\},\qquad d\le D.
$$

Because the state now encodes \(d\), **Bellman optimality again guarantees a deterministic, memory‑less greedy policy**—but w\.r.t. the *new* value function.  Two requirements for the agent to adapt optimally are:

| Requirement                          | Why it matters                                                                  | Practical mechanism                                                                    |
| ------------------------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| ❤️ *Deadline awareness* in the state | Otherwise the policy cannot condition on the shrinking horizon                  | Add \(d\) explicitly, or learn a hazard‑conditioned value function                       |
| ❤️ *Replanning speed*                | Needs to recompute greedy action under new \(V^*\)                                | Model‑based Bellman backup; or multi‑head critics already trained at multiple horizons |
| ❤️ *Curiosity damping*               | High intrinsic reward can still lure the agent away from urgent extrinsic goals | Anneal intrinsic weight \(\beta\) as \(d\downarrow\)                                       |

Algorithms for **uncertain episode length RL** make this explicit: they maintain posterior estimates of the horizon distribution and update policies online; regret bounds match the discounted‑MDP baseline. ([researchgate.net][10], [arxiv.org][11])

---

## 5 Practical design patterns

| Pattern                                            | What it fixes                                                                 | References                                      |
| -------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------- |
| **Hazard‑rate (hyperbolic) discounting**           | Removes procrastination without artificially large γ                          | ([openreview.net][7], [researchgate.net][6])    |
| **Multi‑horizon value heads**                      | Immediate re‑optimisation when \(D\) changes                                    | ([openreview.net][7])                           |
| **Average‑reward ⇄ discounted equivalence tricks** | Combine the stability of discounted TD‑learning with average‑reward semantics | ([era.library.ualberta.ca][2], [arxiv.org][12]) |
| **Termination‑MDP frameworks**                     | Model exogenous deadlines explicitly                                          | ([papers.neurips.cc][13])                       |

---

## 6 Open research issues & tests  *(Progress)*

* **Span‑bias control** in average‑reward RL: new Õ(√T) regret algorithms assume ergodicity; real wandering tasks may violate it.  How robust are policies if some states are transient?
* **Curiosity annealing schedules**: what tapering of intrinsic‑reward weight guarantees bounded regret when deadlines shorten?
* **Empirical test**: run a grid‑world forager with (i) pure average‑reward, (ii) hazard‑rate discounting, then introduce a sudden hard deadline; measure regret and task completion rate.

These open points highlight where further data or proofs are still needed.

---

### Key take‑aways

*With an indefinite horizon, a “curiosity + average‑reward” agent can rationally drift forever; the behaviour is a case‑study in instrumental convergence.*
*Injecting even uncertain knowledge of a possible deadline (hazard) converts the optimisation to a discount‑style or finite‑horizon problem, instantly making procrastination sub‑optimal and enabling a greedy memory‑less policy to focus on tangible goals.*

[1]: https://rltheory.github.io/w2021-lecture-notes/planning-in-mdps/lec2/?utm_source=chatgpt.com "2. The Fundamental Theorem - RL Theory"
[2]: https://era.library.ualberta.ca/items/42307739-a774-4d6b-b1a3-de9fbc949575/view/6fd6b311-d88b-4cf7-8800-831746b681ec/Naik_Abhishek_202404_PhD.pdf?utm_source=chatgpt.com "[PDF] Reinforcement Learning for Continuing Problems Using Average ..."
[3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8481628/?utm_source=chatgpt.com "A Reinforcement Learning Approach to Understanding Procrastination"
[4]: https://2019.ccneuro.org/proceedings/0000509.pdf?utm_source=chatgpt.com "[PDF] Procrastination in Rational Agents"
[5]: https://en.wikipedia.org/wiki/Instrumental_convergence?utm_source=chatgpt.com "Instrumental convergence"
[6]: https://www.researchgate.net/publication/221944679_On_Hyperbolic_Discounting_and_Uncertain_Hazard_Rates?utm_source=chatgpt.com "On Hyperbolic Discounting and Uncertain Hazard Rates"
[7]: https://openreview.net/forum?id=rkezdaEtvH&utm_source=chatgpt.com "Hyperbolic Discounting and Learning Over Multiple Horizons"
[8]: https://arxiv.org/pdf/1902.06865?utm_source=chatgpt.com "[PDF] hyperbolic discounting and learning over multiple horizons - arXiv"
[9]: https://ojs.aaai.org/index.php/AAAI/article/view/26088/25860?utm_source=chatgpt.com "[PDF] Online Reinforcement Learning with Uncertain Episode Lengths"
[10]: https://www.researchgate.net/publication/368333078_Online_Reinforcement_Learning_with_Uncertain_Episode_Lengths?utm_source=chatgpt.com "Online Reinforcement Learning with Uncertain Episode Lengths"
[11]: https://arxiv.org/abs/2302.03608?utm_source=chatgpt.com "Online Reinforcement Learning with Uncertain Episode Lengths"
[12]: https://arxiv.org/pdf/2405.15050?utm_source=chatgpt.com "[PDF] Reinforcement Learning for Infinite-Horizon Average-Reward Linear ..."
[13]: https://papers.neurips.cc/paper_files/paper/2022/file/e83b86156555ab9692743f9f8f67adf1-Paper-Conference.pdf?utm_source=chatgpt.com "[PDF] Reinforcement Learning with a Terminator"


Below is a rigorous, compact formalisation of **“wandering” conceived purely as a *policy* (i.e., a state‑conditioned probability kernel over actions) rather than as a reward‑maximising objective.**  I first give a general definition, then instantiate three common wandering kernels (Brownian, correlated, Lévy) and list their key mathematical properties.

---

## 1 Setting

Let the interaction between an agent and its environment be modelled as a (time‑homogeneous) **Markov decision process (MDP)**

$$
\mathcal M=(\mathcal S,\mathcal A, P, r,\gamma),
$$

with finite or measurable state set \(\mathcal S\) and action set \(\mathcal A\).  A (stochastic) **policy** is a Markov kernel

$$
\pi:\mathcal S\times\mathcal A\;\longrightarrow\;[0,1],
\qquad
\sum_{a\in\mathcal A}\pi(a\mid s)=1.
$$

> **Definition (Wandering policy).**
> A policy \(\pi_{\textsf W}\) is a *wandering policy* if
>
> 1. it is **task‑agnostic**: its specification uses no information from the external reward \(r\);
> 2. it maintains a **non‑degenerate support**: \(\pi_{\textsf W}(a\mid s)>0\) for every state–action pair that keeps the agent mobile;
> 3. its action distribution has statistics that keep the state‑visitation measure \(\upsilon_t\) *broad* or *heavy‑tailed* over time.

In other words, wandering is encoded entirely in \(\pi_{\textsf W}\); any objectives (extrinsic or intrinsic) may be imposed **after‑the‑fact** by off‑policy evaluation or importance weighting.

---

## 2 Three canonical wandering kernels

Below \(x_t\in\mathbb R^d\) denotes position, the action \(a_t\) is a displacement vector, and \(\hat \theta_t\) is the unit heading at time \(t\).

| Kernel                                | Policy density \(\pi(a\mid x)\)                                                                                                                                        | First‑passage scaling                                                                                                                                                                                         | Key parameters / notes                                                       |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **(i) Brownian / simple random walk** | \(\displaystyle \pi_{\text{B}}(a\mid x)=\mathcal N(a;0,\sigma^2I)\) (continuous) or uniform on the \(2d\) unit lattice steps                                             | Mean first‑passage time \(T\!\propto\!R^2\) in 2‑D                                                                                                                                                              | variance \(\sigma^2\) controls diffusion coefficient ([en.wikipedia.org][1])   |
| **(ii) Correlated random walk (CRW)** | Heading persistence: \(\displaystyle\pi_{\text{CRW}}(a\mid \hat\theta_{t-1})\propto\exp\!\bigl(\kappa\,\hat\theta_{t-1}\!\cdot\! \tfrac{a}{\|a\|}\bigr)f(\|a\|)\)      | Effective diffusivity \(D_{\text{eff}}=\tfrac{\sigma^2}{2(1-\rho)}\) with \(\rho=\tanh\kappa\)                                                                                                                    | \(\kappa>0\) (Von‑Mises concentration) gives persistence; \(f(\|a\|)\) as in (i) |
| **(iii) Lévy flight / walk**          | Isotropic step‑length law:  \(\displaystyle\pi_{\alpha}(a\mid x)=\frac{C_\alpha}{\|a\|^{\,1+\alpha}}\;1_{\{\ell_{\min}\le\|a\|\le\ell_{\max}\}}\) with uniform heading | First‑passage exponent transitions from diffusive (\(\alpha\!>\!2\)) to ballistic (\(\alpha\!\le\!1\)); optimally \(\alpha\approx2\) for sparse revisitable targets ([en.wikipedia.org][1], [journals.plos.org][2]) | tail index \(1<\alpha\le3\); truncation \(\ell_{\max}\) ensures finite mean      |

Mathematically, each kernel defines a **state‑transition operator**

$$
P_{\textsf W}(x'\mid x)=\int_{\mathcal A}\!\! \delta\!\bigl(x'-x-a\bigr)\,\pi_{\textsf W}(a\mid x)\,da,
$$

turning \(\{x_t\}\) into a Markov chain whose ergodic, mixing and heavy‑tail properties can be studied independently of any reward.

---

## 3 Relationship to other RL constructs

1. **Behaviour prior.**  In Bayesian or maximum‑entropy RL one often samples actions from a *default* policy \(\mu(a\mid s)\).  Choosing \(\mu=\pi_{\textsf W}\) forces every downstream control law to be absolutely continuous w\.r.t. a wandering measure, guaranteeing coverage of the state‑space.

2. **Off‑policy evaluation.**  Given any extrinsic reward \(r\), one may compute the value

$$
V^{\pi_{\textsf W}}(s)=\mathbb E_{\pi_{\textsf W}}\!\Bigl[\sum_{t\ge0}\gamma^t r(s_t,a_t)\Bigr],
$$

or else re‑weight \(\pi_{\textsf W}\) trajectories with importance ratios \(\tfrac{\pi_\theta}{\pi_{\textsf W}}\) to learn a task‑adapted policy \(\pi_\theta\).

3. **Temperature or tail index as a *knob*.**  The variance \(\sigma^2\) in (i), persistence \(\kappa\) in (ii) or tail exponent \(\alpha\) in (iii) plays the same rôle as the exploration temperature in a soft‑max policy: lowering \(\alpha\) or increasing \(\sigma\) yields wider exploration.

4. **Connection to curiosity.**  Adding an intrinsic reward \(r^{\text{int}}\) does **not** change \(\pi_{\textsf W}\); instead one switches to a new control policy \(\pi_{\text{curious}}\propto\pi_{\textsf W}\exp\bigl(\beta\,Q^{\text{int}}\bigr)\).  Hence wandering can be seen as the *uninformed limit* (\(\beta\to0\)) of curiosity‑driven acting.

---

## 4 Why call it a “policy” rather than an “objective”?

* In the definition above, everything that makes the agent wander is embedded in the stochastic law \(\pi_{\textsf W}\); **no optimisation problem is solved**.
* This mirrors how RL algorithms treat the *behaviour* policy during data collection: it is a *given* kernel, not the solution of a Bellman equation.
* Framing wandering as a policy cleanly separates **physics‑style motion models** (step‑length laws, heading persistence) from **decision‑theoretic objectives** (extrinsic reward, information gain).  One may thus swap in different objectives *post hoc* without altering the exploratory substrate.

---

### Summary

A *wandering policy* is simply a Markov transition kernel whose parameters enforce sustained, uncertainty‑reducing movement—often realised as Gaussian diffusion, correlated walks, or Lévy‑flight tails.  Unlike intrinsic‑motivation formulations, nothing about these kernels requires defining or maximising a utility; they are **behaviour priors** that can later be repurposed by any objective‑driven control layer.

[1]: https://en.wikipedia.org/wiki/L%C3%A9vy_flight "Lévy flight - Wikipedia"
[2]: https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1011528 "Lévy movements and a slowly decaying memory allow efficient collective learning in groups of interacting foragers | PLOS Computational Biology"


Below I build a **formal model of “wandering‑like” behaviour** that

1. **does not rely on expected return or average‑reward as the yard‑stick**,
2. **explains why a greedy, memory‑less policy can drift forever**, and
3. **suggests alternative performance metrics** that capture the phenomenon more faithfully.

The exposition proceeds in four logical steps:

| Step  | Question answered                                                                     |
| ----- | ------------------------------------------------------------------------------------- |
| **A** | *Why is expected return (discounted **or** average) blind to endless drifting?*       |
| **B** | *How can we model drifting when “the goal itself moves” (goal‑drift MDP)?*            |
| **C** | *What does a “wandering‑like” greedy policy look like in that model?*                 |
| **D** | *If not expected return, what should we use to evaluate or constrain such behaviour?* |

---

## A Why the usual value functions miss the pathology

### Average reward (continuing tasks)

For an infinite‑horizon continuing MDP, the objective

$$
\rho^\pi = \lim_{T\to\infty}\frac1T\mathbb E_\pi\!\Bigl[\sum_{t=0}^{T-1} r_t\Bigr]
$$

**ignores when rewards arrive**; all policies that eventually obtain the same long‑run rate are tied.  In sparse‑reward domains the rate is often **zero for every feasible policy**, so endless delay suffers no penalty.  Recent theory even shows that many discounted‑policy‑improvement bounds become vacuous as \(\gamma\!\to\!1\), underscoring the degeneracy of average‑reward optimisation.&#x20;

### Discounted return

A fixed discount \(\gamma<1\) *does* penalise delay, but only at a geometric rate.  If the agent grossly over‑estimates its remaining lifetime, the effective \(\gamma\) it *acts* under is close to 1, recreating the same “why not wait?” incentive.

### Observation

**Neither formulation sees the cost of *starting‑but‑not‑finishing*.**  Something else—progress made, commitments, switching costs—has to be measured.

---

## B A Goal‑Drift MDP (formalising the intuition)

Add an **unobserved, non‑stationary goal variable** \(g_t\in\mathcal G\) to the classic MDP:

* **State observed by the agent:** \(s_t\in\mathcal S\)
* **Latent goal dynamics:** \(g_{t+1}\sim \mathcal P(g_{t+1}\mid g_t)\)
* **Extrinsic reward:** \(r_t = R(s_t,a_t,g_t)\)

The learner sees only \(s_t\), so from its viewpoint the reward function itself **changes over time**.  The tuple \(\bigl(\mathcal S,\mathcal G,\mathcal A,P,R\bigr)\) forms a **Partially Observed, Non‑Stationary MDP (PONMDP)**.

*If \(g_t\) evolves faster than a task can be completed, the optimal myopic response is to “follow the latest carrot”, causing drift.*

---

## C Wandering as a Greedy Policy under Goal Drift

Define the **greedy wandering policy**

$$
\pi_W(a\mid s_t) \;=\; \delta\!\Bigl(a = \arg\max_{a'} \mathbb E_{g_t}[R(s_t,a',g_t)\mid\text{belief }b_t]\Bigr),
$$

where \(b_t\) is the agent’s Bayesian belief over \(g_t\) obtained from past observations.
Because \(g_t\) is unobserved and volatile, \(b_t\) never stabilises; hence \(\pi_W\) keeps **re‑choosing** new “optimal” actions, appearing to **start and abandon subtasks repeatedly**.

Key properties:

| Property                                                              | Mathematical statement                                                                                                                                                                                                                          |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| (P1) *Memory‑less in \(s_t\).*                                          | \(\pi_W\) depends on history only through the current posterior \(b_t\); if \(g_t\) is Markov with rapid mixing, \(b_t\) collapses to the stationary prior—effectively Markov in \(s_t\).                                                                 |
| (P2) *Greedy wrt instantaneous goal.*                                 | No look‑ahead is performed; the agent optimises \(R_t\) for the present \(g_t\).                                                                                                                                                                    |
| (P3) *Drift occurs when \(g_t\) variance exceeds task‑completion time.* | Formally, let \(\tau_\text{finish}\) be the hitting time of a goal state under a stationary goal \(g\).  If \(\mathbb E[\text{number of goal switches in }(t,t+\tau_\text{finish})] \gg 1\), the probability of ever hitting *any* goal goes to zero. |

### Relationship to human “procrastination”

Cognitive‑science models that attribute procrastination to **myopic value estimation** (“pick what feels rewarding *now*”) reproduce the same endless switching. ([pmc.ncbi.nlm.nih.gov][1])

---

## D Better ways to quantify and rein‑in wandering

Because **expected return collapses to ties**, we need **alternative performance metrics**:

| Metric                                      | Captures                                                                      | Formal definition / bound                                                                                                                                                                                    |
| ------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Dynamic regret** (non‑stationary bandits) | Lost utility versus an oracle that *tracks* the moving goal                   | \(\displaystyle R_T^{\text{dyn}}=\sum_{t=1}^{T}\bigl(\mu_{t}^{\*}-\mu_{t}^{a_t}\bigr)\).  Algorithms now minimise \(R_T^{\text{dyn}}\sim\widetilde O(\sqrt{T\!S})\) where \(S\) = #goal switches. ([arxiv.org][2]) |
| **Progress distance**                       | How far the agent moves the environment toward *any* goal before it switches  | A task‑specific Lyapunov function \(L(s)\); require \(\Delta L_t<0\) on average.                                                                                                                                 |
| **Commitment cost / switch penalty**        | Discourages repeated resets                                                   | Augment reward: \(r'_t=r_t-\lambda\cdot\mathbf 1[g_{t}\neq g_{t-1}]\).                                                                                                                                         |
| **Hazard‑rate discounted value**            | Models uncertain horizon so delay is risky                                    | Use \(\gamma_t = (1-h)^t\) with hazard \(h>0\).                                                                                                                                                                  |
| **Option‑completion rate**                  | Fraction of initiated options that terminate successfully within deadline \(D\) | Empirical estimate \(\widehat P(\text{complete}\le D)\).                                                                                                                                                       |

### What “optimal” means here

Instead of maximising \(V^\pi\), we now **minimise dynamic regret *and* bound the switch‑penalty term**.  Under standard assumptions, an agent that incorporates small intrinsic costs for goal‑switching can still achieve the \(O(\sqrt{T})\) dynamic‑regret floor while eliminating unbounded drift.

---

## Practical take‑aways

1. **Phenomenon first, metric second.**  If the real concern is “never finishing”, evaluate **progress‑based or regret‑based** criteria, not time‑averaged reward.
2. **Latent shifting goals are enough to generate drift** even from a purely greedy, memory‑less rule.  The cure is to *expose goal volatility* (through hazard‑discounting or explicit switch costs) so that delay becomes obviously sub‑optimal.
3. **Wandering as a policy** is best viewed as the **behaviour prior** that exploration or curiosity will later refine—not as something to optimise directly.  Analysing it through dynamic regret or option‑completion keeps the formal machinery honest about the downsides of endless starts‑without‑finishes.

---

### Further reading

* Degeneracy of average‑reward optimisation:&#x20;
* RL models of procrastination / myopic valuation: ([pmc.ncbi.nlm.nih.gov][1])
* Dynamic‑regret bounds for non‑stationary goals: ([arxiv.org][2])

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8481628/ "
            A Reinforcement Learning Approach to Understanding Procrastination: Does Inaccurate Value Approximation Cause Irrational Postponing of a Task? - PMC
        "
[2]: https://arxiv.org/abs/2201.06532 "[2201.06532] A New Look at Dynamic Regret for Non-Stationary Stochastic Bandits"



### When an **indefinite‑horizon wanderer** suddenly learns there is a hard deadline

---

#### 1 Problem set‑up

* Before time \(t_0\) the agent behaves under a **wandering policy** \(\pi_{\textsf W}\) (Sec. 2 of our earlier note):

  * no explicit horizon,
  * objective implicitly modelled by average reward or by a very large discount \(\gamma\approx1\).
* At \(t_0\) the environment announces **“only \(D\) steps remain.”**

  * In formal terms, the MDP becomes **finite‑horizon** with state augment \(d\in\{0,\dots,D\}\) (“time‑to‑go”).
  * Extrinsic reward and transition kernels stay unchanged.

---

#### 2 What *should* an optimal agent do?

Because the state is now \((s,d)\), Bellman’s equation turns into a **backward recursion**:

$$
V_d(s)=
\begin{cases}
\max_{a} R(s,a)+\sum_{s'}P(s'|s,a)\,V_{d-1}(s'), & d>0,\\[6pt]
0,& d=0,
\end{cases}
\qquad
\pi^\*(s,d)=\arg\max_{a}\,Q_d(s,a).
$$

*Result:* the optimal policy is **deterministic, greedy and memory‑less *in the enlarged state space***.
All exploration bonuses, curiosity terms, or Lévy‑tail wandering vanish from the policy as \(d\!\to\!0\); they survive only if they add immediate utility.

---

#### 3 Will the *existing* wandering agent make that jump?

| Agent capability                                                 | Behaviour after the announcement                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Time‑aware (\(d\) already part of the observation)**             | One Bellman/actor‑critic update re‑computes \(\pi^\*(\cdot,d)\). Performance drop is \(O(\tfrac{1}{\sqrt{n(d)}})\) where \(n(d)\) is data in the new slice. Empirically, tabular and deep agents equipped with a time channel adapt within a few episodes. ([arxiv.org][1]) |
| **Multi‑horizon critic (many \(γ\)‑heads or hyperbolic ensemble)** | *Zero‑shot adaptation*: pick the head whose effective horizon \(\approx D\); switch instantly.                                                                                                                                                                          |
| **Time‑unaware wandering agent**                                 | Continues drifting; state aliasing makes the deadline invisible, exactly the “Last‑Moment” failure shown by Pardo et al. ([arxiv.org][1])                                                                                                                             |
| **Agent with hazard‑rate discounting**                           | Already used \(\gamma_t=(1-h)^t\); the sudden hard deadline is just the extreme \(h=1\) event, so it naturally becomes short‑sighted and stops wandering.                                                                                                                 |

---

#### 4 Mechanisms that guarantee quick pivot from wandering to goal‑seeking

| Technique                              | How it works                                                                                                                | Practical pointer                                                                                  |                                                                                                |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Add \(d\) to the observation**         | Restores Markov property; lets standard RL instantly condition on “how much time is left.”                                  | Time‑aware PPO & DQN gain 20–50 % return on MuJoCo and Atari when deadlines vary. ([arxiv.org][1]) |                                                                                                |
| **Multi‑horizon / hyperbolic critics** | Learn \(Q_\gamma\) for a grid of \(\gamma\) or learn \(Q(s,a,\gamma)\); at test time pick the \(\gamma\) matching the revealed \(D\). | Efficient Multi‑Horizon Learning (NeurIPS‑22).                                                     |                                                                                                |
| **Meta‑policy over horizons**          | Treat \(D\) as a context variable and meta‑learn a policy (\pi(a                                                              | s,D)).                                                                                             | Time‑Adaptive RL (ICLR‑20 workshop) shows zero‑shot transfer over random \(D\). ([arxiv.org][2]) |
| **Intrinsic‑reward annealing**         | Multiply curiosity bonus by \(\beta(d)=\beta_0\frac{d}{D}\); exploration pressure fades as the deadline looms.                | Used in deadline‑constrained navigation and scheduling tasks.                                      |                                                                                                |
| **Option‑completion penalty**          | Charge \(-\lambda\) for abandoning an option when \(d<D_\text{min}\). Forces commitment near the deadline.                      |                                                                                                    |                                                                                                |

---

#### 5 Corner cases and failure modes

1. **Announcement arrives too late**: if \(D<\tau_{\text{react}}\) (agent’s planning latency), even a perfect planner cannot finish; dynamic regret remains \(\Omega(D)\).
2. **Partial observability**: if the agent only gets a vague “soon” signal rather than exact \(d\), treat horizon as latent and track a belief \(b(d)\); planning becomes a POMDP.
3. **Conflicting intrinsic drives**: strong undamped curiosity may still dominate short‑term extrinsic gain; tuning \(\beta(d)\) is essential.
4. **Non‑stationary goals + deadline**: combine *switch cost* (\(-\lambda\)) with deadline discounting; otherwise the learner may still oscillate between multiple half‑finished goals.

---

#### 6 Take‑away rules for designers

1. **Expose time left**—either explicitly or via a hazard‑rate discount—if you ever expect a wandering system to meet a sudden deadline.
2. **Prepare in advance** with multi‑horizon critics or context‑conditioned actors; “compile once, act at any \(D\).”
3. **Dampen exploration pressure** as \(d\) shrinks; otherwise intrinsic bonuses override urgency.
4. **Measure the right thing** near deadlines: track *option‑completion rate* or *dynamic regret*, not long‑run average reward.

> **Bottom line:** Wandering is rational only under an endless horizon. The moment a credible finite deadline appears, any agent that can *represent* that horizon will pivot from Lévy‑like drifting to sharply goal‑directed exploitation—provided your architecture has given it the state features or value heads to do so.

[1]: https://arxiv.org/pdf/1712.00378 "Time Limits in Reinforcement Learning"
[2]: https://arxiv.org/abs/2004.08600 "[2004.08600] Time Adaptive Reinforcement Learning"


### 1 Recap: the “fundamental theorem” for fully observable MDPs

For any discounted MDP with finite (or Borel) state set \(\mathcal S\), finite action set \(\mathcal A\) and \(\gamma\in(0,1)\),

$$
V^{\!*}(s)=\max_{a\in\mathcal A}\Bigl[r(s,a)+\gamma\sum_{s'}P(s'|s,a)V^{\!*}(s')\Bigr],\qquad  
\pi^{\!*}(s)=\arg\max_{a}Q^{\!*}(s,a),
$$

there exists **at least one deterministic, stationary (Markov) optimal policy** \(\pi^{\!*}\) (Howard 1960; Puterman 1994).  Randomisation or time‑dependent policies are never needed. ([download.e-bookshelf.de][1])

---

### 2 From MDP to POMDP: the information‑state trick

A (time‑homogeneous) **POMDP** augments the hidden state \(x_t\in\mathcal X\) with an observation \(o_t\in\Omega\).
The **belief**

$$
b_t(x)=\Pr(x_t=x\mid o_{0:t},a_{0:t-1})
$$

is a sufficient statistic; the belief dynamics are Markov:

$$
b_{t+1}=T(b_t,a_t,o_{t+1}).
$$

Define the **belief‑MDP** \(\widehat{\mathcal M}\equiv(\mathsf B,\mathcal A,\widehat P,\widehat r,\gamma)\) where \(\mathsf B\) is the simplex of probability distributions over \(\mathcal X\).
Smallwood & Sondik (1973, 1978) proved

> **POMDP fundamental theorem.**
> For any discounted POMDP with finite \(\mathcal X,\mathcal A\) and \(\gamma\in(0,1)\)
>
> * the optimal value function \(V^{\!*}(b)\) on \(\mathsf B\) is the unique fixed point of the Bellman operator,
> * \(V^{\!*}\) is piece‑wise linear and convex, and
> * there exists an optimal **deterministic, stationary policy over beliefs**
>   \(\pi^{\!*}:\mathsf B\!\to\!\mathcal A\). ([techfak.uni-bielefeld.de][2])

Thus the “MDP theorem’’ survives **unchanged** once we replace “state’’ by “information state (belief)”.

---

### 3 PONMDP ≔ “partially observed, *non‑stationary* MDP’’

Let the hidden state factor into

$$
x_t=(s_t,\,g_t),\qquad g_{t+1}\sim \underbrace{\mathcal P(g_{t+1}\mid g_t)}_{\text{exogenous\,mode}},
$$

where \(g_t\) encodes the **mode that makes dynamics or rewards drift**.
The agent sees only an observation \(o_t\) generated from \(x_t\).  We call this a **PONMDP** (Kaelbling et al. 1998; Lecarpentier & Rachelson 2019). ([en.wikipedia.org][3], [papers.neurips.cc][4])

*If the mode process \(\{g_t\}\) itself is Markov and **time‑homogeneous**, we can still treat \((s_t,g_t)\) as the latent state of an ordinary POMDP.*
Nothing in Smallwood–Sondik’s proof relies on the state being fully observable or “task” being stationary—only on:

* finite latent state,
* bounded rewards,
* discount \(\gamma<1\).

#### **PONMDP fundamental theorem (discounted case)**

Assume

1. finite sets \(\mathcal S,\mathcal G,\mathcal A\);
2. discount \(\gamma\in(0,1)\);
3. transition kernel \(P\bigl((s',g')\mid s,g,a\bigr)\) that is stationary in time;
4. reward \(r(s,g,a)\) bounded.

Define the joint belief

$$
b_t(s,g)=\Pr(s_t=s,g_t=g\mid o_{0:t},a_{0:t-1}).
$$

Then

* the belief process \(b_t\) is Markov under any policy;
* the Bellman operator

  $$
  (\mathcal T V)(b)=\max_{a}\Bigl[\widehat r(b,a)+\gamma\!\!\sum_{o} \Pr(o\mid b,a)\,V\bigl(T(b,a,o)\bigr)\Bigr]
  $$

  is a \(\gamma\)-contraction on the space of bounded functions;
* its unique fixed point \(V^{\!*}\) is **piece‑wise linear and convex** when \(\mathcal X\) is finite;
* a **deterministic stationary policy**

  $$
  \pi^{\!*}(b)=\arg\max_{a}\bigl[\widehat r(b,a)+\gamma\sum_{o}\Pr(o\mid b,a)V^{\!*}(T(b,a,o))\bigr]
  $$

  is optimal.
  Hence the ordinary “fundamental theorem’’ survives verbatim: randomness and explicit time dependence are unnecessary once the **belief over \((s,g)\)** is used as the state.

Citations: Sondik’s infinite‑horizon proof extends directly; Kaelbling et al. give the modern belief‑MDP formulation. ([en.wikipedia.org][3], [users.isr.ist.utl.pt][5])

---

### 4 What if the non‑stationarity is **time‑driven**?

If transition or reward kernels really depend on an absolute deadline \(d\) (e.g. “\(D\) steps left’’) we enlarge the latent state to \((s_t,g_t,d_t)\) with \(d_{t+1}=d_t-1\).
Because \(d_t\) decrements deterministically, the augmented process **is stationary**, and the theorem above now yields an optimal policy that is

* deterministic **in the augmented belief** \((b_t,d_t)\);
* therefore *time‑dependent* when viewed only through observable variables—a direct generalisation of the classic finite‑horizon result. ([people.csiro.au][6])

---

### 5 When the theorem **fails**

* If \(g_t\) is *adversarial* or changes without a stationary Markov law, the belief process is no longer Markov; no optimal stationary policy is guaranteed.  Research then shifts to **dynamic‑regret** bounds instead of optimality. ([papers.neurips.cc][4])
* With continuous \(\mathcal G\) one still gets existence, but measurability conditions (Polish spaces, bounded rewards, etc.) are required; proofs mirror the MDP case (Bertsekas & Shreve 1996).

---

### 6 Take‑away

> **POMDPs and their non‑stationary cousins obey the same structural theorem once you promote the agent’s *information state* (belief, plus any needed clock) to be “the state’’ of a fully observable MDP.**

The price of partial observability is **not** the loss of an optimal deterministic policy—it is the explosion of state dimensionality (continuous simplex of beliefs) and computational hardness.

[1]: https://download.e-bookshelf.de/download/0000/5714/47/L-G-0000571447-0015280627.pdf?utm_source=chatgpt.com "[PDF] Markov Decision Processes - download"
[2]: https://www.techfak.uni-bielefeld.de/~skopp/Lehre/STdKI_SS10/POMDP_solution.pdf?utm_source=chatgpt.com "[PDF] POMDP solution methods"
[3]: https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process "Partially observable Markov decision process - Wikipedia"
[4]: https://papers.neurips.cc/paper/8942-non-stationary-markov-decision-processes-a-worst-case-approach-using-model-based-reinforcement-learning.pdf "Non-Stationary Markov Decision Processes, a Worst-Case Approach using Model-Based Reinforcement Learning"
[5]: https://users.isr.ist.utl.pt/~mtjspaan/readingGroup/slides12022007.pdf?utm_source=chatgpt.com "[PDF] Partially observable Markov decision processes"
[6]: https://people.csiro.au/-/media/People-Finder/F/J/jonathan-ferrermestres/POMDP_MEE2021.pdf?utm_source=chatgpt.com "[PDF] A primer on partially observable Markov decision processes ..."


Below is a step‑by‑step, fully formal answer. I first restate the classic *Fundamental Theorem* for discounted MDPs, then show—mathematically and with precise conditions—how it **continues to hold** the instant a hard deadline is revealed, provided we *augment the state with a countdown*.
Where it *doesn’t* hold (if you insist on keeping the original state description) I explain why, and how much of the past now matters.

---

## 1 Classical result (Puterman 1994)

For a discounted, time‑homogeneous MDP

$$
\mathcal M=(\mathcal S,\mathcal A,P,r,\gamma),\quad 
|\mathcal S|,\;|\mathcal A|<\infty,\;0<\gamma<1,
$$

Puterman’s Theorem 6.2.7 guarantees

* a unique optimal value function \(V^\*\) solving the Bellman fixed‑point equation, and
* **at least one deterministic, stationary (Markov) policy**

  $$
  \pi^\*\!:\mathcal S\to \mathcal A,\qquad  
  \pi^\*(s)=\arg\!\max_{a}Q^\*(s,a). 
  \] :contentReference[oaicite:0]{index=0}  
  $$

The proof relies on the **contraction** of the Bellman operator in the sup‑norm with modulus \(\gamma\).

---

## 2 After the surprise deadline: build a *countdown‑augmented* MDP

At announcement time \(t_0\) the agent learns “exactly \(D\) steps remain.”
Create an **augmented state space**

$$
\widetilde{\mathcal S}= \mathcal S\times\{0,1,\dots,D\},\qquad  
\tilde s_t=(s_t,d_t),\; d_t=D-(t-t_0).
$$

Transition kernel and rewards:

$$
\tilde P\bigl((s',d-1)\mid(s,d),a\bigr)=P(s'|s,a),\; (d>0),\qquad  
\tilde r((s,d),a)=r(s,a).
$$

Because \(d_{t+1}=d_t-1\) the joint dynamics are **still time‑homogeneous**.
Therefore \(\widetilde{\mathcal M}= (\widetilde{\mathcal S},\mathcal A,\tilde P,\tilde r,\gamma)\) is an *ordinary* discounted MDP with finite state space.

---

### 2.1 Bellman operator in the new space

For \(d>0\):

$$
(\mathcal T V)(s,d)=\max_{a}\Bigl[r(s,a)+\gamma\sum_{s'}P(s'|s,a)\,V(s',d-1)\Bigr],
\qquad   
(\mathcal T V)(s,0)=0.
$$

* **Contraction:** \(\|\mathcal T V-\mathcal T W\|_\infty\le\gamma\|V-W\|_\infty\);
* **Fixed point:** unique \(V^\*\) on \(\widetilde{\mathcal S}\);
* **Optimal policy:**

  $$
  \pi^\*_{\text{aug}}(s,d)=
  \arg\max_{a}\Bigl[r(s,a)+\gamma\sum_{s'}P(s'|s,a)V^\*(s',d-1)\Bigr].
  $$

Hence **Puterman’s theorem applies *immediately*** in the countdown‑augmented state space.

---

### 2.2 How the policy looks in the *original* state space

Define \(\mu_t(s)=\pi^\*_{\text{aug}}\bigl(s,d_t\bigr).\)

Because \(d_t\) is a deterministic function of elapsed time,
\(\mu_t\) is **deterministic but non‑stationary** when viewed only through \(\mathcal S\).
The countdown is the *only* piece of history that matters; longer‑range history is still irrelevant.

---

## 3 What if you *refuse* to augment with \(d_t\)?

If the agent’s internal state ignores \(d_t\), the environment is **no longer Markov** from its viewpoint; the Bellman operator need not be a contraction and no stationary policy is guaranteed.
The fundamental theorem then *fails for the agent* (though it is still true for the omniscient modeller who sees \(d_t\)).  

---

## 4 Undiscounted finite horizon (γ = 1)

Many deadline problems use **total reward** over a horizon \(D\).
Set

$$
V_0(s)=0,\quad
V_{k}(s)=\max_{a}\Bigl[r(s,a)+\sum_{s'}P(s'|s,a)\,V_{k-1}(s')\Bigr]
\quad(k=1,\dots,D).
$$

This **dynamic‑programming recursion** (backwards induction) yields
deterministic decision rules \(\pi_k(s)\).
The optimal policy is *Markov in \((s,d)\)* but **cannot be stationary** because \(\gamma=1\) eliminates contraction.  Classic finite‑horizon texts prove existence of such time‑indexed deterministic policies. ([people.eecs.berkeley.edu][1])

---

## 5 Partial observability (PONMDP) with a deadline

Replace \(s_t\) by the hidden pair \((x_t,g_t)\).
Belief \(b_t:=\Pr(x_t,g_t\mid\text{history})\) evolves via a Bayes filter *and* the deterministic countdown \(d_t\).
The belief‑countdown pair \((b_t,d_t)\) is a fully observable state of a **belief‑MDP**:

* Bellman operator on the (continuous) belief simplex is still a \(\gamma\)‑contraction;
* Optimal policy is **deterministic, stationary in \((b,d)\)** and piece‑wise linear–convex in \(b\). ([techfak.uni-bielefeld.de][2], [stats.stackexchange.com][3])

Thus even in the PONMDP, the augmented fundamental theorem remains valid; only the state explosion (belief × countdown) complicates computation.

---

## 6 Role of prior history under a sudden deadline

| Information carried from history                               | Needed after deadline? | Why                                                        |
| -------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------- |
| Countdown \(d_t\) (= time since announcement)                    | **Yes**                | Determines which slice \((s,d)\) the Bellman recursion uses. |
| Sufficient statistic for hidden state (belief)                 | **Yes** in PONMDP      | Keeps Markov property.                                     |
| Earlier action/observation sequence beyond those two summaries | **No**                 | Fully absorbed by \((b_t,d_t)\).                             |

So **history gains importance only through these *two* low‑dimensional summaries**; no further dependence arises.

---

## 7 Key take‑aways

1. **Add the countdown to the state** and the discounted‑MDP fundamental theorem applies *immediately*: a deterministic, stationary optimal policy exists in the enlarged space.
2. If you omit the countdown (state aliasing) or move to γ = 1 without augmenting state, stationarity is lost; the best you can guarantee is a deterministic **time‑indexed** policy from backward induction.
3. In PONMDPs, augment the *belief* with the countdown; the classic Smallwood‑Sondik structure theorem (piece‑wise linear convex value) plus contraction yields the same existence result.

In short: **wandering plus hard deadline ⇒ new Markov state = (belief, countdown)**.
Switching to that state instantly restores all the structural guarantees you relied on before the deadline arrived.

[1]: https://people.eecs.berkeley.edu/~jiantao/2902021spring/scribe/EE290_Lecture_16.pdf?utm_source=chatgpt.com "[PDF] Lecture 16 (Planning Algorithms for Markov Decision Processes)"
[2]: https://www.techfak.uni-bielefeld.de/~skopp/Lehre/STdKI_SS10/POMDP_solution.pdf?utm_source=chatgpt.com "[PDF] POMDP solution methods"
[3]: https://stats.stackexchange.com/questions/600900/existence-of-the-optimal-control-in-finite-horizon-mdp?utm_source=chatgpt.com "Existence of the optimal control in finite horizon MDP - Cross Validated"



Below is an \*\*intuitive “picture‑book” of the two classic dynamic‑programming algorithms—value iteration (VI) and policy iteration (PI)—drawn in the space of *trajectory distributions*.  The same construction works

* for the **pre‑deadline** “wandering” world (indefinite horizon, implicit discount γ≈1), and
* for the **post‑announcement** world where we add a deterministic *count‑down* \(d\in\{D,D-1,\dots ,0\}\) to the state.

I first build the geometry, then show how VI and PI move inside it.

---

## 1 The trajectory / occupancy simplex

### 1.1 Finite‑horizon (after the deadline is known)

*Horizon* \(H=D\).
A **length‑\(H\) trajectory** is

$$
\tau=(s_0,a_0,\dots ,a_{H-1},s_H)\in(\mathcal S\times\mathcal A)^{H-1}\times\mathcal S .
$$

Let \(N:=|\mathcal S|\cdot|\mathcal A|^{H-1}\cdot|\mathcal S|\).
Any stochastic policy–dynamics pair induces a point

$$
q_\pi\in\Delta^{N-1}\!:=\Bigl\{q\in\mathbb R^{N}_{\ge0}\;:\;\sum_\tau q(\tau)=1\Bigr\},
$$

i.e. a **probability simplex** over trajectories.

---

### 1.2 Why not every point is feasible

Because trajectories must respect dynamics, the feasible set is a *lower‑dimensional polytope* inside the simplex, defined by the **flow (occupancy) constraints**

$$
\sum_{a}q_h(s,a)=\sum_{s',a'}q_{h-1}(s',a')\,P(s\mid s',a')\quad(1\le h\le H),\tag{C1}
$$

where
\(q_h(s,a)=\Pr_\pi[s_h=s,a_h=a]\).

$$
\mathcal Q_H:=\Bigl\{q\ge0\text{ satisfying (C1)}\Bigr\}\subset\Delta^{N-1}\quad\text{(the **occupancy polytope**)}.:contentReference[oaicite:0]{index=0}
$$

* **Vertices (extreme points)** of \(\mathcal Q_H\) correspond *one‑to‑one* to **deterministic Markov policies** on the *augmented* state \((s,d)\).([mit.edu][1])
* Edges connect policies that differ in exactly **one** state–deadline slice—crucial for PI below.

---

### 1.3 Indefinite horizon (the wandering era)

With discount γ, the **discounted occupancy measure**

$$
\rho_\pi(s,a)=\mathbb E_\pi\!\Bigl[\sum_{t=0}^{\infty}\gamma^{t}\mathbf 1\{s_t=s,a_t=a\}\Bigr]
$$

lives in a *countably*‑infinite but still *polyhedral* set

$$
\mathcal Q_\gamma=\Bigl\{\rho\ge0: \ \rho(s')=\mathbf d_0(s')+\gamma\sum_{s,a}\rho(s,a)P(s'|s,a)\Bigr\}.
$$

Setting γ = 1 collapses the constraints and creates the **degeneracy** that allowed wandering.

---

## 2 The objective as a *hyper‑plane*

For either horizon,

$$
\text{Value of a policy } \pi
\;=\;
\langle r,\,q_\pi\rangle
\quad(\text{finite }H),
\qquad
=
\langle r,\,\rho_\pi\rangle
\quad(\text{discounted}),
$$

i.e. the dot‑product of the reward vector with the occupancy point.
Therefore *solving an MDP is just a **linear programme** over \(\mathcal Q\)*.

---

## 3 Geometric life of **value iteration**

VI lives in **value‑function space** \( \mathbb R^{|\widetilde{\mathcal S}|}\) rather than in \(\mathcal Q\), but there is a dual picture:

1. Each Bellman backup

   $$
   (\mathcal TV)(s,d)=\max_{a}\bigl[r(s,a)+\gamma\,\!*V\bigr]
   $$

   is the **point‑wise maximum of affine maps** → a convex, piece‑wise‑linear operator.
2. Geometrically, you start with some \(V_0\) and apply a **γ‑contraction** that pulls every point straight toward the *unique* fixed point on the top surface of that polyhedral “roof”.([rltheory.github.io][2])
3. In the trajectory picture, \(V_k\) is the slope of a supporting hyper‑plane to the value polytope; each iteration steepens the plane until it just touches the facet corresponding to an optimal deterministic policy (vertex of \(\mathcal Q\)).

So VI is **successive tangent‑plane tightening** on the convex roof of achievable returns.

---

## 4 Geometric life of **policy iteration**

Policy iteration works **directly inside \(\mathcal Q\)**:

1. **Policy‑evaluation step** fixes a vertex \(q_{\pi_i}\).
2. The **greedy‑improvement step** looks at the *advantage*

   $$
   A_{\pi_i}(s,d,a)=Q_{\pi_i}(s,d,a)-V_{\pi_i}(s,d)
   $$

   and, if positive, **swaps** \(a\) into the policy at slice \((s,d)\).

*Swapping an action in exactly one slice moves \(q_{\pi_i}\) along an **edge of \(\mathcal Q_H\)** to an *adjacent* vertex \(q_{\pi_{i+1}}\) with strictly higher objective, exactly like a **simplex pivot**.([web.stanford.edu][3])*

Hence PI is “**edge‑walking on the occupancy polytope**” until it reaches a reward‑maximising vertex.

---

## 5 Where does **prior history** show up?

* All of \((S\times A)^{t-1}\times S\) collapses into a **single occupancy vector** \(q\) that obeys linear flow constraints.
* When the deadline is revealed, we *double* state‑indices with \(d\); the polytope simply becomes a **layered product** of \(H\) identical flow constraints—still linear, still with vertices = deterministic Markov in \((s,d)\).
* No other aspect of the past is needed: history influences future control only through the current **coordinate** in that larger polytope.

---

### Visual summary

| Algorithm            | Space it moves in                                          | Geometric move                                        | Fixed point / terminus                       |                                                            |                                                            |
| -------------------- | ---------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| **Value iteration**  | (\mathbb R^{                                               | \widetilde{\mathcal S}                                | }) (value vectors)                           | γ‑contraction toward top facet of a piece‑wise‑linear roof | Single point where the tangent plane touches optimal facet |
| **Policy iteration** | Occupancy polytope \(\mathcal Q_H\) (or \(\mathcal Q_\gamma\)) | Simplex‑style edge pivot from vertex to better vertex | Optimal vertex = deterministic Markov policy |                                                            |                                                            |

With the deadline, we *embed* everything in a higher‑dimensional but still convex polytope; the **Fundamental Theorem** continues to guarantee that an optimal solution is found at a vertex, so both algorithms keep their geometric character—only the dimension of the polytope (and hence the size of each edge step) grows.

[1]: https://www.mit.edu/~jnt/Papers/J098-05-sm-MDP.pdf?utm_source=chatgpt.com "[PDF] On the Empirical State-Action Frequencies in Markov Decision ... - MIT"
[2]: https://rltheory.github.io/lecture-notes/planning-in-mdps/lec2/?utm_source=chatgpt.com "2. The Fundamental Theorem - RL Theory"
[3]: https://web.stanford.edu/~yyye/SimplexMDP4.pdf?utm_source=chatgpt.com "[PDF] The Simplex and Policy-Iteration Methods are Strongly Polynomial ..."


Below is a **fully worked derivation** of **value iteration (VI)** for the
“ **surprise‑deadline** ” version of our wandering agent.
Everything is expressed *first* in the standard algebraic style, *then* in the occupancy‑measure / trajectory‑geometry style so you can see how the steps line up with the intuitive polytope picture sketched earlier.

---

## 0 Notation recap

| Symbol                                                   | Meaning                                                 |                                            |
| -------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------ |
| \(\mathcal S\)                                             | physical state set (finite)                             |                                            |
| \(D\)                                                      | number of steps *remaining* after the announcement      |                                            |
| \(d\in\{0,\dots ,D\}\)                                     | countdown clock; \(d=0\) terminates the episode           |                                            |
| \(\widetilde{\mathcal S}:=\mathcal S\times\{0,\dots ,D\}\) | **augmented state**                                     |                                            |
| \(\gamma\in(0,1)\)                                         | discount factor (kept constant before & after deadline) |                                            |
| (\tilde P\bigl((s',d-1)\mid(s,d),a\bigr)=P(s'            | s,a))                                                   | time‑homogeneous kernel in augmented space |
| \(\tilde r((s,d),a)=r(s,a)\)                               | reward does **not** depend on \(d\)                       |                                            |

---

## 1 Bellman operator in the augmented space

Define the **optimal Bellman operator**

$$
(\mathcal T V)(s,d)=
\begin{cases}
\displaystyle\max_{a\in\mathcal A}\!\Bigl[r(s,a)+\gamma\sum_{s'}P(s'|s,a)V(s',d-1)\Bigr], & d>0,\\[10pt]
0,& d=0.
\end{cases}\tag{1}
$$

*The \(d=0\) boundary condition encodes the hard deadline.*

---

### 1.1 \(\mathcal T\) is a γ‑contraction

For any two bounded value vectors \(V,W\in\mathbb R^{|\widetilde{\mathcal S}|}\)

$$
\|\mathcal TV-\mathcal TW\|_\infty
\;\le\;
\gamma\,\|V-W\|_\infty, \qquad\text{sup‑norm}. \qquad\quad\text{(Puterman, 1994)}:contentReference[oaicite:0]{index=0}
$$

The proof uses the usual “subtract same actions” trick inside the max and the triangle inequality; the countdown index \(d\) plays no rôle—it merely says “if \(d=0\) both sides are zero”.

---

### 1.2 Existence and uniqueness of the fixed point

Because \(\mathcal T\) is a γ‑contraction on a complete normed space, the **Banach fixed‑point theorem** gives

$$
V^{\!*}=\lim_{k\to\infty}\mathcal T^{\,k}V_0, \qquad
\|V_k-V^{\!*}\|_\infty\le\gamma^{k}\|V_0-V^{\!*}\|_\infty.\tag{2}
$$

So VI converges **exponentially fast** in iterations, exactly as in an ordinary discounted MDP.

---

## 2 Value‑iteration algorithm, step by step

```text
Input : V0  (arbitrary, e.g. all zeros)
For k = 0,1,2,...
    For each (s,d) with d>0
        Vk+1(s,d) ← maxa [ r(s,a) + γ Σs' P(s'|s,a) Vk(s',d-1) ]
    Vk+1(s,0) ← 0   for all s
Output: V* ≔ limit of Vk
```

* **Policy extraction (optional each sweep)**

  $$
  \pi_{k+1}(s,d)=\arg\max_{a}\Bigl[r(s,a)+\gamma\!\sum_{s'}P(s'|s,a)\,V_k(s',d-1)\Bigr].\tag{3}
  $$

  When \(\|\mathcal T V_k - V_k\|_\infty<\varepsilon\frac{1-\gamma}{2\gamma}\) the policy \(\pi_k\) is \(\varepsilon\)-optimal. (Standard stopping rule.)

---

### 2.1 Why *only* today’s value matters

The update for slice \(d\) depends **only on slice \(d-1\)**.
Thus VI sweeps *backwards through the countdown* exactly like tabular dynamic programming for finite horizons; nevertheless we are still running **one** contraction in the enlarged state space, not \(D\) separate ones.

---

## 3 Occupancy‑measure (geometric) view

### 3.1 Layered occupancy variables

For \(h=0,\dots ,D-1\)

$$
q_h(s,a)=\Pr_{\pi}\![s_h=s,\,a_h=a],\qquad
q_{h+1}(s)=\sum_{a}q_h(s,a)P(s'|s,a).
$$

Stack \(q:=\bigl(q_0,\dots ,q_{D-1}\bigr)\).
Flow constraints give a **polytope**

$$
\mathcal Q_{D}=\Bigl\{q\ge0 : q_{h+1}(s')=
\sum_{s,a}q_h(s,a)P(s'|s,a)\Bigr\}. \tag{4}
$$

Vertices correspond one‑to‑one with deterministic Markov policies on \((s,d)\) because choosing a single action for every slice \((s,d)\) fixes a unique feasible flow q.([rltheory.github.io][1])

### 3.2 Value as a hyper‑plane

$$
\langle r, q\rangle
=\sum_{h=0}^{D-1}\sum_{s,a} \gamma^{\,h}\,r(s,a)\,q_h(s,a).
$$

The VI fixed point \(V^{\!*}\) is exactly the slope of the **supporting hyper‑plane** that touches \(\mathcal Q_D\) at the optimal vertex.

### 3.3 What a Bellman backup does geometrically

* Start with a hyper‑plane slope \(V_k\).
* Compute, for each \((s,d)\), the action that yields the steepest ascent in direction \(V_k\).
* This is equivalent to *pivoting* the current hyper‑plane until it *touches but never cuts* the polytope—hence the
  “tangent‑plane tightening’’ picture mentioned earlier.

Because each pivot is dominated by \(\gamma\), the hyper‑plane tilts ever less with each sweep, mirroring the contraction of Equation (2).

---

## 4 Connection to the **pre‑deadline wandering phase**

With no clock, the state is just \(s\) and the occupancy set collapses to \(\mathcal Q_\gamma\).
When the deadline arrives we **embed** \(\mathcal Q_\gamma\) into the larger \(\mathcal Q_D\) by replicating each old state across \(d\)-layers.
VI simply continues in the new space; the previous value vector supplies **warm‑start initialisation** for layers \(d\!\approx\!D\).

---

## 5 Does any longer‑range *history* enter the Bellman equations?

No.  All dependencies are funnelled through the countdown coordinate:

$$
P\bigl((s',d-1)\mid(s,d),a\bigr)\;
\Longrightarrow\;
V_{k+1}(s,d)=f\bigl(V_k(\cdot,d-1)\bigr).
$$

Thus the *entire* past beyond the belief/state summary—and that single integer \(d\)—remains irrelevant **even after** the sudden horizon change.

---

### Recap

1. **Define** the countdown‑augmented Bellman operator (1).
2. **Show contraction** ⇒ unique fixed point and exponential error decay (2).
3. **Implement** VI as Equation (3); every sweep is one pass *backwards* through \(d\).
4. **Geometric view:** each backup is a γ‑scaled pivot of a supporting hyper‑plane over the occupancy polytope \(\mathcal Q_D\).
5. **History** beyond the \((s,d)\) pair never re‑enters; the wandering agent instantly has a Markovian framing once the clock is added.

These steps supply the full mathematical scaffolding behind the earlier intuition of “value iteration = successive tangent‑plane tightening” in the surprise‑deadline setting.

[1]: https://rltheory.github.io/lecture-notes/planning-in-mdps/lec2/?utm_source=chatgpt.com "2. The Fundamental Theorem - RL Theory"


Below are the **missing “glue” steps** that tie the surprise‑deadline value‑iteration derivation to the two classic theorems you asked about.

---

## 1 Banach Fixed‑Point Theorem ⇒ existence & uniqueness of \(V^{\!*}\)

### 1.1 Set‑up as a contraction mapping

* **Metric space.**

  $$
  \bigl(\mathbb R^{|\widetilde{\mathcal S}|},\;\|\cdot\|_\infty\bigr)
  \quad\text{with}\quad
  \widetilde{\mathcal S}=\mathcal S\times\{0,\dots ,D\}.
  $$

  This is complete because it is finite‑dimensional.

* **Bellman operator** (same as Eq. (1) last reply):

  $$
  (\mathcal T V)(s,d)=
  \begin{cases}
     \displaystyle\max_{a}\Bigl[r(s,a)+\gamma\sum_{s'}P(s'|s,a)V(s',d-1)\Bigr], & d>0,\\
     0,& d=0.
  \end{cases}
  $$

* **Contraction proof.**
  For any \(V,W\)

  $$
  |(\mathcal T V)(s,d)-(\mathcal T W)(s,d)|
  \;\le\;
  \gamma\max_{a}\sum_{s'}P(s'|s,a)|V(s',d-1)-W(s',d-1)|
  \le
  \gamma\|V-W\|_\infty.
  $$

  So \(\|\mathcal T V-\mathcal T W\|_\infty\le\gamma\|V-W\|_\infty\) with \(0<\gamma<1\).

### 1.2 Invoke Banach

**Banach Fixed‑Point Theorem (1922).**
If \(\mathcal F\) is a contraction on a complete metric space, it has exactly one fixed point \(x^\*\); the Picard iterates \(x_{k+1}=\mathcal F x_k\) converge to \(x^\*\) at geometric rate.

Apply with \(\mathcal F\equiv\mathcal T\).
⇒ Unique \(V^{\!*}\) satisfying \(V^{\!*}=\mathcal T V^{\!*}\) and
\(\|V_k-V^{\!*}\|_\infty\le\gamma^k\|V_0-V^{\!*}\|_\infty\).

---

## 2 Fundamental Theorem of MDPs ⇒ existence of a deterministic, stationary optimal policy

### 2.1 Greedy policy w\.r.t. \(V^{\!*}\)

Define

$$
\pi^{\!*}(s,d)\;=\;\arg\max_{a}\Bigl[r(s,a)+\gamma\sum_{s'}P(s'|s,a)V^{\!*}(s',d-1)\Bigr].
$$

Because the maximiser can be chosen deterministically (finite actions), \(\pi^{\!*}\) is deterministic and **stationary** in the augmented state \((s,d)\).

### 2.2 Optimality proof

For any policy \(\pi\) let \(Q_\pi\) be its state–action value.
Bellman optimality of \(V^{\!*}\) implies

$$
Q_\pi(s,d,\pi^{\!*}(s,d))\;\le\;V^{\!*}(s,d)
\quad\text{and}\quad
Q_{\pi^{\!*}}(s,d,a)\;\le\;V^{\!*}(s,d)\quad\forall a.
$$

Unfolding one step and using induction on \(d\) shows \(V_{\pi^{\!*}}=V^{\!*}\ge V_\pi\;\forall\pi\).
Therefore \(\pi^{\!*}\) is globally optimal.

### 2.3 Connection to the classical statement

Puterman’s (1994) “Fundamental Theorem” reads:

> *For any finite, discounted MDP there exists at least one deterministic, stationary optimal policy.*

We are **still** in a finite, discounted MDP—only the state set is \(\widetilde{\mathcal S}\).
Hence the theorem applies verbatim the instant the countdown is appended.

---

## 3 How these two theorems underpin value iteration in our scenario

| Step in the VI proof                                         | Theorem invoked                                                       |
| ------------------------------------------------------------ | --------------------------------------------------------------------- |
| Show \(\mathcal T\) contracts ⇒ unique fixed point             | **Banach**                                                            |
| Convergence rate \(\|V_k-V^{\!*}\|_\infty\le\gamma^k\Delta_0\) | **Banach**                                                            |
| Extract greedy deterministic \(\pi^{\!*}\)                     | **Fundamental Theorem** (guarantees such a \(\pi^{\!*}\) is sufficient) |
| Prove \(\pi^{\!*}\) optimal                                    | **Fundamental Theorem + Bellman optimality**                          |

Thus Banach gives us **existence & uniqueness of the value**, while the Fundamental Theorem tells us that *knowing that value* is enough to read off a **deterministic, stationary, Markov policy** which attains it—even after the horizon shock.

---

### Take‑away

* **Banach fixed‑point theorem** ≡ the engine that makes value iteration converge.
* **Fundamental theorem of MDPs** ≡ the guarantee that the fixed point defines a simple deterministic stationary policy that is optimal in the countdown‑augmented world.

With both pieces explicitly spelled out, every algebraic step in value iteration for the surprise‑deadline problem now rests on these two foundational results.



Below is a **complete mathematical walkthrough of *policy iteration* (PI)** for the

> **“surprise‑deadline” MDP**
> in which, at time \(t_{0}\), the agent suddenly discovers that only \(D\) steps remain.
> Exactly as in the value‑iteration proof, we first *augment the state* with a countdown \(d\) and then analyse PI in that enlarged—but still finite and discounted—MDP.

---

## 0 Set‑up recap

* **Augmented state space** \(\widetilde{\mathcal S}:=\mathcal S\times\{0,1,\dots ,D\}\).
* **Transitions**

$$
\tilde P\bigl((s',d-1)\mid(s,d),a\bigr)=
    \begin{cases}
      P(s'|s,a), & d>0,\\
      0, & d=0.
    \end{cases}
$$

* **Rewards** \(\tilde r((s,d),a)=r(s,a)\) (independent of the clock).
* **Discount** \(0<\gamma<1\) (same before and after the deadline).
* **Boundary** All value functions satisfy \(V(s,0)=0\).

---

## 1 Policy iteration algorithm (tabular form)

```text
Input : any deterministic policy π0 : 𝒮×{0..D} → 𝒜
Repeat   i = 0,1,2,…
  1. POLICY‑EVALUATION
     Solve   Vπi = Tπi Vπi
         where (Tπ V)(s,d) =
               r(s,π(s,d)) + γ Σs' P(s'|s,π(s,d)) V(s',d-1)
               and V(s,0)=0
  2. POLICY‑IMPROVEMENT
     For every (s,d>0) set
        a* = argmaxa [ r(s,a) + γ Σs' P(s'|s,a) Vπi(s',d-1) ]
        πi+1(s,d) ← a*
Until   πi+1 = πi  (no changes)  →  output π*
```

### 1.1 Why evaluation is **easy**

Because the right‑hand side for layer \(d\) depends only on layer \(d-1\),
policy evaluation does **not** require matrix inversion:

```
for d = 1 … D
    for all s
        Vπ(s,d) ← r(s,π(s,d))
                   + γ Σs' P(s'|s,π(s,d)) Vπ(s',d-1)
```

This backward pass costs \(O(D·|𝒮|·|𝒜|)\).

---

## 2 Correctness proofs

### 2.1 Policy‑evaluation equation

For fixed \(\pi\),

$$
V_\pi(s,d)=
\begin{cases}
r(s,\pi(s,d))+\gamma\sum_{s'}P(s'|s,\pi(s,d))V_\pi(s',d-1), & d>0,\\[6pt]
0,& d=0 .
\end{cases}\tag{1}
$$

*The unique solution exists because the system is triangular in \(d\).*

### 2.2 Policy‑improvement theorem (countdown version)

Define the **advantage**

$$
A_\pi(s,d,a)=
r(s,a)+\gamma\sum_{s'}P(s'|s,a)V_\pi(s',d-1)\;-\;V_\pi(s,d).\tag{2}
$$

Let \(\pi'\) coincide with \(\pi\) everywhere except maybe at \((s,d)\), where it chooses

$$
\pi'(s,d)=\arg\!\max_{a}A_\pi(s,d,a).\tag{3}
$$

Then

$$
V_{\pi'}(s,d)\;\ge\;V_\pi(s,d)\quad\forall (s,d),\tag{4}
$$

with strict \(>\) if any \(A_\pi(s,d,a)>0\) at a changed slice.

*Proof.*
Write the Bellman equations for both policies; subtract; use (2) and monotone induction over \(d\).

### 2.3 Monotone improvement & termination

Because the state space \(\widetilde{\mathcal S}\) is **finite**,

* the sequence \(\{V_{\pi_i}\}\) is monotonically non‑decreasing,
* it is bounded above by \(V^{\!*}\) (optimal value from value iteration),
* and each improvement step that changes at least one slice raises some state’s value strictly.

There are only

$$
N_{\text{pol}}=|𝒜|^{\,|𝒮|\,(D+1)}
$$

deterministic policies, so PI must stop in **≤ \(N_{\text{pol}}-1\)** iterations with a policy \(\pi^*\) that no longer improves—hence is optimal.

---

## 3 Occupancy‑measure geometry (edge‑pivot view)

### 3.1 Layered occupancy vector of a policy

$$
q^{\pi}_d(s,a)=\Pr_{\pi}[s_d=s,\,a_d=a],\qquad
d=0,\dots ,D-1.\tag{5}
$$

These satisfy linear **flow constraints**

$$
q_{d+1}^{\pi}(s')=\sum_{s,a}q_{d}^{\pi}(s,a)\,P(s'|s,a).\tag{6}
$$

The feasible set \( \mathcal Q_D\) is a polytope; every deterministic \(\pi\) corresponds to a **vertex**.

### 3.2 Objective hyper‑plane

$$
\langle r, q^{\pi}\rangle
=\sum_{d=0}^{D-1}\sum_{s,a} \gamma^{d}\,r(s,a)\,q^{\pi}_d(s,a).\tag{7}
$$

### 3.3 Policy iteration = simplex method

* **Policy‑evaluation:** compute the value of current vertex \(q_{\pi_i}\).
* **Policy‑improvement:** pick one slice \((s,d)\) with positive advantage; swapping the action moves along the **edge** that changes only that coordinate, landing at the adjacent vertex \(q_{\pi_{i+1}}\).
* By (4) the dot‑product (7) strictly increases, so PI is **edge‑walking** upwards until it reaches the top vertex \(q_{\pi^*}\).

Hence the algebraic PI algorithm and the geometric simplex pivot are identical descriptions.

---

## 4 Relationship to the **fundamental theorem of MDPs**

The countdown‑augmented process is still an ordinary finite, discounted MDP.
Puterman’s theorem therefore guarantees that

1. **some deterministic, stationary policy is optimal**—exactly what PI searches through;
2. **policy‑improvement cannot cycle** because every pivot raises value and there are finitely many vertices.

Thus PI’s convergence proof is nothing more than an explicit constructive use of the fundamental theorem combined with the linear‑program geometry of the occupancy polytope.

---

## 5 Key practical observations

| Feature                              | Effect in the surprise‑deadline setting                                                                             |    |                                                                   |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | -- | ----------------------------------------------------------------- |
| **Triangular linear system**         | Evaluation step is an \(O(D)\) backward sweep, cheaper than matrix inversion.                                         |    |                                                                   |
| **Number of improvable slices**      | At most (                                                                                                           | 𝒮 | ,(D+1)-1) iterations; each step can change *many* slices at once. |
| **Warm start from wandering policy** | Initialise \(\pi_0\) with the pre‑deadline greedy policy; early layers already near‑optimal, so PI terminates faster. |    |                                                                   |

---

### Final takeaway

> **Policy iteration in the countdown‑augmented MDP is just “simplex on the occupancy polytope.”**
> Each evaluation step assigns a price (value) to the current vertex; each improvement step moves along a single edge that raises that price.  Finiteness of the polytope and monotone value increase guarantee convergence to the deterministic, stationary policy promised by the fundamental theorem of MDPs.



























