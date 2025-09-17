---
date: "2025-07-12"
title: "(9) Briefly on Distributional RL"
summary: "(9) Briefly on Distributional RL"
lastmod: "2025-07-12"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


### Core Concepts

| Concept                                      | Brief Explanation                                                                                                                                                                                           | Where Introduced                       |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **Function approximation in RL**             | Replaces state‑indexed tables with parametric functions so learning scales to huge or continuous state spaces.                                                                                              | pp. 261‑262, opening section           |
| **State aliasing**                           | When two or more distinct states share parameters, updates performed on one state inevitably change the estimate for the others, potentially propagating error.                                             | Figure 9.1 & Example 9.1, pp. 262‑264  |
| **Linear value‑function approximation**      | The value is expressed as an inner product \(V_w(x)=\phi(x)^{\top}w\).  Linearity in **parameters** gives closed‑form updates and tractable analysis.                                                         | Definition 9.2, p. 264                 |
| **Projected Bellman operator**               | Because \(T_\pi V\) usually falls outside the linear space, it is orthogonally projected back with respect to a weighted \(L^2\) norm \(\|·\|_{\xi,2}\).                                                          | §9.3, pp. 266‑268                      |
| **Contraction under steady‑state weighting** | If the projection weight \(\xi\) is chosen as the policy’s steady‑state distribution \(\xi_\pi\), the composed operator \(\Pi_{\phi,\xi_\pi}T_\pi\) is a \(\gamma\)-contraction, guaranteeing a unique fixed point. | Theorem 9.8, pp. 268‑270               |
| **Semi‑gradient TD learning**                | Updates \(w\leftarrow w+\alpha\delta_t\phi(x_t)\) with TD‑error \(\delta_t=r+\gamma\phi(x_{t+1})^\top w-\phi(x_t)^\top w\).  Cheaper than full gradient but can diverge.                                        | §9.4, eq. (9.11), p. 271               |
| **Baird’s counter‑example**                  | A two‑state MDP where semi‑gradient TD diverges for many update distributions, illustrating the sensitivity to off‑policy sampling.  Growth is visualised in Figure 9.2b.                                   | Example 9.9, pp. 272‑274 & Figure 9.2  |
| **Linear distributional methods (QTD, CTD)** | Extends linear approximation to quantile‑based and categorical return distributions; retains linearity in parameters, not in outputs.                                                                       | §9.5, pp. 274‑277                      |
| **Signed‑distribution approximation**        | Drops the probability constraint, allowing negative mass so linear structure is preserved; leads to a doubly‑projected Bellman operator that is \(½\)-contractive.                                            | §9.6‑§9.7, pp. 278‑284 & Theorem 9.13  |

---

### Key Arguments & How They Are Supported

1. **Linearity is the simplest, analyzable way to generalise in large MDPs**

   * The chapter motivates with Go and Mountain‑Car, domains where tabular value storage is impossible (pp. 261‑262).  Analytic properties (closed‑form least squares, gradient expression) follow directly from Definition 9.2.&#x20;

2. **Projection has to respect the sampling distribution or learning diverges**

   * Proof of Theorem 9.8 shows contraction only under \(\xi_\pi\).  Example 9.9 demonstrates empirical divergence when \(\xi\neq\xi_\pi\); swapping to the steady‑state weights stabilises learning (dashed vs dotted curves in Figure 9.2b).&#x20;

3. **Semi‑gradient TD is *not* true gradient descent and can mis‑align with the projected fixed point**

   * Equation (9.12) decomposes TD into a stochastic gradient step toward \(\Pi T_\pi V\); but feedback created by using \(w\) both in prediction and target yields instability.  Baird’s counter‑example formalises this.&#x20;

4. **Distributional RL can be married with linear approximation, but extra care is needed**

   * For quantiles, gradient of the pinball loss (eq. 9.16) yields bounded errors that differ qualitatively from TD.  For categorical models, soft‑max parameters introduce convexity but break linearity, motivating the signed‑mass relaxation (eq. 9.22).&#x20;

5. **Signed‑mass relaxation restores linear geometry and preserves contractivity**

   * Lemmas 9.14‑9.16 decompose the doubly‑projected operator into a \(½\)-contraction; Proposition 9.18 then bounds the compounded approximation error.  Figure 9.3 shows practical behaviour in the Cliff domain, including negative mass aliasing.&#x20;

---

### Practical Frameworks & Methodologies

| Framework                                                | How to Apply                                                                                                                                                 | Typical Use‑case                                                                                    |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| **Least‑Squares Linear Value Approximation** (Prop. 9.3) | Solve \(w^*=(\Phi^\top\Xi\Phi)^{-1}\Phi^\top\Xi V_\pi\) once trajectories allow full‑return estimates.                                                         | Batch policy evaluation when replay or simulator access is available.                               |
| **Projected Dynamic Programming**                        | Iterate \(V_{k+1}=\Pi_{\phi,\xi}T_\pi V_k\) or its sample‑based analogue (mini‑batch least squares each iteration).                                            | Fitted value or Q‑iteration in large discrete tasks.                                                |
| **Semi‑gradient TD(0)**                                  | Online update (eq. 9.11) with small step‑size, *but* only safe if sampling on‑policy or representation satisfies stability conditions (Exercise 9.10 hints). | Real‑time learning on embedded systems or games.                                                    |
| **Linear QTD / CTD**                                     | Maintain *m* weight vectors, update with eqs. (9.16) or (9.19) respectively; allows distributional predictions with linear costs.                            | Risk‑sensitive control where quantiles or full return densities matter.                             |
| **Signed‑categorical Algorithm**                         | Represent masses \(p_i(x)=\phi(x)^\top w_i + (1/m)(1-\sum_j\phi(x)^\top w_j)\); update with eq. (9.24).  Guarantees \(½\)-contraction.                           | Research or safety settings where theoretical guarantees on distributional estimates are essential. |

---

### Notable Insights, Examples & Diagrams

* **Aliasing Danger** – *Figure 9.1 (p. 262)* shows a four‑state MDP where sharing a single parameter for states \(y,z\) forces an inevitable trade‑off; bootstrapping further contaminates even the “clean” states \(x_1,x_2\).&#x20;
* **Empirical Divergence** – *Figure 9.2b (p. 273)* presents 100 TD runs; log‑error lines fan out exponentially, visually emphasising instability. Switching the visitation frequencies collapses error, confirming the theoretical weight of \(\xi_\pi\).&#x20;
* **Negative Mass as a Tool not a Bug** – *Figure 9.3c‑d (p. 285)* displays histograms where some bins dip below the axis; these “signed” corrections allow the approximation to balance errors across aliased states when features are scarce.&#x20;

---

### Synthesis & Broader Significance

1. **Bridge from Tabular to Continuous RL.**
   The chapter formalises how to *move beyond lookup tables* while retaining convergence guarantees.  The linear‑projected framework becomes the template for modern *fitted value iteration*, LSTD, LSPI, and, by analogy, deep‑RL techniques that replace \(\phi\) by neural embeddings.&#x20;

2. **Cautionary Lessons for Deep RL.**
   Instabilities attributed to function‑approximation/bootstrapping interplay (the “deadly triad”) were historically observed with neural networks; Baird’s counter‑example offers a minimal, reproducible stress‑test.  The signed‑distribution analysis similarly foreshadows challenges when producing calibrated uncertainty estimates with deep nets.&#x20;

3. **Unified View of Expected and Distributional Learning.**
   By showing that the *same* projection‑contraction logic extends from scalar values to full return distributions (albeit with a \(½\) modulus), the chapter provides conceptual glue between classical RL theory and the burgeoning distributional literature.  This underpins risk‑aware algorithms, quantile regression approaches, and variance‑aware exploration.&#x20;

4. **Design Rules for Practitioners.**

   * Use on‑policy data or a *compatible* feature basis (Exercise 9.11) if relying on semi‑gradient TD.
   * Prefer batch least‑squares or double‑fixed‑point methods (e.g., GTD) when collecting data off‑policy.
   * If predicting distributions, consider signed‑mass or softmax‑probability parameterisations; both achieve tractability, the former offering stronger theory, the latter cleaner probabilistic semantics.

Collectively, the material provides the mathematical and algorithmic toolkit required to **scale reinforcement learning from toy tabs to real‑world, high‑dimensional problems** while illuminating the pitfalls and remedies that emerge when approximation, sampling, and bootstrapping interact.

---



Below is a “what’s‑actually‑new” checklist that pinpoints the genuine additions this chapter brings to a *distributional* RL treatment.  Everything is referenced to the chapter pages so you can verify each claim quickly.

---

## 1. Extending Distributional RL *beyond* Tabular Domains

| Novel element                                                                                                                        | Why it matters                                                                                                                                                                                                    | Where it appears                           |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Linear QTD & CTD updates** – first explicit derivation of semi‑gradient *quantile* and *categorical* TD rules with shared features | Lets you train *distribution* predictors in Atari‑scale or continuous spaces exactly as you would linear TD for values.  Prior distributional work stopped at tabular or deep models with no intermediate theory. | eqs. (9.16) & (9.19), pp. 274‑277          |
| **Bounded error signals for QTD/CTD**                                                                                                | Shows that, unlike scalar TD whose TD‑error is unbounded, each update step lies in \[−1, 1].  This foreshadows their empirical stability and justifies larger stepsizes.                                          | p. 277, discussion after eq. (9.19)        |
| **Signed‑distribution approximation**                                                                                                | Introduces a *third* representation (not quantile, not soft‑max categorical) in which negative mass is allowed so linearity is preserved.  This is brand‑new to the literature.                                   | Definition 9.10 & eq. (9.22), pp. 278‑280  |
| **Doubly‑projected Bellman operator** \( ⇧<sub>ϕ,ξ,ℓ²</sub> ⇧<sub>c</sub> T \)                                                         | Shows how to keep BOTH the categorical grid *and* the shared‑parameter constraint in one contraction mapping – something not previously available for distributions.                                              | pp. 280‑281                                |

---

## 2. New Theoretical Guarantees

| Result                                                                         | What is new                                                                                                                                               | Where               |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| **Theorem 9.13** – ½‑contraction of the doubly‑projected operator              | The first *distributional* analogue of the classical Tsitsiklis‑Van Roy projection theorem.  Guarantees convergence even with aliasing and negative mass. | p. 282              |
| **Proposition 9.18** – finite‑error bound combining *two* approximation layers | Quantifies how much error accumulates when you compress *both* over states **and** over return support; no such bound existed before.                     | p. 284              |
| **Pythagorean lemma for signed distributions**                                 | Generalises the Cramér‑projection geometry (used only for probabilities up to now) to signed measures, enabling clean orthogonality decompositions.       | Lemma 9.17, p. 283  |

---

## 3. Fresh Insights on Stability & Aliasing

* **Aliasing‑driven divergence explained visually** – Figure 9.2 couples Baird’s minimal counter‑example with feature sharing, explicitly showing how *distribution* mismatch in the update distribution drives blow‑ups (log‑error fans out).&#x20;
* **Why negative mass is helpful** – Figure 9.3 reveals that permitting signed mass lets the optimiser “borrow” probability to cancel unavoidable errors, something impossible in the probability‑only schemes.&#x20;
* **Error‑bounded semi‑gradient story** – Equation (9.12) decomposes TD as an *approximate* step toward the projected Bellman target, clarifying exactly where feedback loops can destabilise distributional learning.&#x20;

---

## 4. Bridging Theory to Practice

1. **Road‑map to Deep‑RL** – The linear QTD/CTD formulas (and their bounded errors) are the templates used verbatim inside *IQN*, *QR‑DQN*, *C51* etc.  Up to now these deep agents had no small‑scale theoretical counterpart.
2. **Design heuristics justified** – The chapter formally explains why practitioners sample on‑policy (steady‑state) when mixing bootstrap + approximation: it is the only weight choice that preserves contraction (Theorem 9.8).&#x20;
3. **Complexity analysis** – Update (9.24) shows the signed algorithm runs in \(O(m^2+mn)\), giving the first clear cost bound for distributional learning with shared features.&#x20;

---

### Bottom line

Earlier chapters taught *what* distributional RL is; Chapter 9 is the first to tell you **how to scale it** and **what can (and cannot) be proved** once you leave the comfort of tabular grids.
*If you ever want distributional guarantees for function approximation, you need the operator, the ½‑contraction proof, and the signed trick – none existed before this chapter.*
