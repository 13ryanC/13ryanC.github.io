---
date: "2025-06-30"
title: "Banach Fixed Point"
summary: "Wandering"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### Banach Fixed‑Point Theorem

*(also called the Contraction Mapping Principle)*

---

#### Formal statement

Let \((X,d)\) be a **complete metric space**, i.e. every Cauchy sequence in \(X\) converges to a point of \(X\).
Let \(T:X\to X\) be a **contraction mapping**:

$$
\exists\;\lambda\in(0,1)\quad\text{such that}\quad 
d\!\bigl(Tx,Ty\bigr)\le\lambda\,d(x,y)\quad\forall\,x,y\in X .
$$

Then

1. **Existence**: \(T\) possesses a unique fixed point \(x^\ast\in X\) (i.e. \(Tx^\ast=x^\ast\)).

2. **Constructive convergence** (Picard iteration): Starting from any \(x_0\in X\) and defining

   $$
   x_{n+1}=T x_n,\qquad n\ge 0 ,
   $$

   the sequence \((x_n)\) converges to \(x^\ast\) and

   $$
   d(x_n,x^\ast)\le \lambda^{\,n}\,d(x_1,x_0)\;\bigl/\;(1-\lambda).
   $$

3. **A‑posteriori error bound**:

   $$
   d(x_n,x^\ast)\;\le\;\frac{\lambda}{1-\lambda}\,d(x_n,x_{n-1}).
   $$

---

#### Key concepts and assumptions

| Item                     | Meaning                                                                            | Essential because…                                                 |
| ------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Metric space** \((X,d)\) | Set \(X\) with distance \(d\) satisfying positivity, symmetry, and triangle inequality | Gives a notion of “closeness”.                                     |
| **Complete**             | Every Cauchy sequence converges in \(X\)                                             | Guarantees that the limit of the iteration stays inside the space. |
| **Contraction**          | Lipschitz constant \(\lambda<1\)                                                     | Shrinks distances, forcing successive iterates together.           |

*If any of these hypotheses is dropped, the theorem can fail; see pitfalls below.*

---

#### Sketch of proof (multi‑hop reasoning)

1. **Construct sequence**
   \(x_{n+1}=T x_n\).
   Because \(T\) is a contraction, successive differences shrink geometrically:

   $$
   d(x_{n+1},x_n)\le\lambda^{\,n}\,d(x_1,x_0).
   $$

2. **Cauchy property**
   For \(m>n\),

   $$
   d(x_m,x_n)\le\sum_{k=n}^{m-1}d(x_{k+1},x_k)
   \le d(x_1,x_0)\sum_{k=n}^{\infty}\lambda^{\,k}
   =\frac{\lambda^{\,n}}{1-\lambda}\,d(x_1,x_0).
   $$

   Thus \((x_n)\) is Cauchy.

3. **Completeness ⇒ limit exists**
   Since \(X\) is complete, \(x_n\to x^\ast\in X\).

4. **Limit is fixed point**
   Continuity of \(T\) (follows from the contraction inequality) yields
   \(T x^\ast= \lim T x_n=\lim x_{n+1}=x^\ast\).

5. **Uniqueness**
   If \(y^\ast\) is another fixed point, then
   \(d(x^\ast,y^\ast)=d(Tx^\ast,Ty^\ast)\le\lambda\,d(x^\ast,y^\ast)\).
   With \(\lambda<1\) this forces \(d(x^\ast,y^\ast)=0\).

---

#### Why it matters (applications)

| Area                                | Typical role of the theorem                                                                                                    |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Ordinary Differential Equations** | Proves existence & uniqueness of solutions to \(y'=f(t,y)\) via the Picard‑Lindelöf method.                                      |
| **Integral equations**              | Shows kernels with small norm have unique solutions.                                                                           |
| **Numerical analysis**              | Justifies convergence of iterative solvers (e.g. Jacobi method under diagonal dominance).                                      |
| **Dynamic programming / economics** | Ensures Bellman operator has a unique value function and gives a contraction‑based iteration scheme.                           |
| **Fractals**                        | The Hutchinson operator on subsets of \(\mathbb{R}^n\) is a contraction in the Hausdorff metric; its fixed point is the fractal. |

---

#### Pitfalls & limits

* **Completeness is unavoidable**: A contraction on an **incomplete** space can lack a fixed point (e.g. \(T:x\mapsto x/2\) on \((0,1)\) has no fixed point inside the open interval).
* **Lipschitz constant must be \(<1\)**: If \(\lambda=1\), uniqueness and convergence may fail (consider rotations on the circle).
* **Not all fixed‑point theorems are contractions**: Brouwer and Schauder require compactness, not a metric shrink; their conclusions are existential but non‑constructive.

---

#### Typical workflow in practice

1. **Model** your problem as \(x = T x\).
2. **Verify** completeness of the underlying space (often a Banach space of functions).
3. **Estimate** a Lipschitz constant \(\lambda<1\) for \(T\).
4. **Iterate**: start with any \(x_0\) and apply Picard iteration.
5. **Use error bounds** above for stopping criteria and certified tolerances.

---

#### Suggested tests when uncertain

* Compute two successive iterates \(x_{n-1},x_n\). If
  \(\dfrac{d(x_n,x_{n-1})}{1-\lambda}\) is below tolerance, you are within that tolerance of the true solution.
* If \(\lambda\) is not easily bounded \(<1\), the hypothesis might fail—try another norm or restrict the domain.

---

### Bottom line

The Banach fixed‑point theorem gives a **powerful, algorithmic** guarantee: under a simple metric‑shrink condition in a complete space, the solution exists, is unique, and is reached by an explicit geometric‑rate iteration whose error you can monitor as you go.
