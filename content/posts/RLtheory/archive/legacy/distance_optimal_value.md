---
date: "2025-06-30"
title: "Distance of optimal value function"
summary: "Distance of optimal value function"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

Let

$$
T:\mathbb{R}^{|S|}\longrightarrow\mathbb{R}^{|S|}, \qquad  
(TV)(s)\;=\;\max_{a\in A}\sum_{s'\in S}P(s,a,s')\,
\Bigl[R(s,a,s')+\gamma\,V(s')\Bigr],
$$

be the **Bellman-optimality operator** for a discounted Markov decision process,
with discount factor $0\le\gamma<1$.
$T$ is a **$\gamma$-contraction** on the Banach space $(\mathbb{R}^{|S|},\|\cdot\|_\infty)$:

$$
\|T U - T V\|_\infty \;\le\; \gamma\,\|U-V\|_\infty 
\qquad\forall\,U,V\in\mathbb{R}^{|S|}.
\tag{1}
$$

---

### Fixed point and value-iteration sequence

* Unique fixed point (optimal value function): $V^\star=T V^\star$.
* Value-iteration iterate: $V_{k+1}=T V_k$, equivalently $V_k=T^k V_0$.

---

### Geometric error bound

Applying (1) with $U=V_k$ and $V=V^\star$,

$$
\|V_{k+1}-V^\star\|_\infty
=\|T V_k - T V^\star\|_\infty
\;\le\;\gamma\,\|V_k - V^\star\|_\infty .
$$

By induction,

$$
\boxed{\;
      \|V_k - V^\star\|_\infty 
      \;\le\; 
      \gamma^{\,k}\,\|V_0 - V^\star\|_\infty
      \;}
      \qquad(k=0,1,2,\dots).
$$

---

### Interpretation

* **“Distance’’** to $V^\star$: $d_k=\|V_k-V^\star\|_\infty$.
* **Convergence rate**: the constant $c=\gamma\in(0,1)$.

Hence

$$
d_k \;=\; c^{\,k}\,d_0,
$$

i.e. the error after $k$ iterations is the initial error multiplied by a factor $c^k$ that shrinks **exponentially** fast.

Below is a step‑by‑step (and assumption‑by‑assumption) derivation of the **geometric error bound** for value iteration in a finite, discounted Markov decision process (MDP).  Nothing is left implicit: every inequality and logical jump is spelled out.

---

## 1. Formal setting

| Symbol           | Meaning                   | Assumption              |                                             |                       |
| ---------------- | ------------------------- | ----------------------- | ------------------------------------------- | --------------------- |
| $S$              | finite set of states, (   | S                       | <\infty)                                    | —                     |
| $A$              | finite set of actions     | —                       |                                             |                       |
| $P(s,a,s')$      | transition probability    | $ \sum_{s'}P(s,a,s')=1$ |                                             |                       |
| $R(s,a,s')$      | one–step reward (bounded) | (                       | R                                           | \le R\_{\max}<\infty) |
| $\gamma$         | discount factor           | $0\le\gamma<1$          |                                             |                       |
| (v\in\mathbb R^{ | S                         | })                      | column vector; $v(s)$ is value of state $s$ | —                     |

We work in the Banach space $\bigl(\mathbb R^{|S|},\|\cdot\|_\infty\bigr)$ with

$$
\|v\|_\infty \;=\;\max_{s\in S}|v(s)|.
$$

---

## 2. The Bellman‑optimality operator $T$

Define

$$
(Tv)(s)\;:=\;\max_{a\in A}\sum_{s'\in S} P(s,a,s')\bigl[R(s,a,s')+\gamma\,v(s')\bigr], 
\qquad \forall\,s\in S.
$$

### 2.1 $T$ is a $\gamma$-contraction

Take any two value vectors $u,v$.  Fix an arbitrary state $s$ and let
$a^\star\in\arg\max_a\sum_{s'}P(s,a,s')[R+\gamma\,u]$ (one maximizing action for $Tu$ in $s$).

$$
\begin{aligned}
|(Tu)(s)-(Tv)(s)|
&= \Bigl|\sum_{s'}P(s,a^\star,s')\bigl[R(s,a^\star,s')+\gamma\,u(s')\bigr]
        -\max_{a'}\sum_{s'}P(s,a',s')\bigl[R+\gamma\,v\bigr]\Bigr|\\[2mm]
&\le \Bigl|\sum_{s'}P(s,a^\star,s')\bigl[R+\gamma\,u\bigr]
        -\sum_{s'}P(s,a^\star,s')\bigl[R+\gamma\,v\bigr]\Bigr| \quad (\text{by maximizer})\\[2mm]
&= \gamma\Bigl|\sum_{s'}P(s,a^\star,s')\bigl[u(s')-v(s')\bigr]\Bigr|\\[2mm]
&\le \gamma\,\|u-v\|_\infty\sum_{s'}P(s,a^\star,s')\\[2mm]
&= \gamma\,\|u-v\|_\infty .
\end{aligned}
$$

Taking the maximum over $s$ gives

$$
\boxed{\;
\|Tu-Tv\|_\infty\;\le\;\gamma\|u-v\|_\infty
\;} \tag{C}
$$

so $T$ is indeed a contraction with modulus $\gamma<1$.

---

## 3. Existence and uniqueness of the fixed point $V^\star$

The **Banach fixed‑point theorem** says:

*Because $T$ is a contraction on a complete metric space, it has a unique fixed point, and iteratively applying $T$ from any starting point converges to that point.*

Therefore, there is a unique $V^\star\in\mathbb R^{|S|}$ such that

$$
T\,V^\star = V^\star,
$$

and $V^\star$ is the optimal value function of the MDP.

---

## 4. Value‑iteration scheme

Choose any initial vector $V_0$ (e.g., $0$ or a heuristic).
Define recursively

$$
V_{k+1} \;:=\; T\,V_k, 
\qquad k=0,1,2,\dots
$$

so $V_k = T^k V_0$.

---

## 5. Deriving the geometric error bound

Let the “distance’’ at iteration $k$ be
$d_k := \|V_k - V^\star\|_\infty$.

### 5.1 One‑step reduction

By the contraction property (C) with $u=V_k,\; v=V^\star$:

$$
d_{k+1} \;=\;\|V_{k+1}-V^\star\|_\infty
          \;=\;\|T V_k - T V^\star\|_\infty
          \;\le\;\gamma\,\|V_k - V^\star\|_\infty
          \;=\;\gamma\,d_k.
\tag{1}
$$

### 5.2 Induction over $k$

Base case $k=0$: $d_0 = \|V_0 - V^\star\|_\infty$ (trivial).

Induction hypothesis: $d_k \le \gamma^{\,k} d_0$.

Induction step using (1):

$$
d_{k+1}\;\le\;\gamma\,d_k
         \;\le\;\gamma\bigl(\gamma^{\,k}d_0\bigr)
         \;=\;\gamma^{\,k+1} d_0.
$$

Thus the statement holds for all $k\in\mathbb N$.

### 5.3 Final bound

$$
\boxed{\;
\|V_k - V^\star\|_\infty \;\le\; \gamma^{\,k}\,\|V_0 - V^\star\|_\infty,
\qquad k=0,1,2,\dots
\;} \tag{2}
$$

---

## 6. Interpretation and remarks

* **Exponential decay.**  The error shrinks by a factor of $\gamma$ every iteration—hence “geometric’’ convergence.
* **Independence from rewards.**  Only $\gamma$ and the initial gap appear in (2); reward magnitudes affect $V^\star$ but not the rate.
* **Norm choice.**  The same proof works for any weighted‑sup norm; the constant becomes $\gamma$ times that weight ratio.
* **Generalizations.**  For policy evaluation (fixed policy $\pi$) the operator
  $(T_\pi v)(s)=\sum_{s'}P_\pi(s,s')[R_\pi(s,s')+\gamma v(s')]$
  is linear but still a $\gamma$-contraction, so (2) holds verbatim.
* **Infinite state spaces.**  Provided $T$ maps a complete normed space into itself and condition (C) holds, the Banach argument still applies (e.g., $S$ countable, $v$ bounded).

---

### Checklist of logical dependencies

1. Bounded rewards ⇒ $T$ well‑defined on $\mathbb R^{|S|}$.
2. $\gamma<1$ ⇒ contraction modulus $<1$.
3. Contraction ⇒ unique fixed point & convergence.
4. Contraction inequality ⇒ geometric error bound.

No step requires anything stronger than $0\le\gamma<1$ and bounded rewards.
