---
_build:
  render: never
  list: never

date: "2025-07-12"
title: "(7) Briefly on Distributional RL"
summary: "(7) Briefly on Distributional RL"
lastmod: "2025-07-12"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


### 1  Core concepts

| Concept                                    | Essence                                                                                                                                                                                                                                                                     | Why it matters                                                                                                             |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Risk‑neutral control**                   | Formulated as maximising the expected discounted return \(J(\pi)=\mathbb E_\pi[\sum_{t\ge0}\gamma^{t}R_t]\).  Proposition 7.2 proves that an *optimal deterministic, stationary Markov policy* always exists, so the search can be restricted to simple mappings \(X\!\to\!A\). | Reduces the combinatorial policy space to a tractable subset and justifies classical dynamic‑programming methods.          |
| **Bellman optimality operator** \(T\)        | Maps a state–action value function \(Q\) to \(TQ(x,a)=\mathbb E[R+\gamma\max_{a'}Q(X',a')]\). Lemma 7.3 shows \(T\) is a \(\gamma\)-contraction in \(\lVert\cdot\rVert_\infty\).                                                                                                      | Guarantees geometric convergence of *value iteration* and underpins **Q‑learning**.                                        |
| **Distributional control perspective**     | Extends value prediction from scalars to *return distributions* \(\eta(x,a)\).  A *greedy selection rule* \(G\) yields a family of **distributional Bellman optimality operators** \(T^G\).                                                                                       | Allows agents to reason about risk and higher‑order uncertainty, not just means.                                           |
| **Action gap \(\mathrm{gap}(Q,x)\)**         | Difference between the best and second‑best \(Q\)-values in a state.  When a unique optimal policy exists (\(\mathrm{gap}(Q^\*)>0\)), distributional value iteration provably converges (Theorem 7.9).                                                                          | Quantifies how robust a greedy policy is to approximation errors and drives several algorithmic tweaks.                    |
| **Risk measures & risk‑sensitive control** | General objective \(J_\rho(\pi)=\rho(\sum_t\gamma^{t}R_t)\) with coherent measures such as Variance, Entropic risk, VaR, CVaR (Def 7.14, Exs 7.16‑7.18).                                                                                                                      | Brings modern RL closer to safety‑critical or financial applications where variance or tail losses dominate expectations.  |

---

### 2  Key arguments developed by the authors

1. **Stationary Markov sufficiency** – Even though history‑dependent or stochastic policies are admissible, they do *not* increase optimal return in the risk‑neutral case; thus algorithm design can focus on deterministic stationary policies.&#x20;

2. **Convergence of classical vs. distributional methods** – While \(T\) is a contraction, the analogous distributional operator \(T^G\) is *not* (Proposition 7.7). Therefore extra care (action‑gap arguments, mean‑preserving projections) is needed to obtain convergence guarantees.&#x20;

3. **Necessity of refined greedy rules** – With multiple optimal actions the sequence \(\{\eta_k\}\) can cycle (Example 7.11, *diagram on page 210*), hence the choice of \(G\) materially affects learning dynamics.&#x20;

4. **Risk alters optimal‑policy structure** – Under variance constraints the optimal policy may need randomisation, memory of the trajectory, or explicit time dependence (Examples 7.19–7.21, *Figure 7.5*). This contrasts sharply with the risk‑neutral case and highlights *time‑inconsistency* of some risk criteria.&#x20;

5. **Computational hardness** – Optimising mean–variance objectives is NP‑hard; exact dynamic programming is infeasible, motivating approximate or gradient methods.&#x20;

---

### 3  Practical frameworks & algorithms

| Framework                                                         | Main idea                                                                                                                                                       | Deployment guidance                                                                                              |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Value iteration / Q‑learning**                                  | Iterate \(Q_{k+1}=TQ_k\) or stochastic updates \(Q\leftarrow Q+\alpha\big[r+\gamma\max_{a'}Q(x',a')-Q(x,a)\big]\).                                                  | Baseline for discrete spaces; becomes unstable under function approximation without safeguards.                  |
| **Distributional value iteration** \(\eta_{k+1}=\Pi_F T^{G}\eta_k\) | Combine greedy rule \(G\) with an *expectation‑preserving projection* \(\Pi_F\) (e.g., Categorical or Quantile) to propagate full distributions.                    | Use when risk or uncertainty modelling is required; ensure projection preserves means to keep value‑consistency. |
| **Categorical Q‑learning**                                        | Sample‑based counterpart using fixed support \(\{z_i\}\) and KL‑like projection; converges when a unique optimal policy exists.                                   | Default in many deep‑RL libraries (e.g., C51); balance support size with memory/compute.                         |
| **CVaR‑optimising dynamic programme** (Sec 7.8)                   | Augment state with running shortfall \(B_t\); iterate distributional operator that minimises expected \([B-G]^+\). Theorem 7.22 gives finite‑iteration error bound. | Suitable for risk‑averse planning; needs either function approximation over \(B\) or discretisation.               |
| **Policy‑gradient risk optimisation** (implied)                   | Because many risk measures break Bellman monotonicity, gradient or occupancy‑measure methods are pragmatic alternatives.                                        | Use when analytic dynamic programming is intractable; expect convergence only to local optima.                   |

---

### 4  Notable insights, examples & visuals

* The *left panel of Figure 7.3* (p. 210) shows a one‑state MDP where distributional learning oscillates forever, vividly illustrating non‑convergence without an action gap.
* *Figure 7.5* (p. 216) presents three toy MDPs proving that variance‑constrained optimal policies can be (a) stochastic, (b) history‑dependent, or (c) non‑stationary—dispelling the intuition that Markov‑deterministic suffices once risk is introduced.
* The *zig‑zag curves in Figure 7.6* (p. 217) quantify how a cleverly chosen stopping‑time policy outperforms any stationary policy under tight variance budgets, underscoring time‑inconsistency.
* Proposition 7.7’s counter‑example shows even “nice” probability metrics (e.g., Wasserstein‑1) cannot rescue contraction of \(T^{G}\); this shifts focus from *metric* tricks to *gap* and *uniqueness* properties.

---

### 5  Synthesis & value for further study

*Chapter 7* provides the bridge from **distributional prediction (Chs 4‑6)** to **distributional control**, clarifying which classical guarantees carry over and where fundamentally new behaviour arises.

* It crystallises **three tiers of complexity**:

  1. **Expectation‑based control** – well understood, contraction tools work.
  2. **Distributional‑expectation control** – expectation preserved; need gap/unique‑optimal‑policy arguments.
  3. **General risk‑sensitive control** – Bellman monotonicity breaks; must augment state, relax optimality notions, or accept hardness.

* Practitioners gain:

  * A checklist for algorithm design—ensure mean‑preserving projection, identify action gap, verify uniqueness.
  * Awareness that **risk criteria dictate policy class**; ignoring this can silently doom convergence.
  * A concrete template (augmented‑state CVaR iteration) to operationalise downside‑risk objectives—portable to other coherent measures.

* For researchers, the chapter highlights open questions: designing *continuous*, *stable* greedy rules when multiple optimal actions exist; scalable approximations for dynamic risk measures; and unifying distributional RL with policy‑gradient methods under risk.

Together, these foundations empower anyone building RL systems to **move beyond average‑return optimisation toward principled, risk‑aware decision‑making**, while understanding the mathematical caveats that accompany this leap.&#x20;
