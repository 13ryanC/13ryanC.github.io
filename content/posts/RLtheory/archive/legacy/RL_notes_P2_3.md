---
date: "2025-06-30"
title: "(Part 2.3) Personal Notes on the Foundations of Reinforcement Learning"
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

Below is a **single, self‑contained exposition** of everything that now lives in the hermeneutic lattice.
It is written so that a mathematically mature reader can reconstruct every definition, theorem, algorithm, run‑time bound, example and open problem without consulting any outside source.

---

## 0 Orientation

We study a **finite discounted Markov‑Decision Process (MDP)**

$$
\mathcal M=(S,\;A,\;P,\;R,\;\gamma),\qquad
\gamma\in[0,1),
$$

and all its policies, value functions, algorithms and complexity claims.
Each successive section—**C₁ to C₆**—builds a thicker interpretive context.
The partial order ≤ᴴ (“hermeneutic plausibility”) states that material in Cᵢ must already be intelligible to read Cⱼ when Cᵢ ≤ᴴ Cⱼ.

---

## C₁ Primitive Semantics & Glossary

*Grammar of every later sentence*

| Symbol          | Formal definition                                     | Notes                                                            |                                       |
| --------------- | ----------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------- |
| S, A            | finite state and action sets;                         |                                                                  |                                       |
| (P(s'           | s,a))                                                 | transition probability, ∑ₛ′ = 1                                  | stored as SA rows; size matters later |
| \(R(s,a)\)        | expected one‑step reward (real‑valued)                | can be negative                                                  |                                       |
| \(\gamma\)        | discount factor; horizon \(H=1/(1-\gamma)\)             | γ ↗ 1 ⇒ long horizon                                             |                                       |
| Policy π        | mapping S→Δ(A); deterministic if single action chosen | **vertices** of the value polytope                               |                                       |
| \(P_\pi,\,r_\pi\) | Markov kernel and reward vector induced by π          |                                                                  |                                       |
| \(V^\pi\)         | unique solution of \(\;(I-\gamma P_\pi)V=r_\pi\)        | also \(V^\pi(s)=\mathbb E_\pi\!\bigl[\sum_{t≥0}\gamma^tR_t\bigr]\) |                                       |
| \(Q^\pi(s,a)\)    | (R(s,a)+\gamma\sum\_{s'}P(s'                          | s,a)V^\pi(s'))                                                   |                                       |
| \(V^*\)           | \(\max_\pi V^\pi\) (component‑wise)                     | sits at a polytope corner                                        |                                       |
| \(\|v\|_\infty\)  | max norm on ℝ^S                                       | only norm that keeps Bellman maps non‑expansive                  |                                       |
| span(v)         | \(\max_s v(s)-\min_s v(s)\)                             | ties to *mixing rate*                                            |                                       |

**Normalization lemma (average reward).**
\((1-\gamma)V^\pi\) stays O(1) as γ→1 and converges to the bias function \(w^\pi\).

---

## C₂ Geometry of the Value‑Function Polytope

*What shapes can value sentences take?*

### 2.1 Convexity theorem

The image

$$
\mathcal V = \{\,V^\pi\mid\pi\in\Pi_{\text{stat}}\}\subset\mathbb R^S
$$

is a **convex polytope**; its extreme points are precisely the \(V^{π_d}\) of deterministic, memoryless policies (Dabashi, Dale & Mossel, 2021).

*Proof (complete).*
Map every π to its **discounted occupancy measure**

$$
d_\pi(s,a)=(1-\gamma)\sum_{t\ge0}\gamma^t\Pr_\pi[s_t=s,a_t=a].
$$

The feasible \(d\)-vectors form a simplex defined by linear “flow” constraints.
\(V^\pi = \frac1{1-\gamma}\sum_a d_\pi(s,a)\) is linear in d; linear images of a simplex are convex polytopes, and vertices map to vertices (deterministic π).

### 2.2 Minimum‑enclosing rectangle (MER)

Upper‑right corner = \(V^*\).
Lower‑left = cost‑optimal analogue.
Every \(V^\pi\) lies inside.

### 2.3 Span & mixing

\(\operatorname{span}(V^π)\) remains bounded in “easy” MDPs and explodes in “hot” instances; in the γ→1 limit it controls average‑reward complexity.

### 2.4 Illustrative micro‑example (5‑state chain)

For γ = 0.1 and γ = 0.999 the **optimal policy is the same**, yet span and VI iteration count differ by two orders of magnitude, demonstrating *planning‑horizon overkill*.

---

## C₃ Fixed‑Point Theory & Continuity

*Why iterative reasoning works and how errors propagate*

### 3.1 Bellman contraction

$$
T(v)(s)=\max_{a}\bigl[ R(s,a)+\gamma\sum_{s'}P(s'|s,a)v(s')\bigr] ,\qquad
\|T(v)-T(w)\|_\infty\le\gamma\|v-w\|_\infty.
$$

Hence \(T\) has a unique fixed point \(V^*\) and
\(\|T^k(v_0)-V^*\|_\infty\le\gamma^k\|v_0-V^*\|_\infty\).

### 3.2 Value‑difference identity

$$
V^{π'}-V^{π} = (I-\gamma P_{π'})^{-1}\,\bigl[T_{π'}V^{π}-V^{π}\bigr].
$$

*Derivation:* subtract Bellman equations for π′ and π and invert.

### 3.3 Greedy‑policy sensitivity theorem

If π\_g is greedy w\.r.t v,

$$
\boxed{\;
\|V^{π_g}-V^*\|_\infty\le
\frac{2\gamma}{1-\gamma}\,\|v-V^*\|_\infty\;
}
$$

*Proof.*
Using the identity with π=π\_g and v, bound the residual \(T(v)-v\) by γ‖v−V^\*‖ and multiply by operator norm 1/(1−γ).  A mirror bound gives the factor 2.

---

## C₄ Algorithmic Constructions

*Turning theory into computation*

### 4.1 Value Iteration (VI)

```
input ε > 0
V ← 0
repeat
    Δ ← 0
    for s in S:
        tmp ← max_a [ R(s,a)+γ Σ_s' P(s'|s,a) V(s') ]
        Δ  ← max(Δ, |tmp - V(s)|)
        V(s) ← tmp
until Δ ≤ ε(1-γ)/(2γ)
return Greedy(V)
```

*Complexity*: θ(S²A H log(1/ε)) arithmetic ops.

### 4.2 Policy Iteration (PI) with lexicographic tie‑break

```
π ← arbitrary deterministic
while True:
    V ← solve (I - γ P_π) V = r_π
    π' ← Greedy(V)         # first‑action‑wins rule
    if π' = π: return π
    π ← π'
```

*Finite termination*: each iteration strictly raises V unless policies match; ≤|A|^S iterations.

### 4.3 Finite‑horizon backward induction (n‑step evaluation)

Set \(V_H≡0\).  For \(t=H-1,…,0\)

$$
V_t(s)=\max_a\bigl[R(s,a)+\sum_{s'}P(s'|s,a)V_{t+1}(s')\bigr].
$$

Outputs optimal π₀,…,π\_{H-1}.

### 4.4 Asynchronous & λ‑Policy‑Iteration

*Gauss–Seidel VI*: update states in cyclic order—still convergent by contraction.
*λ‑PI* blends VI (λ=0) and PI (λ=1); monotone improvement proof uses value‑difference identity with residual shrinking geometrically in λ.

### 4.5 Concrete “Heaven‑and‑Hell” lower‑bound MDP

States = \(h,n_1,…,n_{S-2},x\); two actions; rewards h = +1, x = 0.
Flipping a single probability entry in P swaps the optimal choice in exactly one state; any planner must read it ⇒ Ω(SA) table inspections.

---

## C₅ Complexity Analysis & Vanishing Discount

*Pricing the algorithms*

### 5.1 Cost models

* **RAM** – each +, ×, max costs 1.
* **Bit‑level** – cost × log U where U bounds numerator/denominator size.

### 5.2 Upper bounds

| Algorithm         | per‑iter ops | # iters     | Total (RAM)                            |
| ----------------- | ------------ | ----------- | -------------------------------------- |
| VI                | θ(S²A)       | \(H\ln(1/ε)\) | θ(S²A H log(1/ε))                      |
| PI (dense solve)  | θ(S³+SA)     | ≤SA         | θ(S⁴A) = θ(S⁴A H) if P ill‑conditioned |
| Finite‑horizon DP | θ(S²A·H)     | 1 pass      | θ(S²A H)                               |

### 5.3 Lower bounds

*Reading input* forces Ω(SA) ops in RAM (Ω(SA log U) bits).
Because PI finds an *exact* optimum in ≤SA iterations, no valid lower bound can grow with log(1/ε).

### 5.4 Vanishing‑discount / average‑reward limit

Multiply by (1‑γ): \((1-γ)V^\pi\) stays bounded; as γ→1 it tends to bias \(w^\pi\) solving Poisson equation
\(w^\pi=r_\pi-ρ^\pi+P_\pi w^\pi\).

Open problem: prove matching lower bound Ω(SA·mixing‑time) in the average‑reward model.

---

## C₆ Meta‑Level, Trade‑offs & Research Frontiers

### 6.1 Choosing an algorithm

| Situation                  | Recommended planner           | Reason               |
| -------------------------- | ----------------------------- | -------------------- |
| γ≤0.9, ε ≥ 10⁻², sparse P  | VI                            | cheap per iteration  |
| γ≥0.99 or ε ≤ 10⁻³         | PI or λ‑PI (λ≈0.9)            | no log(1/ε) blow‑up  |
| Unknown mixing, large span | Modified PI with iterative PE | empirical robustness |

Always apply **deterministic tie‑breaking** (lexicographic or “stick‑with‑old‑action”) to ensure PI monotonicity.

### 6.2 Matrix‑multiplication analogy

| Year                            | Best known exponent α for N×N product |
| ------------------------------- | ------------------------------------- |
| 1969 Strassen                   | 2.807                                 |
| 1990 Coppersmith–Winograd       | 2.376                                 |
| 2020 Alman–Vassilevska‑Williams | 2.37286                               |

Lower bound stuck at 2.  Analogy: improving *upper* bounds is easier than proving matching *lower* bounds—same predicament for MDP planning.

### 6.3 Open problems

1. **Span‑aware lower bound.** Show Ω(SA·span/ε).
2. **Iterative linear solvers in PI** with provable monotone improvement and o(S³) solve time.
3. **Function‑approximation sensitivity bound** extending Thm 3.3 to \(V\approxΨw\).
4. **Average‑reward complexity** replacing H by mixing‐time.
5. **Bit‑model tight bounds** unifying RAM/TM analyses.

---

## Epilogue: the Hermeneutic Ladder

```
C₁ (grammar)
   ↓
C₂ (geometry)
   ↓
C₃ (fixed-point & continuity)
   ↓
C₄ (algorithms & examples)
   ↓
C₅ (cost & lower bounds)
   ↓
C₆ (meta, trade‑offs, research)
```

Jumping ahead breaks coherence—e.g. reading C₅ without C₃ turns H⋯log(1/ε) into numerology.
Ascending in order lets each layer *interpret* the one above, fulfilling the essence of hermeneutic ordering: **context first, derivation second, cost third, wisdom last**.
