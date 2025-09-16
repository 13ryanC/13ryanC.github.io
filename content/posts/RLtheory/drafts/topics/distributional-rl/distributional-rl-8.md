---
date: "2025-07-12"
title: "(8) Briefly on Distributional RL"
summary: "(8) Briefly on Distributional RL"
lastmod: "2025-07-12"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


**Chapter 8 “Statistical Functionals” – Comprehensive Breakdown**

---

### 1  Core Concepts

| Concept                                               | Formal Definition                                                                                                                                     | Why it Matters                                                                                                                                        |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Statistical functional**                            | A mapping  $\phi:P(\mathbb R)\!\to\!\mathbb R$ that assigns a real value to an entire probability distribution $\nu$.                                 | Lets us focus on *properties* (mean, variance, quantile, expectile, etc.) instead of the full distribution.                                           |
| **Sketch**                                            | A *vector* of $m$ statistical functionals $\Phi=(\phi_1,\dots,\phi_m)$.                                                                               | Provides a compact, task‑driven “summary” (e.g., first $m$ moments, selected quantiles).                                                              |
| **Bellman‑closed sketch**                             | A sketch for which there exists an operator $T^\pi_\Phi$ s.t. $\Phi(T^\pi \eta)=T^\pi_\Phi(\Phi(\eta))$.                                              | Guarantees *exact* dynamic programming on the sketch without needing the full distribution. Figure 8.1 on p. 240 visualises the commutative diagram.  |
| **Moment Bellman operator** $T^{\pi}_{(m)}$           | Recursion that updates the first $m$ (uncentred) moments of the return distribution (Def. 8.6).                                                       | Extends classical Bellman equations to higher‑order information (variance, skew…).                                                                    |
| **Statistical Functional Dynamic Programming (SFDP)** | Iterate  $s_{k+1}=\Phi\!\bigl(T^\pi\,\overset{\large\triangleright}{\eta}\!(s_k)\bigr)$ where $\triangleright$ is an *imputation* map $s\mapsto\eta$. | General recipe for *approximate* DP when the sketch is **not** Bellman‑closed. Algorithm 8.1 spells out the workflow.                                 |
| **Imputation strategy**                               | Any map $\triangleright: \text{Image}(\Phi)\!\to\!P(\mathbb R)$ that reconstructs a plausible distribution from functional values.                    | Bridges the gap between functionals and distributions; can be *exact* or *approximate*.                                                               |

---

### 2  Key Arguments of the Chapter

1. **Why focus on functionals?**
   Estimating specific distributional properties can be *simpler and more accurate* than approximating the entire return distribution. For example, variance can be computed to machine precision via a linear system, while categorical/quantile schemes typically mis‑estimate it.&#x20;

2. **Bellman‑closed sketches enable error‑free DP**
   If a sketch is Bellman‑closed (moments are the canonical example), plain value‑iteration–style updates converge exactly to the true functional values (Prop. 8.9).&#x20;

3. **Most interesting sketches are *not* Bellman‑closed**
   Quantiles, medians, and “at‑least” indicators fail Bellman‑closedness; vivid counter‑examples (Figure 8.2 on p. 242) show that median at a parent state cannot be deduced from child‑state medians.&#x20;

4. **SFDP provides a principled workaround**
   By pairing any sketch with an imputation routine, one recovers an *approximate* projected Bellman operator equivalent to Distributional Dynamic Programming with a custom projection.&#x20;

5. **Moment sketches are *essentially unique* among expectation‑type functionals**
   Theorem 8.12 proves that any Bellman‑closed sketch expressible as expectations of deterministic functions $f_i(Z)$ must contain exactly the information of a finite set of moments—no richer.&#x20;

---

### 3  Practical Frameworks & Algorithms

| Framework                                     | How it works                                                                                                                                    | Practical Use‑cases                                                                                                     |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **m‑Moment Dynamic Programming**              | Iterate $M_{k+1}=T^{\pi}_{(m)} M_k$; provably convergent for any start $M_0$ (Prop. 8.7).                                                       | Low‑variance estimation of mean, variance, skewness for policy evaluation or risk‑sensitive control.                    |
| **Moment TD‑Learning** (Eq. 8.16)             | Unbiased stochastic update using single‑step samples; retains near‑contractive behaviour by inductively exploiting lower‑order moment accuracy. | Online agents that learn mean & variance simultaneously without double sampling.                                        |
| **Statistical Functional DP (Algorithm 8.1)** | Loop: *impute* distribution from current stats → apply $T^\pi$ → extract new stats.                                                             | Enables DP with quantiles, expectiles, CVaR, custom risk measures.                                                      |
| **Expectile Dynamic Programming (EDP)**       | Treat expectiles as the sketch; impute via root‑finding/optimisation (Eq. 8.14–8.15) over an $n$-quantile representation.                       | Smooth alternative to quantiles; useful for coherent risk measures and variance‑sensitive policies.                     |
| **Projection‑via‑Imputation = DDP**           | Any (sketch, imputer) pair defines a *projection* $\Pi_F$ that is *diffusion‑free* when the sketch is Bellman‑closed (Prop. 8.17).              | The design freedom of $\Phi$ and $\triangleright$ becomes a toolkit for constructing new distributional RL algorithms.  |

---

### 4  Notable Insights, Examples & Diagrams

* **Figure 8.1 (p. 240)** – *Commutative diagram* vividly shows that Bellman closedness lets us “commute” sketch extraction and Bellman updates, eliminating approximation error.
* **Figure 8.2 (p. 242)** – Two crafted MDPs demonstrate that identical child‑state medians can yield different parent medians, proving median functional is *not* Bellman‑closed.
* **Expectile intuition** – Expectiles generalise the mean via an *asymmetric squared‑loss* (Eq. 8.13). $\tau>0.5$ yields “optimistic” summaries, $\tau<0.5$ “pessimistic”—offering a continuum of risk sensitivity.&#x20;
* **Uniqueness of moment sketches** – The proof (Remark 8.2) cleverly uses closure under translation & scaling to invoke Engert’s theorem, showing only polynomials survive—hence moments are the sole expectation‑based Bellman‑closed set.&#x20;
* **Centered vs. uncentered moments** – Direct variance Bellman equation (Eq. 8.17) needs dual samples; learning uncentered moments then algebraically centering is sample‑efficient, underlining a subtle algorithmic design trade‑off.&#x20;

---

### 5  Synthesis & Broader Significance

1. **Bridges Value‑Function RL and Distributional RL**
   Chapter 8 reframes distributional RL as *functional RL*: instead of chasing full distributions or mere expectations, we can target *just‑right* summaries aligned with control objectives or risk preferences.

2. **Provides a Unifying Lens for Existing Methods**
   Classical TD (*mean*), C51 (*categorical*), QR‑DQN (*quantiles*), and new methods like EDP all fit into the (Sketch, Imputation) template, clarifying their similarities and differences.

3. **Sets Foundations for Risk‑Aware Algorithms**
   By formalising expectiles, CVaR and other risk measures as statistical functionals with dynamic‑programming recipes, the chapter lays mathematical groundwork for principled risk‑sensitive policy optimisation.

4. **Highlights Fundamental Limits**
   The uniqueness theorem flags that no finite expectation‑based sketch surpasses moments in being Bellman‑closed; hence, *approximation is inevitable* for most exotic objectives, motivating research on better imputations and error analysis.

5. **Catalyst for Future Work**
   Upcoming chapters (especially Ch. 10) build on these ideas to handle *infinite* families (e.g., full CDFs, characteristic functions), leading toward representation‑free or kernel‑based distributional RL. Chapter 8 supplies the conceptual scaffolding needed to appreciate those advances.

---

**Take‑away for Practitioners**

* Use **moment DP/TD** when you need accurate means & variances cheaply.
* Deploy **SFDP** with a custom sketch when your performance metric (e.g., quantile at 95 %) is *not* moment‑based; pick an imputation that is computationally tractable and respects critical invariants (e.g., mean‑preserving).
* Expectiles offer a *smooth, coherent* alternative to quantiles—consider them when you need differentiable risk measures.
* Always test whether your sketch is Bellman‑closed; if not, plan for approximation and monitor induced bias.
