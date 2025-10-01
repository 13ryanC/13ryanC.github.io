---
_build:
  render: never
  list: never

date: "2025-07-19"
title: "Draft A. Foundations of Sequential Multi‑Agent Decision‑Making"
summary: "A. Foundations of Sequential Multi‑Agent Decision‑Making"
lastmod: "2025-07-19"
category: "Notes"
series: ["RL Topics", "MARL"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

## 4. What Level of Observability Should Agents Have?

> How much of the world should an intelligent agent be allowed (or required) to “see,” and how much of the agent should the rest of us be able to “see”?

This fundamental design question governs the interaction between an agent and its environment, as well as between the agent and its human overseers. The answer involves critical trade-offs between performance, computational cost, physical feasibility, and safety. The issue can be decomposed into two distinct, yet related, domains: the agent's observability of the world, and our observability of the agent.

---

### Perceptual Observability: The Agent's View of the World

An agent's ability to perceive its environment is a foundational choice in its design, formally captured by the mathematical frameworks used to model its decision-making process. This choice defines the trade-space for **perceptual observability**. The two primary models, Stochastic Games and Partially Observable Stochastic Games (POSGs), represent the poles of this spectrum.

* **Full Observability (Stochastic Games):** Choosing a **Stochastic Game (SG)**, also known as a Markov Game, as the underlying model implies that every agent has perfect and complete information about the state of the world.
    * **Formalism:** A multi-agent SG is defined as a tuple \(\langle S, \{A_i\}_{i=1..N}, T, \{R_i\}_{i=1..N} \rangle\), where:
        * \(S\) is the set of all possible world states.
        * \(A_i\) is the set of actions for agent \(i\).
        * \(T: S \times A \to \Delta(S)\) is the transition function, where \(P(s' | s, \vec{a})\) gives the probability of moving to state \(s'\) from state \(s\) after joint action \(\vec{a} = \langle a_1, ..., a_N \rangle\).
        * \(R_i: S \times A \to \mathbb{R}\) is the reward function for agent \(i\).
    * The crucial assumption is that the true state \(s \in S\) is directly provided to each agent. This satisfies the **Markov Property**, \(P(s_{t+1}|s_t, \vec{a}_t) = P(s_{t+1}|s_t, \vec{a}_t, ..., s_0, \vec{a}_0)\), meaning the current state contains all information needed for optimal decision-making. This simplifies an agent's **policy** \(\pi_i\), which becomes a direct mapping from states to actions, \(\pi_i: S \to A_i\). However, assuming full observability is often physically impossible or prohibitively expensive.

* **Partial Observability (POSGs):** Choosing a **Partially Observable Stochastic Game (POSG)** is a more realistic approach. Here, an agent receives only a private observation—a piece of probabilistic evidence about the state.
    * **Formalism:** A POSG extends the SG tuple with observation components: \(\langle S, \{A_i\}, T, \{R_i\}, \{\Omega_i\}, O \rangle\).
        * \(\Omega_i\) is the set of possible observations for agent \(i\).
        * \(O\) is the observation function, where \(P(\vec{o} | s', \vec{a})\) gives the probability of the agents receiving the joint observation \(\vec{o} = \langle o_1, ..., o_N \rangle\) after transitioning to state \(s'\).
    * This uncertainty forces the agent to perform **belief state tracking**. It maintains a **belief state** \(b_i\), a probability distribution over all possible world states (\(b_i \in \Delta(S)\)). After taking action \(a_i\) and receiving observation \(o_i'\), the agent updates its belief from \(b_i\) to \(b_i'\) using a Bayesian filter:
        $$
        b_i'(s') = \eta P(o_i' | s') \sum_{s \in S} P(s' | s) b_i(s)
        $$
        where \(\eta\) is a normalising constant. This continuous update is computationally expensive. The agent's policy must now map from this high-dimensional belief space to actions, \(\pi_i: \Delta(S) \to A_i\), which is a significantly harder problem to solve.

---

### Operational Observability: Our View of the Agent

The other side of this coin is **operational observability**—often referred to as transparency or, more broadly, **AI Observability**. This concerns our ability to inspect an agent's internal state and decision-making calculus. This includes its **policy** \(\pi_i\) (its strategy), its **value function** \(V^{\pi}_i\) (its prediction of future rewards), or its **belief state** \(b_i\).

* **Formalism:** An agent's goal is to learn a policy \(\pi_i\) that maximizes its **value function** \(V^{\pi}_i\), which is the expected sum of discounted future rewards:
    $$
    V_i^{\pi}(s_0) = \mathbb{E}_{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t R_i(s_t, \vec{a}_t) | s_0 \right]
    $$
    where \(\gamma \in [0, 1)\) is a discount factor that prioritizes sooner rewards. Transparency means having access to the parameters that define \(\pi_i\) and \(V_i^{\pi}\) to understand *how* the agent arrives at its decisions.

Greater transparency is a prerequisite for robust debugging, safety verification, and legal accountability. In high-stakes environments, the ability to audit an agent's decision logic is essential for trust and compliance, a central goal of **Explainable AI (XAI)**. However, maximizing transparency can expose proprietary logic and create overwhelming data management challenges.

Ultimately, the choice of observability level is determined by balancing the agent's computational complexity against the physical costs of sensing and the pressing need for external oversight.

| School of thought | Slogan | Rationale | Objections |
| :--- | :--- | :--- | :--- |
| **Max-information** | “See everything; log everything.” | Maximises agent performance by providing complete data. Enables comprehensive debugging, auditing, and post-hoc analysis. | Often physically impossible or financially prohibitive. Creates significant privacy risks, conflicting with regulations like GDPR. Generates massive, costly-to-manage datasets and increases the system's attack surface. |
| **Minimal-need** | “Only observe what you strictly need.” | Aligns with the principle of data minimization in privacy law. Reduces computational load and data storage costs. Constrains the agent's capabilities, which can reduce the attack surface for adversarial manipulation. | Makes debugging extremely difficult as root causes may be unobserved. Creates the risk of "unknown unknowns" or critical blind spots, where the agent is unaware of rare but crucial environmental factors, leading to catastrophic failure. |
| **Adaptive/elastic**| “Dial observability up or down on demand.” | Offers a dynamic balance between the above extremes. Low-cost, privacy-preserving operation is the default, but full-observability "flight recorder" mode can be triggered for debugging, anomaly detection, or periodic audits. | Adds significant architectural and computational complexity to the system. Defining robust triggers for changing observability levels is non-trivial. Creates potential for "observer effects" or gaming, where agents learn to alter their behavior when they detect they are under closer scrutiny. |
