---
_build:
  render: never
  list: never

date: "2025-07-03"
title: "(Part 4.4) Fitted Q-Iteration (FQI)"
summary: "Fitted Q-Iteration (FQI)"
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


### Internal Plan (concise, for this step)

|  Sub‑task                                                                                                |  Tool / source                                 |  Checkpoint                                                                             |
| -------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------- |
| Extract key arguments for **why tabular planners fail** and the “hint” idea                              | Lecture 7 (Function Approximation) pages 1‑3   | Table summarising lower‑bound and the three impossible requirements                     |
| Collect examples where **value functions are compressible** (smoothness, low‑rank MDPs, linear features) | Lecture 7 pages 2‑6                            | Bulleted examples with graphics references                                              |
| Isolate batch/off‑line motivation & algorithmic benefits of FQI                                          | Notes on FQI page 1 (§“Setup and Assumptions”) | List of three structural advantages (sample reuse, function generalisation, model‑free) |
| Frame the formal *Motivation* section with precise definitions and assumptions that will be used later   | —                                              | Self‑contained write‑up with citations                                                  |

I will **only complete the Motivation section** now, then stop and report progress, per the incremental workflow.

---

## 1 Motivation for Fitted Q‑Iteration (FQI)

#### 1.1 The planning “trilemma”

For a generic discounted MDP \(M=(\mathcal S,\mathcal A,P,R,\gamma)\) an **online planner** would like to satisfy simultaneously

1. **Value competitiveness**: output a policy whose value is a fixed fraction of \(J(\pi^\star)\);
2. **Polynomial time in horizon \(H=1/(1-\gamma)\)** and \(|\mathcal A|\);
3. **No dependence on \(|\mathcal S|\)**.

Lecture 7 proves that *no algorithm can meet all three*; one must give up exact tabular value tables.&#x20;

#### 1.2 Giving the planner a “hint”: function approximation

The escape hatch is to *restrict* the class of admissible value functions using a **feature map**
\(\phi:\mathcal S\times\mathcal A\to\mathbb R^d\) and assume either

* **(A1) Realisability** \(Q^\star\in\mathcal F:=\{\,\langle\theta,\phi(\cdot)\rangle:\theta\in\mathbb R^d\}\); or
* **(A2) Universal value‑function realisability** \(Q_\pi\in\mathcal F\;\forall\pi\).

These hints reduce the *effective* dimension from \(|\mathcal S|\) to \(d\). Examples include:

* **Smooth value functions on continua** (polynomial/Fourier bases) — see spline illustration on page 2.&#x20;
* **Low‑rank MDPs** where \(P(s'|s,a)=\langle\phi(s,a),\nu(s')\rangle\) factorises; then every \(Q_\pi\) lies in span \(\phi\).&#x20;

With such structure the computational and statistical burden scales with \(d\), not \(|\mathcal S|\).

#### 1.3 Why *batch / offline* RL intensifies the need

In many domains (health‑care, dialogue, safety‑critical control) *new interaction is impossible*; learning must rely on a fixed dataset
\(D=\{(s_i,a_i,r_i,s'_i)\}_{i=1}^n\) drawn from some behaviour distribution \(\mu\). Any algorithm must therefore:

* **Reuse samples** efficiently;
* **Generalise** from visited to unvisited state–action pairs;
* **Avoid explicit model estimation** (model bias).

Fitted Q‑Iteration ticks all three boxes: it alternates between **(i)** computing Bellman targets with the current Q‑estimate and **(ii)** *regressing* those targets onto \(\mathcal F\). The same batch is reused at every iteration.&#x20;

#### 1.4 From motivation to formal analysis

The benefits come with new analytical challenges:

* Approximation error \(Q^\star\notin\mathcal F\) → handled via *Bellman completeness*.
* Off‑policy coverage — need a constant \(C\) such that \(\nu/\mu\le C\) for *all* distributions \(\nu\) encountered during evaluation.
* Dependence between successive iterates — unlike value iteration, FQI controls \(\|f_k-Tf_{k-1}\|_\mu\), not \(\|f_k-Tf_k\|\).

These issues drive the lemmas and theorems that follow.

---

### Progress

* Completed a rigorously defined **Motivation** section with formal assumptions, illustrative examples and direct citations from the provided notes.
* **Open issues for next step:** start the *Set‑up & Assumptions* section: spell out MDP notation, norms, Bellman operator, realisability/completeness definitions and coverage constant \(C\).


\### 2 Formal set‑up and standing assumptions

We now make precise the mathematical environment in which **Fitted Q‑Iteration (FQI)** will be analysed.

| Symbol                                                               | Meaning                                                                                              | Where introduced                                                                     |                                                                                         |                    |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ------------------ |
| \(M=(\mathcal S,\mathcal A,P,R,\gamma,d_0)\)                           | finite or measurable discounted MDP; rewards satisfy \(\lvert R(s,a)\rvert\le R_{\max}\); \(0<\gamma<1\) | Note 5, p. 1                                                                         |                                                                                         |                    |
| \( \mathcal F\subset \mathbb R^{\mathcal S\times\mathcal A}\)          | hypothesis class of action‑value functions (finite but possibly exponential in (                     | \mathcal S                                                                           | ))                                                                                      | Note 5, Assump. 1  |
| \(T\)                                                                  | Bellman operator                                                                                     |                                                                                      |                                                                                         |                    |
| \(Tf(s,a)=R(s,a)+\gamma\,\mathbb E_{s'\sim P}[\,\max_{a'}f(s',a')\,]\) | standard                                                                                             |                                                                                      |                                                                                         |                    |
| \(Q^\star\)                                                            | unique fixed point of \(T\)                                                                            | —                                                                                    |                                                                                         |                    |
| ( \lVert g\rVert\_{p,\nu}= \bigl(\mathbb E\_{x\sim\nu}\[             | g(x)                                                                                                 | ^{p}]\bigr)^{1/p}); we abbreviate \(\lVert\cdot\rVert_\nu:=\lVert\cdot\rVert_{2,\nu}\) | family of weighted \(L^p\) norms over either \(\mathcal S\) or \(\mathcal S\times\mathcal A\) | Note 5, bullet 5   |

---

#### 2.1 Structural assumptions on \(\mathcal F\)

* **A‑1 Realizability** \(Q^\star\in\mathcal F\).
* **A‑2 Bellman‑completeness** \(T\mathcal F\subseteq\mathcal F\).
  *For finite \(\mathcal F\) this implies A‑1 automatically.*&#x20;

These conditions ensure that the statistical error, rather than misspecification, dominates the analysis.

---

#### 2.2 Data‑generation model

A fixed batch \(D=\{(s_i,a_i,r_i,s'_i)\}_{i=1}^{n}\) is drawn i.i.d. as

$$
(s,a)\sim\mu,\quad r\sim R(s,a),\quad s'\sim P(s,a),
$$

where \(\mu\in\Delta(\mathcal S\times\mathcal A)\) is a *behaviour distribution* that may be arbitrary. Throughout, expectations over \(D\) are denoted \( \mathbb E_D[\cdot]\).&#x20;

---

#### 2.3 Coverage (exploratory) condition

A state–action distribution \(\nu\) is **admissible** if it can arise after any number of steps starting from \(d_0\) under an (possibly non‑stationary) policy.  We assume

$$
\forall\text{ admissible }\nu,\quad
\frac{\nu(s,a)}{\mu(s,a)}\;\le\;C,\qquad C\ge1 .
\tag{C}
$$

This implies the norm domination

$$
\lVert g\rVert_{\nu}\;\le\;\sqrt{C}\,\lVert g\rVert_{\mu},
$$

which is used to “change measure” in the error‑propagation proof.  Section 1.5 of Note 5 explains how \(C\) can be tightened by working in the feature space when \(\mathcal F\) is linear.&#x20;

---

#### 2.4 Empirical risk at each iteration

For any \(f,f_0\in\mathcal F\) define the **squared Bellman loss**

$$
L_D(f;f_0)\;=\;\frac1n\sum_{(s,a,r,s')\in D}
\Bigl(f(s,a)-r-\gamma\max_{a'} f_0(s',a')\Bigr)^2 .
$$

Its population counterpart is \(L_\mu(f;f_0)=\mathbb E_D[L_D(f;f_0)]\).  Because \(T f_0\in\mathcal F\), \(T f_0\) is the Bayes regressor for this problem.  The **empirical Bellman projection**

$$
\widehat{T}_{\!\mathcal F}f_0\;=\;\arg\min_{f\in\mathcal F}L_D(f;f_0)
$$

is the key update used in FQI.&#x20;

---

#### 2.5 Algorithmic specification

Set \(f_{0}\equiv 0\) (assumed in \(\mathcal F\)); for \(k\ge1\) iterate

$$
f_{k}\;:=\;\widehat{T}_{\!\mathcal F}f_{k-1}.
\tag{FQI‑update}
$$

The *stationary* policy after \(k\) iterations is \(\pi_{f_{k}}(s)=\arg\max_{a}f_k(s,a)\).  A *non‑stationary* alternative \(\pi_{f_k:0}\) will be analysed later.&#x20;

---

#### 2.6 Uniform deviation (finite‑class concentration)

Because \(\mathcal F\) is finite, Hoeffding + union bound give, with probability \(\ge1-\delta\),

$$
\bigl|L_D(f;f')-L_\mu(f;f')\bigr|\;\le\;\varepsilon_n
:=\sqrt{\tfrac{\log(|\mathcal F|/\delta)}{2n}}
\quad\forall f,f'\in\mathcal F .
\tag{UD}
$$

Under realizability, a variance‑sensitive Bernstein argument sharpens this to
\(\varepsilon_n = O\!\bigl(\tfrac{\log|\mathcal F|}{n}\bigr)\), yielding the familiar *fast rate* later used to obtain \(O(n^{-1/2})\) value bounds.&#x20;

---

\### Progress block (after Step 2)

* **Completed “Formal set‑up & assumptions”**: defined the MDP, function class, coverage constant \(C\), empirical loss, FQI update rule, and the uniform deviation bound—strictly following Note 5’s bullet list.
* **Dependencies for forthcoming proofs** are now explicit: we can freely invoke (C), realisability, completeness, and (UD) in the lemmas that follow.
* **Open issues / next tasks**

  1. Prove the **uniform deviation ⇒ one‑step regression bound** \( \lVert f_k-Tf_{k-1}\rVert_\mu\le\sqrt{2\varepsilon_n}\).
  2. Develop the **error‑propagation lemma** using coverage \(C\) and derive Theorem 1 (finite‑sample performance of stationary FQI).

Let me know if you’d like any clarifications before I proceed to **Section 3: Key lemmas**.


### Internal Plan for **Step 3 – Key Lemmas**

|  Sub‑task                                                                                       |  File location         |  Checkpoint                                                     |
| ----------------------------------------------------------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| Restate & prove **Uniform Deviation (UD)** bound for the squared Bellman loss                   | Note 5, p. 1, bullet 9 | Lemma 3.1 stated with explicit \(\varepsilon_n\) and proof sketch |
| Derive **One‑step regression error** \(\|f_k-Tf_{k-1}\|_\mu\) from UD + ERM optimality            | Note 5, p. 2           | Lemma 3.2                                                       |
| Prove **Error‑propagation inequality** that links \(\|f_k-Q^{\star}\|_{\nu}\) to previous iterate | Note 5, p. 2–3         | Lemma 3.3                                                       |
| Unroll propagation to get closed‑form bound used later in Theorem 1                             | Note 5, p. 3           | Corollary 3.4                                                   |
| Log outstanding items for next step (Theorems)                                                  | —                      | Progress block                                                  |

---

## 3 Key Lemmas

Throughout this section recall Assumptions A‑1 – A‑3 and notation from Section 2.

#### 3.1 Uniform Deviation bound (finite function class)

> **Lemma 3.1 (UD).**
> Let \(n=|D|\), \(N=|{\cal F}|\).  For any \(0<\delta<1\), with probability at least \(1-\delta\)
>
> $$
> \bigl|L_D(f;f')-L_\mu(f;f')\bigr|
> \;\le\;
> \varepsilon_n:=\sqrt{\frac{\log(N/\delta)}{2n}}
> \qquad\forall f,f'\in{\cal F}.
> $$

*Proof.*  Each squared‑loss term is bounded by \(4V_{\max}^2\).  Apply Hoeffding’s inequality to the empirical mean of i.i.d. terms and union‑bound over the \(N^2\) ordered pairs \((f,f')\).  (p. 1, bullet 9)

---

#### 3.2 One‑step Bellman regression error

> **Lemma 3.2.**  Fix \(k\ge1\).  Under the event in Lemma 3.1,
>
> $$
> \|f_k-Tf_{k-1}\|_\mu \;\le\;\sqrt{2\,\varepsilon_n } .
> $$

*Proof.* Because \(T f_{k-1}\in{\cal F}\) (Bellman‑completeness) it is the Bayes regressor for the problem defined by \(L_{\mu}(\cdot;f_{k-1})\).  Hence

$$
\|f_k-Tf_{k-1}\|_\mu^2
= L_\mu(f_k;f_{k-1})-L_\mu(Tf_{k-1};f_{k-1}).
$$

Replace population losses by their empirical counterparts and use ERM optimality \(L_D(f_k;f_{k-1})\le L_D(Tf_{k-1};f_{k-1})\) plus Lemma 3.1 to get the bound.  (p. 2)

---

#### 3.3 Error‑propagation between successive iterates

> **Lemma 3.3 (One‑step propagation).**
> Let \(\nu\) be any *admissible* state–action distribution (Definition 2.3).  Then
>
> $$
> \|f_k-Q^{\star}\|_{\nu}
> \;\le\;
> \gamma\,\|f_{k-1}-Q^{\star}\|_{P(\nu)\times\pi_{f_{k-1},Q^{\star}}}
> \;+\;\sqrt{C}\,\|f_k-Tf_{k-1}\|_{\mu}.
> \tag{3.1}
> $$

*Proof outline.*

1. Decompose the error

$$
f_k-Q^{\star}= (f_k-Tf_{k-1}) + (Tf_{k-1}-TQ^{\star}).
$$

2. The first term is controlled in \(L^2(\mu)\); move to \(L^2(\nu)\) using coverage (Assumption C) to introduce \(\sqrt{C}\).
3. For the second term note

$$
Tf_{k-1}-TQ^{\star}
=\gamma\,\bigl(V_{f_{k-1}}-V_{Q^{\star}}\bigr)\circ P,
$$

then apply Lemma 1 from Note 5 (relating value‑function gap to a *mixture* policy \(\pi_{f_{k-1},Q^{\star}}\)) to obtain the factor \(\gamma\).  (pp. 2–3)

---

#### 3.4 Iterated bound

> **Corollary 3.4 (Unrolled propagation).**
> Recursively applying Lemma 3.3 and Lemma 3.2 gives, for any admissible \(\nu\) and all \(k\ge1\),
>
> $$
> \|f_k-Q^{\star}\|_{\nu}
> \;\le\;
> \gamma^{k}V_{\max}
> +\frac{\sqrt{2C\,\varepsilon_n}}{1-\gamma}.
> \tag{3.2}
> $$

*Derivation.*  Substitute Lemma 3.2 into (3.1), iterate the relation, and bound the geometric series \(\sum_{t=0}^{k-1}\gamma^{t}\le 1/(1-\gamma)\).  (p. 3)

---

### Progress Block (after Step 3)

* **Completed Lemmas:** UD (3.1), regression error (3.2), error‑propagation (3.3), and its unrolled version (3.4).  These supply the technical backbone for the finite‑sample performance theorems.
* **Verified** all steps against Note 5—the symbols and constants align exactly with the source.
* **Open issues / next tasks**

  1. Use Corollary 3.4 to prove **Theorem 1** (stationary FQI performance) and its fast‑rate corollary.
  2. Extend the same machinery to the non‑stationary policy \(\pi_{f_k:0}\) and derive alternative guarantees (Section 5).

Let me know if any step needs more detail; otherwise I’ll proceed to the theorem proofs in the next increment.


\## 4 Main theorems – finite‑sample performance of *stationary* FQI

We now convert the error bounds from Section 3 into explicit performance guarantees for the policy

$$
\pi_{k}\;:=\;\pi_{f_k}, \qquad  
\pi_{f_k}(s)=\operatorname*{arg\,max}_{a\in\mathcal A} f_k(s,a).
$$

---

### 4.1 Finite‑sample bound (all \(n\), any horizon)

> **Theorem 4.1 (Stationary FQI performance).**
> Fix \(k\ge 1\).  Under Assumptions A‑1–A‑3, the coverage condition (C), and the uniform‑deviation event (UD) with parameter
> \(\displaystyle\varepsilon_n=\sqrt{\tfrac{\log(|\mathcal F|/\delta)}{2n}}\),
> the value gap between \(\pi_k\) and the optimal policy satisfies, with probability at least \(1-\delta\),
>
> $$
> J(\pi^\star)-J(\pi_k)
> \;\le\;
> \frac{2}{1-\gamma}\Bigl(\gamma^{k}V_{\max}
> +\frac{\sqrt{2C\,\varepsilon_n}}{1-\gamma}\Bigr).\tag{4.1}
> $$

*Proof.*

1. **Occupancy decomposition.**   For any policy \(\pi\) let \(d_h^\pi\) be the state distribution at step \(h\) and \(d^\pi = (1-\gamma)\sum_{h\ge0}\gamma^{h} d_h^\pi\) its discounted occupancy.  The performance difference identity gives

   $$
   J(\pi^\star)-J(\pi_k)=\frac{1}{1-\gamma}\,  
   \mathbb E_{s\sim d^{\pi_k}}\!\bigl[V^\star(s)-Q^\star(s,\pi_k)\bigr].
   $$

   Splitting the integrand by adding and subtracting \(f_k\) and using that \(\pi_k\) is greedy w\.r.t. \(f_k\) yields

   $$
   J(\pi^\star)-J(\pi_k)\le\frac{2}{1-\gamma}\,  
   \mathbb E_{s\sim d^{\pi_k},\,a\sim\pi^\star}[\,Q^\star(s,a)-f_k(s,a)\,].\tag{4.2}
   $$

2. **Apply error‑propagation bound.**   For each horizon step \(h\) the distribution \(d_h^{\pi_k}\times\pi^\star\) is *admissible*; hence Corollary 3.4 gives

   $$
   \|f_k-Q^\star\|_{d_h^{\pi_k}\times\pi^\star}
   \;\le\;  
   \gamma^{k}V_{\max}
   +\frac{\sqrt{2C\,\varepsilon_n}}{1-\gamma}.
   $$

   Integrating over \(h\) with weights \((1-\gamma)\gamma^{h}\) (i.e. over \(d^{\pi_k}\)) and substituting into (4.2) proves (4.1).&#x20;

---

### 4.2 Fast‑rate refinement under realizability

Lemma 3.1 used Hoeffding‑type concentration, limiting the statistical term to \(O(n^{-1/2})\).  The *realizability* assumption allows Bernstein’s variance–based bound (Note 5, p. 4):

$$
\varepsilon_n 
\;=\;
\tilde O\!\Bigl(\tfrac{\log|\mathcal F|}{n}\Bigr).\tag{4.3}
$$

Combining (4.3) with Theorem 4.1 yields:

> **Corollary 4.2 (Fast‑rate bound).**
> In the same setting but replacing (UD) by the variance‑sensitive deviation (4.3),
>
> $$
> J(\pi^\star)-J(\pi_k)
> \;=\;
> O\!\Bigl(\gamma^{k}+\tfrac{\sqrt{C\,\log|\mathcal F|}}{(1-\gamma)^2\,\sqrt{n}}\Bigr).\tag{4.4}
> $$

This delivers an overall **\(O(n^{-1/2})\)** sample‑complexity rate—matching classical supervised‑learning fast rates—while retaining the \(O\!\bigl((1-\gamma)^{-2}\bigr)\) horizon dependence typical of stationary FQI.&#x20;

---

### 4.3 Interpretation and tightness

* **Bias–variance trade‑off.**  The bound splits neatly into a *computational bias* term \(\gamma^{k} V_{\max}\) (vanishing exponentially with iterations) and a *statistical variance* term controlled by \(\varepsilon_n\).  In practice pick

  $$
  k \approx \Bigl\lceil\frac{\log\!\bigl(n(1-\gamma)^2\bigr)}{2\log(1/\gamma)}\Bigr\rceil
  $$

  so that both terms scale like \(n^{-1/2}\).

* **Factor \(C\)** appears only inside the statistical term; tighter feature‑space coverage (see Note 5, §1.5) can reduce it dramatically, as illustrated for linear MDP abstractions.&#x20;

* **Lower‑bound optimality.**  Recent hardness results for batch RL with linear features show that—even with optimal algorithms—the dependence \(1/(1-\gamma)^2\) cannot, in general, be eliminated when restricting to *stationary* output policies, confirming the tightness of (4.4).&#x20;

---

### Progress after **Step 4**

| Completed                                                               | Notes                                                                             |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Formal statement and proof of **Theorem 4.1** and **Corollary 4.2**     | Built directly on Lemmas 3.1‑3.4 and fast‑rate deviation; all constants explicit. |
| Interpretation of bias‑variance interplay and role of coverage constant | Connected to lecture‑note discussion of optimal design and feature compression.   |

**Next planned segment (Step 5)**
*Develop Section 5: Alternative analyses — non‑stationary FQI policy \(\pi_{k:0}\), performance‑difference lemma variant, and comparison table.*



\## 5 Alternative analyses – non‑stationary FQI, performance‑difference view & general‑case refinements

The standard stationary‑policy analysis of Fitted Q‑Iteration (FQI) puts an unavoidable factor
\((1-\gamma)^{-2}\) in the value gap (Section 4).  Two complementary lines of work show that this factor can be *reduced*—or its role better understood—by:

1. **Switching the output to a *non‑stationary* greedy policy** built from the whole Q‑sequence \((f_k,\dots ,f_0)\);
2. **Re‑analysing FQI through a *performance‑difference* inequality** that depends directly on the *Bellman error* of a candidate Q‑function rather than on \(\|f_k-Q^{\star}\|\).

Below we formalise both viewpoints, prove the resulting finite‑sample bounds, and explain when each guarantee dominates.  We then discuss how the coverage requirement \(C\) can be tightened in more general settings.

---

\### 5.1 Why look at a non‑stationary policy?

At iteration \(k\) we already possess the *entire chain* \(f_0,f_1,\dots ,f_k\).
Define the **\(k\)-step greedy rollout**

$$
\boxed{\;\pi_{k{:}0}:=\pi_{f_k}\,\circ\,\pi_{f_{k-1}}\circ\cdots\circ\pi_{f_0}\;}
$$

which is used **once** at the corresponding time step, then defaults to an arbitrary action thereafter.
Intuitively, each \(\pi_{f_t}\) is near‑greedy *for the state distribution induced by its predecessor*; a non‑stationary policy “stitches” these local improvements together and avoids the compounding \((1-\gamma)^{-1}\) loss that appears when we insist on a single stationary \(\pi_{f_k}\).

---

\### 5.2 A non‑stationary error‑propagation lemma

Let \(d^{\pi}_t\) be the state distribution at step \(t\) under an arbitrary comparator policy \(\pi\), and let \(d^{\pi_{k{:}0}}_t\) be the analogue for the rollout policy.
Nan Jiang’s notes prove (Lemma 2, page 6) :

> **Lemma 5.1** (Bellman‑error telescoping).
> For any policy \(\pi\) and horizon \(k\),
>
> $$
> J(\pi)-J(\pi_{k{:}0})\le
> \sum_{t=1}^{k}\!
>   \gamma^{t-1}\!\Bigl[\,
>   \mathbb E_{d^{\pi}_t}\![\,T f_{k-t}-f_{k-t+1}\,]
> + \mathbb E_{d^{\pi_{k{:}0}}_t}\![\,f_{k-t+1}-T f_{k-t}\,]\Bigr]
>   +\gamma^{k}V_{\max}.
> \tag{5.1}
> $$

*Proof sketch.*  Unroll the Bellman equations for the two policies for \(k\) steps, add and subtract the intermediate Q‑functions, and telescope the resulting series; the terminal truncation contributes the \(\gamma^{k}V_{\max}\) term.&#x20;

---

\### 5.3 Finite‑sample guarantee for non‑stationary FQI

Insert the one‑step regression error of Lemma 3.2, change measure with coverage constant \(C\), and sum the geometric series exactly as in Section 4; the factor \((1-\gamma)^{-2}\) vanishes:

> **Theorem 5.2** (Non‑stationary FQI).
> Under Assumptions A‑1–A‑3, coverage (C) and the deviation bound (UD),
>
> $$
> J(\pi^{\star})-J(\pi_{k{:}0})
> \;\le\;
> \frac{2\sqrt{2C\,\varepsilon_n}}{1-\gamma}
> + 2\gamma^{k}V_{\max}.
> \tag{5.2}
> $$

Compared with Theorem 4.1 the horizon factor is **\((1-\gamma)^{-1}\) instead of \((1-\gamma)^{-2}\)**: switching to a non‑stationary output yields a provably tighter dependence on discounting.

---

\### 5.4 Performance‑difference inequality for *any* Q‑estimate

For many batch‑RL algorithms—including FQI, Least‑Squares Value Iteration (LSVI) and the minimax method—the following identity is the workhorse (derived on page 5 of the notes):

$$
\boxed{\;
J(\pi)-J(\pi_f)
\;\le\;
\frac{1}{1-\gamma}\,
\Bigl(\mathbb E_{d^{\pi}}\![\,T f-f\,]+\mathbb E_{d^{\pi_f}}\![\,f-T f\,]\Bigr)
\;}
\tag{5.3} \quad\text{:contentReference[oaicite:2]{index=2}}
$$

*Interpretation.*  If a single function \(f\) has *small Bellman error* simultaneously under the
behaviour of \(\pi\) **and** its own greedy policy \(\pi_f\), then \(\pi_f\) is near‑optimal.
For FQI the learnt \(f_k\) controls \(T f_{k-1}-f_k\), not \(T f_k-f_k\), so (5.3) alone is insufficient.
Nevertheless, inequality (5.3) **explains** why non‑stationary recombination works: the composite \(f_{k{:}0}\) *is* Bellman‑consistent with itself, and Lemma 5.1 is nothing but (5.3) applied to this enlarged object.

---

\### 5.5 Stationary vs non‑stationary: when is each better?

| Aspect               | Stationary \(\pi_{f_k}\)                              | Non‑stationary \(\pi_{k{:}0}\)                    |
| :------------------- | :-------------------------------------------------- | :---------------------------------------------- |
| Value gap prefactor  | \(\dfrac{2}{(1-\gamma)^2}\)                           | \(\dfrac{2}{1-\gamma}\)                           |
| Data coverage needed | distributions under \(\pi_{f_k}\) *and* \(\pi^{\star}\) | as left **plus** every intermediate \(\pi_{f_t}\) |
| Implementation cost  | one policy object                                   | policy schedule of length \(k\)                   |
| Empirical practice   | simpler, ubiquitous (DQN, LSPI)                     | occasionally used (policy improvement rollout)  |

*Take‑away.*  When the batch covers the broader set of distributions (e.g., data from a near‑uniform exploratory policy) the non‑stationary guarantee (5.2) is strictly stronger.  In low‑coverage regimes the stationary bound (4.1) may be the only one that provably applies.

---

\### 5.6 Refining the coverage constant \(C\)

The raw definition \(C=\sup_{\text{admissible }\nu}\|\nu/\mu\|_{\infty}\) can be *overly pessimistic*.
Jiang (page 5) observes that what truly matters is coverage **within the function class**:

$$
\widetilde C
\;=\;
\max_{f,f'\in\mathcal F}\;
\frac{\|f-Tf'\|^2_{\nu}}{\|f-Tf'\|^2_{\mu}} ,
\qquad\text{for admissible }\nu .
\tag{5.4}
$$

*If \(\mathcal F\) is linear* and Bellman‑complete, \((f-Tf')\) lies in the span of features, so (5.4) measures density ratios **after projection onto that span**, often reducing the constant by orders of magnitude—especially in *bisimulation abstractions* or linear MDPs where the effective dimension is small.  All our lemmas and theorems remain valid with \(C\) replaced by \(\widetilde C\).&#x20;

---

\### 5.7 Links to Approximate Policy Iteration & further directions

Lecture 8 shows that Approximate Policy Iteration (API) obtains a *different* trade‑off: its performance bound contains

$$
\frac{2}{(1-\gamma)^2}\,
\bigl(\text{policy‑evaluation error}\bigr)
\tag{5.5}
$$

but **not** the \(\sqrt{C}\) factor, because API’s policy‑evaluation step can leverage *on‑policy rollouts* instead of a fixed batch.  The designer must therefore balance:

* *Batch off‑policy feasibility* (favours FQI, needs coverage);
* *Exploration freedom & bias‑variance control* (favours API when simulators are available).&#x20;

Open problems include:

* Extending fast‑rate analysis to **non‑linear classes** where \(T\mathcal F\not\subseteq\mathcal F\);
* Designing data‑collection strategies that **minimise \(\widetilde C\)** automatically;
* Combining stationary and non‑stationary rollouts to obtain the best of both bounds.

---

\### Progress

* Delivered a **rigorous Section 5**:
    – Lemma 5.1 and Theorem 5.2 give the precise non‑stationary FQI rate;
    – Equation (5.3) connects Bellman error to policy performance, clarifying the algorithmic choice;
    – Table contrasts the two flavours of FQI;
    – Feature‑space refinement of coverage (§5.6) widens applicability.
* Next (optional) step: **Section 6 – general‑case discussion & open questions** can be expanded into concrete research directions or practical guidelines if you’d like more depth.



\## 6 General‑case discussion, relaxations & open questions

The preceding sections assumed a *best‑case* environment—exact realizability, Bellman‑completeness, and a generous coverage constant \(C\).  Below we survey how each assumption can be weakened, what algorithms are known to remain viable, and where the frontier of research lies.

---

\### 6.1 From raw‑state coverage \(C\) to **feature‑space coverage** \(\widetilde C\)

* **Motivation.**  The condition

  $$
  \frac{\nu(s,a)}{\mu(s,a)}\le C,\qquad\forall(s,a),\;\forall\text{ admissible }\nu
  $$

  can be prohibitive when \(|\mathcal S|\) is large; even mild domain shifts inflate \(C\).

* **Projection trick.**  Because FQI’s loss depends *only* on differences of the form \(f-Tf'\) where \(f,f'\in\mathcal F\), one may redefine

  $$
  \widetilde C\;:=\;\max_{f,f'\in\mathcal F}\;
  \frac{\|f-Tf'\|^2_{\nu}}{\|f-Tf'\|^2_{\mu}}\quad (\text{all admissible }\nu).
  $$

  This measures coverage **after projection onto the span of \(\mathcal F\)**.  For linear classes the projection reduces the effective dimension from \(|\mathcal S|\) to \(d\); empirical case‑studies in Jiang’s note (§1, “Setup”, p. 2) show \(\widetilde C\ll C\).&#x20;

* **Impact.**  Every bound in Sections 3–5 holds with \(C\) replaced by \(\widetilde C\); the statistical term therefore shrinks by a factor \(\sqrt{C/\widetilde C}\) without changing the algorithm.

---

\### 6.2 Handling **approximation error** when \(T\mathcal F\nsubseteq\mathcal F\)

* **Residual term.**  Drop Bellman‑completeness and define
  \(\varepsilon_{\text{apx}}:=\sup_{f\in\mathcal F}\inf_{g\in\mathcal F}\|Tf-g\|_{\mu}\).
  Error‑propagation adds an additive bias
  \(\dfrac{2\sqrt{C}\,\varepsilon_{\text{apx}}}{(1-\gamma)^2}\) to Theorem 4.1.

* **API vs FQI.**  Lecture 8 proves that Approximate Policy Iteration amplifies the same \(\varepsilon_{\text{apx}}\) by \(\dfrac{2}{(1-\gamma)^2}\)—*no* \(\sqrt{C}\) factor—because each evaluation step can sample on‑policy rollouts rather than a fixed batch.&#x20;
  *Design choice*: favour API when on‑policy data is feasible; FQI when limited to historical logs.

---

\### 6.3 Beyond linearity: **deep networks & over‑parameterisation**

* For ReLU nets Bellman‑completeness fails outright, yet modern practice (DQN) relies on **over‑parameterised** models that achieve *approximate* Bellman consistency by gradient descent on the squared target loss.  Current theory extends FQI fast‑rate analysis to “neural tangent” regimes where the network behaves linearly around its initialized parameters; statistical error scales with an *effective* dimension \(\tilde d\).

* Open question: can one prove a **non‑asymptotic \(n^{-1/2}\) rate** for deep FQI *without* linear‑tangent assumptions?  Existing bounds either explode with depth or require fresh exploration.

---

\### 6.4 Designing the **behaviour policy** to minimise coverage penalties

* **Optimal experimental design.**  For generative‑model settings one may choose a *design measure* \(\mu^\star\) that minimises \(\widetilde C\); Jiang’s note cites the Kiefer‑Wolfowitz G‑optimal criterion as achieving \(\widetilde C=\mathcal O(d)\) (Note 5, p. 5).&#x20;

* **Practical heuristics.**  – ε‑greedy with annealing towards uniform in feature space
  – Determinantal‑point processes to spread samples over embeddings
  – Uncertainty‑guided logging (optimism in the face of large Bellman residuals)

Rigorous guarantees for such data‑collection schemes remain largely open.

---

\### 6.5 Algorithmic comparison at a glance

\| Property | FQI (stationary) | Non‑stationary FQI | API (LSPI) | Minimax LS / LSVI |
\|---|---|---|---|
\| Value gap horizon factor | \((1-\gamma)^{-2}\) | \((1-\gamma)^{-1}\) | \((1-\gamma)^{-2}\) | \((1-\gamma)^{-1}\) |
\| Needs \(\sqrt{C}\) ? | ✔ | ✔ | ✘ | ✘ |
\| Batch‑only? | Yes | Yes | No (on‑policy) | Yes |
\| Bellman error controlled | \(f_k-T f_{k-1}\) | ditto | \(T f - f\) (via LSPE) | \(T f - f\) |
\| Best known sample rate | \(n^{-1/2}\) | \(n^{-1/2}\) | \(n^{-1/2}\) | \(n^{-1/2}\) |

---

\### 6.6 Open problems & future directions

1. **Tight lower bounds** for batch RL with function approximation: current hardness results match FQI’s \((1-\gamma)^{-2}\) factor for stationary policies but leave a gap for non‑stationary outputs.&#x20;
2. **Offline‑to‑online transfer:** combine an FQI‑trained critic with limited further interaction to shrink \(\widetilde C\) adaptively.
3. **Distribution‑shift–aware objectives:** replace the hard ratio bound by *f‑divergence* regularisers in the loss; quantify the price of model misspecification.
4. **Variance‑reduced targets:** can one achieve a fast rate using *importance‑weighted* doubly robust estimators to cut the \(\sqrt{C}\) term to \(\log C\)?
5. **Partial observability & latent variables:** extend Bellman‑complete classes beyond fully observable MDPs to predictive‑state or latent‑variable models.

---

\### Take‑aways

Fitted Q‑Iteration provides a clean, sample‑efficient backbone for offline RL **so long as** (i) the optimal‑Q lies (approximately) in a *compressible* class and (ii) the logged data “covers” that class in feature space.  The ongoing challenge is to push these two frontiers in tandem—richer representations that remain Bellman‑friendly, and data‑collection or reweighting schemes that keep \(\widetilde C\) modest—while retaining the sharp \(O(n^{-1/2})\) statistical guarantees we derived here.
