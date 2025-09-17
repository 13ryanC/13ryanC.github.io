---
date: "2025-06-30"
title: "Value Identity"
summary: "Value Identity"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

Below is a self‑contained, rigorous discussion of what the identity

$$
v^{\pi'}-v^{\pi}
      =(I-\gamma P_{\pi'})^{-1}
        \bigl[r_{\pi'}-(I-\gamma P_{\pi'})v^{\pi}\bigr]
      =(I-\gamma P_{\pi'})^{-1}
        \bigl[T_{\pi'}v^{\pi}-v^{\pi}\bigr]
\tag{★}
$$

means, how it is derived, and **why it matters for planning algorithms in Markov Decision Processes (MDPs)**.

---

## 1. Formal context

| symbol                               | definition                                                                    | assumptions                        |         |               |
| ------------------------------------ | ----------------------------------------------------------------------------- | ---------------------------------- | ------- | ------------- |
| \((\mathcal S,\mathcal A,P,r,\gamma)\) | discounted, finite (or measurable) MDP                                        | \(0\le\gamma<1\)                     |         |               |
| \(\pi,\pi'\)                           | stationary deterministic or stochastic policies                               | —                                  |         |               |
| \(P_\pi\)                              | state–state transition matrix under \(\pi\): ((P\_\pi)\_{ss'}=\sum\_a \pi(a     | s)P(s'                             | s,a))   | rows sum to 1 |
| \(r_\pi\)                              | expected one‑step reward vector: ((r\_\pi)\_s=\sum\_a\pi(a                    | s)r(s,a))                          | bounded |               |
| \(v^\pi\)                              | value function (expected return) of \(\pi\): \(v^\pi=(I-\gamma P_\pi)^{-1}r_\pi\) | linear‑algebra form of Bellman eq. |         |               |
| \(T_\pi\)                              | Bellman operator: \(T_\pi v = r_\pi+\gamma P_\pi v\)                            | linear, contraction                |         |               |

---

## 2. Derivation of (★)

Start from the Bellman equations for the two policies:

$$
v^{\pi'} = T_{\pi'}v^{\pi'}=r_{\pi'}+\gamma P_{\pi'}v^{\pi'},\quad
v^{\pi} = T_{\pi}v^{\pi}=r_{\pi}+\gamma P_{\pi}v^{\pi}.
$$

Subtract the second from the first:

$$
v^{\pi'}-v^{\pi}=r_{\pi'}-r_\pi+\gamma P_{\pi'}v^{\pi'}-\gamma P_{\pi}v^{\pi}.
$$

Isolate \(v^{\pi'}-v^{\pi}\) on both sides, add and subtract \(\gamma P_{\pi'}v^{\pi}\):

$$
v^{\pi'}-v^{\pi}
   = r_{\pi'} - \gamma P_{\pi'}v^{\pi}
     \;+\;\gamma P_{\pi'}(v^{\pi'}-v^{\pi})
     \;+\;\gamma(P_{\pi'}-P_\pi)v^{\pi}.
$$

Collect the term with \(v^{\pi'}-v^{\pi}\):

$$
(I-\gamma P_{\pi'})\,(v^{\pi'}-v^{\pi})
   = r_{\pi'} - (I-\gamma P_{\pi'})v^{\pi}.
$$

Left‑multiply by \((I-\gamma P_{\pi'})^{-1}\) (which exists because \(0\le\gamma<1\) makes \(I-\gamma P_{\pi'}\) diagonally dominant for stochastic \(P_{\pi'}\)):

$$
v^{\pi'}-v^{\pi} = (I-\gamma P_{\pi'})^{-1}
                   \bigl[r_{\pi'}-(I-\gamma P_{\pi'})v^{\pi}\bigr].
$$

Recognising the bracketed term as \(T_{\pi'}v^{\pi}-v^{\pi}\) yields the final form (★).

---

## 3. Interpretations

### 3.1 *Fundamental‑matrix view*

\((I-\gamma P_{\pi'})^{-1}\) is the **resolvent** or *fundamental matrix* of the Markov chain under \(\pi'\).  Its \((s,s')\) entry equals the expected discounted number of times that policy \(\pi'\) visits \(s'\) when starting in \(s\).  Hence

$$
(v^{\pi'}-v^{\pi})(s)
   = \sum_{t=0}^\infty \gamma^t\,\Pr_{\pi'}[S_t=s'|S_0=s]\;
                         \bigl[T_{\pi'}v^{\pi}-v^{\pi}\bigr](s').
$$

**Take‑away:** **value improvement propagates along the future state‑distribution of \(\pi'\)**.

### 3.2 *Advantage view*

Because \(T_{\pi'}v^{\pi}-v^{\pi}\) equals the **state‑wise advantage** of switching from \(\pi\) to \(\pi'\) while still evaluating with \(v^{\pi}\), (★) is a vectorised form of the **performance‑difference lemma**:

$$
J(\pi')-J(\pi) = \frac{1}{1-\gamma}\,
                 \mathbb E_{s\sim d_{\pi'}}\bigl[ A_{\pi}(s,\pi'(s)) \bigr],
$$

where \(d_{\pi'}\) is the discounted future‑state distribution under \(\pi'\).
Thus (★) **quantifies how local Bellman errors translate into global return gains**.

### 3.3 *Linear fixed‑point view*

(★) reveals that *if* \(T_{\pi'}v^{\pi} \preceq v^{\pi}\) component‑wise, then \(v^{\pi'}\preceq v^{\pi}\).  This monotonicity statement underpins **policy improvement guarantees**.

---

## 4. Why (★) is central to *planning* algorithms

| Planning phase                              | Role of (★)                                                                                                                                                                                                                                    | Practical effect                                                                   |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Policy evaluation**                       | Gives a *residual‑correction* formula: if you already have \(v^{\pi}\) and consider a tentative policy \(\pi'\), you can estimate \(v^{\pi'}\) by adding the (discounted, propagated) Bellman residual instead of solving a brand‑new linear system. | Speeds up modified policy iteration (MPI) and *successor‑feature* approaches.      |
| **Policy improvement**                      | The sign of \([T_{\pi'}v^{\pi}-v^{\pi}]\) tells *where* \(\pi'\) is better; (★) tells *how much*.  Greedy or soft‑greedy improvement amounts to choosing \(\pi'\) that maximises this lift.                                                          | Justifies one‑step look‑ahead (value‑iteration) and advantage‑based exploration.   |
| **Safe or conservative planning**           | (★) admits upper/lower bounds if the residual is bounded or approximated; this enables *policy certificates* guaranteeing that deploying \(\pi'\) will not decrease return by more than \(\epsilon\).                                              | Underlies *safe policy iteration*, *Dyna‑style rollout*, and trust‑region methods. |
| **Off‑policy policy evaluation (OPE)**      | Setting \(\pi\) to a behaviour policy and \(\pi'\) to a target policy, (★) relates *known* \(v^{\pi}\) to *unknown* \(v^{\pi'}\) via quantities whose expectation can be estimated with importance sampling.                                           | Core to doubly‑robust/DR‑DICE and linear‑off‑policy LSTD(L).                       |
| **Sensitivity analysis & planning horizon** | Differentiating (★) w\.r.t.\ \(\gamma\) or model parameters yields how value changes with horizon length or transition probabilities.                                                                                                            | Useful in *robust MDPs* and model‑based design.                                    |

---

## 5. Algorithmic instantiations

1. **Modified Policy Iteration (MPI)**
   Uses the update
   \(\tilde v_{k+1}=v^{\pi_k}+M\bigl(T_{\pi_{k+1}}v^{\pi_k}-v^{\pi_k}\bigr),\)
   where \(M\) is a truncated version of \((I-\gamma P_{\pi_{k+1}})^{-1}\).  This is literally (★) with an approximation to the fundamental matrix, giving a tunable spectrum between value and policy iteration.

2. **Successor Features (SFs)**
   Decompose \(r_{\pi'}\) as feature weights; \((I-\gamma P_{\pi'})^{-1}\) becomes the *successor feature* matrix \(\Psi_{\pi'}\).  Equation (★) is then \(v^{\pi'}-v^{\pi}=\Psi_{\pi'}\bigl(\theta_{\pi'}-\theta_{\pi}\bigr)\).  Planning reduces to linear operations in feature space.

3. **Safe Policy Improvement with Baseline Bootstrapping (SPIBB)**
   Deviations from a baseline \(\pi\) are constrained so that \(\lVert(I-\gamma P_{\pi'})^{-1}(T_{\pi'}v^{\pi}-v^{\pi})\rVert_\infty\) is provably positive, ensuring no performance drop.

4. **Trust‑Region Policy Optimisation (TRPO) & PPO**
   Continuous‑control planners maximise \(\hat A_\pi\) while bounding KL divergence; the advantage estimator comes from (★) but with samples replacing exact expectations.

---

## 6. Practical tips & caveats

| Issue                                                                                                                                         | Mitigation informed by (★)                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Large/continuous state spaces:** directly inverting \(I-\gamma P_{\pi'}\) is infeasible.                                                      | Use Monte‑Carlo rollout to approximate \((I-\gamma P_{\pi'})^{-1}\), or represent it via successor features, or use linear‑solvers (LSTD, conjugate gradient). |
| **Function approximation bias:** if \(v^\pi\) is imperfect, the residual term may mislead improvement.                                          | Regularise with confidence intervals on \(T_{\pi'}v^{\pi}-v^{\pi}\); employ safe‑policy improvement criteria.                                                  |
| **Model uncertainty:** in model‑based planners, \(P_{\pi'}\) is estimated; then the propagated error can blow up in \((I-\gamma P_{\pi'})^{-1}\). | Robust MDP formulations replace the inverse with worst‑case resolvents, bounding planning risk.                                                              |

---

## 7. Summary significance

*Equation (★) is the *bridge* between local Bellman residuals and global value differences.*
It formalises **how a candidate policy’s one‑step advantage accumulates over its own future visitation distribution**, providing:

* a **quantitative policy‑improvement certificate**,
* a **computational shortcut** for incremental planning,
* the **theoretical foundation** for safe, robust, and off‑policy evaluation methods.

Because modern planners—be they tabular, linear‑function‑approximation, or deep‑RL—ultimately rely on estimating or bounding \(T_{\pi'}v^{\pi}-v^{\pi}\) and propagating it, (★) is not just algebraic ornamentation; it is **central to almost every algorithm that iteratively tweaks a policy toward optimality while controlling risk and computational cost**.
