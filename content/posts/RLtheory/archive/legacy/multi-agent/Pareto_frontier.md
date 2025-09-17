---
date: "2025-07-11"
title: "Pareto frontier"
summary: "Pareto frontier"
lastmod: "2025-07-11"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

A design is Pareto optimal if we cannot improve one metric without worsening another.

Your sentence captures the intuition, but a **rigorous definition** helps avoid ambiguity—especially when there are more than two metrics or when “improve” can mean “≤” rather than “<”.

---

## Formal statement (multi‑objective optimisation)

Let

* **Decision space** \(X\subseteq\mathbb{R}^n\) (all feasible designs \(x\)).
* **Objective vector** \(f:X\to\mathbb{R}^m\), where

  $$
    f(x)=\bigl(f_1(x),\dots,f_m(x)\bigr)
  $$

  and each \(f_i\) is a scalar metric to be **minimised** (the usual convention; if a metric is to be maximised you minimise its negative).

### Pareto dominance

For two designs \(x,y\in X\),

$$
  y \prec x \quad\Longleftrightarrow\quad 
  \begin{cases}
     f_i(y)\le f_i(x) & \text{for every } i\in\{1,\dots,m\},\\
     f_j(y)<  f_j(x) & \text{for at least one } j .
  \end{cases}
$$

\(y\prec x\) means *y dominates x*.

### Pareto optimality

A design \(x^\star\in X\) is **Pareto optimal** (sometimes **efficient**) iff

$$
  \nexists\,y\in X:\; y\prec x^\star .
$$

Equivalently—your wording—*no metric can be strictly improved without at least one other becoming strictly worse.*

---

## Weak vs. strong efficiency

Some authors also use “weakly Pareto optimal”:

$$
  \nexists\,y\in X:\; f_i(y)<f_i(x^\star)\;\forall i .
$$

Weak efficiency allows ties in all metrics; strong efficiency (the definition above) requires a *strict* loss somewhere for any gain.

---

## Practical implications

1. **Pareto front/set** – The collection of all Pareto‑optimal designs forms the trade‑off surface engineers explore.
2. **Cardinality** – Unless metrics are perfectly correlated, the Pareto set is typically infinite (a curve, surface, etc.), not a single point.
3. **Decision making** – Moving along the front reflects shifting priorities (e.g., cost vs. weight). External preferences (utility functions, constraints, or interactive steering) are added *after* generating the front.
4. **Algorithms** – Evolutionary multi‑objective algorithms (NSGA‑II/III, SPEA2, MOEA/D), scalarisation methods (ε‑constraint, weighted sums), or mathematical programming with KKT conditions are common ways to approximate or locate Pareto‑optimal solutions.

---

## Common pitfalls

* **Single‑metric focus** – If you aggregate metrics too early (e.g., a weighted sum with fixed weights), you may miss large portions of the true Pareto front—especially if it is non‑convex.
* **Incomparable designs** – Metrics with different monotonic directions (say, “higher is better” for strength but “lower is better” for cost) must be normalised or sign‑corrected before applying the dominance test.
* **Discreteness** – In discrete design spaces, every feasible point can be Pareto optimal in degenerate cases; dominance checks still work but the front may be very large.

---

### Bottom line

> **A design is Pareto optimal if and only if no other feasible design improves one objective without causing at least one strict deterioration in another.**

Your original sentence is correct for the *strict* version; the formalism above shows the edge cases and lets you test designs algorithmically.

The Pareto frontier is the subset of all designs that are Pareto optimal.



Your statement is almost always *understood* correctly, but two closely‑related sets are routinely conflated:

| Name (common synonyms)                                   | Lives in …                                         | Formal definition                                               |
| -------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------- |
| **Pareto‑optimal set**<br>(efficient set, *Pareto set*)  | **Decision/design space** \(X\subseteq\mathbb{R}^n\) | \(P \;=\;\bigl\{\,x\in X \mid\nexists\,y\in X:\;y\prec x\bigr\}\) |
| **Pareto frontier**<br>(Pareto front, trade‑off surface) | **Objective space** \(\mathbb{R}^m\)                 | \(F \;=\;f(P)=\bigl\{\,f(x)\mid x\in P\bigr\}\)                   |

*Here \(y\prec x\) denotes *Pareto dominance* and \(f:X\!\to\!\mathbb{R}^m\) is the vector of objectives, all assumed to be minimised.*

---

### Why the distinction matters

* **Visualisation** – Engineers plot the *frontier* \(F\) because it shows explicit trade‑offs between metrics (cost vs performance, etc.).
* **Decision making** – A final choice must ultimately be a design \(x\in P\); selecting a point on \(F\) is only half the story—you still need the corresponding design variables.
* **Algorithm design** – Some algorithms (e.g., evolutionary methods) operate in \(X\) and return \(P\); others (e.g., adaptive sampling in objective space) aim directly at \(F\).

---

### Putting it together

> **The Pareto frontier is the image, in objective space, of the subset of designs that are Pareto optimal.**
> When people say “the frontier is the set of Pareto‑optimal designs,” they usually mean this shorthand, but strictly speaking the frontier and the efficient set live in different spaces.

Remember this mental model:

```
Design  x  ──f──▶  Objectives  f(x)
   │                       │
   └─ efficient set  P     └─ frontier  F
```

Keeping the two sets distinct prevents confusion when you (i) implement dominance checks in \(X\) yet (ii) plot or reason about trade‑offs in \(f(X)\).


A design dominates another design if it is equal or better in all objectives.


Your sentence matches the **weak** version of dominance. Most authors, however, reserve the word **“dominates”** (or **Pareto‐dominates**) for the **strict** version—where at least one objective is *strictly* better.
Below is the hierarchy that removes the ambiguity.

---

## Set‑up

Let

* \(X\subseteq\mathbb{R}^n\) be the feasible design space.
* \(f:X\!\to\!\mathbb{R}^m,\;f(x)=\bigl(f_1(x),\dots,f_m(x)\bigr)\) be the vector of objectives to **minimise** (if an objective is to be maximised, work with its negative).

For two designs \(x,y\in X\) define, component‑wise,

$$
f(y)\le f(x)\;:\;\;f_i(y)\le f_i(x)\quad \forall i\in\{1,\dots,m\}.
$$

---

## Three related relations

| Symbol       | Name                                   | Condition on \(y\) relative to \(x\)                        | Comments                                                                                       |
| ------------ | -------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| \(y\prec x\)   | **(Strict) Pareto dominance**          | \(f(y)\le f(x)\) **and** \(f_j(y)<f_j(x)\) for **some** \(j\) | “Equal or better in all, strictly better in at least one.” Used in defining Pareto optimality. |
| \(y\preceq x\) | **Weak dominance** (weak Pareto order) | \(f(y)\le f(x)\)                                          | Allows complete ties—your wording matches this case.                                           |
| \(f(y)=f(x)\)  | **Indifference** (objective tie)       | equality in every objective                             | Distinct designs can map to the same objective vector.                                         |

### Relationship

$$
y\prec x \;\Longrightarrow\; y\preceq x,\qquad
y\preceq x\; \centernot\!\Longrightarrow\; y\prec x.
$$

---

## Why the distinction matters

* **Pareto‑optimal set** uses the *strict* relation:

  $$
  P=\{x\in X \mid \nexists\,y\in X:\,y\prec x\},
  $$

  ensuring that every non‑dominated design is truly “best‑possible” in *some* direction.

* **Algorithms** (e.g., NSGA‑II/III, SPEA2) test strict dominance so that ties do not eliminate equally good designs.

* **Visualisation**: points that are weakly but not strictly dominated still appear on the boundary of the achievable region; deciding whether to prune them depends on the decision‑maker’s attitude toward ties.

---

## Quick example (two objectives: weight & cost, both to minimise)

| Design | Weight (kg) | Cost (\$) | Pairwise comparison to A                  |
| ------ | ----------- | --------- | ----------------------------------------- |
| **A**  | 10          | 100       | –                                         |
| **B**  | 10          | 90        | \(B\prec A\) (strict)                       |
| **C**  | 10          | 100       | \(C\preceq A\) but **not** \(C\prec A\) (tie) |
| **D**  | 8           | 120       | incomparable (one better, one worse)      |

*Only B dominates A in the strict sense; C is merely weakly dominating.*

---

### Bottom line

> **Strict Pareto dominance:** equal or better in every objective **and** strictly better in at least one.
> **Weak dominance:** equal or better in every objective (ties allowed).

Specify which notion you mean to avoid confusion in multi‑objective optimisation or when implementing dominance checks in code.

How do we generate the Pareto frontier.



Below is a structured “recipe book” for **generating (i.e. computing or approximating) the Pareto frontier** of a multi‑objective design problem.  Each section answers a sub‑question and points to widely‑used algorithms, with formal assumptions and links to implementation resources.

---

## 0.  Problem statement you must supply

Let

$$
\min_{x\in X} f(x)=\bigl(f_1(x),\dots ,f_m(x)\bigr),\qquad
X\subseteq\mathbb{R}^n .
$$

*Specify*

* **Decision domain \(X\)** – continuous, integer, mixed?
* **Objectives \(f_i\)** – black‑box, differentiable, or cheaply evaluable?
* **Budget** – number of function calls you can afford.

Everything else follows from these traits.

---

## 1.  Tiny or enumerable design spaces

*(\(|X|\lesssim10^5\))*

1. **Enumerate all feasible \(x\in X\)**.
2. **Pareto filter**: keep a design if no other row strictly dominates it (Algorithm 1 below).
3. Map surviving designs through \(f\) – that image is the frontier.

> **Complexity**: \(O(|X|^2)\) naïvely; \(O(|X|\log|X|)\) with divide‑and‑conquer filters.

This is exact, but tractable only for small discrete problems.

---

## 2.  Scalarisation (convert to many single‑objective runs)

| Method                                     | How                                                                                                   | Pros                                                                                                     | Cons                                                                |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Weighted‑sum**                           | Solve \(\min_x \sum_i w_i f_i(x)\) for many weight vectors \(w\) sampled on the simplex                   | Simple; any single‑objective solver works                                                                | Misses *non‑convex* parts of the frontier ([Purdue Engineering][1]) |
| **ϵ‑Constraint**                           | Pick one objective to keep; turn the others into constraints \(f_j(x)\le \epsilon_j\); sweep \(\epsilon\) | Captures non‑convex fronts; you control point spacing ([openmdao.github.io][2], [openmdao.github.io][2]) | Needs many runs; tight ε values can make problems infeasible        |
| **Chebyshev / NBI / Augmented Lagrangian** | Minimise a distance to an *ideal* or *utopia* point                                                   | Good spread; handles non‑convexity                                                                       | Implementation effort                                               |

**When to use** – You already have a robust single‑objective optimiser (SQP, IPOPT, etc.) and the objective evaluations are cheap enough to run it dozens–hundreds of times.

---

## 3.  Evolutionary Multi‑Objective Algorithms (EMOAs)

### 3.1  NSGA‑II (the workhorse)

**Loop** until termination:

1. Initialise population \(P\).
2. **Fast non‑dominated sorting** ⟶ fronts \(F_1,F_2,\dots\).
3. **Crowding‑distance** preserves diversity inside a front.
4. Tournament‑select parents, apply crossover & mutation to create offspring \(Q\).
5. Next generation \(P\gets\) best \( |P|\) individuals from \(P\cup Q\).

Detailed pseudocode and explanations are in the original paper by Deb et al. (2002) ([sci2s.ugr.es][3], [GeeksforGeeks][4]) and modern tutorials ([Pymoo][5]).

**Strengths**

* Handles discontinuous or highly‑non‑convex fronts.
* No derivatives needed.
* Good anytime behaviour—front improves gradually.

**Weaknesses**

* Thousands of function calls typical.
* Parameter tuning (population, crossover, mutation) affects quality.

> *Implementation*: `pymoo` has a ready NSGA‑II and dozens of variants ([Pymoo][5]).

### 3.2  Other EMOAs

* **MOEA/D** – decomposes the problem into many scalar sub‑problems whose solutions share information ([ResearchGate][6]).
* **NSGA‑III / R‑NSGA‑II** – use reference points to scale past three objectives (> 3 D front).
* **SPEA2, SMS‑EMOA** – hypervolume‑based selection.

Choose these if:

* \(m>3\) objectives (NSGA‑III, MOEA/D).
* You care about hypervolume as a convergence metric (SMS‑EMOA).
* You can run tens of thousands of evaluations or use cheap surrogates.

---

## 4.  Surrogate‑based or Bayesian Multi‑Objective Optimisation

*(“expensive” objectives, e.g. CFD in minutes)*

1. **Build Gaussian‑process (GP) or other surrogate** for each \(f_i\).
2. **Acquisition function**: Expected Hypervolume Improvement (EHVI) or its parallel forms qEHVI ([ScienceDirect][7], [NeurIPS Proceedings][8]).
3. **Sequential loop**: sample a batch maximizing the acquisition, evaluate expensive model, update surrogate, repeat.

   Libraries: **BoTorch** and **Trieste** offer EHVI / qEHVI implementations ([BoTorch][9], [secondmind-labs.github.io][10]).

**Advantages**

* Orders of magnitude fewer true evaluations (tens–hundreds).
* Provides uncertainty estimates on the frontier.

**Trade‑offs**

* Extra coding effort.
* GP scalings \(O(N^3)\); high‑dimensional design spaces need sparse or deep‑kernel surrogates.

---

## 5.  Gradient‑based continuous methods

When \(f\) is smooth and derivatives are available, solve Karush‑Kuhn‑Tucker (KKT) conditions:

$$
\exists\;\lambda\in\Delta^{m-1} :
\sum_{i=1}^{m} \lambda_i\nabla f_i(x^\star)=0 ,
$$

and \(x^\star\) satisfies constraints.

Practical realisation:

* Use scalarisation with *adaptive* weights that follow a predictor–corrector path across the front.
* Good for low‑dimensional \(X\) and high precision requirements.

---

## 6.  Post‑processing: The Pareto filter (Algorithm 1)

```pseudo
Input:  Set S of candidate designs, objective vectors f(x)
Output: Pareto‑optimal subset P ⊆ S
P ← ∅
for each x in S:
    dominated ← FALSE
    for each y in S:
        if f(y) ≤ f(x) and f(y) ≠ f(x):
            dominated ← TRUE
            break
    if not dominated:
        P ← P ∪ {x}
return P
```

This exact filter is embedded in EMOAs (Step 2 of NSGA‑II) and in many scalarisation post‑runs.

---

## 7.  Choosing a method – Decision tree

```
             Is |X| tiny?
             ┌──Yes──› Brute enumeration + Pareto filter
             │
             No
             │
   Are objectives expensive (≫ seconds)?
             ┌──Yes──› Surrogate / MOBO (EHVI)
             │
             No
             │
   Do you have derivatives & need high precision?
             ┌──Yes──› Gradient/KKT path‑following
             │
             No
             │
   Can you run many evaluations?
             ┌──Yes──› EMOA (NSGA‑II, MOEA/D, …)
             │
             No
             │
       Scalarisation sweep (ϵ‑constraint preferred)
```

---

## 8.  Software quick‑start

| Ecosystem        | Algorithms included                                  | Notes                            |
| ---------------- | ---------------------------------------------------- | -------------------------------- |
| **pymoo** (PyPI) | NSGA‑II/III, MOEA/D, SMS‑EMOA, etc. ([Pymoo][11])    | Python, very modular             |
| **Platypus**     | EMOAs + scalarisation toolkit                        | Python/Java                      |
| **DEAP**         | Evolutionary toolbox; roll your own NSGA‑II          | Python                           |
| **OpenMDAO**     | Direct ϵ‑constraint driver ([openmdao.github.io][2]) | Seamless with engineering models |
| **BoTorch / Ax** | Bayesian MO (EHVI, qNEHVI) ([BoTorch][9])            | GPUs, PyTorch                    |

---

## 9.  Practical tips & pitfalls

* **Non‑convexity** – avoid pure weighted‑sum unless you know the front is convex.
* **Uniform coverage** – NSGA‑II’s crowding distance or MOEA/D’s weight lattice tends to spread points; ϵ‑constraint spacing gives manual control.
* **High‑dimensional objective space** – visualise with parallel coordinates; NSGA‑III or reference‑point methods maintain diversity.
* **Stochastic algorithms** – run multiple seeds; report hypervolume or inverted generational distance (IGD) with confidence intervals.
* **Termination** – stop by budget, plateau in hypervolume, or change in crowding distance.
* **Validation** – recompute objectives for final set with high‑fidelity model if surrogates or coarse solvers were used.

---

### Key takeaway

> **Generate the Pareto frontier by repeatedly solving easier sub‑problems—either single‑objective surrogates (scalarisation, Bayesian acquisition) or population updates (EMOAs)—and preserving only the nondominated outcomes.**
> The “best” generator depends on evaluation cost, smoothness, dimensionality, and the precision/density of points you need.

Armed with the decision tree and algorithm sketches above, you can match your problem context to an implementation with confidence, measure convergence using hypervolume or IGD, and iterate until the frontier density meets your engineering or decision‑making needs.

[1]: https://engineering.purdue.edu/~sudhoff/ee630/Lecture09.pdf?utm_source=chatgpt.com "[PDF] Lecture 9: Multi-Objective Optimization"
[2]: https://openmdao.github.io/PracticalMDO/Notebooks/Optimization/multiobjective.html?utm_source=chatgpt.com "Multiobjective optimization"
[3]: https://sci2s.ugr.es/sites/default/files/files/Teaching/OtherPostGraduateCourses/Metaheuristicas/Deb_NSGAII.pdf?utm_source=chatgpt.com "[PDF] A fast and elitist multiobjective genetic algorithm: NSGA-II"
[4]: https://www.geeksforgeeks.org/non-dominated-sorting-genetic-algorithm-2-nsga-ii/?utm_source=chatgpt.com "Non-Dominated Sorting Genetic Algorithm 2 (NSGA-II)"
[5]: https://pymoo.org/algorithms/moo/nsga2.html?utm_source=chatgpt.com "NSGA-II: Non-dominated Sorting Genetic Algorithm - pymoo"
[6]: https://www.researchgate.net/publication/3418989_MOEAD_A_Multiobjective_Evolutionary_Algorithm_Based_on_Decomposition?utm_source=chatgpt.com "(PDF) MOEA/D: A Multiobjective Evolutionary Algorithm Based on ..."
[7]: https://www.sciencedirect.com/science/article/pii/S2210650217307861?utm_source=chatgpt.com "Multi-Objective Bayesian Global Optimization using expected ..."
[8]: https://proceedings.neurips.cc/paper/2020/hash/6fec24eac8f18ed793f5eaad3dd7977c-Abstract.html?utm_source=chatgpt.com "Differentiable Expected Hypervolume Improvement for Parallel Multi ..."
[9]: https://botorch.org/docs/multi_objective/?utm_source=chatgpt.com "Multi-Objective Bayesian Optimization - BoTorch"
[10]: https://secondmind-labs.github.io/trieste/0.13.3/notebooks/multi_objective_ehvi.html?utm_source=chatgpt.com "Multi-objective optimization with Expected HyperVolume Improvement"
[11]: https://pymoo.org/?utm_source=chatgpt.com "pymoo: Multi-objective Optimization in Python"

constraint method; lexicographic method; 


Below are **self‑contained, implementation‑ready descriptions** of the two classical *a‑posteriori* generators of Pareto‑optimal solutions you asked about.  Each method is given in the same structure so you can compare them quickly.

---

## 1 The ε‑Constraint (Constraint) Method

### 1.1 Idea

Choose **one objective** to optimise; impose **upper bounds** \(\epsilon_j\) (hence the name) on every other objective.  By sweeping the \(\epsilon_j\) values you trace the entire Pareto front—even its non‑convex parts ([openmdao.github.io][1]).

### 1.2 Mathematical Formulation (minimisation)

Let \(f=(f_1,\dots ,f_m)\) with all \(f_i\) to be minimised.
Pick an “active” objective \(f_1\).  For a prescribed vector \(\epsilon=(\epsilon_2,\dots ,\epsilon_m)\),

$$
\begin{aligned}
\min_{x\in X}\; & f_1(x) \\
\text{s.t. }\; & f_j(x)\;\le\;\epsilon_j,\quad j=2,\dots ,m .
\end{aligned}
\tag{EC\(_{\epsilon}\)}
$$

### 1.3 Algorithm (bi‑objective version for clarity)

```
Input   : objective pair (f1,f2), feasible set X,
          grid of ε-values   ε1<ε2<...<εK  covering f2’s range
Output  : nondominated set P  (decision space) and F=f(P) (frontier)

for ε in {ε1,…,εK}:
    solve   min f1(x)   s.t.   f2(x) ≤ ε ,   x∈X
    if feasible:
        store solution x, objective pair (f1(x),f2(x))
Pareto filter stored points   ←  Algorithm 1 in my previous reply
```

*General \(m>2\) case*: loop over a grid for \((\epsilon_2,\dots,\epsilon_m)\) or vary them sequentially.

### 1.4 Strengths & Weaknesses

| ✔ Produces points on **any** (even non‑convex) front ([openmdao.github.io][1])  | ✘ Needs many runs (one per ε‑vector)                                                       |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| ✔ Direct control over spacing of points                                         | ✘ Feasibility issues if ε too tight                                                        |
| ✔ Works with **any** single‑objective solver (linear, nonlinear, mixed‑integer) | ✘ A separate front is needed for each choice of “active” objective to ensure full coverage |

### 1.5 Practical Tips

* **Epsilon grid** – Find the natural bounds by first solving the two “anchor” single‑objective problems \(\min f_1, \min f_2,\dots\).
* **Augmented ε‑constraint** – For MILPs or badly scaled problems, add a penalty term to soften the constraints; see the GAMS *Augmented ε‑Constraint* driver ([gams.com][2]).
* **Parallelism** – Each ε run is independent; embarrassingly parallel on a cluster.

---

## 2 Lexicographic (Pre‑emptive) Method

### 2.1 Idea

Rank objectives by *priority*.  Fully optimise the most important one; **freeze its optimum value as a constraint**; proceed to the next objective, and so on.  The solution honours priorities exactly (any improvement in a higher‑ranked objective overrides any loss in lower ones).

### 2.2 Mathematical Formulation (minimisation)

Let the priority order be \(f_1 \succ f_2 \succ \dots \succ f_m\).

**Stage 1**

$$
\begin{aligned}
\min_{x\in X} &\; f_1(x)              &\quad\Rightarrow\quad& z_1^\star=f_1(x_1^\star)
\end{aligned}
$$

**Stage t = 2 … m**

$$
\begin{aligned}
\min_{x\in X}\; & f_t(x) \\
\text{s.t.}\; & f_k(x) = z_k^\star,\quad k=1,\dots ,t-1 ,
\end{aligned}
$$

giving \(x_t^\star\) and \(z_t^\star=f_t(x_t^\star)\).
The final design \(x_m^\star\) is **lexicographically optimal** ([Wikipedia][3], [gams.com][2]).

### 2.3 Algorithm (sequential implementation)

```
Input   : priority-ordered objectives (f1,...,fm), feasible set X
Output  : unique lexicographic optimum x*, objective vector f(x*)

for t = 1 … m:
    solve   min ft(x)      subject to   fk(x)=zk*   for k < t
    if infeasible:  stop – no solution exists
    record  zk* = ft(x_t*)
return x* = x_m*
```

### 2.4 Strengths & Weaknesses

| ✔ Simple; only **m** solves                        | ✘ **Extremely rigid** – tiny gains in \(f_1\) can wipe out immense gains in \(f_2,…\)            |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| ✔ Guarantees a unique best solution if ties absent | ✘ Does **not** generate an entire Pareto front; yields a **single** corner (supported) point |
| ✔ Compatible with any single‑objective solver      | ✘ Front becomes sensitive to scaling and numerical tolerances in equality constraints        |

### 2.5 Typical Use Cases

* **Design rules** with a strict hierarchy (e.g., *meet safety spec first, then minimise cost*).
* Generating “anchor” points for pay‑off tables, nadir values, or initialisation of other MOO methods ([gams.com][2]).
* Multi‑stage planning where earlier objectives are *hard* requirements.

---

## 3 When to Use Which?

| Situation                                                   | Recommended method                                    |
| ----------------------------------------------------------- | ----------------------------------------------------- |
| Need **many Pareto points** for trade‑off visualisation     | ε‑Constraint (grid or adaptive sweep)                 |
| Only one **dominant requirement** followed by tie‑breakers  | Lexicographic                                         |
| Mixed‑integer or black‑box models, solver already available | Either: both rely on sequential single‑objective runs |
| Front may be **non‑convex**                                 | ε‑Constraint (weighted‑sum would miss it)             |
| Budget of solver calls is very small (∼ m)                  | Lexicographic                                         |

---

### Key Take‑aways

* **ε‑Constraint** = *“optimise one, limit the rest”*  →  generates a *set* of nondominated points.
* **Lexicographic** = *“satisfy No. 1 perfectly, then No. 2, …”*  →  produces **one** priority‑respecting solution.
* Both are conceptually simple, solver‑agnostic, and complement weighted‑sum and evolutionary algorithms in a full MOO toolkit.

[1]: https://openmdao.github.io/PracticalMDO/Notebooks/Optimization/multiobjective.html "Multiobjective optimization"
[2]: https://www.gams.com/49/docs/T_LIBINCLUDE_MOO.html "Multi-Objective Optimization (moo)"
[3]: https://en.wikipedia.org/wiki/Lexicographic_optimization "Lexicographic optimization - Wikipedia"


weighted sum method, The weighted sum method will miss parts of non-convex Pareto frontiers.


### 1 What the weighted‑sum method actually does

For positive weights \(w\in\mathbb{R}^m_{>0}\) with \(\sum_{i=1}^{m}w_i=1\) the *weighted‑sum scalarisation* solves

$$
\min_{x\in X}\;w^{\mathsf T}f(x)=\sum_{i=1}^{m}w_i\,f_i(x)\qquad(\text{all }f_i\text{ are to be minimised}).
\tag{WS\(_w\)}
$$

Geometrically this pushes an *affine half‑space*
\(\{z\in\mathbb{R}^m\mid w^{\mathsf T}z=c\}\)  inward until it first touches the attainable objective set
\(\mathcal Z:=f(X)\).

---

### 2 Supported vs. unsupported Pareto points

* **Supported (or “convex‐hull”) points** are the ones hit by some supporting hyperplane of \(\mathcal Z\); they are exactly the optimal images of \((\text{WS}_w)\).
* **Unsupported** points are Pareto–optimal but lie in a *concave indentation* of \(\mathcal Z\); no hyperplane with non‑negative normal can touch them.

Hence

$$
\boxed{\text{Weighted sum } \Longleftrightarrow \text{supported solutions only}} \quad\text{(Theorem, ⋄)}.
$$

References: formal proofs in recent surveys on “supportedness” ([arXiv][1]) and classic optimisation texts; concise statement for MIP problems on OR‑StackExchange ([Operations Research Stack Exchange][2]).

---

### 3 Why non‑convex fronts disappear

If the *Pareto frontier* \(F=f(P)\subset\mathbb{R}^m\) is non‑convex, there exist Pareto points \(z^u\in F\) such that every supporting hyperplane touches \(F\) at *different* point(s) \(z^s\).
By Theorem ⋄, no weight vector will make \(z^u\) optimal in \((\text{WS}_w)\).
Therefore **any concave arc (or “dent”) on the front is skipped** by the weighted‑sum sweep ([SciSpace][3]).

---

### 4 Concrete two‑objective example (discrete)

| Design | \(f_1\) | \(f_2\) |          Supported?          |
| ------ | :---: | :---: | :--------------------------: |
| **A**  |   0   |   2   | ✔ (weight ratio \(w_1/w_2>1\)) |
| **B**  |   2   |   0   |        ✔ (\(w_1/w_2<1\))       |
| **C**  |   1   |  1.5  |           ❌ concave          |

*All three points are nondominated, but any line \(w_1 f_1 + w_2 f_2 = \text{const}\) that passes through **C** also intersects the convex hull edge \(\overline{AB}\); thus **C** can never win \((\text{WS}_w)\).*

---

### 5 Conditions under which weighted‑sum *is* complete

* The attainable set \(\mathcal Z\) is **(piecewise) convex** *and*
* weights are allowed to vary over **all** strictly positive directions.

Then \((\text{WS}_w)\) sweeps exactly the front. This is the classical result for linear objectives over convex \(X\).

---

### 6 What to do when the front is non‑convex

| Limitation of plain weighted‑sum  | Practical work‑around                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Skips unsupported points          | **ε‑Constraint** method (Sect. 1 of previous answer) finds *all* Pareto points ([Operations Research Stack Exchange][2])             |
| Poor density / clustering         | **Adaptive weighted‑sum** (AWS) perturbs weights and adds local constraints, recovering concave regions ([ResearchGate][4])          |
| Highly non‑convex or disconnected | **Normal Boundary Intersection (NBI)**, **Normal Constraint**, **MOEA/D**, **NSGA‑II/III**—frontier–focused instead of scalarisation |

---

### 7 Key take‑aways

*Weighted‑sum is simple and fast, but:*

1. **Only supported Pareto points appear**—any concave segment of the true frontier is invisible.
2. Convexity of the *image* set, not just of the decision space, is the crucial assumption.
3. When completeness matters, switch to ε‑constraint, adaptive WS, or evolutionary / surrogate‑based algorithms.

> **Rule of thumb**: use weighted‑sum for a quick *first cut*; if the front bends inward anywhere, augment it with a complementary generator.

[1]: https://arxiv.org/html/2501.13842v1 "On Supportedness in Multi-Objective Combinatorial Optimization"
[2]: https://or.stackexchange.com/questions/5000/does-the-weighted-sum-approach-find-all-pareto-optimal-solutions-in-milp "mixed integer programming - Does the weighted sum approach find all pareto-optimal solutions in MILP - Operations Research Stack Exchange"
[3]: https://scispace.com/papers/adaptive-weighted-sum-method-for-bi-objective-optimization-4m33p3rtnt?utm_source=chatgpt.com "(PDF) Adaptive weighted-sum method for bi-objective optimization"
[4]: https://www.researchgate.net/profile/He-Lehtihet/post/can_we_handle_Min_max_problem_with_multiobjective_optimization_tool_box_at_a_time/attachment/59d6419079197b807799d86d/AS%3A435329455923200%401480802038490/download/Adaptive%2BWeighted%2BSum%2B%282004%29.pdf "Adaptive Weighted Sum Method for Bi-objective Optimization"


goal programming; L_1, L_2, L_\infty norms; weighted exponential sum;



Below are **three scalarisation families** that turn a multi‑objective problem

$$
\min_{x\in X}f(x)=\bigl(f_1(x),\dots ,f_m(x)\bigr)
$$

into single‑objective sub‑problems whose optima are (at least weakly) Pareto‑optimal.
For each method you will find a **formal model, algorithm sketch, Pareto‑completeness properties, and practical pros/cons.**

---

## 1 Goal Programming (GP)

| Feature              | Description                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------------------- |
| *Philosophy*         | Satisfy target “goals” \(g_i\) rather than minimise \(f_i\) per se.                                     |
| *Decision variables* | Original \(x\) plus **deviation variables** \(d_i^{+},d_i^{-}\ge0\) for over/under‑achieving each goal. |
| *Generic model*      |                                                                                                     |

$$
\begin{aligned}
\min_{x,d^{+},d^{-}}\; & \Phi(d^{+},d^{-})\\
\text{s.t.}\;&f_i(x) - g_i = d_i^{+}-d_i^{-}\quad (i=1,\dots,m)\\
            &x\in X,\;d_i^{\pm}\ge0
\end{aligned}
$$

*Variants of* \(\Phi\):

1. **Weighted** GP \( \Phi=\sum_{i}w_i(d_i^{+}+d_i^{-})\)
2. **Pre‑emptive (lexicographic)** GP — minimise deviations in strict priority levels \(P_1\succ P_2\succ\cdots\).
3. **Chebyshev GP** minimise \(\max_i w_i(d_i^{+}+d_i^{-})\). ([Wikipedia][1]) |

### How it generates Pareto points

* If all weights \(w_i>0\) the optimum is **weakly Pareto‑optimal**. Proper tuning (or pre‑emptive tiers) removes weak dominance.
* Sweeping the goal vector \(g\) (e.g. along a grid between the ideal and nadir points) yields a *set* that approximates the frontier.

### Strengths

* Converts straight into LP/MILP, so any robust single‑objective solver can be reused.
* Lets stakeholders phrase requirements as **targets**, which is often psychologically easier than setting abstract weights.

### Caveats

* Poorly chosen \(g\) may land outside the feasible image—⇒ infeasible model.
* Weighted GP can return *internally dominated* solutions if the weights/normalisation are inconsistent; post‑filtering is advised. ([Department of Engineering][2])

---

## 2 Global‑Criterion / Compromise Programming

 (L₁, L₂, L∞ norms)

### 2.1 Definition

Choose an **ideal (utopia) point** \(z^{\star}=(z^{\star}_1,\dots ,z^{\star}_m)\) with
\(z^{\star}_i=\min_{x\in X}f_i(x)\).
For a weight vector \(w\in\mathbb{R}^m_{>0}\) on the simplex and a norm index \(p\in[1,\infty]\)

$$
\boxed{\;GC_{p}(w):\;
\min_{x\in X}\;
\bigl\|w\odot\bigl(f(x)-z^{\star}\bigr)\bigr\|_{p}
\;}
\tag{1}
$$

*Special cases*

* \(p=1\) → **Manhattan / weighted‑sum of deviations** (sometimes called the *augmented* L¹ when a small \(\rho\sum f_i\) is added to break ties).
* \(p=2\) → **Euclidean compromise programming** (smooth, differentiable).
* \(p=\infty\) → **Chebyshev (min–max)**: \(\min_x\max_i w_i\,[f_i(x)-z^{\star}_i]\).

### 2.2 Pareto‑completeness

* **Chebyshev (L∞)**: for every Pareto point there exists a weight vector making it optimal, even on **non‑convex** fronts. ([White Rose Research Online][3], [arXiv][4])
* \(1\le p<\infty\)**:** guarantees weak Pareto optimality, but *may* skip unsupported points unless the front is convex or an “augmented” term is added. ([www2.math.uni-wuppertal.de][5])

### 2.3 Implementation tips

* Normalise objectives (range or goal‑based) before applying weights.
* In practice solve a *sequence* of (1) with different \((w,p)\) to sample the front; Latin‑hypercube weight sampling gives good coverage.
* L∞ formulation becomes a smooth LP/NLP with an auxiliary variable \( \lambda\):

$$
\min_{x,\lambda}\;\lambda\;\; \text{s.t.}\; w_i\,[f_i(x)-z^{\star}_i]\le\lambda,\;i=1..m.
$$

### Pros & Cons

\| ✔ Smooth (for p<∞) → gradient methods; Chebyshev captures concave regions | ✘ Needs ideal point; inaccuracies here distort results |
|✔ One optimisation per weight‑vector; trivially parallel | ✘ Weight vectors near coordinate axes can cause numerical scaling issues |

---

## 3 Weighted **Exponential** (or \(p\)‑power) **Sum**

### 3.1 Scalarising function

$$
\boxed{\;WES_{p}(w):\;
\min_{x\in X}\Bigl(\sum_{i=1}^{m}w_i\,[f_i(x)]^{\,p}\Bigr)^{\!1/p}}
\qquad
p>0,\;w_i>0,\;\sum w_i=1
\tag{2}
$$

(Equivalent to \(\min \sum w_i f_i^p\) when the \(1/p\) root is dropped—it does not affect arg min.) ([Department of Computer Science][6])

### 3.2 Relationship to other norms

* \(p=1\) → ordinary weighted sum.
* \(p\to\infty\) → approaches the Chebyshev scalarisation, because \((\sum w_if_i^{p})^{1/p}\to\max_i f_i\).
* Thus WES forms a **continuous bridge** between linear and min–max norms.

### 3.3 Pareto coverage

* For *any* \(p>0\) the optimum is weakly Pareto‑optimal when all \(w_i>0\).
* As \(p\) grows, WES increasingly emphasises the largest component; with sufficiently large \(p\) and suitable weights it can recover unsupported points that plain weighted sums miss. ([Department of Computer Science][6])
* However, extremely large \(p\) (≥ 100) cause ill‑conditioning; use scaled objectives or logarithmic reparameterisation.

### 3.4 Algorithmic notes

1. Pick a small set of exponents (e.g. \(p\in\{1,2,4,8,16\}\));
2. For each \(p\) sample weights \(w\);
3. Solve (2) with any smooth NLP solver—gradients exist wherever \(f_i\) are differentiable.
4. Apply a Pareto filter to the union of solutions.

This typically yields a denser and more uniformly spaced front than using weights alone, at only \(O(|p|\times|w|)\) runs.

### Advantages / Limits

\| ✔ Captures concave regions earlier than L¹/L² | ✘ Exponent tuning still heuristic; no universal “best” \(p\) |
\| ✔ Smooth everywhere (except when some \(f_i=0\)) | ✘ Large \(m\) ⇒ high‑dimensional weight simplex |

---

## 4 Quick comparison

| Property                   | Goal Prog.                         | L₁/L₂/L∞ Norm                          | Weighted Exp. Sum            |
| -------------------------- | ---------------------------------- | -------------------------------------- | ---------------------------- |
| Inputs                     | Targets \(g_i\) (+ weights/priority) | Weights \(w\), norm \(p\), ideal \(z^\star\) | Weights \(w\), exponent \(p\)    |
| Yields                     | **One** solution per model run     | One solution per \((w,p)\)               | Same                         |
| Captures non‑convex front? | Yes, if goals sweep                | L∞: yes; p<∞: not guaranteed           | Often, for large \(p\)         |
| Smooth objective?          | Yes (linear/quadratic)             | p<∞: smooth; L∞ need auxiliary var     | Yes                          |
| Solvers                    | LP/MILP/NLP                        | Same                                   | Same                         |
| Typical use                | Satisficing, policy targets        | Engineering “distance‑to‑ideal”        | Front densification after WS |

---

### Practical take‑aways

* **Start** with a Chebyshev (L∞) or WES \(p\!>\!4\)**:** both reliably reach unsupported regions that plain weighted sums miss.
* **Goal programming** is invaluable when stakeholders can state **concrete targets**. Use weighted or Chebyshev GP to stay on (or project onto) the Pareto set.
* **Parameter sweeps** (weights, \(p\), or goal levels) are essential; one scalarisation run ≠ the frontier. Automate grid or Latin‑hypercube sampling and Pareto‑filter the union.
* Always **normalise** objectives before weighting—especially when mixing different units—to avoid unintended bias.
* Post‑process with a hypervolume or spread metric to check whether additional weight/exponent samples are needed.

These three scalarisation families, used judiciously and often **in combination**, will let you map virtually any Pareto frontier—convex or not—using only standard single‑objective optimisation building blocks.

[1]: https://en.wikipedia.org/wiki/Goal_programming "Goal programming - Wikipedia"
[2]: https://www3.eng.cam.ac.uk/~dr241/3E4/Lectures/3E4%20Lecture%206?utm_source=chatgpt.com "[PDF] Goal Programming • Multiple Objective Optimisation"
[3]: https://eprints.whiterose.ac.uk/id/eprint/86090/8/WRRO_86090.pdf "Methods for multi-objective optimization: An analysis"
[4]: https://arxiv.org/html/2308.12243v4?utm_source=chatgpt.com "Multi-Objective Optimization for Sparse Deep Multi-Task Learning"
[5]: https://www2.math.uni-wuppertal.de/~klamroth/publications/skwmu02.pdf?utm_source=chatgpt.com "[PDF] Norm-Based Approximation in Multicriteria Programming1"
[6]: https://www.cs.jhu.edu/~kevinduh/notes/duh11multiobj-handout.pdf "Multi-objective optimization"

weighted min-max method;



## Weighted **Min–Max** (Weighted Chebyshev, Weighted Tchebycheff) Scalarisation

> **Core idea:** Minimise the **largest** weighted deviation of the objective vector from a chosen reference (usually the *ideal* or *utopian* point).
> This turns “reduce **all** objectives” into “shrink the *worst*‑offending component first.”

---

### 1 Mathematical formulation

Let

* \(X\subseteq\mathbb{R}^n\) — feasible designs
* \(f:X\to\mathbb{R}^m\) — objectives to **minimise**
* \(z^{\star}\in\mathbb{R}^m\) — reference point (often \(z^{\star}_i=\min_{x\in X}f_i(x)\))
* \(w\in\mathbb{R}^m_{>0}\), \(\sum_i w_i=1\) — positive weights

Define the **weighted min–max problem**

$$
\boxed{\; \min_{x\in X}\;
\varphi_{w}(x)
\;},\qquad
\varphi_{w}(x):=\max_{1\le i\le m} \;w_i\,[\,f_i(x)-z^{\star}_i\,] .
\tag{WM\(_w\)}
$$

*Auxiliary‑variable NLP/LP form* (smooth and solver‑friendly):

$$
\begin{aligned}
\min_{x,\;\lambda} \;& \lambda \\[2pt]
\text{s.t. } & w_i\,[f_i(x)-z^{\star}_i]\;\le\;\lambda,\quad i=1,\dots ,m,\\
             & x\in X .
\end{aligned}
$$

---

### 2 Pareto‑optimality guarantees

* **Weak Pareto‑optimality:** every solution of (WM\(_w\)) with strictly positive \(w\) is weakly Pareto‑optimal.
* **Completeness:** for *every* Pareto‑optimal point \(x^{\dagger}\) there exists a weight vector \(w\!\succ\!0\) (often unique up to scaling) such that \(x^{\dagger}\) solves (WM\(_w\)) ([SpringerLink][1]).
* **Non‑convex fronts:** unlike plain weighted‑sum, (WM\(_w\)) reaches **unsupported** Pareto points inside concave regions of the frontier ([ScienceDirect][2]).

---

### 3 Algorithmic workflow (frontier sampling)

```
Input  : objective f, feasible set X
Output : set P of Pareto designs; frontier F=f(P)

1. Compute or approximate ideal point z⋆  (solve m single‑objective runs)
2. Choose a spread of weight vectors {w(1),…,w(K)} on the (m−1)-simplex
3. For each weight w(k):
       Solve (WM_w(k))  →  design x(k)
4. Collect S = {x(k)} and apply Pareto filter  →  P
5. Map F = f(P); repeat with more weights until coverage metric (e.g. hyper‑
   volume or spacing) stabilises
```

*Weight sampling*: Latin‑Hypercube or the MOEA/D “weight lattice” give even coverage; denser sampling near coordinate axes magnifies extremes.

---

### 4 Practical strengths and caveats

\| ✔ **Captures concave regions** missed by weighted‑sum | ✘ Requires a **good reference** point; an inaccurate \(z^{\star}\) skews the search |
|✔ **One optimisation per weight** → embarrassingly parallel | ✘ Sensitive to **scaling**; always normalise \(f_i\) or use range‑based weights |
|✔ Smooth auxiliary form — usable with gradient NLP, MILP, or black‑box solver | ✘ Very small weights can create flat regions ⇒ numerical ill‑conditioning |
|✔ Provably convergent to *any* Pareto point as weights vary | ✘ Each run gives **one** point; many runs needed for dense fronts |

---

### 5 Connections and extensions

| Relation                                                       | Comment                                                                                                                       |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **L∞ norm** with weights = (WM\(_w\))                            | It is precisely the weighted Chebyshev distance to \(z^{\star}\).                                                               |
| **Weighted exponential / p‑power sum**                         | As \(p\to\infty\) the weighted \(p\)-norm tends to (WM\(_w\)); using several \(p\) values bridges between ordinary WS and min–max.    |
| **Normal Boundary Intersection (NBI)** & **Normal Constraint** | These methods solve sequences of (WM\(_w\))‑type sub‑problems along normals to the convex hull to obtain evenly spaced fronts.  |
| **MOEA/D decomposition**                                       | Uses (WM\(_w\)) or its Tchebycheff variant as sub‑problem inside an evolutionary framework; inherits the completeness property. |

---

### 6 Illustrative bi‑objective example

Suppose \(f_1\) = cost, \(f_2\) = weight (both to minimise) with ideal point $$z^{\star}=(100\,\$,\,10\,\text{kg})$$.
*Weights*: \(w=(0.7,\,0.3)\).
*Scalar objective*:

$$
\varphi_w(x)=\max\Bigl\{0.7\,[f_1(x)-100],\;0.3\,[f_2(x)-10]\Bigr\}.
$$

The optimiser pushes **whichever of the two scaled gaps is larger** toward zero first; if cost is far above ideal but weight is near ideal, it prioritises cost until the scaled gaps tie, then improves both.
By sweeping \(w_1/w_2\) you trace the complete nondominated curve, including concave bends that a weighted‑sum sweep would skip.

---

### 7 When to choose weighted min–max

| Use it when …                                                                                       | Consider alternatives if …                                                                                            |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| You need **all** Pareto points, including unsupported ones, yet want a deterministic scalar solver. | Objectives are costly and you can afford only \~ 30 evaluations → prefer Bayesian multi‑objective + EHVI.             |
| You have an accurate or cheaply approximable ideal/utopian point.                                   | The ideal point is unknown or noisy → ε‑constraint (no reference needed) or NSGA‑II.                                  |
| A solver for min–max formulations (LP/NLP/MILP) is readily available.                               | The design space is highly non‑smooth / discrete and solver performance is poor → decomposition‑based EMOAs (MOEA/D). |

---

### 8 Take‑away formula

$$
\boxed{\textbf{Weighted Min–Max:}\;
x^{\star}(w)
=\arg\min_{x\in X}\,
\Bigl[
\max_{i}\,w_i\,\bigl(f_i(x)-z^{\star}_i\bigr)
\Bigr],\quad w\succ0
}
$$

Vary \(w\) over the positive simplex → **complete Pareto coverage**, even on non‑convex frontiers ([ScienceDirect][2], [SpringerLink][1]).

Adopt normalisation, sample weights systematically, and filter duplicates; the result is a rigorous, solver‑agnostic pipeline for mapping the entire Pareto frontier.

[1]: https://link.springer.com/article/10.1007/s10898-023-01284-x?utm_source=chatgpt.com "Analysis of the weighted Tchebycheff weight set decomposition for ..."
[2]: https://www.sciencedirect.com/topics/engineering/tchebycheff?utm_source=chatgpt.com "Tchebycheff - an overview | ScienceDirect Topics"


We can also adopt standard population methods to encourage populations to spread over the Pareto frontier, like using vector evaluated genetic algorithm to optimise different sub-populations for different objectives and select parents from different sub-populations.



### Population‑based multi‑objective optimisation at a glance

Because a **population** stores many candidate designs simultaneously, evolutionary and swarm algorithms can advance *several* points toward the Pareto frontier in one run.  The key design choice is **how fitness is assigned so that (i) pressure toward non‑domination and (ii) pressure toward diversity coexist**.  “Vector‑evaluated” methods are the earliest explicit attempt.

---

## 1 Vector Evaluated Genetic Algorithm (VEGA)

| Step                                                                                                                                    | Description |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **1. Partition** the global population \(P\) of size \(N\) into \(m\) *equal* sub‑populations \(P^{(1)},\dots ,P^{(m)}\) — one per objective.   |             |
| **2. Objective‑wise fitness**: in sub‑population \(P^{(j)}\) rank individuals by the single objective \(f_j\) only (ties get average rank). |             |
| **3. Parent selection** is performed **within each sub‑population** using the ranks just computed.                                      |             |
| **4. Recombine** all selected parents, apply crossover + mutation to create \(N\) offspring.                                              |             |
| **5. Replace** the old population with the offspring and loop to Step 1.                                                                |             |

*(J. D. Schaffer, 1985) ([ResearchGate][1])*

### 1.1 Why it can *spread* along the front

Because each objective occasionally becomes the *sole* selection criterion, individuals that are good at different objectives survive together, populating different regions of objective space.

### 1.2 Known weaknesses

* **Bias toward extremes**: single‑objective ranking favours individuals near axis minima; the centre of the front is under‑represented ([biomechanical.asmedigitalcollection.asme.org][2]).
* **No elitism**: Pareto‑optimal parents can vanish from one generation to the next.
* **Fitness discontinuity** when objectives differ greatly in scale.

---

## 2 Modern population methods that fix VEGA’s flaws

| Algorithm (year)                 | Main ideas                                                                                                                 | How diversity is preserved                                             | Advantages over VEGA                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **NSGA‑II** (2002)               | Fast non‑dominated sorting + crowding distance + explicit elitism                                                          | Secondary sort on *crowding distance* within each non‑domination front | Covers entire front steadily; \(O(mN^2)\) but efficient in practice ([sci2s.ugr.es][3]) |
| **SPEA2** (2002)                 | External archive + fitness based on dominance count + k‑th‑nearest‑neighbour density                                       | Truncation keeps archive uniformly spread                              | Better convergence metric (strength); archive adds elitism                            |
| **MOEA/D** (2007)                | Decompose MOO into \(K\) scalar sub‑problems (weighted min–max, Tchebycheff, …); neighbouring sub‑problems share information | Implicit via geographic weights                                        | Linear per‑generation cost; natural parallelism                                       |
| **NSGA‑III / R‑NSGA‑II** (2013–) | Reference‑point based niching for \(m>3\) objectives                                                                         | Reference directions on a simplex                                      | Maintains spread in high‑D objective spaces where crowding fails                      |

All four inherit VEGA’s *concept* of working with a population but replace its selection rule.

---

## 3 Designing sub‑population schemes today

1. **Partition strategy**

   * *Static equal blocks* (VEGA style)
   * *Dynamic proportions* based on objective difficulty or hypervolume contribution
2. **Cross‑sub‑population mating**

   * Randomly choose parents from *different* sub‑pops to promote mixture of trade‑offs.
   * Or restrict mating to *adjacent* objectives (ring topology) for smoother interpolation.
3. **Migration / elite exchange**

   * Copy top Pareto solutions into every sub‑population each generation (adds elitism while retaining specialised pressure).
4. **Secondary fitness modifier**

   * Apply *crowding distance* or *fitness sharing* after objective‑wise ranking to mitigate the extreme‑solution bias.
5. **Termination**

   * Monitor hypervolume or inverted generational distance (IGD); stop when Δmetric < ε for \(k\) generations.

---

## 4 Implementation tips

| Issue                                              | Mitigation                                                                                                                             |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Objective scaling** – one metric dominates ranks | Normalise \(f_i\) to \[0, 1] or use percentile ranks inside each sub‑pop.                                                                |
| **Premature loss of good individuals**             | Keep an *external archive* updated every generation; insert archive elites back into mating pool.                                      |
| **High cost per evaluation**                       | Couple VEGA‑like partitioning with **surrogate models** (one per sub‑pop) so each objective is emulated locally.                       |
| **Uneven front sampling**                          | Periodically *rotate* which objective each partition optimises; over \(m·T\) generations each sub‑pop has targeted every objective once. |

---

## 5 When to pick a VEGA‑style partition over NSGA‑II

| Prefer VEGA‑style if …                                                                                                 | Choose non‑domination algorithms if …                                                                      |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Objectives are **computationally separable** and single‑objective specialists exist (e.g., tuning separate PID loops). | You need *systematic* Pareto coverage without manual tweaking of partitions.                               |
| Implementation simplicity or legacy GA code must be reused.                                                            | You require theoretical guarantees of elitism and convergence.                                             |
| You plan to add your own diversity / elitism modules and like the interpretability of sub‑populations.                 | The front has \(>3\) objectives or severe concavity that crowding/reference‑direction methods handle better. |

---

### Key take‑aways

* **VEGA proves the principle** that multi‑objective evolutionary search can spread naturally by alternating single‑objective pressures.
* **Without diversity control and elitism, VEGA is biased**—modern MOEAs fix this with non‑domination sorting, archiving, reference directions, or decomposition.
* **Sub‑population ideas remain useful**: hybrid schemes (e.g., MOEA/D’s neighbourhoods, differential objective cycling) often outperform a single mixed population when objectives decompose naturally.

By combining *objective‑wise specialisation* with *elitist preservation* and *density control*, you obtain the best of VEGA’s intuitive spread and NSGA‑II’s reliable convergence to the full Pareto frontier.

[1]: https://www.researchgate.net/publication/220885605_Multiple_Objective_Optimization_with_Vector_Evaluated_Genetic_Algorithms?utm_source=chatgpt.com "(PDF) Multiple Objective Optimization with Vector Evaluated Genetic ..."
[2]: https://biomechanical.asmedigitalcollection.asme.org/book/chapter-pdf/2797850/859735_paper19.pdf?utm_source=chatgpt.com "materialized view selection using vector evaluated genetic algorithm"
[3]: https://sci2s.ugr.es/sites/default/files/files/Teaching/OtherPostGraduateCourses/Metaheuristicas/Deb_NSGAII.pdf?utm_source=chatgpt.com "[PDF] A fast and elitist multiobjective genetic algorithm: NSGA-II"


We can also rank individuals using a non-domination ranking.

Pareto filters filter out individuals that are already dominated by other design point.

Niche techniques help encourage an even spread of points.

At some point, we are going to need to pick a single design and go with it. We could do so by creating a single objective using (i.e., the weighted sum method). But how do we pick the weights?


### Why “just set some numbers” is *not* enough

Weights in a weighted‑sum objective

$$
F_w(x)=\sum_{i=1}^{m}w_i\,f_i^{\;\text{norm}}(x),\qquad 
w_i>0,\;\sum_{i=1}^{m}w_i=1
$$

encode **your explicit rate of exchange** between objectives.
If they are picked arbitrarily the chosen design can be *far* from the decision‑maker’s real preferences, or even dominated once the objectives are rescaled.  Weight selection therefore has to be treated as a **preference‑elicitation exercise**—not a purely mathematical tuning knob.

Below is a toolbox‑style guide, arranged from *lowest‑effort* to *most‑rigorous* approaches.

---

## 1 Prerequisites (do these first)

| Task                                                                                                                                | Why it matters                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **1.1 Define value direction**: convert all “maximise” metrics to minimisation (e.g. \( -\text{utility}\)).                           | Keeps dominance and weighting rules consistent.                            |
| **1.2 Normalise each objective**—common choices: linear to \([0,1]\) using its *range on the Pareto set* or the *ideal/nadir* points. | Otherwise a \$10 k change dwarfs a 1 kg change regardless of “importance”. |
| **1.3 Check units & monotonicity**.                                                                                                 | Prevents hidden bias from unit choices (e.g., kg vs g).                    |

---

## 2 Quick‑but‑formal elicitation methods

| Method                                                                                             | Elicitation questions (typical)                                                                                                                 | How weights are computed                       | Pros                                                             | Cons / when to avoid                                       |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------- |
| **Direct rating / 100‑point budget**                                                               | “Distribute 100 chips across the criteria proportional to their importance.”                                                                    | \(w_i = \frac{\text{chips}_i}{100}\)             | Fast; good for small teams.                                      | Coarse; people anchor on round numbers.                    |
| **SMART / SMARTER** (Simple Multi‑Attribute Rating) ([ScienceDirect][1])                           | Rank criteria by importance; give top rank 100, next 90, … (SMART) or use “rank sum” formula (SMARTER).                                         | Rank‑based formula normalises automatically.   | No pairwise burden; robust to scale.                             | Differences between neighbouring ranks forced to be equal. |
| **Swing weighting** (“swing matrix”) ([analysisfunction.civilservice.gov.uk][2], [web.mst.edu][3]) | “If **all** criteria are at their worst, which single *swing* to best would you take first, second, …?”  Allocate 100 points over these swings. | Convert points to \(w_i\) after *range* scaling. | Incorporates both range and importance; intuitive for engineers. | Needs clear best/worst levels; 30–60 min workshop.         |

All three produce a **weight vector once**, after which you evaluate every design with the same \(F_w\).

---

## 3 Analytic Hierarchy Process (AHP) – the classic pairwise route

1. **Structure a hierarchy**: goal → criteria → (sub‑criteria)
2. **Pairwise comparisons** on a 1–9 importance scale for each sibling pair.
3. **Eigenvector** of each comparison matrix ⇒ local weights; roll them up.
4. **Consistency ratio** < 0.1? If not, revisit judgements. ([Wikipedia][4], [1000minds][5])

**Strengths**

* Captures subtle nuances; built‑in consistency check.
* Widely supported in commercial / open‑source tools.

**Caveats**

* \(O(m^2)\) judgements; becomes tiring for \(m>8\).
* Produces complete order even if the DM is indifferent—check by sensitivity analysis.

---

## 4 Interactive or “preference‑driven” weighting

Instead of asking for numbers up front, **let the frontier guide the discussion**:

| Family                                    | How it works                                                                                                                                                                   | Key sources                                      |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| **Trade‑off queries / Zionts–Wallenius**  | Show the DM two frontier designs; ask “prefer A, B, or indifferent?” Infer linear inequalities on \(w\); repeat until a unique region remains.                                   | ([ScienceDirect][6])                             |
| **Interactive Evolutionary MOO**          | An EMOA periodically presents a diverse “menu” of solutions; the DM scores or ranks them; a machine‑learning model updates \(w\) or a utility proxy guiding the next population. | ([ScienceDirect][7])                             |
| **Pareto‑front region of interest (ROI)** | DM specifies a reference point \(z^{\text{aspire}}\); algorithm automatically finds \(w\) (or ε‑constraint box) that zooms into designs better than \(z^{\text{aspire}}\).           | Recent interactive ε‑constraint work ([SSRN][8]) |

*Advantages*:

* No need to articulate weights in abstract units.
* Can stop as soon as a satisfactory design appears.

---

## 5 Group or uncertain preferences

* **Aggregating multiple stakeholders**:

  * Average weights (if compromise acceptable)
  * Weighted voting / bargaining
  * Social‑choice rules (e.g. Borda) when consensus impossible.

* **Imprecise weights**: treat each \(w_i\) as an interval; compute **robust solution** via Stochastic Multi‑attribute Acceptability Analysis (SMAA) or max‑regret criteria.

---

## 6 After you have weights – sanity checks

1. **Dominance audit**: verify that the chosen design is on (or very near) the Pareto frontier produced earlier; if not, redo normalisation or elicitation.
2. **Sensitivity sweep**: perturb each \(w_i\) ±10 % (or over stated confidence intervals) and see if design selection changes.  Huge flips → revisit elicitation.
3. **Stakeholder validation**: present *what‑if* scenarios (“With these weights we accepted +5 % cost to save 1 kg. Is that OK?”).

---

## 7 If elicitation fails – fallback heuristics

* **Knee‑point detection**: pick the design with the largest curvature change on the frontier; gives a “balanced compromise” without explicit weights.
* **Min‑max normalised regret**: choose \(x^\star=\arg\min_x\max_i\frac{f_i(x)-z_i^\star}{z_i^{\text{worst}}-z_i^\star}\); equivalent to weighted min–max with equal weights.
* **Median objective**: minimise the median of ranked, normalised objectives—robust to outliers but only defensible when loss symmetry is acceptable.

---

## 8 Putting it into practice – a micro‑workflow

```text
Step 0  Generate/approximate Pareto front  P
Step 1  Pick an elicitation method  →  weight vector  w
Step 2  Normalise P’s objective columns  f_i^norm
Step 3  Evaluate F_w(x) = Σ w_i f_i^norm(x)  ∀ x∈P
Step 4  Choose x* = argmin F_w
Step 5  Sensitivity & dominance checks  →  accept or return to Step 1/2
```

*Automate Steps 2–5 in a notebook so the DM can tweak weights live.*

---

### Take‑away rules of thumb

1. **Always normalise first**, otherwise weights are meaningless.
2. **Use swing weighting or AHP** when you can afford a 30‑min workshop—these two methods balance rigour with cognitive load.
3. **Go interactive** if stakeholders struggle to verbalise trade‑offs; let real designs anchor their intuition.
4. **Never skip sensitivity analysis**; if small weight changes flip the decision, you don’t yet understand preferences well enough.

Following this structured elicitation–validation loop converts “pick some weights” from a guess into a transparent, defensible decision‑making step.

[1]: https://www.sciencedirect.com/science/article/abs/pii/S0749597884710879?utm_source=chatgpt.com "Improved Simple Methods for Multiattribute Utility Measurement"
[2]: https://analysisfunction.civilservice.gov.uk/policy-store/an-introductory-guide-to-mcda/?utm_source=chatgpt.com "An Introductory Guide to Multi-Criteria Decision Analysis (MCDA)"
[3]: https://web.mst.edu/lib-circ/files/Special%20Collections/INCOSE/Using%20the%20Swing%20Weight%20Matrix%20to%20Weight%20Multiple%20Objectives.pdf?utm_source=chatgpt.com "[PDF] Using the Swing Weight Matrix to Weight Multiple Objectives"
[4]: https://en.wikipedia.org/wiki/Analytic_hierarchy_process?utm_source=chatgpt.com "Analytic hierarchy process - Wikipedia"
[5]: https://www.1000minds.com/decision-making/analytic-hierarchy-process-ahp?utm_source=chatgpt.com "What is the Analytic Hierarchy Process (AHP)? - 1000minds"
[6]: https://www.sciencedirect.com/science/article/abs/pii/S2193943821000923?utm_source=chatgpt.com "Interactive resolution of multiobjective combinatorial optimization ..."
[7]: https://www.sciencedirect.com/science/article/abs/pii/S0305048323000890?utm_source=chatgpt.com "Explainable interactive evolutionary multiobjective optimization"
[8]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5034848&utm_source=chatgpt.com "An interactive method for multi-objective optimization - SSRN"












