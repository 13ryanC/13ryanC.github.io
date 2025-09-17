---
date: "2025-06-30"
title: "(Part 3.3) Personal Notes on the Foundations of Reinforcement Learning"
summary: "Aim to provide more insight on RL foundations for beginners"
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

# Comprehensive Notes on Finite Discounted Markov‑Decision Processes

*(A hermeneutically ordered, fully‑expanded synthesis of the entire lecture bundle)*

---

## Table of Contents

1. **Administrative & Pedagogical Frame**
2. **Cluster 1 Foundational Ontology**
3. **Cluster 2 Policies & Value Vocabulary**
4. **Cluster 3 Bellman Operators & Fixed‑Point Logic**
5. **Cluster 4 Fundamental Theorem of MDPs**
6. **Cluster 5 Algorithms**

   * 5.1 Value Iteration (VI)
   * 5.2 Policy Iteration (PI)
7. **Cluster 6 Complexity Theory of Planning**
8. **Cluster 7 Error Metrics & Engineering Trade‑offs**
9. **Cluster 8 Peripheral but Insight‑Bearing Topics**
10. **Glossary (all terms in one place)**
11. **Worked Quiz & Essay Prompts**

Each section is self‑contained yet positioned in the **≤ᴴ hermeneutic lattice**: earlier sections supply the conceptual premises on which later sections depend.

---

## 1 Administrative & Pedagogical Frame  ▣ (A‑1, A‑2, B‑1, B‑2)

* **Course cadence** | Assignment 0 solutions released; Assignment 1 due in two weeks.
* **Channels** | Slack for Q\&A; lecture notes posted on course website; project description forthcoming.
* **Learning agenda** | (i) Recap & computational questions, (ii) Policy Iteration, (iii) Inherent complexity.
* **Assessment material** | Ten short‑answer quiz items and five essay prompts appear in § 11.

*These meta‑data do not affect technical proofs but explain why the exposition periodically pauses for “quiz”, “essay”, or “project” sign‑posts.*

---

## 2 Cluster 1 – Foundational Ontology of an MDP

### 2.1 Formal Definition

A **finite discounted MDP** is the quintuple

$$
\mathcal M=(S,A,P,R,\gamma),
\quad\gamma\in(0,1).
$$

| Symbol   | Minimal definition                                                                 | Historical note                                                |
| -------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| \(S\)      | finite set of **states**                                                           | Adopted from Markov chains (Andrey Markov, 1913).              |
| \(A\)      | finite set of **actions**                                                          | Appears in Howard (1960).                                      |
| \(P\)      | transition kernel \(P(\cdot\mid s,a)\in\Delta(S)\)                                   | *Stochastic matrix:* each row sums to 1.                       |
| \(R\)      | reward function \(R:S\times A\times S\to\mathbb R\) (*or* \(R:S\times A\to\mathbb R\)) | Utility notion from economics.                                 |
| \(\gamma\) | **discount**                                                                       | Guarantees bounded geometric series; reflects time preference. |

### 2.2 Why γ < 1?

Without discounting and with non‑negative rewards, value functions can diverge.  Most contraction‑based proofs require \(\gamma<1\) to ensure a fixed point exists.

---

## 3 Cluster 2 – Policies & Value Vocabulary

### 3.1 Policy Classes

| Type                            | Symbol  | Map                        |
| ------------------------------- | ------- | -------------------------- |
| **Memory‑less**                 | \(\pi\)   | \(S\to\Delta(A)\)            |
| **Deterministic**               | \(\pi_d\) | \(S\to A\)                   |
| **General (history‑dependent)** | \(\Pi\)   | \(H_t=(SA)^tS \to\Delta(A)\) |

> **Planning vs Learning Sidebar ▣ (H‑2)**
> *Planning* assumes \(P,R\) known; sufficiency of memory‑less deterministic policies holds. *Learning* (unknown model) needs history for exploration and credit assignment.

### 3.2 Value Function

Given policy \(\pi\) and start state \(s\),

$$
V^\pi(s)=\mathbb E\!\Bigl[\sum_{t=0}^{\infty}\gamma^{t}R(S_t,A_t,S_{t+1})\Bigr].
$$

**Max‑norm ▣ (C‑3)** \(\|V\|_\infty=\max_{s\in S}|V(s)|\) is the metric used for contractions.

### 3.3 Reduction Lemma (Memory‑less Suffices)

*Statement.* For known \(P,R\) and \(\gamma<1\) there exists a deterministic memory‑less policy \(\pi_d\) achieving \(V^{\pi_d}=V^*:=\sup_\Pi V^\Pi\).

*Proof sketch.* At each state \(s\) pick \(a^*(s)\in\arg\max_a Q^\Pi(s,a)\) where \(Q^\Pi\) is the action‑value under any candidate optimal policy.  Replacing the stochastic/history rule by \(a^*(s)\) never decreases value (monotonicity of Bellman operator). Apply for all states.

---

## 4 Cluster 3 – Bellman Operators & Fixed‑Point Logic

### 4.1 Operators

*Policy evaluation*

$$
(T_\pi V)(s)=\sum_{a}\pi(a\!\mid\!s)\Bigl[R(s,a)+\gamma\sum_{s'}P_{s,a,s'}\,V(s')\Bigr].
$$

*Optimality*

$$
(TV)(s)=\max_{a}\Bigl[R(s,a)+\gamma\sum_{s'}P_{s,a,s'}\,V(s')\Bigr].
$$

### 4.2 Structural Properties

* **Monotonicity** \(V\le W\Rightarrow T_\pi V\le T_\pi W,\;TV\le TW\).

* **γ‑Contraction** \(\|T_\pi V-T_\pi W\|_\infty\le\gamma\|V-W\|_\infty\) and likewise for T.

* **Pull‑out‑Constant Lemma ▣ (D‑1)**

  $$
  T_\pi(V+c\mathbf 1)=T_\pi V+\gamma c\mathbf 1,\quad T(V+c\mathbf 1)=T V+\gamma c\mathbf 1.
  $$

  *Proof.* Row sums of stochastic matrix equal 1.

* **Non‑linear Contraction Proof ▣ (D‑2)**
  For T, note

  $$
  |TV(s)-TW(s)|\le\max_a\gamma\sum_{s'}P_{s,a,s'}|V-W|(s')\le\gamma\|V-W\|_\infty.
  $$

### 4.3 Banach Fixed‑Point Theorem

Any γ‑contraction on the complete metric space \((\mathbb R^{|S|},\|\cdot\|_\infty)\) has a **unique** fixed point; iterating the map converges at rate γⁿ.

*Applications* \(T_\pi\) ↦ \(V^\pi\); \(T\) ↦ \(V^*\).

---

## 5 Cluster 4 – Fundamental Theorem of MDPs

### 5.1 Statement

1. (*Greedy sufficiency*) If \(\pi\) is greedy w\.r.t. \(V^*\) then \(V^\pi=V^*\).
2. (*Bellman fixed‑point*) \(V^*=T V^*\).

### 5.2 Proof

*Part 1.* See reduction argument in previous answer; key steps: \(V^\mu\le TV^*\), monotonicity, contraction.

*Part 2.* Because greedy \(\pi\) satisfies \(T_\pi V^*=T V^*\) and \(V^\pi\!=\!T_\pi V^\pi\!=\!V^*\), substitute to obtain \(V^*=T V^*\).

> **Footnote ▣ (H‑1)** Once \(V^*\) is known, greedifying is a table look‑up—computationally cheap relative to computing \(V^*\).

---

## 6 Cluster 5 – Algorithms

### 6.1 Value Iteration (VI)

**Algorithm.** Initialise \(V_0\) (e.g., 0). Iterate \(V_{k+1}=T V_k\).

**Convergence.** \(\|V_k-V^*\|_\infty\le\gamma^k\|V_0-V^*\|_\infty\).

**Policy Loss Bound ▣ (E‑1)**
If \(\|V_k-V^*\|_\infty\le\varepsilon\) and \(\pi_k\) is greedy w\.r.t \(V_k\), then

$$
V^*-V^{\pi_k}\le\frac{2\varepsilon}{1-\gamma}.
$$

*Proof.*

1. \(V^{\pi_k}=T_{\pi_k}V^{\pi_k}\le T_{\pi_k}V_k+\gamma\|V_k-V^{\pi_k}\|_\infty\).
2. \(T_{\pi_k}V_k=TV_k\ge V_k\). Combine, bound recursively, sum geometric series.

### 6.2 Policy Iteration (PI)

**Algorithm.**

1. Evaluate \(V_k=(I-\gamma P_{\pi_k})^{-1}R_{\pi_k}\).
2. Improve \(\pi_{k+1}(s)=\arg\max_a Q_{V_k}(s,a)\).
3. Stop if \(\pi_{k+1}=\pi_k\).

**Monotone improvement.** \(V_{\pi_{k+1}}\ge V_{\pi_k}\).

**Elimination Lemma ▣ (E‑2)**
After

$$
k^*=\Big\lceil \frac{\log(SA/(1-\gamma))}{\log\bigl(\frac1{1-\gamma}\bigr)} \Big\rceil
$$

iterations, at least one state‑action pair used by \(\pi_0\) is never selected again.  Hence PI terminates after \(O\!\bigl(\tfrac{SA}{1-\gamma}\log\tfrac{SA}{1-\gamma}\bigr)\) iterations (Ye–Inan–Wang, 2017).

---

## 7 Cluster 6 – Complexity Theory

### 7.1 Upper‑Bound Summary

| Alg. | Cost/iter | # Iters                                         | Total                                                  |
| ---- | --------- | ----------------------------------------------- | ------------------------------------------------------ |
| VI   | Θ(S²A)    | Θ\bigl(\frac{\log1/\varepsilon}{1-\gamma}\bigr) | Θ\bigl(\frac{S²A}{1-\gamma}\log\frac1\varepsilon\bigr) |
| PI   | Θ(S³)     | poly\(\frac{SA}{1-\gamma}\)                       | Θ(S³·poly(SA/(1-γ)))                                   |

### 7.2 Lower Bound Ω(S²A) – “Heaven/Hell” Construction ▣ (F‑1)

Let \(S= \{1,\dots,S-2,\ \text{Heaven},\ \text{Hell}\}\).
For each regular state \(i\) choose one distinguished action \(a_i^*\):

* \(P(\text{Heaven}\mid i,a_i^*)=1\), reward = 1.
* All other actions go deterministically to *Hell*, reward = 0.
* Heaven returns to itself with reward 1; Hell self‑loops with 0.

Identifying all \(a_i^*\) is equivalent to reading S·A table entries; proving optimality for **every** state costs Ω(S²A).

### 7.3 Open Question 1/(1‑γ) Dependence ▣ (C‑2)

No lower bound yet includes the effective‑horizon factor.  Is it artefact or inherent?  Open.

---

## 8 Cluster 7 – Error Metrics & Engineering Trade‑offs

### 8.1 Absolute vs Relative

*Absolute ε:* uniform additive bound.
*Relative ρ:*

$$
\frac{|V^{\pi}(s)-V^*(s)|}{|V^*(s)|}\le\rho.
$$

### 8.2 Why Relative Error Is Hard ▣ (G‑1)

Let γ = 0.99, rewards ≈ 10⁻³ so \(V^*\approx10^{-1}\).  To keep ρ = 1 % you need ε ≈ 10⁻³, inflating policy‑loss bound by \(\tfrac{2}{1-\gamma}=200\).  Practical algorithms seldom justify such precision.

### 8.3 Engineering Recipe

| Domain                     | Recommended method                    |
| -------------------------- | ------------------------------------- |
| Real‑time game AI          | VI to ε≈10⁻²(1–γ) then greedify.      |
| Safety‑critical (avionics) | Exact PI or LP.                       |
| Very large MDP             | Model‑free RL; accept sampling noise. |

---

## 9 Cluster 8 – Peripheral but Insight‑Bearing Topics

### 9.1 Effective Horizon \(H\approx\lceil\frac1{1-\gamma}\rceil\)

Rewards after H steps contribute ≤ e⁻¹ to value; rollouts can truncate safely.

### 9.2 Small‑S Exhaustive Search

For fixed |S| = m, enumerate all \(|A|^m\) deterministic policies, solve \(m\times m\) linear systems, pick best.  Runtime independent of \(1/(1-\gamma)\).

### 9.3 History Sufficiency in Learning

In unknown MDPs policies must encode exploration: optimism, posterior sampling, etc.  Memory‑less sufficiency collapses.

---

## 10 Glossary (complete)

* **Action (A)** Choice available in a state.
* **Banach Fixed‑Point Theorem** Contraction → unique fixed point, geometric convergence.
* **Bellman Operators** \(T_\pi,\,T\).
* **Contraction Mapping** Lipschitz constant \(<1\).
* **Discount γ** Temporal weighting factor.
* **Effective Horizon** ≈ \(1/(1-\gamma)\).
* **Geometric Rate** Error shrinks by factor γ each iteration.
* **Max‑norm** \(\|v\|_\infty=\max_s|v(s)|\).
* **Monotonicity** Order preservation under \(T_\pi,T\).
* **Policy (memory‑less / deterministic / general)** See § 3.
* **Stochastic Matrix** Row‑stochastic transition matrix (\(\sum_{s'}P_{s,a,s'}=1\)).
* **Value Function \(V^\pi,V^*\)** Expected discounted return.

*(Every other glossary item from the original notes is subsumed in the text above.)*

---

## 11 Quiz & Essay Prompts (with brief keys)

### 11.1 Ten Short‑Answer Questions

1. **List the five‑tuple defining an MDP.** → S,A,P,R,γ.
2. **Memory‑less vs general policy?** Dependence on current state vs full history; optimal planning needs only memory‑less.
3. **State the Fundamental Theorem.** Greedy w\.r.t \(V^*\) is optimal; \(V^*=TV^*\).
4. **Role of \(T\).** One‑step look‑ahead maximiser; fixed point is \(V^*\).
5. **Why does VI converge?** T is a γ‑contraction; Banach theorem.
6. **Iteration complexity of VI?** \(O\!\bigl(\frac{\log 1/\epsilon}{1-\gamma}\bigr)\).
7. **Two steps in PI.** Policy evaluation + improvement.
8. **Major advantage of PI.** Finite‑step exact optimality.
9. **Meaning of 1/(1‑γ).** Effective planning horizon.
10. **Why need monotonicity & contraction in proofs?** Preserve inequalities; guarantee convergence.

### 11.2 Essay Prompts (outline answers)

1. **Compare VI & PI.** Trade accuracy vs per‑iteration cost; VI approximate geometric; PI exact finite.
2. **Explain Banach’s role.** Contraction → unique fixed point & geometric convergence.
3. **Two parts of Fundamental Thm.** Memory‑less sufficiency; V\* fixed point; foundation for PI.
4. **Influence of γ.** Controls horizon, complexity, error blow‑up.
5. **Exact vs approximate.** Exact costly (matrix inversion); approximate adequate when reward scale large.

---

### Final Schematic

```
S,A,P,R,γ ─→ Policy/Value ─→ Bellman Ops ─→ Fundamental Thm
                                   │              │
                                   ▼              ▼
                         Algorithms (VI, PI) ─→ Complexity
                                   │
                                   ▼
                Pragmatics / Approximation Trade‑offs
                                   │
                                   ▼
               Horizon | Small‑S Enumeration | Exploration
```

The arrows denote logical and explanatory precedence; each node now incorporates **all content**—definitions, lemmas, proofs, examples, anecdotes, administrative notes, quizzes—that appeared anywhere in the original lecture material.
