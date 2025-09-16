---
date: "2025-07-14"
title: "n-step bootstrapping"
summary: "n-step boostrapping"
lastmod: "2025-07-14"
category: "Notes"
series: ["RL Theory", "RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


### Core Concepts

| Concept                                          | Essence                                                                                                                                                           | Why It Matters                                                                                                                |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **n‑step return *G<sub>t\:t+n</sub>***           | Discounted sum of the next *n* rewards plus the bootstrapped value *n* steps ahead. It smoothly interpolates between one‑step TD (n = 1) and Monte‑Carlo (n → ∞). | Lets practitioners tune the bias‑variance trade‑off and “escape the tyranny of the single time‑step.”                         |
| **Error‑reduction property**                     | The worst‑case error of the expected *n*-step return is ≤ γⁿ times the worst‑case error of the baseline estimate (Eq. 7.3).                                       | Guarantees that every *n*-step TD update moves predictions toward *v*<sup>π</sup>, providing theoretical safety.              |
| **On‑policy vs. off‑policy multi‑step learning** | On‑policy versions use raw returns; off‑policy versions weight them by an *n*-step importance‑sampling ratio (Eq. 7.10).                                          | Enables learning about a target policy while behaving more exploratively—crucial for modern RL where behaviour ≠ evaluation.  |
| **Sampling vs. expectation backups**             | Sarsa samples the next action, Tree‑backup fully averages over actions, and Expected‑Sarsa mixes the two.                                                         | Highlights a spectrum between low‑variance, high‑bias (expectation) and high‑variance, low‑bias (sampling) updates.           |
| **Unifying Q(σ)**                                | Uses a per‑step mixing parameter σ∈\[0,1] to decide whether each transition is sampled (σ=1) or expected (σ=0), generalising every preceding algorithm.           | Gives designers fine‑grained, state‑dependent control over variance and computational cost.                                   |

### Key Arguments the Chapter Advances

1. **Intermediate horizon often wins** – In the 19‑state random walk, the RMS error curve (Figure 7.2, p. 145) bottoms out for n≈4–8, beating both TD(0) and Monte‑Carlo extremes.&#x20;
2. **n‑step updates liberate policy cadence** – You can act every small Δt yet bootstrap over coarser, behaviourally meaningful intervals, avoiding a rigid compromise.&#x20;
3. **Off‑policy learning is feasible but variance‑sensitive** – Simple importance‑sampling works but explodes when behaviour ≠ target; Tree‑backup and control‑variates cut variance without bias.&#x20;
4. **Q(σ) offers a conceptual unification** – By letting σ vary, one obtains Sarsa, Expected‑Sarsa, Tree‑backup, or any hybrid, clarifying their relationships (Figure 7.5, p. 155).&#x20;

### Practical Frameworks & Algorithms

| Framework                               | Update Target                                                                             | Best‑use Scenarios                                                                      | Implementation Notes                                                                                 |                                                                           |
| --------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **n‑step TD (prediction)**              | *G<sub>t\:t+n</sub>* (Eq. 7.1)                                                            | State‑value estimation under a fixed policy.                                            | Maintain a circular buffer of length n+1 for (S, R) and update state S<sub>τ</sub> at time t = τ+n.  |                                                                           |
| **n‑step Sarsa (control)**              | Same idea applied to Q, bootstrapping from Q(S<sub>t+n</sub>, A<sub>t+n</sub>) (Eq. 7.4). | On‑policy control with faster propagation of reward (Grid‑world demo, Fig 7.4, p. 147). | Strengthens the last *n* actions of each episode rather than only the last one.                      |                                                                           |
| **Off‑policy n‑step Sarsa**             | Importance‑weighted *G<sub>t\:t+n</sub>* (Eq. 7.11).                                      | Learning a greedy policy while acting ε‑greedy.                                         | Multiply TD error by product of π⁄β ratios except the first action.                                  |                                                                           |
| **Per‑decision control‑variate method** | Recursively mixes importance sampling with a baseline V̄ (Eq. 7.13 & 7.14).               | Reduces variance when target & behaviour differ moderately.                             | Adds a zero‑mean term so expectation is unchanged but variance shrinks.                              |                                                                           |
| **n‑step Tree‑backup**                  | Expands every non‑sampled branch using π(a                                                | s) (Eq. 7.16).                                                                          | Off‑policy control without any importance sampling; ideal when action space is small/moderate.       | Computes a weighted tree of depth *n*; cost grows with branching factor.  |
| **n‑step Q(σ)**                         | Hybrid target in Eq. 7.17 with per‑step σ.                                                | Situations demanding dynamic variance control or computational budgeting.               | Setting σ via a heuristic (e.g., high near terminal states) is common in practice.                   |                                                                           |

### Notable Insights, Examples & Visual Evidence

* **Backup diagrams** – The chain‑to‑tree visuals (Figures 7.1 & 7.3, pp. 142, 146) vividly show how longer returns gather more real rewards before bootstrapping.&#x20;
* **Performance curves** – The U‑shaped error plots on page 145 quantify the bias/variance trade‑off and motivate tuning *n* per problem.&#x20;
* **Grid‑world path (Fig 7.4, p. 147)** – Demonstrates why multi‑step control learns **far** more from each episode: 10‑step Sarsa updates an entire action chain after a single reward.&#x20;
* **Tree‑backup illustration (p. 152)** – Shows how expected branches replace sampling, explaining its stability when behaviour ≠ target.&#x20;

### Synthesis & Field Significance

* **Bridge to Eligibility Traces (TD(λ))** – n‑step methods are the forward‑view of TD(λ); chapter 12 will collapse them into a single online algorithm with negligible memory. Understanding n‑step logic clarifies why λ‑returns work.&#x20;
* **Bias–Variance Dial** – By selecting *n* (and, in Q(σ), σ) practitioners can customise learning speed vs. stability—mirrored today in DQN’s multi‑step targets and actor‑critic rollouts.&#x20;
* **Foundational for Off‑policy Deep RL** – Importance‑sampled multi‑step returns underpin algorithms like Retrace, ACER and IMPALA; tree‑backup ideas appear in V‑trace. Mastery of this chapter equips you to read, implement, and improve those methods.&#x20;
* **Conceptual Clarity for Algorithm Design** – Seeing Sarsa, Expected‑Sarsa, Q‑learning, Tree‑backup, and Q(σ) as points on a common spectrum fosters principled innovation rather than ad‑hoc tweaks.&#x20;

---

**Take‑away for Practitioners**

1. **Pick *n* deliberately** – Start with *n*≈5 – 10 for episodic tasks; cross‑validate alongside step‑size.
2. **Mind the variance** – If behaviour diverges from target, prefer Tree‑backup or small σ in Q(σ); else plain n‑step Sarsa suffices.
3. **Use control variates** – When you must importance‑sample, subtract a baseline (V̄) to keep updates stable.
4. **Remember computational scaling** – Each extra step costs memory (buffer of length *n*+1) and CPU; eligibility traces later show how to amortise this.
5. **View multi‑step as a lens** – Diagnose slow propagation of reward or oscillatory TD targets by visualising the backup diagrams and adjusting *n*, σ, or branching strategy accordingly.

Mastering these ideas equips you to craft RL agents that learn faster, cope with off‑policy data, and balance stability against responsiveness—skills central to cutting‑edge reinforcement learning practice.



























































































