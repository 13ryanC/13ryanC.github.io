# A Complete Guide to Probability Theory and Markov Decision Processes

## Table of Contents
1. [Foundational Concepts](#foundational-concepts)
2. [Unified Probability Framework](#unified-probability-framework)
3. [Markov Decision Processes: Complete Foundation](#markov-decision-processes-complete-foundation)
4. [Understanding Discounting and Time Horizons](#understanding-discounting-and-time-horizons)
5. [Policies and the Agent-Environment Loop](#policies-and-the-agent-environment-loop)

---

## Foundational Concepts

Before diving into the advanced material, let's establish the mathematical foundation with clear explanations of key concepts.

### What is a Set?
A **set** is simply a collection of objects. For example:
- \(S = \{1, 2, 3\}\) is a set containing three numbers
- \(A = \{\text{left, right, stay}\}\) is a set containing three actions

### What is a Function?
A **function** \(f: X \to Y\) is a rule that assigns to each element \(x\) in set \(X\) exactly one element \(f(x)\) in set \(Y\).

Example: If \(X = \{1, 2, 3\}\) and \(Y = \{a, b\}\), then \(f(1) = a, f(2) = b, f(3) = a\) defines a function.

### What is Probability?
**Probability** measures how likely events are to occur, always between 0 (impossible) and 1 (certain).

### What is a Random Variable?
A **random variable** is not actually a variable—it's a function that assigns numbers to the outcomes of a random experiment.

Example: When rolling a die, we can define \(X\) as "the number showing on the die." Here \(X\) can take values 1, 2, 3, 4, 5, or 6, each with probability 1/6.

### What is Expected Value?
The **expected value** (or expectation) of a random variable is its long-run average value. For a discrete random variable:
$$\mathbb{E}[X] = \sum_{x} x \cdot P(X = x)$$

Example: For a fair die, \(\mathbb{E}[X] = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + \cdots + 6 \cdot \frac{1}{6} = 3.5\)

### What is a Markov Chain?
A **Markov chain** is a sequence of random states where the next state depends only on the current state, not on the history of how we got there.

Example: Weather prediction where tomorrow's weather depends only on today's weather, not on yesterday's.

---

## 1. Unified Probability Framework

### 1.1 Core Structure: Building Blocks of Probability

To work with probability rigorously, we need three components:

#### Probability Space
A **probability space** \((\Omega, \mathcal{F}, P)\) consists of:

1. **Sample space** \(\Omega\): The set of all possible outcomes
   - Example: When flipping a coin, \(\Omega = \{\text{heads, tails}\}\)

2. **Event space** \(\mathcal{F}\): A collection of events (subsets of \(\Omega\)) that we can assign probabilities to
   - Example: \(\mathcal{F} = \{\emptyset, \{\text{heads}\}, \{\text{tails}\}, \{\text{heads, tails}\}\}\)

3. **Probability measure** \(P\): A function that assigns probabilities to events
   - Example: \(P(\{\text{heads}\}) = 0.5\), \(P(\{\text{tails}\}) = 0.5\)

**Key requirement:** \(P(\Omega) = 1\) (something must happen)

#### What is a σ-algebra?
A **σ-algebra** (sigma-algebra) \(\mathcal{F}\) is a special collection of subsets that includes:
- The empty set \(\emptyset\)
- The whole space \(\Omega\)  
- Complements of any set in the collection
- Countable unions of sets in the collection

*Why do we need this?* It ensures we can consistently assign probabilities to all events we care about.

#### Random Variables: Connecting Outcomes to Numbers
A **random variable** \(X\) is a function \(X: \Omega \to \mathbb{R}\) that assigns a real number to each outcome.

**Measurability requirement:** We need \(X\) to be **measurable**, meaning we can compute probabilities for events like \(\{X \leq a\}\).

### 1.2 Universal Distribution Theory via Push-Forward Measures

#### What is a Push-Forward Measure?
When we have a random variable \(X\), its **push-forward measure** (also called the **law** or **distribution** of \(X\)) tells us the probability that \(X\) takes values in any given set.

**Mathematical definition:**
$$\boxed{P_X := X_* P}, \quad P_X(B) := P(X^{-1}(B))$$

**Plain English:** \(P_X(B)\) is the probability that \(X\) lands in set \(B\).

#### This Single Framework Handles All Distribution Types:

1. **Discrete distributions** (random variable takes countable values):
   - \(p_X(x) = P_X(\{x\}) = P(X = x)\)
   - Example: Rolling a die, \(p_X(3) = 1/6\)

2. **Continuous distributions** (random variable takes uncountable values):
   - \(P_X(B) = \int_B f_X(y) \, dy\) where \(f_X\) is the probability density function
   - Example: Height of randomly selected person

3. **Mixed distributions** (combination of discrete and continuous):
   - Handled automatically by the push-forward measure framework

### 1.3 Generating Functions: Powerful Tools for Analysis

#### What are Generating Functions?
A **generating function** is a mathematical tool that encodes all the information about a random variable in a single function.

**General form:**
$$G_X(\theta) := \mathbb{E}[g_\theta(X)] = \int g_\theta(x) \, P_X(dx)$$

where \(g_\theta\) is a **kernel function** that depends on parameter \(\theta\).

#### Three Important Types:

| Type | Kernel \(g_\theta(x)\) | What it recovers | When to use |
|------|---------------------|------------------|-------------|
| **Probability generating function** | \(s^x\) | Probabilities: \(P(X = k) = \frac{1}{k!} \frac{d^k G_X}{ds^k}(0)\) | Discrete random variables |
| **Moment generating function** | \(e^{tx}\) | Moments: \(\mathbb{E}[X^n] = \frac{d^n G_X}{dt^n}(0)\) | Finding means, variances |
| **Characteristic function** | \(e^{itx}\) | Complete distribution via inversion | Most general, always exists |

**Example:** For a coin flip (\(X = 1\) for heads, \(X = 0\) for tails):
- Probability generating function: \(G_X(s) = 0.5 \cdot s^0 + 0.5 \cdot s^1 = 0.5 + 0.5s\)
- From this: \(P(X = 0) = G_X(0) = 0.5\), \(P(X = 1) = G_X'(0) = 0.5\)

### 1.4 Martingales: Modeling Fair Games

#### What is a Filtration?
A **filtration** \((\mathcal{F}_t)_{t \geq 0}\) represents the information available at each time \(t\). It's a sequence of σ-algebras where \(\mathcal{F}_s \subseteq \mathcal{F}_t\) for \(s \leq t\).

**Intuition:** As time progresses, we gain more information, never less.

#### What is a Martingale?
A **martingale** is a sequence of random variables \((X_t)\) representing a "fair game" where:
$$\mathbb{E}[X_t \mid \mathcal{F}_s] = X_s \quad \text{for all } s \leq t$$

**Plain English:** Given what you know now, your expected future value equals your current value.

**Example:** Your total winnings in a fair casino game form a martingale.

---

## 2. Markov Decision Processes: Complete Foundation

### 2.1 What is a Markov Decision Process?

A **Markov Decision Process (MDP)** is a mathematical framework for modeling decision-making in situations where:
- Outcomes are partly random and partly under the control of a decision maker
- The current state fully determines the probabilities of future states (Markov property)

**Real-world examples:**
- Robot navigation: states are locations, actions are movements
- Investment decisions: states are portfolio values, actions are buy/sell decisions
- Game playing: states are board positions, actions are moves

### 2.2 MDP Components Explained

An MDP consists of five components: \(M = (S, A, P, r, \gamma)\)

#### States (\(S\))
The **state space** \(S\) contains all possible situations the system can be in.
- **Finite case:** \(S = \{s_1, s_2, \ldots, s_n\}\) (what we'll focus on)
- **Example:** In a grid world, \(S = \{(1,1), (1,2), \ldots, (5,5)\}\)

#### Actions (\(A\))
The **action space** \(A\) contains all possible decisions.
- **Finite case:** \(A = \{a_1, a_2, \ldots, a_m\}\)
- **Example:** In robot navigation, \(A = \{\text{up, down, left, right}\}\)

#### Transition Probabilities (\(P\))
The **transition kernel** \(P\) specifies how actions change states:
$$P_a(s, s') = \text{Probability of moving from state } s \text{ to state } s' \text{ when taking action } a$$

**Key property:** \(\sum_{s' \in S} P_a(s, s') = 1\) for all \(s, a\) (probabilities sum to 1)

#### Rewards (\(r\))
The **reward function** \(r_a(s)\) gives the immediate reward for taking action \(a\) in state \(s\).
- **Bounded assumption:** \(|r_a(s)| \leq R_{\max}\) for some finite \(R_{\max}\)
- **Example:** +10 for reaching goal, -1 for each step, -100 for hitting obstacle

#### Discount Factor (\(\gamma\))
The **discount factor** \(\gamma \in [0, 1)\) determines how much future rewards matter:
- \(\gamma = 0\): Only immediate rewards matter
- \(\gamma\) close to 1: Future rewards nearly as important as immediate ones

### 2.3 Measurable Space Construction: The Mathematical Foundation

#### Why Do We Need Measure Theory?

To rigorously define probabilities and expectations, we need measurable spaces.

**For finite sets:** This is straightforward
- State space: \(S\) with **power set** \(\mathcal{S} = 2^S\) (all possible subsets)
- Action space: \(A\) with power set \(\mathcal{A} = 2^A\)

#### Trajectory Space
The **trajectory space** \(T\) contains all possible infinite sequences of states and actions:
$$T = (S \times A)^{\mathbb{N}} = \{(s_0, a_0, s_1, a_1, s_2, a_2, \ldots)\}$$

**Coordinate maps:** For any trajectory \(\tau = (s_0, a_0, s_1, a_1, \ldots)\):
- \(S_t(\tau) = s_t\) (state at time \(t\))
- \(A_t(\tau) = a_t\) (action at time \(t\))

#### Information Structure: What We Know When
The **history filtration** captures the information available at each time:
$$\mathcal{F}_t = \sigma(S_0, A_0, \ldots, S_t)$$

**Plain English:** \(\mathcal{F}_t\) contains exactly the information observable after seeing state \(S_t\) but before choosing action \(A_t\).

### 2.4 The Trajectory Measure: Making Probability Precise

#### The Challenge
Given an MDP and a policy (decision rule), what is the probability of any particular trajectory?

#### The Solution: Ionescu-Tulcea Theorem

**Theorem:** For every initial distribution \(\mu\), policy \(\pi\), and MDP transition kernel \(P\), there exists a unique probability measure \(\mathbb{P}_\mu^\pi\) on the trajectory space such that:

1. **Initial condition:** \(\mathbb{P}_\mu^\pi(S_0 = s) = \mu(s)\)
2. **Policy condition:** \(\mathbb{P}_\mu^\pi(A_t = a \mid \mathcal{F}_t) = \pi_t(a \mid H_t)\)
3. **Markov transition:** \(\mathbb{P}_\mu^\pi(S_{t+1} = s' \mid \mathcal{F}_t, A_t) = P_{A_t}(S_t, s')\)

**What this means:** We can compute the probability of any trajectory or any event about trajectories in a unique, well-defined way.

#### Canonical Probability Space
We can identify our abstract probability space with the trajectory space itself. This means:
- Every random variable becomes a coordinate function
- All expectations and probabilities are uniquely determined
- We can work directly with trajectories

### 2.5 Stationary Policies: Simplifying the Framework

#### What is a Stationary Policy?
A **stationary policy** \(\pi\) makes decisions based only on the current state:
$$\pi(a \mid s) = \text{Probability of taking action } a \text{ in state } s$$

**Key insight:** The policy doesn't change over time and doesn't depend on history.

#### Policy-Averaged Quantities
For a stationary policy, we can compute averaged versions of rewards and transitions:

**Average reward:**
$$r^\pi(s) = \sum_{a \in A} \pi(a \mid s) r_a(s)$$

**Average transition probabilities:**
$$P^\pi(s, s') = \sum_{a \in A} \pi(a \mid s) P_a(s, s')$$

#### The Value Function
The **value function** \(v^\pi(s)\) gives the expected total discounted reward starting from state \(s\):
$$v^\pi(s) = \mathbb{E}_s^\pi\left[\sum_{t=0}^{\infty} \gamma^t r_{A_t}(S_t)\right]$$

**Bellman equation:** The value function satisfies:
$$v^\pi(s) = r^\pi(s) + \gamma \sum_{s'} P^\pi(s, s') v^\pi(s')$$

**Matrix form:** \(v^\pi = r^\pi + \gamma P^\pi v^\pi\)

**Solution:** \(v^\pi = (I - \gamma P^\pi)^{-1} r^\pi\)

*Why does this work?* The matrix \((I - \gamma P^\pi)\) is invertible because \(\gamma < 1\).

### 2.6 The Markov Property: The Key Assumption

The **Markov property** states that the future depends only on the present, not on the past:
$$\mathbb{P}(S_{t+1} = s' \mid S_0, A_0, \ldots, S_t, A_t) = \mathbb{P}(S_{t+1} = s' \mid S_t, A_t)$$

**This is the fundamental assumption that makes MDPs tractable.**

### 2.7 Extensions and Generalizations

| Variant | Key Change | When to Use |
|---------|------------|-------------|
| **Finite-horizon MDP** | Stop after \(H\) steps, \(\gamma = 1\) | Games with known end time |
| **Average-reward MDP** | Optimize long-run average reward | Steady-state systems |
| **Countable state/action spaces** | Infinite but countable sets | Queueing systems |
| **Continuous spaces** | Uncountable state/action spaces | Robotics, finance |

---

## 3. Understanding Discounting and Time Horizons

### 3.1 Why Do We Discount Future Rewards?

#### Economic Intuition
- **Time preference:** \(1 today is worth more than \)1 tomorrow
- **Uncertainty:** Future rewards are less certain
- **Opportunity cost:** Money today can be invested

#### Mathematical Benefits
- **Convergence:** Infinite sums become finite
- **Contraction:** Algorithms converge faster
- **Stability:** Numerical computations are more stable

### 3.2 The Discounted Return: Mathematical Foundation

#### Definition
For any trajectory \(\tau = (s_0, a_0, s_1, a_1, \ldots)\):
$$R(\tau) = \sum_{t=0}^{\infty} \gamma^t r_{A_t}(S_t)$$

#### Key Properties

**Boundedness:** Since rewards are bounded by \(R_{\max}\):
$$|R(\tau)| \leq R_{\max} \sum_{t=0}^{\infty} \gamma^t = \frac{R_{\max}}{1-\gamma}$$

**Measurability:** \(R(\tau)\) is a well-defined random variable.

**Integrability:** Expected values always exist and are finite.

### 3.3 Effective Horizon: When Can We Stop Planning?

#### The Tail Problem
After many time steps, discounted rewards become negligible. The **tail remainder** after horizon \(H\) is:
$$\text{Tail}_H(\tau) = \sum_{t=H}^{\infty} \gamma^t r_{A_t}(S_t)$$

#### Uniform Bound
The tail is bounded by:
$$|\text{Tail}_H(\tau)| \leq \frac{\gamma^H R_{\max}}{1-\gamma}$$

#### Effective Horizon Formula
For error tolerance \(\varepsilon\), the **effective horizon** is:
$$H_{\gamma,\varepsilon} = \left\lceil \frac{\ln(1/(\varepsilon(1-\gamma)))}{1-\gamma} \right\rceil$$

**Rule of thumb:** \(H_{\text{effective}} \approx \frac{1}{1-\gamma}\)

### 3.4 Practical Guidelines for Choosing \(\gamma\)

#### Task-Based Selection

**Known task duration:** If the task naturally ends after \(H\) steps:
$$\gamma \approx 1 - \frac{1}{H}$$

**Unknown duration:** Common choices:
- \(\gamma = 0.9\): Effective horizon ≈ 10 steps
- \(\gamma = 0.99\): Effective horizon ≈ 100 steps
- \(\gamma = 0.999\): Effective horizon ≈ 1000 steps

#### Domain-Specific Recommendations

| Domain | Typical \(\gamma\) | Reasoning |
|--------|------------------|-----------|
| **Robotics** | 0.99 | Smooth control, long horizons |
| **Games** | 0.95 or finite horizon | Clear episode structure |
| **Finance** | \(e^{-r \Delta t}\) | Based on interest rates |
| **Navigation** | 0.9-0.99 | Depends on path length |

### 3.5 Comparing Different Objective Functions

| Objective | Formula | Pros | Cons | Best For |
|-----------|---------|------|------|----------|
| **Discounted** | \(\sum_{t=0}^{\infty} \gamma^t r_t\) | • Always converges<br>• Fast algorithms<br>• Stable numerics | • Introduces bias<br>• Parameter tuning | Most RL problems |
| **Finite-horizon** | \(\sum_{t=0}^{H-1} r_t\) | • No discount bias<br>• Natural for episodes | • Need known horizon<br>• Harder algorithms | Games, robotics |
| **Average reward** | \(\lim_{T \to \infty} \frac{1}{T}\sum_{t=0}^{T-1} r_t\) | • Scale-invariant<br>• Long-term optimal | • Requires ergodicity<br>• Slow convergence | Steady-state control |

---

## 4. Policies and the Agent-Environment Loop

### 4.1 What is a Policy?

A **policy** is a decision-making rule that tells an agent what action to take in each situation.

#### Types of Policies

**History-dependent policy:** Decisions can depend on the entire history of states and actions.
$$\pi = (\pi_0, \pi_1, \pi_2, \ldots)$$
where \(\pi_t\) maps histories of length \(t\) to probability distributions over actions.

**Stationary policy:** Decisions depend only on the current state.
$$\pi: S \to \Delta(A)$$
where \(\Delta(A)\) is the set of probability distributions over actions.

**Deterministic policy:** Always chooses the same action in each state.
$$\pi(s) = a \text{ (single action, not a distribution)}$$

#### History Spaces
At time \(t\), the **history space** is:
$$\mathsf{H}_t = (S \times A)^t \times S$$

**Example:** At \(t = 1\), a history looks like \((s_0, a_0, s_1)\).

### 4.2 The Agent-Environment Loop

#### The Interaction Protocol
The agent and environment interact through the following sequence:

1. **Environment provides initial state:** \(S_0 \sim \mu\) (initial distribution)
2. **Agent chooses action:** \(A_t \sim \pi_t(\cdot \mid H_t)\) (based on history)
3. **Environment responds:** \(S_{t+1} \sim P_{A_t}(S_t, \cdot)\) (Markov transition)
4. **Agent receives reward:** \(r_{A_t}(S_t)\)
5. **Repeat from step 2**

#### Mathematical Formulation
$$\boxed{\begin{aligned}
& S_0 \sim \mu \\
& A_t \mid \mathcal{H}_t \sim \pi_t(\cdot \mid H_t) \\
& S_{t+1} \mid \mathcal{H}_t, A_t \sim P_{A_t}(S_t, \cdot)
\end{aligned}}$$

### 4.3 Trajectory Measures: Making Everything Precise

#### The Fundamental Theorem
**Ionescu-Tulcea Theorem:** For every initial distribution \(\mu\), policy \(\pi\), and MDP \(M\), there exists a unique probability measure \(\mathbb{P}_\mu^\pi\) on the space of all trajectories.

**What this means:** We can compute probabilities and expectations for any trajectory-based event in a unique, well-defined way.

#### Canonical Probability Space
We work directly with the trajectory space \(T = (S \times A)^{\mathbb{N}}\):
- Each trajectory \(\tau = (s_0, a_0, s_1, a_1, \ldots)\) is a point in \(T\)
- Random variables are coordinate functions: \(S_t(\tau) = s_t\), \(A_t(\tau) = a_t\)
- All randomness is captured by the measure \(\mathbb{P}_\mu^\pi\)

### 4.4 Stationary Policies and Markov Chains

#### Induced Markov Chain
Under a stationary policy \(\pi\), the state sequence \((S_t)\) forms a Markov chain with:

**Transition probabilities:**
$$P^\pi(s, s') = \sum_{a \in A} \pi(a \mid s) P_a(s, s')$$

**Reward function:**
$$r^\pi(s) = \sum_{a \in A} \pi(a \mid s) r_a(s)$$

#### Why This Matters
- **Simplification:** Instead of tracking full histories, we only need current states
- **Analysis:** We can use Markov chain theory to analyze long-term behavior
- **Computation:** Value functions satisfy simple linear equations

### 4.5 Value Functions: Evaluating Policies

#### State Value Function
The **state value function** gives the expected total discounted reward starting from state \(s\):
$$v^\pi(s) = \mathbb{E}_s^\pi\left[\sum_{t=0}^{\infty} \gamma^t r_{A_t}(S_t)\right]$$

#### Action Value Function
The **action value function** gives the expected total discounted reward starting from state \(s\) and taking action \(a\):
$$q^\pi(s, a) = \mathbb{E}_s^\pi\left[\sum_{t=0}^{\infty} \gamma^t r_{A_t}(S_t) \mid A_0 = a\right]$$

#### Bellman Equations
These functions satisfy recursive relationships:

**State value:** \(v^\pi(s) = \sum_a \pi(a \mid s) q^\pi(s, a)\)

**Action value:** \(q^\pi(s, a) = r_a(s) + \gamma \sum_{s'} P_a(s, s') v^\pi(s')\)

### 4.6 Policy Evaluation: Computing Value Functions

#### Matrix Formulation
For a stationary policy, the value function satisfies:
$$v^\pi = r^\pi + \gamma P^\pi v^\pi$$

#### Solving the Linear System
**Direct solution:** \(v^\pi = (I - \gamma P^\pi)^{-1} r^\pi\)

**Iterative solution (Value iteration):**
1. Start with \(v^{(0)} = 0\)
2. Update: \(v^{(k+1)} = r^\pi + \gamma P^\pi v^{(k)}\)
3. Repeat until convergence

**Why it works:** The operator \(T^\pi v = r^\pi + \gamma P^\pi v\) is a contraction with factor \(\gamma < 1\).

### 4.7 Notation and Conventions

#### Expectation Notation
- \(\mathbb{E}_\mu^\pi[\cdot]\): Expected value under policy \(\pi\) starting from distribution \(\mu\)
- \(\mathbb{E}_s^\pi[\cdot]\): Expected value under policy \(\pi\) starting from state \(s\)
- \(\mathbb{P}_\mu^\pi[\cdot]\): Probability under policy \(\pi\) starting from distribution \(\mu\)

#### Why These Notations Matter
- **Precision:** Each notation specifies exactly which probability measure we're using
- **Clarity:** We can distinguish between different policies and initial conditions
- **Rigor:** All expectations are well-defined because the trajectory measure exists and is unique

---

## Summary and Key Takeaways

### The Big Picture
This guide has taken you through the mathematical foundations of probability theory and Markov Decision Processes. Here's what we've covered:

1. **Probability foundations:** Sample spaces, random variables, and distributions
2. **MDP structure:** States, actions, transitions, rewards, and policies
3. **Measure theory:** Why we need it and how it ensures everything is well-defined
4. **Discounting:** How to handle infinite time horizons practically
5. **Policies:** How agents make decisions and how to evaluate them

### Key Insights

**Everything is well-defined:** The measure-theoretic framework ensures that all probabilities and expectations have unique, unambiguous meanings.

**Markov property is crucial:** The assumption that the future depends only on the present (not the past) makes MDPs tractable.

**Discounting serves multiple purposes:** It ensures convergence, reflects time preferences, and enables practical algorithms.

**Policies can be complex:** While stationary policies are often sufficient, the framework supports arbitrary history-dependent decision rules.

### Next Steps
With this foundation, you're ready to explore:
- Dynamic programming and optimal control
- Reinforcement learning algorithms
- Stochastic optimal control
- Advanced topics in decision theory

The mathematical rigor developed here provides the solid foundation needed for all advanced work in sequential decision making under uncertainty.
