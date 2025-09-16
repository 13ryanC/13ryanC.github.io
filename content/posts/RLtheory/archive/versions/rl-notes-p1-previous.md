---
date: "2025-06-27"
title: "(Part 1) MDP Fundamentals and Optimality" 
summary: "Aim to provide more insight on RL foundations for beginners. Includes MDP definitions, bellman eq, funda thm, value functions, contrction mappings. Ensure rigorous definitions of MDP, value functions, contraction mappings."
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

## TL;DR: 

### The Core Idea
Reinforcement Learning: agents learn optimal decisions in uncertain environments through trial and error, formalized using **Markov Decision Processes (MDPs)**.

### Mathematical Foundation
**MDP**: States, Actions, Transition probabilities, Rewards, discount factor. 

Agent follows a **policy** to maximize expected future rewards. 

Key insight: current state contains all info needed for optimal decisions.

### Three Domains of RL
**1. Planning**: Environment is known → find optimal actions via dynamic programming/search

**2. Offline RL**: Learn from fixed dataset → avoid trying actions not in data  

**3. Online RL**: Learn while interacting → balance exploration vs exploitation

### The Central Challenge
**Problem**: Learn optimal behavior without knowing how the environment works

**Solution**: Must explore (try new actions) even if it hurts short-term performance

### Bottom Line
RL provides a unified framework for sequential decision-making under uncertainty. The core challenge is balancing exploration (learning) with exploitation (performing well) across three different practical scenarios.

---

# Measure-Theoretic Framework

## 1. Foundational Measurable Spaces

We begin with finite sets $S$ (states) and $A$ (actions) and establish their natural measurable structures:

| Symbol | Meaning | σ-field |
|--------|---------|---------|
| $S$ | Finite state set | $\mathcal{S} = 2^S$ |
| $A$ | Finite action set | $\mathcal{A} = 2^A$ |

**Discrete σ-field Choice:** For any finite set $E$, we equip it with the discrete σ-field $2^E$ (the power set). This choice is natural because:
- It contains all singletons, making every individual element measurable
- It's closed under all set operations (countable unions, intersections, complements)
- For finite sets, this is the richest σ-field possible
- Probability computations become purely combinatorial

## 2. Single Time-Step Space

Before constructing infinite trajectory spaces, we establish the building block:

**Single Time-Step Space:** $\Omega_0 := S \times A$ with σ-field $\mathcal{F}_0 := \mathcal{S} \otimes \mathcal{A} = 2^{S \times A}$.

This represents a single state-action pair, the fundamental unit of a trajectory.

## 3. Infinite Trajectory Space Construction

### 3.1 The Trajectory Space

**Definition:** The trajectory space is the countable product:
$$T := (S \times A)^{\mathbb{N}} = \{(s_0,a_0,s_1,a_1,\ldots) : s_t \in S, a_t \in A \text{ for all } t \geq 0\}$$

Each element $\tau \in T$ represents an infinite sequence of state-action pairs.

**Product σ-field:** We equip $T$ with the product σ-field:
$$\mathcal{T} := \bigotimes_{t=0}^{\infty} \mathcal{F}_0$$

This is the smallest σ-field making all coordinate projections measurable.

### 3.2 Coordinate Processes

**Definition:** Define the canonical coordinate maps on $T$:
- $S_t : T \to S$ by $S_t(\tau) = s_t$ where $\tau = (s_0,a_0,s_1,a_1,\ldots)$
- $A_t : T \to A$ by $A_t(\tau) = a_t$

**Measurability:** Both $S_t$ and $A_t$ are measurable by construction of the product σ-field. Specifically, for any $B \in \mathcal{S}$:
$$S_t^{-1}(B) = \{\tau \in T : S_t(\tau) \in B\}$$
belongs to $\mathcal{T}$ because the product σ-field is defined precisely to ensure all coordinate projections are measurable.

**Canonical Process:** The sequence $((S_t, A_t))_{t \geq 0}$ forms the canonical stochastic process on trajectory space, providing the observable coordinates at each time without requiring any probabilistic dynamics.

### 3.3 Cylinder Sets: The Building Blocks

**Definition:** For any finite sequence $h_{0:t} = (s_0,a_0,\ldots,s_t) \in (S \times A)^t \times S$, define the cylinder set:
$$C_t(h_{0:t}) := \{\tau \in T : (S_0(\tau), A_0(\tau), \ldots, S_t(\tau)) = (s_0,a_0,\ldots,s_t)\}$$

**Interpretation:** $C_t(h_{0:t})$ contains all infinite trajectories that begin with the specified finite history $h_{0:t}$.

**Key Properties:**

1. **Generation of $\mathcal{T}$:** The cylinder sets generate the product σ-field:
   $$\mathcal{T} = \sigma\left(\{C_t(h_{0:t}) : t \geq 0, h_{0:t} \in (S \times A)^t \times S\}\right)$$

2. **π-system Structure:** Cylinder sets form a π-system (closed under finite intersections):
   $$C_t(h) \cap C_u(g) = \begin{cases}
   C_{\max(t,u)}(\text{merged history}) & \text{if } h \text{ and } g \text{ are consistent} \\
   \varnothing & \text{otherwise}
   \end{cases}$$

3. **Point Separation:** Any two distinct trajectories $\tau_1 \neq \tau_2$ are separated by some cylinder set (they first differ at some time $n$, and the cylinder of length $n$ contains one but not the other).

### 3.4 Uniqueness of Probability Measures

**Fundamental Theorem:** The π-λ (Dynkin) theorem provides the key uniqueness result:

> If two probability measures $\mathbb{P}$ and $\mathbb{Q}$ on $(T,\mathcal{T})$ agree on all cylinder sets, then $\mathbb{P} = \mathbb{Q}$.

**Proof Outline:** Cylinder sets form a π-system that generates $\mathcal{T}$ and separates points. The π-λ theorem then guarantees uniqueness.

**Practical Consequence:** Any probability measure on trajectory space is uniquely determined by its finite-dimensional distributions:
$$\mu_t(h_{0:t}) = \mathbb{P}(C_t(h_{0:t}))$$

This is the infinite-dimensional analogue of the Carathéodory extension theorem.

## 4. Probability Kernels and Markov Dynamics

### 4.1 Kernel Definitions

**Probability Kernel:** A map $K: (X,\Sigma_X) \times \Sigma_Y \to [0,1]$ is a probability kernel if:
- For each $x \in X$: $K(x,\cdot)$ is a probability measure on $(Y,\Sigma_Y)$
- For each $B \in \Sigma_Y$: $K(\cdot,B)$ is $\Sigma_X$-measurable

**Examples in Our Setting:**
- Transition kernel: $P: S \times A \times \mathcal{S} \to [0,1]$
- Policy kernel: $\pi_t: H_t \times \mathcal{A} \to [0,1]$ where $H_t$ is the space of histories up to time $t$

### 4.2 Trajectory Measure Construction

**Ionescu-Tulcea Theorem:** Given an initial distribution $\mu_0$ on $S$ and a sequence of kernels defining the dynamics, there exists a unique probability measure $\mathbb{P}$ on $(T,\mathcal{T})$ such that the coordinate processes $(S_t, A_t)$ have the prescribed finite-dimensional distributions.

**Construction:** The measure is uniquely determined by specifying:
$$\mathbb{P}(C_t(s_0,a_0,\ldots,s_t)) = \mu_0(s_0) \cdot \pi_0(a_0|s_0) \cdot P(s_1|s_0,a_0) \cdot \pi_1(a_1|s_0,a_0,s_1) \cdots$$

## 5. Information Structure and Filtrations

### 5.1 Timeline and Causality

The temporal structure of decision-making follows this pattern:
```
t=0: observe S_0 → choose A_0 → t=1: observe S_1 → choose A_1 → ...
```

**Crucial Timing:** At time $t$, the agent observes state $S_t$ and then chooses action $A_t$ based on the history $(S_0,A_0,\ldots,S_{t-1},A_{t-1},S_t)$.

### 5.2 History Filtration

**Definition:** 

The history filtration $(\mathcal F_t)_{t \geq 0}$ is defined by:

$$
\mathcal F_t := \sigma(S_0,A_0,S_1,A_1,\ldots,S_{t-1},A_{t-1},S_t)
$$

**Key Point:** 

$\mathcal{F}_t$ contains the information available to the agent *just before* choosing action $A_t$. 

Notably, $A_t$ is not included in $\mathcal{F}_t$ because it hasn't been chosen yet.

**Filtration Property:** 

Since information accumulates over time, we have $\mathcal F_t \subseteq \mathcal F_{t+1}$ for all $t$.

### 5.3 History Process

**Definition:** The history process $H_t: T \to (S \times A)^t \times S$ is defined by:
$$H_t(\tau) := (S_0(\tau), A_0(\tau), \ldots, S_{t-1}(\tau), A_{t-1}(\tau), S_t(\tau))$$

**Measurability:** $H_t$ is $\mathcal{F}_t$-measurable by construction, representing the concrete information available at time $t$.

**Note:** The history ends with a state $S_t$, not an action, reflecting that the agent observes the current state before choosing the action.

### 5.4 Admissible Policies

**Definition:** A policy $\pi = (\pi_t)_{t \geq 0}$ is *admissible* if each $A_t$ is $\mathcal{F}_t$-measurable. This means:
- Actions can depend on past states and actions
- Actions can depend on the current state
- Actions cannot depend on future information

**Mathematical Formulation:** For each $t$, there exists a measurable function $f_t$ such that:
$$A_t = f_t(H_t)$$

This captures the intuitive notion that rational agents cannot use information they don't possess.

## 6. Applications and Interpretations

### 6.1 Value Functions

**Definition:** For an admissible policy $\pi$ and return $G_t$, the value function is:
$$V_t^\pi := \mathbb{E}^\pi[G_t | \mathcal{F}_t]$$

The conditioning on $\mathcal{F}_t$ ensures that value functions depend only on information available to the agent.

### 6.2 Martingale Theory

**Application:** In temporal difference learning, the error terms form martingale differences with respect to the history filtration:
$$\mathbb{E}[\delta_t | \mathcal{F}_t] = 0$$

This property is crucial for convergence proofs in reinforcement learning algorithms.

### 6.3 Stopping Times

**Definition:** A random time $\tau$ is a stopping time if $\{\tau \leq t\} \in \mathcal{F}_t$ for all $t$.

**Interpretation:** The decision to stop at time $\tau$ depends only on information available up to that time, not on future information.

## 7. Summary of Key Insights

### 7.1 Hierarchical Structure

The framework builds in natural stages:
1. **Finite spaces** → discrete σ-fields (computational tractability)
2. **Single time-step** → product structure (compositional building blocks)
3. **Infinite trajectories** → product σ-field (infinite-dimensional probability)
4. **Cylinder sets** → generating system (finite-dimensional specifications)
5. **Uniqueness** → π-λ theorem (well-posed probability measures)

### 7.2 Information and Causality

The history filtration $(\mathcal{F}_t)$ formalizes:
- **Non-anticipation:** Decisions cannot depend on future information
- **Adaptation:** Processes are measurable with respect to available information
- **Causality:** The mathematical structure enforces temporal causality

### 7.3 Practical Implications

| Concept | Mathematical Role | Practical Importance |
|---------|------------------|---------------------|
| Cylinder sets | Generate σ-field | Computational tractability |
| History filtration | Define admissible policies | Enforce causality |
| Coordinate processes | Canonical representation | Model-free analysis |
| Uniqueness theorem | Well-posed measures | Consistent probability models |

## 8. Technical Appendix

### 8.1 Essential Definitions

| Concept | Definition |
|---------|------------|
| **σ-field** | Collection closed under complements and countable unions |
| **Measurable map** | Preimage of measurable sets is measurable |
| **Product σ-field** | Smallest σ-field making projections measurable |
| **π-system** | Collection closed under finite intersections |
| **π-λ theorem** | π-system generating same σ-field as λ-system implies equality |

### 8.2 Common Misconceptions

**Misconception 1:** "Why not include $A_t$ in $\mathcal{F}_t$?"
- **Answer:** Including $A_t$ in $\mathcal{F}_t$ would assume the agent knows the action before choosing it, violating causality.

**Misconception 2:** "Is this the same as the canonical filtration?"
- **Answer:** No. The canonical filtration would include $A_t$ at time $t$. Our history filtration is intentionally one step behind to respect decision-making timing.

**Misconception 3:** "Why not use topological methods?"
- **Answer:** For finite state and action spaces, measure theory provides the most natural framework. Topology adds unnecessary complexity without benefits.

This measure-theoretic framework provides the rigorous foundation for probabilistic reasoning about infinite-horizon sequential decision processes, ensuring that all constructions respect causality and information constraints while maintaining computational tractability through the finite-dimensional structure of cylinder sets.

# The Markov Decision Process Framework

The unifying mathematical foundation for reinforcement learning is the Markov Decision Process (MDP), formally defined as the 5-tuple:

$$\mathcal{M} = \langle S, A, P, R, \gamma \rangle$$

where:
- **States ($S$):** The set of all possible environment configurations (equipped with $\sigma$-algebra $\Sigma_S$)
- **Actions ($A$):** The set of all possible agent actions (equipped with $\sigma$-algebra $\Sigma_A$)
- **Transition kernel ($P(\cdot \mid s,a)$):** Probability distribution over next states given current state-action pair
- **Reward function ($R: S \times A \to \mathbb{R}$):** Expected immediate reward for taking action $a$ in state $s$
- **Discount factor ($\gamma \in [0,1)$):** Controls the trade-off between immediate and future rewards

The discount factor serves multiple purposes: it ensures finite returns in infinite-horizon problems, creates an effective horizon of approximately $\frac{1}{\varepsilon(1-\gamma)}$ steps, and provides implicit regularization favoring earlier rewards.

# Policies and the Agent-Environment Loop

A **policy** $\pi$ defines the agent's strategy for action selection. In its most general form, a policy is a sequence of conditional probability distributions $\{\pi_t\}_{t \geq 0}$:

$$\pi_t : \mathcal{H}_t \to M_1(A)$$

where $\mathcal{H}_t = (S \times A)^{t-1} \times S$ represents the history space at time $t$, and $M_1(A)$ denotes probability measures over actions.

The **history** at time $t$ is: $H_t = (S_0, A_0, S_1, \ldots, S_{t-1}, A_{t-1}, S_t)$

The agent-environment interaction forms a closed feedback loop:
1. Initial state $S_0 \sim \mu$ (initial state distribution)
2. Action selection $A_t \sim \pi_t(H_t)$
3. State transition $S_{t+1} \sim P(\cdot \mid S_t, A_t)$
4. Reward observation $R_t = R(S_t, A_t)$

A **stationary Markov policy** is a single kernel $\pi : S \times \Sigma_A \to [0,1]$ that depends only on the current state.

# Value Functions and Bellman Equations

The agent's goal is to maximize expected **discounted return**:

$$
J(\pi) = \mathbb E_{\mu}^{\pi} \left[ \sum_{t=0}^{\infty} \gamma^t R(S_t,A_t) \right]
$$

This leads to the definition of **value functions**:

$$V^\pi(s) := \mathbb{E}^\pi \left[\sum_{t=0}^{\infty}\gamma^{t}R_t \mid S_0=s\right]$$

$$Q^\pi(s,a) := \mathbb{E}^\pi \left[\sum_{t=0}^{\infty}\gamma^{t}R_t \mid S_0=s, A_0=a\right]$$

The **optimal value functions** are:

$$
V^\ast (s) = \sup_{\pi} V^\pi(s), \quad Q^\ast (s,a) = \sup_{\pi}Q^\pi(s,a)
$$

Define the policy-induced reward and transition functions:
$$R_\pi(s):=\int_A\pi(\mathrm{d}a\mid s)\,R(s,a), \quad P_\pi(\mathrm{d}s'\mid s):=\int_A\pi(\mathrm{d}a\mid s) P(\mathrm{d}s'\mid s,a)$$

The **Bellman equations** for policy evaluation are:

$$
V^\pi(s) = R_\pi(s) +\gamma\int_S P_\pi(\mathrm{d}s'\mid s)\,V^\pi(s')
$$

$$
Q^\pi(s,a) = R(s,a) +\gamma\int_S P(\mathrm{d}s'\mid s,a) \int_A \pi(\mathrm{d}a'\mid s')\,Q^\pi(s',a')
$$

The **Bellman optimality equations** are:

$$
V^\ast (s)=\max_{a} \lbrace R(s,a) +\gamma\int_S P(\mathrm{d}s'\mid s,a)\,V^*(s') \rbrace
$$

$$
Q^\ast (s,a)=R(s,a) +\gamma\int_S P(\mathrm{d}s'\mid s,a)\, \max_{a'}Q^*(s',a')
$$

Any deterministic policy greedy with respect to $Q^*$ is optimal.

# State Occupancy Measures

The **state occupancy measures** characterize the distribution of states visited under policy $\pi$:

$$d_{\mu,T}^\pi(s):=\frac{1}{T}\sum_{t=0}^{T-1} \mathbb{P}_\mu^\pi(S_t=s) \quad \text{(finite-horizon)}$$

$$d_\mu^\pi(s):=(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t} \mathbb{P}_\mu^\pi(S_t=s) \quad \text{(discounted)}$$

The performance objective can be rewritten as:

$$
J(\pi)=\frac{1}{1-\gamma} \mathbb E_{s\sim d_\mu^\pi}[R_\pi(s)]
$$

### Alternative Performance Criteria

Beyond discounted return, other objectives include:
- **Finite-horizon return:** $G^H_t = \sum_{k=0}^{H-1} R_{t+k+1}$
- **Average reward:** $\lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^{T}R_t$
- **Cumulative regret:** $\text{Regret}(T) = \sum_{t=0}^{T-1}(V^*(S_t) - R_t)$

### Theoretical Considerations

**Key theoretical results:**
- **Sufficiency of Markovian policies:** For MDPs, the current state is a sufficient statistic—optimal policies need only depend on current state, not full history
- **Deterministic optimality:** While policies can be stochastic, a deterministic optimal policy always exists
- **Existence of optimal policies:** Under regularity conditions (continuous bounded rewards, continuous transitions, compact action spaces), measurable optimal policies are guaranteed to exist

**Simplifying assumptions** commonly made to avoid measure-theoretic complexity:
1. **Finitude:** State and action spaces are finite
2. **Full observability:** Agent has direct access to current state

# The Three Domains of Reinforcement Learning

The field can be conceptualized as three overlapping domains addressing different aspects of sequential decision-making:

![Venn diagram](https://raw.githubusercontent.com/13ryanC/13ryanC.github.io/main/content/posts/RLtheory/images/venn_diagram.png)

### 1. Planning (Model-Based Control)

**Setting:** Known transition kernel $P(s' \mid s,a)$ and reward function $R(s,a)$

**Objective:** Determine optimal actions without further environment interaction

**Key approaches:**
- **Dynamic programming:** Solving Bellman optimality equation for closed-loop optimal policy
- **Trajectory optimization:** Open-loop optimization of action sequences $(a_{0:H-1})$ ignoring feedback during execution  
- **Online search:** Look-ahead methods (e.g., MCTS, AlphaZero) that replan at each step under computational constraints

**Computational complexity:** Even with perfect models, exact planning is computationally hard (P-complete for finite MDPs; PSPACE-hard for POMDPs).

### 2. Batch (Offline) RL

**Setting:** Static dataset $\mathcal{D} = \{(s_i, a_i, r_i, s'_i)\}$ from unknown behavior policy $\mu$, with no further interaction allowed

**Core challenge:** **Extrapolation error** - learned policy $\pi$ may query state-action pairs outside $\mu$'s support

**Solution approaches:**
- **Behavioral constraints:** Constraining $\pi$ near $\mu$ (behavior cloning, KL penalties)
- **Pessimistic value estimation:** Learning conservative value functions with uncertainty penalties (Conservative Q-Learning)
- **Importance sampling:** Density-ratio estimation for off-policy correction

### 3. Online RL (Interactive Learning)

**Protocol:** At each time-step $t = 0, 1, \ldots$:
1. Agent observes state $s_t$
2. Chooses action $a_t \sim \pi_t(\cdot \mid H_t)$ 
3. Environment yields reward $r_t$ and next state $s_{t+1}$
4. Agent updates parameters, producing $\pi_{t+1}$

**Central challenge:** **Exploration-exploitation trade-off** - gathering informative data while maximizing reward

**Exploration strategies:**
- **Random exploration:** ε-greedy, Boltzmann exploration
- **Optimism under uncertainty:** UCB, RLSVI
- **Posterior sampling:** Thompson sampling, PSRL

**Learning paradigms:**
- **On-policy:** Updates use current policy data (e.g., PPO)
- **Off-policy:** Reuses past trajectories with importance sampling corrections (e.g., Q-learning, DDPG)

## The Central Challenge: Learning Under Uncertainty

The fundamental RL problem: *How can an agent learn an optimal policy when transition dynamics $P$ and rewards $R$ are unknown?*

This necessitates **exploration**—sometimes sacrificing immediate reward to gather information for future exploitation. The theoretical limit is captured by the **identifiability barrier**:

> **Identifiability Barrier**
> 
> If two MDPs differ only in $P(\cdot \mid s,a)$ for some state-action pair $(s,a)$, any algorithm avoiding $(s,a)$ with probability 1 produces identical trajectories in both environments and cannot be simultaneously optimal.

Success is measured by how efficiently agents balance exploration and exploitation across diverse environments, guided only by self-generated trajectory data.

### Extensions and Alternative Frameworks

**Common MDP extensions:**

| Framework | Key Distinction | New Challenges |
|-----------|-----------------|----------------|
| **POMDP** | Partial observability via $O(o \mid s)$ | Belief-state explosion; intractable control |
| **Semi-MDP** | Actions with variable duration | Temporal abstraction; hierarchical planning |
| **Multi-agent MDP** | Multiple decision-makers | Coupled rewards; game-theoretic considerations |
| **CMDP** | Constrained optimization | Feasible-set identification; dual learning |
| **Multi-objective RL** | Vector-valued rewards | Preference elicitation; Pareto optimality |

Each framework preserves the core state → action → reward structure while addressing specific real-world complexities.

## References

* RL Theory. (2021, January 19). *Lecture 1 (2021-01-12)* [Video]. YouTube. [http://www.youtube.com/watch?v=0oJmSULoj3I](http://www.youtube.com/watch?v=0oJmSULoj3I)
* RL Theory. (2022, January 9). *Lecture 1 (2022-01-05)* [Video]. YouTube. [http://www.youtube.com/watch?v=rjwxqcVrVws](http://www.youtube.com/watch?v=rjwxqcVrVws)
* RL Theory. (2025, February 5). *The fundamental theorem* [Lecture notes]. [https://rltheory.github.io/w2021-lecture-notes/planning-in-mdps/lec2/](https://rltheory.github.io/w2021-lecture-notes/planning-in-mdps/lec2/)
* RL Theory. (2025, February 5). *Introductions* [Lecture notes]. [https://rltheory.github.io/lecture-notes/planning-in-mdps/lec1/](https://rltheory.github.io/lecture-notes/planning-in-mdps/lec1/)
* Jiang, N. (2024, September 27). *MDP preliminaries* [Lecture notes]. [https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf)
