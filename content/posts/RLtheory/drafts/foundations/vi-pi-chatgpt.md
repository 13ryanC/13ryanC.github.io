---
date: "2025-07-02"
title: "(Part 2) Dynamic Programming: Value vs Policy Iteration"
summary: "Two classic planning algorithms for solving known MDPs. Present VI/ PI side by side; prove convergence rates, complexity"
category: "Tutorial"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero4.png
image: /assets/images/card4.png
---

## TL;DR

**Value Iteration (VI)**: Repeatedly applies the Bellman optimality operator until the value function converges. Memory-light but can require many sweeps.

**Policy Iteration (PI)**: Alternates between *policy evaluation* and *policy improvement*; converges in finite iterations. Sample-efficient but each iteration requires solving a linear system.

Both exploit **dynamic programming** principles. Under standard assumptions (finite \(S\), \(A\), \(\gamma<1\)), both return an optimal deterministic policy.

| Algorithm | Convergence Rate | Ops per Sweep | Total Ops for \(\delta\)-Optimal \(\pi\) |
|-----------|------------------|---------------|-------------------------------------|
| **Value Iteration** | \(\lVert v_k-v^*\rVert_\infty\leq\gamma^{k}\lVert v_0-v^*\rVert_\infty\) | \(\tilde O(S^2A)\) | \(\tilde O \big(S^2A\frac{1}{1-\gamma}\log \frac{1}{\delta}\big)\) |
| **Policy Iteration** | Geometric + eliminates ≥1 bad action every \(H_\gamma\) iterations | \(\tilde O(S^3+SA)\) | \(\tilde O \big(\frac{SA}{1-\gamma}\big)\) iterations |

**Trade-off**: VI is simple and memory-efficient; PI takes fewer outer iterations but each is more expensive (matrix solve). For large sparse \(S\), VI's sweeps may be cheaper; for high accuracy or strong polynomial guarantees, PI wins.

---

## 1. Mathematical Foundation

When the full MDP \(\langle S,A,P,R,\gamma\rangle\) is known, planning reduces to solving the Bellman optimality fixed-point:

$$
v^*(s)=\max_{a}\Bigl\{R(s,a)+\gamma\sum_{s'}P(s'|s,a)\,v^*(s')\Bigr\}
$$

### Bellman Operators

**Policy operator**: 
$$T_\pi v = R_\pi + \gamma P_\pi v, \qquad R_\pi(s)=\sum_a \pi(a|s)R(s,a)$$

**Optimality operator**: 
$$(Tv)(s)=\max_{a}\bigl\{R(s,a)+\gamma\langle P(s,a),v\rangle\bigr\}$$

Both are \(\gamma\)-contractions in \(\|\cdot\|_\infty\), with \(T\)'s unique fixed point being \(v^*\).

**Greedy map**: \(\Gamma(v)=\arg\max_a R(s,a)+\gamma \langle P(s,a),v\rangle\)

### Key Policy Error Bound
For any vector \(v\) and greedy policy \(\pi=\Gamma(v)\):
$$v^*-v_\pi \leq \frac{2\gamma}{1-\gamma}\,\lVert v^*-v\rVert_\infty\;1 \tag{★}$$

This shows that *near-optimal values ⇒ near-optimal greedy policies*.

---

## 2. Value Iteration

```pseudo
v ← 0
repeat
    v ← Tv          # synchronous Bellman backup
until max_s |Δv(s)| ≤ ε(1−γ)/2
π̂ ← Γ(v)            # output greedy policy
```

**Per-sweep cost**: \(\Theta(S^2A)\) operations with random-access tables.

**Iterations needed**: \(k \geq \frac{\ln(1/\varepsilon(1-\gamma))}{1-\gamma}\) to make greedy \(\pi\) be \(\varepsilon\)-optimal.

**Total complexity**: \(\tilde O\big(S^2A\frac{1}{1-\gamma}\ln\frac{1}{\delta}\big)\) for \(\delta\)-optimal policy.

### Relative-Error Stopping
Stop when \(\lVert v_k-v_{k-1}\rVert_\infty \leq \frac{\delta(1-\gamma)}{2\gamma}\max_s|v_k(s)|\) to ensure \(v_{\Gamma(v_k)} \geq (1-\delta)v^*\).

---

## 3. Policy Iteration

```pseudo
π ← arbitrary deterministic policy
repeat
    # (i) exact evaluation
    solve v ← (I − γP_π)⁻¹ r_π       # cost ≈ O(S³)
    # (ii) greedy improvement
    for s in S:
        π_new(s) ← argmax_a [R(s,a)+γ P(s,a)·v]
    until π_new = π
    π ← π_new
```

### Convergence Properties

1. **Geometric progress**: \(v_{\pi_{k+1}} \geq T v_{\pi_k} \geq v_{\pi_k}\) implies \(\|v_{\pi_k}-v^*\|_\infty \leq \gamma^k\|v_{\pi_0}-v^*\|_\infty\)

2. **Strict progress**: After one horizon \(H_\gamma=\lceil\ln 1/(1-\gamma)\rceil\) iterations, at least one suboptimal action is forever discarded, guaranteeing finite termination in at most \((SA-S)\) improvements.

**Total complexity**: \(\tilde O\bigl((S^3+SA)\,\frac{SA-S}{1-\gamma}\bigr)\) operations, but only \(\tilde O\bigl(\frac{SA}{1-\gamma}\bigr)\) iterations (independent of \(\delta\)) — hence **strongly polynomial** for fixed \(\gamma\).

---

## 4. Modified Policy Iteration

Interpolates between VI and PI by evaluating for \(m\) Bellman sweeps then improving. Choosing \(m\) balances iteration count versus per-iteration cost.

---

## 5. Theoretical Limitations

### Computational Lower Bounds
Any algorithm returning a deterministic \(\delta\)-optimal policy must read \(\Omega(S^2A)\) numbers, proven by needle-in-a-haystack constructions.

### Value Iteration's Infinite Complexity
**Proposition (Feinberg–Huang–Scherrer '14)**: For a 3-state deterministic MDP, there exists a reward function such that VI initialized at \(v_0=0\) **never** switches a suboptimal action — its iteration complexity is *infinite*.

Thus VI is not strongly polynomial, whereas PI is.

---

## 6. Practical Guidelines

| Scenario | Recommendation | Rationale |
|----------|----------------|-----------|
| **Small \(S\) (≤ 10³)** | Policy Iteration | Few iterations, exact solve cheap |
| **Large, sparse \(S\)** | Value Iteration or Asynchronous variants | Matrix factorization prohibitive |
| **Need finely-tuned \(\pi\)** | Modified PI with small \(m\) | Faster asymptotics than VI, cheaper than PI |
| **Function approximation** | Generalized PI (GPI) | Both VI & PI become approximate; stability matters |

**Diagnostics**: Monitor \(\Delta v_k\) for VI; for PI, test whether greedy improvement changes any \((s,a)\).

---

## References

- Singh & Yee 1994 – tight policy-error bound in Eq. (★)
- Ye 2011 – first strongly polynomial bound for PI
- Scherrer 2016 – simplified proof & better constants
- Chen & Wang 2017 – complexity lower bounds under different input encodings

---

*Part 3* will extend DP to **approximate** settings and large-scale function approximation.
