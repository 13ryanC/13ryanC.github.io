---
_build:
  render: never
  list: never

date: "2025-07-14"
title: "Eligibility Traces"
summary: "Eligibility Traces"
lastmod: "2025-07-14"
category: "Notes"
series: ["RL Theory", "RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### 1. Core Concepts

| Concept                                     | Essence                                                                                                                                                                                              | Why it matters                                                                                                      |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Eligibility trace (`z`)**                 | A short‑term memory vector, updated every time step, that records how strongly each parameter has “participated” in recent predictions. It decays at rate `λγ`                                       | Enables credit assignment to many past states/actions with one TD error, greatly accelerating learning.             |
| **λ‑return**                                | A *compound* target that geometrically averages all *n‑step* returns with weights `(1‑λ)λ^{n‑1}` (Fig 12.1‑12.2). Monte‑Carlo ↔ TD are the two end‑points (`λ=1` and `λ=0`).                         | Provides a smooth knob to trade bias vs variance and to unify TD & MC theory.                                       |
| **Forward vs. backward view**               | *Forward* view defines the ideal update target that depends on future rewards; *backward* view implements the same effect online using the current TD error and eligibility traces (Fig 12.4‑12.5).  | Gives both conceptual clarity (forward) and computational practicality (backward).                                  |
| **TD(λ) family**                            | Extends 1‑step TD with eligibility traces; includes *true‑online TD(λ)*, *Sarsa(λ)*, *Tree‑Backup(λ)* and off‑policy variants (GTD(λ), GQ(λ), HTD(λ), Emphatic TD(λ)).                               | Supplies deployable algorithms for prediction and control with tabular, linear or nonlinear function approximation. |
| **Dutch / replacing / accumulating traces** | Three trace update rules; *dutch* (Eq 12.11) yields an exact implementation of the online λ‑return for linear FA (“true‑online” methods).                                                            | Choice of trace affects stability, bias and ease of derivation; dutch traces dominate for linear models.            |
| **Truncated λ‑return & re‑doing updates**   | Limits the forward horizon to *n* steps (TTD(λ)) or successively *recomputes* all past updates each time new data arrive (online λ‑return).                                                          | Offers tuneable time–computation trade‑offs and motivates true‑online TD.                                           |
| **Variable γ and λ**                        | Allows state/action‑dependent discounting and bootstrapping; leads to generalized return (Eq 12.17‑12.22).                                                                                           | Unifies episodic, continuing‑discounted, options and pseudo‑termination in one framework.                           |
| **Off‑policy control‑variated traces**      | Combine per‑decision importance sampling with eligibility traces to obtain stable off‑policy learning (Eq 12.24‑12.30).                                                                              | Makes eligibility‑based TD viable when behaviour ≠ target policy.                                                   |

---

### 2. Key Arguments Developed in the Chapter

1. **Eligibility traces unify and generalize TD & Monte‑Carlo**
   *The λ spectrum* shows intermediates often outperform both extremes on tasks such as the 19‑state random walk (Fig 12.3, 12.6).&#x20;

2. **Backward‑view algorithms can match forward‑view ideals with far less memory**
   True‑online TD(λ) reproduces the full online λ‑return sequence exactly while retaining **O(d)** complexity.&#x20;

3. **Intermediate λ gives best empirical performance**
   Four diverse benchmarks (Mountain‑Car, Random‑Walk, Puddle‑World, Cart‑Pole) all exhibit U‑shaped curves with minima around λ≈0.4–0.9 (Fig 12.14).&#x20;

4. **Trace choice matters**
   Dutch traces dominate replacing/accumulating in both theory (exactness) and practice (Fig 12.8, 12.11).&#x20;

5. **Off‑policy TD needs both expectation correction *and* distribution correction**
   Algorithms such as GTD(λ) or Emphatic‑TD(λ) satisfy these two requirements and guarantee stability with linear function approximation.&#x20;

---

### 3. Practical Frameworks & Methodologies

| Framework                                             | Where defined                                                              | When to use                                                                            | Implementation highlights                                                   |
| ----------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **TD(λ)** (Alg. box p. 292‑293)                       | On‑policy value prediction                                                 | Any tabular/linear FA task where data arrive online                                    | Update: `w ← w + α δ z`; trace: `z ← γλ z + ∇v̂`.                           |
| **True‑online TD(λ)** (box p. 300)                    | On‑policy value prediction with *exact* λ‑return                           | Preferred for linear FA; avoids bias from trace approximation                          | Dutch trace (Eq 12.11); extra term `(α (δ + V – Vold) z – α (V – Vold) x)`. |
| **Sarsa(λ) & True‑online Sarsa(λ)** (box p. 305‑307)  | On‑policy control                                                          | Combine ε‑greedy exploration with traces; excellent on Mountain‑Car (Fig 12.10‑12.11). |                                                                             |
| **Truncated TD(λ)** / **TTD(λ)** (Fig 12.7)           | Limited memory or real‑time constraints                                    | Maintain buffer of last *n* feature vectors; learning delay n‑steps.                   |                                                                             |
| **Watkins’s Q(λ)** (Fig 12.12)                        | Off‑policy Q‑learning with traces, but cuts trace on first non‑greedy step | Simple to code; convergent tabularly, yet loses credit after exploration action.       |                                                                             |
| **Tree‑Backup(λ)** (Fig 12.13)                        | Off‑policy control **without importance sampling**                         | Uses target‑policy probabilities to down‑weight branches; more stable.                 |                                                                             |
| **GTD(λ), GQ(λ), HTD(λ), Emphatic‑TD(λ)** (Sec 12.11) | Stable linear off‑policy learning                                          | Require secondary weights `v` & possibly emphatic/F matrices; proven convergent.       |                                                                             |

*Implementation tip*: In tabular cases, store only traces whose value `|z(i)|` > ε to keep runtime near the 1‑step cost, because most traces decay quickly.&#x20;

---

### 4. Notable Insights, Examples & Visual Evidence

* **Weighting diagram (Fig 12.2, p. 290)** — visually clarifies how λ controls exponential decay; useful when teaching practitioners to choose λ.
* **Random‑walk curves (Fig 12.3 & 12.6, p. 291‑295)** — show TD(λ) ≈ λ‑return at small α but diverges at large α, justifying true‑online methods.
* **Grid‑world credit‑assignment illustration (Example 12.1, p. 304)** — contrasts one‑step, n‑step and λ‑trace backups; powerful teaching aid.
* **Mountain‑Car performance (Fig 12.10‑12.11, p. 306)** — replacing traces with λ≈0.9 halve the steps‑to‑goal versus n‑step Sarsa.
* **Performance summary (Fig 12.14, p. 318)** — synthesises four tasks, reinforcing “intermediate λ best” rule‑of‑thumb.
* **Forward‑Back‑triangle (p. 299)** — underpins derivation of true‑online TD; demonstrates clever algebraic trick of keeping only diagonal weights.

These empirical studies cement the theoretical claim that eligibility traces bring large **sample‑efficiency gains** without untenable computation.

---

### 5. Synthesis & Foundational Value

*Eligibility traces* are now visible as the **bridge** connecting seemingly disparate strands of RL theory:

* **Monte‑Carlo ↔ TD unification** – λ offers a continuum, letting practitioners tune variance/bias to dataset size and reward delay.
* **Online, incremental learning** – Backward‑view algorithms deliver MC‑quality targets on each step, critical for real‑time control and continual learning agents.
* **Off‑policy viability** – Combining traces with control‑variates and emphatic weighting resolves the “deadly triad”, anchoring modern algorithms such as IMPALA or R2D3.
* **Generalised returns** – State‑dependent γ and λ integrate discounting, episodic resets, options and temporally‑abstract predictions under one roof, simplifying architecture design.

For **applied work**, the chapter provides ready‑to‑use pseudocode, hyper‑parameter heuristics (choose λ in mid‑range; scale α by feature dimension), and implementation tricks (sparse trace storage). For **research**, it highlights open questions on automatic λ selection, non‑linear true‑online extensions, and variance control in off‑policy traces.

---

### Take‑Away Practical Wisdom

1. **Start with true‑online TD(λ) or Sarsa(λ)** when using linear function approximation; pick λ≈0.7 and tune α.
2. **Use traces whenever reward delay >> episode length**; they usually pay for themselves in data efficiency.
3. **For off‑policy prediction**, default to GTD(λ) or Emphatic‑TD(λ); for off‑policy control without importance sampling, prefer Tree‑Backup(λ).
4. **Monitor trace sparsity** in tabular implementations; prune near‑zero entries for speed.
5. **Remember λ is not a free lunch**—λ → 1 increases variance sharply; avoid pure Monte‑Carlo unless variance is well‑controlled.

By mastering the frameworks in this chapter, a practitioner gains the conceptual and algorithmic toolkit required to build **fast‑learning, stable, and versatile RL agents** across prediction and control tasks, on‑policy and off‑policy, tabular or function‑approximation.&#x20;



























































































