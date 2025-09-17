---
date: "2025-07-13"
title: "(3) Briefly on Multi-Agent RL" 
summary: "(3) Briefly on Multi-Agent RL"
lastmod: "2025-07-13"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### Hierarchy of game models in Chapter 3

| Level in the hierarchy                          | Formal tuple (illustrative)                                                                                                   | What is **new** compared with the level below                                                                                                                 | Where defined / illustrated        |                        |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ---------------------- |
| **Normal‑form (strategic) game**                | ⟨ *I*, {*Aᵢ*}, {*Rᵢ*} ⟩                                                                                                       | One‑shot, simultaneous move; no notion of state or time.                                                                                                      | Definition 2 and Fig 3.2, p. 44–46 |                        |
| **Repeated normal‑form game**                   | The same normal‑form game played for *T* steps (finite or infinite); policies π(a\|h) depend on the joint‑action history *h*. | Introduces temporal structure and memory, but still no explicit environment state.                                                                            | § 3.2, p. 47 f.                    |                        |
| **Stochastic game (Markov game)**               | ⟨ *I*, *S*, {*Aᵢ*}, *T*, {*Rᵢ*}, µ ⟩                                                                                          | Adds a fully observable environment state that evolves via a Markov transition kernel \*T(s′                                                                  |  s,a)\*.                           | Definition 3, p. 48 f. |
| **Partially Observable Stochastic Game (POSG)** | Same as stochastic game **plus**:<br>• observation sets { *Oᵢ* }<br>• observation functions *Oᵢ(a,s,oᵢ)*                      | Agents no longer see the true state; they act on (possibly noisy) private observations—capturing hidden information, sensing limits, and noisy communication. | Definition 4, p. 51–53             |                        |

The book depicts these relationships in **Figure 3.1**:
*Normal‑form* ⟶ *Repeated* ⟶ *Stochastic* ⟶ *POSG*, with each level strictly generalising the one before and including it as a special case (e.g., an MDP is a one‑agent stochastic game).&#x20;

---

#### Reward‑structure axis (orthogonal to the hierarchy)

At **every** level above, games may be further characterised as:

* **Zero‑sum** – agents’ rewards sum to zero.
* **Common‑reward (fully co‑operative)** – all agents share the same reward.
* **General‑sum** – no restriction on how rewards relate.

These categories are introduced for normal‑form games and explicitly carried up to stochastic games and POSGs.

---

#### Why the distinctions matter

* **Choosing the minimal adequate model** – If your application has no hidden state, a repeated normal‑form game may suffice; if sensors are noisy, you need a POSG.
* **Algorithm implications** – Zero‑sum stochastic games invite minimax or self‑play methods; common‑reward POSGs map to decentralised POMDP solvers; general‑sum POSGs often require equilibrium‑seeking or opponent‑modelling techniques.
* **Research clarity & reproducibility** – Writing down the full tuple (agents, actions, state, transition, rewards, observations) forces clarity about assumptions and makes environments unambiguous.

These four models—normal‑form, repeated, stochastic and partially observable stochastic—form the conceptual backbone on which the rest of the text builds solution concepts (Chapter 4) and learning algorithms (Parts II–III).


![Hierarchy of game models](https://raw.githubusercontent.com/13ryanC/13ryanC.github.io/main/content/posts/RLtheory/topics/MARL/images/hierarchy_game_models.png) 


---


Below is a step‑by‑step tour through the **hierarchy of game models** introduced in Chapter 3. Each level adds exactly the extra machinery needed to represent richer real‑world interactions, so you can pick the simplest one that still captures the phenomena you care about.

---

## 0.  Markov Decision Process (MDP) – *“one‑agent leaf”*

> **Tuple:** ⟨ *S*, *A*, *T*, *R*, µ ⟩
> Although the chapter’s focus is multi‑agent, Figure 3.1 explicitly anchors the ladder with the familiar single‑agent MDP.  An MDP has:

* one agent,
* a fully observable environment state,
* Markovian dynamics *T(s′ | s,a)* and reward *R(s,a,s′)*.

All higher‑level game models reduce to an MDP when you collapse the agent set to a singleton.

---

## 1.  Normal‑form (Strategic) Game

> **Tuple:** ⟨ *I*, {*Aᵢ*}, {*Rᵢ*} ⟩

* **What it is:** A *single* simultaneous‑move interaction; no notion of state or time.
* **Key properties**

  * Pay‑off matrix fully specifies incentives (hence “matrix game” for two players).
  * Reward‑structure tags – *zero‑sum*, *common‑reward*, *general‑sum* – are defined here and inherited upward.
* **Why it matters:** Serves as the atomic kernel; every later model can be viewed as “gluing together” normal‑form games (see Figure 3.3).

---

## 2.  Repeated Normal‑form Game

> **Construction:** Play the same normal‑form game for *T* discrete rounds (finite or infinite).

* **New element:** *Time* and *memory*.  Policies may condition on the entire joint‑action history *hₜ* rather than a single stage.
* **Subtleties**

  * Finite vs. infinite horizon leads to “end‑game” effects; infinite repetition is often modelled by a geometric termination probability, linking directly to the RL discount factor γ = 1 − pₜₑᵣₘ.
  * Famous history‑based strategies such as Tit‑for‑Tat live in this space.

---

## 3.  Stochastic Game (a.k.a. Markov Game)

> **Tuple:** ⟨ *I*, *S*, {*Aᵢ*}, *T*, {*Rᵢ*}, µ ⟩

* **New element:** An explicit, fully observable **state** that evolves stochastically according to the *joint* action.
* **Key characteristics**

  * Retains the Markov property just like an MDP.
  * Includes a repeated normal‑form game as the special case |S| = 1 (the environment never changes).
  * Also subsumes the single‑agent MDP when |I| = 1.
* **Typical use‑cases:** Multi‑robot coordination, team sport simulators, any setting where the world carries a separate evolving state.

---

## 4.  Partially Observable Stochastic Game (POSG) – *top of the ladder*

> **Adds per agent:** observation set *Oᵢ* and observation function *Oᵢ(a,s,oᵢ)*

* **New element:** **Partial observability.**  Agents receive private, possibly noisy observations rather than the true state.
* **Consequences**

  * Agents must act on *observation histories* and maintain belief states; Eq. 3.5 shows the exact Bayesian filter for a single agent.
  * POSG collapses to:

    * a stochastic game when observations reveal (s, a) exactly.
    * a POMDP when |I| = 1.
* **Special cases:** Common‑reward POSGs are known as Dec‑POMDPs – the canonical model for decentralised multi‑robot planning.

---

### Orthogonal Dimensions that Cut Across the Hierarchy

| Dimension                 | How it is specified                                                                                                      | Impact                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **Reward structure**      | zero‑sum / common‑reward / general‑sum                                                                                   | Determines appropriate solution concepts (minimax, team‑optimal, Nash). Defined for normal‑form games and inherited upward. |
| **Communication actions** | Split each action into (environment‑act, message) – messages appear in others’ observations but not the state transition | Allows modelling of emergent protocols or lossy channels at any level.                                                      |
| **Knowledge assumptions** | Which elements (S, T, Rᵢ, Oᵢ, n) are known, unknown, or common knowledge                                                 | Drives the choice between model‑based planning and model‑free learning.                                                     |

---

## Visual Summary

Figure 3.1 from the text places the models in a *nested* diagram:

```
          +-----------------------------+
          | Partially Observable SG     |
          |  (POSG)                    |
          +---------------+-------------+
                          |
            +-------------v-----------+
            |  Stochastic Game        |
            +-------------+-----------+
                          |
            +-------------v-----------+
            | Repeated Normal‑form    |
            |        Game             |
            +-------------+-----------+
                          |
            +-------------v-----------+
            |   Normal‑form Game      |
            +-------------+-----------+
                          |
            +-------------v-----------+
            |    MDP (single agent)   |
            +-------------------------+
```

Each box **strictly contains** the one below: remove partial observability ➜ stochastic game; collapse S to one state ➜ repeated game; remove time ➜ normal‑form game; collapse agents to one ➜ MDP.

---

### How to Use This Hierarchy in Practice

1. **Start simple.**  Ask: *Do I need an evolving state? Do agents have private information?*
   *If no state → normal‑form; if state but full information → stochastic; if hidden state → POSG.*
2. **Tag the reward structure** to anticipate algorithm families (e.g., self‑play for zero‑sum, value‑decomposition for common‑reward).
3. **Document the tuple** (agents, actions, state, transitions, rewards, observations).  This forces clarity and makes your environment reproducible.
4. **Add communication** only when messages must be treated strategically rather than as a side‑channel API.

Mastering this ladder of models lets you describe *any* multi‑agent interaction precisely and choose algorithms whose assumptions actually match your problem.


---


### Mathematical specification of each model & how they nest

| Level                                              | Formal definition (tuple + constraints)                                                                                                                                                                                                                     | New mathematical ingredients relative to the level **below**                                                                                                                                             | Supersets / special‑case relations                                                                        |                                                                                                         |        |                             |   |       |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------ | --------------------------- | - | ----- |
| **0. Markov Decision Process (MDP)**               | ⟨ *S*, *A*, *T*, *R*, µ ⟩ where *T*: S × A × S → \[0,1], *R*: S × A × S → ℝ, µ: S → \[0,1] and ∑<sub>s′</sub>*T*(s,a,s′)=1.                                                                                                                                 | Single agent; fully observed state.                                                                                                                                                                      | Special case of every multi‑agent model with                                                              | I                                                                                                       |  = 1.  |                             |   |       |
| **1. Normal‑form game**                            | ⟨ *I*, {A<sub>i</sub>}, {R<sub>i</sub>} ⟩ with finite agent set *I* and action Cartesian product *A* = Π<sub>i</sub>A<sub>i</sub>. Each R<sub>i</sub>: *A* → ℝ.                                                                                             | Introduces **multiple agents**; still one shot, no state/time.                                                                                                                                           | Becomes an MDP when                                                                                       | I                                                                                                       |  = 1.  |                             |   |       |
| **2. Repeated normal‑form game**                   | Given a stage game G = ⟨*I*, {A<sub>i</sub>}, {R<sub>i</sub>}⟩, play for *t = 0…T‑1* (T finite or ∞). Each policy ω<sub>i</sub>(a<sub>i,t</sub>                                                                                                             |  h<sub>t</sub>) is a distribution over A<sub>i</sub> conditioned on the **joint‑action history** h<sub>t</sub> = (a₀,…,a<sub>t‑1</sub>). Per‑round reward: r<sub>i,t</sub>=R<sub>i</sub>(a<sub>t</sub>). | Adds **time index** and **memory** (history‑dependent strategies).                                        | Stage game is recovered with T = 1. Discounted infinite play maps to RL via γ = 1 − p<sub>term</sub>.   |        |                             |   |       |
| **3. Stochastic game (Markov game)**               | ⟨ *I*, *S*, {A<sub>i</sub>}, *T*, {R<sub>i</sub>}, µ ⟩ with *T*: S × A × S → \[0,1], R<sub>i</sub>: S × A × S → ℝ; Markov property                                                                                                                          |                                                                                                                                                                                                          |                                                                                                           |                                                                                                         |        |                             |   |       |
| Pr(s<sub>t+1</sub>, r<sub>t</sub>                  |  history)=Pr(s<sub>t+1</sub>, r<sub>t</sub>                                                                                                                                                                                                                 |  s<sub>t</sub>, a<sub>t</sub>).                                                                                                                                                                          | Adds a **fully observable state process**. History h<sub>t</sub> now alternates states and joint actions. | Contains the repeated game when                                                                         | S      |  = 1; contains an MDP when  | I |  = 1. |
| **4. Partially‑Observable Stochastic Game (POSG)** | Extends stochastic game with, for each agent *i*:  • finite observation set O<sub>i</sub>  • observation function O<sub>i</sub>: A × S × O<sub>i</sub> → \[0,1] s.t. ∑<sub>o</sub>O<sub>i</sub>(a,s,o)=1. Agent *i*’s policy ω<sub>i</sub>(a<sub>i,t</sub>  |  h<sup>o</sup><sub>i,t</sub>) depends on its **private observation history** h<sup>o</sup><sub>i,t</sub> = (o<sub>i,0</sub>,…,o<sub>i,t</sub>).                                                          | Introduces **partial observability**; agents no longer share the true state or one another’s actions.     | Reduces to a stochastic game when observations reveal (s<sub>t</sub>,a<sub>t−1</sub>); to a POMDP when  | I      |  = 1.                       |   |       |

---

#### Composition: how each model **builds on** the previous

1. **Time composition**  
   Repeated game = ∑<sub>t=0}^{T‑1} G  
   (sequential composition of identical stage games)

2. **State composition**  
   Stochastic game = ⨁<sub>s∈S</sub> G<sub>s</sub> where each state s indexes a *local* normal‑form game with pay‑offs R<sub>i</sub>(s,·). The transition kernel *T* stitches those stage games into a Markov chain.&#x20;

3. **Information‑hiding composition**  
   POSG = (Stochastic game) ⨂ Observation channel, where each channel O<sub>i</sub> stochastically **filters** (s<sub>t</sub>, a<sub>t‑1</sub>) into a private signal o<sub>i,t</sub>.

Mathematically, define
    Pr(o<sub>t</sub>, s<sub>t</sub> | s<sub>t‑1</sub>, a<sub>t‑1</sub>) = *T*(s<sub>t‑1</sub>, a<sub>t‑1</sub>, s<sub>t</sub>) · ∏<sub>i</sub>O<sub>i</sub>(a<sub>t‑1</sub>, s<sub>t</sub>, o<sub>i,t</sub>)
which factorises the joint dynamics into **environment** × **observation channels**.&#x20;

---

### Key equations added at each step

| Level           | Central equation / constraint                                                          | Purpose                                           |                                                         |
| --------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------- |
| Normal‑form     | ∑<sub>a<sub>i</sub></sub> ω<sub>i</sub>(a<sub>i</sub>) = 1                             | Mixed strategy distribution.                      |                                                         |
| Repeated        | Return = ∑<sub>t</sub>γ⁽ᵗ⁾ R<sub>i</sub>(a<sub>t</sub>),   γ = 1 − p<sub>term</sub>    | Connects infinite repetition to RL discounting.   |                                                         |
| Stochastic game | ∑<sub>s′</sub>*T*(s,a,s′)=1   & Markov property Eq (3.3)                               | Valid transition kernel; memorylessness.          |                                                         |
| POSG            | **Observation normalisation** ∑<sub>o</sub>O<sub>i</sub>(a,s,o)=1                      | Ensures each O<sub>i</sub> is a conditional pmf.  |                                                         |
|                 | **Bayesian filter** b<sub>t+1</sub>(s′)=∑<sub>s</sub>b<sub>t</sub>(s)*T*(s,a,s′)\*O(o  |  a,s′)                                            | Belief‑state update for a single‑agent limit (Eq 3.5).  |

---

### Complexity growth by dimension counts

| Dimension                           | Normal‑form | Repeated | Stochastic | POSG          |               |     |   |       |
| ----------------------------------- | ----------- | -------- | ---------- | ------------- | ------------- | --- | - | ----- |
| Agents *n*                          | ✔︎          | ✔︎       | ✔︎         | ✔︎            |               |     |   |       |
| Time steps *T*                      | —           | ✔︎       | ✔︎         | ✔︎            |               |     |   |       |
| States                              | —           | —        |            | S             |               |     | S |       |
| Private observations                | —           | —        | —          | ∑<sub>i</sub> | O<sub>i</sub> |     |   |       |
| Joint history length used in policy | 0           | T        | T (        | S             |  + 1)         | T ( | O |  + 1) |

Thus each upward move along the hierarchy strictly **adds at least one new set** (S or O<sub>i</sub>) and/or enlarges the domain on which policies are defined, leading to exponential growth in the joint action–information space.

---

### Take‑aways for modelling & algorithm choice

* **Pick the lowest level that matches reality.**
  Hidden sensors → POSG; dynamic world but shared vision → Stochastic game; instantaneous incentives → Normal‑form.
* **Algorithms must respect the added structure.**

  * Minimax / self‑play assume the zero‑sum reward tag (orthogonal axis) at any level.
  * Value‑decomposition and factorised critics rely on the state *S* of stochastic games.
  * Belief filters or recurrent policies are unavoidable in POSGs because optimal actions are functions of information sets rather than states.

This mathematical ladder provides the blueprint for **composing** increasingly expressive game models while preserving the simpler ones as limiting cases.


---


### Why “simple” matrix games get hard fast

Even though a **normal‑form game** is defined by nothing more than a finite set of players, their pure‑action sets and a payoff table

$$
G =\bigl\langle I, \{A_i\}_{i\in I}, \{R_i : A\to\mathbb R\}_{i\in I}\bigr\rangle,
\qquad A=\prod_{i\in I}A_i ,
$$

several distinct sources of **complexity** arise the moment we try to *compute, predict, or learn* behaviour in the game.
Below is a structured tour of those sources, together with the best‑known complexity results.

---

## 1 Representational (input‑size) complexity

| Parameter              | Scaling law                             | Consequence                                                                                                                                              |           |      |   |                                                                                                                                                                                                                                             |
| ---------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---- | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of pure actions | (                                       | A                                                                                                                                                        | =\prod\_i | A\_i | ) | The payoff table grows **exponentially** in the number of players; storing it already becomes infeasible for modest \(n\) unless we adopt *succinct* encodings such as graphical, circuit or polymatrix games. ([people.seas.harvard.edu][1]) |
| Mixed strategies       | Continuous simplex \(\Delta(A_i)\)        | Optimisation problems involve real‑valued variables and constraints, not just combinatorial search.                                                      |           |      |   |                                                                                                                                                                                                                                             |
| Succinct encodings     | Pay‑offs computed by circuits or graphs | Eliminates the table blow‑up, **but** many decision questions become *coNP‑ or \(\#\)P‑hard* on these compact descriptions. ([people.seas.harvard.edu][1]) |           |      |   |                                                                                                                                                                                                                                             |

---

## 2 Computational complexity of key solution concepts

### 2.1 Nash equilibrium (NE)

| Variant of the problem                         | Formal statement                                                                  | Complexity status                                                                                                                             | Notes        |    |       |                                                                                               |
| ---------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -- | ----- | --------------------------------------------------------------------------------------------- |
| **Compute one NE** (general game, ≥ 2 players) | Output a mixed‑strategy profile \(\sigma\) with no profitable unilateral deviation. | **PPAD‑complete** for 2‑player and ≥ 3‑player games (no polynomial‑time algorithm is known unless PPAD = P). ([MIT CSAIL][2], [MIT CSAIL][3]) |              |    |       |                                                                                               |
| **Compute one NE, zero‑sum 2‑player**          | Same, but \(R_1=-R_2\).                                                             | **Polynomial time** via a pair of linear programmes (one primal, one dual). ([econweb.ucsd.edu][4])                                           |              |    |       |                                                                                               |
| **Verify** whether a given profile is an NE    | “Is NE?” decision problem.                                                        | **coNP‑complete** for succinct representations; polynomial for explicit tables (just test best responses). ([people.seas.harvard.edu][1])     |              |    |       |                                                                                               |
| **Count NE**                                   | Return                                                                            | NE                                                                                                                                            | or decide if | NE |  > k. | **\(\#\)P‑complete** even for two‑player symmetric games. ([people.cs.pitt.edu][5], [arXiv][6]) |

> **PPAD** (“Polynomial Parity Arguments on Directed graphs”) is a class of total search problems whose solutions are guaranteed by a parity argument; Nash equilibrium sits at its core. ([MIT CSAIL][2])

### 2.2 Correlated equilibrium (CE)

Because a CE is the optimum of a *linear* feasibility system,

$$
\sum_{a\in A} p(a)\bigl(R_i(a_i,a_{-i})-R_i(a'_i,a_{-i})\bigr)\ge 0\quad\forall i,a_i,a'_i,
$$

finding one reduces to linear programming and is thus solvable in polynomial time. ([NeurIPS Proceedings][7])
(Computing a **welfare‑optimal** CE is also polynomial, but the LP can be large.)

### 2.3 Approximate Nash equilibrium

| Guarantee                                             | Status                                                                                                   |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| \(\varepsilon\)=0.5 well‑supported NE in bimatrix games | Polynomial‑time LP‑based algorithms exist. ([epubs.siam.org][8])                                         |
| Any constant \(\varepsilon<\frac12\)                    | Quasi‑polynomial time and matching lower bounds; no fully‑polynomial scheme is known. ([ACM SIGecom][9]) |
| \(\varepsilon\)-NE in n‑player games                    | Requires \(2^{\Omega(n)}\) queries to pay‑offs in the oracle model. ([arXiv][10])                          |

---

## 3 Strategic complexity & multiplicity

* **Multiple equilibria**: Normal‑form games can harbour an exponential number of Nash equilibria, making *selection* or *prediction* difficult. Counting is \(\#\)P‑hard (above).
* **Equilibrium refinements** (trembling‑hand perfect, proper, etc.) add further fixed‑point constraints—no polynomial algorithms are known in general, and most decision problems are NP‑ or PSPACE‑hard in succinct representations. *Practical takeaway*: you seldom have the luxury of computing refined equilibria in large games.

---

## 4 Learning & dynamic‑process complexity

| Learning dynamic            | Convergence guarantee                                                                                              | Complexity issue                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| Best‑response dynamics      | Converges only in potential or zero‑sum games; may cycle otherwise.                                                | Detecting convergence is PSPACE‑hard.                         |
| No‑regret / fictitious play | Time‑average play converges to CE, **not** necessarily NE; number of steps can be exponential in \(1/\varepsilon\).  | Relates to hardness of approximating NE. ([MIT CSAIL][2])     |
| Replicator dynamics         | Continuous‑time ODE; may take exponential time to approach equilibrium and can get stuck at unstable fixed points. | Illustrates that even *analog* computation is not a shortcut. |

---

## 5 How structure tames complexity

| Structural restriction                                        | Effect on complexity                                                                                                  | Typical algorithms                           |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| 2‑player **zero‑sum**                                         | LP ⇒ polynomial.                                                                                                      | Simplex, interior‑point, primal‑dual.        |
| **Potential** or **congestion** games                         | Pure NE always exist; best‑response dynamics converges in finite steps, but number of steps can still be exponential. | Better‑response or steepest improvement.     |
| **Polymatrix** or **graphical** games with bounded tree‑width | Computing an NE becomes polynomial (DP along the graph).                                                              | Message‑passing or MILP using small cliques. |

---

## 6 Practical implications for modellers and engineers

1. **Storage first.** A raw payoff table is feasible only for a handful of agents; use graphical, factored or sampled representations otherwise.
2. **Choose the solution concept that fits the scale.** For large strategic‑form games, correlated (or coarse correlated) equilibria are often the only tractable targets.
3. **Exploit special structure ruthlessly.** Zero‑sum? → LP. Congestion? → potential‑based dynamics.
4. **Treat general Nash computation as intractable by default.** Unless PPAD collapses, you’ll rely on heuristics (regret minimisation, evolutionary search) whose runtime is empirical rather than worst‑case.
5. **Approximation has hard limits.** Even “just” a 0.1‑NE can inherit quasi‑polynomial or exponential lower bounds, so budget for that in runtime expectations.

---

### Cheat‑sheet of complexity results for normal‑form games

| Task                         | General game (explicit table)                        | 2‑player zero‑sum                        | \(k\)-player succinct game                                   |
| ---------------------------- | ---------------------------------------------------- | ---------------------------------------- | ---------------------------------------------------------- |
| Find one NE                  | **PPAD‑complete** ([MIT CSAIL][2])                   | **P** (LP) ([econweb.ucsd.edu][4])       | **PPAD‑complete** ([people.seas.harvard.edu][1])           |
| Verify NE                    | **P**                                                | **P**                                    | coNP‑ or coNP\(\#\)P‑complete ([people.seas.harvard.edu][1]) |
| Count NE                     | \(\#\)P‑complete ([people.cs.pitt.edu][5])             | \(\#\)P‑complete ([arXiv][6])              | \(\#\)P‑complete                                             |
| Compute CE                   | **P** (LP) ([NeurIPS Proceedings][7])                | **P**                                    | **P**                                                      |
| ε‑NE (\( \varepsilon\le 0.5\)) | Quasi‑poly / exp time lower bound ([ACM SIGecom][9]) | Poly‑time for ½‑NE ([epubs.siam.org][8]) | 2^{Ω(n)} queries needed ([arXiv][10])                      |

---

Normal‑form games look deceptively static, but underneath they are a rich minefield of hardness results.  Recognising *which* of the above complexities bites in your application is the first step toward selecting a workable representation, solution concept and algorithm.

[1]: https://people.seas.harvard.edu/~salil/research/nash-aug09.pdf?utm_source=chatgpt.com "[PDF] The Computational Complexity of Nash Equilibria in Concisely ..."
[2]: https://people.csail.mit.edu/costis/simplified.pdf?utm_source=chatgpt.com "[PDF] The Complexity of Computing a Nash Equilibrium"
[3]: https://people.csail.mit.edu/costis/journal_ver10.pdf?utm_source=chatgpt.com "[PDF] The Complexity of Computing a Nash Equilibrium"
[4]: https://econweb.ucsd.edu/~jsobel/172aw02/notes9.pdf?utm_source=chatgpt.com "[PDF] Linear Programming Notes IX: Two-Person Zero-Sum Game Theory"
[5]: https://people.cs.pitt.edu/~kirk/CS1699Fall2014/lect4.pdf?utm_source=chatgpt.com "[PDF] Lecture: Complexity of Finding a Nash Equilibrium"
[6]: https://arxiv.org/abs/1412.0969?utm_source=chatgpt.com "Settling Some Open Problems on 2-Player Symmetric Nash Equilibria"
[7]: https://proceedings.neurips.cc/paper/2020/file/e366d105cfd734677897aaccf51e97a3-Paper.pdf?utm_source=chatgpt.com "[PDF] Polynomial-Time Computation of Optimal Correlated Equilibria in ..."
[8]: https://epubs.siam.org/doi/10.1137/23M1549237?utm_source=chatgpt.com "A Polynomial-Time Algorithm for 1/2-Well-Supported Nash Equilibria ..."
[9]: https://sigecom.org/exchanges/volume_15/2/RUBINSTEIN.pdf?utm_source=chatgpt.com "[PDF] Settling the Complexity of Computing Approximate Two-Player Nash ..."
[10]: https://arxiv.org/abs/1606.04550?utm_source=chatgpt.com "Settling the complexity of computing approximate two-player Nash ..."


---


Below is a **focused “complexity map”** for **repeated normal‑form games** (RNGs)—i.e., a single stage game \(G=\langle I,\{A_i\},\{R_i\}\rangle\) played over a horizon
\(t=0,1,\dots\)—together with the best‑established results on why the model becomes hard the moment it is iterated.

> **Note on the chapter PDF** – the file you shared earlier has timed‑out on the server, so I cannot reopen it for verbatim quotations. The summary below therefore rests on the public literature; if you want precise excerpts from the book again, please re‑upload the PDF.

---

## 1 Representational explosion

| Dimension                    | One‑shot game           | Repeated for \(T\) rounds (finite)                                   | Repeated, \(T=\infty\) (discount \(\delta\)) |                 |                    |        |            |
| ---------------------------- | ----------------------- | ------------------------------------------------------------------ | ---------------------------------------- | --------------- | ------------------ | ------ | ---------- |
| Pure‑history space           | 1 joint action          | (                                                                  | A                                        | ^{T}) histories | countably infinite |        |            |
| Strategy space per player    | \(\Delta(A_i)\) (simplex) | functions \(h_t \mapsto a_{i,t}\) ⇒ **doubles exponentially** in \(T\) | **uncountable**                          |                 |                    |        |            |
| Storage need (explicit tree) | (\Theta(                | A                                                                  | ))                                       | (\Theta(        | A                  | ^{T})) | impossible |

Succinct encodings (graphical or circuit games) mitigate storage but trigger new hardness results (coNP‐ or \(\#\)P‑completeness for several decision tasks) .

---

## 2 Finite‑horizon games: “easy” and “hard” simultaneously

### 2.1 **Subgame‑perfect equilibrium (SPE) by backward induction**

*If the stage game has a **unique** Nash equilibrium*, backward induction gives the unique SPE in **\(O(T\cdot|A|)\)** time (lectures in MIT‑OCW) ([MIT OpenCourseWare][1]).

### 2.2 What makes the finite case hard

| Hard task                                                       | Complexity result                                                                                                           | Intuition                                                       |
| --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| *Does there exist* an SPE with average pay‑off ≥ \(\mathbf{v}\)?  | **NP‑hard** in general succinct games (folklore; reduction from Subset‑Sum).                                                | Incentive‑compatibility constraints couple all rounds.          |
| *Enumerate* all SPE outcome paths                               | Number of paths can grow **exponentially in \(T\)** (each history‑contingent threat choice branches).                         | Each punishment continuation is a game tree itself.             |
| *Compute minimal‑memory strategy* that attains a given SPE path | Requires solving a shortest‑path in an exponentially‑sized automaton space; **NP‑hard** (Rubinstein‑style automata models). | Balancing reward and memory creates a bi–criteria optimisation. |

---

## 3 Infinite‑horizon games: discounting, Folk Theorem & hardness

### 3.1 The Folk Theorem’s upside

For perfect monitoring and discount factor \(\delta\) near 1, **every** payoff vector that is
(i) feasible and (ii) individually‑rational can be supported by an SPE.
Classic constructive proofs (Abreu–Pearce–Stacchetti 1990) rely on “grim‑trigger” threat automata.

### 3.2 Computational downside

| Players                          | Task                                                                                                                                                                                                        | Complexity status                                                                                           |    |                                                                                   |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -- | --------------------------------------------------------------------------------- |
| 2                                | Find one (approx.) Nash equilibrium                                                                                                                                                                         | **Polynomial time** (Littman & Stone, 2005) – uses Folk Theorem to cut to a 2‑D linear feasibility problem. |    |                                                                                   |
| ≥ 3                              | Find any \(\varepsilon\)-NE (even (\varepsilon=1/                                                                                                                                                             | A                                                                                                           | )) | **PPAD‑complete**  – a reduction shows k‑player one‑shot ↔ (k+1)-player repeated. |
| Graphical games, constant degree | Still PPAD‑hard unless players are **computationally bounded**; with a polynomial‑time bound and standard crypto assumptions, Halpern‑Pass‑Seeman devise an efficient algorithm for a *computational* SPE . |                                                                                                             |    |                                                                                   |

Hence the Folk Theorem enlarges the equilibrium **set**, but does **not** make any particular equilibrium easier to locate once you have three or more strategic agents.

---

## 4 Strategy‑implementation (automata) complexity

* Measuring complexity by the **number of states** in a finite automaton that realises a strategy:

  * Tit‑for‑Tat needs 2 states, Grim Trigger 2, but certain payoff profiles require machines whose size grows **at least linearly in \(1/(1-\delta)\)**.
  * Rubinstein (1986) showed that players who minimise *both* average payoff loss and automaton size may be stuck with the classical Prisoner’s‑Dilemma outcome even when cooperation is supportable ([ScienceDirect][2]).

---

## 5 Learning & dynamic‐process complexity

| Learning dynamic                 | Converges in RNG?                                                                                                                                                     | Complexity insight                                                                                               |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| No‑regret (MWU, Hedge)           | Time‑average play → Correlated Equilibrium in zero‑sum 2‑player; **need not** reach NE in general‑sum or ≥ 3 player games.                                            | Myth‑of‑Folk‑Theorem paper proves any dynamics that yields an \(\varepsilon\)-NE would solve a PPAD‑hard problem . |
| Last‑iterate (stabilised regret) | Algorithms exist for **zero‑sum** RNGs (Dinh et al. 2021) but rely on strong convexity assumptions ([Proceedings of Machine Learning Research][3]).                   |                                                                                                                  |
| Independent Q‑learning           | PAC‑style sample complexity is exponential in horizon for general‑sum repeated games (hardness of independent learning in Markov games) ([sham.seas.harvard.edu][4]). |                                                                                                                  |

---

## 6 Algorithmic work‑arounds

* **Poly‑time constructive schemes** for two‑player repeated games with large action sets (Conitzer & Sandholm “Fast Equilibrium Computation…”) sidestep full enumeration via outcome‑sampling and curse‑of‑dimensionality heuristics ([CMU School of Computer Science][5]).
* **Set‐valued dynamic programming** (Abreu‑Sannikov; Goldlücke‑Kranz) approximate the entire equilibrium payoff frontier; runtime is polynomial in \(|A|\) but pseudo‑polynomial in \(1/(1-\delta)\) ([econtheory.org][6]).
* **Public‑signal decomposition** lets one compute Perfect‑Public‑Equilibrium payoffs via linear programmes when the monitoring structure is common‑knowledge and low‑dimensional ([arXiv][7]).

---

## 7 Practical take‑aways

1. **Finite horizon ⇒ backwards induction is your friend** *if* the stage game’s NE is unique.
2. **Infinite horizon, ≥ 3 players ⇒ treat exact equilibrium search as PPAD‑hard.** Use approximation or extra structure (zero‑sum, public monitoring, bounded rationality).
3. **Account for memory limits**: if agents or hardware must implement finite automata, many Folk‑Theorem payoffs disappear.
4. **Learning dynamics ≠ equilibrium computation**: no‑regret ensures at best correlated equilibria and becomes an impossibility proof for fast NE search in large RNGs.
5. **When possible, compress the game** (graphical / polymatrix) *and* exploit discount‑factor structure—otherwise the strategy space explodes exponentially.

These layers of complexity show why repeated normal‑form games, despite their deceptively simple definition, sit at the frontier of both theoretical hardness and practical algorithm design.

[1]: https://ocw.mit.edu/courses/14-12-economic-applications-of-game-theory-fall-2012/54f153ef7ed7800f367ce2b4021a18db_MIT14_12F12_chapter12.pdf "Session 12 Lecture Notes"
[2]: https://www.sciencedirect.com/science/article/pii/0022053186900219?utm_source=chatgpt.com "Finite automata play the repeated prisoner's dilemma - ScienceDirect"
[3]: https://proceedings.mlr.press/v132/dinh21a.html?utm_source=chatgpt.com "Last Round Convergence and No-Dynamic Regret in Asymmetric ..."
[4]: https://sham.seas.harvard.edu/sites/projects.iq.harvard.edu/files/kakade/files/hardness_of_independent_learning_and_sparse_equilibrium_computation_in_markov_games.pdf?utm_source=chatgpt.com "[PDF] Hardness of Independent Learning and Sparse Equilibrium ..."
[5]: https://www.cs.cmu.edu/~conitzer/fastAAAI13.pdf?utm_source=chatgpt.com "[PDF] Fast Equilibrium Computation for Infinitely Repeated Games"
[6]: https://econtheory.org/ojs/index.php/te/article/viewFile/20140313/10807/322?utm_source=chatgpt.com "[PDF] An algorithm for two-player repeated games with perfect monitoring"
[7]: https://arxiv.org/html/2411.01566v1?utm_source=chatgpt.com "An algorithm for two-player repeated games with imperfect public ..."


---



Below is a **solution‑concept–free** examination of the two foundations in the hierarchy: **normal‑form games** (one‑shot matrix games) and their **repeated** versions.
The emphasis is strictly on the *modelling* and *computational* burdens that arise **before** any notion of “optimal play,” “best response,” or “equilibrium” is introduced.

---

## 1 Normal‑Form (Strategic) Games ─ inherent complexities

| Aspect                                      | Where the difficulty comes from                                                                                                                                                                                                             | Practical consequences                                                                                                                                                            |                                                                                                                |                                                                                                                                                                        |                                                                    |      |         |                                                                                                                                                                                                                                           |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pay‑off table size**                      | A profile is a Cartesian product \(A=\prod_{i=1}^{n}A_i\).  The number of rows in the table is (                                                                                                                                              | A                                                                                                                                                                                 | = \prod\_i                                                                                                     | A\_i                                                                                                                                                                   | ), which is *exponential in the number of players* whenever each ( | A\_i | \ge 2). | Storing or even reading the full table becomes infeasible for modest \(n\).  Designers adopt *succinct representations* (graphical, polymatrix, circuit, continuous utilities) at the cost of losing the simple rectangular data structure. |
| **Action‑space heterogeneity**              | Players may have different numbers or types of actions (discrete, continuous, parameterised).                                                                                                                                               | A uniform tabular layout no longer suffices; one must transform continuous choices into discretised grids or analytic payoff functions.                                           |                                                                                                                |                                                                                                                                                                        |                                                                    |      |         |                                                                                                                                                                                                                                           |
| **Mixed and behavioural strategies**        | Even before talking about “optimal” behaviour, the mere *set* of probabilistic strategies is a simplex in (\mathbb R^{                                                                                                                      | A\_i                                                                                                                                                                              | }) (or an infinite‑dimensional object if \(A_i\) is continuous).                                                 | Any downstream computation—e.g., sampling random behaviour for simulation—must handle floating‑point probability vectors and, potentially, numerical stability issues. |                                                                    |      |         |                                                                                                                                                                                                                                           |
| **Reward‑structure tagging**                | Zero‑sum, common‑reward, and general‑sum labels are defined **at this level**.  They do not create algorithmic hardness per se, but they *fork* all subsequent modelling paths (e.g., how you log performance or allocate rewards in code). | Every simulation or data pipeline must carry the tag so that later modules (learning, evaluation, visualisation) can interpret payoffs correctly.                                 |                                                                                                                |                                                                                                                                                                        |                                                                    |      |         |                                                                                                                                                                                                                                           |
| **Preference encoding vs. numeric payoffs** | In many domains only ordinal preferences (rankings) are known, not cardinal utilities.  Converting those into numeric payoffs is non‑trivial and can bias later analysis.                                                                   | Modellers must decide on scaling, normalisation and tie‑breaking conventions **before** any solution concept enters.                                                              |                                                                                                                |                                                                                                                                                                        |                                                                    |      |         |                                                                                                                                                                                                                                           |
| **Data consistency & validation**           | A payoff array provided by domain experts or scraped from logs can be inconsistent (e.g., illegal actions, missing entries).                                                                                                                | Without validated, complete data, *no* theoretical or empirical study—equilibrium‑based or otherwise—can proceed.  Automated checks and domain‑specific constraints are required. |                                                                                                                |                                                                                                                                                                        |                                                                    |      |         |                                                                                                                                                                                                                                           |
| **Sampling / simulation support**           | Many empirical studies rely on Monte‑Carlo roll‑outs of random profiles.  Enumerating (                                                                                                                                                     | A                                                                                                                                                                                 | ) grows exponentially; drawing uniform samples becomes hard to implement correctly for unbalanced action sets. | Efficient combinatorial enumeration or rejection‑sampling libraries become part of the basic tooling, independent of how “optimal” play will later be defined.         |                                                                    |      |         |                                                                                                                                                                                                                                           |

---

## 2 Repeated Normal‑Form Games ─ complexities added by iteration

A repeated game is specified by:

* the stage game \(G=\langle I,\{A_i\},\{R_i\}\rangle\);
* a horizon \(T\in\mathbb N\cup\{\infty\}\) or a termination rule (e.g., geometric \(p_\text{stop}\));
* an aggregation rule for per‑round rewards (sum, average, discounted sum).

### 2.1 Explosion of the underlying game tree

* **Joint‑action histories**: after \(t\) rounds there are \(|A|^t\) distinct paths.
* **Explicit extensive‑form** representation therefore needs \(\Theta\left(\sum_{k=0}^{T-1}|A|^{k}\right)\) nodes—exponential in \(T\).
* Memory and disk usage grow prohibitively quickly; any simulator that logs complete histories must implement pruning, compression, or on‑the‑fly roll‑outs.

### 2.2 Strategy‑space size before optimisation

A *pure* strategy for player \(i\) is a deterministic function

$$
\pi_i:\mathcal H_t \to A_i, \quad 
\mathcal H_t = \bigl(A\bigr)^{t}
$$

where \(\mathcal H_t\) is the set of length‑\(t\) joint histories. Even for modest horizons this means:

* \(\bigl| \text{PureStrategies}_i \bigr| = |A_i|^{|A|^{T}}\) *(double‑exponential)*.
* Mixed strategies would be probability distributions over this already enormous set.

Hence, **long before** introducing equilibria, the very *act of naming* an arbitrary strategy becomes impossible without some compact description (state machines, parameterised policies, decision trees, neural networks, etc.).

### 2.3 Memory and implementability constraints

If strategies are executed by finite automata:

* The number of automaton states needed to represent arbitrary history‑dependent behaviour grows at least linearly in the size of the observed history set; for infinite‑horizon discounted games it can be unbounded.
* Physical agents (robots, edge devices) often impose hard RAM limits, forcing the modeller to exclude entire swaths of the abstract strategy space **a priori**.

### 2.4 Monitoring and data‑logging complexity

The repeated framework is agnostic to *how* players learn what happened in previous rounds.  Two orthogonal modelling choices have big technical consequences:

| Monitoring assumption                                                     | Data the modeller must track                                 | Implementation burden                                                          |
| ------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| **Perfect public monitoring** (everyone observes the exact joint action)  | Single shared log of actions; same for all players           | Simple, but log still \(\Theta(T)\) long.                                        |
| **Imperfect or private monitoring** (noisy, player‑specific observations) | Separate observation histories \(o_{i,0:T-1}\) for each player | Multiplicative storage; one must define observation channels and random seeds. |

Importantly, these logging mechanisms are required purely to **specify** what information players *could* condition on later, without regard to equilibria.

### 2.5 Time‑aggregation rules

Whether stage rewards are **summed**, **averaged**, or **discounted** affects:

* Numeric range and scaling (risk of overflow in long horizons).
* Alignment with empirical data (e.g., discounting matches human time preference).
* Compatibility with downstream learning algorithms (some require non‑negative returns).

Yet all of these considerations arise before we ask “what is an optimal policy?”—they are necessary just to compute well‑defined payoffs for *any* pair of fixed strategies.

### 2.6 Simulation runtime vs. horizon length

Running \(M\) roll‑outs of length \(T\) with \(n\) players and per‑step logging cost \(c\):

$$
\text{CPU time} = O(M \cdot T \cdot c),\qquad
\text{RAM} = O(T \cdot \text{log‐size}),\quad
\text{Disk} = O(M \cdot T).
$$

When \(T\) is large or unbounded, faithfully simulating every round may not be viable; approximate, event‑driven or batch‑update simulators are needed.

---

## 3 Key modelling lessons (before any solution concept appears)

| Lesson                                                                                                                                                                                                                       | Rationale |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **Budget storage first.**  Decide how payoffs, histories and observation traces will be stored or generated on‑demand before you pick an algorithm.                                                                          |           |
| **Adopt compact encodings early.**  Graphical or factored payoff models, parameterised policies, and log compression do not depend on equilibria—they are prerequisites for *any* non‑trivial study.                         |           |
| **Separate information structure from behaviour.**  Precisely specifying what each player perceives in each round is essential groundwork; the “best response” question can only be asked *after* that scaffold is in place. |           |
| **Think about implementability.**  If strategies must run on real hardware or finite‑state controller pools, bake those memory limits into the model; otherwise later solution‑concept work may be moot in practice.         |           |
| **Clarify time aggregation.**  Summed, average and discounted returns can produce orders‑of‑magnitude differences in numeric scale and variance, affecting every metric collected later on.                                  |           |

---

### Summary

* A **normal‑form game** already carries exponential‐size data structures and continuous strategic choices, demanding careful representation and data‑validation **before** any consideration of rationality.
* **Repeating** that stage game multiplies the modelling load: the history tree explodes exponentially, strategies become uncountably many objects, and logging, memory and runtime constraints dominate engineering decisions.
* All these complexities are intrinsic to the **definition and simulation** of the games themselves; they arise even if you never ask what “optimal play” looks like.  Solution concepts will layer on *top* of this groundwork, not replace it.



---



### What “complexity” means in the hierarchy of game models

When the book (and my earlier summaries) speak of *increasing complexity*, the term is **not a single‑number score**.
Instead it is a short‑hand for **how many distinct modelling burdens a designer must shoulder** in order to specify the game *before* any solution concept is considered.
Four independent burdens matter:

| Dimension of burden                               | “How big is it?” proxy                                                                                                                                                   | Why it matters at the modelling stage                                                         |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Structural** (what sets must be declared)       | Number and type of elements in the formal tuple: agents I, actions Aᵢ, state S, observation sets Oᵢ, transition T, observation kernels Oᵢ(·), etc.                       | Each extra set forces you to gather more domain knowledge and encode more data.               |
| **Descriptive** (storage size)                    | Bits needed to list pay‑offs, kernels, observation matrices, etc.  For finite games this is proportional to the product of the cardinalities of all sets just mentioned. | Determines RAM/disk requirements and whether a tabular description is even possible.          |
| **Information‑theoretic** (what each agent knows) | Size and richness of the history each agent may condition on (joint‑action history, state history, private‑observation history).                                         | Controls how large a policy representation must be, even if you never ask for “optimal” ones. |
| **Computational scaffolding** (simulation effort) | Cost to draw one trajectory of length T (sampling next state, sampling observations, logging), or to enumerate all histories if you need an exhaustive tree.             | Affects runtime of empirical studies, Monte‑Carlo evaluations, data generation for learning.  |

A model is *higher* in the hierarchy precisely because it **strictly adds at least one new burden** to *all* four columns above.

---

### How the standard hierarchy is ranked

| Rank  | Model                                           | New element(s) introduced<br>(relative to the previous row) | Consequences for each burden                                                                                                                                       |      |                             |
| ----- | ----------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- | --------------------------- |
| **0** | **MDP** (single agent)                          | • agent count fixed to 1                                    | Baseline reference.                                                                                                                                                |      |                             |
| **1** | **Normal‑form game**                            | • multiple agents *I*                                       | Descriptive size multiplies by (\prod\_i                                                                                                                           | A\_i | ).                          |
| **2** | **Repeated normal‑form game**                   | • discrete time<br>• joint‑action history                   | Information sets explode: (                                                                                                                                        | A    | ^t) histories at depth \(t\). |
| **3** | **Stochastic game** (a.k.a. Markov game)        | • explicit environment state *S*<br>• transition kernel *T* | Every pay‑off row now indexed by *state* as well as *joint action*.  Simulation must sample *T*.                                                                   |      |                             |
| **4** | **Partially Observable Stochastic Game** (POSG) | • private observation sets Oᵢ<br>• observation kernels Oᵢ   | Descriptive size adds the observation matrices; information sets for policies become each player’s private observation history, giving the largest strategy space. |      |                             |

```
Normal‑form  →  +time  →  Repeated  →  +state  →  Stochastic  →  +hidden state  →  POSG
```

Each arrow means that **you cannot write down the model on the right unless you have already written down everything on the left *and* something new**.

---

#### Quantitative illustration (finite games)

Let

* \(n = |I|\) players
* \(m = \max_i |A_i|\) max pure actions per player
* \(|S|\) number of states
* \(|O|\) max observations per player

| Model       | Minimal description length (big‑O, bits) | Number of possible length‑\(T\) histories seen by one agent |           |   |                                 |    |   |                    |
| ----------- | ---------------------------------------- | --------------------------------------------------------- | --------- | - | ------------------------------- | -- | - | ------------------ |
| Normal‑form | \(O(m^{n})\)                             | 1                                                         |           |   |                                 |    |   |                    |
| Repeated    | \(O(m^{n})\) (for stage game)            | \(m^{nT}\)                                                  |           |   |                                 |    |   |                    |
| Stochastic  | (O(                                      | S                                                         | ;m^{,n} + | S | ^2 m^{,n})) (pay‑offs + kernel) | (( | S | ,m^{,n})^{T})      |
| POSG        | previous row + (O(n,                     | S                                                         | ,         | O | ,m^{,n})) (obs. tables)         | (( | O | )^{nT}) per player |

The growth is **multiplicative** at every step; that is the formal sense in which each level is “more complex.”

---

### Why “complexity” is defined this way **before** solution concepts

1. **Expressiveness first** – If a phenomenon (e.g., hidden information) *cannot* be expressed in the simpler model, no equilibrium or learning rule built for that model can ever be appropriate.
2. **Resource budgeting** – Storage, runtime and logging requirements are fixed by the model’s ingredients, regardless of whether you later seek optimal play, simulate random play or fit behavioural data.
3. **Separation of concerns** – By isolating *descriptive complexity* we can later study how hard it is to compute equilibria *conditional on* that description.  The ranking is therefore solution‑concept agnostic.

---

#### What the ranking is **not**

* It is **not** an ordering of *difficulty of finding equilibria*.  (Two‑player zero‑sum normal‑form games are easy to solve; three‑player POSGs can be easier under special monitoring.)
* It is **not** an ordering of *field importance* or *practical relevance*.  Many real‑world problems are adequately captured by repeated or stochastic games and need not climb to POSGs.

---

### Take‑away

\*“Higher complexity” means **more ingredients to specify, more data to store, larger information sets per agent, and longer simulation runtimes**—before any rational‑choice or learning machinery is invoked.
The hierarchy is ranked by the minimal additional ingredient(s) you must add to capture new phenomena, making the chain **additive in modelling burdens** and therefore a clean yard‑stick for comparing game models.


---



Below is a **solution‑concept–free** look at the burdens you face as soon as you move from a repeated matrix game to a **stochastic game (a.k.a. Markov game)**.
Everything here concerns *specifying, storing, simulating or gathering data* for the model—nothing about how agents should “play well” once the model exists.

---

## 1  Formal ingredients you must now supply

| New ingredient in the tuple                   | What it is                                                                                  | Why it complicates life                                                                                                                                    |                                         |      |      |                                                                                                                  |                                                                                                |   |        |    |                                                 |
| --------------------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---- | ---- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | - | ------ | -- | ----------------------------------------------- |
| **Environment state set *S***                 | A finite or continuous set that summarises everything relevant about the world at time *t*. | You must design a state representation with enough detail to matter, but small enough to fit in memory—and document a coding for every tool in your stack. |                                         |      |      |                                                                                                                  |                                                                                                |   |        |    |                                                 |
| \*\*Transition kernel \*T(s′                  |  s,a)\*\*                                                                                   | For every joint action *a* and current state *s*, a probability distribution over next states *s′*.                                                        | Even with finite sets the table size is | S    | ² ×  | A                                                                                                                | , which grows at least quadratically in state count and exponentially in player count (because | A |  = ∏₁ⁿ | Aᵢ | ).  Tabular storage quickly becomes unworkable. |
| **State‑indexed reward functions Rᵢ(s,a,s′)** | One table (or function) per agent giving the immediate payoff of the transition (s,a,s′).   | Adds another                                                                                                                                               | S                                       | ² ×  | A    | numeric array per agent.  If rewards depend only on (s,a) or (s′) you must prove and code those simplifications. |                                                                                                |   |        |    |                                                 |
| **Initial‑state distribution µ(s)**           | Probability distribution over starting states.                                              | Must be estimated, engineered or sampled; affects reproducibility of every experiment.                                                                     |                                         |      |      |                                                                                                                  |                                                                                                |   |        |    |                                                 |

All previous ingredients—agent set *I* and per‑player action sets *Aᵢ*—carry over unchanged.

---

## 2  Descriptive (storage) complexity

| Parameter      | Table storage if kept explicit |   |      |   |          |   |                      |   |     |   |      |   |          |
| -------------- | ------------------------------ | - | ---- | - | -------- | - | -------------------- | - | --- | - | ---- | - | -------- |
| **Transition** | O(                             | S | ² ·  | A | ) floats |   |                      |   |     |   |      |   |          |
| **Rewards**    | O(                             | I |  ·   | S |  ·       | A | ) to O(              | I |  ·  | S | ² ·  | A | ) floats |
| **Total bits** | Θ(                             | S | ² ·  | A |  · (1+   | I | )) in the worst case |   |     |   |      |   |          |

Hence:

* With 3 players each having 10 actions (|A| = 10³ = 1000) and |S| = 1000, the transition table alone is 1 billion floats ≈ 4 GB in 32‑bit storage.
* Designers almost always turn to **compressed or parametric representations**—factored state variables, graphical models, neural networks, or procedural simulators that compute T on demand.

---

## 3  Sampling & simulation complexity

| Stage                              | Cost driver                                                                                                                                                        | Practical issue                                                                                                                                     |   |                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | - | ----------------------------------------------------------------------- |
| **Single step**                    |  • sampling one *s′* \~ T(s,a)                                                                                                                                     |                                                                                                                                                     |   |                                                                         |
|  • evaluating Rᵢ(s,a,s′)           | If *T* is non‑trivial (e.g., involves physics or black‑box code) a single step can take milliseconds to minutes, setting the wall‑clock for any Monte‑Carlo study. |                                                                                                                                                     |   |                                                                         |
| **Episode rollout** (length *T*)   | O(T · c\_step) CPU; O(T) log size                                                                                                                                  | Long‑horizon games blow up runtime and disk if you log every state and action.  Requires event‑driven logs, checkpointing or on‑the‑fly statistics. |   |                                                                         |
| **Batch experiments** (M episodes) | O(M · T · c\_step)                                                                                                                                                 | Parallelisation bumps into GPU/CPU memory if *T* and                                                                                                | S | are large; careful seed management needed for statistical independence. |

Even before asking whether behaviour is “good,” you must decide *how many* trajectories you can afford just to observe what the model does.

---

## 4  State‑space design and explosion

1. **Granularity tension**
   *Too fine*: |S| explodes, killing tables and slowing simulators.
   *Too coarse*: important distinctions vanish, making later analysis (including equilibrium notions, learning, etc.) impossible.

2. **Continuous state variables**
   When *S* is ℝᵏ (e.g., positions, velocities), *T* becomes a probability density, not a table.

   * Consequence: you now need analytic expressions, numerical solvers or black‑box simulators—none of which fit into simple data pipelines.

3. **Hybrid, factored or hierarchical states**
   *S* often mixes discrete mode variables with continuous physical variables.  Documentation and code must keep them synchronised and version‑controlled.

---

## 5  Non‑stationarity from each agent’s perspective

Because *T* depends on the **joint** action, the environment dynamics are *non‑stationary for every single agent taken in isolation*.
Even if you never speak of “optimality,” this implies:

* **Data‑collection protocols** (e.g., log random play) must record the *entire* joint action at each step, otherwise the empirical transition frequencies are uninterpretable.
* **Simulators** must run *all* agents’ action‑selection code synchronously; you cannot substitute sampled “environment noise” without bias.

---

## 6  Unknown‑model settings (learning the game itself)

Frequently the modeller does **not** know *T* or *Rᵢ*.  Then, **before** thinking about rational behaviour, you confront:

| Task                 | Sample‑complexity driver                                                                                  | Tooling needed                                                                                                                                            |
| -------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Model estimation** | Number of (s,a) pairs to cover × variance of *T*                                                          | Exploratory policy library, statistical estimators, confidence‑interval code.                                                                             |
| **Identifiability**  | Some state transitions may be unobservable because other agents never pick certain actions in early data. | Experimental design or randomised control policies built *just to see what can happen*.                                                                   |
| **Storage of data**  | Each transition sample is (s,a,r,s′)                                                                      | For high‑speed simulators, data pipes must sustain millions of events / second; for real‑world robotics, logging hardware must be rugged and timestamped. |

All of these chores arise independently of any later optimisation goal.

---

## 7  Time‑aggregation and reward‑scaling issues

Whether you plan to **sum**, **average**, or **discount** stage rewards, you must:

1. **Fix numeric types** (double vs. float vs. fixed‑point) so cumulative returns don’t overflow or underflow.
2. **Synchronise conventions** across multiple agents; otherwise you cannot compare or visualise trajectories coherently.
3. **Ensure cross‑platform reproducibility**—random seeds plus floating‑point determinism are tricky when *T* calls external physics engines.

---

## 8  Debugging, validation and reproducibility

Stochastic games embed randomness at two levels:

1. **Action sampling** (each agent’s behaviour generator)
2. **State transition sampling** (the environment kernel)

This introduces failure modes **not present in deterministic models**:

* **Flaky tests** – identical code paths can yield different logs; you need statistical validation rather than single‑run assertions.
* **Heisenbugs** – bugs that appear only under rare action combinations; systematic stress‑testing tools (e.g., adversarial action fuzzers) become part of the infrastructure.
* **Version skew** – even minor changes in *S* encoding or reward scaling invalidate stored datasets, requiring schema versioning.

---

## 9  Memory‑limited or embedded deployments

When a stochastic game is implemented on actual robots or edge devices:

* **On‑board RAM** may be too small to store a full state; you need lossy encoding or off‑board state trackers.
* **Real‑time constraints** impose hard deadlines on the *T* sampling function—physical actuators cannot wait for a slow physics kernel.

These engineering constraints must be reconciled *before* any behavioural theory is layered on.

---

## 10  Key modelling take‑aways

1. **Schema before strategy.** Write a precise data schema for (state, joint action, reward, next state) tuples; everything else builds on that.
2. **Compress early.** Unless |S| is tiny, plan for factored states, generative simulators or neural surrogates from day one—plain tables do not scale.
3. **Budget simulation time.** In research prototypes, the *environment step* often dominates wall‑clock; profile it and cache what you can.
4. **Version‑control your random seeds and kernels.** Stochasticity plus collaborative development is a recipe for irreproducible results unless rigorously controlled.
5. **Distinguish unknown vs. known models.** If *T* and *Rᵢ* are to be learned from data, allocate sample budgets and logging formats *before* any optimisation loop is even written.

---

### Summary

A **stochastic game** piles four big modelling burdens on top of a repeated matrix game:

1. **You must invent and encode a state space *S***.
2. **You must specify or learn a transition kernel *T***—an object whose size explodes with both state and joint‑action sets.
3. **You must store and sample from much larger data structures**, or build compressed/generative surrogates.
4. **You must run, log and validate probabilistic simulations** that are now non‑stationary from each agent’s point of view.

All of this complexity is present **before** you ever ask what constitutes “good play.”  Handling it well is the foundation on which any subsequent analysis—equilibrium, learning or otherwise—must stand.


---



Below is a **model‑centric comparison** of the two frameworks that sit at the top of the hierarchy introduced in Chapter 3:

|                                      | **Partially Observable MDP (POMDP)**                                                                | **Partially Observable Stochastic Game (POSG)**                                                                                                                                                                |                                                                    |                                                                                                                                                                                                                                                                                                             |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| ------------------------------------ | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | - | --- | - | --- | - | --- | - | ---- | - | ---------- | ---------------- | - | ----- | -- | ------------------ | - | ----- | -- | ------------------------------------------------------------- |
| **Purpose**                          | Single‑agent sequential decision‑making under state uncertainty.                                    | Multi‑agent extension of a POMDP—captures strategic interactions when each agent sees only a private signal.                                                                                                   |                                                                    |                                                                                                                                                                                                                                                                                                             |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| **Formal tuple**<br>(finite case)    | ⟨ *S*, *A*, *T*, *R*, Ω, *O*, µ ⟩                                                                   | ⟨ *I*, *S*, {Aᵢ}, *T*, {Rᵢ}, {Ωᵢ}, {Oᵢ}, µ ⟩                                                                                                                                                                   |                                                                    |                                                                                                                                                                                                                                                                                                             |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| **Key sets**                         | *S*—hidden environment state<br>*A*—agent’s actions<br>Ω—observation alphabet                       | Same *S* plus:<br>*I*—multiple agents<br>{Aᵢ}—action set per agent<br>{Ωᵢ}—private observation alphabets                                                                                                       |                                                                    |                                                                                                                                                                                                                                                                                                             |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| **Transition kernel**                | \*T(s′                                                                                              |  s,a)\*                                                                                                                                                                                                        | Same functional form but joint‑action input: \*T(s′                |  s,a¹,…,aⁿ)\*.                                                                                                                                                                                                                                                                                              |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| **Observation model**                | \*O(o                                                                                               |  s′,a)\*—probability of observing *o* after taking *a* and landing in *s′*.                                                                                                                                    | One kernel per agent: \*Oᵢ(oᵢ                                      |  s′,a¹,…,aⁿ)\*.  Signals can be correlated but need not be identical.                                                                                                                                                                                                                                       |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| **Reward specification**             | Scalar reward *R(s,a,s′)* to the lone agent.                                                        | Vector of rewards {Rᵢ(s, a¹,…,aⁿ, s′)}—each agent can value outcomes differently (general‑sum case).                                                                                                           |                                                                    |                                                                                                                                                                                                                                                                                                             |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| **Policy domain**                    | Maps **private observation history** to actions:<br>π\_t : (o₀,a₀,…,o\_{t−1},a\_{t−1},o\_t) ↦ a\_t. | Each agent has its own mapping; additionally, an agent’s optimal action may depend on *beliefs about other agents’ policies*, making the effective policy domain much larger.                                  |                                                                    |                                                                                                                                                                                                                                                                                                             |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| **Belief representation**            | A probability distribution over *S* (                                                               | S                                                                                                                                                                                                              | ‑dimensional simplex).  Update via Bayes filter using *T* and *O*. | No single sufficient statistic is known in general.  Each agent could maintain a distribution over *(state, other agents’ private histories or policies)*—an **infinite‑dimensional object** in principle.  Practical systems approximate with RNNs, factorised beliefs, interactive particle filters, etc. |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| **Stationarity from an agent’s eye** | Environment dynamics are **Markovian and stationary** once the agent’s action is fixed.             | Dynamics appear **non‑stationary** to any single agent because state transitions depend on *other agents’ evolving actions*.  This complicates data collection and model learning even before strategy enters. |                                                                    |                                                                                                                                                                                                                                                                                                             |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |
| **Descriptive size (tabular)**       | O(                                                                                                  | S                                                                                                                                                                                                              | ² ·                                                                | A                                                                                                                                                                                                                                                                                                           |  +  | S |  ·  | A |  ·  | Ω |  +  | S | ² ·  | A | ) numbers. | Adds a factor of | A |  = ∏ᵢ | Aᵢ | everywhere **and** | Ω |  = ∏ᵢ | Ωᵢ | for observation tables → multiplicative explosion in players. |
| **Special cases / reductions**       | —                                                                                                   | • If                                                                                                                                                                                                           | I                                                                  |  = 1, a POSG is exactly a POMDP. <br>• If each Oᵢ reveals (s′,a) perfectly, the POSG collapses to a fully observable stochastic game.                                                                                                                                                                       |     |   |     |   |     |   |     |   |      |   |            |                  |   |       |    |                    |   |       |    |                                                               |

---

## Why the additional agents create qualitatively new burdens

1. **Joint‑action input everywhere**
   Every probability table that was indexed by *a* in a POMDP is now indexed by the *joint* action (a¹,…,aⁿ).  Storage blows up exponentially with player count, and a simulator must synchronise all agents’ action calls each step.

2. **Information asymmetry**
   Because observations are *private*, the global system is no longer *common‑knowledge*.  When logging data or designing experiments you must record **who saw what when**; otherwise you cannot later reconstruct valid input to any agent’s policy.

3. **Belief nesting problem**
   In a POMDP the Bayes filter returns a belief over hidden state.
   In a POSG, an agent who wants to predict the future must reason about
   *state* + *other agents’ beliefs* + *other agents’ beliefs about its own beliefs*, etc.  Even without invoking “optimality,” writing down such interactive beliefs is an infinite regress; all practical codes truncate or approximate.

4. **Non‑stationary data‑collection**
   When you treat the other agents as part of the “environment,” the transition law appears to change as their behaviour changes (learning, exploration, fatigue).  Any statistical estimate of *T* from off‑policy data must therefore include the joint action in the conditioning set, or else be biased.

5. **Reward heterogeneity channel**
   The multi‑reward vector means that a single experience tuple (s,a,r,s′) in a data set now contains *n* reward numbers.  Downstream logging, visualisation, and evaluation tools must track them separately even before anyone decides what counts as success.

---

## Concrete example

| Scenario         | POMDP framing                                                                                           | POSG framing                                                                                                                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Drone in fog** | Single drone navigates with noisy lidar.  Hidden state = true (x,y,z).  Observation = noisy range scan. | Two drones share airspace but each has its own noisy lidar and chooses velocity vector.  Transition of altitude depends on **both** drones’ thrust actions; each sees only its own sensor readings.                       |
| **Implication**  | Designer specifies *T* over positions conditioned on *one* action.  Belief = 3‑D Gaussian.              | Designer specifies *T* over 6‑D joint positions conditioned on *two* actions.  Each drone’s belief must (at minimum) estimate the other drone’s position **and** guess its next velocity command to propagate the filter. |

---

## Modelling checklist for POSGs (add‑ons relative to POMDPs)

1. **Enumerate agents** and tag every action, observation and reward entry with an agent index.
2. **Define joint‑action interface** that your simulator accepts (array, dict, message bus).
3. **Specify observation‑sharing rules** (private, broadcast, delayed, lossy).  These rules are part of the model, not an implementation detail.
4. **Design logging schema**: (time, state, a¹,…,aⁿ, o¹,…,oⁿ, r¹,…,rⁿ).  Without this full tuple you cannot replay or debug.
5. **Plan for belief approximation**: decide early whether you will maintain factored beliefs, particle filters, or recurrent embeddings, because exact recursive belief update is impossible in the general POSG.

---

### Take‑away

A **POMDP** is a *one‑agent* hidden‑state control problem whose uncertainty can be summarised by a single Bayesian belief over the environment state.
A **POSG** generalises this to *multiple agents*, forcing every data structure—transition kernel, observation model, reward table, history log, belief—to scale with the **joint** action and **private** information of **all** players.
This multiplication of sets and the emergence of interactive uncertainty are what make the POSG strictly more complex, even before any discussion of rational decision making or equilibrium arises.



---



### Complexity audit for **Partially Observable Stochastic Games (POSGs)**

*(everything here concerns creating, storing, simulating, or measuring the model **before** any notion of “optimal play,” “equilibrium,” or “strategy quality” is introduced)*

---

## 1  Ingredients you must supply

| New since POMDP or fully‑observable SG | What it is                                 | Why it already adds complexity                                                             |                                                                           |                                               |
| -------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- | --------------------------------------------- |
| **Agent set *I*** (                    | I                                          |  > 1)                                                                                      | Distinct decision‑makers.                                                 | All data structures now carry an agent index. |
| **Joint‑action space *A* = ΠᵢAᵢ**      | Cartesian product of individuals’ actions. | Size grows multiplicatively with each new player.                                          |                                                                           |                                               |
| **Private observation alphabets Ωᵢ**   | Signals visible only to agent *i*.         | Requires separate observation tables; storage grows with ∏ᵢ                                | Ωᵢ                                                                        | .                                             |
| \*\*Observation kernels Oᵢ(oᵢ          |  s′,a)\*\*                                 | Probability that agent *i* receives observation *oᵢ* after joint action *a* lands in *s′*. | One conditional distribution per agent per state–action pair—huge tensor. |                                               |
| **Reward vectors Rᵢ(s,a,s′)**          | Immediate payoff for every agent.          | Logging must track                                                                         | I                                                                         | reward numbers per step.                      |

All elements from a stochastic game (*S*, *T*, µ, etc.) remain and multiply in size because their indices now include joint actions.

---

## 2  Descriptive (storage) blow‑up

Let

* *n* = |I| agents
* *m* = max\_i |Aᵢ| actions per agent
* |S| states
* |Ω| = max\_i |Ωᵢ| observations

| Table                          | Size if stored explicitly |   |          |   |   |
| ------------------------------ | ------------------------- | - | -------- | - | - |
| Transition **T**               | O(                        | S | ² · mⁿ)  |   |   |
| Each observation kernel **Oᵢ** | O(                        | S |  · mⁿ ·  | Ω | ) |
| All observation kernels        | O(n ·                     | S |  · mⁿ ·  | Ω | ) |
| Reward tensors                 | O(n ·                     | S | ² · mⁿ)  |   |   |

**Exponential** in player count and **quadratic** in state count: in practice you must switch to factored, sparse, procedural, or neural representations.

---

## 3  Explosion of information histories

* **Joint‑action history length t** ⇒ |A|ᵗ = (mⁿ)ᵗ possibilities.
* **Private observation histories**: each agent sees (oᵢ₀,…,oᵢₜ); joint space size = ∏ᵢ|Ωᵢ|ᵗ.
* Simulators and loggers that keep raw histories incur **multiplicative storage per agent**; compression or on‑the‑fly summarisation is unavoidable.

---

## 4  Belief representation becomes interactive

### Single‑agent (POMDP) baseline

Belief = probability vector over *S* (|S|‑dimensional simplex).

### POSG add‑ons

An agent who wishes to model future uncertainty must—in principle—track a distribution over

$$
(s,\text{other agents’ private histories})\quad\text{or}\quad
(s,\text{other agents’ policies}).
$$

This object is **infinite‑dimensional** and cannot be tabulated.
Practical systems approximate with:

* Factorised beliefs (assume independence).
* Interactive particle filters (sample other agents’ hidden variables).
* Recurrent neural encoders (embed observation history).

Selecting and validating one of these schemes is a modelling burden that arises long before optimisation.

---

## 5  Non‑stationarity at the individual level

Even with a **fixed** transition kernel *T*, the environment seen by a single agent is **non‑stationary** because state transitions depend on **others’ actions**, which can vary arbitrarily across time.  Consequences:

1. **Data‑collection pipelines** must record the full joint action each step; otherwise empirical estimates of *T* or *Oᵢ* are biased.
2. **Statistical estimation** of transition or observation models must condition on joint actions, multiplying sample requirements.

---

## 6  Simulation workload

| Factor                        | Effect on runtime or memory                                                                                                                                       |   |                                    |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | - | ---------------------------------- |
| **Synchronising agent calls** | Each step you must gather all actions, then sample *T* once.  In distributed simulators this creates network barriers.                                            |   |                                    |
| **Per‑step sampling cost**    | For physics‑based or high‑fidelity *T*, adding more agents often scales super‑linearly because collision checks, constraints, or communication messages increase. |   |                                    |
| **Logging schema**            | (time, *s*, a¹,…,aⁿ, o¹,…,oⁿ, r¹,…,rⁿ) ⇒ record size O(n +                                                                                                        | S | ).  Large *n* inflates disk usage. |
| **Parallelisation limits**    | Shared state coupling makes embarrassingly‑parallel roll‑outs hard; you often need synchronised clusters or GPUs.                                                 |   |                                    |

---

## 7  Learning or estimating the model itself

* **Coverage problem** — many (s, a¹,…,aⁿ) combinations are rarely visited; sample complexity grows with mⁿ.
* **Identifiability** — private observations mean that some state components can never be inferred without special probing experiments.
* **Experiment design** — you might need randomised action injection or scripted behaviour to illuminate dark corners of *T* or *Oᵢ*.

---

## 8  Observation‑sharing and communication channels

*Design choice, not yet behaviour*:

1. **Public vs. private signals** — Will some observations be broadcast?
2. **Latency and loss** — Does oᵢ arrive with delay, or can it be dropped?
3. **Message actions** — If agents can send explicit messages, the joint‑action space enlarges to (a\_env, msg).  You must extend *Oᵢ* to include other agents’ messages and decide how messages affect bandwidth and simulator step time.

Each option multiplies logging requirements and may require additional simulators for network delays.

---

## 9  Real‑time / embedded constraints

Robotic or edge deployments must now:

* Run multiple perception and control loops concurrently.
* Maintain separate private memory buffers for each agent’s observations.
* Exchange signals if any observations are broadcast—introducing latency, packet loss, and security concerns (encryption, authentication).

These engineering constraints interact directly with observation timing and thus with the definition of the POSG itself.

---

## 10  Debugging and reproducibility

* **Heisenbugs** — Rare joint‑action combinations cause states unreachable in single‑agent testing; comprehensive scenario stress‑tests are required.
* **Seed management** — Need a reproducible sequence of *joint* random events; per‑agent PRNG streams must be coordinated.
* **Schema evolution** — Adding a new agent or observation field breaks older logs; rigorous versioning and migration scripts are mandatory.

---

## 11  Key pre‑strategy take‑aways

1. **Expect exponential storage growth.**  Without factored or generative kernels, tables die as soon as *n* or |S| passes modest values.
2. **Plan belief approximations early.**  Exact interactive beliefs are impossible; choose particle filters, variational schemes, or RNN embeddings and validate their numerical stability.
3. **Log everything—or accept irrecoverable uncertainty.**  Missing joint actions or private observations renders most post‑hoc analyses unusable.
4. **Instrument for non‑stationarity.**  Build metrics that track how empirical transition statistics drift as other agents change behaviour.
5. **Design observation and communication layers as first‑class citizens.**  Their timing, bandwidth, and loss characteristics are *part of the model*, not after‑thought implementation details.

---

### Summary

A **POSG** merges the hidden‑state uncertainty of a POMDP with the multi‑agent coupling of a stochastic game, then multiplies every table, log, and computational loop by the product of players’ action and observation sets.
Before a single line of optimisation code is written, you must solve:

* **Exponential data‑representation problems**,
* **Interactive belief approximation**,
* **Synchronous simulation and logging**, and
* **Robust, version‑controlled engineering pipelines** under intrinsic non‑stationarity.

Handling these burdens correctly is the prerequisite for any subsequent analysis or algorithmic endeavour in partially observable multi‑agent worlds.



---



### Complexity gap between **POMDPs** and **POSGs**

*(strictly at the modelling, storage, simulation and data‑handling level — still **no** reference to solution concepts or “optimality”)*

| Complexity dimension                                          | POMDP (single agent)                                                  | POSG (multi‑agent, partially observable)                                                                      | How the burden grows when you go from POMDP → POSG                                                                                                   |                                                                                                                                                   |                                                                                                                                                          |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |
| ------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | - | --- | - | --- | - | ------- | -- | -------- | ------------- | ------------------------------------------------------------ | -------- | - | ---------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Agents**                                                    | Exactly **1**                                                         | **n > 1** distinct agents                                                                                     | Every core object (actions, observations, rewards, logs) gains an agent index; costs scale at least linearly in *n* and often exponentially.         |                                                                                                                                                   |                                                                                                                                                          |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |
| **Action space**                                              | Set *A*                                                               | Joint space *A* = ΠᵢAᵢ (size ≈ mⁿ if each agent has *m* actions)                                              | Tables and simulators now index by the *product* of players’ choices; storage and sample demands blow up multiplicatively.                           |                                                                                                                                                   |                                                                                                                                                          |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |
| **Observation model**                                         | One kernel \*O(o                                                      |  s′,a)\* and alphabet Ω                                                                                       | One kernel per agent: \*Oᵢ(oᵢ                                                                                                                        |  s′,a¹,…,aⁿ)\* with private alphabets Ωᵢ                                                                                                          | Tensor dimensionality jumps from                                                                                                                         | S |  ×  | A |  ×  | Ω | to n ×  | S  |  × mⁿ ×  | Ω             | , plus you must track which message each agent actually saw. |          |   |                        |                                                                                                                 |
| **Reward logging**                                            | Single scalar *rₜ* per step                                           | Vector (r¹ₜ,…,rⁿₜ) per step                                                                                   | Disk, bandwidth and analytics code must handle                                                                                                       | I                                                                                                                                                 | numbers per time‑step instead of one.                                                                                                                    |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |
| **Belief maintenance**                                        | Belief over *S* (                                                     | S                                                                                                             | ‑dimensional vector); exact Bayesian filter feasible when *S* moderate                                                                               | No finite‑dimensional sufficient statistic; in principle an agent needs a distribution over *(state, other agents’ hidden variables or policies)* | Belief update becomes intractable analytically; you must pick an approximation (particle filters, variational, RNN) and accept extra compute and memory. |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |
| **Stationarity from one agent’s view**                        | Transition law *T* is fixed; environment is Markov once action chosen | Apparent dynamics for any single agent are **non‑stationary** because transitions depend on *others’ actions* | Statistical estimation and simulation must record joint actions to remain unbiased; time‑varying behaviour of peers complicates repeatability tests. |                                                                                                                                                   |                                                                                                                                                          |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |
| **Descriptive storage (finite case)**                         | O(                                                                    | S                                                                                                             | ² ·                                                                                                                                                  | A                                                                                                                                                 |  +                                                                                                                                                       | S |  ·  | A |  ·  | Ω | )       | O( | S        | ² · mⁿ + n ·  | S                                                            |  · mⁿ ·  | Ω | ) — exponential in *n* | Full tabular representations become impossible after a few agents; compression or procedural kernels mandatory. |
| **Log size per time‑step**                                    | (s,a,o,r) → constant                                                  | (s, a¹,…,aⁿ, o¹,…,oⁿ, r¹,…,rⁿ) → O(n+                                                                         | S                                                                                                                                                    | )                                                                                                                                                 | Trace files and replay buffers grow linearly in *n*; networked simulators transfer more data each tick.                                                  |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |
| **Simulation synchronisation**                                | Single perception–act loop                                            | Must gather *all* agents’ actions before sampling one environment transition                                  | Adds barriers or message passing in distributed simulators; latency can dominate wall‑clock timing.                                                  |                                                                                                                                                   |                                                                                                                                                          |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |
| **Model identification / data coverage**                      | Need samples for each (s,a)                                           | Need samples for each (s,a¹,…,aⁿ) and for each agent’s observation map                                        | Sample complexity increases by mⁿ; rare joint actions may never occur without forced exploration scripts.                                            |                                                                                                                                                   |                                                                                                                                                          |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |
| **Engineering artefacts** (seeds, versioning, test harnesses) | One PRNG stream, one observation recorder                             | Multiple PRNG streams, per‑agent observation buffers, coordinated seed management                             | Reproducibility tooling becomes multi‑process or networked; schema migrations must preserve agent labels.                                            |                                                                                                                                                   |                                                                                                                                                          |   |     |   |     |   |         |    |          |               |                                                              |          |   |                        |                                                                                                                 |

---

#### Intuitive picture

1. **Cartesian blow‑up** – Every place the POMDP had a dimension indexed by *a*, the POSG now has a dimension indexed by the *joint* action.
2. **Private views** – Separate observation alphabets and kernels create *n* extra tensors and *n* extra log channels.
3. **Interactive uncertainty** – Because each agent’s observations conceal both the state **and** other agents’ observations, exact filtering turns into an infinite regress.
4. **Non‑stationarity** – Even if the physical world dynamics *T* stay fixed, the distribution over next states **seen by one agent** drifts whenever peers change behaviour; this complicates any empirical measurement or model‑learning pipeline.
5. **All resource curves steepen** – Memory, disk, bandwidth, CPU time and required episode count all grow at least linearly and often exponentially with the number of agents.

---

### Practical consequences **before** optimisation enters

| Task you might need to do              | POMDP cost                      | Additional POSG overhead                                                                                         |
| -------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Load model from file**               | Parse a few large arrays        | Parse and correctly **shard** observation and reward arrays per agent; join them on consistent indexing schemes. |
| **Roll out 1 M trajectories**          | Parallelise easily across cores | Must coordinate joint actions across cores; requires barriers or shared‑memory structures.                       |
| **Store dataset for offline learning** | (s,a,o,r) tuples → modest size  | Tuple size multiplies by *n*; high‑cardinality joins needed during preprocessing.                                |
| **Visualise traces**                   | Single timeline plot            | Multiple timelines, plus overlays to show what each agent privately “saw”—UI tooling more complex.               |
| **Audit transition statistics**        | Condition on (s,a) pairs        | Condition on (s,a¹,…,aⁿ) and perhaps on *agent ID* when analysing observations; data sparsity acute.             |

---

### Bottom line

*Moving from a POMDP to a POSG multiplies **every** modelling ingredient by the product of the agents’ action and observation sets, introduces interactive uncertainty that destroys simple belief updates, and replaces a stationary data‑generation process with one that drifts as other agents act.*
These factors raise **storage, compute, logging, synchronisation and identifiability costs**—all **before** you attempt to define or compute any notion of intelligent behaviour.



---


### Quick‑Assessment Checklist

Use the questions below **in order**. Stop as soon as you reach the first *Yes* in each block—that is the **lowest‑complexity model** that can still capture the phenomenon you face.
*(Separate “reward structure” tags—zero‑sum, common‑reward, general‑sum—apply at **every** level and should be recorded after you choose the model.)*

---

#### Block A Is it even multi‑agent?

| Question                                                                      | If **No**                                      | If **Yes**          |
| ----------------------------------------------------------------------------- | ---------------------------------------------- | ------------------- |
| > Are there **two or more decision‑makers** whose choices influence outcomes? | Use an **MDP / POMDP** (single‑agent setting). | Proceed to Block B. |

---

#### Block B One‑shot or temporally extended?

| Question                                                                                                         | If **Yes**                              | If **No**           |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ------------------- |
| > Does everything of interest happen in a **single simultaneous move** (no notion of time, no carry‑over state)? | Use a **Normal‑Form (Strategic) Game**. | Proceed to Block C. |

*Heuristics*: auctions with sealed bids, static pricing duels, Rock‑Paper‑Scissors variants.

---

#### Block C Static repetition or evolving environment state?

| Question                                                                                                                          | If **Yes**                           | If **No**           |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------- |
| > Does the world have **no explicit state** beyond the running record of who played what? (Each period is the *same* stage game.) | Use a **Repeated Normal‑Form Game**. | Proceed to Block D. |

*Heuristics*: Iterated prisoner’s‑dilemma tournaments, repeated ad‑auctions, contractual relationships with no external dynamics.

---

#### Block D Is the true environment state fully visible to all?

| Question                                                                                                 | If **Yes**                               | If **No**           |
| -------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------- |
| > Can **every agent perfectly observe** the current environment state as well as all past joint actions? | Use a **Stochastic Game (Markov Game)**. | Proceed to Block E. |

*Heuristics*: board games with full information (chess, Go); multi‑robot tasks with a shared global map.

---

#### Block E Handle hidden or private information

| Question                                                                                                    | If **Yes**                                      | Model needed |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ------------ |
| > Does at least one agent have **private or noisy observations** of the state and/or other agents’ actions? | **Partially Observable Stochastic Game (POSG)** |              |

*Heuristics*: poker, multi‑drone search where each drone has limited sensors, any setting with lossy or delayed communication.

---

### Additional decision tags (orthogonal—mark them once the base model is chosen)

1. **Reward structure**

   * Zero‑sum   all rewards sum to zero.
   * Common‑reward   all agents share the same payoff.
   * General‑sum   anything else.

2. **Communication actions**

   * Are explicit messages part of the problem?
   * If *Yes*, extend the chosen model by adding a **message component** to each action and an entry in the observation function.

3. **Knowledge/parameter certainty**

   * Known dynamics & rewards → planning / simulation setting.
   * Unknown dynamics & rewards → learning / data‑driven setting (collect corresponding logging requirements early).

4. **Continuous or large discrete sets**

   * If any core set (state, action, observation) is continuous or huge, plan for parameterised or generative representations rather than raw tables.

---

### How to use the checklist in practice

1. **Answer the blocks in sequence** for the *simplest* scenario you cannot rule out—this avoids over‑complicating the model.
2. **Record the formal tuple immediately** (agents, actions, state, transitions, observations, rewards); this forces clarity and aids reproducibility.
3. **Tag orthogonal features** (reward structure, communication, unknown parameters) so downstream teammates or tools can read the assumptions at a glance.
4. **Re‑evaluate only if new evidence appears** (e.g., discovering hidden sensors or delayed messages). Otherwise keep the model stable—changing levels mid‑project is costly.

This checklist should fit on a single slide or README and is designed to spare practitioners from premature deep dives into unnecessary modelling complexity.



---


### Rapid Game‑Model Triage

**Purpose :** help engineers decide—in a few minutes and with no game‑theory background—**which formal model from Chapter 3** is the *least* complex one that still captures their multi‑agent scenario.
*(Everything below is model‑selection only; it deliberately avoids solution concepts, learning algorithms, or implementation details.)*

---

#### 1  Is it a *multi‑agent* decision problem?

| Question                                                                 | If **No** (one decision‑maker)                         | If **Yes** (≥ 2 agents) |
| ------------------------------------------------------------------------ | ------------------------------------------------------ | ----------------------- |
| Do two or more independent entities choose actions that affect outcomes? | **Use an MDP or POMDP** (single‑agent RL). ─► **STOP** | Continue to § 2.        |

---

#### 2  Does the environment have an **evolving state**?

| Question                                                             | If **No**                              | If **Yes**                              |
| -------------------------------------------------------------------- | -------------------------------------- | --------------------------------------- |
| Does anything change between actions besides logging who chose what? | Proceed to § 3. *(Static interaction)* | Proceed to § 4. *(Dynamic interaction)* |

---

#### 3  Static interaction: one‑shot or repeated?

| Question                                                                                                                | Model                         | When it fits                                                               |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------- | -------------------------------------------------------------------------- |
| All strategic choices happen in **one simultaneous move**—there is no “next round”.                                     | **Normal‑Form Game**          | Auctions with sealed bids; Rock‑Paper‑Scissors; single pricing duel.       |
| The **same** stage interaction repeats for T rounds (finite or infinite) and policies may use the joint‑action history. | **Repeated Normal‑Form Game** | Iterated Prisoner’s Dilemma; daily ad auctions with no new external state. |

*If either answer is **Yes**, mark the choice and skip to § 7.*

---

#### 4  Dynamic interaction: explicit environment state

| Question                                                                                  | If **Full observability** | If **Partial / noisy / private observability**  |
| ----------------------------------------------------------------------------------------- | ------------------------- | ----------------------------------------------- |
| Can every agent see the entire current environment state *and* the previous joint action? | **Stochastic Game**       | **Partially Observable Stochastic Game (POSG)** |

*Helpful heuristics*

* Full observability → board games, centralized simulators with shared global map.
* Partial observability → robots with local sensors, card games with hidden hands, fog‑of‑war RTS.

---

#### 5  Optional additions that do **not** change the base model

After picking the row above, decide whether you also need:

| Add‑on                                                                        | How to model it (per Chapter 3)                                                                                                    |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Communication actions** (messages that do **not** alter the physical state) | Augment each action with a message component `a_i = (x_i, m_i)`; messages enter other agents’ observations (§ 3.5, Eq 3.6–3.7).    |
| **Continuous state, action, or observation sets**                             | Same model, but store `T`, `O_i` etc. as analytic or generative functions rather than tables.                                      |
| **Unknown dynamics / rewards**                                                | Keep the chosen tuple but note that the real system is a *black box*; your code must estimate or sample `T`, `O_i`, `R_i` (§ 3.6). |

---

#### 6  Record the **reward‑structure tag** (orthogonal)

* Zero‑sum   ∑ R\_i = 0
* Common‑reward R\_i = R\_j ∀i,j
* General‑sum   anything else

Tag it for later—it influences evaluation metrics and algorithm families but **does not change the chosen game model**.

---

#### 7  Fill in the formal tuple immediately

| Model                | Required tuple elements                |
| -------------------- | -------------------------------------- |
| Normal‑Form          | ⟨ I, {A\_i}, {R\_i} ⟩                  |
| Repeated Normal‑Form | Same as above + horizon *T*            |
| Stochastic Game      | ⟨ I, S, {A\_i}, T, {R\_i}, µ ⟩         |
| POSG                 | Stochastic‑game tuple + {Ω\_i}, {O\_i} |

Writing the tuple forces clarity on *what must be measured, logged, or simulated* and prevents miscommunication across a team.

---

### How to use this checklist

1. **Walk top‑to‑bottom once** for the simplest scenario that you cannot rule out; resist jumping to POSG unless partial information is truly indispensable.
2. **Mark the optional add‑ons and reward tag** right after picking the base model.
3. **Share the filled tuple in your README or design doc**—all downstream algorithm or simulation choices hinge on these ingredients.
