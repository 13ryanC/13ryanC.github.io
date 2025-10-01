---
_build:
  render: never
  list: never

date: "2025-07-11"
title: "(4.2) Function Approximation, Lower Bounds & Realizability – From LSPI to TensorPlan"
summary: "We move beyond tabular online‑planning and show how linear representations, tight lower bounds and new optimistic planners reshape the landscape."
lastmod: "2025-07-11"
category: "Notes"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

Lec 7, 8, 9, 10, 11

## 1 Why a *Part II*?

Section 4.1 established that *sampling a sparse look‑ahead tree* yields a query cost independent of |S| but still exponential in the effective horizon \(k\) and the branching factor \(A\).  
The natural next question is:

> *Can clever representations, or cleverer algorithms, break those exponential barriers?*  

Lectures 7‑11 give a surprisingly complete answer.  
Below is a stitched‑together narrative that hits the high‑points:

---

## 2 Linear Features ≈ Compression for Values (Lec 7)

### 2.1 The setup  
A **feature‑map** \(\phi:S\timesA\to\mathbb R^{d}\) lets us *compress* action‑value functions:

\[
q(s,a)\approx\langle \phi(s,a),\theta\rangle ,
\]

so optimisation moves from \(|S|\)‑dimensional tables to \(d\)‑dimensional parameter vectors.  
Two “hints” (assumptions) appeared:  

| Code | Meaning |
|---|---|
| **B1(\(\varepsilon\))** | *The* \(q^\*\) lies within \(\varepsilon\) of the feature span. |
| **B2(\(\varepsilon\))** | *All* policy value‑functions \(q^{\pi}\) lie within \(\varepsilon\). |

B2 ⇒ B1, but is much stronger. :contentReference[oaicite:0]{index=0}

### 2.2 Low‑rank & “linear” MDPs  
Lecture 7 shows several kernels (e.g. *homoscedastic noise* or *factored transitions*) that automatically satisfy B2 with small \(d\).  
Hence linear features are *not* mere convenience – sometimes they are the correct model. :contentReference[oaicite:1]{index=1}

---

## 3 Approximate Policy Iteration & LSPI (Lec 8)

### 3.1 Why LSPI works  
*Least‑Squares Policy Iteration* (LSPI) constrains every policy‑evaluation step to the feature span and then performs a greedy step.  

*Key technical trick:* choose **G‑optimal design points** – a set \(C\subseteq S\timesA\) of size \(\tilde O(d^{2})\) – so that regression error *outside* \(C\) is inflated by at most \(\sqrt d\).  
With \(m\) Monte‑Carlo roll‑outs per design point and a truncated horizon \(H\):

\[
\|q^{\pi}-\widehat q^{\pi}\|_\infty
\le
(1+\sqrt d)\varepsilon_{\text{approx}}

\tilde O\Bigl(
\frac{\gamma^{H}}{1-\gamma}

\sqrt{\frac{\log |C|}{m(1-\gamma)^{2}}}
\Bigr). \quad
\]  
(See Lemma “LSPE extrapolation control”) :contentReference[oaicite:2]{index=2}

### 3.2 Performance bound  
After \(K=O\bigl(\tfrac1{1-\gamma}\log\tfrac1\delta\bigr)\) iterations,  

\[
v^{\pi_{K}} \ge
v^\* - O\Bigl(
\frac{\varepsilon_{\text{approx}}+\varepsilon_{\text{stat}}}{(1-\gamma)^{2}}
\Bigr).
\]

Critically, **state‑space size never appears**; the cost is polynomial in \((d,1/(1-\gamma))\). :contentReference[oaicite:3]{index=3}

---

## 4 Hard Limits: Lower‑bound Machinery (Lec 9)

### 4.1 “Needle‑in‑a‑haystack” with large *A*  
If \(A\) is allowed to grow like \(\exp(d)\), any planner—*no matter how smart*—needs  

\[
\Omega\Bigl(\exp\bigl(\tfrac{d\varepsilon^{2}}{32\delta^{2}}\bigr)\Bigr)
\]

queries before it can rule out enough feature vectors to act \(\delta\)‑optimally.  
Proof leverages the Johnson–Lindenstrauss (JL) packing to generate *almost‑orthogonal* rows of \(\Phi\) and a high‑probability **needle lemma** (one non‑zero in a huge binary array). :contentReference[oaicite:4]{index=4}

### 4.2 Small *A*, finite horizon  
Even when \(A\) is constant, a depth‑\(H\) tree forces  

\[
\widetilde\Omega\Bigl(\frac{A^{H}}{H}\Bigr)
\]

queries unless \(H\) is itself smaller than the JL packing number \(u(d,\varepsilon,\delta)\).  
Hence the exponential dependence on either \(d\) *or* \(H\) is *information‑theoretic*. :contentReference[oaicite:5]{index=5}

---

## 5 Realizability Revisited (Lec 10)

### 5.1 Switching metrics: only \(q^\*\) must fit  
Suppose **only the *optimal* \(q^\*\) is realizable** (B1 with \(\varepsilon=0\)).  
One might hope this weaker promise makes life easier – it does *not*.  

A cleverly designed *tree with exponentially many actions* shows that any \(\delta\)‑sound planner still needs  

\[
\exp\bigl(\Omega(d)\bigr)
\]

queries.  The proof mixes the large‑\(A\) construction with stage‑indexed scaling tricks so that the “good” action gap remains constant across the tree.  :contentReference[oaicite:6]{index=6}

---

## 6 Escaping the Trap: **TensorPlan** (Lec 11)

### 6.1 Change the objective  
Lecture 11 flips the lens again: require **only \(v^\*\) (state values)** to be realizable and keep \(A\) *constant*.  
Under this *v‑realizability* assumption, TensorPlan achieves **poly\((d,H,1/\delta)\)** query complexity.

### 6.2 How TensorPlan works  

1. **Lift to tensors.**  
   The *discriminant*  
   \(\Delta(s,a,h,\theta)=r_a(s)+\langle P_a(s)\phi_{h+1},\theta\rangle-\phi_h(s)^\top\theta\)  
   is linear in the \(A\)‑fold tensor product
   \(F(\theta)=\bigotimes_{a=1}^{A}(1,\theta^\top)^\top\).  
   Local Bellman consistency at \((s,h)\) is simply  
   \(\prod_{a}\Delta(s,a,h,\theta)=0\). :contentReference[oaicite:7]{index=7}  

2. **Hypothesis set \(\Theta\).**  
   Start with the Euclidean ball \(\|\theta\|_2\le B\).  
   Every time a sampled transition violates consistency, cut \(\Theta\) with the linear constraint \(F(\theta)^\top x=0\).

3. **Optimism & elimination.**  
   Pick \(\theta^+=\arg\max_{\theta\in\Theta}\phi_0(s_0)^\top\theta\),  
   roll it out greedily *only until* you spot a violation, then shrink \(\Theta\) again.

Because each cut is orthogonal to all previous ones, at most \((d+1)^{A}-1\) cuts can occur, so total queries are  

\[
mH(d+1)^{A}
\quad\text{with}\quad
m=O\Bigl(\frac{(H+B)^{2}}{\delta^{2}}\Bigr).
\] :contentReference[oaicite:8]{index=8}  

### 6.3 Surprising side‑effect  
TensorPlan competes with **the best deterministic policy *whose* \(v^\pi\) is realizable**, even if \(q^\*\) itself is *not*. The aggressive cuts remember only “surprising” transitions; everything else is ignored.  

---

## 7 Take‑aways

| Myth | Reality |
|---|---|
| “Linear features always make planning easy.” | Only under *state‑value* realizability **and** small \(A\). Large action sets re‑introduce exponential hardness. |
| “Better approximation ⇒ exponential speed‑up.” | Sometimes yes (TensorPlan), sometimes not (B1 lower bound). |
| “Off‑the‑shelf LSPI is enough.” | LSPI is powerful under B2, but *sub‑optimal* for long horizons with small \(d\). |

---

## 8 Open Problems

1. **Computational tractability of TensorPlan.**  
   Keeping \(\Theta\) as an intersection of \(\le (d+1)^{A}\) half‑spaces may be NP‑hard; no poly‑time implementation is known.  
2. **Online‑access only simulators.**  
   TensorPlan needs “local reset” access. Can we remove that requirement?  
3. **Beyond linearity.**  
   Do analogous guarantees exist for *non‑linear* (e.g. neural) representations without extra assumptions?

*Stay tuned for Part III, where we bring these theoretical insights into deep‑RL practice…*

---

*References*  
CS & colleagues, “Function Approximation”, “Approximate Policy Iteration”, “Limits of Query‑Efficient Planning”, “Planning under \(q^\*\) Realizability”, “Planning under \(v^\*\) Realizability (TensorPlan I.)”, 2021‑2023 lecture notes. 
