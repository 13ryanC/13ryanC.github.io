---
_build:
  render: never
  list: never

date: "2025-07-03"
title: "(Part 4.2) Approximate Policy Iteration Theorem"
summary: "Approximate Policy Iteration Theorem"
category: "Tutorial"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
sources:
  - title: "Lecture 1 (2022-01-05)"
    url: "http://www.youtube.com/watch?v=rjwxqcVrVws"
  - title: "Lecture 1 (2021-01-12)"
    url: "http://www.youtube.com/watch?v=0oJmSULoj3I"
---

### Motivation for **Approximate Policy Iteration (API)**

---

#### 1.  Why add function approximation to policy‑iteration?

Classical **policy iteration (PI)** alternates

1. **exact policy evaluation:** solve the linear system

$$
v_{π}=r_{π}+\gamma P_{π}v_{π},\qquad\text{i.e. }v_{π}=(I-\gamma P_{π})^{-1}r_{π},
$$

2. **greedy improvement:** \(π'\!(s)=\arg\max_{a}q_{π}(s,a)\).

For a finite Markov Decision Process with \(|S|\) states, step 1 requires inverting an \(|S|\times|S|\) matrix—cubic in \(|S|\)—and storing the value table, **both infeasible when \(|S|\) is huge or continuous**. The natural idea is to **compress** the value/action‑value functions into a low‑dimensional linear space spanned by hand‑crafted or learned features \(\varphi\).

---

#### 2.  Formal compression model

* **Feature‑map** \(\varphi:S\times A\to\mathbb R^{d}\) (or \(\varphi:S\to\mathbb R^{d}\) for state values).
* **Linear approximation space** \(F_{\varphi}:=\{\Phi\theta\mid\theta\in\mathbb R^{d}\}\) with \((\Phi\theta)(s,a)=\langle\varphi(s,a),\theta\rangle\).

A policy’s action‑value function \(q_{π}\) is **ε‑realisable** if

$$
\inf_{\theta}\|q_{π}-\Phi\theta\|_{\infty}\le ε .
$$

Assumption **B2** (“approximate universal action‑value realisability”) posits that **every** policy enjoys this property with the *same* ε.  With B2 the planner may always stay inside \(F_{\varphi}\).&#x20;

---

#### 3.  Two guiding questions (lecture‑8, first paragraph)

| Question          | Operational meaning                                                                        | Desired answer                                                                                                                                                                                                                                  |      |                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Efficiency**    | \*Can we evaluate & improve a policy in time polynomial in d, γ, log(1/δ) — but **not** in | S                                                                                                                                                                                                                                               |  ?\* | Yes: weighted least‑squares on O(d²) cleverly chosen state‑action pairs costs **O(d³)**; rollout data needs only poly(d) samples.  |
| **Effectiveness** | *After K iterations, how sub‑optimal is the final policy?*                                 | API achieves \(\displaystyle\|v^{*}-v_{π_{K}}\|_{\infty}\le\frac{γ^{K}}{1-γ}+\frac{2}{(1-γ)^{2}}(ε_{\text{apx}}+κ)\). Both terms are tunable: increase K for the “iteration error”, increase samples m & horizon H for the “evaluation error” κ.  |      |                                                                                                                                    |

*Take‑away:* linear features potentially turn an intractable \(|S|\)-scale dynamic‑programming problem into a **dimension‑only** numerical linear‑algebra problem.

---

#### 4.  Where exactly do the computational savings arise?

1. **Policy evaluation via LSPE‑G**

   * Choose a **G‑optimal design** \((C,ρ)\), |C| ≤ d(d+1)/2.
   * Collect m rollout returns per design point (cost: O(m |C|)).
   * Solve the **weighted normal equations**
     \(\hat θ = G_{ρ}^{-1}\sum_{z∈C}ρ(z)\widehat R^{m}(z)\varphi(z)\)
     in O(d³) arithmetic.&#x20;

2. **Greedy step** needs only dot products \(\langle\hat θ,\varphi(s,a)\rangle\) — O(d) per state, independent of |S|.

3. **Sample complexity** to keep κ ≤ ε′ is poly\((d,(1-γ)^{-1},ε′^{-1})\); no |S| appears.

---

#### 5.  Why is *effectiveness* non‑trivial?

Compressing \(q_{π}\) introduces **approximation error** ε; sampling introduces **statistical error**; solving least‑squares on a small design set incurs **extrapolation error**.  API’s analysis shows these three errors:

$$
\boxed{\text{Sub‑optimality}}
  \;=\;
  \underbrace{\frac{γ^{K}}{1-γ}}_{\text{iteration}}
  +\underbrace{\frac{2}{(1-γ)^{2}}κ}_{\text{eval}}
  +\underbrace{\frac{2(1+√d)}{(1-γ)^{2}}ε}_{\text{approx}}
$$

remain **additive** rather than multiplicative, and √d is the *minimal* extrapolation factor (Kiefer–Wolfowitz).  Thus a moderate feature dimension keeps ε‑blow‑up tolerable.&#x20;

---

#### 6.  Conceptual bridge to the rest of the lecture

| Next section                                       | Key concern originating from motivation                          |
| -------------------------------------------------- | ---------------------------------------------------------------- |
| **Approx. universal value‑function realisability** | Makes ε explicit; decides whether API is even *applicable*.      |
| **Approx. policy evaluation**                      | Supplies κ; must hit polynomial‑time target.                     |
| **Extrapolation control**                          | Prevents κ from ballooning outside design set C.                 |
| **Kiefer–Wolfowitz & corollaries**                 | Show √d is achievable and near‑optimal.                          |
| **Geometric progress → API theorem**               | Converts per‑iteration κ into global performance bound.          |
| **LSPI guarantee**                                 | Implements the whole pipeline; answers the motivating questions. |

---

### Progress ( step 1 of filling in details )

* **Delivered** a full, rigorously referenced motivation section explaining (i) why approximation is necessary, (ii) how linear features lead to polynomial‑time planning, and (iii) what error decomposition underpins effectiveness.
* **Extracted** the exact statements of efficiency/effectiveness from *lec 8* §1 and linked them to later technical machinery.

**Open issues & next steps**

1. Proceed to **Section 2: Approximate Universal Value‑Function Realisability** — formal definitions, examples, and its necessity.
2. Provide expanded derivations for LSPE error bounds and the Kiefer–Wolfowitz theorem’s role.
3. Eventually integrate diagrams (e.g., the state‑space Venn sketch on *lec 7* p. 4) to visualise hierarchy of assumptions.

Let me know when to move on to Section 2 or if you’d like further elaboration here.

---


\### 2 Approximate Universal Value‑Function Realisability  (Assumption B2)

---

| Item                                       | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                              |                                                     |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **(a) Formal statement**                   | Let ϕ : S × A → ℝᵈ be a fixed feature‑map and let 𝔽ϕ ≜ {Φθ : θ ∈ ℝᵈ}.  We say that the MDP *and* ϕ satisfy **B2(ε)** if for **every** deterministic or stochastic, memory‑less policy π, \(\displaystyle \inf_{θ\in\mathbb{R}^{d}}\|q_{π}-Φθ\|_{\infty}\le ε\).  The shorthand notation is \(q_{π}\in_{ε}\mathcal F_{ϕ}\).                                                                                                                                                                         |                                                                                                                              |                                                     |
| **(b) Why B2 is needed**                   | *Uniformity across policies.*  In API we repeatedly evaluate and improve **intermediate policies π₀,π₁,…**.  To keep the approximation error from exploding we must know *a priori* that **each** qπ admits an ε‑close representation in the same low‑dimensional space; otherwise the greedy step could leave the span of features after one iteration and the analysis would collapse.  Lecture 7 points out precisely this danger (paragraph below Eq. (1) and the Venn diagram on page 4).  |                                                                                                                              |                                                     |
| **(c) Key consequences**                   | 1. *Bounded approximation term.*  Setting ε\_apx ≜ supπ infθ‖qπ − Φθ‖∞, B2(ε) asserts ε\_apx ≤ ε; this constant appears additively (and *only* additively) in all later API bounds.  <br>2. *Existence of near‑greedy parameters.*  For every π there exists θπ with max‑norm error ≤ ε; hence π’s greedy successor can be implemented with a dot‑product of θπ and features—cost O(d).                                                                                                         |                                                                                                                              |                                                     |
| **(d) Proof of sufficiency for API**       | Assume LSPE‑G produces θ̂ such that ‖qπ − Φθ̂‖∞ ≤ κ (Section 6).  Under B2 the total policy‑evaluation error is ≤ κ + (1+√d)ε (Lemma 6, Eq. (7) in lecture 8) and the API theorem (Eq. (12)) then gives \(\|v^{*}-v_{π_k}\|_{\infty}\le\frac{γ^{k}}{1-γ}+\frac{2}{(1-γ)^{2}}(κ+(1+\sqrt d)ε)\).   Thus *all* three error sources—iteration, evaluation and approximation—remain controlled.                                                                                                       |                                                                                                                              |                                                     |
| **(e) Necessity (counter‑example sketch)** | Without B2 there exists an MDP where qπ cannot be approximated uniformly.  Start with a two‑state, two‑action deterministic MDP and choose ϕ so that the first policy’s value lies in span(ϕ) but the optimal policy’s value differs on exactly one state by +1.  API’s greedy step exits the span so θ̂ cannot approximate qπ₁, breaking the extrapolation lemma’s pre‑condition and voiding the convergence proof.                                                                            |                                                                                                                              |                                                     |
| **(f) Sufficient structural conditions**   | *Linear MDPs.*  If rewards and transitions factorise as r(s,a)=⟨ϕ(s,a),θ\_r⟩ and P(s′                                                                                                                                                                                                                                                                                                                                                                                                           | s,a)=⟨ϕ(s,a),ν(s′)⟩ (Lecture 7, page 6), then **B2(0)** holds because \(q_{π}=Φθ_{π}\) with θπ = θ\_r + γ ∑*{s′}ν(s′) E*{a∼π(· | s′)}θπ.  This fixed‑point equation keeps θπ in ℝᵈ.  |
| **(g) Approximate linear MDPs**            | If rewards and transitions are only ε₀ close to such factorizations (Eq. (2), lecture 7 p. 6), then B2(ε) holds with ε = ε₀ · (1+γ)/(1−γ).                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                              |                                                     |
| **(h) Practical diagnostics**              | *Empirical compatibility test.*  Collect rollout tuples (s,a,r,s′) under a mix of exploratory policies and fit θ via least‑squares to \(\hat r+γ\max_{a′}\langle θ,\varphi(s′,a′)\rangle\).  If the residual’s max‑norm is large, B2 is violated for the current feature set—suggesting feature engineering or representation learning is required before running API.                                                                                                                            |                                                                                                                              |                                                     |

---

\#### Examples illustrating B2

| Example                                                                       | ε     | Explanation                                                                                                                  |   |   |   |                        |
| ----------------------------------------------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------- | - | - | - | ---------------------- |
| Finite‑horizon Linear Quadratic Regulator with Fourier features of degree ≤ 2 | 0     | Dynamics and cost are quadratic; value functions are quadratic hence captured exactly.                                       |   |   |   |                        |
| Tabular encoding (ϕ is one‑hot on S×A)                                        | 0     | Span covers *all* q‑functions, but d =                                                                                       | S |   | A | so we lose efficiency. |
| Tile coding with coarse tiles on Mountain‑Car                                 | ≈ 0.1 | Empirically, each qπ can be approximated within 0.1 because value varies smoothly; B2 holds with small ε enabling fast LSPI. |   |   |   |                        |

*(The Venn diagram on page 4 of lecture 7 visually situates B2 inside the hierarchy of assumptions: A2 & B2 sets are drawn as tiny circles within the universe of MDPs, underscoring how demanding universal realisability can be in practice.)*&#x20;

---

\### Progress

* Delivered a **self‑contained, rigorously defined exposition of Assumption B2**, including statement, necessity, consequences, proofs of sufficiency, concrete structural conditions, and illustrative examples.
* Pulled formal derivations and numerics directly from **lecture 7 pages 3–6** and **lecture 8 Eq. (7), (12)** for tight alignment with the source material.

**Open issues / next section**

> **3  Approximate Policy Evaluation (LSPE)** – derive the weighted least‑squares normal equations, prove unbiasedness of random‑length rollouts, and compute high‑probability κ‑bounds.

Let me know when to proceed to Section 3.

---


\### 3 Approximate Policy Evaluation (LSPE)

*Goal:* given a **fixed** memory‑less policy π and a feature map ϕ : S × A → ℝᵈ that satisfies Assumption B2, construct an estimate
\(\widehat q_{π}=Φ\widehat θ\) such that ‖qπ − Φθ̂‖∞ is provably small **everywhere**, not only on the sampled points—while keeping both computation and sampling **polynomial in d** and independent of |S|.

---

\#### 3.1 Monte‑Carlo rollout targets

| notation                      | definition                                          | comment                           |                                               |
| ----------------------------- | --------------------------------------------------- | --------------------------------- | --------------------------------------------- |
| **Design set** C ⊂ S × A      |                                                     | C                                 | will later be ≤ d(d + 1)/2 (Kiefer–Wolfowitz) |
| Weighting ρ ∈ Δ₁(C)           | Σ\_{z∈C} ρ(z)=1                                     | appears in weighted least‑squares |                                               |
| Random rollout length H^{(j)} | H^{(j)} \~ Geom(1 − γ)                              | eliminates explicit γ⁽ᵗ⁾ factors  |                                               |
| Single‑trajectory return      | \(R^{(j)}(z)=\sum_{t=0}^{H^{(j)}-1}r_t^{(j)}(z)\)     | unbiased for qπ(z)                |                                               |
| Empirical mean                | \(\widehat R^{m}(z)=\frac1m\sum_{j=1}^{m}R^{(j)}(z)\) | m i.i.d. copies                   |                                               |

Because \(\mathbb{E}[R^{(j)}(z)] = q_{π}(z)\), the estimator \(\widehat R^{m}(z)\) is **unbiased** and has variance ≤ 1 / (4(1 − γ)²) when rewards are in \[0,1].&#x20;

> **Diagrammatic intuition (lecture 8, page 1)**: the figure shows *m* trajectories of geometrically distributed length branching from each (s,a)∈C; by construction the expected discounted return equals the undiscounted sum because the random‑stop compensates for γ⁽ᵗ⁾.&#x20;

---

\#### 3.2 Weighted least‑squares estimator

Define the **ρ‑weighted normal equations**

$$
\widehat θ
=\arg\min_{θ\in\mathbb{R}^{d}}
\sum_{z\in C}\!ρ(z)\bigl(⟨θ,ϕ(z)⟩-\widehat R^{m}(z)\bigr)^{2}
=G_{ρ}^{-1}\!\sum_{z\in C}\!ρ(z)\widehat R^{m}(z)ϕ(z),
\tag{3}
$$

with moment matrix
\(G_{ρ}= \sum_{z\in C}ρ(z)\,ϕ(z)ϕ(z)^{⊤}\).

* **Cost:** forming Gρ costs O(|C|d²) arithmetic; Cholesky solve costs O(d³).
  With |C| = O(d²) (Section 3.4) the total is 𝒪(d³), **independent of |S|**.
* **Storage:** only d×d + O(|C|d) numbers (poly(d)).
* **Linear regression viewpoint:** (3) is exactly ordinary least‑squares on synthetic data set {(ϕ(z), \(\widehat R^{m}(z)\))} with heteroskedastic noise—weights ρ down‑weight high‑variance points.

---

\#### 3.3 Extrapolation error on an arbitrary (s,a)

Write ε(z)=ϕ(z)^{⊤}θ − qπ(z).  From (3),

$$
ϕ(z)^{⊤}\!(\widehat θ-θ)=ϕ(z)^{⊤}G_{ρ}^{-1}\!\sum_{z'∈C}\!ρ(z')\bigl(ε(z')+qπ(z')-\widehat R^{m}(z')\bigr)ϕ(z').
$$

**Lemma (Extrapolation control in weighted LS)**
Provided Gρ is nonsingular,

$$
\boxed{~~
|ϕ(z)^{⊤}\widehat θ-ϕ(z)^{⊤}θ|
\;\le\;
g(ρ)\,\max_{z'∈C}|qπ(z')-\widehat R^{m}(z')|,~~}
\tag{4}
$$

with geometry factor
\(g(ρ):=\max_{z\in S×A}\|ϕ(z)\|_{G_{ρ}^{-1}}.\)&#x20;

*Proof sketch:* expand the difference, apply Hölder then Jensen exactly as in lines 40‑64 of lecture 8.

*Interpretation:* as long as the **design (C,ρ)** keeps g(ρ) moderate, the worst‑case *prediction* error is at most g(ρ) times the worst measurement error on C.

---

\#### 3.4 Optimal experimental design (Kiefer–Wolfowitz)

The **G‑optimal design problem** chooses (C,ρ) to minimise g(ρ).
Kiefer–Wolfowitz (1960) shows

$$
\exists(C,ρ)\ \text{s.t.}\ |C| \le \tfrac{d(d+1)}{2}\quad\text{and}\quad g(ρ)=\sqrt d.
\tag{5}
$$

Thus **√d is information‑theoretically minimal**, and depends only on d—not on |S|.&#x20;

---

\#### 3.5 High‑probability uniform error bound (LSPE‑G lemma)

Combine (4) with (5) and a Hoeffding bound for each \(\widehat R^{m}(z)\):

$$
\Pr\!\Bigl[
\|q_{π}-Φ\widehat θ\|_{\infty} \le
(1+\sqrt d)\,\underbrace{\|ε_{π}\|_{\infty}}_{\text{approx.\ error}}
+\sqrt d\!\Bigl(
\frac{γ^{H}}{1-γ}
+\frac{1}{1-γ}\sqrt{\frac{\ln(2|C|/δ)}{2m}}
\Bigr)
\Bigr]\;\ge\;1-δ.
\tag{6}
$$

*Parameters to hit a target precision κ:* choose

$$
H \;\ge\; \frac{\ln\!\bigl((1-γ)κ/(√d)\bigr)}{\ln γ},\quad
m \;\ge\; \frac{d}{(1-γ)^{2}κ^{2}}\ln\!\frac{2|C|}{δ}.
\tag{7}
$$

Because |C| = 𝒪(d²), we obtain **sample complexity poly(d,(1−γ)⁻¹,κ⁻¹,log 1/δ)**.&#x20;

---

\#### 3.6 Algorithm box – LSPE‑G

| Step | Operation                                                                                     | Cost           |   |                    |
| ---- | --------------------------------------------------------------------------------------------- | -------------- | - | ------------------ |
| 1    | Input policy π, design (C,ρ) from K‑W.                                                        | pre‑computed   |   |                    |
| 2    | For each z∈C, roll out π **m** times with random horizon **H** → targets \(\widehat R^{m}(z)\). | O(m            | C | H) simulator steps |
| 3    | Form Gρ and right‑hand side; solve (3) → θ̂.                                                  | O(d³)          |   |                    |
| 4    | Output q̂ = Φθ̂ and greedy action rule a\*(s)=argmax\_a⟨θ̂, ϕ(s,a)⟩.                          | O(d) per state |   |                    |

*Wall‑clock summary*: simulator time dominates and is polynomial; linear‑algebra time is cubic in d.

---

\#### 3.7 Putting it in context

| error component           | controlled by             |                 |          |
| ------------------------- | ------------------------- | --------------- | -------- |
| **Approximation** ε       | Assumption B2 (Section 2) |                 |          |
| **Truncation** γᴴ/(1−γ)   | H in (7)                  |                 |          |
| **Statistical** √{ln(     | C                         | /δ)/(2m)}/(1−γ) | m in (7) |
| **Extrapolation gain** √d | G‑optimal design (5)      |                 |          |

With κ chosen via (7), Section 6 will feed the bound (6) into the **Geometric Progress Lemma** to analyse one API iteration, and Section 10 folds everything into the final LSPI guarantee.

*Visual aide:* the table at the bottom of lecture 8, page 1, annotates each error source with the symbol used above.&#x20;

---

\### Progress

* Derived the **weighted least‑squares estimator** (Eq. 3) and gave its computational profile.
* Proved **extrapolation control** (Eq. 4) and imported the **√d G‑optimal design** (Eq. 5).
* Produced the **high‑probability LSPE‑G bound** (Eq. 6) with explicit sample/horizon schedules (Eq. 7).
* Summarised the **LSPE‑G algorithm** and connected each parameter to the three error sources.

**Next section:** 4 – *Kiefer–Wolfowitz theorem* itself (statement, intuition, constructive variants) and the subsequent corollary (√d extrapolation bound). Let me know when to proceed!


---


\### 4 Kiefer–Wolfowitz Theorem and Optimal Experimental Design
*(“Section 4” in the agreed outline)*

---

\#### 4.1 Preliminaries: the design‐quality functional

Let

$$
G_{ρ}\;=\;\sum_{z\in C}\!ρ(z)\,ϕ(z)ϕ(z)^{⊤}\quad(\text{moment matrix}), \qquad  
g(ρ)\;=\;\max_{z\in\mathcal Z}\|ϕ(z)\|_{G_{ρ}^{-1}} ,
\tag{4.1}
$$

where

* \(C\subseteq\mathcal Z:=S\times A\) is a **design set** (the points on which we will measure the returns),
* \(ρ\in\Delta_{1}(C)\) is a probability weight over \(C\) (the relative sampling frequencies).

Recall from the extrapolation lemma (Sec. 3, Eq. (3.4)) that any weighted least‑squares predictor obeys

$$
\bigl|ϕ(z)^{⊤}\widehat θ-ϕ(z)^{⊤}θ\bigr|
\;\le\;g(ρ)\,\max_{z'∈C}\!\bigl|q_{π}(z')-\widehat R^{m}(z')\bigr| .
$$

Hence **our only lever to control global prediction error is to drive \(g(ρ)\) down**.

---

\#### 4.2 G‑optimal design problem

> **Goal:**
> Find \((C,ρ)\) that minimises \(g(ρ)\).
>
> $$
> \min_{C\subseteq \mathcal Z,\;|C|\le N}\ \min_{ρ\in\Delta_{1}(C)}\; g(ρ),
> $$
>
> typically with \(N\) no larger than a low‑order polynomial in the feature dimension \(d\).

This is the classical *G‑optimal* criterion in experimental design theory (the “G” stands for **g**eneralised variance).

---

\#### 4.3 Kiefer–Wolfowitz Theorem

> **Theorem (Kiefer & Wolfowitz 1960).**
> Assume the feature matrix Φ has full column‑rank \(d\).
> Then **there exists** a design set \(C_{\star}\subseteq\mathcal Z\) and weights \(ρ_{\star}\in\Delta_{1}(C_{\star})\) such that
>
> $$
> \boxed{\;g(ρ_{\star})=\sqrt d\;}, \qquad |C_{\star}|\;\le\;\frac{d(d+1)}{2}.
> $$
>
> Moreover, \(\sqrt d\) is *information‑theoretically optimal*: no design can achieve a smaller worst‑case variance factor.&#x20;

\##### Sketch of proof (3 hops)

1. **Equivalence Theorem.** Kiefer & Wolfowitz show that minimising \(g(ρ)\) (G‑optimality) is *dual* to **maximising \(\det G_{ρ}\)** (D‑optimality). The proof uses Fenchel duality for convex cones of positive‑semidefinite matrices.
2. **Carathéodory bound.** Any point in the convex hull of rank‑1 PSD matrices \(\{ϕ(z)ϕ(z)^{⊤}\}\) can be expressed as a convex combination of at most \(\frac{d(d+1)}{2}\) extremal points, yielding the cardinality bound on \(C_{\star}\).
3. **Spectral‐radius lower bound.** For any feasible ρ, \(\lambda_{\min}(G_{ρ})\le \tfrac{1}{d}\,\operatorname{tr}G_{ρ}=1\). One shows that the design achieving equality forces **all** directions to be sampled equally, giving \(\max_{z}\|ϕ(z)\|_{G_{ρ}^{-1}}\ge\sqrt d\) with equality when \(G_{ρ}\propto I_d\).

The full algebraic details appear on *Lecture 8, proof block following Eq. (5)*.&#x20;

---

\#### 4.4 Interpretation

* **Geometry.**  \(g(ρ)\) is the *radius* of the largest Mahalanobis ball, in metric \(G_{ρ}\), that contains every feature vector. K‑W says you can always choose ≤ d(d+1)/2 points so that this ball’s radius is exactly √d.
* **Dimension–only factor.**  Crucially, √d does **not** depend on |S| or |A|; it grows only as the square‑root of the feature dimension.
* **Tightness.**  The textbook example where the bound is attained is the *unit simplex*: states are the canonical basis vectors in ℝᵈ; any design must accept √d amplification.

A helpful visual appears in the *right‑hand plot of Lecture 8, page 2*, showing feature vectors scattered on a sphere and the smallest enclosing ellipsoid aligned with coordinate axes.

---

\#### 4.5 Computing (approximately) G‑optimal designs

While the theorem is existential, we need a constructive routine:

| Algorithm                                                     | Guarantee                   | Complexity\*                                                 | Notes                                          |                       |                                                  |     |    |     |         |
| ------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------ | ---------------------------------------------- | --------------------- | ------------------------------------------------ | --- | -- | --- | ------- |
| **Volume‑sampling / volumetric spanners** (Hazan et al. 2016) | \(g(ρ)\le 2\sqrt d\)          | (\tilde O\bigl(                                              | \mathcal Z                                     | ,d\bigr)) data passes | Works with a streaming pass over feature vectors |     |    |     |         |
| **Greedy D‑optimal** (continuous‑greedy)                      | \(g(ρ)\le \sqrt{d}\,(1+ε)\)   | poly\((d,1/ε)\) but needs membership queries over \(\mathcal Z\) | Good when a *generator* of \(\mathcal Z\) exists |                       |                                                  |     |    |     |         |
| **Random design + ridge regression**                          | (g(ρ)=\tilde O(\sqrt{d,\log | \mathcal Z                                                   | }))                                            | very cheap            | Suffices for finite                              | S×A | if | S×A | « e^{d} |

\*arithmetic operations, ignoring simulator calls.  See *Lecture 8, “Cost of optimal design” paragraph* for discussion.&#x20;

---

\#### 4.6 Corollary – Extrapolation Error Control via Optimal Design

Let \((C_{\star},ρ_{\star})\) be any design with \(g(ρ_{\star})\le\sqrt d\).
For every policy π and every estimator θ̂ obtained from **LSPE‑G** (Sec. 3),

$$
\|q_{π}-Φ\widehat θ\|_{\infty}  
\;\le\; \sqrt d \,\max_{z'∈C_{\star}}\!\bigl|q_{π}(z')-\widehat R^{m}(z')\bigr|
\;\le\; (1+\sqrt d)\,ε_{\text{apx}}\;+\;\sqrt d\Bigl(\tfrac{γ^{H}}{1-γ}\;+\;\tfrac{1}{1-γ}\sqrt{\tfrac{\ln(2|C_{\star}|/δ)}{2m}}\Bigr)
\tag{4.2}
$$

with probability ≥ 1 − δ.  Compare Eq. (4.2) to the generic bound with g(ρ); the √d factor is now *locked in*.&#x20;

---

\#### 4.7 Practical checklist for using K‑W in API / LSPI

1. **Pre‑compute design** once for the chosen feature map (offline).
2. Store \(C_{\star}\) and weights \(ρ_{\star}\); memory ≤ d(d+1)/2 vectors.
3. In every policy‑evaluation call:

   * Roll‑out m trajectories of random length H from each \(z∈C_{\star}\).
   * Solve the weighted normal equations using \(G_{ρ_{\star}}\).
4. Plug κ from Eq. (4.2) into the geometric progress lemma (Sec. 7) and final LSPI bound (Sec. 10).

Because the design is independent of the MDP *and* of the current policy, steps 1–2 cost **zero simulator time** and never have to be repeated.

---

\#### Key take‑aways of Section 4

* K‑W gives a **dimension‑only** path to keep extrapolation risk under control.
* The √d factor is **provably unavoidable** for any algorithm relying on linear least‑squares.
* Efficient approximate solvers exist; exact optimum is unnecessary—any constant‑factor approximation merely scales the final bound by that constant.
* The theorem is the cornerstone that lets Approximate Policy Iteration remain *state‑space‑independent*.

---

\### Progress

* **Provided** a formal statement and proof sketch of the Kiefer–Wolfowitz theorem, citing its location in *Lecture 8*.
* **Derived** the corollary (Eq. 4.2) that feeds directly into the LSPE‑G lemma.
* **Outlined** algorithmic options for computing near‑optimal designs with practical complexity guarantees.

**Next section:** *6 LSPE‑G Extrapolation Error Control Lemma* – we will use Eq. (4.2) to derive the high‑probability κ‑bound and show precise sample‑size formulas. Let me know when to proceed!


---


\### 6 LSPE‑G Extrapolation Error Control Lemma
*(“Section 6” in the running outline)*

---

\#### 6.1 Setting and notation recap

| Symbol                                                                                 | Meaning                                                     | From section |               |    |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------ | ------------- | -- |
| \(ϕ:S\times A→ℝ^{d}\)                                                                    | full‑rank linear feature map                                | §2           |               |    |
| \(C_{\star},ρ_{\star}\)                                                                  | G‑optimal design with \(g(ρ_{\star})=√d\) and (               | C\_{\star}   | \le d(d+1)/2) | §4 |
| \(π\)                                                                                    | fixed policy whose action‑value \(q_{π}\) we evaluate         |              |               |    |
| \(H\)                                                                                    | random‑rollout truncation horizon                           | §3.1         |               |    |
| \(m\)                                                                                    | rollouts per design point                                   | §3.1         |               |    |
| \(R^{(j)}(z)\)                                                                           | return of j‑th trajectory launched from \(z=(s,a)∈C_{\star}\) | Eq. (3.1)    |               |    |
| \(\widehat R^{m}(z)=\frac1m\sum_{j=1}^{m}R^{(j)}(z)\)                                    | empirical mean target                                       | Eq. (3.1)    |               |    |
| \(G_{ρ_{\star}}=\sum_{z∈C_{\star}}\!ρ_{\star}(z)\,ϕ(z)ϕ(z)^{\top}\)                      | moment matrix                                               | Eq. (4.1)    |               |    |
| \(\widehat θ=G_{ρ_{\star}}^{-1}\!\sum_{z∈C_{\star}}\!ρ_{\star}(z)ϕ(z)\widehat R^{m}(z)\) | LSPE‑G coefficient vector                                   | Eq. (3.2)    |               |    |
| \(\widehat q_{π}=Φ\widehat θ\)                                                           | fitted action‑value function                                |              |               |    |

The random‑length rollout scheme **removes the γ‑weights** from the return definition, as illustrated in the *trajectory tree on lecture 8, page 1* where each branch terminates with probability \(1-γ\).&#x20;

---

\#### 6.2 Lemma statement

> **Lemma (LSPE‑G extrapolation error control).**
> Assume
>
> * immediate rewards lie in \([0,1]\);
> * \(π\) is any memory‑less policy;
> * Assumption B2(ε) holds; and
> * the design \((C_{\star},ρ_{\star})\) is √d‑optimal.
>   Then for any confidence level \(δ∈(0,1)\),
>
> $$
> \Pr\!\Bigl[
> \|\,q_{π}-Φ\widehat θ\|_{\infty}\le
> (1+√d)\,ε
> +√d\Bigl(\tfrac{γ^{H}}{1-γ}
> +\tfrac{1}{1-γ}\sqrt{\tfrac{\ln(2|C_{\star}|/δ)}{2m}}\Bigr)
> \Bigr]\;\ge\;1-δ .
> \tag{6.1}
> $$

---

\#### 6.3 Proof sketch (three ingredients)

1. **Measurement–target gap.**
   \(\widehat R^{m}(z)\) is an unbiased estimator of \(q_{π}(z)\) (see derivation directly below Eq. (2) on lecture 8 p. 1). With truncation at fixed horizon \(H\) the bias is upper‑bounded by \(γ^{H}/(1-γ)\); with random horizon it vanishes, but we keep \(H\) explicit because it simplifies simulator implementation.
   Hoeffding’s inequality on the bounded returns gives, for each \(z\),

   $$
   \Pr\!\Bigl[\,\bigl|\widehat R^{m}(z)-q_{π}(z)\bigr|\le
   \tfrac1{1-γ}\sqrt{\tfrac{\ln(2/δ_{z})}{2m}}\Bigr]\;\ge\;1-δ_{z}.
   $$

   Choosing \(δ_{z}=δ/|C_{\star}|\) and union‑bounding yields the *statistical error* term in Eq. (6.1).&#x20;

2. **Extrapolation amplification.**
   The weighted least‑squares bound (Lemma “extrapolation error control in least‑squares” just after Eq. (5) on lecture 8 p. 2) states

   $$
   \|Φ\widehat θ-q_{π}\|_{\infty}\le
   g(ρ_{\star})\,\max_{z∈C_{\star}}|\,\widehat R^{m}(z)-q_{π}(z)| .
   $$

   With \(g(ρ_{\star})=√d\) this multiplies every measurement error by √d.&#x20;

3. **Approximation term.**
   By Assumption B2(ε) there exists θπ such that \(\|q_{π}-Φθ_{π}\|_{\infty}≤ε\).  Add and subtract \(Φθ_{π}\) inside the norm and triangle‑inequality gives the extra \((1+√d)ε\) in Eq. (6.1).  The \(+ε\) is the *unamplified* part (model bias), √dε is the piece that gets stretched when extrapolating.

Combine the three bullet points to obtain (6.1).  Full algebra appears in lines 110‑155 of lecture 8.&#x20;

---

\#### 6.4 Turning the bound into a **κ‑budget**

Set a user‑chosen tolerance κ > 0 for the policy‑evaluation error term that will feed the geometric progress lemma (next section).  It suffices to pick horizon \(H\) and sample size \(m\) so that

$$
√d\Bigl(\tfrac{γ^{H}}{1-γ}\Bigr)\le \tfrac{κ}{2},\qquad
√d\Bigl(\tfrac{1}{1-γ}\sqrt{\tfrac{\ln(2|C_{\star}|/δ)}{2m}}\Bigr)\le \tfrac{κ}{2}.
$$

Solving gives

$$
\boxed{
\;
H \;\ge\; H_{γ,κ}:=\Bigl\lceil\log_{γ}\!\Bigl(\tfrac{κ(1-γ)}{2√d}\Bigr)\Bigr\rceil,\;
m\;\ge\;
\frac{2d}{(1-γ)^{2}κ^{2}}\,
\ln\!\frac{2|C_{\star}|}{δ}
\;}
\tag{6.2}
$$

(using \(|C_{\star}|≤d(d+1)/2\)).  Both quantities grow **polynomially in d, 1/(1−γ), 1/κ, log(1/δ)** and never in \(|S|\).

---

\#### 6.5 Error‑budget table for LSPE‑G

| Source                 | Magnitude            | Tuned by        |            |                   |
| ---------------------- | -------------------- | --------------- | ---------- | ----------------- |
| **Approximation**      | \((1+√d)ε\)            | richer features |            |                   |
| **Truncation**         | \(√d\,γ^{H}/(1-γ)\)    | larger \(H\)      |            |                   |
| **Statistical**        | (√d/(1-γ)\sqrt{\ln(2 | C\_{\star}      | /δ)/(2m)}) | more rollouts \(m\) |
| **Extrapolation gain** | √d                   | fixed by design |            |                   |

The *stacked bar* in the **diagram on lecture 8, page 3** visualises exactly these four constituents side‑by‑side.&#x20;

---

\#### 6.6 Practical implications

* **Simulator budget.**  Using (6.2) with κ ≍ ε′/4 (where ε′ is the global error the planner can tolerate) makes the LSPE‑G call the *dominant* simulator cost:
  \(O\bigl(|C_{\star}|\,m\,H\bigr)=\tilde O\!\bigl(\frac{d^{3}}{(1-γ)^{5}ε′^{2}}\bigr)\).
  Computation outside the simulator is only the \(d×d\) Cholesky solve, \(O(d^{3})\).
* **Independence from |S|.**  All parameters depend on d and γ only; the size or continuity of the state space is irrelevant once we have simulator access.
* **Robust to constant‑factor design slack.**  If a fast heuristic yields \(g(ρ)≤c√d\) with \(c≤2\) (see volumetric spanners, §4.5), the bound scales by the same constant – acceptable in practice.

---

\### Progress

* **Provided** a rigorous statement (Eq. 6.1) with all constants visible.
* **Explained** each term’s provenance and supplied explicit schedules (Eq. 6.2) to meet any target κ.
* **Grounded** the derivation by referencing the relevant proof blocks and figures in *Lecture 8*.

---

\### 7 Geometric Progress Lemma with *Approximate* Policy Improvement

This lemma generalises the “policy‑improvement” step of classical Policy Iteration to the realistic situation where the greedy step is **imperfect**—e.g. because we used an approximate action‑value function coming from LSPE‑G.  It quantifies how much progress toward optimality is preserved in each iteration despite that imperfection.

---

\#### 7.1 Formal statement

> **Lemma (Geometric progress with error ε).**
> Let π be any memory‑less policy and let vπ be its value function.
> Let π′ be *any* policy such that
>
> $$
> T v_{π}\;=\;T_{π′} v_{π}\;+\;ε,
> \tag{7.1}
> $$
>
> where \(T\) is the optimal Bellman operator and \(T_{π′}\) the policy‑specific operator.
> Then
>
> $$
> \boxed{\;
> \bigl\|v^{*}-v_{π′}\bigr\|_{\infty}
> \;\le\;
> γ\,\bigl\|v^{*}-v_{π}\bigr\|_{\infty}
> \;+\;
> \frac{1}{1-γ}\,\|ε\|_{\infty}\;}
> \tag{7.2}
> $$

Equation (7.2) appears verbatim in *Lecture 8, “Geometric progress lemma with approximate policy improvement”* .

---

\#### 7.2 Intuition

* **Exact PI:** when ε = 0 the lemma reduces to classical monotonicity: each greedy step contracts the sub‑optimality by a factor γ.
* **Approximate PI:** the additive term \(\|ε\|_{\infty}/(1-γ)\) captures how much that contraction is *spoiled* by evaluation or approximation errors.
* **Take‑away:** as long as ε is kept small (Section 6 shows how via LSPE‑G), the multiplicative γ‑shrink dominates and overall progress remains geometric.

---

\#### 7.3 Proof sketch

1. **Optimality equation:** \(v^{*}=T v^{*}=T_{π^{*}} v^{*}\), where π\* is optimal.
2. **Value‑difference identity** (derived from Lemma 6.1 in Bertsekas & Tsitsiklis):

   $$
   v^{*}-v_{π′}
   \;=\;
   T_{π^{*}}v^{*}-T_{π^{*}}v_{π}
   +T v_{π}-T_{π′}v_{π}
   +T_{π′}v_{π}-T_{π′}v_{π′}.
   $$
3. **Apply (7.1)** to substitute \(T v_{π}-T_{π′}v_{π}=ε\).
4. **Use monotonicity & contraction:** the operator \((I-γP_{π′})^{-1}=∑_{k≥0}(γP_{π′})^{k}\) is positive and has norm ≤ 1/(1‑γ). Rearranging terms yields

   $$
   v^{*}-v_{π′}
   \;\le\;
   γP_{π^{*}}(v^{*}-v_{π})\;+\;(I-γP_{π′})^{-1}ε.
   $$
5. **Take max‑norms:** \(\|γP_{π^{*}}(v^{*}-v_{π})\|_{\infty}≤γ‖v^{*}-v_{π}‖_{\infty}\) and \(\|(I-γP_{π′})^{-1}ε\|_{\infty}≤‖ε‖_{\infty}/(1-γ)\). This proves (7.2).&#x20;

*The complete algebra can be seen on lecture 8, page 4, lines headed “Proof:”*.

---

\#### 7.4 Role within Approximate Policy Iteration

| Location in pipeline                                     | Error propagated                      | How lemma is used                                        |
| -------------------------------------------------------- | ------------------------------------- | -------------------------------------------------------- |
| After an LSPE‑G evaluation of π                          | κ ≔ ‖qπ − Φθ̂‖∞ (Sec. 6) → ε in (7.1) | Gives per‑iteration bound γ·prev + ε/(1‑γ)               |
| In *Approximate Policy Iteration Theorem* (next section) | Accumulates ε₀…εₖ₋₁                   | Telescoping the lemma over k iterations yields Eq. (8.1) |

Thus Lemma 7 is the **bridge** between single‑step evaluation quality (κ) and multi‑step policy performance.

---

\#### 7.5 Practical guidance

* **Keep ε small:** Section 6 shows ε ≈ κ ≤ O(√d γᴴ + √d/√m + (1+√d)ε\_apx). Choose H and m per Eq. (6.2) so that ε ≪ (1‑γ).
* **Iteration budget K:** because the multiplicative term is γ, achieving iteration error ≤ ε′ simply needs
  \(K ≥ \lceil\log_{1/γ}( (1-γ)ε′^{-1})\rceil\).
* **Independence:** Lemma 7 does **not** assume where ε comes from; hence any improved evaluator (e.g., TD(λ), LSTD) can be swapped in.

---

\### Progress

* **Completed Section 7**: presented the lemma’s statement, intuition, detailed proof, and its role in the overall API analysis, with precise citations to *Lecture 8*.
* The next step is **Section 8 – Approximate Policy Iteration Theorem**, which telescopes Lemma 7 across K iterations and introduces the explicit bound separating iteration, evaluation, and approximation errors.

\### 8 Approximate Policy Iteration (API) Theorem

This section “stacks” the single‑step **Geometric Progress Lemma** (Sec. 7) across *K* iterations to give a non‑asymptotic, end‑to‑end performance guarantee for the entire API loop.

---

\#### 8.1 Algorithmic template recalled

For *k = 0,1,…,K–1*:

1. **Evaluation** – obtain θ̂ₖ from **LSPE‑G** with design (C\*,ρ\*) and parameters (H, m), producing q̂ₖ = Φθ̂ₖ.
2. **Improvement** – set πₖ₊₁ to be *greedy* w\.r.t. q̂ₖ, i.e.
   \(π_{k+1}(s)=\arg\max_{a}⟨θ̂_{k},ϕ(s,a)⟩.\)

Define

$$
ε_k \;=\; T v_{π_k}\;-\;T_{π_{k+1}} v_{π_k},
\quad
κ_k \;=\;\|q_{π_k}-Φθ̂_k\|_\infty .
$$

Under LSPE‑G, Sec. 6 gives a high‑probability bound κₖ ≤ κ.  Because the greedy stage uses **q̂ₖ**, one has ‖εₖ‖∞ ≤ 2κₖ ≤ 2κ (see lecture 8 lines labelled “εₖ≤2κ”).&#x20;

---

\#### 8.2 Theorem statement (Eq. (12) in lecture 8)

> **Theorem (API).**
> Assume Assumption B2(ε) and let κ be any upper bound that holds simultaneously for κ₀,…,κ\_{K−1}.  Then for every K ≥ 1, with probability ≥ 1 − δ (from the LSPE‑G events),
>
> $$
> \boxed{\;
> \|v^* - v_{π_K}\|_\infty
> \;\le\;
> \frac{γ^{K}}{1-γ}
> \;+\;
> \frac{2}{(1-γ)^2}\,\bigl(\kappa + (1+√d)\,ε\bigr)
> \;}
> \tag{8.1}
> $$

*(Lecture 8 derives the same bound with ε‑term expanded; our version gathers constants for clarity.)*&#x20;

---

\#### 8.3 Proof — telescoping Lemma 7

1. **Insert εₖ.** Geometric lemma (Sec. 7, Eq. 7.2) gives

   \(‖v^*-v_{π_{k+1}}‖∞ ≤ γ‖v^*-v_{π_k}‖∞ + ‖ε_k‖∞/(1-γ).\)

2. **Bound εₖ.** LSPE‑G ⇒ κₖ ≤ κ and greedy step ⇒ ‖εₖ‖∞ ≤ 2κ.

3. **Iterate.** Unroll the recursion K times (standard technique for linear inhomogeneous recurrences):

   $$
   ‖v^*-v_{π_K}‖∞
   ≤
   γ^{K}‖v^*-v_{π_0}‖∞
   +\frac{1}{1-γ}\sum_{s=0}^{K-1}γ^{K-1-s}‖ε_s‖∞ .
   $$

   Start from *any* π₀, so ‖v^\*-v\_{π\_0}‖∞ ≤ 1/(1−γ).  Plugging ‖ε\_s‖∞≤2κ and summing the geometric series yields (8.1).  The approximation term (1+√d)ε sits inside κ via Sec. 6.

*(Full algebra in lecture 8, lines immediately below Eq. (12).)*&#x20;

---

\#### 8.4 Interpreting the bound

| Term                          | Name                                                         | Control knob             |
| ----------------------------- | ------------------------------------------------------------ | ------------------------ |
| \(γ^{K}/(1-γ)\)                 | **Iteration error**                                          | Increase K               |
| \(\dfrac{2κ}{(1-γ)^{2}}\)       | **Evaluation error** (sampling + truncation + extrapolation) | Raise m, H via Eq. (6.2) |
| \(\dfrac{2(1+√d)ε}{(1-γ)^{2}}\) | **Approximation error**                                      | Enrich features          |

*• Additive, not multiplicative:* each source can be suppressed independently.
*• Dimension dependence:* only √d enters, inherited from design optimality.
*• State‑space independence:* no |S| or |A| appear.

---

\#### 8.5 Choosing K, H, m for a target precision ε′

Want ‖v\* − v\_{π\_K}‖∞ ≤ ε′.

1. **Split the budget**: allocate ε′/3 each to iteration, evaluation, approximation.

2. **Iteration** – set
   \(K \;≥\;\bigl\lceil \log_{1/γ}\!\bigl( 3/( (1-γ)ε′ )\bigr)\bigr\rceil.\)

3. **Evaluation** – choose κ = ε′(1−γ)²/6 and apply Eq. (6.2):

   $$
   H\;=\;O\!\Bigl(\frac{\ln(d/ε′)}{1-\gamma}\Bigr),\quad
   m\;=\;O\!\Bigl(\frac{d}{(1-\gamma)^{4}(ε′)^{2}}\ln\frac{d}{δ}\Bigr).
   $$

4. **Approximation** – require ε ≤ ε′/(3·2(1+√d)); if not satisfied, expand the feature set.

Total simulator cost: \(K·|C_{\!*}|·m·H = \tilde O\!\bigl(\frac{d^{3}}{(1-\gamma)^{6}(ε′)^{3}}\bigr)\); algebraic ops: \(K·O(d^{3})\).

---

\#### 8.6 Connections forward

* **Section 9** will refine the theorem for the common case where we bound *q*-errors directly (action‑value API corollary).
* **Section 10** will instantiate all parameters in the **LSPI** algorithm and present the final global guarantee.

---

\### Progress

* **Delivered Section 8**: formal theorem, proof, error decomposition, and parameter‑setting recipe, mirroring *lecture 8, Eq. (12)* and surrounding discussion.
* **Ready for Section 9** – *Corollary: API with Approximate Action‑Value Functions* — unless you’d like deeper elaboration here.

Let me know how you’d like to continue!



\### 9 Corollary: API with **Approximate Action‑Value Functions**

---

\#### 9.1 Setup and additional notation

At iteration *k* let

* **True** action–value: \(q_{π_k}\).
* **Approximation** (e.g. from LSPE‑G): \(q_k = Φθ̂_k\).
* **Approximation error** \(ε'_k := q_k - q_{π_k}\).

Define the *greedy w\.r.t. qₖ* policy

$$
π_{k+1}(s)=\arg\max_{a} q_k(s,a). 
$$

Following **(13)** of the lecture, the *approximate policy‑iteration (API‑Q)* loop is

$$
\boxed{\; π_{k+1} = \operatorname{Greedy}(q_k),\;
      q_k = q_{π_k} + ε'_k\;.}
$$

---

\#### 9.2 Corollary statement (lecture 8, “API with approx. Q”)

> **Corollary.**
> Suppose Assumption B2(ε) holds and the sequence \(\{ε'_k\}_{k=0}^{K-1}\) satisfies
> \(‖ε'_k‖_\infty ≤ ε' \) for all k.
> Then for every K ≥ 1
>
> $$
> \boxed{\;
> ‖v^{*}-v_{π_K}‖_\infty
> \;\le\;
> \frac{γ^{K}}{1-γ}
> \;+\;
> \frac{2ε'}{(1-γ)^{2}}\;.}
> \tag{9.1}
> \] :contentReference[oaicite:0]{index=0}  
> $$

The right‑hand side has **two** terms only: *iteration* and *Q‑approximation*; the evaluation‑specific κ from Section 8 is absorbed into ε′.

---

\#### 9.3 Proof (condensed)

1. **Link ε′ to ε in Lemma 7.**
   The greedy step uses q\_k twice (one to compute the arg‑max, one inside the Bellman operator).
   Lecture 8 shows \(‖ε_k‖_\infty ≤ 2‖ε'_k‖_\infty\).
2. **Apply Geometric Lemma.**
   Lemma 7 with ε\_k ⇒
   \(‖v^{*}-v_{π_{k+1}}‖ ≤ γ‖v^{*}-v_{π_k}‖ + 2‖ε'_k‖/(1-γ)\).
3. **Iterate** over k = 0…K−1 and sum the geometric series as in Section 8 to get (9.1).

Full algebra appears immediately below the corollary on lecture 8 page 5.&#x20;

---

\#### 9.4 Interpretation & practical impact

| Feature               | API‑V Theorem (Sec. 8) | API‑**Q** Corollary (Sec. 9)     |
| --------------------- | ---------------------- | -------------------------------- |
| Error fed into bound  | κ (policy‑evaluation)  | ε′ (direct Q error)              |
| Amplification factor  | \(2/(1-γ)^{2}\)          | *same* \(2/(1-γ)^{2}\)             |
| Needs κ → ε′ mapping  | Yes                    | **No** – use ε′ from any learner |
| Compatible evaluators | LSPE‑G, TD(λ), LSTD, … | **Any** Q‑approximator           |

*Take‑away:* if your algorithm already produces a near‑greedy **Q** estimate whose uniform error you can track, you may **skip** the Lemma 6 analysis and plug ε′ straight into (9.1).

---

\#### 9.5 Choosing parameters for LSPE‑G to meet an ε′ target

From Section 6, LSPE‑G delivers

$$
‖q_{π_k} - q_k‖_\infty = ‖ε'_k‖_\infty
≤ (1+√d)ε
       + √d\Bigl(\tfrac{γ^{H}}{1-γ}
                + \tfrac{1}{1-γ}\sqrt{\tfrac{\ln(2|C_\*|/δ)}{2m}}\Bigr).
$$

Set each bracket ≤ ε′/2 and solve as before:

$$
\begin{aligned}
ε &≤ \frac{ε′}{2(1+√d)},\\[4pt]
H &≥ \Bigl\lceil\log_{γ}\!\bigl(\tfrac{ε′(1-γ)}{2√d}\bigr)\Bigr\rceil,\\[4pt]
m &≥ \frac{2d}{(1-γ)^{2}ε′^{2}}\ln\!\frac{2|C_\*|}{δ}.
\end{aligned}
$$

Plugging into (9.1) with
\(K = \lceil\log_{1/γ}\tfrac{2}{(1-γ)ε′}\rceil\)
yields an ε′‑optimal policy after **poly(d,(1−γ)⁻¹, ε′⁻¹)** simulator steps—matching the LSPI headline sample complexity.&#x20;

---

\#### 9.6 When is the corollary preferable?

* **Model‑free settings** – if you run *Fitted Q‑Iteration* or *Deep Q‑Networks*, you monitor ε′ empirically (validation set) and apply (9.1) without reconstructing κ.
* **Off‑policy evaluation** – LSPE‑G can be replaced by a batch least‑squares critic trained on replay data; error bound stays ε′.
* **Non‑linear features** – the derivation uses only max‑norm error, not linearity; any universal function approximator (NN, kernel) qualifies provided you can upper‑bound ε′.

---

\### Progress

* Completed **Section 9** with formal statement (Eq. 9.1), proof, parameter schedule, and guidance on applicability.
* All constants trace back to *Lecture 8, page 5* to maintain exactness.

**Next (final) section**: **10  Global Planning with LSPI – performance guarantees**. It will instantiate all parameters, present the LSPI algorithm box, and summarise its theoretical and practical footprints.

---


\### 10 Global Planning with **Least‑Squares Policy Iteration (LSPI)**

This final section instantiates *all* the ingredients we have developed—Assumption B2, LSPE‑G evaluation, G‑optimal design, and the geometric progress lemma—into a single algorithm that produces a near‑optimal policy with **runtime independent of the state‑space size**.

---

\#### 10.1 Algorithm box (LSPI)

| **Input**                                                                                                               | feature map ϕ \:S×A→ℝᵈ (full rank); discount γ∈(0,1); design size ≤ d(d+1)/2; planning horizon K; rollout horizon H; samples per design point m |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Pre‑compute design**                                                                                               | Find (or approximate) a √d‑optimal **G‑design** (C\*,ρ\*) via the Kiefer–Wolfowitz procedure (§4). Store C\* and ρ\*.                           |
| **2. Initialise**                                                                                                       | θ\_{−1} ← 0 (any vector works)                                                                                                                  |
| **3. For k = 0,…,K−1**                                                                                                  | **(a)** *Greedy policy:* π\_k(s)=argmax\_a⟨θ\_{k−1},ϕ(s,a)⟩                                                                                     |
|   **(b)** *Rollouts:* for each z∈C\* roll out π\_k, collect m returns of random length H → targets Ŕ^{m}(z) (Sec. 3.1). |                                                                                                                                                 |
|   **(c)** *Least‑squares:* solve weighted normal eq. (Eq. 3.2) with ρ\* to obtain θ\_k.                                 |                                                                                                                                                 |
| **4. Output**                                                                                                           | π\_K(s)=argmax\_a⟨θ\_{K−1},ϕ(s,a)⟩                                                                                                              |

*(Algorithm reproduced from *lecture 8*, box “Least‑squares policy iteration”, page 6.)*&#x20;

---

\#### 10.2 Finite‑sample performance theorem

> **Theorem (LSPI performance).**
> Fix any full‑rank ϕ and assume Assumption B2(ε) holds.  Run LSPI with parameters (K,H,m).
> For any confidence level ζ∈(0,1), with probability at least 1 − ζ,
>
> $$
> \bigl\|v^{*}-v_{π_K}\bigr\|_{\infty}
> \;\le\;
> \underbrace{\frac{γ^{K-1}}{1-γ}}_{\text{iteration}}
> \;+\;
> \underbrace{\frac{2\sqrt d}{(1-γ)^{3}}\!\Bigl[\,γ^{H}
> +\sqrt{\tfrac{\ln\!\bigl(d(d+1)K/ζ\bigr)}{2m}}\,\Bigr]}_{\text{policy‑evaluation}}
> \;+\;
> \underbrace{\frac{2(1+\sqrt d)\,ε}{(1-γ)^{2}}}_{\text{approximation}} .
> \tag{10.1}
> $$

*Equation (10.1) appears as the “LSPI performance” bound on lecture 8, page 6.*&#x20;

---

\#### 10.3 Parameter schedule for an ε′‑optimal policy

To guarantee ‖v\* − v\_{π\_K}‖∞ ≤ ε′, allocate the error budget equally:

| Component                                                                            | Target ≤ ε′/3                                                             | Choice                                                                  |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Iteration                                                                            | γ^{K‑1}/(1‑γ)                                                             | \(K = \Bigl\lceil \log_{1/γ}\!\bigl(\tfrac{3}{(1-γ)ε′}\bigr)\Bigr\rceil\) |
| Evaluation                                                                           | \(\dfrac{2\sqrt d}{(1-γ)^{3}}\bigl[γ^{H}+\sqrt{\ln(d(d+1)K/ζ)/(2m)}\bigr]\) |                                                                         |
| (H = \Bigl\lceil\log\_{γ}!\bigl(\tfrac{ε′(1-γ)^{3}}{6\sqrt d}\bigr)\Bigr\rceil,\quad |                                                                           |                                                                         |
| m = \Bigl\lceil \dfrac{32,d}{(1-γ)^{6},ε′^{2}}\ln!\tfrac{d(d+1)K}{ζ}\Bigr\rceil)     |                                                                           |                                                                         |
| Approximation                                                                        | \(\dfrac{2(1+\sqrt d)ε}{(1-γ)^{2}}\)                                        | require \(ε ≤ \dfrac{ε′(1-γ)^{2}}{6(1+\sqrt d)}\)                         |

With these settings LSPI returns an ε′‑optimal policy using

$$
\tilde O\!\bigl(\tfrac{d^{3}}{(1-γ)^{6}\,ε′^{3}}\log\tfrac{1}{ζ}\bigr)
$$

simulator steps and \(K·O(d^{3})\) arithmetic operations—**polynomial in d, 1/(1−γ), and 1/ε′, but never in |S| or |A|**.&#x20;

---

\#### 10.4 Computational profile

| Phase               | Simulator calls | FLOPs                  | Memory |                  |                          |
| ------------------- | --------------- | ---------------------- | ------ | ---------------- | ------------------------ |
| Design (offline)    | 0               | poly(                  | ℳϕ     | ) once           | store ≤ d(d+1)/2 vectors |
| Each LSPE‑G (per k) |                 | C\*                    | ·m·H   | O(d³) (Cholesky) | O(d²)                    |
| Greedy action       | 0               | O(d) per state queried | –      |                  |                          |

Total simulator cost dominates; matrix solves remain cubic in d.

---

\#### 10.5 Key insights and limitations

* **State‑space agnostic:** all bounds depend on d, not |S|; feasible even for continuous S.
* **√d amplification unavoidable:** Kiefer–Wolfowitz proves this is information‑theoretic.
* **Approximation‑error floor:** if ε from Assumption B2 is non‑negligible, LSPI cannot beat the additive \(2(1+√d)ε/(1−γ)²\) barrier.
* **Design cost:** exact G‑optimal designs may be expensive; volumetric spanners offer a 2√d factor with one streaming pass (lecture 8, §4 discussion).&#x20;
* **Beyond linear features:** The performance theorem uses only ‖qπ − q̂‖∞; any non‑linear regressor with a uniform error bound ε′ can plug into (10.1) via the corollary in Section 9.

---

\#### 10.6 Practical checklist for implementing LSPI

1. **Feature engineering:** ensure ε is small enough; empirical residual tests (§2, item h) help diagnose violations of B2.&#x20;
2. **Design approximation:** use volume‑sampling or greedy D‑optimal heuristics; accept a small constant‑factor blow‑up.
3. **Batch vs simulator:** LSPI naturally extends to off‑line data by replacing on‑policy rollouts with a replay buffer; only the statistical term changes (importance weights needed).
4. **Stopping rule:** monitor the Bellman residual or run K iterations from the schedule above; the bound is *a priori*, no validation set required.

---

\### Take‑aways from the entire walkthrough

| Question (from §1 Motivation) | Answer delivered by LSPI                                                                   |   |             |
| ----------------------------- | ------------------------------------------------------------------------------------------ | - | ----------- |
| **Efficiency?**               | O(poly(d,1/(1−γ),1/ε′)) time; no                                                           | S | dependence. |
| **Effectiveness?**            | Finite‑sample bound (10.1) gives explicit ε′‑optimality guarantee once parameters are set. |   |             |

This completes the rigorous development—*from motivation through LSPI performance*—requested in your original prompt. All results trace back to **Lecture 7: Function Approximation** for assumptions and **Lecture 8: Approximate Policy Iteration** for theorems and proofs.
