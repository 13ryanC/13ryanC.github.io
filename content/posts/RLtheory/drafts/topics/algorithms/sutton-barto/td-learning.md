---
_build:
  render: never
  list: never

date: "2025-07-14"
title: "Temporal Difference Methods"
summary: "Temporal Difference Methods"
lastmod: "2025-07-14"
category: "Notes"
series: ["RL Theory", "RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


### Overview

Chapter 6 of *Reinforcement Learning: An Introduction* (“Temporal‑Difference Learning”) introduces TD learning—the idea most closely associated with modern reinforcement learning—and develops it from first principles through fully fledged control algorithms. The chapter’s 22 pages combine intuitive examples, formal proofs, algorithmic blue‑boxes, backup diagrams, figures, and historical notes.&#x20;

---

## 1. Core Concepts

| Concept                                 | Essence                                                                                                                                                                                                                   | Where it is established                                   |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Temporal‑Difference (TD) Learning**   | Learning predictions by *bootstrapping*—updating estimates partly from other learned estimates rather than waiting for final outcomes; unifies ideas from Monte‑Carlo (sampling) and Dynamic Programming (bootstrapping). | §6.1, esp. eqs. 6.2 & 6.4 and the backup diagram on p. 3. |
| **TD Error (δₜ)**                       | The one‑step prediction error δₜ = Rₜ₊₁ + γ V(Sₜ₊₁) – V(Sₜ); drives all TD updates and appears throughout RL theory.                                                                                                      | Eq. 6.5, p. 3.                                            |
| **Bootstrapping vs. Sampling Spectrum** | TD combines Monte‑Carlo’s use of raw experience with DP’s bootstrapping, providing a continuum later bridged by *n‑step* and *λ‑return* methods.                                                                          | Intro, Figure 6.1, discussion on pp. 1‑4.                 |
| **On‑policy vs. Off‑policy Learning**   | Distinguishes methods that evaluate/update the behaviour policy itself (e.g., Sarsa) from those that evaluate a different, typically greedy, target policy while behaving exploratorily (e.g., Q‑learning).               | §6.4–6.6.                                                 |
| **Maximisation Bias & Double Learning** | Using `max` over noisy estimates produces optimistic bias; maintaining two independent value functions and decoupling action‑selection from evaluation (Double Q‑learning) mitigates it.                                  | §6.7, Figure 6.5.                                         |
| **Afterstates**                         | States *after* the agent’s deterministic action but before stochastic environment response—useful when immediate action effects are known (e.g., board games, queuing).                                                   | §6.8.                                                     |

---

## 2. Key Arguments Developed by the Authors

1. **TD methods are *sound* and *efficient*.**
   *They converge to the correct value function like DP and Monte‑Carlo but require neither a model nor complete episodes, and learn online with low computation.* Empirical speed‑ups are shown in the random‑walk study (Figure 6.2) and analytically explained through certainty‑equivalence optimality under batch updates.&#x20;

2. **Bootstrapping earlier is advantageous in long or continuing tasks.**
   The “Driving Home” narrative (Figure 6.1) illustrates that waiting until the end of an episode wastes learning opportunities, whereas TD updates refine estimates immediately—critical for non‑terminating tasks or very long episodes.&#x20;

3. **TD control requires explicit handling of exploration; on‑policy and off‑policy have distinct trade‑offs.**
   Sarsa integrates action‑selection stochasticity into its targets, yielding safer behaviour under exploration (Cliff‑Walking example). Q‑learning, while converging to the optimal *value* faster, can behave poorly online due to mismatch between behaviour and target policy. Expected Sarsa offers a variance‑reduced middle ground.&#x20;

4. **Maximisation bias can materially degrade policies; double learning is a simple, principled fix.**
   The two‑network trick eliminates the positive bias without additional per‑step cost—important in noisy domains.&#x20;

---

## 3. Practical Frameworks & Methodologies

| Algorithm / Framework                                | Purpose & Highlights                                                                                                               | Real‑world Use Cases                                                                             |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Tabular TD(0)** (Box, p. 2)                        | One‑step policy evaluation; online, incremental; no model.                                                                         | Predicting customer lifetime value while data streams in.                                        |
| **Sarsa (on‑policy TD control)** (Box, p. 12)        | Learns *Q* for current behaviour policy and improves it via ε‑greedy; convergent if every state‑action is visited.                 | Robotics with continual exploration; safe navigation (Windy Gridworld).                          |
| **Q‑learning (off‑policy)** (Box, p. 13)             | Directly approximates optimal Q\*, independent of behaviour; supports arbitrary exploration strategies.                            | Industrial process control where exploration must respect safety constraints handled externally. |
| **Expected Sarsa** (§6.6)                            | Replaces sampled next‑action with expectation under policy—lower variance, more stable with large α.                               | Finance or recommendation systems where variance reduction is critical.                          |
| **Double Q‑learning / Double Expected Sarsa** (§6.7) | Two decoupled estimators remove maximisation bias.                                                                                 | High‑noise environments such as ad‑click optimisation.                                           |
| **Batch TD vs. Batch MC Analysis** (§6.3)            | Shows TD converges to certainty‑equivalence estimates—insight for offline RL with fixed logs.                                      | Fitting value functions from historical medical records without online interaction.              |
| **Afterstate Formulation** (§6.8)                    | Learn value of post‑action states, collapsing symmetric action representations; faster learning in deterministic‑transition games. | Chess/open‑loop games; inventory queuing where assignment action is fully known.                 |

---

## 4. Notable Insights, Examples & Case Studies

| Example (page)                                 | What it Demonstrates                                                                                    | Practitioner Take‑away                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Driving‑Home Prediction** (Fig 6.1, pp. 4‑5) | TD updates exploit partial journey information; Monte‑Carlo waits for destination.                      | Use TD when feedback arrives gradually (e.g., web‑session length prediction). |
| **Random Walk** (Fig 6.2, pp. 7‑8)             | Empirical learning‑speed comparison—TD beats constant‑α MC given same data.                             | Expect TD to out‑perform MC on stochastic sequential problems.                |
| **Windy Gridworld** (Example 6.5, p. 12)       | Sarsa adapts to stochastic wind and learns near‑optimal trajectories online.                            | TD control algorithms handle environment noise gracefully.                    |
| **Cliff‑Walking** (Example 6.6, p. 14)         | Sarsa’s caution vs. Q‑learning’s risk under ε‑greedy exploration; Expected Sarsa combines best of both. | Align learning objective with online safety requirements.                     |
| **Maximisation‑Bias MDP** (Fig 6.5, pp. 16‑17) | Q‑learning over‑selects sub‑optimal action; Double Q‑learning corrects it.                              | In noisy reward settings, incorporate double estimators to avoid optimism.    |
| **Backup Diagrams** (Fig 6.4, p. 15)           | Visual grammar for understanding how information flows in each algorithm.                               | Use diagrams for debugging custom TD variants.                                |

---

## 5. Synthesis Value & Connection to Broader Themes

* **Conceptual bridge** – TD sits between Monte‑Carlo and Dynamic Programming, providing a continuum later generalised by *n‑step* and *λ‑return* algorithms (Chapter 7 & 12), and by model‑based planning (Chapter 8). Understanding TD is prerequisite for eligibility traces, actor–critic methods, and deep RL.
* **Foundational algorithmic motifs** – TD error, bootstrapping, on‑ vs off‑policy duality, and maximisation bias recur in modern methods such as DQN, A3C, and AlphaZero.
* **Statistical learning perspective** – The certainty‑equivalence result links TD to maximum‑likelihood estimation; double learning echoes ensemble methods for variance/bias control.
* **Practical orientation** – By emphasising online, incremental computation with minimal memory, the chapter grounds RL in realistic deployment constraints—streaming data, partial episodes, safety‑critical exploration.&#x20;

---

## 6. Practitioner’s Quick‑Reference Checklist

| Question to ask                                   | Relevant TD tool                                  |
| ------------------------------------------------- | ------------------------------------------------- |
| Need value predictions before episodes terminate? | TD(0)                                             |
| Must improve a policy while behaving safely?      | Sarsa or Expected Sarsa with ε‑greedy/soft policy |
| Exploration policy differs from target policy?    | Q‑learning or Expected Sarsa (off‑policy)         |
| High reward noise causes over‑optimism?           | Double Q‑learning / Double Expected Sarsa         |
| Deterministic immediate action effects known?     | Afterstate value function                         |

---

**Bottom line:** Chapter 6 equips you with the theoretical rationale and working algorithms to learn from *ongoing* experience without a model, striking a balance between sample efficiency and computational simplicity. Mastery of TD learning is indispensable for any practitioner or researcher aiming to apply reinforcement learning to real‑world sequential decision problems.&#x20;



























































































