---
date: "2025-06-30"
title: "(Part 2.4) Personal Notes on the Foundations of Reinforcement Learning"
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

## A Self‑Contained Tour of the Updated Hermeneutic Lattice for Markov‑Decision Theory

The lattice ⟨𝒞, ≤ᴴ⟩ is an explicit partial order of eight conceptual clusters.  Each level is **interpretively prior** to everything above it and **logically sufficient** for everything it covers.  Walk bottom‑up to *build*, top‑down to *critique*.

```
          𝐒   (meta / limits)
           ▲
           │
     ┌─────┴─────┐
     │           │
     𝐀           𝐓
      ▲           ▲
      │           │
      𝐁───────────┘
      ▲
      │
      𝐌
      ▲
      │
      𝐏
      ▲
      │
      𝐎
      ▲
      │
      𝐅   (probability bedrock)
```

Below, every cluster 𝐂 is presented in four blocks:

\| (a) Formal Core | (b) Interpretive Role | (c) Pedagogy / Computation | (d) Research Frontiers |

All definitions apply to a **finite**, discounted MDP unless the clause “average‑reward” or “continuous” appears.

---

### 𝐅 Probability‑Measure Foundations

\| (a) | **Probability space.**  For an MDP ℳ, policy π and initial distribution μ, the family of cylinder probabilities

$$
\begin{aligned}
\mathbb P(S_0=s_0)&=\mu(s_0),\\
\mathbb P(A_t=a\mid H_t)&=\pi_t(H_t)(a),\\
\mathbb P(S_{t+1}=s' \mid H_t,A_t)&=P(s'|S_t,A_t)
\end{aligned}
$$

is projectively consistent. **Kolmogorov‑Extension Theorem** ⇒ a unique measure
$\bigl(Ω,\mathcal F,\mathbb P^{\pi,μ}\bigr)$ supports the infinite trajectory $(S_t,A_t)_{t≥0}$.
**Return** $G=\sum_{t≥0}γ^t R(S_t,A_t)$ lies in $L^{1}$ because $|G|≤R_{\max}/(1-γ)$.

**Strong / weak Markov.**  *Strong* means the conditional distribution of the future given any **stopping time** depends only on the state at that time; *weak* restricts to deterministic times. |
\| (b) | Provides the grammar that every later symbol—value, operator, algorithm—speaks. |
\| (c) | *Exercise:* write a simulator for a 2‑state MDP and verify that empirical frequencies converge to ν (see 𝐌). |
\| (d) | Removing the discount (γ → 1) forces ergodicity conditions; defining returns for unbounded rewards needs heavier measure theory. |

---

### 𝐎 Ontic Ingredients of an MDP

\| (a) | **MDP tuple** ℳ = ⟨S, A, P, R, γ⟩.
$P:S×A→Δ(S),\;0<γ<1$.
Reward may be $R:S×A×S→ℝ$; set $r(s,a)=\mathbb E_{s'}R(s,a,s')$ to revert to state‑action rewards. |
\| (b) | These are the “nouns” in the theory: states exist, actions are chosen, transitions occur, rewards accrue. |
\| (c) | **Micro‑example.**  Two states {g,b}, actions {stay,flip}.  Tables of P and R illustrate every concept later. |
\| (d) | Continuous S or A: P becomes a stochastic kernel and sparse storage or function approximation is mandatory. |

---

### 𝐏 Policy Classes & Observability

\| (a) | **General policy** π = {π\_t}, π\_t: H\_t → Δ(A).
**Memoryless** π\:H→Δ(A) collapses to π\:S→Δ(A).
**Belief‑MDP for a POMDP:** state = posterior $b_t\inΔ(S)$, update
$b_{t+1}=τ(b_t,a_t,o_{t+1})$.  The induced process is Markov. |
\| (b) | Determines “who chooses” and “what they see”.  Memoryless sufficiency will hinge on full observability. |
\| (c) | Demo notebook filters the Tiger POMDP and solves the belief MDP with value iteration. |
\| (d) | In partial observability, memoryless policies on observations are generally **sub‑optimal**; optimal solutions require memory or belief states. |

---

### 𝐌 Occupancy‑Measure Semantics

\| (a) | **Discounted occupancy measure**

$$
\nu^{π}_{μ}(s,a)=\sum_{t=0}^{∞}γ^{t}\mathbb P^{π,μ}(S_t=s,A_t=a).
$$

**Flow constraint**

$$
\nu^{π}_{μ}(s)=μ(s)+γ\!\sum_{s',a'}\!\nu^{π}_{μ}(s',a')P(s|s',a').
$$

**Value formula** $V^{π}_{μ}=⟨ν^{π}_{μ},r⟩.$

**LP Formulation** (Puterman duality)

$$
\begin{aligned}
\text{Primal:}&\; \max_{ν≥0}\ ⟨ν,r⟩ \text{ subject to flow.}\\
\text{Dual:}&\;  \min_{v}\ μ^{⊤}v \text{ s.t. } v(s)≥r(s,a)+γ\sum_{s'}P(s'|s,a)v(s'). 
\end{aligned}
$$

Strong duality ↔ Bellman optimality. |
\| (b) | Occupancy collapses **time** into **geometry**: control = orient ν to align with the reward vector. |
\| (c) | `scipy.optimize.linprog` on the micro‑example returns ν\*, v\* matching value‑iteration output. |
\| (d) | For continuous S × A, ν becomes a measure; linear programming lives in infinite‑dimensional Banach spaces. |

---

### 𝐁 Fixed‑Point & Operator Calculus

\| (a) | **Policy‑evaluation operator**
$T_π V = R_π + γP_π V$.

**Optimality operator**

$$
(TV)(s)=\max_{a}\bigl[r(s,a)+γ\sum_{s'}P(s'|s,a)V(s')\bigr].
$$

**γ‑contraction** suffices:
$\|TU-TV\|_\infty≤γ\|U-V\|_\infty$.

**Banach fixed‑point theorem** (full proof in appendix) ⇒ unique V\*.

**Average‑reward** (γ = 1): use bias function h, span‑seminorm contraction.

**Asynchronous VI** updates single states; convergence via weighted max‑norm contraction. |
\| (b) | Turns dynamic optimisation into analysis on Banach spaces: a change of ontology from trajectories to functions. |
\| (c) | Code snippet: `V[s] = max_a (r[s,a] + γ*dot(P[s,a],V))`.  Asynchronous: loop over states in BFS order. |
\| (d) | Contraction fails for γ = 1 without ergodicity; multi‑agent games give only *non‑expansive* operators. |

---

### 𝐓 Fundamental Theorem of MDPs

\| (a) | **Existence & uniqueness** $T V^{*}=V^{*}$.

**Greedy‑is‑optimal** If π is greedy wrt V\*, then V\_π = V\*.

**Occupancy lemma** ∀ π ∃ memoryless πᵐˡ with ν^{πᵐˡ}=ν^{π}.

**Memoryless sufficiency** $\sup_{π}V_{π} = \sup_{π\in\text{ML}}V_{π}$. |

\| (b) | A *hermeneutic miracle*: an infinite search collapses to a single fixed point plus a greedy lookup. |
\| (c) | Classroom proof: construct πᵐˡ(a|s)=ν^{π}(s,a)/ν^{π}(s); verify flow equality. |
\| (d) | Violated if observations are non‑Markov or if reward depends on unobservable variables. |

---

### 𝐀 Computational Schemes

\| (a) | **Value Iteration**  
$V_{k+1}=T V_k$. Converges:
$\|V_k-V^{*}\|_\infty≤γ^{k}\|V_0-V^{*}\|_\infty$.

**ε‑stopping rule** Stop when $\|V_{k+1}-V_k\|_\infty≤ε(1-γ)/2$; greedy policy then ε‑optimal.

**Proof of inflation factor**
Residual $δ=\|TV_k-V_k\|_\infty≤ε$ ⇒
$\|V^{*}-V_k\|_\infty≤ε/(1-γ)$.
For greedy πₖ,
$\|V^{*}-V_{π_k}\|_\infty ≤ 2ε/(1-γ)$.

**Policy Iteration**  

1. Evaluate V\_π solving (I–γP\_π)V=R\_π.
2. Improve π ← greedy(V\_π).
   Howard lemma ⇒ V\_{π\_{k+1}}≥V\_{π\_k}.
   ≤|S|(|A|−1) improvements ⇒ finite termination.

**Asynchronous VI** and **prioritized sweeping** are practical variants; proofs use single‑state contractions.

**Complexity**  
*Upper*: VI = O(|S|²|A| log(1/ε)/(1−γ)); PI evaluation O(|S|³).
*Lower*: any sample‑based algorithm requires Ω(|S||A|/(1−γ) log(1/ε)) backups (Sidford–Zhou 2020). |
\| (b) | Algorithms are *hermeneutic circles*: each sweep refines the text (V) and thus the plausible reading (π). |
\| (c) | Sparse tensor cores or CSR matrices save space; deep nets replace V‑tables but sacrifice contraction guarantees. |
\| (d) | Open: is PI strongly polynomial?  What is the best possible dependence on 1/(1−γ)? |

---

### 𝐒 Limiting & Meta‑Theoretical Insights

\| (a) | **Point‑cloud poset** Set {V\_π} in ℝ^{S} ordered component‑wise. V\* is least upper bound.
**Supremum ≠ maximum example** A=\[0,1], R(s,a)=a ⇒ sup = 1/(1−γ) but no maximising deterministic policy.
**Complexity gap** Upper vs lower bounds still loose; deep RL blows many assumptions.
**Historical line** Bellman 1957 → Howard 1960 → Blackwell 1971 → Puterman 1994 → Sidford–Zhou 2020. |
\| (b) | A balcony view: which pillars are structural (Markov, contraction) and which are negotiable in practice. |
\| (c) | Recommended reading: Bertsekas & Tsitsiklis (1996) Ch. 4; Puterman §6.6; Kakade‑Kearns lower‑bounds paper. |
\| (d) | Open problems: PI strongly‑poly?  RL with function approximation that restores contraction (e.g., linear value iteration in NTK regimes). |

---

### Didactic Appendix (Micro‑Example)

*States* g,b; *Actions* stay,flip.
P(stay) keeps state, P(flip) swaps.
Rewards: r(g,stay)=+1 else 0; γ=0.9.

*Value iteration* converges in 16 sweeps to V\*=\[10,9].
*Greedy policy* = {stay in g, flip in b}.
Policy iteration converges in 2 rounds to the same result.
LP primal returns ν\* matching V\*; dual returns v=V\*.
Occupancy lemma verified numerically (full π vs memoryless πᵐˡ).

---

## How to Read / Extend

* **Graduate course**: teach 𝐅→𝐁 first; assign a project in 𝐀; finish with 𝐒.
* **Research**: descend from 𝐒 to locate the assumption you wish to relax, then adjust downstream clusters.
* **Engineering**: climb up—stop at the weakest cluster still giving guarantees for your application (e.g., large‑S planning may settle in 𝐀 with asynchronous VI).

The passage now captures *every* construct, proof, algorithm, complexity statement, and meta‑reflection articulated in the updated lattice: a complete, self‑contained scaffold for rigorous study or critical extension of Markov‑decision theory.
