---
date: "2025-06-30"
title: "Span of value function and mixing rate"
summary: "Span of value function and mixing rate"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

Below I explain, in a step‑by‑step (multi‑hop) fashion, why the **span of the (relative‑)value/bias function, `sp(h)`, is regarded as a more fundamental complexity measure for Markov‑decision‑process (MDP) learning and planning than any “mixing‑rate’’ or “mixing‑time’’ parameter.**

---

## 0.  Formal background and notation

| symbol                                   | definition (finite state–action MDP)                                               |
| ---------------------------------------- | ---------------------------------------------------------------------------------- |
| `P_π`                                    | transition matrix of the Markov chain induced by stationary policy π               |
| `τ(π)`                                   | *mixing time* of `P_π` (smallest `t` s.t. ‖P\_π^t(s,·) – μ\_π‖₁ ≤½ for all states) |
| `τ_unif`                                 | `sup_π τ(π)` – a *uniform* mixing bound required by many analyses                  |
| `ρ_π`                                    | long‑run average reward of π                                                       |
| `h_π`                                    | **bias/relative‑value function** solving the Poisson equation                      |
|   `ρ_π + h_π(s) = r_π(s) + (P_π h_π)(s)` |                                                                                    |
| `sp(h)`                                  | **span seminorm** `sp(h) ≜ max_s h(s) – min_s h(s)` (translation‑invariant)        |

We focus on weakly‑communicating MDPs, where `sp(h_π)` is always finite, while `τ(π)` can be ∞.

---

## 1.  Sub‑question A   What makes `sp(h)` mathematically “primary”?

### A1.  It is the **natural contraction modulus** of Bellman operators

The Bellman optimality operator `T` is **1‑Lipschitz in the span seminorm** even in average‑reward problems:

```
sp(T v – T w)  ≤  sp(v – w).
```

Hence value iteration, Q‑learning, policy evaluation, etc. converge at a rate dictated by `sp(·)` without *any* stochastic‑mixing assumption ([proceedings.neurips.cc][1]).  No comparable universal contraction holds under total‑variation or Euclidean norms that underlie mixing‑time analyses.

### A2.  It is **reward‑scale and policy independent**

`sp(h)` depends only on differences of long‑run values across states; adding a constant to all rewards leaves it unchanged.  In contrast, a mixing rate is purely a property of a *single* Markov chain and ignores rewards altogether.  When rewards change, learning difficulty changes proportionally to `sp(h)` but `τ` is unaffected—a sign that `sp(h)` is closer to the optimisation objective.

---

## 2.  Sub‑question B   Limitations of mixing‑time parameters

* **Non‑existence/∞ values.**  If *one* policy is periodic or non‑ergodic, `τ_unif = ∞`; most mixing‑based algorithms then have vacuous guarantees.  `sp(h)` remains finite whenever optimal bias is finite (weakly communicating MDPs).
* **Over‑conservativeness.**  Optimal policies often mix much faster than the worst‑case `τ_unif`; nevertheless those algorithms must size their confidence intervals for the larger quantity, leading to loose bounds.
* **Incomparability.**  “Fast mixing’’ does not imply low span.  A one‑state reward‑sensitive MDP has `τ(π)=0` yet an arbitrarily large `sp(h)` if rewards differ greatly between actions.

---

## 3.  Sub‑question C   Provable relationships show `sp(h)` is a tighter yard‑stick

For any weakly‑communicating MDP

```
sp(h_*) = H   ≤   8·τ_*   ≤   8·τ_unif   and   H ≤ D
```

where `τ_*` is the *smallest* mixing time over optimal policies and `D` is the diameter ([arxiv.org][2], [openreview.net][3]).
Thus every uniform‑mixing or diameter‑based guarantee translates into an *equal or stronger* span‑based guarantee, but **not vice‑versa**, establishing `H` as the more granular quantity.

---

## 4.  Sub‑question D   Algorithmic evidence

| result                                          | assumption                         | sample‑complexity upper bound | remark                                                                            |
| ----------------------------------------------- | ---------------------------------- | ----------------------------- | --------------------------------------------------------------------------------- |
| Zurek & Chen 2024                               | *none beyond weakly communicating* | `Õ(SA·H/ε²)`                  | **minimax‑optimal** in `H` and dominates all mixing‑based bounds ([arxiv.org][2]) |
| Prior work (e.g. Bartlett & Tewari; Jin et al.) | requires finite `τ_unif`           | `Õ(SA·τ_unif/ε²)`             | vacuous when `τ_unif=∞`, looser when `H ≪ τ_unif` ([arxiv.org][2])                |

Similar improvements hold for discounted MDPs (`Õ(SA·H/(1–γ)²ε²)` vs the classic `Õ(SA/(1–γ)³ε²)`) and for regret bounds in online RL.  These advances were possible only after abandoning mixing in favour of span.

---

## 5.  Sub‑question E   Concrete counter‑example

> **Deterministic 2‑state rotor**
>
> * State 1  → State 2 → State 1 (period 2, no randomness).
> * Rewards: `r(1)=0`, `r(2)=1`.
> * Any policy inherits the period‑2 chain ⇒ **no mixing** (`τ_unif = ∞`).
> * Bias solves `h(1)=0`, `h(2)=1` ⇒ `sp(h)=1`.

All span‑based algorithms learn optimally in `Õ(SA/ε²)` samples, whereas mixing‑time based algorithms give no guarantee at all—perfectly illustrating the superiority of `sp(h)`.

---

## 6.  Putting it together – why span is “more fundamental”

1. **Universal contraction & convergence.**  Span is the metric under which Bellman dynamics behave; mixing is not needed for this fixed‑point theory.
2. **Always finite, policy‑agnostic.**  Guarantees in `H` apply to every weakly‑communicating MDP, whereas mixing‑based guarantees break the moment ergodicity fails.
3. **Tighter & minimax‑exact bounds.**  `H` upper‑bounds all traditional parameters (`D`, `τ_unif`), permitting sharper sample‑ or regret‑complexity results, and these bounds have matching lower bounds.
4. **Aligned with the control objective.**  Learning difficulty arises from *value variation* across states; `sp(h)` measures exactly that.  Mixing measures only how quickly *state distributions* forget the past—important in Markov‑chain theory but secondary for decision‑making.

Hence, both mathematically and algorithmically, **`sp(h)` supplies the minimal, reward‑relevant information needed to quantify and attain optimal learning performance, while mixing rates are a coarser, sometimes ill‑defined proxy.**

---

### Residual uncertainties & suggested tests

*In practice*, span is unknown; algorithms must estimate or adapt to it.  Recent works design span‑free confidence sets or doubling‑trick schedulers—empirical validation on large tasks remains limited.  A worthwhile experiment is to compare span‑adaptive and mixing‑based algorithms on MDPs where `H ≪ τ_unif` (e.g., sparse‑reward cyclic mazes) to quantify the practical sample‑efficiency gap.

[1]: https://proceedings.neurips.cc/paper/2021/file/096ffc299200f51751b08da6d865ae95-Paper.pdf?utm_source=chatgpt.com "[PDF] Finite Sample Analysis of Average-Reward TD Learning and Q ..."
[2]: https://arxiv.org/pdf/2311.13469 "Span-Based Optimal Sample Complexity for Average Reward MDPs"
[3]: https://openreview.net/forum?id=HPvIf4w5Dd&noteId=bWX39IVkSa&utm_source=chatgpt.com "Finding good policies in average-reward Markov Decision Processes..."

---



Below is a self‑contained technical survey of **mixing rates (a.k.a. mixing times)** in the context of finite‑state Markov Decision Processes (MDPs).  I proceed in five logical layers:

| Layer                           | Guiding sub‑question                             | Outcome                                                                       |
| ------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------- |
| **1. Markov‑chain basics**      | How is mixing defined for an ordinary chain?     | Formal definitions, equivalent characterisations.                             |
| **2. From chains to MDPs**      | How does control alter the notion?               | Policy‑induced chains, worst‑policy (“uniform”) mixing time.                  |
| **3. Quantitative bounds**      | How can we compute / bound a mixing rate?        | Spectral gap, conductance, coupling, and geometric‑ergodicity parameters.     |
| **4. Algorithmic consequences** | Why does mixing matter in RL theory?             | Sample‑complexity and regret factors, average‑reward vs. discounted settings. |
| **5. Practical tips**           | How do practitioners estimate or improve mixing? | Diagnostics, design heuristics, and caveats.                                  |

---

## 1  Mixing for a Markov chain

**Setup.**
Let \(P\in\mathbb R^{|S|\times|S|}\) be the transition matrix of a *finite*, *irreducible*, *aperiodic* Markov chain with unique stationary distribution \(\pi\).

### 1.1  Total‑variation definition

For \(x\in S\) write

$$
d_x(t)\;=\;\left\lVert P^{t}(x,\cdot)-\pi\right\rVert_{\mathrm{TV}}
  \;=\;\tfrac12\sum_{y\in S}\bigl|P^{t}(x,y)-\pi(y)\bigr|.
$$

The **ε‑mixing time** is the *worst‑case* time to fall below ε:

$$
t_{\text{mix}}(\varepsilon)\;=\;
\min\{\,t:\max_{x\in S}d_x(t')\le\varepsilon\;\text{for all }t'\ge t\;\}.
\tag{1}
\]:contentReference[oaicite:0]{index=0}  

Often one fixes ε = ¼ and writes simply \(t_{\text{mix}}\).

### 1.2  Exponential (geometric) decay & “mixing rate”

If a chain is *uniformly ergodic* there exist constants \(C<\infty\) and \(0<\beta<1\) s.t.

\[
\max_{x\in S}d_x(t)\;\le\;C\,\beta^{\,t}\quad(t\ge0).
\tag{2}
$$

Here **β** (or \(\rho=\beta\)) is called the *mixing rate*; $t_{\text{mix}}(\varepsilon)=
\lceil\log_{\!\beta}(\varepsilon/C)\rceil$.

### 1.3  Spectral‑gap connection (reversible case)

If \(P\) is reversible, let

$$
\lambda_1=1>\lambda_2\ge\cdots\ge\lambda_{|S|}
$$

be its eigenvalues.  The **spectral gap** is

$$
\gamma=1-\lambda_2.
$$

For lazy chains (diagonal entries ≥½) one has

$$
t_{\text{mix}}(\varepsilon)
\;\le\;
\frac{1}{\gamma}\,
\log\!\left(\frac{1}{\varepsilon\;\pi_{\min}}\right),
\quad
\beta\;=\;1-\gamma, 
\tag{3}
\]:contentReference[oaicite:1]{index=1}  
and the reciprocal \(t_{\text{relax}}:=1/\gamma\) is often called the *relaxation time*.

---

## 2  Extending to MDPs

An **MDP** is a tuple \((S,A,P,R)\) with \(P(s'|s,a)\) the controlled kernel.  
Given a *stationary* (Markov) policy \(π(a|s)\), the state process is a Markov chain with matrix \(P_{π}(s,s')=\sum_{a}π(a|s)P(s'|s,a)\).

### 2.1  Policy‑specific mixing time  

\[
t_{\text{mix}}^{π}(\varepsilon)
:=t_{\text{mix}}(P_{π},\varepsilon)
\quad\text{as defined in (1).}
$$

### 2.2  Uniformly ergodic MDPs

The MDP is called **uniformly ergodic** if

$$
\sup_{π}\;t_{\text{mix}}^{π}(\varepsilon)<\infty
\quad(\text{equivalently } 
\sup_{π}\beta_{π}<1).
\tag{4}
$$

Denote the worst‑policy constant by

$$
T_*\;=\;\max_{π}t_{\text{mix}}^{π}(¼).
$$

Uniform ergodicity is the strongest mixing assumption used in modern RL analysis; it underpins the current *optimal* sample‑complexity bounds for average‑reward learning ([arxiv.org][1]).

**Weaker notions.**

| Name                   | Typical control‑theoretic use   | Formal condition on \(P_{π}\)                                                  |
| ---------------------- | ------------------------------- | ---------------------------------------------------------------------------- |
| *Geometric ergodicity* | Discounted MDPs                 | (2) holds for each π, but C,β may depend on π                                |
| *Weak communicating*   | Classic Puterman average‑reward | Only *optimal* policies need to be ergodic; sub‑optimal ones may fail to mix |

---

## 3  Bounding or estimating a mixing rate

| Technique                              | Core idea                                    | Bound produced                                               |
| -------------------------------------- | -------------------------------------------- | ------------------------------------------------------------ |
| **Spectral gap**                       | (3) above                                    | \(t_{\text{mix}}\le trel\log\!\frac1{ε\pi_{\min}}\).           |
| **Conductance Φ**                      | Cheeger inequality                           | \(t_{\text{mix}}\le \tfrac{1}{Φ^2}\log\!\frac1{ε\pi_{\min}}\). |
| **Path/canonical paths**               | Flow congestion                              | \(t_{\text{mix}}\le ρ_{\text{edge}} \log\!\frac1{επ_{\min}}\). |
| **Coupling / strong‑stationary times** | Construct joint copies that coalesce         | Often sharp, sometimes exact.                                |
| **Doeblin condition**                  | For continuous spaces, gives a β‑mixing rate | β = 1−δ where δ is the Doeblin mass.                         |

See the survey notes ([statslab.cam.ac.uk][2], [statslab.cam.ac.uk][2]) for derivations.

---

## 4  Why mixing matters in reinforcement learning

### 4.1  Sample‑complexity factors

For a generative simulator, learning an ε‑optimal *average‑reward* policy over a uniformly ergodic MDP with \(S\) states and \(A\) actions requires

$$
\Theta\!\bigl(SA\,T_*/\varepsilon^{2}\bigr)
$$

samples — and this **lower bound is tight** ([arxiv.org][1]).  Faster mixing (smaller \(T_*\)) directly lowers the oracle complexity.

### 4.2  Finite‑trajectory regret

In online control, regret bounds typically scale like

$$
O\!\bigl(\sqrt{T_*\;S A\,T}\bigr)
$$

for horizon \(T\); i.e. weak mixing slows down exploration.

### 4.3  Discounted‑reward evaluation

Temporal‑difference or Monte‑Carlo estimates have variance terms proportional to \(t_{\text{mix}}^{π}/(1-\gamma)\).  If \((1-\gamma)^{-1}\gg t_{\text{mix}}^{π}\), then discounted evaluation “forgets” the initial state *before* discounting truncates the reward tail, leading to cleaner asymptotics.

---

## 5  Practical guidance

| Task                              | Recommended practice                                                                                                         | Pitfalls                                                                                |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Diagnose mixing**               | Autocorrelation plots, Gelman–Rubin, empirical TV distance via long roll‑outs.                                               | Diagnostics require *state* observations; latent‑state RL needs proxies.                |
| **Estimate \(t_{\text{mix}}^{π}\)** | Spectral estimator of relaxation time or bootstrap TV‑distance curves from a single trajectory ([proceedings.mlr.press][3]). | High variance when \(π_{\min}\) is tiny; non‑reversible chains complicate eigen analysis. |
| **Improve mixing**                | • Add exploration bonus / entropy regularisation.<br>• Insert stochastic “trembling‑hand” noise (Doeblin mass).              | Artificial noise can degrade optimality; tune noise level carefully.                    |
| **Algorithm design**              | Use episode lengths ≥ \(T_*\).  In posterior sampling or optimistic algorithms, set confidence widths ∝ \(1/\sqrt{T_*}\).        | If \(T_*\) unknown, adaptive doubling or empirical‑mixing tests are required.             |
| **Theoretical checks**            | Verify that every policy induces an *irreducible aperiodic* chain; otherwise \(T_*=\infty\).                                   | Common MDP benchmarks (e.g. SparseRiverSwim) *violate* this silently.                   |

---

### Worked example (ring random walk)

For an uncontrolled lazy random walk on an \(n\)-cycle:

* \(\gamma = 1 - \cos\!\frac{2\pi}{n}\approx \tfrac{2\pi^2}{n^{2}}\).
* Hence \(t_{\text{mix}}(¼)=\Theta\!\bigl(n^{2}\log n\bigr)\).

If an agent may choose to *stay* with probability 1, the *worst‑policy* mixing time blows up to ∞; the class is **not** uniformly ergodic.  Adding a small compulsory jitter δ restores \(\beta\le 1-δ\).

---

## Key take‑aways

1. **Definition.**  Mixing time quantifies worst‑case convergence to stationarity; mixing *rate* is the associated exponential decay factor β.
2. **MDP nuance.**  One speaks of \(t_{\text{mix}}^{π}\) for a fixed policy and \(T_*\) for the policy class; *uniform ergodicity* means \(T_*<\infty\).
3. **Computation.**  In finite spaces, spectral gap bounds are sharp up to logarithms; in practice, combine eigen analysis with coupling arguments.
4. **RL impact.**  \(T_*\) controls statistical hardness: sample‑complexity, regret, and variance all degrade linearly or sub‑linearly with \(T_*\).
5. **Design lever.**  Careful exploration, entropy bonuses, or engineered randomness can shrink \(T_*\) and accelerate learning.

---

### Further reading

* Levin, Peres & Wilmer: *Markov Chains and Mixing Times* (Cambridge, 2017) — classic text ([stat.berkeley.edu][4]).
* Wang, Blanchet & Glynn (2024): Optimal sample complexity for uniformly ergodic AMDPs ([arxiv.org][1]).
* Hsu et al. (2020+) & Wolfer (2020): Estimating mixing times from a single trajectory ([proceedings.mlr.press][3]).

These works deepen the theory and provide algorithmic recipes for both analysis and empirical estimation.

[1]: https://arxiv.org/html/2310.08833v2 "Optimal Sample Complexity for Average Reward Markov Decision Processes"
[2]: https://www.statslab.cam.ac.uk/~ps422/mixing-notes.pdf?utm_source=chatgpt.com "[PDF] Mixing times of Markov chains - University of Cambridge"
[3]: https://proceedings.mlr.press/v117/wolfer20a/wolfer20a.pdf?utm_source=chatgpt.com "[PDF] Mixing Time Estimation in Ergodic Markov Chains from a Single ..."
[4]: https://www.stat.berkeley.edu/users/aldous/260-FMIE/Levin-Peres-Wilmer.pdf?utm_source=chatgpt.com "[PDF] Markov Chains and Mixing Times David A. Levin Yuval Peres ..."


---


Below is a structured technical compendium on the **span of the value function** for finite–state Markov Decision Processes (MDPs).  Each section answers a narrower sub‑question; read sequentially or jump to the topic of interest.

---

### 1 Formal definition and basic algebra

| Symbol                | Definition                                                                 |
| --------------------- | -------------------------------------------------------------------------- |
| \(v:S\!\to\!\mathbb R\) | Any real vector indexed by states                                          |
| **Span seminorm**     | \(\displaystyle\text{sp}(v)\;=\;\max_{s\in S} v(s)\;-\;\min_{s\in S} v(s)\). |

*Seminorm vs. norm.*  \(\text{sp}(v+c\mathbf 1)=\text{sp}(v)\) for every constant \(c\); the kernel is the one‑dimensional subspace \(\{\mathbf 1\}\), so “span” is a **seminorm** (no point separation).  Equivalently

$$
\text{sp}(v)\;=\;2\min_{c\in\mathbb R}\|v-c\mathbf 1\|_\infty ,
$$

a fact used extensively in error analyses.&#x20;

*Weighted variant.*  With positive weights \(w\),
\(\text{sp}_w(v)=\max_{s}v(s)/w(s)-\min_{s}v(s)/w(s)\).  Nothing below changes materially if the weights are bounded.

---

### 2 Where does span enter MDP theory?

#### 2.1  Differential (average‑reward) value functions

For an ergodic MDP let \(ρ^{π}\) be the steady‑state average reward of policy \(π\).
The **bias** (relative value) function \(h^{π}\) solves

$$
h^{π}(s)=\bigl(r(s,π(s))-\rho^{π}\bigr)+\sum_{s'}P(s'|s,π(s))\,h^{π}(s').
$$

Only \(h^{π}\) **up to an additive constant** is identified, so the natural size measure is \(H_{π}:=\text{sp}(h^{π})\).

#### 2.2  Discounted value functions

Even in discounted settings the performance‑loss bound

$$
|V^{π}(s)-V^{*}(s)|\le\frac{\text{sp}(T V^{π}-TV^{*})}{1-\gamma}
$$

shows that span governs how Bellman residuals translate into control error.

#### 2.3  Complexity parameters

Three popular hardness measures satisfy

$$
H_* \;:=\;\text{sp}(h^{*})\;\;\le\;D\;\;\le\;τ_{\!*},
$$

where \(D\) is the *diameter* (shortest expected hitting time between states) and \(τ_{\!*}\) any upper bound on the mixing time of an optimal policy.&#x20;

---

### 3 Analytic properties of the span seminorm

| Property                                                       | Implication                                                                                                                                                                      |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Shift‑invariance**: \( \text{sp}(v+c\mathbf 1)=\text{sp}(v)\). | Bias functions can be normalised arbitrarily (e.g. min = 0) without affecting analysis.                                                                                          |
| **Triangle inequality & absolute homogeneity**                 | Standard seminorm relations hold; proofs mirror the \(L_\infty\) norm.                                                                                                             |
| **Dual viewpoint**                                             | \(\tfrac12\text{sp}(v)=\max_{μ,ν}\langle v, μ-ν\rangle\) where the max ranges over probability measures; this connects span to the Dobrushin ergodic coefficient. ([arxiv.org][1]) |
| **Projective metric**                                          | Hilbert’s projective distance between vectors equals \(\log\bigl(\tfrac{\max v}{\min v}\bigr)\); its linearisation is precisely the span seminorm.                                 |

---

### 4 Contraction and convergence facts

| Setting                          | Bellman / transition operator \(F\)              | Contraction factor w\.r.t. span                                                                                                                                     |                                                                                                                    |
| -------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Discounted MDP, operator \(T\)     | (T v (s)=\max\_{a}(r(s,a)+\gamma\sum\_{s'}P(s' | s,a)v(s')))                                                                                                                                                         | ≤ γ in the ordinary ∞‑norm; the same bound holds for span because \(\text{sp}(T v - T u)\le\gamma\,\text{sp}(v-u)\). |
| Average‑reward policy evaluation | \(R^{π} - ρ^{π}\mathbf 1 + P_{π}h\)              | Contraction modulus \(\alpha=1-δ_{π}\) where \(δ_{π}\) is the Doeblin mass; equivalently \(\alpha\) is the Dobrushin coefficient of \(P_{π}\). ([cmap.polytechnique.fr][2]) |                                                                                                                    |
| Robust or risk‑averse MDPs       | Robust Bellman operator                        | Under ergodicity such operators remain span‑contractive, enabling TD/Q‑learning proofs.                                                                             |                                                                                                                    |

**Practical consequence.**  Value‑Iteration or Relative‑Value‑Iteration errors decay geometrically in span; stopping after
\(\lceil \log(\varepsilon/H_0)/\log(1/\alpha)\rceil\) iterations guarantees span ≤ ε.&#x20;

---

### 5 Algorithmic and statistical roles

| Problem                                      | Best‑known bounds                                                      | Span’s role                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Policy identification with a simulator**   | \(\Theta\!\bigl(SA\,H_*/\varepsilon^{2}\bigr)\) samples (tight).         | \(H_*\) replaces larger \(D\) or \(τ_{\!*}\) in older bounds.      |
| **Online regret (weakly communicating MDP)** | \(\tilde O\!\bigl(H_*\sqrt{SA\,T}\bigr)\) with algorithms such as SCAL.  | Exploration bonuses are scaled by an input bound \(c\ge H_*\). |
| **Finite‑sample TD / Q‑learning**            | \(O(1/\varepsilon^{2})\) trajectories for span‑error ≤ ε.                | Proofs exploit span‑contraction absent in any norm.          |

---

### 6 Computation and estimation

1. **Exact evaluation.**  In a small MDP one can compute \(h^{π}\) (or \(V^{*}\)) by solving linear equations, then take max–min.
2. **Online estimates.**  Track running maxima and minima of a bootstrapped value iterate; stopping rules based on confidence bands give high‑probability upper bounds.&#x20;
3. **Upper‑bounding surrogates.**  If \(H_*\) is unknown, use the diameter \(D\) or an empirical mixing‑time bound; guarantees simply degrade gracefully because \(H_*\le D\le τ_{\!*}\).

---

### 7 Relationship to other complexity notions

```
tightest   ←      H_* (optimal bias span)
                ≤ D  (MDP diameter)
                ≤ τ_* (mixing time bound)
```

*Span* captures **reward‑weighted** variability, ignoring unproductive detours that inflate diameter and mixing time.  Hence span‑based bounds are regularly one or two orders of magnitude sharper on hard but well‑connected tasks (e.g. RiverSwim with added bypass states).

---

### 8 Common pitfalls and best practices

| Pitfall                                                                                      | Mitigation                                                                            |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Forgetting shift‑invariance: comparing two values that differ by a constant gives zero span. | Always normalise one vector (e.g. set min = 0) before comparison.                     |
| Using span as a Lyapunov function when \(δ_{π}=0\).                                            | Verify *irreducibility*; otherwise no contraction exists.                             |
| Confusing span with total variation of a *distribution*.                                     | Span lives in **value space**, not probability space, although duality links the two. |

---

### 9 Open research directions

* **Efficient span estimation** without a simulator remains unsolved for large, partially observed systems.
* **Span‑aware deep RL**: merging span constraints with function approximation is still empirical.
* **Beyond MDPs**: span‑like seminorms recently appeared in non‑Markovian control and risk‑sensitive settings; theory is fragmentary.&#x20;

---

## Key take‑aways

1. **Definition:** \(\text{sp}(v)=\max v-\min v\); a seminorm invariant to shifts.
2. **Why it matters:** In average‑reward control the Bellman operator is *only* a contraction under span, making span central to convergence proofs and statistical rates.
3. **Complexity:** The optimal bias span \(H_*\) is the sharpest known problem‑length parameter, tightening sample‑complexity and regret bounds compared with diameter or mixing time.
4. **Practice:** When analysing algorithms, bound \(H_*\) (or supply an upper proxy); when implementing RL code, monitor span decay for robust stopping criteria.

These concepts equip you to recognise, analyse and exploit span in both theoretical work and applied reinforcement‑learning pipelines.

[1]: https://arxiv.org/pdf/2201.03103 "[PDF] Dual Seminorms, Ergodic Coefficients and Semicontraction Theory"
[2]: https://www.cmap.polytechnique.fr/~gaubert/PAPERS/GaubertQuIEOTD14QuFinal.pdf "[PDF] Dobrushin's ergodicity coefficient for Markov operators on cones"
