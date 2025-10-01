---
_build:
  render: never
  list: never

date: "2025-07-13"
title: "(2) Briefly on Multi-Agent RL" 
summary: "(2) Briefly on Multi-Agent RL"
lastmod: "2025-07-13"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


### Core Concepts

1. **Reinforcement‑Learning (RL) problem definition** – The chapter begins by formalising an RL problem as the *combination* of (i) a decision‑process model (e.g., MDP, POMDP, multi‑armed bandit) and (ii) a learning objective (typically maximising expected discounted return). This pairing is visualised in *Figure 2.1 on page 20* and establishes a clear separation between *environment specification* and *performance criterion*.&#x20;

2. **Agent–environment interaction loop** – *Figure 2.2 on page 21* depicts the single‑agent loop: observe state → choose action → environment transitions and emits reward → repeat. This loop grounds all subsequent algorithmic discussion.&#x20;

3. **Markov Decision Process (MDP)** – Definition 1 introduces the finite MDP (states S, actions A, transition kernel T, reward function R, initial distribution µ) and explains the Markov property (Equation 2.3). The *Mars‑Rover* diagram (*Figure 2.3 on page 23*) provides an illustrative worked example.&#x20;

4. **Learning objective: discounted return** – Sections 2.3–2.4 motivate discounted returns (Equation 2.6) for both terminating and continuing tasks, interpret γ both as (i) termination probability and (ii) time‑preference weighting, and introduce absorbing states to unify episodic and continuing settings.&#x20;

5. **Value functions and Bellman equations** – State‑value *V* and action‑value *Q* functions (Equations 2.10–2.20) yield the Bellman recursion, the Bellman *optimality* equations (Equations 2.24–2.25), and the greedy policy extraction rule (Equation 2.26). These equations form the analytical backbone for all RL algorithms discussed later.&#x20;

6. **Algorithmic families**

   * **Dynamic Programming (DP)** – Policy‑iteration and value‑iteration algorithms are derived, including convergence proofs via contraction mapping (Section 2.5, Algorithm 1).
   * **Temporal‑Difference (TD) learning** – On‑policy SARSA (Algorithm 2, Equation 2.53) and off‑policy Q‑learning (Algorithm 3, Equation 2.58) learn purely from sampled experience and bootstrapping, dispensing with the need for a known model.&#x20;

7. **Exploration–exploitation dilemma** – ε‑greedy policies (Equation 2.55) operationalise exploration while guaranteeing the “visit‑every‑state–action‑pair” requirement for convergence of TD methods.&#x20;

8. **Evaluation methodology** – Section 2.7 advocates *learning curves* plotted against cumulative interaction steps (not episodes) to fairly compare algorithms, and demonstrates this with the four‑panel plot set in *Figure 2.4 on page 37*.&#x20;

9. **Reward‑function equivalence** – Section 2.8 proves that the two common reward parameterisations, R(s,a,s′) and R(s,a), are equivalent by expectation transformation (Equation 2.63).&#x20;

### Key Arguments and Authorial Positions

| Theme                                                           | Author’s Position                                                                                                                    | Supporting Moves                                                       |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Need for RL**                                                 | RL uniquely tackles sequential decision problems where supervision is absent and dynamics are unknown.                               | Contrast with supervised/unsupervised learning (Section 2.1).          |
| **Model‑based vs model‑free**                                   | DP delivers exact solutions but is impractical without a model; TD generalises to real‑world settings by using sampled trajectories. | Side‑by‑side exposition of DP and TD, convergence guarantees for both. |
| **Discounting is part of the *problem*, not an algorithm knob** | The discount factor γ belongs to the *objective*; altering γ changes the optimal policy itself (Mars‑Rover γ=0.95 vs 0.5 example).   | Numerical comparison in Section 2.7.                                   |
| **Evaluation fairness**                                         | Reporting performance per episode can mislead; cumulative time‑steps is a more faithful measure of data efficiency.                  | Rationale in Section 2.7, illustrated by Figure 2.4.                   |

### Practical Frameworks & Methodologies

1. **Problem‑formulation checklist**

   1. Enumerate states, actions, terminal set.
   2. Specify reward signal and initial‑state distribution.
   3. Choose discount factor reflecting horizon/uncertainty preferences.
   4. Decide evaluation metric(s).

2. **Dynamic‑Programming workflow**
   *Iterative Policy Evaluation → Greedy Policy Improvement* (Equation 2.28 & 2.38) until policy stabilises; or Value‑Iteration single‑sweep update (Equation 2.47).

3. **TD‑Learning recipe**

   ```text
   observe (s,a,r,s′)
   δ ← r + γ·bootstrap − Q(s,a)
   Q(s,a) ← Q(s,a) + α·δ
   ```

   *Bootstrap* = Q(s′,a′) for SARSA; = maxa Q(s′,a) for Q‑learning. Include ε‑greedy exploration and learning‑rate schedule meeting ∑αk=∞, ∑αk²<∞.

4. **Performance‑analysis protocol** – Capture learning curves, undiscounted returns, episode length, and domain‑specific win metrics; always relate back to the defined objective.

These frameworks are generic and directly transplantable to industrial RL projects: e.g., robotics path planning (DP viable if physics model known), online recommendation (TD with ε‑greedy), or operations‑research simulations (value‑iteration under full model).&#x20;

### Notable Insights, Examples & Case Studies

* **Mars‑Rover MDP (Figure 2.3, page 23)** – A compact yet rich illustration of risk‑reward trade‑offs, stochastic transitions, and how γ shapes optimal path choice.
* **Contraction‑mapping proof sketch (Section 2.5)** – Offers theoretical intuition on why successive Bellman backups converge; valuable when justifying iterative solvers in safety‑critical deployments.
* **Learning‑rate & exploration sensitivity (sub‑plots c & d in Figure 2.4)** – Empirically demonstrates how hyper‑parameter schedules influence convergence speed—practical guidance for tuning.
* **Reward‑function equivalence (Section 2.8)** – Pragmatic tip: modellers can choose whichever parameterisation is simpler for data collection or simulator instrumentation without affecting policy quality.&#x20;

### Synthesis Value & Positioning within the Field

* **Foundation for Multi‑Agent RL (MARL)** – All later MARL chapters extend these single‑agent constructs to strategic settings; understanding Bellman ideas is prerequisite for grasping *value‑decomposition*, *equilibrium concepts*, and *opponent modelling* that follow.
* **Bridge to Function Approximation & Deep RL** – Chapter 2 deliberately defers approximation (Chs 7–8); however, the presented algorithms map one‑to‑one onto their deep counterparts (e.g., deep‑Q networks simply replace tabular Q with a neural approximator).
* **Conceptual Clarity Advantage** – By disentangling *environment* vs *objective*, the chapter arms practitioners with a diagnostic lens: when RL fails, is it modelling, objective design, learning dynamics, or exploration that is mis‑specified?
* **Reusable Algorithmic Paradigms** – The iterative‑evaluation/greedy‑improvement paradigm recurs in policy‑gradient, actor‑critic, and model‑based planning methods; recognising it early accelerates mastery of advanced literature.&#x20;

---

**Take‑away:** Chapter 2 offers a rigorous yet application‑oriented tour of single‑agent reinforcement learning, equipping readers with the theoretical lenses (MDP, value functions, Bellman equations) and the practical toolkits (DP, SARSA, Q‑learning, evaluation discipline) that underpin nearly every modern RL system.
