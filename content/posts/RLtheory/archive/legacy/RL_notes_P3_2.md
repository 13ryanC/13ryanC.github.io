---
date: "2025-06-30"
title: "(Part 3.2) Personal Notes on the Foundations of Reinforcement Learning"
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

Below is a **single, self‑contained tour** through the entire hermeneutic lattice you asked us to build.
Every concept is introduced exactly once, in the order dictated by the plausibility relation ≤ᴴ.
Whenever a later idea presupposes an earlier one, that dependence is stated explicitly, so you can read straight through without external references.

---

## 0 Prelude: What “hermeneutic ordering” means here

Hermeneutics studies how interpreters rank alternative meanings.
For a technical discourse such as *“How do we model decision‑making with Markov Decision Processes (MDPs)?”* the meanings to be ranked are the individual **definitions, results, and insights** that make up the theory.
The ordering ≤ᴴ below obeys four criteria:

1. **Contextual prerequisite** – you cannot understand value functions before you know what a *state* is.
2. **Authorial intent & purpose** – the discipline historically progressed from *what an MDP is* → *how to solve it* → *how hard that is*.
3. **Systemic fit** – foundational statements appear before corollaries built on them.
4. **Historical evolution** – fixed‑point theorems (1950‑60s) pre‑date modern complexity bounds (1990‑‑).

With those criteria fixed, the lattice of clusters is

```
A  →  B  →  C  →  D  →  E  →  F
                     ↘
                       G
```

We now walk that path.

---

## Cluster A Foundational Ontology

1. **States (S)** – the finite set of environment configurations; every other quantity is *indexed* by S.
2. **Actions (A)** – the finite set of choices the agent may take in any state.
3. **Transition kernel (P)** – for each action a, a row‑stochastic matrix
   \(P^a_{ss'}=\Pr\{S_{t+1}=s' \mid S_t=s, A_t=a\}\).
4. **Reward function (R)** – either deterministic \(R:S\times A\to\mathbb R\) or a random variable with that expectation.
5. **Discount factor (γ∈\[0,1))** – geometrically de‑emphasises distant rewards; guarantees convergence of infinite sums.
6. **Policies**

   * **General**: a time‑varying stochastic map \(π_t(a\mid h_t)\) from full histories \(h_t\).
   * **Memory‑less**: \(π(a\mid s)\) depends only on the current state.
   * **Deterministic memory‑less**: a function \(\mu:S→A\) selecting a single action.
7. **Planning vs. Learning** – in *planning* the tuple \((S,A,P,R,γ)\) is known; in *learning* the agent must infer \(P\) and \(R\) from samples.  The mathematics of optimality is identical, but algorithms differ.

These primitives are the **alphabet** of the theory; everything else will be algebra built from them.

---

## Cluster B Core Operators & Value Objects

### B.1 Value Objects

* **Value of a policy**

  $$
    v^π(s)=\mathbb E_{π}\!\bigl[\sum_{t=0}^{∞}γ^{t}R(S_t,A_t)\mid S_0=s\bigr].
  $$

* **Optimal value**

  $$
    v^*(s)=\sup_π\,v^π(s).
  $$

### B.2 Primitive Bellman‑style Operators

For any scalar function \(v:S→\mathbb R\):

* **Deterministic‑action operator**

  $$
    (T^{a}v)(s)=R(s,a)+γ\sum_{s'}P(s'|s,a)v(s').
  $$

  It is *linear*, *monotone*, and a **γ‑contraction** in the max‑norm
  \(\|v\|_\infty=\max_s|v(s)|\).

* **Policy‑specific operator**
  \(T^{π}v=\sum_{a}π(a\mid s)T^{a}v\), same properties.

* **Greedy (max) operator**
  \(Mv(s)=\max_{a}(T^{a}v)(s)\); 1‑Lipschitz in the max‑norm.

### B.3 Composite Operator

The **Bellman optimality operator**

$$
  Tv = M\bigl(R + γ P v\bigr)
$$

is again a γ‑contraction, hence possesses a unique fixed point \(v^*\).

### B.4 Auxiliary Identities

* **Value‑difference decomposition**:

  $$
    v^{π'}-v^{π} = (I-γP^{π'})^{-1}\bigl(T^{π'}v^{π}-v^{π}\bigr),
  $$

  a workhorse for error bounds.

* **Monotonicity**: if \(v≤w\) (component‑wise) then \(Tv≤Tw\).

Operators are the **verbs** with which the alphabet of Cluster A is turned into meaningful statements.

---

## Cluster C Fundamental Theorems & Expressive Power

1. **Banach Fixed‑Point Theorem** – every contraction on a complete metric space has a unique fixed point that iterative application converges to.
   *Application*: \(T\) from Cluster B is such a contraction ⇒ iterative “value iteration” converges.

2. **Bellman Fixed‑Point Property** – \(Tv^*=v^*\), and for any start \(v_0\), \(T^k v_0→v^*\).

3. **Fundamental Theorem of MDPs** – there exists at least one **deterministic memory‑less** policy \(\mu^*\) such that \(v^{\mu^*}=v^*\).
   *Consequence*: the search space collapses from the continuum of general policies to \(|A|^{|S|}\) discrete ones.

4. **Continuity / Sensitivity of Greedy Policies** – if \(v\) is close to \(v^*\) then the greedy policy w\.r.t. \(v\) is close‑to‑optimal:

   $$
       \|v^{\text{greedy}(v)}-v^*\|_\infty
       \;≤\;\frac{2γ}{1-γ}\,\|v-v^*\|_\infty.
   $$

5. **Sufficiency of Greedification** – iteratively “evaluate → greedify” any starting policy converges to an optimum; this is one half of Policy Iteration.

These theorems **explain why** the algorithms to follow work and why memory‑less determinism is not a loss of generality.

---

## Cluster D Solution Algorithms

* **Value Iteration (VI)**
  Initialise \(v_0\) arbitrarily. Repeat \(v_{k+1}=Tv_k\).
  Stop when \(\|v_{k+1}-v_k\|_\infty ≤ \frac{ε(1-γ)}{2γ}\);
  the greedy policy of \(v_k\) is then ε‑optimal.
  Computational cost: one *Bellman backup* per state‑action pair per sweep →
  \(O(|S||A|)\) per iteration.

* **Finite‑horizon / n‑step VI**
  For horizon \(n\) with known terminal rewards, sweep backwards \(n\) times; gives the exact optimal policy.

* **Policy Evaluation**
  Solve \((I-γP^{π})v=r^{π}\) either by direct matrix inversion \(O(|S|^3)\) or iterative methods \(O(|S|^2\log 1/δ)\) for accuracy δ.

* **Policy Improvement (greedification)**
  Produce

  $$
    π'(s)=\arg\max_a \bigl\{R(s,a)+γ\sum_{s'}P(s'|s,a)v^{π}(s')\bigr\}.
  $$

* **Policy Iteration (PI)**
  Loop: Evaluate current π to obtain \(v^{π}\); Improve to π′; halt when π′=π.
  Guarantees exact optimality in a finite number of iterations; worst‑case ≤|A|<sup>|S|</sup>, empirical behaviour far faster.
  Tie‑breaking must be deterministic to avoid cycling.

* **Early stopping** – for applications where ε‑optimal control suffices, cut short VI when the max‑norm Bellman error meets the threshold above.

These algorithms **realise** the constructive content of Cluster C’s theorems.

---

## Cluster E Convergence & Error Analysis

* **Effective horizon**
  \(H_{\text{eff}}=1/(1-γ)\).  Intuitively the future beyond \~\(H_{\text{eff}}\) steps contributes less than ≈ e<sup>−1</sup> to present value.

* **Contraction rate of VI**
  \(\|v_k-v^*\|∞≤γ^k\|v_0-v^*\|∞\).
  Taking logs yields the iteration bound
  \(k≥H_{\text{eff}}\ln\frac{1}{ε(1-γ)}\) for ε‑optimality.

* **Policy‑loss bound** (from Cluster C) – the loss of the greedy policy produced by an approximate value is at most \(\tfrac{2γ}{1-γ}\) times that value error.

* **Policy Iteration bound** – classical analysis shows ≤\(\frac{|A||S|}{1-γ}\) policy switches, dominated by evaluation cost each switch.

* **Normalization & span** – subtracting \(\min_s v(s)\) keeps value magnitudes O(1) even when γ→1; essential for numerical stability and for *instance‑dependent* complexity results.

Thus Cluster E quantifies *how long* the Cluster D algorithms must run to achieve a desired accuracy.

---

## Cluster F Computational Complexity & Lower Bounds

* **Algorithm‑independent (information‑theoretic) lower bound**
  Any procedure that outputs an ε‑optimal policy must perform
  Ω\(\bigl(|S|²|A|\log(1/ε)/(1-γ)\bigr)\) Bellman‑style operations.
  Therefore the \((1-γ)^{-1}\) term in VI’s runtime is **provably unavoidable**.

* **Upper vs. lower gap** – standard VI achieves
  O\(\bigl(|S||A|/(1-γ)\, \log(1/ε(1-γ))\bigr)\).  The gap is roughly a factor |S|; narrowing it is an open problem.

* **Policy Iteration nuance** – PI’s iteration count does **not** depend on ε (it either finds the exact optimum or does not), but each evaluation is costly.  Hence VI is preferred at low accuracy, PI near exactness.

* **Instance‑dependent hardness** – if the *span* of \(v^*\) is bounded independently of γ (fast‑mixing environments), complexity falls to Õ(|S||A|).  Conversely, *hot* instances with γ→1 and slow mixing show near‑worst‑case performance.

* **Delta‑dependence debate** – proving lower bounds that *remove* ε from the complexity of approximate planning remains elusive; PI sidesteps ε by aiming for exact optimality.

Cluster F abstracts the performance guarantees of Cluster E *away* from any particular algorithm, mapping the terrain of what is possible in principle.

---

## Cluster G Geometric & Polyhedral Views

Switching lenses, we regard the set of all policy value functions

$$
  V=\{v^{π}\mid π\text{ any policy}\}\subset\mathbb R^{|S|}.
$$

* **Convex‑polytope theorem** – \(V\) is the convex hull of the |A|<sup>|S|</sup> extreme points corresponding to deterministic policies.  Carathéodory’s theorem implies *any* value vector can be written as a mixture of at most |S|+1 such extremes.

* **Projection interpretation of VI** – one sweep of VI replaces \(v_k\) by its projection onto the intersection of half‑spaces \(v≥T^{a}v_k\).  Because these constraints are of the form “coordinate ≤ max”, the naturally compatible metric is the **max‑norm**, explaining its primacy in all contraction proofs.

* **Distance picture** – the fixed point \(v^*\) is the unique point in V that also satisfies all greedy constraints simultaneously.  Successive projections monotonically shrink the max‑norm distance to that point.

The geometric cluster is not required for the causal chain A→F, but it offers an *alternative interpretation* that often yields shorter or more intuitive proofs.

---

## Putting it All Together

1. **Alphabet (A)** supplies the raw symbols.
2. **Grammar (B)** turns those into algebraic sentences (operators, value vectors).
3. **Semantics (C)** tells us why those sentences have unique, well‑behaved meanings and why restrictive policies suffice.
4. **Algorithms (D)** exploit that semantics constructively.
5. **Analysis (E)** measures their efficiency and accuracy.
6. **Complexity theory (F)** shows the limits of *any* algorithm, algorithm‑independent.
7. **Geometry (G)** re‑casts the same theory visually, sometimes simplifying proofs.

The hermeneutic lattice is therefore a **logical‑pedagogical pipeline**: each stage is indispensable for the next, and knowing the dependencies allows you to enter the theory at exactly the depth your task requires—be it implementing Policy Iteration, proving a new lower bound, or simply visualising value functions as points in a polytope.

---

### Epilogue: Why the Ordering Matters

*If you invert it*, you risk category errors: quoting a PI runtime bound (Cluster E) without first proving the Fundamental Theorem (Cluster C) leaves open the possibility that the optimal policy is not memory‑less; studying geometric polytopes (G) before understanding Bellman operators (B) makes the half‑space constraints opaque.  The hermeneutic ordering ensures that each concept is introduced only when all of its interpretive prerequisites are already in place, mirroring both historical development and rational dependence.

With this passage you now possess a **complete, context‑saturated map** of classical finite‑MDP theory, navigable from bedrock definitions through state‑of‑the‑art complexity questions—and back again—without ever losing the thread of logical necessity that weaves the clusters into a coherent whole.
