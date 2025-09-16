---
date: "2025-07-14"
title: "Monte-Carlo Methods"
summary: "Monte-Carlo Methods"
lastmod: "2025-07-14"
category: "Notes"
series: ["RL Theory", "RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


**Chapter 5 – *Monte Carlo Methods* (Sutton & Barto)** provides the first full treatment of learning *directly from experience* in reinforcement‑learning (RL) settings. It contrasts sharply with the Dynamic Programming (DP) material of Chapter 4 by eliminating the need for a complete model of the environment and by *not* bootstrapping. Below is a structured breakdown that distils the conceptual foundations and practical guidance most useful to practitioners and researchers.&#x20;

---

### 1. Core Concepts

| Concept                                            | Essence                                                                                                                                                                                                                      | Why it matters                                                                                                                                |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Monte Carlo (MC) estimation**                    | Learn value functions by **averaging complete returns** obtained from sampled episodes. Requires only sequences of *(state, action, reward)* and *episode termination*.                                                      | Enables learning when transition probabilities are unknown or intractable.                                                                    |
| **Episodic tasks & returns**                       | MC methods are defined for tasks that terminate; updates occur *after* an episode.                                                                                                                                           | Guarantees well‑defined finite returns and simplifies theory.                                                                                 |
| **First‑visit vs. Every‑visit MC**                 | Whether statistics are updated using the *first* encounter of a state in an episode or *all* encounters. Both converge, but with slightly different variance properties.                                                     | Provides a choice between easier theory (first‑visit) and easier extension to function approximation (every‑visit).                           |
| **Action‑value focus**                             | MC methods often estimate $q_\pi(s,a)$ because, without a model, one cannot look ahead from $v_\pi(s)$ alone.                                                                                                                | Makes policy improvement feasible through greedy or ε‑greedy selection.                                                                       |
| **Exploring Starts & ε‑soft policies**             | Mechanisms to ensure every state–action pair is sampled infinitely often—either by randomising initial state–action pairs or by keeping the behaviour policy stochastic (ε‑greedy/ε‑soft).                                   | Addresses the exploration–exploitation dilemma without explicit optimism or upper‑confidence bounds.                                          |
| **Generalised Policy Iteration (GPI) via MC**      | Alternate MC‑based evaluation with policy improvement to converge toward optimality (e.g., *Monte Carlo ES* algorithm).                                                                                                      | Extends the classic DP idea to model‑free settings.                                                                                           |
| **Off‑policy learning & Importance Sampling (IS)** | Learn about *target* policy π while following a different *behaviour* policy b by weighting returns with likelihood ratios. Ordinary IS is unbiased but high‑variance; weighted IS trades a small bias for finite variance.  | Decouples data collection from the policy being optimised (crucial for safety constraints, legacy data, or differing exploration strategies). |
| **Variance‑reduction extensions**                  | *Discounting‑aware* and *per‑decision* IS truncate or distribute ratios to cut variance, esp. when γ ≪ 1 or episodes are long.                                                                                               | Modern research direction that stabilises off‑policy MC.                                                                                      |

---

### 2. Key Arguments & Authorial Positions

1. **MC vs. DP Trade‑off** – The chapter argues MC methods are often *simpler and more viable* than DP because they bypass the need to tabulate or manipulate transition probability matrices. The blackjack discussion (pp. 92 – 96) shows that simulating games is trivial while computing analytic transition probabilities is “complex and error‑prone.”&#x20;

2. **Independence of Estimates** – Because MC does not bootstrap, each state’s estimate is statistically independent of others. This independence makes MC attractive when only *a subset* of states matters (soap‑bubble example, p. 95).&#x20;

3. **Exploration is the Central Practical Issue** – Deterministic policies starve many state–action pairs of data; hence methods such as exploring starts or ε‑greedy improvement are mandatory for convergence.

4. **Variance Limits the Power of Naïve Off‑policy IS** – The “Infinite Variance” counter‑example (pp. 106 – 108) demonstrates that ordinary IS can fail catastrophically. This motivates weighted IS and discount‑aware refinements.&#x20;

5. **GPI Framework is Universal** – Regardless of whether learning is on‑policy or off‑policy, the alternation of (approximate) evaluation and improvement steps moves both value estimates and policies toward optimality.

---

### 3. Practical Frameworks & Algorithms

| Algorithm / Framework                    | Purpose                                                                                                                            | High‑level Workflow                                                                                                                                                                  |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **First‑Visit MC Prediction**            | Estimate $V_\pi$.                                                                                                                  | After each episode, back‑up return G to the first visit of each state. (Pseudo‑code page 93.)                                                                                        |
| **Every‑Visit MC Prediction**            | Alternate estimator with easier incremental update.                                                                                | Same as above but update on *all* visits.                                                                                                                                            |
| **Monte Carlo ES (Exploring Starts)**    | *On‑policy* control without function approximation.                                                                                | 1) Randomly pick initial (s,a); 2) Generate episode using current policy; 3) Update $Q(s,a)$ by averaging returns; 4) Make policy greedy w\.r.t. Q. (Page 99.)                       |
| **On‑policy ε‑Greedy MC Control**        | Remove exploring‑starts assumption.                                                                                                | Maintain ε‑soft policy; after each episode update Q then make policy ε‑greedy w\.r.t. new Q. (Algorithm page 101.)                                                                   |
| **Off‑policy Weighted‑IS MC Prediction** | Evaluate π while following b.                                                                                                      | Track cumulative IS weights C(s,a); update Q incrementally with ratio‑weighted returns. (Algorithm page 110.)                                                                        |
| **Off‑policy Weighted‑IS MC Control**    | Learn optimal deterministic π\* while exploring with any ε‑soft b.                                                                 | Same as above but after each episode: (i) update Q via weighted IS, (ii) set π(s) ← argmax\_a Q(s,a), (iii) discard step contributions once a non‑greedy action appears. (Page 111.) |
| **Incremental Mean Updates**             | Replace return lists by running averages to reduce memory, using the “sample‑average update” trick from Chapter 2. (Exercise 5.4). |                                                                                                                                                                                      |

---

### 4. Notable Insights, Examples & Illustrations

* **Blackjack Benchmark (Figures pp. 94 & 100)** – Shows MC can converge to near‑perfect play (\~500 k simulated hands). Surfaces illustrate value differences between “usable‑ace” and “no‑ace” subspaces, highlighting state‑representation issues.

* **Soap‑Bubble Dirichlet Problem (p. 95, image)** – Positions MC as a general solver for Laplace‑type equations: random walks starting at a point yield its boundary‑value solution, illustrating MC’s utility beyond RL.

* **Infinite‑Variance Trap (Figure 5.4)** – A single‑state MDP where ordinary IS fails despite unbiasedness, underscoring the *practical* necessity of variance‑controlled estimators.

* **Racetrack Control Exercise (pp. 111 – 112, map images)** – Demonstrates application of ε‑greedy MC control in a continuous‑episode task with stochastic slip, exemplifying how to encode and solve a safety‑critical control problem with sparse rewards.

These examples serve both as didactic tools and as canonical testbeds for algorithmic benchmarking.&#x20;

---

### 5. Synthesis Value & Broader Connections

1. **Bridge between DP and TD** – Chapter 5 completes the spectrum: DP (model‑based & bootstrapping) → MC (model‑free, no bootstrapping) → **Temporal‑Difference (TD)** methods in Chapter 6 that combine both strengths. Understanding MC prepares readers to appreciate TD’s bias‑variance trade‑off and eligibility traces.

2. **Foundation for Policy‑Gradient & Actor‑Critic** – Many modern policy‑gradient algorithms rely on MC returns (or variants like Generalised Advantage Estimation) for *unbiased* gradient targets. The chapter grounds why full‑trajectory returns are usable and when high variance demands baselines or bootstrapping.

3. **Exploration Principles** – ε‑soft and exploring‑start ideas foreshadow advanced exploration schemes (e.g., entropy regularisation, optimism in the face of uncertainty).

4. **Off‑policy Evaluation (OPE)** – Weighted IS formulæ laid out here are the theoretical backbone for contemporary OPE in recommender systems and causal inference, where logged data must be re‑weighted to predict performance of new strategies.

5. **Sample‑efficiency vs. Simplicity** – By contrasting MC’s independence property with DP’s efficiency, the chapter clarifies how algorithm choice depends on *data availability*, *model fidelity*, and *computational budget*.

---

### Key Take‑aways for Practitioners

* **When to use MC**: episodic tasks, easy simulators, or limited interest in a subset of states.
* **Always manage variance**: prefer weighted IS; consider discount‑aware or per‑decision techniques when γ < 1 or episodes are long.
* **Guarantee coverage**: adopt ε‑soft behaviour policies or engineered exploring starts.
* **Leverage incremental updates** to avoid memory blow‑ups and enable online learning.
* **Treat MC control as a baseline**: it is conceptually clean, easy to implement, and a useful benchmark before moving to TD or function‑approximation regimes.

---

*Chapter 5 thus equips the reader with the first practical, model‑free toolkit for value estimation and optimal control, while surfacing the statistical challenges that motivate the TD and function‑approximation methods developed later in the book.*


























































































