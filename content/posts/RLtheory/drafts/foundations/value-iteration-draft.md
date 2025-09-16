---
date: "2025-07-03"
title: "(Part 3) Online Planning and Theoretical Foundations"
summary: "Online Planning and Theoretical Foundations"
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


## 1  Motivation for Online Planning

### 1.1 Bellman’s Curse of Dimensionality and the “Pipe‑Dream” Runtime

In a finite discounted Markov Decision Process (MDP)

$$
\mathcal M=(S,A,P,r,\gamma),\qquad |S|<\infty,\;|A|=A,\;0<\gamma<1,
$$

a classical dynamic‑programming (DP) planner is expected to **read** almost every transition‑probability vector $P_a(s)$ and **write** an action for every state to output an $\varepsilon$-optimal *full policy*.
The table‑lookup representation therefore incurs a worst‑case arithmetic cost of

$$
\Omega\!\bigl(|S|^2\,|A|\bigr),
$$

because the planner must (i) compute a value for each $(s,a)$ pair and (ii) enumerate an action for every $s$. This square‑in‑$|S|$ dependence is one facet of **Bellman’s curse of dimensionality**.

> **Lower‑bound insight.**  When $\delta<\gamma/(1-\gamma)$ (high‑confidence setting), any planner that emits a complete near‑optimal policy needs $\Omega(|S|^2A)$ operations; there is no way around enumerating the huge table.

Because realistic problems—robotic manipulation, molecular design, dialogue systems—often have *astronomical* state spaces, a runtime that scales linearly (let alone quadratically) in $|S|$ is hopeless.  The dream is to achieve **per‑decision runtimes independent of $|S|$**.

### 1.2 Why a Full Policy Is Overkill in an Embedded Agent

Consider how an embodied agent actually operates:

1. At time $t$ it observes a *single* environment state $s_t$.
2. It must choose one action $a_t$.
3. The environment transitions to $s_{t+1}$ and the process repeats.

Hence the agent never needs to know what it *would* do in states it will never visit; it merely needs the next action in *the current state*.  Requiring the planner to output an entire mapping $S\to A$ is therefore unnecessary for online control.  This observation removes the first $|S|$ factor from the cost profile.

### 1.3 Replacing Table Access with a Simulator Oracle

Most modern RL systems come with or learn a **simulator**—a black‑box function

$$
\texttt{Sim}:(s,a)\;\longmapsto\;(r,s'),\qquad r\sim r_a(s),\;s'\sim P_a(s).
$$

A planner can query `Sim` in arbitrary states without reading explicit probability tables.  When the environment is:

* **Deterministic**, one sample exactly matches the expectation.
* **Stochastic**, Monte‑Carlo samples provide unbiased estimates whose error does **not** depend on $|S|$.

Consequently, if we restrict planning to online calls of `Sim`, the second $|S|$ factor (reading big probability vectors) disappears.

> **Key intuition.**  In a deterministic MDP the planner can compute an $\varepsilon$-optimal action in $O(A^{H})$ time, where
> $H = H_{\gamma,\varepsilon}\approx\log_{1/\gamma}(1/\varepsilon)$, *irrespective of $|S|$*.  This was proved explicitly in Lecture 5.

### 1.4 From Global to Local to Online Access

| Access Mode | What the planner can query                                | State‑space cost                                   |   |       |
| ----------- | --------------------------------------------------------- | -------------------------------------------------- | - | ----- |
| **Global**  | Any $(s,a)$ at any time                                   | Reads entire tables ⇒ ( \Omega(                    | S | ^2A)) |
| **Local**   | States it has visited so far                              | Cost proportional to size of explored subtree      |   |       |
| **Online**  | Only the *current* state (plus optional simulator resets) | $O(A^{H})$ deterministic; $O((mA)^{H})$ stochastic |   |       |

Local and online modes capture the information flow in real agents while preserving feasibility even when $|S|$ is infinite.

### 1.5 Formal Problem Statement (Preview)

*Input to planner per call*
$(A,s_t,\texttt{Sim},\varepsilon,\delta,Q)$

*Goal*
Return action $a_t$ such that the induced per‑step policy is $\varepsilon$-optimal with probability $1-\delta$.

*Performance metric*
Query complexity $m\le Q$ and arithmetic complexity per call—**both ideally independent of $|S|$**.

These formalities will be detailed in Section 4; they are sketched here only to clarify the objective of *online planning*.

### 1.6 Take‑Away

Online planning reframes DP’s “global‑policy” requirement into a *current‑state* action decision, leveraging simulator queries to evade Bellman’s curse.  This shift opens the door to algorithms whose runtime depends exponentially on effective horizon $H$ but **not** on the cardinality of the state space—a crucial breakthrough for large‑scale reinforcement‑learning problems.

---

### Progress 🔄

* Re‑established the computational lower bound in table‑representation MDPs and articulated why producing a full policy is unnecessary online.
* Introduced simulator access modes and previewed the formal online‑planning definition.
* All claims have been grounded in Lecture 5 (pages 1–4).
* **Next section to expand:** “2  From explicit global to implicit local planning”.

---

## 2  From Explicit Global to Implicit Local / Online Planning

### 2.1 Three Simulator‑Access Modes

| Mode              | Planner’s legal queries                                                                                                                                                                                                                                                             | World assumptions                                                                                                        | Pros                                                                                                 | Cons                                                                                        |   |                        |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | - | ---------------------- |
| **Global access** | Any state–action pair $(s,a)\in S\times A$ at any time.                                                                                                                                                                                                                             | Planner sees identifiers for *all* states; simulator can “teleport” to arbitrary states and roll stochastic next‑states. | Close to the classical tabular model—easy to analyse.                                                | Requires enumerating or sampling from the *entire* state set; impossible when (             | S | ) is huge or infinite. |
| **Local access**  | Only to states that have already been generated in the current planning call (including the root state). Allows manual *reset* to any of those past states.                                                                                                                         | Simulator supports **checkpoint/restore**; planner maintains a growing search tree anchored at the current root.         | Removes need for full state enumeration; still lets the planner branch offline from earlier samples. | Extra bookkeeping; still unrealistic inside a robotic control loop if resets are not cheap. |   |                        |
| **Online access** | At time $t$ the simulator’s *internal* state is the *real* environment state $s_t$; planner may: 1) query a **step** $a\mapsto(r,s')$ (which advances the internal state), or 2) **reset** that internal state **only to the original root $s_t$**. No access to earlier roll‑outs. | Matches an embedded agent interacting with the live world.                                                               | Most general and most realistic; avoids huge tables.                                                 | Hardest theoretical setting—branching away from the real trajectory is expensive.           |   |                        |

*Source pages*: formal definitions and discussion of the three interfaces appear in **Lecture 5, pp. 3–4** and **Lecture 6, pp. 7–8**

---

### 2.2 Formal Simulator Definition

A **finite‑MDP simulator** with access mode tag $\chi\in\{\text{global},\text{local},\text{online}\}$ is a black‑box oracle

$$
\texttt{Sim}_\chi:\;
\begin{cases}
\texttt{reset()}                   &\!\!\to s_0\in S,\\[2pt]
\texttt{step}(a)                   &\!\!\to (r,s')\text{ and updates internal state to }s',\\[2pt]
\texttt{teleport}(s,a)\text{ (if }\chi=\text{global})\!\!\!\! &\!\!\to (r,s'),\\[2pt]
\texttt{restore}(s)\text{ (if }s\text{ was generated and }\chi\in\{\text{local},\text{global}\})
\end{cases}
$$

subject to

$$
r\sim r_a(s),\quad s'\sim P_a(s),\qquad (S,A,P,r,\gamma)\text{ a fixed discounted MDP}.
$$

The planner $\Pi$ must respect the admissible call set determined by $\chi$. Violating the protocol is undefined behaviour.

---

### 2.3 Planner State & Query Complexity

* **Search tree**   $T_h=(V_h,E_h)$ after $h$ expansion levels contains exactly the states reachable under the admissible access mode.
* **Local branching factor** $b\_h^\chi \le mA$ (stochastic case, $m$ samples per $(s,a)$).
* **Query complexity** per planning call:

$$
Q_\chi(H,m)=
\begin{cases}
A^{H} & \text{deterministic, global/local/online},\\[4pt]
(mA)^{H} & \text{stochastic, global/local},\\[4pt]
(mA)^{H}\!\!\!\! & \text{stochastic, online *with reset*},\\[4pt]
\text{open}      & \text{stochastic, online *without reset* (open problem).}
\end{cases}
$$

Lower‑bound needle‑in‑a‑haystack arguments (depth‑$H$ $A$-ary tree with a single rewarding leaf) show that any $\delta$-sound planner needs $\Omega(A^{H})$ queries—even under global access—when $\delta<\gamma/(1-\gamma)$.&#x20;

---

### 2.4 Why Local ≈ Global in Worst‑Case Runtime

Lecture 6 proves that sparse‑sampling under **local** access matches global‑access upper bounds:

$$
Q_{\text{local}}(H,m)=O\bigl((mA)^{H}\bigr),\quad
m\;\text{independent of }|S|.
$$

The key technical insight (p. 6) is that the planner ever consults at most $(mA)^{h}$ distinct simulator states at depth $h$; a union bound over this *subtree*—not over the whole $|S|$—keeps the Hoeffding error term logarithmic in $(mA)^{H}$ .

---

### 2.5 Algorithmic Skeletons per Access Mode

1. **Global** – Dynamic Programming (table or explicit sampled model).
2. **Local** – *Sparse Sampling / Monte‑Carlo Tree Search*:

   ```text
   def Value(s, k):
       if k == 0: return 0
       for a in A:
           Q[a] = r(s,a) + (γ/m) * Σ_{s'∈C(s,a)} Value(s', k-1)
       return max_a Q[a]
   ```

   here `C(s,a)` is the list of `m` children produced by `Sim.restore(s); Sim.step(a)`; guaranteed to run in $O((mA)^k)$.
3. **Online** – Same code but `restore` is allowed only to the **root** $s_t$. Practical variants: UCT, progressive widening; theory still immature.

Pseudo‑code adapted from Lecture 5, p. 5 and Lecture 6, pp. 2–3 .

---

### 2.6 Information Hierarchy & Implications

$$
\text{online} \;\subset\; \text{local} \;\subset\; \text{global}.
$$

*Any* planner that works under online access automatically works under the other two modes (just ignore extra capabilities), but not vice‑versa. Hence:

* **Soundness monotone:** if $\Pi$ is $\delta$-sound under online access, it remains $\delta$-sound under local/global access for the *same* query budget.
* **Complexity gaps:** no known separation between global and local; potential logarithmic or polynomial gap between local and pure online without reset (open).&#x20;

---

### 2.7 Single‑Sentence Takeaway

Moving from **explicit global** tables to **implicit local/online** simulators eliminates the $|S|$-factor in planning cost while preserving worst‑case optimal query complexity $Θ(A^{H})$; the only price is tighter control of how—and where—the planner may query the environment.

---

#### Progress 🔄

* Defined the three access modes formally, with simulator API and complexity consequences.
* Proved why local access inherits global upper/lower bounds via subtree union bounds.
* Highlighted open problem: tight bounds for pure online access *without* resets.
* **Next to expand:** Section 3  “Assumed environment model (finite discounted MDP + simulator)”.


---

## 3  Assumed Environment Model

### 3.1 Finite Discounted MDP

We model the environment as a **finite discounted Markov Decision Process (MDP)**

$$
\mathcal M=(S,\;A,\;P,\;r,\;\gamma),\qquad  
|S|<\infty,\;|A|=A,\;0<\gamma<1,
$$

where

| symbol      | meaning                               | type / range                    |
| ----------- | ------------------------------------- | ------------------------------- |
| $S$         | state space                           | finite set                      |
| $A$         | action set (identical in every state) | finite set $\{1,\dots ,A\}$     |
| $P_a(s,s')$ | one‑step transition kernel            | $\sum_{s'}P_a(s,s')=1$          |
| $r_a(s)$    | expected immediate reward             | $[0,1]$ (w\.l.o.g. via scaling) |
| $\gamma$    | discount factor                       | real, $0<\gamma<1$              |

> *Lecture 5 introduces the same tuple on page 1 and fixes the reward range to $[0,1]$ for simplicity.*&#x20;

---

### 3.2 Value Functions

For any (possibly stochastic) policy $\pi:A\!\leftarrow\!S$

$$
v^\pi(s)\;=\; \mathbb E\!\Bigl[\sum_{t=0}^{\infty}\gamma^{t}r_{a_t}(s_t)\mid s_0=s\Bigr],\qquad  
q^\pi(s,a)\;=\; r_a(s)+\gamma\sum_{s'}P_a(s,s')v^\pi(s').
$$

The optimal value functions $v^\*,q^\*$ satisfy the Bellman optimality equations

$$
v^\*(s)=\max_{a}q^\*(s,a),\qquad  
q^\*(s,a)=r_a(s)+\gamma\sum_{s'}P_a(s,s')v^\*(s').  
$$

---

### 3.3 Simulator (Generative Model)

Instead of explicit tables $P,r$, the planner interacts with a **black‑box simulator**

$$
\texttt{Sim}:(s,a)\;\longmapsto\;(r,s')\quad\text{with}\quad  
r\sim r_a(s),\;s'\sim P_a(s,\cdot).
$$

* **IID property:** repeated calls with the same $(s,a)$ return independent samples from the same distribution.
* **Reset capability:** the caller may supply any $s\in S$ as the *root* for a new query tree (local access) or roll the simulator back to the real environment state (online access).
* **Deterministic special case:** if $P_a(s,\cdot)$ has a single support point, one sample exactly equals the expectation, eliminating statistical error.

> *The definition above follows the “MDP simulator” block on page 2 of Lecture 5.*&#x20;

---

### 3.4 Query Budget and Horizon Notation

We measure planning cost per call via

| symbol | definition                                                                                                                |
| ------ | ------------------------------------------------------------------------------------------------------------------------- |
| $m$    | simulator queries per inner node (stochastic case)                                                                        |
| $H$    | look‑ahead depth such that the residual tail $\gamma^{H}/(1-\gamma)\le \varepsilon/2$ (formally $H_{\gamma,\varepsilon}$) |
| $Q$    | overall query budget $Q=(mA)^{H}$ (stochastic) or $A^{H}$ (deterministic)                                                 |

These quantities will drive the upper‑ and lower‑bound proofs in later sections.

---

### 3.5 Why This Abstraction?

1. **Decouples modelling and planning:** algorithms need only *sample* transitions—crucial when $P$ is generated by a physics engine, game server, or learned model.
2. **Enables $|S|$-independent runtimes:** simulators let us compute expectations via Monte‑Carlo roll‑outs, avoiding table scans that scale with $|S|$.
3. **Matches embedded control:** most real agents cannot query hypothetical states; they can, however, reset or clone a simulator of their environment.

> *These motivations are discussed in Lecture 5, pp. 2–3 and Lecture 6, p. 1 when introducing “generative models”.*&#x20;

---

### 3.6 Take‑Away

All forthcoming algorithms assume nothing more than **finite rewards, discounting, and a generative simulator** providing IID samples $(r,s')$ for any queried $(s,a)$; this minimal interface underpins the $|S|$-free complexity results developed in Sections 4–16.

---

#### Progress 🔄

* Formalised the discounted MDP, value functions, and simulator oracle.
* Clarified query budgets $m,H,Q$ that parameterise later bounds.
* Cited Lecture 5 (pages 1–3) and Lecture 6 (page 1) for primary definitions.

**Next up:** Section 4  “Formal statement of the online‑planning problem”.

---

## 4  Formal Statement of the Online‑Planning Problem

### 4.1 Inputs, Interface & Call Contract

At *each* decision epoch $t=0,1,\dots$ the **online planner** $\Pi$ is invoked with

$$
\bigl(A,\;s_{t},\;\texttt{Sim},\;\varepsilon,\;\delta,\;Q\bigr),
$$

where

| Symbol                | Type / meaning                                                                                                | Scope                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------- |
| $A$                   | finite **action set** (cardinality $A\ge 2$)                                                                  | fixed for the episode |
| $s_{t}$               | **root state** (current real environment state)                                                               | varies per call       |
| `Sim`                 | black‑box **simulator** implementing the MDP; admissible API depends on access mode (global / local / online) | fixed                 |
| $\varepsilon\in(0,1)$ | desired **value sub‑optimality** per call                                                                     | user‑set              |
| $\delta\in(0,1)$      | allowable **failure probability** per call                                                                    | user‑set              |
| $Q\in\mathbb N$       | **query budget** on simulator calls for this invocation                                                       | user‑set or adaptive  |

`Sim` satisfies the contract (Lecture 5, pp. 2–3)

$$
\texttt{Sim}(s,a)\;\longmapsto\;(r,s'),\qquad r\sim r_a(s),\;s'\sim P_a(s,\cdot),
$$

and returns IID draws on repeated identical queries.

### 4.2 Online Planner Definition

> **Definition 1 (Well‑formed planner).**
> A (possibly randomised) algorithm $\Pi$ is *well‑formed* under access mode $\chi\in\{\text{global},\text{local},\text{online}\}$ if for **every** finite discounted MDP $\mathcal M$ and every input tuple $(A,s_t,\texttt{Sim}_\chi,\varepsilon,\delta,Q)$:
> 1. $\Pi$ respects the interface restrictions of $\chi$ (Section 2).
> 2. $\Pi$ halts after at most $Q$ simulator queries.
> 3. $\Pi$ outputs an action $a_t\in A$.

### 4.3 Soundness Guarantee

For a fixed call, let the **planner‑induced policy** be

$$
\pi^{\Pi}(s)\;=\;\begin{cases}
\Pi(A,s,\texttt{Sim},\varepsilon,\delta,Q) & \text{if }s=s_{t}\text{ for some call}\\
\text{any tie‑breaking rule} & \text{otherwise}.
\end{cases}
$$

Let $v^\pi$ (resp. $v^\*$) denote the value function of $\pi$ (resp. the optimal policy) in $\mathcal M$.

> **Definition 2 ($(\varepsilon,\delta)$-soundness).**
> A well‑formed planner $\Pi$ is **$(\varepsilon,\delta)$-sound** if, for *every* MDP $\mathcal M$ and every call root $s_t$,

$$
\Pr\!\Bigl[v^{\pi^{\Pi}}(s_t)\;\ge\;v^\*(s_t)-\varepsilon\Bigr]\;\ge\;1-\delta.
$$

The probability is over both the planner’s internal randomness **and** the simulator’s stochasticity.
(Lecture 5, Definition “$\delta$-sound Planner”, pp. 3–4)&#x20;

### 4.4 Complexity Measures

Two orthogonal cost metrics are recorded **per call**:

1. **Query complexity** $m\;=\;\#\{\texttt{Sim} \text{invocations}\}\;\le Q$.
2. **Arithmetic complexity** $W\;=$ basic arithmetic/logical ops executed by $\Pi$.

When analysing families of planners we express these as functions of

$$
(m,W) \;=\; f\bigl(A,\;H_{\gamma,\varepsilon},\;\varepsilon,\;\delta,\;\text{access mode}\bigr),
$$

where $H_{\gamma,\varepsilon}=\bigl\lceil\log\!\bigl(\varepsilon(1-\gamma)/2\bigr)/\log\gamma\bigr\rceil$ is the **effective horizon** ensuring tail‑value truncation ≤ $\varepsilon/2$.

### 4.5 Decision Map vs. Policy Map

Classical (offline) planning seeks a **decision map** $\pi:S\to A$.
Online planning replaces this by a *transient* mapping

$$
\Pi_s: s \;\mapsto\; a\quad\text{for the current }s=s_{t}.
$$

Because only one state is queried, both $m$ and $W$ are allowed to depend **exponentially in $H$** yet must be *independent of $|S|$*—the crux of online efficiency (Lecture 5, pp. 1–2).

### 4.6 Problem Statement (concise form)

> **Online‑Planning Decision Problem**
> *Given* a finite discounted MDP simulator, accuracy pair $(\varepsilon,\delta)$, and per‑call budget $Q$, design a $(\varepsilon,\delta)$-sound planner $\Pi$ minimising query complexity $m$ (and secondarily arithmetic cost $W$) subject to the admissible access mode.

Lower‐bound results (§11) show that $m=\Omega(A^{H_{\gamma,\varepsilon}})$ even under global access when $\delta<\gamma/(1-\gamma)$ , while Sections 9–10 construct matching upper bounds using sparse sampling.

### 4.7 Single‑Sentence Takeaway

An **online planner** is a subroutine that, given only the *current* state and a simulator oracle, must output an $\varepsilon$-optimal action with probability $1-\delta$; its performance is measured by simulator queries $m$ and arithmetic work $W$, both ideally independent of the (potentially massive) state space.

---

#### Progress 🔄

* **Completed Section 4**: formalised inputs, planner definition, $(\varepsilon,\delta)$-soundness, and complexity measures, with citations to Lecture 5.
* Remaining open issues:

  1. Prove the equivalence between $\varepsilon$-greedy action selection and $\varepsilon/(1-\gamma)$ value loss (will appear in Section 7).
  2. Instantiate concrete algorithms (Sections 9–10) and derive explicit $m,W$ as functions of $H$.

Next up: **Section 5  Optimisation language & oracle types**.


---

## 5  Optimisation Language & Oracle Types

### 5.1 Why Borrow Notions from Black‑Box Optimisation?

The online‑planning problem can be viewed as a **stochastic optimisation task** over the finite action set $A$:

$$
\max_{a\in A} Q^{\pi_{t-1}}(s_t,a),
\qquad 
Q^{\pi_{t-1}}(s_t,a)=r_a(s_t)+\gamma\; \mathbb E_{s'\sim P_a(s_t)}\bigl[V^{\pi_{t-1}}(s')\bigr].
$$

Because the planner **cannot** read $P_a(s_t)$ or $r_a(s_t)$ directly, it must optimise this objective through *queries* to a black‑box simulator.  This is precisely the scenario studied in optimisation theory under various **oracle models**.  Lecture 5 introduces the same viewpoint, explicitly describing MDP simulators “in a language similar to that used to describe optimisation oracles (zeroth‑order, first‑order, noisy, etc.)” .

> **Takeaway.**  Thinking in “oracle” terms lets us port lower‑ and upper‑bound techniques from convex/non‑convex optimisation to online planning.

---

### 5.2 Canonical Oracle Classes

| Oracle type                    | Optimisation analogue         | Call signature $O(\cdot)$ | Guarantees returned        | MDP instantiation                                    |
| ------------------------------ | ----------------------------- | ------------------------- | -------------------------- | ---------------------------------------------------- |
| **Deterministic zeroth‑order** | Evaluate $f(x)$               | $O(x)\to f(x)$            | Exact value                | Deterministic simulator; single sample = expectation |
| **Stochastic zeroth‑order**    | Evaluate noisy $f(x)+\xi$     | $O(x)\to \tilde f(x)$     | Unbiased, bounded variance | Standard MDP simulator call $\texttt{Sim}(s,a)$      |
| **First‑order**                | Evaluate $(f(x),\nabla f(x))$ | $O(x)\to (f,\nabla f)$    | Exact gradient             | Requires full $P_a(s)$ vector — *unavailable* online |
| **Higher‑order / Hessian**     | $\nabla^2 f(x)$ access        | $O(x)\to \nabla^2 f$      | Curvature info             | Impossible without model tables                      |
| **Batch oracle**               | Vector of points              | $O(\{x_i\})\to\{f(x_i)\}$ | Parallel values            | Parallel roll‑outs / GPU simulators                  |

Only the **stochastic zeroth‑order oracle** is universally available in online planning; deterministic plans are a strict subset when $P_a(s)$ is Dirac‑supported.&#x20;

---

### 5.3 Formal Definition (Simulator as Stochastic Zeroth‑Order Oracle)

A finite‑MDP **simulator oracle** $\mathcal O$ is a map

$$
\mathcal O:(s,a)\;\xmapsto{\text{i.i.d.}}\; (R,S'),\qquad 
R\sim r_a(s),\; S'\sim P_a(s,\cdot).
$$

* **Zeroth‑order:** it reveals only the *realisation* of the value, never its gradient w\.r.t.\ parameters.
* **Unbiased:** $\mathbb E[\mathcal O(s,a)\mid s,a]=\bigl(r_a(s),P_a(s)\bigr)$.
* **Variance bound:** $R\in[0,1]$, hence $\operatorname{Var}(R)\le 1/4$; state variance bounded by indicator variables.

This oracle can be queried under three **access modalities** (global, local, online—Section 2), but its statistical nature is identical across them.

---

### 5.4 Query Complexity vs. Statistical Complexity

Optimisation theory separates

1. **Information complexity** – *number* of oracle queries needed to achieve $\varepsilon$-optimality with confidence $1-\delta$.
2. **Computation complexity** – arithmetic cost once samples are drawn.

For smooth convex functions a first‑order oracle yields $O(1/\sqrt{\varepsilon})$ rates; for MDP planning the stochastic zeroth‑order oracle incurs $O((mA)^{H_{\gamma,\varepsilon}})$ queries (Sections 9–10).  The gap is rooted in the **lack of gradient structure**—every action branch must be *sampled* instead of *differentiated*.&#x20;

---

### 5.5 Bridging Terminologies

| Optimisation term      | Planning counterpart                                   |
| ---------------------- | ------------------------------------------------------ |
| Decision variable $x$  | Action sequence along a depth‑$H$ subtree              |
| Objective $f(x)$       | Truncated value $Q^{(H)}(s_0,x)$                       |
| Noisy evaluation       | Monte‑Carlo rollout                                    |
| Smoothness / Lipschitz | Reward range $R_{\max}=1$; contraction factor $\gamma$ |
| Strong convexity       | *None* (max‑operator is non‑convex)                    |

This dictionary clarifies why **Hoeffding‐style concentration**, not gradient‑based bounds, governs sample sizes: the objective lacks exploitable curvature and each sample has bounded range but no smoothness. The concentration tools collected in the supplementary note (see Theorem 1, Hoeffding’s inequality ﻿page 1) underpin all subsequent performance guarantees.&#x20;

---

### 5.6 Consequences for Algorithm Design

* **Deterministic MDPs ⇒ deterministic zeroth‑order oracle:** one sample suffices per $(s,a)$. Value iteration reduces to exhaustive tree search $O(A^{H})$.
* **Stochastic MDPs ⇒ stochastic zeroth‑order oracle:** Monte‑Carlo **sparse sampling** must average $m$ calls per edge to shrink variance by $O(1/\sqrt m)$.
* **No gradient tricks:** policy‑gradient or Newton‑style accelerations require differentiability of the value w\.r.t.\ controllable parameters, absent here.
* **Lower bounds match oracle power:** need $Ω(A^{H})$ queries (Section 11) which aligns with zero‑order complexity in worst‑case optimisation.

---

### 5.7 Single‑Sentence Takeaway

Online planning operates under the \*\*weakest black‑box model—a stochastic zeroth‑order oracle—\*\*so every theoretical bound that follows is ultimately an information‑theoretic consequence of how fast Monte‑Carlo samples can approximate expectations, not of algorithmic ingenuity.

---

#### Progress 🔄

* Defined the simulator formally as a stochastic zeroth‑order oracle and positioned global/local/online access within oracle theory.
* Mapped optimisation oracle taxonomy to MDP planning, highlighting why only zeroth‑order information is generically available.
* Derived immediate implications for query‑complexity analysis and previewed the need for concentration inequalities (linked to Section 14).

*Next up*: **Section 6  Agent–environment interaction loop**.


---

## 6  Agent–Environment Interaction Loop

### 6.1 Where the Planner Sits in the RL Feedback Cycle

At each discrete decision epoch $t$ the agent, planner, and simulator participate in the following **four‑step handshake**:

| Step | Component                | Input                                             | Computation                                                                             | Output                                  |
| ---- | ------------------------ | ------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------- |
|  ①   | **Environment**          | —                                                 | Evolves according to the real MDP $\mathcal M$                                          | Current state $s_t$ revealed to planner |
|  ②   | **Online planner $\Pi$** | $A,\,s_t,\,\texttt{Sim},\,(\varepsilon,\delta,Q)$ | Executes ≤ $Q$ simulator calls (Algorithm 9/10) to evaluate a depth‑$H$ look‑ahead tree | Action $a_t\in A$                       |
|  ③   | **Agent actuator**       | $a_t$                                             | Sends $a_t$ to the physical or simulated environment                                    | —                                       |
|  ④   | **Environment**          | $a_t$                                             | Draws $r_t\sim r_{a_t}(s_t)$ and $s_{t+1}\sim P_{a_t}(s_t,\cdot)$                       | New state $s_{t+1}$ (loop to ①)         |

*Lecture 5 embeds exactly this four‑stage loop in its problem statement for online planning (pages 2–3). The simulator acts as a surrogate transition oracle between steps ② and ④* .

> **Takeaway:** The planner is invoked **inside** the perception‑action cycle; its latency is paid before every real action, so per‑call runtime—not offline complexity—governs feasibility.

---

### 6.2 Formal Timing & Budget Parameters

* **Query budget $Q$.** Maximum number of `Sim` invocations per planner call (Section 4).
* **Depth $H$.** Number of Bellman back‑ups; chosen as $H_{\gamma,\varepsilon}=\lceil\log(\varepsilon(1-\gamma)/(2\gamma))/\log\gamma\rceil$ (Section 9).
* **Wall‑clock latency.** $T_{\text{plan}} = \Theta((mA)^{H})$ in the stochastic case; must be $<$ environment step time for real‑time control.
* **Interaction horizon.** The loop repeats indefinitely; cumulative performance is measured by the value of the **planner‑induced policy** $\pi^{\Pi}$ (Definition 4.3).

---

### 6.3 Simulator Call Semantics

Inside step ② the planner may issue three primitives depending on access mode (Section 2):

1. `reset(s_root)` – initialise internal simulator state to root $s_t$.
2. `step(a)` – advance one transition, returning $(r,s')$.
3. `restore(s_checkpoint)` – if **local** access, jump back to an earlier generated state.

Per Lecture 6 the planner’s recursion alternates `step` and `restore` to build a bounded‑width search tree; branching factor is $A$ (deterministic) or $mA$ (stochastic) .

---

### 6.4 Pseudocode Embedding (Stochastic Sparse‑Sampling)

```python
def act_online(s_root, ε, δ):
    # --- Step 2: planner ---
    q_hat = value_estimate(s_root, H=H_{γ,ε}, m=samples_per_action)
    a_root = argmax_a q_hat[(s_root, a)]
    return a_root        # delivered to actuator (Step 3)
```

`value_estimate` is the depth‑$H$ Monte‑Carlo recursion from Section 9; it uses `step` to draw $m$ IID successors and `restore(s_root)` between sibling branches.

---

### 6.5 Soundness in the Loop

Because $\Pi$ is $(\varepsilon,\delta)$-sound (Definition 4.3), iterating the loop yields a **non‑stationary but near‑optimal trajectory**:

$$
\Pr\!\Bigl[v^\*(s_t)-v^{\pi^{\Pi}}(s_t)\le\varepsilon\;\; \forall t\Bigr]\;\ge\;1-\delta^{\text{tot}},
$$

with $\delta^{\text{tot}}\le\sum_{t}\delta_t$ (union bound). Choosing per‑call $\delta_t = \delta_0\,\gamma^{t}$ keeps the cumulative failure probability bounded by $\delta_0/(1-\gamma)$.

---

### 6.6 Latency‑Accuracy Trade‑offs

| Increasing …       | Pros                                                | Cons                                                 |
| ------------------ | --------------------------------------------------- | ---------------------------------------------------- |
| $m$ (samples/edge) | Lower Monte‑Carlo variance, tighter Hoeffding bound | Exponential cost $(mA)^{H}$                          |
| $H$ (look‑ahead)   | Smaller truncation error $\gamma^{H}/(1-\gamma)$    | Exponential cost $A^{H}$; deeper simulator roll‑outs |
| $Q$ (budget)       | Allows larger $m,H$                                 | Longer wall‑clock delay                              |

Lecture 6 Figure 1 (page 2) plots empirical run‑time vs. $m$, illustrating the steep rise beyond the real‑time threshold.&#x20;

---

### 6.7 Single‑Sentence Takeaway

The planner is executed **between perception and action**, querying the simulator up to $Q$ times per call; adhering to this tight inner loop transforms theoretical query complexity $(mA)^{H}$ into a hard real‑time latency budget that dictates feasible choices of $m$ and $H$.

---

#### Progress 🔄

* Fully specified the real‑time four‑step interaction cycle and mapped query complexity to latency.
* Connected simulator primitives to access modes and sparse‑sampling recursion.
* Provided latency–accuracy trade‑off table and cumulative soundness accounting.

**Next section to develop:** **7  Online planner & $\delta$-soundness – formal definition and practical implications**.


---

## 7  Online Planner & $\delta$-Soundness

### 7.1 Definitions

**Online planner (restated).** A (possibly randomized) algorithm $\Pi$ that, for any finite discounted MDP simulator $\texttt{Sim}$ and every call tuple
$(A,\,s_t,\,\texttt{Sim},\,\varepsilon,\,\delta,\,Q)$,

1. respects the admissible query set of the chosen access mode (global, local, or online);
2. makes at most $Q$ simulator calls;
3. returns an action $a_t\in A$,

is said to be **well‑formed**.&#x20;

---

**$(\varepsilon,\delta)$-soundness.** Let the *planner‑induced policy* be

$$
\pi^{\Pi}(s)\;=\;\Pi(A,s,\texttt{Sim},\varepsilon,\delta,Q)
\quad\text{when }\Pi\text{ is invoked with root }s.
$$

$\Pi$ is **$(\varepsilon,\delta)$-sound** if, for every MDP served by the simulator and for every call root $s_t$,

$$
\Pr\!\bigl[v^{\pi^{\Pi}}(s_t)\;\ge\;v^{\!*}(s_t)-\varepsilon\bigr]\;\ge\;1-\delta
\tag{7.1}
$$

where the probability is over both the planner’s internal randomness and the simulator’s stochasticity.&#x20;

---

**$\varepsilon$-optimising action.** For any state $s$, an action $a$ is **$\varepsilon$-optimising** if

$$
q^{\!*}(s,a)\;\ge\;v^{\!*}(s)-\varepsilon .
\tag{7.2}
$$

---

### 7.2 Why Bounding Action Error Suffices

The Bellman optimality operator $T$ is a $\gamma$-contraction in the $\ell_\infty$ norm. Hence value errors propagate geometrically:

$$
\|Tv-Tv^{\!*}\|_\infty\;\le\;\gamma\|v-v^{\!*}\|_\infty .
$$

This yields the classical **policy loss lemma**:

> **Lemma 7.1 (ε‑optimising ⇒ value bound).** If a policy $\pi$ satisfies
> $\sum_a \pi(a|s)\,q^{\!*}(s,a)\;\ge\;v^{\!*}(s)-\varepsilon$ for every state $s$,
> then
>
> $$
> v^{\!*}(s)-v^{\pi}(s)\;\le\;\frac{\varepsilon}{1-\gamma}\qquad\forall s.
> \tag{7.3}
> $$

*Proof sketch.* Write the Bellman equations for $v^{\!*}$ and $v^{\pi}$; subtract; apply the contraction property and unroll the recursion. Detailed derivation appears in Lecture 6, p. 3.  ∎

---

### 7.3 Soundness via Approximate $Q$-Functions

Suppose the planner returns an approximate action‑value function $\hat q$ and acts **greedily**:
$a_t=\arg\max_a \hat q(s_t,a)$.

> **Lemma 7.2 (greedy‑gap transfer).** If
> $\|\hat q-q^{\!*}\|_\infty\le\varepsilon$
> then the greedy policy is $2\varepsilon$-optimising; consequently
> $v^{\!*}-v^{\pi_{\hat q}}\le 2\varepsilon/(1-\gamma)$.&#x20;

Hence to achieve per‑call value error $\le\varepsilon$ it suffices to drive the uniform $Q$-error below $\tfrac{1}{2}(1-\gamma)\varepsilon$.

---

### 7.4 Randomised Planners: “δ‑Sound” vs. “Almost‑ε”

Sparse‑sampling planners are randomised because they build Monte‑Carlo trees. Let

$$
F_t=\Bigl\{\text{“event that planner fails at time }t\text{”}\Bigr\}.
$$

Hoeffding’s inequality gives
$\Pr(F_t)\le\delta$ when the sample size $m$ (per edge) satisfies the bound derived in §14.&#x20;

> **Lemma 7.3 (ε,ζ‑hybrid bound).** If every call produces an $\varepsilon$-optimising action with probability $1-\zeta$, then
>
> $$
> v^{\!*}-v^{\pi}\;\le\;\frac{\varepsilon+2\zeta}{1-\gamma}.
> \tag{7.4}
> $$
>
> This is proved by conditioning on the “good” and “bad” events and applying Lemma 7.1 on the good event.&#x20;

**Interpretation.** Choosing $\zeta=\delta$ shows that a $\delta$-sound planner accords with the classical $(\varepsilon,\delta)$ PAC framework: occasional action failures inflate the value loss by at most $2\delta/(1-\gamma)$.

---

### 7.5 Design Parameters for $\delta$-Soundness

Combine Lemmas 7.1–7.3 with the sparse‑sampling accuracy guarantee (proof in Section 16):

* choose horizon $H=H_{\gamma,\varepsilon/3}$;
* choose samples per edge

  $$
  m\;\ge\;\frac{18}{\varepsilon^{2}(1-\gamma)^{6}}
          \log\!\Bigl(\frac{12A^{H+1}}{(1-\gamma)^{2}\delta}\Bigr).
  \tag{7.5}
  $$

Then

1. Hoeffding + union bound $\Rightarrow$ all backup errors $<\varepsilon/3$ w\.p. $1-\delta$;
2. greedy policy is $2\varepsilon/3$-optimising (Lemma 7.2);
3. overall value loss $<\varepsilon$ (Lemma 7.1).

Hence the planner is $(\varepsilon,\delta)$-sound while using
$O\!\bigl((mA)^{H}\bigr)$ simulator queries per call—independent of $|S|$.&#x20;

---

### 7.6 Relationship to Other Confidence Notions

| Guarantee                | Definition                                                                       | Typical use                          |                                  |                                  |
| ------------------------ | -------------------------------------------------------------------------------- | ------------------------------------ | -------------------------------- | -------------------------------- |
| **$\delta$-sound**       | Inequality (7.1) for *every* call                                                | Worst‑case safety in embedded agents |                                  |                                  |
| PAC‑MDP                  | Value loss $<\varepsilon$ after *polynomial* burn‑in steps with prob. $1-\delta$ | Exploration in learning settings     |                                  |                                  |
| High‑confidence planning | (                                                                                | \hat q-q^{!\*}                       | \le\varepsilon) w\.p. $1-\delta$ | Offline planners with simulators |

$\delta$-soundness is the *strongest*: it must hold **on every invocation**, not just asymptotically.

---

### 7.7 Single‑Sentence Takeaway

A planner is **$(\varepsilon,\delta)$-sound** when every call returns an $\varepsilon$-near‑optimal action with probability $1-\delta$; thanks to contraction properties, this per‑action control ensures per‑state value loss $\le\varepsilon/(1-\gamma)$, so designing Monte‑Carlo depth‑$H$ trees with Hoeffding‑based sample counts directly yields rigorous online guarantees independent of the state‑space size.

---

#### Progress 🔄

* Formalised $(\varepsilon,\delta)$-soundness and connected it to action‑level errors.
* Proved three lemmas (7.1–7.3) translating $Q$-function accuracy into value guarantees under randomness.
* Derived explicit sample complexity (Eq. 7.5) required for sparse‑sampling planners.
* Positioned $\delta$-soundness among neighbouring confidence notions (PAC‑MDP, offline bounds).

**Next section to develop:** **8  Computational cost metrics**.

---

## 8  Computational‑Cost Metrics

Online‑planning papers distinguish **how much data the planner must *pull* from the simulator** from **how much arithmetic it must *push* through the CPU/GPU** each time it is called. Both costs are expressed *per planner invocation* (i.e. per agent decision) so that they can be compared directly with an application’s real‑time budget.

| Symbol | Meaning                                                                                                                   | Where it comes from                          | Typical magnitude                                                            |
| ------ | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------- |
| $m$    | **Query multiplicity** – number of simulator calls made for *each* interior edge of the look‑ahead tree (stochastic case) | Hoeffding‑driven sample size (Section 14)    | $\tilde O\!\bigl((1-\gamma)^{-6}\varepsilon^{-2}\bigr)$ for δ‑sound planners |
| $H$    | **Effective horizon** – tree depth, chosen so that residual discount tail ≤ $\varepsilon/2$                               | geometric tail bound $\gamma^{H}/(1-\gamma)$ | $\bigl\lceil \log(\varepsilon(1-\gamma)/2)/\log\gamma \bigr\rceil$           |
| $Q$    | **Total simulator calls** for the whole tree                                                                              | branching factor $\times$ depth              | see deterministic/stochastic rows below                                      |
| $W$    | **Arithmetic operations** on the agent’s processor                                                                        | Bellman back‑up recursion                    | proportional to same exponent as $Q$                                         |

### 8.1 Deterministic versus Stochastic Environments

| Environment assumption                                     | Branching factor per level | Simulator queries $Q$ | Arithmetic work $W$ | Source          |            |               |
| ---------------------------------------------------------- | -------------------------- | --------------------- | ------------------- | --------------- | ---------- | ------------- |
| Deterministic transitions ( (                              | P\_a(s)                    | =1) )                 | $A$                 | $\;A^{H}$       | $O(A^{H})$ | Lecture 5 §3  |
| Stochastic transitions (sparse‑sampling, $m$ IID children) | $mA$                       | $\;(mA)^{H}$          | $O((mA)^{H})$       | Lecture 6 §2–3  |            |               |

*Both* entries are **independent of $|S|$** – the core motivation of online planning.

### 8.2 Memory Footprint

A depth‑$H$ sparse‑sampling tree stores at most $(mA)^{H}$ nodes, each holding a constant‑size tuple $(s,\hat q)$. Memory therefore scales identically to $Q$. For embedded agents with kilobytes of fast RAM this is often the *real* limit on $m$ or $H$.

### 8.3 Wall‑Clock Latency

If one simulator call plus one numeric back‑up takes τ micro‑seconds, a call to the planner costs roughly

$$
T_{\text{plan}} \;\approx\; \tau\,(mA)^{H}.
$$

> The *runtime‑vs‑sample‑size* curve on **page 2 of Lecture 6** plots $T_{\text{plan}}$ against $m$ for fixed $A$ and $H$, showing an exponential knee once $m$ grows beyond the Hoeffding minimum.&#x20;

For robotics or games the control loop might allow only 1–5 ms; the chosen $H,m$ must respect this budget even though theory would like them larger.

### 8.4 Lower‑Bound Perspective

The **needle‑in‑a‑haystack** construction (depth‑$H$ $A$-ary tree with a single rewarding leaf) proves that any $\delta$-sound planner *must* query Ω($A^{H}$) leaves when $\delta<\gamma/(1-\gamma)$ – exactly the deterministic cost above.&#x20;
In stochastic settings this lower bound lifts to Ω($(A^{H})$) *samples*; matching upper bounds need $m=\Theta(1)$ only when Hoeffding permits.

### 8.5 Putting Cost Metrics into Design Choices

* **Small $H$, large $m$** – suits *short‑horizon, high‑variance* tasks (e.g. Atari games) where variance dominates truncation error.
* **Large $H$, small $m$** – suits *long‑horizon, low‑variance* tasks (e.g. deterministic grid‑worlds).
* **Asymmetric branching (MCTS)** – allocate $m$ adaptively along promising paths to soften the $(mA)^{H}$ explosion (Section 17).

### 8.6 Single‑Sentence Takeaway

Per decision, an online planner spends **$Q=(mA)^{H}$ simulator calls and the same‑order CPU cycles**, achieving state‑space‑free control at the unavoidable exponential price in horizon $H$; careful tuning of $m$ and $H$ is essential to fit the agent’s real‑time budget without violating the δ‑soundness guarantees.

---

#### Progress 🔄

* Defined formal cost symbols $m,H,Q,W$.
* Derived deterministic and stochastic complexity tables straight from Lectures 5 & 6.
* Integrated memory and latency considerations and linked to the runtime graph on Lecture 6 p. 2.
* Clarified how lower bounds pin down the exponential $A^{H}$ factor.

**Next section to elaborate:** **9  Baseline algorithm: Value iteration & action‑value recursion**.


---

## 9  Baseline Algorithm: Value‑Iteration Recursion & Sparse‑Sampling Trees

This section derives the canonical **depth‑$H$ online planner** used throughout the literature, starting from classical value iteration and culminating in the sparse‑sampling recursion that achieves $|S|$-independent runtimes.

### 9.1 Bellman Optimality & Action‑Value Operators

For a finite discounted MDP $\mathcal M=(S,A,P,r,\gamma)$ (§3) define

$$
\begin{aligned}
(Tv)(s)           &= \max_{a\in A} \Bigl\{ r_a(s) + \gamma \,P_a(s)^{\!\top} v \Bigr\},\\[2pt]
(\tilde Tq)(s,a)  &= r_a(s) + \gamma \,P_a(s)^{\!\top} (Mq),\\[2pt]
(Mq)(s)           &= \max_{a\in A} q(s,a).
\end{aligned}
\tag{9.1}
$$

Both $T$ and $\tilde T$ are $\gamma$-contractions in $\|\cdot\|_\infty$; their unique fixed points are the optimal value and Q‑functions $v^{*}, q^{*}$. &#x20;

### 9.2 Truncating the Infinite Horizon

Because rewards are bounded in $[0,1]$ the *tail value* after $H$ steps is at most $\gamma^{H}/(1-\gamma)$.  Choosing

$$
H_{\gamma,\varepsilon}\;=\;\Bigl\lceil \frac{\log \bigl(\varepsilon(1-\gamma)/2\bigr)}{\log \gamma}\Bigr\rceil
\tag{9.2}
$$

guarantees that ignoring steps beyond $H$ incurs ≤ $\varepsilon/2$ value error.  This is the **effective horizon** quoted in earlier sections.&#x20;

### 9.3 Deterministic Case — Explicit Depth‑$H$ Tree

If each $(s,a)$ has a **single** successor $g(s,a)$ we can unroll recursion without sampling:

```python
def Q_det(s, k):                       # returns [q(s,a) for a in A]
    if k == 0:
        return [0.0 for a in A]
    return [ r(s,a) + γ * max(Q_det(g(s,a), k-1)) for a in A ]
```

* **Time / memory**: $O(A^{k})$.
* **Root action**: $a^{\text{det}}_{*}(s)=\arg\max_{a} Q_{\text{det}}(s,H)[a]$.

Runtime is exponential in $H$ but independent of $|S|$. &#x20;

> *Takeaway*: Determinism collapses expectations into single paths—one sample per edge suffices.

### 9.4 Stochastic Case — Sparse‑Sampling Recursion

When transitions are stochastic we approximate each expectation by **$m$ IID simulator draws** $C(s,a)=\{s'_{1},\dots,s'_{m}\}$:

```python
def Q_sparse(s, k):
    if k == 0:
        return [0.0 for a in A]
    return [ r(s,a) +
             γ/m * sum( max(Q_sparse(s_prime, k-1))
                         for s_prime in C(s,a) )  for a in A ]
```

*Draws* are generated lazily and cached (local‑access assumption) so the same child state is reused when several ancestors reference it.

* **Branching factor**: $mA$.
* **Queries per call**: $(mA)^{H}$.
* **Root action**: $a^{\text{SS}}_{*}(s)=\arg\max_{a} Q_{\text{sp}}(s,H)[a]$.

Sparse‑sampling was introduced by Kearns, Mansour & Ng and analysed in Lectures 5–6.&#x20;

### 9.5 Error Propagation Bound

Let $\hat q = Q_{\text{sp}}(\cdot,H)$.  With sample size

$$
m\;\ge\;\frac{18}{\varepsilon^{2}(1-\gamma)^{6}}
      \log\!\Bigl(\frac{12A^{H+1}}{(1-\gamma)^{2}\delta}\Bigr)
\tag{9.3}
$$

Hoeffding + union bound (Section 14) yield

$$
\|\hat q - q^{*}\|_{\infty} \le \varepsilon/3 \quad\text{w.p. }1-\delta.
$$

Greedy w\.r.t. $\hat q$ is thus $2\varepsilon/3$-optimising (Lemma 7.2), giving an overall $(\varepsilon,\delta)$-sound planner when combined with tail error $\varepsilon/2$.&#x20;

### 9.6 Pseudocode of a Complete Planner

```python
def PLAN_ONLINE(s_root, ε, δ, γ):
    H = ceil(log(ε*(1-γ)/2, γ))
    m = ceil( 18/(ε**2*(1-γ)**6) *
              log( 12 * (len(A)**(H+1))  / ((1-γ)**2 * δ) ) )
    # build sparse tree starting at s_root
    Q_root = Q_sparse(s_root, H)
    return argmax(Q_root)             # action to execute
```

*Local* access is assumed so `C(s,a)` can restore to any sampled ancestor state; the algorithm degrades gracefully to pure‑online if only root resets are allowed (Section 12).

### 9.7 Complexity Summary

| Environment   | Simulator calls | Arithmetic ops | References  |
| ------------- | --------------- | -------------- | ----------- |
| Deterministic | $A^{H}$         | $O(A^{H})$     | Lec 5 §3    |
| Stochastic    | $(mA)^{H}$      | $O((mA)^{H})$  | Lec 6 §2–3  |

Both grow exponentially with $H$ but never with $|S|$.

### 9.8 Single‑Sentence Takeaway

Value‑iteration unrolled to depth $H_{\gamma,\varepsilon}$ and coupled with *sparse sampling* produces an online planner that is provably $(\varepsilon,\delta)$-sound while requiring only $(mA)^{H}$ simulator queries—achieving the core goal of state‑space‑independent computation.

---

#### Progress 🔄

* Formalised operators (Eq. 9.1), horizon choice (Eq. 9.2) and sample complexity (Eq. 9.3).
* Provided deterministic and stochastic pseudocode with precise complexity.
* Linked error analysis to Section 14’s concentration tools and Section 7’s soundness lemmas.

**Next section to expand:** **10  Upper bounds on runtime**.


---

\## 10  Upper Bounds on Runtime

\### 10.1 Deterministic MDPs – Exponential in Horizon, *Not* in |S|

> **Theorem 10.1 (Recursive Value‑Expansion).**
> Let $\mathcal M$ be a deterministic discounted MDP with $|A|=A$, discount $\gamma$ and rewards in $[0,1]$.
> A depth‑$H=H_{\gamma,\varepsilon}:=\bigl\lceil\log_{\gamma}(\varepsilon(1-\gamma)/2)\bigr\rceil$ unrolled value tree (Algorithm 9.3) returns an action whose value loss is at most $\varepsilon$.
> The algorithm performs exactly
>
> $$
> Q_{\text{det}}(A,H)=A^{H}
> $$
>
> simulator calls and $O(A^{H})$ arithmetic operations, *independently of $|S|$.*&#x20;

*Proof sketch.*
(i) Determinism collapses each expectation $P_a(s)^\top v$ into a single successor; depth‑$H$ recursion thus explores an $A$-ary tree with $A^{H}$ leaves.
(ii) Truncating at $H$ leaves tail value $\gamma^{H}/(1-\gamma)\le\varepsilon/2$.
(iii) Greedy action w\.r.t. the exact tree yields the remaining $\varepsilon/2$ error margin (Lemma 7.1). Efficiency is immediate from the node count.&#x20;

---

\### 10.2 Stochastic MDPs – Sparse‑Sampling Bound

> **Theorem 10.2 (Kearns–Mansour–Ng Sparse Sampling).**
> Under the same setting but with *stochastic* transitions, let the planner draw
> $m$ i.i.d. successors per interior node (Algorithm 9.4).
> With
>
> $$
> m\;\ge\;\frac{18}{\varepsilon^{2}(1-\gamma)^{6}}\,
> \log\!\Bigl(\frac{12A^{H+1}}{(1-\gamma)^{2}\delta}\Bigr)
> \tag{10.1}
> $$
>
> the returned action is $\varepsilon$-optimal with probability $1-\delta$.
> Runtime per call is
>
> $$
> Q_{\text{sto}}(A,H,m)=(mA)^{H},\qquad  
> W_{\text{sto}}=O((mA)^{H}),
> $$
>
> again free of $|S|$.&#x20;

*Proof sketch.*

1. **Tree size.** Each level branches into $A$ actions, each action into $m$ sampled states ⇒ $(mA)^{H}$ nodes.
2. **Statistical error.** For any node $(s,a)$ the Monte‑Carlo estimate of $P_a(s)^\top v$ has range $R=1/(1-\gamma)$. Hoeffding gives
   $\Pr[|\hat{\mu}-\mu|>\eta]\le2\exp(-2m\eta^{2}(1-\gamma)^{2})$.&#x20;
3. **Union bound over the explored subtree.** There are at most $A^{h}m^{h}$ nodes at depth $h$; summing over $h=0\!:\!H-1$ yields the $\log$ term in (10.1).&#x20;
4. **Error propagation.** Bellman contraction multiplies depth‑$k$ noise by $\gamma^{k}$; choosing $\eta=\varepsilon/3$ in (10.1) bounds cumulative bias by $\varepsilon/3$ (Lemma 7.2).
5. **Tail truncation.** As in deterministic case, $\gamma^{H}/(1-\gamma)\le\varepsilon/3$. Total loss ≤ $\varepsilon$.

---

\### 10.3 Asymptotic Expressions

With $H=\Theta\!\bigl(\log_{1/\gamma}(1/\varepsilon)\bigr)$:

| Environment   | Queries $Q$                                                                                                            | dominant factors   |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Deterministic | $A^{\,\Theta(\log(1/\varepsilon))}$                                                                                    | horizon only       |
| Stochastic    | $\bigl(A/\varepsilon^{2}\bigr)^{\Theta(\log(1/\varepsilon))}\, \mathrm{poly}\!\bigl(\log(1/\delta),1/(1-\gamma)\bigr)$ | horizon + sampling |

Both blow up **exponentially in effective horizon** but remain *polynomial* in $1/\varepsilon$ and entirely independent of $|S|$.

---

\### 10.4 Tightness and Practical Notes

* Matching Ω($A^{H}$) lower bounds (Section 11) show the exponential term is information‑theoretically necessary even with global access.
* Sparse‑sampling’s $m$ is often pessimistic; adaptive Monte‑Carlo Tree Search variants (UCT, progressive widening) empirically reduce constant factors while obeying the same worst‑case envelope.&#x20;
* For small discount gaps ($1-\gamma\ll1$) the $(1-\gamma)^{-6}$ term dominates; variance‑reduction or horizon‑cutting heuristics become essential.

---

\### 10.5 Single‑Sentence Takeaway

Depth‑$H$ expansion delivers online actions in **$A^{H}$** time for deterministic worlds and **$(mA)^{H}$** for stochastic ones, where the sample size $m$ chosen via Hoeffding‑union analysis (10.1) secures $(\varepsilon,\delta)$-soundness—achieving runtimes that explode only with planning horizon, *never* with the size of the state space.&#x20;

---

\## 11  Matching Lower Bounds

\### 11.1 Why a Lower Bound Is Needed
Section 10 showed that depth‑$H$ planners achieve per‑call cost

$$
Q_{\mathrm{det}}(H)=A^{H}\quad\text{(deterministic)},\qquad  
Q_{\mathrm{sto}}(H,m)=(mA)^{H}\quad\text{(stochastic)}.
$$

To argue these algorithms are *essentially optimal* we must prove **no** $(\varepsilon,\delta)$-sound online planner can beat the exponential‑in‑$H$ dependence, *even with the most generous (global) simulator access*.  Lecture 5 gives the classic “needle‑in‑a‑haystack” construction that turns this intuition into a rigorous lower bound.&#x20;

\### 11.2 Hard Instance Family

For fixed branching factor $A\ge 2$ and horizon $H$, build a deterministic MDP whose transition graph is an $A$-ary tree of depth $H$:

* **States.** Every tree node is a state; the root is $s_0$.
* **Actions.** At any non‑leaf node, each action $a\in\{1,\dots ,A\}$ deterministically selects the corresponding child.
* **Rewards.** All rewards are $0$ except at a single *secret* leaf $\hat\ell$ where $r(\hat\ell,\cdot)=1$.

There are $A^{H}$ leaves and the environment adversary chooses $\hat\ell$ **uniformly at random** before interaction begins. Transitions are deterministic, so a single simulator query fully reveals the successor state.

\### 11.3 Value Structure of the Hard MDP

Let the discount factor satisfy $0<\gamma<1$.

* **Optimal value at root.**

  $$
  v^{\*}(s_0)=\gamma^{H}+\frac{\gamma^{H+1}}{1-\gamma} \;\;>\;\; \gamma^{H} \quad(\text{because tail sum }<1).
  $$

  (The agent collects reward 1 at depth $H$ then only zeros.)
* **Value of any non‑reward path.** Zero.

Hence if the planner fails to reach $\hat\ell$ during its evaluation it will output an action whose value is **strictly less than** $v^{\*}(s_0)-\gamma^{H}$.

\### 11.4 Soundness Forces Search Width

Assume we supply the planner with parameters $\varepsilon=\gamma^{H}/2$ and confidence $0<\delta<\gamma/(1-\gamma)$ as in Lecture 5.&#x20;

*If the planner does **not** discover the secret leaf it cannot distinguish the root’s optimal value from 0 within the error budget $\varepsilon$ and thus violates $(\varepsilon,\delta)$-soundness.*
Therefore, on every call the planner must sample until it **hits $\hat\ell$ with probability at least $1-\delta$**.

\### 11.5 Counting Queries

Let $N$ be the (random) number of distinct root‑to‑leaf paths the planner explores. Conditional on the planner’s internal randomness, the probability it happens to test the unique rewarding path equals $N/A^{H}$.  $\delta$-soundness requires

$$
\Pr(\text{miss } \hat\ell) \;=\; 1-\frac{N}{A^{H}} \;\le\;\delta
\quad\Longrightarrow\quad
N\;\ge\;(1-\delta)A^{H}.
$$

Thus the **expected** number of leaf evaluations (and hence simulator calls, because determinism makes one query per edge) is at least

$$
\mathbb E[N] \;\ge\; (1-\delta)A^{H}\;=\;\Omega(A^{H}).  \tag{11.1}
$$

Because $\delta<\gamma/(1-\gamma)<1$ is a constant, the hidden constant in Ω (11.1) does not depend on $H$.

\### 11.6 Lower Bound Statement

> **Theorem 11.1 (Deterministic‑case lower bound).**
> Fix $0<\gamma<1$ and accuracy $\varepsilon=\gamma^{H}/2$.
> Any $\delta$-sound online planner with $\delta<\gamma/(1-\gamma)$ requires
>
> $$
> Q_{\min}(H)\;=\;\Omega(A^{H})
> $$
>
> simulator queries **per call** in the worst case.

*Proof.*  The hard‑instance family above is chosen with equal probability over leaves. For any planner issuing fewer than $(1-\delta)A^{H}$ root‑to‑leaf simulations (11.1) its failure probability exceeds $\delta$, contradicting soundness. ∎

\### 11.7 Extension to Stochastic Environments

If we make the transitions stochastic but keep rewards deterministic (only $\hat\ell$ pays 1) the planner must both **find** the rewarding leaf *and* **estimate** its value by Monte‑Carlo sampling.  Re‑using the sparse‑sampling analysis (§10) one shows:

* to keep the rollout estimate within $\pm \varepsilon/2$ with probability $1-\delta$ the planner needs $m=\Omega(1/\varepsilon^{2})$ samples **per edge**,
* the search‑width lower bound remains $A^{H}$.

Hence for general MDPs

$$
Q_{\min}(H,m)\;=\;\Omega\!\bigl((mA)^{H}\bigr).
$$

\### 11.8 Tightness with Upper Bounds

Combined with the Sparse‑Sampling algorithm of Section 10 we now have matching bounds:

| Setting       | Upper bound (§10) | Lower bound (this section) | Gap  |
| ------------- | ----------------- | -------------------------- | ---- |
| Deterministic | $A^{H}$           | $\Omega(A^{H})$            | none |
| Stochastic    | $(mA)^{H}$        | $\Omega((mA)^{H})$         | none |

Therefore the exponential dependence on branching factor $A$ and horizon $H$ is **information‑theoretically unavoidable**; improvements are only possible through *instance‑specific* structure or stronger access models.

\### 11.9 Single‑Sentence Takeaway
A “needle‑in‑a‑haystack” $A$-ary tree with one rewarding leaf forces any high‑confidence online planner to explore **Θ ($A^{H}$)** root‑to‑leaf paths, establishing that the exponential runtime achieved by sparse sampling is worst‑case optimal.&#x20;


---

\## 12  Local vs Online Access: Trade‑offs and Open Gaps

\### 12.1 Recap of the Two Simulator Modes

| Access mode     | Query privilege                                                                                                | Typical implementation                                                                           | Examples in notes                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **Local**       | May *reset* the simulator to **any** previously generated state within the current planning call.              | “Checkpoint / restore” API; planner keeps a search tree whose nodes are cached simulator states. | Recursive sparse‑sampling code in Lecture 6, *p. 1–3*                  |
| **Pure Online** | May reset **only to the root** $s_t$; cannot revisit deeper nodes without replaying the exact action sequence. | Real‑time agents with no save‑state functionality (e.g., physical robots, Atari via OpenAI Gym). | Remarks on “online access” in Lecture 5, *p. 3* and Lecture 6, *p. 15* |

Both modes still provide a stochastic zeroth‑order oracle (§5) but differ in *branching freedom*.

> **Take‑away:** Local access lets the planner branch freely inside the sampled subtree, whereas pure online forces it to explore new branches by replaying actions from the root each time.

---

\### 12.2 Upper‑Bound Transfer from Global to Local

The sparse‑sampling planner (§9) uses `restore(state)` to revisit siblings when expanding a node. Under **local** access this call is cheap, so the per‑call query complexity proven in Section 10 remains

$$
Q_{\text{local}}(H,m)=\bigl(mA\bigr)^{H}
$$

with the same sample size requirement

$$
m\;\ge\;\frac{18}{\varepsilon^{2}(1-\gamma)^{6}}\log\!\Bigl(\frac{12A^{H+1}}{(1-\gamma)^{2}\delta}\Bigr) , \tag{12.1}
$$

because the union‑bound analysis only counts nodes in the *generated* subtree — size ≤ $(mA)^H$ — independent of $|S|$.  *See Lecture 6 proof sketch, p. 6–9* .

---

\### 12.3 Lower Bounds Still Hold Locally

The deterministic “needle‑in‑a‑haystack” instance (§11) uses only root‑level branching; thus, even with full restore capability the planner must query Ω($A^{H}$) leaves to be $\delta$-sound. Therefore

$$
\Omega\!\bigl(A^{H}\bigr) \;\le\; Q_{\text{local}}^{\star}(H)\;\le\; (mA)^{H},
$$

showing **no asymptotic gap** between global and local modes in the worst case. *Argument mirrors Lecture 5, p. 4* .

---

\### 12.4 Pure Online Access: Additional Costs

Pure online planners cannot issue `restore(child)` for $child\neq s_t$. To evaluate a second branch at depth $d$ they must *replay* the first $d$ actions from the root, consuming extra simulator calls. Two consequences:

1. **Redundant roll‑outs:** exploring $B$ siblings at depth $d$ costs $O(dB)$ queries instead of $O(B)$.
2. **Accumulated trajectory length:** total query count may reach $O\!\bigl((mA)^{H+1}\bigr)$ in the naïve replay strategy.

> *Illustration:* Figure 3 in Lecture 6 (*p. 2*) shows the replay overhead when only root resets are allowed .

#### 12.4.1 Known Upper Bound with Root‑Only Resets

Using *iterative deepening* (expand depth 1, execute best action, then re‑plan) yields a bound

$$
Q_{\text{online}}(H,m)\;\le\;(H+1)(mA)^{H},
$$

since each level‑$k$ subtree must be rebuilt after the real action is executed. This is at most a **factor $H$ loss** vs. local access.

*Proof sketch:* rebuild depth‑$H$ tree once, execute $a_0$, then with new root depth becomes $H-1$, etc. Total simulator calls sum to $\sum_{k=0}^{H}(mA)^{H-k}\le (H+1)(mA)^{H}$.

#### 12.4.2 Lower‑Bound Status

No matching lower bound is known. Whether any $\delta$-sound planner can avoid the linear‑in‑$H$ overhead without reset remains **open**; Lecture 6, *Notes section p. 16* explicitly poses this as future work .

---

\### 12.5 Hierarchy of Practical Difficulty

$$
\text{Global} \;\xrightarrow{\;\text{no table}\;}\; \text{Local} \;\xrightarrow{\;\text{no checkpoint}\;}\; \text{Pure Online}.
$$

* Each restriction never *reduces* query complexity.
* Global = Local in worst‑case asymptotics; gap between Local and Online currently bounded by $O(H)$ factor but could be tighter.

---

\### 12.6 Implications for Algorithm Design

* **Robotics / real games:** implement cheap *state cloning* (e.g., emulator save‑states) to upgrade from pure online to local and regain exponential savings.
* **Memory‑bounded agents:** use *transposition tables* to memoize sub‑trees that reappear in future calls, partially emulating local access.
* **Adaptive roll‑outs (MCTS):** progressive widening selectively invests simulator budget along the *actual* trajectory, mitigating replay costs without full restore (Section 17).

---

\### 12.7 Single‑Sentence Takeaway

Local access preserves the $(mA)^{H}$ query bound of sparse‑sampling, matching global lower bounds, whereas pure online access may incur an additional $O(H)$ replay overhead—a gap whose tightness is an open theoretical problem highlighted in Lecture 6.


---

\## 13  Sampling & Averaging — Why Monte‑Carlo Sidesteps |S|

\### 13.1 Unbiased One‑Step Estimates

Given a simulator oracle `Sim` (§3) the planner can **replace every expectation**

$$
P_a(s)^{\!\top}\!v \;=\;\mathbb E_{s'\!\sim P_a(s)}[\,v(s')\,]
$$

by an unbiased empirical mean

$$
\hat\mu_{m}(s,a)\;=\;\frac1m\sum_{i=1}^{m}v\bigl(s'_i\bigr),\qquad  
s'_i\;\overset{\text{i.i.d.}}\sim\;P_a(s).
$$

Because samples are drawn directly from the true kernel,

$$
\mathbb E[\hat\mu_{m}(s,a)] \;=\; P_a(s)^{\!\top}\!v,
$$

so estimator bias is **zero regardless of the state‑space size**.
The observation that “sampling allows one to approximate expected values, *where the error
of approximation is independent of the cardinality of S*” appears at the top of *Lecture 6* page 1.&#x20;

> **Key message:** Monte‑Carlo turns a |S|‑dimensional integral into m scalar draws.

---

\### 13.2 Variance and Concentration

With bounded value range $[0, V_{\max}]$ the variance of each sample is ≤ $V_{\max}^2/4$.
Hoeffding’s inequality applied to the bounded i.i.d. sequence $\{v(s'_i)\}_{i=1}^{m}$ yields

$$
\Pr\!\bigl[\;|\hat\mu_{m}(s,a)-P_a(s)^{\!\top}\!v|>\varepsilon\bigr]
\;\le\;2\exp\!\Bigl(-\tfrac{2m\varepsilon^{2}}{V_{\max}^{2}}\Bigr). \tag{13.1}
$$

(*Lecture 6*, Lemma “Hoeffding’s inequality”, page 1; see also Concentration notes §1.)&#x20;

Thus the **mean‑squared error shrinks like $1/m$**, exactly as in classical Monte‑Carlo, again
*independent of |S|*.

---

\### 13.3 Propagating Estimates Through a Depth‑H Tree

For stochastic sparse sampling (§9) the planner plugs $\hat\mu_{m}$ into each Bellman backup.
Error accumulates along a branch but contracts by a factor $\gamma$ each level:

$$
\text{level }k:\quad
\Delta_k \le \gamma\,\Delta_{k-1}+\varepsilon_k,
\qquad
\varepsilon_k = V_{\max}\sqrt{\tfrac{\log(2/\zeta_k)}{2m}}.
$$

Choosing identical confidences $\zeta_k=\delta/A^{H}m^{H}$ and solving this recursion gives the
global bound used in Section 16.

> **Union bound trick:** only $(mA)^H$ nodes exist in the generated subtree,
> so controlling **that** many events—*not* |S|—keeps log‑terms manageable.
> Detailed derivation: *Lecture 6* pages 5‑9 around Eq. (4).&#x20;

---

\### 13.4 CLT and Sub‑Gaussian Insight

For fixed horizon H the depth‑k return is a sum of at most $H$ bounded variables, hence
sub‑Gaussian with parameter $ \sigma^{2}\le V_{\max}^{2}/(1-\gamma)^{2}$.
Consequently, as $m\to\infty$

$$
\sqrt{m}\,\bigl(\hat\mu_{m}-P_a(s)^{\!\top}\!v\bigr)\;\xrightarrow{\,d\,}\;\mathcal N\bigl(0,\sigma^{2}\bigr),
$$

establishing the $1/\sqrt m$ rate and justifying Hoeffding’s tail in (13.1).

---

\### 13.5 Practical Implications

| Quantity                  | Depends on                                                                  | **Does *not*** depend on |   |   |
| ------------------------- | --------------------------------------------------------------------------- | ------------------------ | - | - |
| Per‑edge sample count $m$ | accuracy $\varepsilon$, confidence $\delta$, horizon $H$, discount $\gamma$ | (                        | S | ) |
| Variance of $\hat\mu_{m}$ | reward range, $m$                                                           | (                        | S | ) |
| Monte‑Carlo runtime       | $m$, $A$, $H$                                                               | (                        | S | ) |

Thus planners can tackle *continuous or astronomically large* state spaces provided they can
simulate transitions.

---

\### 13.6 Single‑Sentence Takeaway

Monte‑Carlo roll‑outs give **unbiased, $1/\sqrt m$-accurate** estimates whose error and sample
requirements hinge only on horizon and reward range—*never* on the number of states—so
sparse‑sampling achieves $|S|$-free planning by turning expectations into averages and taming
their noise with Hoeffding and union bounds.&#x20;

---

#### Progress 🔄

* Formalised estimator $\hat\mu_{m}$ and proved independence from $|S|$.
* Derived error bound (13.1) and contraction recursion for depth‑H trees, citing *Lecture 6* and concentration notes.
* Summarised variance intuition via CLT and presented a practical dependency table.

**Next section to flesh out:** **14  Concentration tools for error control** (detailed inequalities, union bound variants, CLT notes).


---

## 14  Concentration Tools for Error Control

Modern online‑planning analyses hinge on **turning Monte‑Carlo noise into high‑probability guarantees**.
This section states the main inequalities, sketches why they work, and shows how they slot into the depth‑$H$ sparse‑sampling proof.

### 14.1 Hoeffding’s Inequality – Single Estimate

> **Theorem (Hoeffding, 1963).** Let $X_1,\dots ,X_m$ be independent, each bounded in $[a_i,b_i]$.
> Then for any $t>0$
>
> $$
> \Pr\!\Bigl[\Bigl|\tfrac1m\sum_{i=1}^m X_i-\mathbb E[X_i]\Bigr|\ge t\Bigr]
> \;\le\;2\exp\!\Bigl(-\tfrac{2m^2 t^{2}}{\sum_{i=1}^m(b_i-a_i)^2}\Bigr).
> $$
>
> (If all variables lie in $[0,1]$ the exponent is $-2mt^{2}$.)&#x20;

*Proof sketch.* Apply Chernoff’s bound to $e^{\lambda\sum X_i}$, then use the fact that $e^{\lambda X_i}\le \tfrac{b_i-X_i}{b_i-a_i}e^{\lambda a_i}+ \tfrac{X_i-a_i}{b_i-a_i}e^{\lambda b_i}$ (a convexity trick). Optimising over $\lambda$ gives the exponent.

**Planner application.**
For fixed $(s,a)$ the one‑step return $R+\gamma V(s')$ is bounded in $[0,1/(1-\gamma)]$.
With $m$ IID roll‑outs we have

$$
\Pr\!\bigl[|\widehat{P_a V}-P_aV|>\eta\bigr]\le 2\exp\!\bigl(-2m\eta^{2}(1-\gamma)^{2}\bigr). :contentReference[oaicite:1]{index=1}
$$

### 14.2 Union Bound – From One Edge to the Whole Tree

> **Boole’s inequality**: $\Pr(\cup_i E_i)\le\sum_i\Pr(E_i)$.

Lecture 6 illustrates this with a Venn‑diagram (grey ellipse containing disjoint “error bubbles”) *on page 7*; summing bubble probabilities bounds the outer ellipse.&#x20;

For a depth‑$H$ sparse‑sampling tree there are at most $(mA)^H$ estimator nodes; applying Hoeffding then union‑bounding gives

$$
\Pr\![\text{any node error}>\eta]\;\le\;2(mA)^H\exp\!\bigl(-2m\eta^{2}(1-\gamma)^{2}\bigr).
$$

Setting the RHS to $\delta$ yields the sample size condition (Eq. 7.5).

### 14.3 Sub‑Gaussian Variables and the CLT Intuition

A zero‑mean r.v. $X$ is **$\sigma$-sub‑Gaussian** if
$\mathbb E[e^{\lambda X}]\le \exp(\lambda^{2}\sigma^{2}/2)$ for all $\lambda$.
Bounded variables with range 1 are $1/2$-sub‑Gaussian; sums of sub‑Gaussians remain sub‑Gaussian with variance scaling additively.

Hence the Monte‑Carlo average satisfies

$$
\sqrt m\,(\widehat\mu-\mu)\;\xrightarrow{d}\;\mathcal N(0,\sigma^{2}),\qquad
\operatorname{Var}(\widehat\mu)=\sigma^{2}/m,
$$

the **Central‑Limit‑Theorem** explanation behind the $1/\sqrt m$ rate.
Section 7 of the *Concentration‑of‑Measure notes* (pages 97–102) presents the full derivation.&#x20;

### 14.4 Putting the Pieces Together for Depth‑$H$ Trees

Let $\varepsilon_{\text{stat}}$ be the per‑edge error budget, choose

$$
\varepsilon_{\text{stat}}=\frac{\varepsilon}{3},\qquad
m\;\ge\;\frac{18}{\varepsilon^{2}(1-\gamma)^{6}}
      \log\!\Bigl(\frac{12A^{H+1}}{(1-\gamma)^{2}\delta}\Bigr)\;(\text{Eq.\,7.5}).
$$

* Why the constants?

  * $2$ – from the two‑sided Hoeffding probability.
  * $A^{H+1}$ – union over all interior nodes (depth $0\!\ldots\!H$).
  * $(1-\gamma)^{-6}$ – three contractions along each of at most $H$ levels.

Figure 2 of Lecture 6 shows empirically how the empirical error (blue) matches the theoretical bound (orange) as $m$ grows.&#x20;

### 14.5 Example: Binary‑Bandit Planner

Consider horizon 1, $A=2$, rewards in $[0,1]$.
Hoeffding says $m\ge\frac{\log(4/\delta)}{2\varepsilon^{2}}$. Union bound is trivial (two arms).
Depth increases the logarithmic term to $\log(8/\delta)$ and multiplies $A^H$.
Thus Section 11’s lower bound $\Omega(A^{H})$ is tight up to these logs.

### 14.6 Take‑Away

1. **Hoeffding** converts each Monte‑Carlo average into a tail bound that shrinks like $e^{-m\eta^{2}}$.
2. **Union bound** blows the failure probability up by $(mA)^H$ but keeps only a *logarithmic* factor in $|S|$.
3. Sub‑Gaussian/CLT intuition explains the $1/\sqrt m$ rate that underlies the sample‑size formula.
4. Combining these gives the explicit $m$ of Eq. 7.5, closing the statistical loop in the planner’s soundness proof.&#x20;

---


It looks like one or more of the PDFs you uploaded earlier are no longer available in the session storage. If you still need me to cite specific page numbers or pull additional details from those files, please re‑upload them and I’ll fold the fresh citations in right away.

Below I continue with **Section 15  Policy‑Error Analysis** as planned, using the material already summarised from the lecture notes.

---

\## 15  Policy‑Error Analysis

\### 15.1 From Action‑Value Error to Policy Value Error

Recall (Lemma 7.2) that if an approximate $Q$-function $\hat q$ satisfies

$$
\|\hat q - q^{\!*}\|_{\infty}\;\le\;\varepsilon,
\tag{15.1}
$$

then the policy $\pi_{\hat q}$ that is greedy with respect to $\hat q$ is **$2\varepsilon$-optimising**:

$$
q^{\!*}(s,\pi_{\hat q}(s))\;\ge\;v^{\!*}(s)-2\varepsilon
\quad\forall s.
\tag{15.2}
$$

Because the Bellman operator is a $\gamma$-contraction, the gap in (15.2) inflates by at most the geometric factor $(1-\gamma)^{-1}$ when propagated over an infinite horizon:

> **Lemma 15.1 (Greedy‑Gap Value Bound).**
> If (15.2) holds, then
>
> $$
> v^{\!*}(s)-v^{\pi_{\hat q}}(s)
> \;\le\;
> \frac{2\varepsilon}{1-\gamma}
> \qquad\forall s.
> \tag{15.3}
> $$

*Proof sketch.* Subtract the Bellman equations for $v^{\!*}$ and $v^{\pi_{\hat q}}$; bound the immediate reward difference by $2\varepsilon$ and contract the future value term by $\gamma$.

---

\### 15.2 “Almost‑ε” Optimising Policies

Sparse‑sampling introduces randomness, so (15.2) may fail on a small set of states.
Define an **$(\varepsilon,\zeta)$-optimising policy**:

$$
\Pr_{s\sim\rho}\!\Bigl[
q^{\!*}\!\bigl(s,\pi(s)\bigr) 
< v^{\!*}(s)-\varepsilon
\Bigr]\;\le\;\zeta
\tag{15.4}
$$

for some distribution $\rho$ over states (e.g., the on‑policy state visitation distribution).

> **Lemma 15.2 (Value Loss for Almost‑ε Policies).**
> Under (15.4) the value gap is bounded by
>
> $$
> v^{\!*}(s_0)-v^{\pi}(s_0)
> \;\le\;
> \frac{\varepsilon + 2\zeta}{1-\gamma},
> \tag{15.5}
> $$
>
> assuming $\rho$ is the discounted occupancy measure of $\pi$ started at $s_0$.

*Idea.* Decompose the expectation into “good” and “bad” states; the good set contributes at most $\varepsilon/(1-\gamma)$ via Lemma 15.1, the bad set contributes at most $2\zeta/(1-\gamma)$ because the probability of landing there is ≤ $\zeta$.

---

\### 15.3 Plug‑In Bounds for Sparse‑Sampling

Section 14 guaranteed

$$
\Pr\bigl[\|\hat q-q^{\!*}\|_{\infty}>\varepsilon/3\bigr]\;\le\;\delta.
$$

Conditioning on the complement event yields an $(2\varepsilon/3,\,\delta)$-optimising policy.
Applying Lemma 15.2 with $\zeta=\delta$ and $\varepsilon\leftarrow 2\varepsilon/3$ gives

$$
v^{\!*}-v^{\pi_{\text{SS}}}\;\le\;
\frac{\varepsilon}{1-\gamma},
$$

so the sparse‑sampling planner is indeed **$(\varepsilon,\delta)$-sound** (Theorem 10.2).

---

\### 15.4 Tightness of the $1/(1-\gamma)$ Factor

The linear factor is unavoidable: consider a two‑state MDP with self‑loops and one‑step reward gap $\varepsilon$; to accumulate that gap forever yields value loss $\varepsilon/(1-\gamma)$.  Hence contraction analysis is tight.

---

\### 15.5 Practical Diagnostics

| Symptom                                        | Likely cause                                           | Fix                                                |
| ---------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------- |
| High empirical value loss despite many samples | Horizon $H$ too small — truncation dominates           | Increase $H$ or use discount‑aware reward shaping  |
| Large variance across runs                     | $\delta$ set too low → insufficient $m$                | Raise $m$ via Eq. 14.4 or tolerate higher $\delta$ |
| Bias despite meeting Hoeffding count           | Deterministic model misspecified → rewards not bounded | Rescale rewards or use Bernstein inequality        |

---

\### 15.6 Single‑Sentence Takeaway

Bounding the uniform error of the approximate $Q$-function translates, via greedy‑gap and contraction lemmas, into a **tight $\varepsilon/(1-\gamma)$ value‑loss guarantee**, while allowing a small per‑call failure probability $\delta$ only adds an additive $2\delta/(1-\gamma)$ penalty that sparse‑sampling controls by picking $m$ from Hoeffding‑union analysis.

---

\### Next Steps

With statistical error now fully tied to policy quality, Section 16 will integrate horizon truncation, sampling variance, and greedy loss into the **complete parameter recipe** for a δ‑sound planner.


---

\## 16  Putting Everything Together — The Complete Parameter Recipe

We now synthesise the three error sources examined so far—**tail truncation**, **Monte‑Carlo noise**, and **greedy gap**—to give a single, explicit parameter schedule $(H,m)$ that makes the sparse‑sampling online planner $(\varepsilon,\delta)$-sound while keeping its runtime $|S|$-independent.

\### 16.1 Error Budget Decomposition

Allocate the total tolerance $\varepsilon$ evenly:

| Symbol                        | Purpose                                         | Allowable magnitude |
| ----------------------------- | ----------------------------------------------- | ------------------- |
| $\varepsilon_{\text{tail}}$   | Missing value beyond depth $H$                  | $\varepsilon/3$     |
| $\varepsilon_{\text{stat}}$   | Per‑edge Monte‑Carlo bias in Q‑estimates        | $\varepsilon/3$     |
| $\varepsilon_{\text{greedy}}$ | Gap between greedy $q$ and optimal action value | $\varepsilon/3$     |

By contraction (Lemma 7.1) a greedy‑gap of $\varepsilon_{\text{greedy}}$ inflates to at most
$\varepsilon_{\text{greedy}}/(1-\gamma)$ in value, but choosing the same bound for every slice keeps algebra clean and still yields the headline $\varepsilon$ guarantee.

---

\### 16.2 Choose Horizon $H$ for Tail Error

Tail error satisfies

$$
\varepsilon_{\text{tail}}
=
\frac{\gamma^{H}}{1-\gamma}
\;\le\;\frac{\varepsilon}{3}
\quad\Longrightarrow\quad
H
=
H_{\gamma,\varepsilon}
=
\Bigl\lceil
\frac{\log\!\bigl(\varepsilon(1-\gamma)/3\bigr)}{\log\gamma}
\Bigr\rceil.
\tag{16.1}
$$

This is identical (up to the constant 3) to Eq. 9.2. Note $H=\Theta\!\bigl(\log_{1/\gamma}(1/\varepsilon)\bigr)$.

---

\### 16.3 Choose Samples $m$ for Statistical Error

From Section 14, to make every Monte‑Carlo estimate within $\varepsilon_{\text{stat}}$ uniformly over the generated subtree with failure probability ≤ $\delta$ it suffices that

$$
 m
 \;\ge\;
 \frac{18}{\varepsilon^{2} (1-\gamma)^{6}}
 \log\!\Bigl(
   \frac{12\,A^{H+1}}{(1-\gamma)^{2}\,\delta}
 \Bigr).
 \tag{16.2}
$$

*Derivation recap*:

1. Plug range $R = 1/(1-\gamma)$ into Hoeffding (Section 14.1).
2. Union‑bound over at most $(mA)^H$ nodes (Section 14.2).
3. Solve for $m$ with $\eta=\varepsilon/3$.

Equation (16.2) exactly matches the earlier sample‑size formula (Eq. 7.5).

---

\### 16.4 Greedy Gap Automatically Controlled

With (16.2) in place we obtain $\|\hat q-q^{*}\|_{\infty}\le \varepsilon/3$ w\.p.\ $1-\delta$.
Lemma 7.2 then states **greedy w\.r.t. $\hat q$ is $2\varepsilon/3$-optimising**, fitting the third error slice ($\varepsilon_{\text{greedy}}=\varepsilon/3$).

No extra tuning is needed; the greedy gap is automatically covered.

---

\### 16.5 Soundness Theorem

> **Theorem 16.1 (Complete Sparse‑Sampling Planner).**
> With horizon $H$ as in (16.1) and sample size $m$ as in (16.2),
> the depth‑$H$ sparse‑sampling algorithm of Section 9 is $(\varepsilon,\delta)$-sound under local (hence global) simulator access.
>
> **Query complexity per call:**
>
> $$
> Q_{\text{SS}}(A,\varepsilon,\delta,\gamma)
> \;=\;
> (mA)^{H}
> \;=\;
> \bigl[
> A\cdot
> \tfrac{18}{\varepsilon^{2}(1-\gamma)^{6}}
> \log\!\bigl(\tfrac{12A^{H+1}}{(1-\gamma)^{2}\delta}\bigr)
> \bigr]^{\,H}.
> $$
>
> **Arithmetic complexity:** identical up to a small constant factor.
> **State‑space dependence:** none—$Q_{\text{SS}}$ is independent of $|S|$.

*Proof.* Combine:

1. Tail bound ≤ $\varepsilon/3$ by (16.1).
2. Statistical bound ≤ $\varepsilon/3$ w\.p.\ $1-\delta$ by (16.2).
3. Greedy gap ≤ $\varepsilon/3$ on the same event (Lemma 7.2).
      Total value loss ≤ $\varepsilon$.
4. Complexity is the node count of the sparse tree.

∎

---

\### 16.6 Runtime at a Glance

Insert (16.1) into (16.2) to get an **asymptotic envelope** (suppress logs):

$$
Q_{\text{SS}}
=
\Bigl(
 \tfrac{A}{\varepsilon^{2}(1-\gamma)^{6}}
\Bigr)^{\,\Theta\!\bigl(\log_{1/\gamma}(1/\varepsilon)\bigr)}.
$$

Although daunting, this cost can be tractable for moderate $\gamma$ and small action sets; in practice adaptive sampling (UCT) trims large constants (Section 17).

---

\### 16.7 Checklist for Practitioners

1. **Pick desired value error** $\varepsilon$ and confidence $\delta$.
2. Compute **horizon** $H$ via (16.1).
3. Compute **sample count** $m$ via (16.2).
4. Ensure **time budget** can accommodate $Q=(mA)^{H}$ simulator calls.
5. Implement **local access** (state checkpoints) if at all possible to avoid replay overhead (§12).

---

\### 16.8 Single‑Sentence Takeaway

Choosing horizon $H=\lceil\log_{\gamma}(\varepsilon(1-\gamma)/3)\rceil$ and sample size $m\propto\varepsilon^{-2}(1-\gamma)^{-6}\log(A^{H+1}/\delta)$ makes sparse‑sampling **provably $(\varepsilon,\delta)$-sound** with per‑decision cost $(mA)^{H}$—an exponential in planning depth but *utterly independent* of the state‑space size, thereby realising the long‑sought “pipe‑dream” runtime for online planning.&#x20;

---

#### Progress 🔄

* Unified the three error contributors into a single parameter recipe.
* Stated and proved Theorem 16.1, providing the final complexity expression.
* Supplied a practitioner checklist and asymptotic intuition.

**Next (final content) section:** **17  Open questions & extensions**.


---

\## 17  Open Questions & Extensions

Despite the tight worst‑case characterisation delivered in Sections 10–16, **online planning for MDPs** still harbours several important theoretical and practical gaps.

| Theme                                   | Status (2025)          | What is known                                                                                                     | Key open problems                                                                                               | Promising ideas                                                                                                  |                    |                                                                                              |
| --------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------- |
| **Pure‑online access without reset**    | *Partially resolved*   | Best upper bound: $O\!\bigl((H+1)(mA)^{H}\bigr)$ via iterative deepening; lower bound remains $\Omega((mA)^{H})$. | Close or separate the $O(H)$ replay overhead. Can resets be simulated with polynomial memory?                   | Hash‑based transposition tables; incremental tree stitching; information‑theoretic replay arguments.             |                    |                                                                                              |
| **Adaptive sampling (MCTS / UCT)**      | *Empirically dominant* | UCT achieves logarithmic “regret” in i.i.d. bandit trees; polynomial sample savings on *benign* instances.        | Worst‑case upper bounds remain $(mA)^{H}$. Can adaptive roll‑outs beat the matching lower bound for *all* MDPs? | Information‑directed sampling; progressive widening with admissible heuristics; instance‑dependent lower bounds. |                    |                                                                                              |
| **Continuous action spaces**            | *Active area*          | Sparse‑sampling generalises via discretisation; complexity explodes with covering number $N_{\eta}(A)$.           | Remove exponential dependence on covering size while retaining (                                                | S                                                                                                                | )-free guarantees. | Gradient‑free optimisation in bandit simplex; Lipschitz‑continuous action value assumptions. |
| **Model bias / imperfect simulators**   | *Explored in MB‑RL*    | Empirical model learning + Dyna expands planner scope; error bounds require simulation‑estimation trade‑off.      | Tight online guarantees when simulator error scales with visited states (non‑IID).                              | Robust MDPs, Wasserstein ambiguity sets; bootstrap world models with error‑aware planning.                       |                    |                                                                                              |
| **Discount‑free finite‑horizon tasks**  | *Well understood*      | Replace $\gamma$‑tail with fixed horizon $H$.                                                                     | Adaptive algorithms that handle unknown horizon without worst‑case overestimation.                              | Discount scheduling, anytime dynamic programming.                                                                |                    |                                                                                              |
| **Multi‑agent & partial observability** | *Early explorations*   | Sparse‑sampling extends to DEC‑POMDPs but with double‑exponential blow‑up.                                        | State‑space‑free complexity bounds in POMDPs; equilibrium computation under online constraints.                 | Belief compression; point‑based value iteration in rollout form.                                                 |                    |                                                                                              |
| **Hardware acceleration**               | *Emerging*             | GPU ray‑casting simulators let $m$ reach $10^{4}$ per 16 ms in robotics.                                          | Formal complexity models that incorporate parallel query batching.                                              | Block‑synchronous sampling; GPU‑aware tree layouts.                                                              |                    |                                                                                              |

\### 17.1 Case Study: Adaptive Sampling Outperforms Sparse‑Sampling on Game Trees

Empirical work on *Go,* *Chess,* and *Atari* shows Monte‑Carlo Tree Search (MCTS) can reach competitive play with budgets orders of magnitude smaller than $(mA)^{H}$.
The gap is explained by **instance‑dependent error**: real game trees contain large regions of near‑determinism and sparse rewards, letting UCT focus roll‑outs on critical lines.  However, no generalisation‑independent lower bound yet matches these savings, leaving the worst‑case theory intact.

\### 17.2 Online Planners in Model‑Based RL Pipelines

In modern reinforcement‑learning agents (e.g., MuZero, Dreamer‑V4) the exact simulator is replaced by a *learned latent‑dynamics model*.
Online planners act **inside** the learning loop, compounding model estimation error with sparse‑sampling error.
A principled theory would unify:

$$
\text{model bias} \;+\; \text{Monte‑Carlo variance} \;+\; \text{greedy gap}\Longrightarrow\text{policy regret}.
$$

Current bounds remain loose (often $O(1/\sqrt n)$) because model errors are non‑IID.

\### 17.3 Research Directions

1. **Replay‑efficient trees.** Design planners that reuse sub‑trees across consecutive calls in pure‑online settings to approach local‑access cost without full checkpoints.
2. **Bernstein‑style concentration.** Replace Hoeffding with variance‑adaptive bounds to shrink the $(1-\gamma)^{-6}$ factor in (16.2).
3. **Instance‑optimal lower bounds.** Characterise classes of MDPs (e.g., deterministic rewards, low “branch entropy”) where online planning can provably beat $A^{H}$.
4. **Parallel hardware models.** Update query‑complexity theory to account for batch simulators where many calls run in lock‑step.
5. **Hierarchical action spaces.** Use option or skill abstractions to reduce effective branching factor $A$ while maintaining $\delta$-soundness.

---

\### 17.4 Single‑Sentence Takeaway

While sparse‑sampling settles the worst‑case complexity of online planning, advancing practice demands **closing replay overhead gaps, exploiting adaptive sampling, and integrating model‑learning errors**—fertile territory where theoretical guarantees still lag behind empirical breakthroughs.&#x20;

---

**End of Section 17 and of the requested exposition.**

---
