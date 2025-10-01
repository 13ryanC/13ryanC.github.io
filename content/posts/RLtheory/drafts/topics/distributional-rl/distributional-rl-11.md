---
_build:
  render: never
  list: never

date: "2025-07-12"
title: "(11) Briefly on Distributional RL"
summary: "(11) Briefly on Distributional RL"
lastmod: "2025-07-12"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


### Core Concepts

| Section                              | Fundamental Ideas & Formal Definitions                                                                                                                                                                                                                                                                                             | Why They Matter                                                                                                                          |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **11 .1 Multi‑agent RL**             | **Multi‑agent Markov Decision Process (MMDP).**  <br>Formalized as \((\mathcal X,\mathcal A,\xi_0,P_{\!X},P_{\!R})\) with a **factorised action space** \(\mathcal A=\prod_{i=1}^{N}\mathcal A_i\) for \(N\) agents (Definition 11.1). Each agent selects \(a_i\in\mathcal A_i\) given a joint state \(x\in\mathcal X\); rewards are shared. | Extends the single‑agent MDP to cooperative settings where agents must learn policies without assuming stationarity of the environment.  |
|                                      | **Distributional Reinforcement Learning (DistRL).**  Learns the full **return distribution** \(Z^\pi(x,a)\) rather than its expectation \(V^\pi(x,a)=\mathbb E[Z^\pi]\).  Risk‑sensitive actions can be chosen via distributional statistics such as an **expectile** \(\operatorname{Exp}_\tau(Z)\).                                    | Captures variability and supports optimism or caution through choice of statistic (e.g., high‑\(\tau\) expectiles).                        |
| **11 .2 Computational Neuroscience** | **Temporal‑Difference (TD) Error.** \(\delta=r+\gamma V(x')-V(x)\).  In dopamine theories, phasic firing ≈ \(\delta\).                                                                                                                                                                                                                 | Classic univariate model for dopaminergic Reward Prediction Errors (RPEs).                                                               |
|                                      | **Distributional TD Model of Dopamine.**  Each dopaminergic neuron \(i\) learns its own expectile \(\theta_i\) with asymmetric step sizes:  \(\theta_i \leftarrow \theta_i + \alpha\bigl[\!\mathbb 1_{r<\theta_i}-\tau_i\bigr](r-\theta_i).\)                                                                                            | Explains heterogeneous, asymmetric firing across neurons (Figures 11.3–11.4) better than scalar TD.                                      |

---

### Key Arguments & Supporting Evidence

| Claim                                                                                                         | Evidence & Reasoning                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Scalar Q‑learning breaks down in cooperative games because each agent faces a non‑stationary environment.** | In the *partially‑stochastic climbing* game (Figure 11.1, p. 321), independent Q‑learning agents converge to a sub‑optimal joint action because exploratory mis‑coordination yields large negative rewards.                                                                 |
| **Optimistic, risk‑seeking value estimates promote coordination.**                                            | *Hysteretic Q‑learning* (larger learning rate for positive TD errors) and a **distributional categorical TD method selecting actions by a high‑\(\tau\) expectile** both drive agents toward the globally optimal action pair in the same game (solid curves in Figure 11.1). |
| **Phasic dopamine activity reflects a *distribution* of future rewards, not a single expected value.**        | Single‑cell recordings in macaques and mice show diverse reversal points and asymmetric slopes (Figures 11.2–11.4) inconsistent with a shared scalar RPE but predicted by the distributional TD update above.                                                               |
| **Distributional RL unifies machine learning practice and biological data.**                                  | Likelihood‑Hysteretic IQN, distributional value‑factorisation, and the distributional TD dopamine model all arise by combining return‑distribution learning with risk sensitivity.                                                                                          |

---

### Practical Frameworks & Methodologies

| Framework / Algorithm                                       | Purpose & Mechanics                                                                                                                                                                               | Real‑World Applicability                                                                                                              |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Centralised vs. Decentralised MMDP Control**              | *Centralised* computes a joint policy offline. *Decentralised* requires each agent to learn from its own local transition \((x,a_i,r,x')\) with no inter‑agent communication.                       | Autonomous vehicles in traffic; drone swarms; multi‑robot warehouses.                                                                 |
| **Hysteretic Q‑learning (HQL)**                             | TD error \(\Delta\); update step size \(\alpha\) for \(\Delta\!>\!0\) and \(\beta\!<\!\alpha\) for \(\Delta\!<\!0\). Equivalent to descending the **expectile loss** at level \(\tau=\alpha/(\alpha+\beta)\). | Cheap optimistic modification usable with tabular or deep Q‑networks; improves cooperative convergence without explicit coordination. |
| **Distributional Categorical TD + Expectile‑Greedy Policy** | Maintain discrete support (e.g., {-30…30}); update with C51‑style projection; choose action with maximal expectile \(\operatorname{Exp}_\tau\). Decay \(\tau\) to anneal optimism.                    | Template for risk‑tunable agents in mixed‑motive games or safety‑critical planning.                                                   |
| **Distributional TD Model of Dopamine**                     | Each neuron represents a different expectile; population encodes a **sample of the return distribution**. Learning rule (Eq. 11.3) is local and biologically plausible.                           | Offers a quantitative bridge from RL to neural data; informs designs of neuromorphic or adaptive prosthetic controllers.              |

---

### Notable Insights & Illustrative Examples

1. **Risk‑sensitive coordination trade‑off.**
   The *stochastic climbing* matrix (page 321) demonstrates that too little optimism (risk‑neutral Q‑learning) under‑explores high‑value joint actions, while too much optimism might chase aleatoric noise. Tunable expectiles provide a *knob* to balance these forces.&#x20;

2. **Neural heterogeneity as distributional coding.**

   * *Figure 11.2* (page 326) shows cue‑shifted phasic bursts aligning with predicted TD errors.
   * *Figure 11.3* contrasts the *linear* error‑response predicted by scalar TD (panel a) with the *asymmetric, neuron‑specific* curves actually observed (panel b).
   * *Figure 11.4* reveals a strong correlation between each neuron’s reversal point and expectile asymmetry, validating the distributional hypothesis.

3. **Cross‑disciplinary resonance.**
   The same expectile mathematics underlies hysteretic updates in robots, optimism in deep RL (e.g., Likelihood‑Hysteretic IQN), and synaptic plasticity rules hypothesised for dopamine. A single framework thus informs **engineering algorithms** and **biological theory** alike.&#x20;

---

### Synthesis & Foundational Value

* **From expectation to distribution.**  The chapter drives home that predicting *only* the mean return is insufficient in complex, uncertain worlds—whether the uncertainty comes from other learners (multi‑agent) or from biological variability (neurons).
* **Risk as a unifying lens.**  Expectiles, asymmetric updates, and optimistic value functions form a common toolkit for negotiating risk, be it coordination risk among agents or reward‑uncertainty in the brain.
* **Bridging theory and practice.**  By connecting formal distributional RL algorithms to empirical neuroscience data, the chapter broadens the relevance of RL beyond AI, suggesting fertile ground for *neuro‑inspired algorithm design* and *AI‑inspired neuroscience*.
* **Launching pad for further study.**  Understanding this dual application equips practitioners to:

  * Design cooperative agents that self‑organise without central control.
  * Incorporate risk‑aware objectives in safety‑critical domains.
  * Investigate biological learning through the computational lens, guiding experiments and interpretive models.
    These threads anticipate ongoing research into distributional methods in finance, engineering control, and cognitive science, as outlined in the concluding remarks and bibliography.&#x20;

---

#### Progress

*Completed a first‑pass extraction and synthesis of conceptual foundations, algorithms, empirical insights, and cross‑domain connections for Chapter 11. Open issues for deeper exploration include (i) formal guarantees for distributional algorithms in non‑stationary multi‑agent settings, and (ii) experimental protocols to test whether distributional coding extends beyond dopamine to other neuromodulators.*
