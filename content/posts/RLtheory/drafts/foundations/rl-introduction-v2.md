---
date: "2025-07-03"
title: "(Part 1) MDP Foundations nad Optimality"
summary: "MDP Foundations and Optimality"
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

## 0. Foundational Concepts

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
$$\boxed{P_X := X \circ P}, \quad P_X(B) := P(X^{-1}(B))$$

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
$$\boxed{P_X := X_* P}, \quad P_X(B) := P(X^{-1}(B)), \quad B \in \mathcal{E}$$

This single construction handles all distribution types:
- **Discrete:** \(p_X(x) = P_X(\{x\}) = P(X = x)\) for countable \(E\)
- **Continuous:** \(P_X(B) = \int_B f_X(y) \, d\lambda(y)\) when absolutely continuous
- **Mixed/singular:** Automatic via Lebesgue decomposition

## 1 Push‑forward (a.k.a. “law”, “distribution”) of a random variable

### 1.1 Formal set‑up

* Measurable spaces

  $$
    (\Omega,\mathcal F)\quad\text{and}\quad(E,\mathcal E),
  $$

  a probability measure \(P\) on \((\Omega,\mathcal F)\), and a **measurable map**

  $$
     X:(\Omega,\mathcal F)\;\longrightarrow\;(E,\mathcal E).
  $$

* **Definition (push‑forward).**

  $$
    \boxed{\;P_X := X_*P\;}
    \quad\Longleftrightarrow\quad
    P_X(B)=P\bigl(X^{-1}(B)\bigr),\qquad B\in\mathcal E.
  $$

* **Key properties**

| Property               | Meaning                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------- |
| Measure on destination | \(P_X\) is a probability measure on \((E,\mathcal E)\).                                               |
| Uniqueness             | If \(Y\) has the same \(P_Y=P_X\) then \(X\) and \(Y\) are *identically distributed*.                     |
| Expectation transfer   | For any integrable \(g:E\to\mathbb R\):  \(\displaystyle\int_\Omega g\!\circ\!X\,dP=\int_E g\,dP_X.\) |

> **Mnemonic:**  “Push the measure \(P\) **forward** through the map \(X\).”

### 1.2 Why the concept is universal

Because *only measurability* is required, the construction works whether \(E\) is

* finite or countably infinite → **discrete** distributions,
* \(\mathbb R^n\) with Borel σ‑field → **continuous** densities,
* Cantor set, fractal, or hybrid → **singular / mixed** cases.

No extra rules have to be invented—the push‑forward covers everything.

### 1.3 How discrete, continuous, and mixed appear naturally

* **Discrete:**  If \(E\) is countable, \(\mathcal E=2^E\),

  $$
    p_X(x):=P_X(\{x\})=P(X=x)
  $$

  is a probability mass function (PMF).

* **Absolutely continuous:**  If \(P_X\ll\lambda\) (Lebesgue measure) then there exists a density \(f_X\) such that

  $$
     P_X(B)=\int_B f_X(y)\,d\lambda(y).
  $$

* **Mixed / singular:**  By the **Lebesgue decomposition theorem** every \(P_X\) on \(\mathbb R\) splits uniquely into

  $$
      P_X = P^{\text{disc}} + P^{\text{cont}}_{\text{dens}} + P^{\text{sing}},
  $$

  each part being generated by the *same* push‑forward formula.

Hence the single line \(P_X=X_*P\) is a universal definition.

### 1.3 Generating Functions as Integral Transforms

For random variable \(X\) with law \(\mu = P_X\) and kernel family \(g_\theta: E \to \mathbb{C}\):
$$G_X(\theta) := \int_E g_\theta(x) \, \mu(dx) = \mathbb{E}[g_\theta(X)]$$

| Transform | Kernel \(g_\theta(x)\) | Domain | Recovers |
|-----------|---------------------|---------|----------|
| **Probability generating** | \(s^x\) | \(\|s\| \leq 1\) | PMF via \(\mu(\{k\}) = \frac{1}{k!} G_X^{(k)}(0)\) |
| **Moment generating** | \(e^{tx}\) | \(t \in \mathcal{D}_M\) | Moments via \(\mathbb{E}[X^n] = M_X^{(n)}(0)\) |
| **Characteristic** | \(e^{itx}\) | \(t \in \mathbb{R}\) | Full distribution via inversion |

## 2 Integral transforms (“generating functions”)

### 2.1 Generic template

Given \(X:\Omega\to E\) with law \(\mu=P_X\) and a **kernel family**

$$
    g_\theta:E\to\mathbb C,\qquad\theta\in\Theta,
$$

define

$$
    \boxed{\;G_X(\theta)
           :=\mathbb E\bigl[g_\theta(X)\bigr]
           =\int_E g_\theta(x)\,\mu(dx)\;}
$$

*Interpretation:* \(G_X\) packages the entire distribution into a function of the parameter \(\theta\).
Different choices of \(g_\theta\) give the classical transforms:

| Name                         | Kernel \(g_\theta(x)\)    | Typical domain                     | Recover                             |       |                                          |
| ---------------------------- | ----------------------- | ---------------------------------- | ----------------------------------- | ----- | ---------------------------------------- |
| Probability generating (PGF) | \(s^{\,x}\) (integer \(x\)) | (                                  | s                                   | \le1) | PMF by \(p_X(k)=\frac{1}{k!}G_X^{(k)}(0)\) |
| Moment generating (MGF)      | \(e^{tx}\)                | open set around \(t=0\) where finite | All integer moments via derivatives |       |                                          |
| Characteristic function (CF) | \(e^{itx}\)               | \(t\in\mathbb R\) (always finite, (  | e^{itx}                             | =1))  | Full law via Fourier inversion           |

> **Why these work:**  In each case \(g_\theta\) is chosen so that differentiation (or inversion) with respect to \(\theta\) isolates coefficients that encode the distribution.

### 2.2 Examples quick check

| Distribution \(X\)         | PGF / MGF / CF closed form                          |
| ------------------------ | --------------------------------------------------- |
| Poisson(\(\lambda\))       | PGF: \(\exp\bigl[\lambda(s-1)\bigr]\)                 |
| Gaussian(\(\mu,\sigma^2\)) | MGF: \(\exp\bigl[\mu t + \tfrac12\sigma^2 t^2\bigr]\) |
| Bernoulli(\(p\))           | CF: \(1-p+pe^{it}\) (shows atoms explicitly)          |

Each result follows straight from the integral definition.

### 1.4 Martingales and Information Flow

A **filtration** \((\mathcal F_t)_{t \in T}\) satisfies \(\mathcal F_s \subseteq \mathcal F_t \subseteq \mathcal F\) for \(s \leq t\).

An adapted process \((X_t)\) with \(X_t \in L^1\) is a **martingale** if \(\mathbb{E}[X_t \mid \mathcal{F}_s] = X_s\) a.s. for all \(s \leq t\).

## 3 Martingales and filtrations (information flow)

### 3.1 Filtration recap

A **filtration** \((\mathcal F_t)_{t\in T}\) is an *increasing* family of σ‑fields:

$$
   \mathcal F_s\subseteq\mathcal F_t\subseteq\mathcal F,\qquad s\le t.
$$

Intuitively: the σ‑field at later time can only reveal *more* events, never fewer.

### 3.2 Martingale definition

Let \(X_t\) be an adapted process, i.e. \(X_t\) is \(\mathcal F_t\)-measurable for each \(t\).
If \(\mathbb E[|X_t|]<\infty\) and

$$
   \boxed{\;
   \mathbb E[X_t\mid\mathcal F_s]=X_s\quad\text{a.s.}\;
   }\qquad(s\le t),
$$

then \((X_t)\) is a **martingale**.

*The slogan:* *“Future conditional expectation equals present value.”*

### 3.3 Why martingales matter

| Feature                     | Consequence                                                                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| *Fair game* property        | Captures “no drift” phenomena (e.g., unbiased estimators, fair betting).                                                                     |
| Optional stopping theorem   | Lets you stop the process at a random time without creating expected profit—crucial for proving validity of stopping rules in RL.            |
| Martingale difference noise | In stochastic‑approximation proofs (e.g. Q‑learning) the update noise forms a martingale difference sequence, enabling convergence theorems. |

### 3.4 Connection to previous “history filtration”

In an MDP or RL environment we often set

$$
   \mathcal F_t:=\sigma(S_0,A_0,\dots,S_t)
$$

(“info known *before* choosing \(A_t\)”).
A value‑function sequence

$$
   V_t := \mathbb E\bigl[\,G_t\mid\mathcal F_t\bigr]
$$

with total return \(G_t=\sum_{k\ge t}\gamma^{k-t}R_{k+1}\) is a **martingale** when rewards are **discounted future cash‑flows**—a key step in dynamic‑programming proofs.


## 2. Markov Decision Processes: Measure-Theoretic Foundation

### 1. Basic Measurable Space Construction

#### 1.1 Fundamental Spaces

For finite sets \(S\) (states) and \(A\) (actions), the measure-theoretic framework requires:

| Symbol | Meaning | Structure |
|--------|---------|-----------|
| \(S\) | Finite state set | Discrete σ-field \(\mathcal{S} = 2^S\) |
| \(A\) | Finite action set | Discrete σ-field \(\mathcal{A} = 2^A\) |
| \(T := (S \times A)^{\mathbb{N}}\) | Trajectory space | Product σ-field \(\mathcal{T} = \bigotimes_{t \geq 0}(\mathcal{S} \otimes \mathcal{A})\) |

**Discrete σ-field:** For any set \(E\), the discrete σ-field on \(E\) is \(2^E\), the set of all subsets of \(E\), which contains \(E\) and \(\varnothing\) and is closed under countable unions and complements because every subset already belongs.

**Why choose the discrete σ-field?** For a finite set this is the coarsest choice that still distinguishes every individual element; there is no loss in generality and calculations become purely combinatorial, probabilities reduce to list of numbers summing to one.

#### 1.2 Single Time-Step Space

Form a single time-step pair: \(\Omega_0 := S \times A\), with σ-field \(\mathcal{F}_0 := \mathcal{S} \otimes \mathcal{A}\).

Because both factors are discrete, thus \(\mathcal{F}_0 = 2^{S \times A}\).

#### 1.3 Trajectory Space Construction

**Infinite Product:**

$$T := (S\times A)^{\mathbb{N}} = \{(s_0,a_0,s_1,a_1,\dots)\mid s_t\in S,\;a_t\in A\;\forall t\ge 0\}$$

**Definition (product σ-field):**

$$\mathcal{T} := \bigotimes_{t\ge0} \mathcal{F}_0$$

is the smallest σ-field making every coordinate projection measurable. Concretely, for **countable** products of **discrete** spaces,

$$\mathcal{T} = \sigma\!\bigl(\{C_t(h_{0:t}) : t\ge0,\;h_{0:t}\in(S\times A)^{t+1}\}\bigr),$$

where \(C_t(h_{0:t})\) are the *cylinder sets* defined below. No topology is needed; measurability hinges entirely on combinatorics.

### 2. Coordinate Process and Cylinder Sets

#### 2.1 Coordinate Process

For \(\tau=(s_0,a_0,s_1,a_1,\dots)\in T\) define

$$S_t(\tau)=s_t, \quad A_t(\tau)=a_t \qquad (t\ge0)$$

**Formal statement:** \(S_t : (T,\mathcal{T})\to(S,\mathcal{S})\) and \(A_t : (T,\mathcal{T})\to(A,\mathcal{A})\) are **measurable** because \(\mathcal{T}\) was constructed precisely to make all projections measurable. Explicitly, for any \(B\in\mathcal{S}\)

$$S_t^{-1}(B)=\{\tau\in T: s_t\in B\}= \bigcup_{h_{0:t}} C_t(h_{0:t})$$

is a countable union of cylinders and hence in \(\mathcal{T}\). The same argument holds for \(A_t\).

**Interpretation:** The pair \(((S_t)_{t\ge0},(A_t)_{t\ge0})\) is the **canonical process** on trajectory space: without having introduced any dynamics (transition laws, policies, etc.), we already have the *observable coordinates* at each time.

#### 2.2 Cylinder Sets

For a finite history \(h_{0:t}=(s_0,a_0,\dots,s_t)\) define the event

$$C_t(h_{0:t}) = \lbrace \tau\in T : (S_0,A_0,\dots,S_t)(\tau)=(s_0,a_0,\dots,s_t) \rbrace$$

**Key properties:**

| Property | Reason |
|----------|---------|
| **Cylinder sets generate \(\mathcal{T}\).** | By definition of the product σ-field; they form a generating π-system. |
| **They are clopen in the product topology** (if one is ever introduced). | Only finitely many coordinates are fixed. |
| **They separate points.** | Any two distinct trajectories first differ at some index \(n\); the corresponding cylinder of length \(n\) contains one but not the other. |

These form a π-system that separates points, ensuring any probability measure on \((T, \mathcal{T})\) is uniquely determined by its values on cylinders.

### 3. Measure Uniqueness Theory

#### 3.1 π-systems and Point Separation

**π-system:** A *π-system* is a collection of sets closed under finite intersections. Cylinders satisfy

$$C_t(h)\cap C_u(g)=\begin{cases}
C_{\max(t,u)}(\text{merged history}) & \text{if }h_{0:t}\text{ and }g_{0:u}\text{ are consistent},\\
\varnothing & \text{otherwise}
\end{cases}$$


1. Clarify the objective: convert the *equality*

$$
C_t(h)\cap C_u(g)=\dots
$$

into an explicit **piecewise‑defined function** whose output is that same intersection.
2. Introduce a function symbol and its domain so the result is unambiguously a function.
3. State the piecewise definition and explain the meaning of each branch and symbol.

---

### Step 1 — Define the function in piecewise form

Let

$$
\Psi:\bigl(\mathcal H\times\mathbb N\bigr)\times\bigl(\mathcal H\times\mathbb N\bigr)\longrightarrow\mathcal P(\Omega),
\qquad
\bigl((h,t),(g,u)\bigr)\longmapsto
\begin{cases}
C_{\max(t,u)}\!\bigl(h\mathbin{\sqcup}g\bigr),
  &\text{if }h_{0:t}\text{ and }g_{0:u}\text{ are **consistent**},\\[6pt]
\varnothing,
  &\text{otherwise}.
\end{cases}
$$

* **Domain**

  * \(\mathcal H\) – set of all admissible partial histories;
  * \(t,u\in\mathbb N\) – their respective cut‑off times.

* **Symbols**

  * \(h_{0:t}\) (resp. \(g_{0:u}\)) – restriction of \(h\) (resp. \(g\)) to the first \(t\) (resp. \(u\)) stages;
  * \(h\sqcup g\) – “merged history,’’ obtained by combining the two prefixes when they are consistent;
  * \(C_k(\cdot)\) – set of completions at horizon \(k\);
  * \(\mathcal P(\Omega)\) – power‑set of the underlying outcome space \(\Omega\).

With this definition the original intersection is simply

$$
C_t(h)\cap C_u(g)\;=\;\Psi\bigl((h,t),(g,u)\bigr),
$$

and \(\Psi\) is manifestly a **piecewise function**: the output is chosen from two disjoint cases determined by the consistency condition.

---

#### Progress

* A single function \(\Psi\) has been introduced and written in canonical piecewise notation, satisfying the request.
* Open issues: none at this stage.

so they form a π-system.

**Point separation:** A π-system \(\mathcal{C}\) **separates points** if for any distinct \(x,y\in T\) there exists \(C\in\mathcal{C}\) with \(x\in C\), \(y\notin C\). This guarantees that a probability measure is *identified* by its values on \(\mathcal{C}\).

#### 3.2 Uniqueness Theorem

By the **π-λ (Dynkin) theorem** (also called the **Monotone Class theorem**):

> *If two probability measures \(\mathbb{P},\mathbb{Q}\) on \((T,\mathcal{T})\) agree on a π-system that generates \(\mathcal{T}\), then \(\mathbb{P}=\mathbb{Q}\).*

Because cylinder sets meet all hypotheses, *specifying the finite-dimensional distributions*

$$\mu_t(h_{0:t}) = \mathbb{P}\bigl(C_t(h_{0:t})\bigr)$$

for every \(t\) and history determines a **unique** probability law on \((T,\mathcal{T})\). This is the countable-product analogue of the Carathéodory extension theorem.

**Application:** Markov decision processes (MDPs), hidden Markov models, and reinforcement-learning environments often define \(\mathbb{P}\) by first stating initial and transition kernels (which give all finite-dimensional probabilities) and then invoke the uniqueness result above to conclude that there exists a single probability space carrying all trajectories.

1. Finite Structure => Discrete \(\sigma\)-fields: Every subset of \(S\) or \(A\) is measurable, so probabilities reduce to finite tables.

2. Infinite horizon => product \(\sigma\)-field: The product \(\sigma\)-field is constructured so projections \((S_t, A_t)\) are measurable; there si no larger \(\sigma\)-field needed for probabilisitc analysis of the canonical process.

3. Cylinder sets => computational handle: They encode finite histories and are sufficient for both defining and computing with probabilities.

4. \(\pi-\lambda\) theorem => unique law: Any probabilities measure is pinned down by its cylinder value,s so you can safety describe an environment by its finite-time beahviour without worrying about inconsistencies at the infinite limit.



| Concept                | Minimal definition used                                                      |
| ---------------------- | ---------------------------------------------------------------------------- |
| σ‑field                | Non‑empty, closed under complement and countable union                       |
| Measurable map         | Pre‑image of any measurable set is measurable                                |
| Product σ‑field        | Smallest σ‑field making all coordinate projections measurable                |
| π‑system               | Non‑empty collection closed under finite intersections                       |
| Dynkin (λ) system      | Contains whole space, closed under complements and countable disjoint unions |
| π‑λ theorem            | π‑system \(\subset\) λ‑system ⇒ generated σ‑fields coincide                    |
| Carathéodory extension | Pre‑measure on an algebra extends uniquely to σ‑field                        |

#### 7 Take‑aways for practitioners

* **Why such heavy machinery for a finite MDP?**
  It pays off when you add *continuous* state features, random episode lengths, or interact with other stochastic processes.  Starting with a measure‑theoretic foundation means later generalisations do not require rewriting proofs.

* **Where to use the canonical process?**
  ‑ To prove existence of optimal policies (dynamic‑programming arguments operate on \(S_t,A_t\)).
  ‑ To define return \(G_t := \sum_{k\ge t}\gamma^{k-t}R_{k+1}\) as a measurable function on \(T\).
  ‑ To study convergence of empirical measures (ergodic theory).

* **What breaks if sets were infinite but non‑measurable?**
  Without σ‑fields that separate points you cannot even *formulate* expected returns or policy gradients rigorously; you would need alternative analytic tools (e.g. outer expectations).

---

#### Summary sentence

The excerpt sets up the space of infinite state–action trajectories as a standard measurable product space, shows that finite‑history cylinder sets generate its σ‑field, and invokes the π‑λ theorem so that any stochastic model is completely characterised by its finite‑dimensional distributions—providing the rigorous backbone for all probability arguments in reinforcement learning and related fields.

### 4. Information Structure and Filtrations

#### 4.1 Timeline and Information Flow

```text
t           t               t+1
| observe S_t | choose A_t | observe S_{t+1} | ...
```

* **Observation phase (left half of each tick):**
  The agent has seen states \$S\_0,\dots,S\_t\$ **but has not yet** committed to the current action \$A\_t\$.

* **Action phase (right half):**
  The control \$A\_t\$ is selected as a *function of what has just been observed*.

The filtration \$(\mathcal{F}\_t)\$ formalizes the “growing information” that is available **just before** each action decision.

#### 4.2 History Filtration

$$
\boxed{\mathcal{F}_t := \sigma\bigl(S_0,A_0,\dots,S_t\bigr)}
$$

**σ‑field generated by variables**

$$
\sigma(X_1,\dots,X_n)
  := \sigma\!\bigl(\{\,X_1^{-1}(B_1)\cap\cdots\cap X_n^{-1}(B_n):  
       B_i\text{ measurable}\,\}\bigr)
$$

Here each \$S\_k\$ (resp. \$A\_k\$) is measured with the discrete σ‑field \$\mathcal{S}\$ (resp. \$\mathcal{A}\$) introduced previously.

Because \$\mathcal{F}*t \subseteq \mathcal{F}*{t+1}\$ (new information accumulates), \$(\mathcal{F}*t)*{t\ge0}\$ is a **filtration**.

#### 4.3 History Process

$$
\boxed{%
  H_t(\omega) :=
    \bigl(S_0(\omega),A_0(\omega),\dots,S_t(\omega)\bigr)
    \in (S\times A)^t \times S}
$$

**Domain / codomain** – Each realisation \$\omega\$ is a trajectory in the canonical space \$T\$.
\$H\_t(\omega)\$ is a *finite list* ending with a **state**, not an **action**.

**Measurability**

$$
H_t : (T,\mathcal{F}_t)
      \longrightarrow
      \bigl((S\times A)^t\times S,\;2^{(S\times A)^t\times S}\bigr)
$$

is \$\mathcal{F}\_t\$‑measurable because it is built from measurable coordinate maps.

### 5. Key Design Principles

#### 5.1 Why \$A\_t\$ is **not** included in \$\mathcal{F}\_t\$

**Decision‑making logic** — at real time \$t\$:

1. The **only random objects already realised** are
   \$S\_0,\dots,S\_t\$ and the earlier actions \$A\_0,\dots,A\_{t-1}\$.
2. The control \$A\_t\$ must be chosen **using those data only**—no clairvoyance.

Hence the *maximal* information set available **before** the choice is

$$
\bigl\{S_0 = s_0,\dots,S_t = s_t,\;
      A_0 = a_0,\dots,A_{t-1} = a_{t-1}\bigr\},
$$

whose σ‑field is precisely \$\mathcal{F}\_t\$.

> **Policy measurability condition**  
> A (possibly stochastic) policy \$\pi\$ is **admissible** iff, for every \$t\$, the prescribed action \$A\_t\$ is *\$\mathcal{F}\_t\$‑measurable*.
> In other words, \$\pi\$ **cannot** depend on future states or chance events.

#### 5.2 Filtration versus Canonical σ‑field

| Symbol             | Contains?                          | Size       | Used for                                       |
| ------------------ | ---------------------------------- | ---------- | ---------------------------------------------- |
| \$\mathcal{T}\$    | *all* trajectory events            | very large | defines probability law                        |
| \$\mathcal{F}\_t\$ | events observable up to time \$t\$ | smaller    | conditioning, martingales, admissible controls |

Every \$\mathcal{F}\_t \subseteq \mathcal{T}\$.
Conditional expectations of returns, value functions, etc. are always taken with respect to \$\mathcal{F}\_t\$ because that matches the agent’s actual knowledge.

---

### 6. Properties and Applications

#### 6.1 Key Properties

1. **Right‑continuity (trivial in discrete time)**
   Since time is discrete, the usual “complete and right‑continuous” convention collapses to
   \$\displaystyle \mathcal{F}*t ;=; \bigcap*{s>t}\mathcal{F}\_s\$ (automatic).

2. **Adaptation of the state process**
   Each \$S\_t\$ is \$\mathcal{F}\_t\$‑measurable by construction, so \$(S\_t)\$ is *adapted*.

3. **Optional sampling / stopping**
   For any stopping time \$\tau\$ (i.e. \${\tau \le t}\in \mathcal{F}*t\$), the stopped history \$H*\tau\$ is \$\mathcal{F}\_\tau\$‑measurable, enabling strong‑Markov proofs.

4. **Predictability of actions**
   Many texts define the *pre‑action* σ‑field
   \$\mathcal{G}*t := \sigma(S\_0,A\_0,\dots,A*{t-1},S\_t)\$ and require \$A\_t\$ to be \$\mathcal{G}\_t\$‑measurable.
   In our notation, \$\mathcal{F}\_t = \mathcal{G}\_t\$.

#### 6.2 Practical Applications

| Task                           | Role of \$\mathcal{F}\_t\$ / \$H\_t\$                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------- |
| **Value‑function definition**  | \$V^\pi\_t := \mathbb{E}^\pi !\bigl\[,G\_t \mid \mathcal{F}\_t\bigr]\$.                 |
| **Policy‑gradient proofs**     | Gradients expressed as expectations of \$\mathcal{F}\_t\$‑measurable score functions.   |
| **Q‑learning convergence**     | Martingale‑difference noise term is \$\mathcal{F}\_t\$‑adapted ⇒ Robbins–Monro applies. |
| **Causal counterfactuals**     | Only interventions measurable w\.r.t. \$\mathcal{F}\_t\$ are admissible.                |
| **Partially observable cases** | Replace \$\mathcal{F}\_t\$ by \$\sigma(O\_0,\dots,O\_t)\$; algebra is identical.        |

---

### 7. Common Misconceptions

* **“Why not include \$A\_t\$ in \$H\_t\$?”**
  Some authors *do* put it in and call the result the *action‑state history*, then set
  \$\mathcal{F}\_t' := \sigma(H\_t, A\_t)\$.
  Nothing breaks mathematically, but conditioning on \$\mathcal{F}\_t'\$ assumes the agent already knows the random variable it is about to choose!

* **“Is \$\mathcal{F}\_t\$ always the canonical filtration generated by \$S\_t, A\_t\$?”**
  No. The *canonical* filtration includes \$A\_t\$ at time \$t\$; the *history* filtration here is intentionally one step *earlier*.

---

### 8. Summary

The history filtration \$(\mathcal{F}\_t)\$ formalises the agent’s knowledge **right before** each decision, and the history process \$H\_t\$ is the concrete record of that knowledge. This separation underpins:

* Well‑posed definitions of admissible (non‑anticipative) policies
* Martingale and stopping‑time arguments essential to optimal‑control proofs
* Causal reasoning about reinforcement‑learning environments

Armed with these notions, one can rigorously discuss conditional expectations, dynamic programming, and learning algorithms without ever resorting to informal “the agent has seen …” language—the mathematics carries that burden.

---

### 2.3 MDP Components and Assumptions

## 0 Notation recap (from earlier sections)

| Symbol                                   | Meaning                                  | Where defined |
| ---------------------------------------- | ---------------------------------------- | ------------- |
| \(S,\,A\)                                  | finite state and action sets             | § 1.1         |
| \(\mathcal S=2^{S},\;\mathcal A=2^{A}\)    | discrete σ‑fields                        | § 1.1         |
| \(T=(S\times A)^{\mathbb N},\;\mathcal T\) | trajectory space                         | § 1.2         |
| \(H_t:\Omega\to (S\times A)^{t}\times S\)  | history process                          | § 2           |
| \(\mathcal F_t=\sigma(H_t)\)               | history filtration (“info before \(A_t\)”) | § 2           |

Throughout, the canonical probability space is \((\Omega,\mathcal T,\mathbb P^{\pi,\mu})\), whose existence/uniqueness is guaranteed by the cylinder‑set argument.

\(\textbf{MDP}\;M = (S, A, P, r, \gamma)\)

**Components:**
- **Initial distribution:** \(\mu \in \Delta(S)\)
- **Policy:** \(\pi = (\pi_t)_{t \geq 0}\) with kernels \(\pi_t: ((S \times A)^t \times S, \mathcal{F}_t) \to (A, \mathcal{A})\)
- **Transition kernel:** \(P: A \times S \to \Delta(S)\) with \(P_a(s,s') := P_a(s,\{s'\})\)
- **Reward function:** \(r: A \times S \to \mathbb{R}\)
- **Discount factor:** \(\gamma \in [0,1)\)

### 1.1 Initial distribution  \(\mu\in\Delta(S)\)

*Formal.*  \(\Delta(S)=\lbrace \mu:S\to[0,1]\mid\sum_{s\in S}\mu(s)=1 \rbrace\) is the **simplex** of probability measures on \(S\).
\(\mu\) is the push‑forward law of \(S_0\): \(P_{S_0}=\mu\).

*Role.*  Seeds the trajectory; together with \(\pi\) and \(P\) it fully determines \(\mathbb P^{\pi,\mu}\).

### 1.2 Policy  \(\pi=(\pi_t)_{t\ge0}\)

Each component is a **stochastic kernel**

$$
\pi_t:\bigl((S\times A)^t\times S,\;\mathcal F_t\bigr)\;\longrightarrow\;\bigl(A,\mathcal A\bigr),
$$

meaning

| Requirement                                                                                    | Translation |
| ---------------------------------------------------------------------------------------------- | ----------- |
| For fixed history \(h\), \(\pi_t(h,\cdot)\) is a probability measure on \((A,\mathcal A)\).          |             |
| For fixed Borel set \(B\subseteq A\), the map \(h\mapsto\pi_t(h,B)\) is \(\mathcal F_t\)-measurable. |             |

*Interpretation.*  **Non‑anticipativity:** the distribution of \(A_t\) depends only on what is known *before* the choice (the history \(H_t\)), never on future random variables.

*Special cases.*

* **Deterministic policy:** \(\pi_t(h,\cdot)=\delta_{\alpha_t(h)}\).
* **Stationary policy:** \(\pi_t\equiv\pi\) independent of \(t\).

### 1.3 Transition kernel  \(P:A\times S\to\Delta(S)\)

For each action–state pair \((a,s)\)

$$
s'\;\mapsto\;P_a(s,s')\quad\text{is a PMF on }S,
$$

and for fixed \(B\subseteq S\), the map \((a,s)\mapsto P_a(s,B)\) is measurable wrt \(\mathcal A\otimes\mathcal S\).

*Why a kernel?*  It lets us write the **one‑step law**

$$
\mathbb P\bigl(S_{t+1}\in B\mid \mathcal F_t,A_t=a\bigr)=P_a(S_t,B).
$$

### 1.4 Reward function  \(r:A\times S\to\mathbb R\)

\(r_a(s)\) is the immediate reward obtained when action \(a\) is applied in state \(s\).

*Random reward at time \(t\).*  \(R_{t+1}:=r_{A_t}(S_t)\) is \(\mathcal F_{t+1}\)-measurable.

### 1.5 Discount factor  \(\gamma\in[0,1)\)

Controls how future rewards are attenuated:

$$
G_0(\tau)=\sum_{t=0}^{\infty}\gamma^{t}r_{A_t}(S_t).
$$

\(\gamma<1\) guarantees geometric convergence once rewards are bounded.

**Assumption 2.1 (Bounded Rewards):** There exists \(R_{\max} \in (0,\infty)\) such that \(|r_a(s)| \leq R_{\max}\) for all \((s,a) \in S \times A\).

*Rationale:* Boundedness ensures the discounted return \(R(\tau) = \sum_{t=0}^{\infty} \gamma^t r_{A_t}(S_t)\) is absolutely convergent with \(|R(\tau)| \leq R_{\max}/(1-\gamma)\).


## 2 Assumption 2.1 (Bounded rewards)

> **There exists \(R_{\max}<\infty\) such that \(|r_a(s)|\le R_{\max}\) for all \((s,a)\).**

### 2.1 Mathematical rationale

Because

$$
|G_0(\tau)|
  \;\le\;
\sum_{t=0}^{\infty}\gamma^{t}R_{\max}
  \;=\;
\frac{R_{\max}}{1-\gamma},
$$

the **return** \(G_0\) is:

1. **Absolutely convergent** (no need to reorder terms).
2. **Uniformly bounded** ⇒ always integrable, \(G_0\in L^\infty(\Omega,\mathcal T,\mathbb P)\).

Hence value functions \(V^{\pi}_\mu :=\mathbb E^\pi_\mu[G_0]\) 

satisfy \(|V^{\pi}_\mu|\le R_{\max}/(1-\gamma)\).

### 2.2 Practical implications

| Benefit                                                      | Where used                                                                 |
| ------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Dominated‑convergence / interchange of limit and expectation | Proofs of policy evaluation and convergence of DP algorithms.              |
| Martingale boundedness                                       | Robbins–Monro and TD‑learning need square‑integrable noise.                |
| Well‑posed Bellman operator                                  | \(T^\pi\) maps bounded functions to bounded functions, ensuring contraction. |

If rewards were **unbounded**, one must switch to growth‑rate conditions (e.g. sub‑Gaussian tails) or risk diverging expectations.

## 3 How the pieces create a **trajectory law**

Given \((\mu,\pi,P)\):

1. **Initial step:** sample \(S_0\sim\mu\).
2. **For each \(t\):**
   a. Draw \(A_t\sim\pi_t(H_t,\cdot)\) (measurable wrt \(\mathcal F_t\)).
   b. Draw \(S_{t+1}\sim P_{A_t}(S_t,\cdot)\).

By Kolmogorov’s extension theorem (implemented through cylinder sets), this sequential description defines a **unique probability measure** \(\mathbb P^{\pi,\mu}\) on \((T,\mathcal T)\).

---

## 4 Connections to earlier concepts

| Earlier notion                    | Role inside the MDP                                                                    |
| --------------------------------- | -------------------------------------------------------------------------------------- |
| Push‑forward measure \(P_X\)        | \(\mu=P_{S_0},\;P_a(s,\cdot)=P_{S_{t+1}\mid S_t=s,A_t=a}\).                              |
| Generating functions              | Moment/characteristic functions of returns, e.g. \(M_{G_0}(t)=\mathbb E[e^{tG_0}]\).     |
| History filtration \(\mathcal F_t\) | Ensures \(\pi_t\) is **adapted**; certifies “no peeking into the future.”                |
| Martingale tools                  | \((V^\pi_t)_{t\ge0}\) and TD error sequences are martingales relative to \(\mathcal F_t\). |

## 5 FAQ‑style clarifications

* **Q:** *Why is the transition kernel written \(P:A\times S\to\Delta(S)\) instead of \(S\times A\to\Delta(S)\)?*
  **A:** Currying is purely cosmetic; the key is that the first argument is the *action actually taken*, the second is the *current state*.

* **Q:** *Can \(\gamma=1\)?*
  **A:** In episodic tasks with almost‑sure finite horizon you can admit \(\gamma=1\).  Here, requiring \(\gamma<1\) keeps the analysis agnostic to horizon assumptions.

* **Q:** *Is boundedness too restrictive?*
  **A:** Many RL proofs extend to sub‑Gaussian rewards; boundedness is a safe baseline that avoids technicalities without losing practical relevance (rewards are clipped or normalised in most implementations).

---

### One‑sentence take‑away

> An MDP is fully specified by an initial state law, a non‑anticipative policy, a Markov transition kernel, a bounded reward map, and a discount factor—together these objects induce a unique probability measure on the infinite trajectory space and guarantee the return is finite, enabling rigorous analysis via the filtration–martingale machinery outlined earlier.


### 2.4 Trajectory Measure Construction via Ionescu-Tulcea

**Theorem 2.1 (Existence of Trajectory Measure):** For every triple \((\mu, \pi, P)\), there exists a unique probability measure \(\mathbb{P}_\mu^\pi\) on \((T, \mathcal{T})\) such that:

1. **Initial condition:** \(\mathbb P_\mu^\pi(S_0 = s) = \mu(s)\) for all \(s \in S\)
2. **Policy condition:** \(\mathbb P_\mu^\pi(A_t = a \mid \mathcal F_t) = \pi_t(a \mid H_t)\) \(\mathbb P_\mu^\pi\)-a.s.
3. **Markov transition:** \(\mathbb P_\mu^\pi(S_{t+1} = s' \mid \mathcal F_t, A_t) = P_{A_t}(S_t, s')\) \(\mathbb P_\mu^\pi\)-a.s.

Moreover, \((S_t, A_t)_{t \geq 0}\) 

is a time-inhomogeneous Markov chain under \(\mathbb P_\mu^\pi\).

> **Theorem (I‑T, 1950).**
> Let \((E_0,\mathcal E_0),(E_1,\mathcal E_1),\dots\) be measurable spaces.
> Suppose we are given
>
> * an **initial probability** \(\lambda_0\) on \((E_0,\mathcal E_0)\);
> * for each \(n\ge1\) a **stochastic kernel**
>
>   $$
>       K_n:(E_0\times\cdots\times E_{n-1},\;
>             \mathcal E_0\otimes\cdots\otimes\mathcal E_{n-1})
>           \;\longrightarrow\;
>             (E_n,\mathcal E_n).
>   $$
>
> Then there exists a **unique** probability measure \(\lambda\) on the infinite product space
>
> $$
>   (E^{\infty},\mathcal E^{\infty})
>   :=\Bigl(\prod_{n\ge0}E_n,\;\bigotimes_{n\ge0}\mathcal E_n\Bigr)
> $$
>
> such that for every \(n\) and every cylinder set
> \(\;C=\{x_{0:n}\in B_0\times\cdots\times B_n\}\),
>
> $$
>     \lambda(C)
>       =\int_{B_0}\lambda_0(dx_0)
>          \int_{B_1}K_1(x_0,dx_1)\;
>          \cdots
>          \int_{B_n}K_n(x_{0:n-1},dx_n).
> $$

*Plain English:*  provide an initial law and a “next‑step kernel” that tells you how to sample coordinate \(n\) *given the entire past*; I‑T stitches them into a **single** probability measure on the whole infinite sequence.

**Proof Construction:** The theorem follows from the Ionescu-Tulcea extension theorem applied to the sequence of kernels:
\(Q_0(s_0) = \mu(s_0), \quad Q_{t+1}((s_{0:t}, a_{0:t}), s_{t+1}) = P_{a_t}(s_t, s_{t+1})\)
\(R_t((s_{0:t}, a_{0:t-1}), a_t) = \pi_t(a_t \mid s_{0:t}, a_{0:t-1}, s_t)\)

## 2 Casting the MDP components into the I‑T template

### 2.1 Choice of coordinate spaces

We want an *ordered* sequence

$$
    (S_0,\,A_0,\,S_1,\,A_1,\,S_2,\,A_2,\dots);
$$

hence set

| Index    | Coordinate | Space            |
| -------- | ---------- | ---------------- |
| \(0\)      | \(S_0\)      | \((S,\mathcal S)\) |
| \(1\)      | \(A_0\)      | \((A,\mathcal A)\) |
| \(2\)      | \(S_1\)      | \((S,\mathcal S)\) |
| \(3\)      | \(A_1\)      | \((A,\mathcal A)\) |
| \(\vdots\) | \(\vdots\)   | \(\vdots\)         |

Thus \(E_{2t}=S,\;E_{2t+1}=A\) and the product space
\((T,\mathcal T)=\prod_{n\ge0}(E_n,\mathcal E_n)\).

### 2.2 Initial measure \(\lambda_0\)

Take

$$
   \lambda_0:=\mu,
$$

the given initial state distribution.

### 2.3 Constructing the kernels \(K_n\)

We alternate **policy kernels** \(R_t\) and **transition kernels** \(Q_{t+1}\).

* **Even index \(n=2t\to n+1=2t+1\)** (choose action):

  $$
      K_{2t+1}(s_0,a_0,\dots,s_t;B)
        :=\pi_t\!\bigl(B\mid s_0,a_0,\dots,a_{t-1},s_t\bigr),
        \quad B\in\mathcal A.
  $$

  This is exactly \(R_t\) in the notation of the excerpt.

* **Odd index \(n=2t+1\to n+1=2t+2\)** (draw next state):

  $$
      K_{2t+2}(s_0,a_0,\dots,a_{t},s_t,a_t;C)
        :=P_{a_t}(s_t,C),
        \quad C\in\mathcal S,
  $$

  i.e. the kernel \(Q_{t+1}\).

Each \(K_n\) is a bona‑fide stochastic kernel: **(i)** for fixed past, \(K_n(\cdot)\) is a probability measure on the next coordinate’s σ‑field; **(ii)** for fixed Borel set, the mapping from past to probability is measurable (because \(\pi_t\) is \(\mathcal F_t\)-measurable and \(P\) is measurable on \(A\times S\)).

---

## 3 Applying I‑T and verifying the three bullets

### 3.1 Existence & uniqueness

By I‑T there is a unique \(\mathbb P_\mu^\pi\) on \((T,\mathcal T)\) that reproduces the iterated‑kernel integrals; denote it simply by \(\mathbb P\).

### 3.2 Initial‑condition bullet

Take cylinder \(C=\{S_0=s\}\).
I‑T integral collapses to \(\lambda_0(\{s\})=\mu(s)\).  ✓

### 3.3 Policy‑condition bullet

Fix \(t\).
Let \(B\subseteq A\).  Consider the function

$$
    \mathbf 1_{\{A_t\in B\}}
          -\pi_t(B\mid H_t).
$$

Its expectation w\.r.t. \(\mathbb P\) is zero by construction (because the step \(K_{2t+1}\) uses exactly \(\pi_t\)).
Standard “tower property” calculations turn this into

$$
    \mathbb P(A_t\in B\mid\mathcal F_t)=\pi_t(B\mid H_t)\quad\text{a.s.}
$$

Hence the second bullet holds.  ✓

### 3.4 Markov‑transition bullet

By the very next kernel \(K_{2t+2}\) we have for \(C\subseteq S\)

$$
    \mathbb P(S_{t+1}\in C\mid\mathcal F_t,A_t)
      =P_{A_t}(S_t,C)\quad\text{a.s.}
$$

Third bullet proved.  ✓

> **Uniqueness note:**
> If another measure satisfies bullets 1‑3, it must match \(\mathbb P\) on **all cylinders** (one proves this by downward induction on the time index using the conditional bullets).
> Cylinder sets generate \(\mathcal T\) and form a π‑system, so by the π‑λ theorem the measure is unique.

---

## 4 Markov‑chain interpretation of \((S_t,A_t)\)

Define the **pair process**

$$
    Z_t:=(S_t,A_t),\qquad t\ge0.
$$

### 4.1 Kernel for \(Z_t\to Z_{t+1}\)

Given \(Z_t=(s,a)\):

1. Sample \(s'\sim P_a(s,\cdot)\).
2. Sample \(a'\sim\pi_{t+1}(\,\cdot\mid H_{t+1})\) where \(H_{t+1}=(H_t,a,s')\).

Therefore the one‑step law of \(Z_{t+1}\) **given the entire past** factorises as

$$
   \mathbb P(Z_{t+1}\in B\times B'\mid\mathcal F_t)
     =\int_{B}P_a(s,ds')
      \int_{B'}\pi_{t+1}(da'\mid H_t,a,s').
$$

If the policy is *state‑only* (Markov) or *time‑only* (in‑homogeneous but no history dependence), the inner integral depends on \(s'\) and \(t\) only, **so** \(Z_t\) becomes a genuine time‑inhomogeneous Markov chain:

$$
   \mathbb P(Z_{t+1}\in\cdot\mid Z_t)=K_t(Z_t,\cdot).
$$

If the policy keeps the *whole* history, \(Z_t\) is *not* Markov—but the **extended process** \(H_t\) is.  Many authors implicitly assume Markov or stationary policies when writing the Markov‑chain remark; always check that hypothesis.

---

## 5 Why this construction is indispensable

| Task that needs \(\mathbb P_\mu^\pi\)                     | How I‑T helps                                                                                             |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Defining the **return** \(G_0=\sum\gamma^t r_{A_t}(S_t)\) | Guarantees \(G_0\) is a measurable function on \((T,\mathcal T)\).                                            |
| Proving **Bellman equations**                           | Conditional expectations in bullets 2‑3 turn into the Bellman operator by taking means under \(\mathbb P\). |
| **Policy‑gradient** or RL algorithm proofs              | One differentiates integrals w\.r.t. \(\mathbb P_\mu^\pi\); its uniqueness avoids ambiguity.                |
| Constructing **simulation trajectories**                | A simulator implements the kernels exactly in the I‑T order.                                              |

---

### One‑line takeaway

> The Ionescu–Tulcea theorem is the assembly line that, starting from *local* ingredients—initial state, policy kernels, and state‑transition kernel—builds a **single, global probability law** on the infinite trajectory space; this law is unique and (under Markov‑type policies) turns the sequence \((S_t,A_t)\) into a time‑inhomogeneous Markov chain, providing the bedrock on which all rigorous MDP analysis stands.

### 2.5 Canonical vs Abstract Probability Spaces

**Canonical Realization:** We may identify \((\Omega, \mathcal{F}, \mathbb{P}_\mu^\pi)\) 

with \((T, \mathcal{T}, \mathbb{P}_\mu^\pi)\) via the identity map \(\iota(\tau) = \tau\). In this **canonical probability space**, each random variable coincides with a coordinate map.

## 1 Two kinds of probability spaces

| Type                                | Formal triple                                         | How random variables are defined                                                                 |
| ----------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Canonical (path) space**          | \((T,\mathcal T,\mathbb P_{\mu}^{\pi})\)                | Directly by *coordinate maps* \(S_t(\tau)=s_t,\;A_t(\tau)=a_t\).                                   |
| **Abstract (model‑specific) space** | \((\tilde\Omega,\tilde{\mathcal F},\tilde{\mathbb P})\) | Random variables \(\tilde S_t, \tilde A_t\) are just measurable maps, not necessarily coordinates. |

Both are legitimate.  The difference is **representation**:

* In the canonical space, the sample point *is* an entire trajectory.
* In an abstract space, the sample point could be anything (a long bit‑string in a simulator, a sequence of random seeds, a physical outcome in the real world, …).

---

## 2 The identity map \(\iota\) and why it matters

Define

$$
\iota:T\longrightarrow T,\quad\iota(\tau)=\tau.
$$

Because \(\iota\) is the identity, pushing forward \(\mathbb P_{\mu}^{\pi}\) through \(\iota\) returns the same measure; i.e. \(\mathbb P_{\mu}^{\pi}=\iota_*\,\mathbb P_{\mu}^{\pi}\).
This simply says **“I’m already living on the path space.”**

*Consequence:*  Every random variable you care about—states, actions, cumulative reward, value function samples—can be *written as a measurable function on the single space \((T,\mathcal T)\)*.  No hidden machinery is required.

---

## 3 From an abstract space back to the canonical one

Suppose the abstract space \((\tilde\Omega,\tilde{\mathcal F},\tilde{\mathbb P})\) carries a process

$$
(\tilde S_0,\tilde A_0,\tilde S_1,\tilde A_1,\dots)
$$

that meets the three consistency conditions (initial law, policy kernel, transition kernel).
Define the **trajectory map**

$$
\Phi:\tilde\Omega\;\longrightarrow\;T,
\qquad
\Phi(\tilde\omega)
   :=\bigl(\tilde S_0(\tilde\omega),\tilde A_0(\tilde\omega),
           \tilde S_1(\tilde\omega),\tilde A_1(\tilde\omega),\dots\bigr).
$$

*Key facts*

1. **Measurability.**  Each coordinate is measurable, hence \(\Phi\) is \((\tilde{\mathcal F},\mathcal T)\)-measurable.
2. **Push‑forward law.**  By construction,

   $$
      \Phi_*\,\tilde{\mathbb P}=\mathbb P_{\mu}^{\pi},
   $$

   because both measures satisfy exactly the same cylinder‑set specifications.
   (Uniqueness follows from the π‑λ argument in § 2.4.)

Thus \(\Phi\) is a *probability‑space morphism* from the abstract space onto the canonical one.

---

**Uniqueness of Expectations:** If an alternative probability space \((\tilde{\Omega}, \tilde{\mathcal{F}}, \tilde{\mathbb{P}})\) supports a process satisfying the same three conditions, then:
\(\int_T f \, d\mathbb{P}_\mu^\pi = \int_T f \, d\tilde{\mathbb{P}} \quad \forall f \in L^1(T, \mathcal{T})\)

This ensures that expectations and probabilities of trajectory-measurable events are **well-defined** regardless of the specific realization.

## 4 **Uniqueness of expectations**

For any integrable \(f:T\to\mathbb R\),

$$
\int_T f\,d\mathbb P_{\mu}^{\pi}
   \;=\;
\int_{\tilde\Omega} f\bigl(\Phi(\tilde\omega)\bigr)\,
                  \tilde{\mathbb P}(d\tilde\omega)
   \;=\;
\int_T f\,d\tilde{\mathbb P}_{\Phi},
$$

where \(\tilde{\mathbb P}_{\Phi}:=\Phi_*\,\tilde{\mathbb P}\).
But \(\tilde{\mathbb P}_{\Phi}=\mathbb P_{\mu}^{\pi}\), so the two outer integrals coincide.

> **Interpretation:**
> *Any* expectation or probability that depends *only* on the realised trajectory (i.e. is \(\mathcal T\)-measurable) is **independent of which underlying sample space you picked**.

---

## 5 Why analysts like the canonical space

| Benefit                        | Explanation                                                                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Transparency**               | Random variables are literally coordinates; no extra notation for “tilde variables.”                                         |
| **Compact proofs**             | Conditioning reduces to manipulating σ‑fields generated by finitely many coordinates.                                        |
| **Simulation ↔ theory bridge** | Simulators produce sample paths, automatically interpreted as points of \(T\).                                                 |
| **Inter‑model comparability**  | Two different simulators with the same kernels push forward to the *same* \(\mathbb P_{\mu}^{\pi}\); results compare directly. |

---

## 6 A word on “probability‑space isomorphism”

If \(\Phi\) is **bijective modulo null sets** and its inverse is measurable, the two spaces are *isomorphic*; they carry the *same* measure‑theoretic structure.
Even when \(\Phi\) is not invertible (e.g. simulator uses extra random bits that don’t appear in trajectories), all \(\mathcal T\)-measurable questions are still answered identically.

---

### One‑sentence takeaway

> The canonical trajectory space \((T,\mathcal T,\mathbb P_{\mu}^{\pi})\) is the **common denominator** for every realisation of an MDP—any other probability space that drives the same state–action process collapses onto it via a measurable map, so all expectations of trajectory‑measurable quantities are guaranteed to be identical.

---

### 2.6 Matrix Formulation for Stationary Policies

For stationary policy \(\pi\), define the **policy-averaged quantities**:
\(r^\pi(s) := \sum_{a \in A} \pi(a \mid s) r_a(s), \quad P^\pi(s,s') := \sum_{a \in A} \pi(a \mid s) P_a(s,s')\)

The **value function** \(v^\pi \in \mathbb{R}^{|S|}\) satisfies the **policy evaluation equation**:
\(v^\pi = r^\pi + \gamma P^\pi v^\pi\)

**Theorem 2.2 (Policy Evaluation Solution):** The unique solution is:
\(v^\pi = (I - \gamma P^\pi)^{-1} r^\pi\)

where invertibility follows from \(\rho(\gamma P^\pi) = \gamma < 1\) (spectral radius).

## 1 Set‑up and standing assumptions

| Symbol                         | Meaning                                                                                            | Notes                                                                                                |
| ------------------------------ | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| \(S=\{1,\dots,n\}\)              | finite state set, \(n=\lvert S\rvert\)                                                               | indexing states by integers lets us use standard vector/matrix notation.                             |
| \(A\)                            | finite action set                                                                                  |                                                                                                      |
| \(\gamma\in[0,1)\)               | discount factor                                                                                    | strict inequality guarantees geometric convergence.                                                  |
| **Stationary policy** \(\pi\)    | mapping \(\pi(a\mid s)\) giving a probability distribution over \(A\) **that does not depend on time** | measurability conditions from earlier sections are automatically satisfied because \(S,A\) are finite. |
| Transition kernels \(P_a(s,s')\) | probability of next state \(s'\) when action \(a\) is taken in state \(s\)                               | each \(P_a\) is a **row‑stochastic** matrix of size \(n\times n\).                                       |
| Reward map \(r_a(s)\)            | bounded by \(R_{\max}\) (Assumption 2.1)                                                             | thus the return is finite.                                                                           |

---

## 2 Policy‑averaged reward and transition matrix

### 2.1 Definitions

$$
\boxed{%
\begin{aligned}
r^{\pi}(s) &:= \sum_{a\in A}\pi(a\mid s)\,r_a(s),\\[2mm]
P^{\pi}(s,s') &:= \sum_{a\in A}\pi(a\mid s)\,P_a(s,s').
\end{aligned}
}
$$

*Why these formulas?*
Condition on **current state only** (because policy is stationary and memory‑less).
Taking expectation over the action choice yields *effective* one‑step reward and transition probabilities that depend on \(s\) alone.

### 2.2 Matrix interpretation

* Let \(r^{\pi}\in\mathbb R^{n}\) be the column vector \((r^{\pi}(1),\dots,r^{\pi}(n))^{\!\top}\).
* Let \(P^{\pi}\in\mathbb R^{n\times n}\) have entries \(P^{\pi}(s,s')\).
  Because \(\pi(\cdot\mid s)\) and \(P_a(s,\cdot)\) are distributions, every row of \(P^{\pi}\) sums to 1 ⇒ \(P^{\pi}\) is **row‑stochastic**.

---

## 3 Value function and the policy evaluation equation

### 3.1 Return random variable

For a trajectory \(\tau=(S_0,A_0,S_1,A_1,\dots)\) generated under policy \(\pi\),

$$
G_0(\tau):=\sum_{t=0}^{\infty}\gamma^{t}\,r_{A_t}(S_t).
$$

### 3.2 Value function \(v^{\pi}\)

$$
v^{\pi}(s):=\mathbb E_{\mu\!=\!\delta_s}^{\pi}[\,G_0\,]\qquad (s\in S),
$$

i.e. expected return when we start *deterministically* from state \(s\).

Place \(v^{\pi}\) into a vector \(v^{\pi}\in\mathbb R^{n}\).

### 3.3 Derivation of the linear system

Condition on the first transition:

$$
\begin{aligned}
v^{\pi}(s)
  &=\mathbb E\bigl[r_{A_0}(s)\bigr]
    +\gamma\sum_{s'}\mathbb P(S_1=s'\mid S_0=s)\,
            v^{\pi}(s')\\[2mm]
  &= r^{\pi}(s)
     +\gamma\sum_{s'}P^{\pi}(s,s')\,v^{\pi}(s').
\end{aligned}
$$

Writing this for **all** states simultaneously gives the **policy evaluation equation**

$$
\boxed{\,v^{\pi}=r^{\pi}+\gamma P^{\pi}v^{\pi}.}
$$

---

## 4 Existence and uniqueness of the solution

Rearrange:

$$
(I-\gamma P^{\pi})\,v^{\pi}=r^{\pi}.
$$

### 4.1 Spectral‑radius argument

* The spectral radius of any stochastic matrix satisfies \(\rho(P^{\pi})=1\).
* Therefore \(\rho(\gamma P^{\pi})=\gamma<1\).

**Fact.** If \(\rho(M)<1\) for a square matrix \(M\), then \((I-M)\) is invertible and its inverse is given by the convergent Neumann series

$$
(I-M)^{-1}=\sum_{k=0}^{\infty}M^{k}.
$$

Apply with \(M=\gamma P^{\pi}\):

$$
(I-\gamma P^{\pi})^{-1}=\sum_{k=0}^{\infty}\gamma^{k}(P^{\pi})^{k}.
$$

Hence

$$
\boxed{v^{\pi}=(I-\gamma P^{\pi})^{-1}\,r^{\pi}}
$$

is well‑defined and unique.

### 4.2 Alternative proof via contraction mapping

Define the Bellman operator \(T^{\pi}:x\mapsto r^{\pi}+\gamma P^{\pi}x\).
Because \(\gamma<1\) and \(\|P^{\pi}x-P^{\pi}y\|_{\infty}\le\|x-y\|_{\infty}\),

$$
\|T^{\pi}x-T^{\pi}y\|_{\infty}\le\gamma\|x-y\|_{\infty},
$$

so \(T^{\pi}\) is a **\(\gamma\)-contraction** on \((\mathbb R^{n},\|\cdot\|_{\infty})\).
By Banach’s fixed‑point theorem, \(T^{\pi}\) has exactly one fixed point—equivalent to solving \(v^{\pi}=T^{\pi}v^{\pi}\).

---

## 5 Computational aspects

| Method                          | Idea                                                         | Convergence guarantee                                                                                 |
| ------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Direct solve**                | Factor \(I-\gamma P^{\pi}\) (Gaussian elimination, LU, etc.)   | \((I-\gamma P^{\pi})\) non‑singular by above.                                                           |
| **Iterative policy evaluation** | Repeatedly apply \(T^{\pi}\): \(v_{k+1}=T^{\pi}v_k\)             | Converges geometrically at rate \(\gamma\).                                                             |
| **TD(0) / TD(λ)**               | Stochastic approximation replacement of the full expectation | Converges under step‑size conditions; martingale difference noise analysis relies on bounded rewards. |

---

## 6 Interpretation and practical consequences

1. **Linear‑systems viewpoint**  
   The value‑function problem is nothing more than solving a *Poisson‑type equation* for a Markov chain with discounting.  All numerical linear‑algebra tools apply.

2. **Influence of \(\gamma\)**  
   As \(\gamma\to1^{-}\), the matrix \(I-\gamma P^{\pi}\) becomes ill‑conditioned; iterative methods slow down and variance of TD estimates grows.

3. **Role of bounded rewards**  
   Guarantees the right‑hand side \(r^{\pi}\) is bounded, so \(v^{\pi}\) is finite even when \((I-\gamma P^{\pi})^{-1}\) is applied term‑by‑term via the Neumann series.

4. **Extension to average‑reward or undiscounted episodic cases**  
   When \(\gamma=1\) but the Markov chain is absorbing (episodic tasks), the state‑value still solves a linear system, but invertibility requires replacing \(I-\gamma P^{\pi}\) with a *transient* sub‑matrix or adding a constraint to pin down the additive constant.

---

### One‑sentence takeaway

> For a stationary policy, averaging over the action choices collapses an MDP into a single Markov chain with matrix \(P^{\pi}\); the corresponding state‑value vector is the unique solution to a *discounted Poisson equation* \((I-\gamma P^{\pi})v^{\pi}=r^{\pi}\), whose invertibility—and thus existence and uniqueness—follows directly from the fact that \(\gamma<1\) shrinks the spectrum of \(P^{\pi}\).

### 2.7 Markov Property and Structural Foundation

The kernel \(P\) enforces the **Markov property**:

\(\mathbb P_\mu^\pi(S_{t+1} = s' \mid H_t, A_t) = P_{A_t}(S_t, s')\)

where \(H_t = (S_0, A_0, \ldots, S_t)\) is the complete history. This is the **sole structural assumption** distinguishing MDPs from general controlled stochastic processes.

## 1 Formal statement of the Markov property in an MDP

For every time index \(t\), state \(s'\in S\), and every history realisation
\(H_t=(S_0,A_0,\dots,S_t)\) together with the current action \(A_t=a\),

$$
\boxed{\;
  \mathbb P_\mu^\pi\bigl(S_{t+1}=s'\mid H_t,A_t=a\bigr)
     \;=\;
  P_{a}(S_t,s')\;
}
\tag{2.7‑M}
$$

*Translation:*

> **Given the present state \(S_t\) and the action \(A_t\), the conditional distribution of the *next* state \(S_{t+1}\) is **independent** of the earlier states and actions.**

---

## 2 Why (2.7‑M) is the *structural* assumption of an MDP

1. **Memoryless dynamics.**
   Only the *last* state–action pair \((S_t,A_t)\) influences the future.  All earlier information becomes irrelevant *once you know \(S_t\)*.

2. **Factorisation of trajectory law.**
   Using (2.7‑M) recursively yields the product form

   $$
       \mathbb P_\mu^\pi(\tau)
         =\mu(s_0)\,
          \Bigl[\prod_{t\ge0}
                \pi(a_t\mid H_t)\;
                P_{a_t}(s_t,s_{t+1})\Bigr],
   $$

   which underpinned the Ionescu–Tulcea construction in § 2.4.

3. **Bellman equations become local.**
   Because the distribution of \(S_{t+1}\) depends only on \((S_t,A_t)\), expectation of future return can be written in terms of *one‑step* conditional expectations, giving the familiar Bellman operator

   $$
       (T^\pi v)(s)=r^\pi(s)+\gamma\sum_{s'}P^\pi(s,s')\,v(s').
   $$

4. **Algorithmic leverage.**
   Dynamic‑programming, Monte‑Carlo tree search, temporal‑difference learning, policy‑gradient methods: *all* exploit the fact that knowledge of \(S_t\) suffices for predicting the distribution of anything that comes later.

---

## 3 Comparison with general controlled stochastic processes

| Feature                   | Markov decision process                                      | General controlled process                                                                              |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Next‑state law            | \(P_a(s,s')\) depends only on current \(s,a\)                    | Could depend on entire history \(H_t\), exogenous latent variables, or hidden context                     |
| State variable            | “Sufficient statistic” for future                            | May be *insufficient*; additional memory or belief state needed                                         |
| Analysis tools            | Bellman equations, contraction mappings, Markov‑chain theory | Often requires *functional* stochastic processes, non‑Markovian SDEs, or history‑augmented state spaces |
| Sample‑path factorisation | Simple product of kernels (Ionescu–Tulcea)                   | No simple factorisation; kernels must be indexed by full past                                           |

**Bottom line:**  the single‑kernel description \(P\) is what lets an MDP collapse a potentially huge historical dependence into a tractable *state* variable.

---

## 4 Common subtleties clarified

1. **Policy may still be history‑dependent.**
   In (2.7‑M) *only the environment dynamics* are Markov.
   If the policy \(\pi_t\) uses the whole history \(H_t\), the *joint* process \((S_t,A_t)\) need not be a Markov chain.
   When \(\pi\) is *Markov* (depends only on current state) or *stationary*, then \((S_t)\) or \((S_t,A_t)\) is Markov as well.

2. **Partially observable models (POMDPs).**
   The raw observation process breaks the Markov property, but one can *restore* it by enlarging the state to the *belief* distribution; this is precisely the “structural assumption” being adjusted.

3. **Continuous‑time or continuous‑state versions.**
   The same conditional‑independence statement is used, only expressed with transition kernels \(P_a(s,dy)\) on Borel sets; all modern RL theory in continuous domains hinges on this property.

---

## 5 Implications for theory and practice

* **Identifiability and sufficiency:**
  If the variable you call “state” *fails* to satisfy (2.7‑M), estimates of value and policy‑gradient updates become biased—algorithms implicitly assume the Markov property.

* **Simulation fidelity:**
  When designing simulators, you must ensure the pseudo‑random generative model respects \(P_a(s,\cdot)\); hidden internal cache or delayed effects inadvertently introduce history dependence and violate the assumption.

* **Model‑based RL:**
  Learning a *dynamics model* means estimating \(P_a(s,\cdot)\).  Thanks to (2.7‑M), this estimation problem decomposes by state–action pairs instead of exponentially many histories.

---

### One‑sentence takeaway

> The equation \(\mathbb P_\mu^\pi(S_{t+1}\!\mid H_t,A_t)=P_{A_t}(S_t,\cdot)\) encapsulates the **Markov property**: once you know the current state and chosen action, the future is conditionally independent of the past; this single structural postulate is what converts an otherwise intractable controlled process into the tractable, algebraically rich framework of Markov decision processes.

---

### 2.8 Extensions and Generalizations

| Variant | Modification | Additional Requirements |
|---------|--------------|------------------------|
| **Finite-horizon** | Add horizon \(H\); set \(\gamma = 1\) | None |
| **Average-reward** | Replace discount with Césaro limit | Ergodicity of \(P^\pi\) |
| **Countable \(S,A\)** | σ-fields become power sets | Bounded rewards |
| **Borel \(S,A\)** | Polish spaces with stochastic kernels | Measurability + compactness |


For each one we answer three questions:

1. **What is being changed** relative to the baseline discounted, infinite‑horizon, finite‑state MDP just analysed?
2. **Why the new formulation is useful / when you would prefer it.**
3. **Which extra mathematical assumptions** are needed so that existence / uniqueness / optimal‑control results still go through.

---

## Baseline for reference

| Component             | Default setting (Sections 2.1 – 2.7)  |         |                |
| --------------------- | ------------------------------------- | ------- | -------------- |
| Horizon               | Infinite \(t\in\mathbb N\)              |         |                |
| Discount              | \(\gamma\in[0,1)\)                      |         |                |
| State / Action spaces | Finite sets \(S,A\) (discrete σ‑fields) |         |                |
| Rewards               | Bounded, (                            | r\_a(s) | \le R\_{\max}) |
| Dynamics              | Markov kernel \(P_a(s,\cdot)\)          |         |                |

All earlier theorems (Ionescu‑Tulcea construction, Bellman equation, contraction mapping, etc.) rely on those ingredients.  The table in § 2.8 shows four standard ways to relax or alter them.

---

## 1 Finite‑horizon MDPs

| Item                   | Description                                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Modification**       | Fix a deterministic horizon \(H\in\mathbb N\).  Return becomes \(\displaystyle G^{H}_0=\sum_{t=0}^{H-1}r_{A_t}(S_t)\).  Equivalent to setting \(\gamma=1\) *and* truncating the sum after \(H\) terms. |
| **Why**                | Episodic tasks (e.g. games, trials) where the episode length is known in advance.  Dynamic‑programming algorithms run *backwards* from \(t=H\).                                                  |
| **Extra requirements** | **None.**  Boundedness is automatic (finite sum of bounded terms).  All value functions are finite; Bellman recursion is simply finite‑step backward induction.                                |

*Technical note.*  The Bellman operator is no longer a contraction (because \(\gamma=1\)), but we only apply it \(H\) times, so a fixed point is not required.

---

## 2 Average‑reward (undiscounted, continuing) MDPs

| Item                  | Description                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Modification**      | Replace the discounted return by the long‑run time average  \(\displaystyle \rho^\pi(s):=\lim_{N\to\infty}\frac1N\sum_{t=0}^{N-1}\mathbb E_s^\pi[r_{A_t}(S_t)]\), formally a **Césaro limit**.  (Often called **gain** or **bias + gain** formulation.)                                                                                                     |
| **Why**               | Evaluates policies in processes that run forever without a natural discount—e.g. factory throughput, packet routing, server farms.                                                                                                                                                                                                                        |
| **Extra requirement** | **Ergodicity** (or at least positive recurrence) of the Markov chain induced by \(\pi\):  \(\displaystyle\lim_{N\to\infty}\frac1N\sum_{t=0}^{N-1}P^{\pi\,t}(s,\cdot)=\eta^\pi(\cdot)\) where \(\eta^\pi\) is a stationary distribution.  This ensures the Césaro limit exists and is *state‑independent* (so a single scalar “average reward” is well defined). |

*Consequences.*

* Bellman equation becomes **Poisson equation**
  \( r^\pi - \rho^\pi \mathbf 1 + P^\pi h^\pi = h^\pi\)
  for the relative‑value (bias) vector \(h^\pi\).
* Algorithms such as relative‑value iteration or average‑reward TD require additional normalisation (e.g. fix \(h^\pi(s^\star)=0\)) but converge under ergodicity.

---

## 3 Countably‑infinite state or action sets

| Item                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Modification**      | Let \(S\) or \(A\) be countably infinite (e.g. integers, finite strings).  Keep the **discrete σ‑field** \(\mathcal S=2^{S}\), \(\mathcal A=2^{A}\).                                                                                                                                                                                                                                                                                          |
| **Why**               | Queueing models, inventory control, simple tabular RL where the index set is countably infinite.                                                                                                                                                                                                                                                                                                                                      |
| **Extra requirement** | **Bounded rewards** are retained *explicitly* to guarantee finiteness of \(\mathbb E^\pi[G_0]\) (the geometric series argument still works).  Most fixed‑point / contraction proofs go through because \(P^\pi\) is still a row‑stochastic matrix (possibly infinite‑dimensional).  Technical lemmas often invoke the **monotone‑convergence theorem** or **dominated‑convergence theorem** instead of finite‑dimensional linear algebra. |

*Additional remarks.*

* (Countable) Ionescu‑Tulcea still constructs the trajectory measure; cylinder sets form a π‑system that separates points just as in the finite case.
* Policy‑evaluation can be infinite‑dimensional linear algebra; one often works in \(l^\infty(S)\) or \(l^2(S,\eta)\).

---

## 4 Borel (uncountable) state or action spaces

| Item                   | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Modification**       | Let \(S,A\) be **Polish spaces** (complete, separable, metric).  Use their Borel σ‑fields.  Transitions become kernels \(P_a(s,\cdot)\) on the Borel sets; policies become **stochastic kernels** \( \pi(\cdot\mid s)\).                                                                                                                                                                   |
| **Why**                | Continuous control (e.g. robotics), finance, queuing with continuous state, function‑approximation RL.                                                                                                                                                                                                                                                                               |
| **Extra requirements** | Two broad kinds:                                                                                                                                                                                                                                                                                                                                                                     |
|                        | **Measurability:** kernels must be jointly measurable; reward must be measurable and (usually) bounded or at least integrable.                                                                                                                                                                                                                                                       |
|                        | **Compactness / continuity:** to *exist* stationary optimal policies one often assumes:  (i) compact action space, (ii) \(s\mapsto P_a(s,\cdot)\) and \(r_a(s)\) are continuous, (iii) measurable‑selection conditions (Berge, Jankov‑von Neumann).  These allow application of fixed‑point theorems (Blackwell, Kakutani) and contraction arguments (Hernández‑Lerma & Lasserre, 1996). |

*Consequences and new phenomena.*

* **Ionescu‑Tulcea** still applies because Polish spaces are standard Borel.
* Contraction of the Bellman operator holds in **sup‑norm of bounded measurable functions** when \(\gamma<1\).
* Existence of **deterministic stationary optimal policies** can fail without continuity/compactness assumptions (need measurable selection theorems).
* Unbounded rewards require growth conditions (e.g. Lyapunov functions) in lieu of a finite \(R_{\max}\).

---

## 5 Summary table (extended)

| Variant         | Return definition                                                    | Key extra assumption(s)                            | Main technical tool                           |
| --------------- | -------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------- |
| Finite horizon  | \(\sum_{t=0}^{H-1} r_{A_t}(S_t)\)                                      | None                                               | Backward induction                            |
| Average reward  | \(\displaystyle\lim_{N\to\infty}\frac1N\sum_{t=0}^{N-1} r_{A_t}(S_t)\) | Ergodicity / positive recurrence                   | Poisson equation, relative‑value iteration    |
| Countable \(S,A\) | Same as baseline                                                     | Bounded rewards                                    | \(l^\infty\) fixed‑point, dominated convergence |
| Borel \(S,A\)     | Same as baseline                                                     | Measurable kernels; often continuity + compactness | Measurable selection; Blackwell contraction   |

---

### One‑sentence takeaway

> Section 2.8 catalogues the four classic ways to move beyond *finite, discounted* MDPs—finite‑duration episodes, long‑run average criteria, countably infinite state/action sets, and fully general Borel spaces—and pinpoints the *minimal extra assumptions* (horizon, ergodicity, boundedness, measurability‑plus‑compactness) needed to keep existence, uniqueness, and optimal‑control theory intact.

### 2.9 Why the Measure-Theoretic Framework Matters

1. **Well-posedness:** Any trajectory-dependent quantity (e.g., discounted return) is measurable on \((T, \mathcal{T})\) with unique distribution
2. **Policy transformation:** Occupancy measures and Bellman operators manipulate \(\mathbb{P}_\mu^\pi\) algebraically with rigorous foundations
3. **Generalization pathway:** The construction extends to uncountable spaces with appropriate measurability conditions
4. **Algorithmic foundations:** Value iteration and policy iteration convergence rely on the measure-theoretic structure

**Example - Inventory Control:** 

States \(s \in \{0, \ldots, \bar{s}\}\) (inventory levels), actions \(a \in \{0, \ldots, \bar{a}\}\) (order quantities), 

demand \(D_t \sim \text{Poisson}(\lambda)\) i.i.d.: 

$
P_a(s, s') = \mathbb P [(s + a - D_t)_+ = s']
$

$
r_a(s) = -c_{\text{hold}}(s + a) - c_{\text{order}}a
$


This fits the framework with \(R_{\max} = c_{\text{hold}}\bar{s} + c_{\text{order}}\bar{a}\) and typical \(\gamma = 0.99\).

## 3. Discounting and Effective Horizon: Detailed Analysis

### 3.1 Discounted Return: Well-Definedness and Measurability

The **discounted return** functional is defined as:
\(R(\tau) = \sum_{t=0}^{\infty} \gamma^t r_{A_t}(S_t), \quad \gamma \in [0,1), \quad |r_a(s)| \leq R_{\max} < \infty\)

**Theorem 3.1 (Boundedness and Measurability):** The discounted return satisfies:
1. **Uniform boundedness:** \(|R(\tau)| \leq \frac{R_{\max}}{1-\gamma}\) for every trajectory \(\tau\)
2. **Measurability:** \(R \in L^{\infty}(T, \mathcal{T}, \mathbb{P}_\mu^\pi)\) for any \((\mu, \pi)\)
3. **Integrability:** \(\mathbb{E}_\mu^\pi[|R|] < \infty\), ensuring value functions are finite

**Proof:** Since \(\sum_{t \geq 0} \gamma^t = 1/(1-\gamma)\), Fubini's theorem yields:
\(|R(\tau)| \leq \sum_{t=0}^{\infty} \gamma^t |r_{A_t}(S_t)| \leq R_{\max} \sum_{t=0}^{\infty} \gamma^t = \frac{R_{\max}}{1-\gamma}\)

Measurability follows from the fact that \(R\) is a limit of measurable functions (finite partial sums).


## 1 Setting and notation

* **State and action spaces** \(S,A\) — finite (§ 2), or more generally countable / Borel so long as rewards are bounded.
* **Reward bound** \(\displaystyle\lvert r_a(s)\rvert\le R_{\max}<\infty\) (Assumption 2.1).
* **Discount factor** \(\gamma\in[0,1)\).
* **Canonical trajectory space** \((T,\mathcal T,\mathbb P_\mu^{\pi})\) built via Ionescu–Tulcea (§ 2.4).
* **Coordinate processes** \(S_t,A_t:T\to S,A\).

Define the **discounted‑return functional**

$$
\boxed{%
   R(\tau)\;:=\;\sum_{t=0}^{\infty}\gamma^{t}\, r_{A_t(\tau)}\!\bigl(S_t(\tau)\bigr),
   \qquad\tau\in T.
}
$$

---

## 2 Uniform boundedness (statement 1)

Because \(\lvert r_{A_t}(S_t)\rvert\le R_{\max}\) for every coordinate pair,

$$
\lvert R(\tau)\rvert
  \;\le\;
  \sum_{t=0}^{\infty}\gamma^{t}R_{\max}
  \;=\;
  R_{\max}\,\frac{1}{1-\gamma}
  \quad\text{(geometric series).}
$$

**Key point:** the bound is **deterministic**—it holds for *every* trajectory.
Hence \(R\) maps \(T\) into the compact interval \([-\frac{R_{\max}}{1-\gamma},\frac{R_{\max}}{1-\gamma}]\).

---

## 3 Measurability (statement 2)

### 3.1 Partial‑sum sequence

Define

$$
R_N(\tau):=\sum_{t=0}^{N}\gamma^{t}r_{A_t}(S_t).
$$

* Each \(R_N\) is a **finite sum of measurable functions** (products of measurable coordinate maps and constants), so \(R_N\!:\;(T,\mathcal T)\to\mathbb R\) is \(\mathcal T\)-measurable.

### 3.2 Pointwise convergence

For every \(\tau\),

$$
\lim_{N\to\infty}R_N(\tau)
  =R(\tau)
  \quad\text{because the series is absolutely convergent (bounded rewards + }\gamma<1\text{).}
$$

### 3.3 Limit of measurable functions

A **pointwise limit** of measurable functions is measurable *provided the limit exists as an extended real number*.
Here the limit lies in a finite interval (previous step), so \(R\) is \(\mathcal T\)-measurable.

### 3.4 Bound places \(R\) in \(L^\infty\)

Since \(\lVert R\rVert_{\infty}\le R_{\max}/(1-\gamma)\), we have

$$
R\in L^{\infty}(T,\mathcal T,\mathbb P_\mu^{\pi})\subseteq L^{1}(T,\mathcal T,\mathbb P_\mu^{\pi}).
$$

---

## 4 Integrability and finiteness of value functions (statement 3)

Because \(\lvert R\rvert\le R_{\max}/(1-\gamma)\) everywhere,

$$
\mathbb E_\mu^{\pi}[\lvert R\rvert]
  \;\le\;
  \frac{R_{\max}}{1-\gamma}\;<\;\infty.
$$

Therefore the **state‑value function**

$$
v^{\pi}(s):=\mathbb E_{\mu=\delta_s}^{\pi}[R]
$$

is finite for every \(s\).
All standard expectations, variances, gradients, etc. are guaranteed to be well‑defined.

---

## 5 Why each property matters in practice

| Property            | Role in RL / control theory                                                                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Uniform boundedness | Ensures numerical stability; lets us clip or normalise returns without losing correctness.                                                                             |
| Measurability       | Allows conditional expectations \(\mathbb E[R\mid\mathcal F_t]\); essential for Bellman equations, martingale arguments, policy‑gradient proofs.                         |
| Integrability       | Guarantees that Monte‑Carlo estimators have finite variance; necessary for LLN / CLT results and convergence of TD and Q‑learning via stochastic‑approximation theory. |

---

## 6 Side remarks and extensions

1. **If \(\gamma=1\)** but the horizon is finite (\(H<\infty\)), boundedness and measurability still hold because the sum has only \(H\) terms.
   For *infinite* horizon with \(\gamma=1\) one must impose a different criterion (e.g. average‑reward or attainment of an absorbing state).

2. **Unbounded rewards** can be allowed if they have light tails (e.g. sub‑Gaussian) and \(\gamma<1\), but proofs require dominated‑convergence arguments with a random dominating function—outside the scope of § 3.1.

3. **Continuous‑time counterparts** replace the series by a discounted integral \(\int_0^\infty e^{-\beta t} r_{A_t}(S_t)\,dt\); analogous boundedness and measurability proofs use the exponential tail \(e^{-\beta t}\).

---

### One‑sentence takeaway

> Because rewards are bounded and the discount factor satisfies \(\gamma<1\), the discounted‑return functional converges absolutely, is a measurable and uniformly bounded map on trajectory space, and therefore has finite expectation—providing the rigorous foundation on which all value‑based reinforcement‑learning methods rest.

### 3.2 Tail Truncation Error Analysis

For any horizon \(H \geq 0\), define the **tail remainder**:

$
\text{Tail}_H(\tau) := \sum_{t=H}^{\infty} \gamma^t r_{A_t}(S_t)
$

**Theorem 3.2 (Uniform Tail Bound):** The tail remainder satisfies:
\(|\text{Tail}_H(\tau)| \leq \frac{\gamma^H R_{\max}}{1-\gamma} \quad \text{for all } \tau \in T\)

**Corollary 3.3 (Approximation Error):** Replacing \(R(\tau)\) with its \(H\)-step prefix incurs at most \(\frac{\gamma^H R_{\max}}{1-\gamma}\) error **uniformly over all policies and initial states**.

### 3.3 Effective Horizon: Precise Characterization

For prescribed tolerance \(\varepsilon > 0\), define the **effective horizon**:
\(H_{\gamma,\varepsilon} := \left\lceil \frac{\ln(1/(\varepsilon(1-\gamma)))}{1-\gamma} \right\rceil\)

**Theorem 3.4 (Effective Horizon Sufficiency):** Truncating after \(H_{\gamma,\varepsilon}\) steps ensures:
\(\frac{\gamma^{H_{\gamma,\varepsilon}}}{1-\gamma} R_{\max} \leq \varepsilon R_{\max}\)

**Proof:** Using \(\gamma^x \leq e^{-(1-\gamma)x}\) for \(\gamma \in [0,1)\):
\(\frac{\gamma^{H_{\gamma,\varepsilon}}}{1-\gamma} R_{\max} \leq \frac{e^{-H_{\gamma,\varepsilon}(1-\gamma)}}{1-\gamma} R_{\max} \leq \varepsilon R_{\max}\)

## 1 Definitions

| Symbol                | Meaning                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| \(R(\tau)\)             | full discounted return  \(\displaystyle R(\tau)=\sum_{t=0}^{\infty}\gamma^{t} r_{A_t}(S_t)\)  (§ 3.1)                 |
| \(H\)                   | deterministic *planning / simulation horizon* (non‑negative integer)                                                |
| \(\text{Tail}_H(\tau)\) | *tail remainder* after step \(H{-}1\):  \(\displaystyle\text{Tail}_H(\tau)=\sum_{t=H}^{\infty}\gamma^{t} r_{A_t}(S_t)\) |
| \(R_{\max}\)            | uniform bound on reward magnitude:  \(\lvert r_a(s)\rvert\le R_{\max}\)                                               |
| \(\gamma\)              | discount factor in \([0,1)\)                                                                                          |

The **\(H\)-step prefix** (often called *partial return*) is

$$
R^{(H)}(\tau)\;:=\;\sum_{t=0}^{H-1}\gamma^{t}r_{A_t}(S_t),
$$

so that

$$
R(\tau)\;=\;R^{(H)}(\tau)\;+\;\text{Tail}_H(\tau).
$$

---

## 2 Theorem 3.2 – Uniform tail bound

> **Statement.**  For every horizon \(H\ge0\) and every trajectory \(\tau\in T\),
>
> $$
>     \bigl\lvert\text{Tail}_H(\tau)\bigr\rvert
>        \;\le\;
>     \frac{\gamma^{H}\,R_{\max}}{1-\gamma}.
> $$
>
> The bound is *deterministic*—it does **not** depend on policy, initial distribution, or the particular trajectory.

### 2.1 Proof

1. **Apply reward bound term‑wise.**
   For each \(t\ge H\),
   \(\lvert r_{A_t}(S_t)\rvert\le R_{\max}\).

2. **Use monotonicity of the absolute value and sum.**

   $$
   \bigl\lvert\text{Tail}_H(\tau)\bigr\rvert
       \;=\;
   \Bigl\lvert\sum_{t=H}^{\infty}\gamma^{t} r_{A_t}(S_t)\Bigr\rvert
       \;\le\;
   \sum_{t=H}^{\infty}\gamma^{t}\lvert r_{A_t}(S_t)\rvert
       \;\le\;
   R_{\max}\sum_{t=H}^{\infty}\gamma^{t}.
   $$

3. **Evaluate the geometric tail.**
   Because \(0\le\gamma<1\),

   $$
       \sum_{t=H}^{\infty}\gamma^{t}
         =\gamma^{H}\sum_{k=0}^{\infty}\gamma^{k}
         =\gamma^{H}\,\frac{1}{1-\gamma}.
   $$

4. **Combine.**

   $$
       \bigl\lvert\text{Tail}_H(\tau)\bigr\rvert
         \le
       R_{\max}\,\frac{\gamma^{H}}{1-\gamma}.
   \qquad\qedhere
   $$

*No probability or expectation is needed; the inequality is purely algebraic.*

---

## 3 Corollary 3.3 – Approximation error bound

Because

$$
    R(\tau)-R^{(H)}(\tau)=\text{Tail}_H(\tau),
$$

taking absolute values and invoking Theorem 3.2 yields

$$
   \lvert R(\tau)-R^{(H)}(\tau)\rvert
      \le
   \frac{\gamma^{H}R_{\max}}{1-\gamma}
   \quad\text{for every }\tau.
$$

### 3.1 Uniformity over policies and initial states

* The derivation uses **only** \(R_{\max}\) and \(\gamma\).
* Neither the policy \(\pi\) nor the initial distribution \(\mu\) appears.
* Hence the same bound holds under *any* \(\mathbb P_{\mu}^{\pi}\).

Consequently:

$$
   \sup_{\mu,\pi}\;
   \bigl\lVert R-R^{(H)}\bigr\rVert_{\infty}
      \;=\;
   \frac{\gamma^{H}R_{\max}}{1-\gamma}.
$$

Taking expectations preserves the bound:

$$
   \bigl\lvert
      \mathbb E_{\mu}^{\pi}[R]
      -\mathbb E_{\mu}^{\pi}[R^{(H)}]
   \bigr\rvert
      \;\le\;
   \frac{\gamma^{H}R_{\max}}{1-\gamma},
$$

so value‑function estimates obtained from \(H\)-step simulations incur *at most* that absolute error.

---

## 4 Practical implications

| Topic                                 | Application of the bound                                                                                                                                                                 |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simulation length planning**        | To guarantee absolute error ≤ \(\varepsilon\), choose  \(\displaystyle H\;\ge\;\Bigl\lceil\frac{\ln\!\bigl((1-\gamma)\varepsilon/R_{\max}\bigr)}{\ln\gamma}\Bigr\rceil\).                    |
| **Value‑iteration stopping**          | In synchronous value iteration the *Bellman residual* after \(H\) sweeps is bounded by \(\gamma^{H}/(1-\gamma)\) times the initial span, directly mirroring the tail bound.                  |
| **Monte‑Carlo policy evaluation**     | If episodes are artificially truncated at horizon \(H\), bias ≤ \(\gamma^{H}R_{\max}/(1-\gamma)\); variance scales with \(\gamma^{2H}\).                                                       |
| **Sample‑complexity proofs**          | PAC‑RL bounds (e.g., Kakade & Langford, 2002) express the required horizon in terms of \(\log(1/\delta)/(1-\gamma)\) via the same geometric‑tail argument.                                 |
| **Model‑based planning (MCTS, Dyna)** | When rollouts are cut at depth \(H\), the backup error into the root Q‑value is capped by the bound; selecting \(H\) proportionally to the desired precision keeps planning bias controlled. |

---

## 5 Side notes and extensions

* **Random horizon** – If the episode length \(T\) is a stopping time with \(\mathbb P(T>H)\le\kappa\), then

  $$
      \mathbb E[\,\lvert\text{Tail}_T\rvert\,]\le
      \frac{\gamma^{H}R_{\max}}{1-\gamma}
      +\kappa\,\frac{R_{\max}}{1-\gamma},
  $$

  combining deterministic tail decay with the probability of a long episode.

* **Continuous‑time discounting** – Replace \(\gamma^{t}\) with \(e^{-\beta t}\); the tail bound becomes \(R_{\max}e^{-\beta H}/\beta\).

* **Unbounded rewards with sub‑Gaussian tails** – Use concentration inequalities and tail integrals; extra logarithmic terms appear, but geometric discounting still dominates.

---

### One‑sentence takeaway

> Because rewards are bounded and discounting is geometric, the contribution of all steps beyond horizon \(H\) is universally limited by \(\gamma^{H}R_{\max}/(1-\gamma)\); this simple inequality quantifies exactly how far into the future you must look to approximate discounted returns—and hence value functions—to within any desired accuracy, regardless of the policy or initial state.

### 3.4 Asymptotic Behavior and Scaling Laws

**Large-Horizon Regime:** When \(\gamma \uparrow 1\) with \((1-\gamma) \ll 1\):

\(H_{\gamma,\varepsilon} = \frac{\ln(1/(\varepsilon(1-\gamma)))}{1-\gamma} (1 + o(1)) = \Theta\left(\frac{1}{1-\gamma}\right)\)

**Practical Rule:** The **effective planning horizon** is approximately:
\(H_{\text{eff}} \approx \frac{1}{1-\gamma}\)

### 3.5 Operational Interpretation of the Discount Factor

#### 3.5.1 Algorithmic Complexity
Dynamic programming error bounds scale as \(\gamma^k/(1-\gamma)\) after \(k\) iterations. For fixed accuracy \(\varepsilon\), the required iterations are:
\(k^* = O\left(\frac{\ln(1/\varepsilon)}{1-\gamma}\right)\)

#### 3.5.2 Modeling Perspectives

**Termination Probability:** If episodes end with probability \(p\) each step, setting \(\gamma = 1-p\) makes the discounted value equal the expected undiscounted total reward before termination.

**Time Preference:** In economics, \(\gamma = e^{-\rho \Delta t}\) where \(\rho\) is the continuous-time discount rate and \(\Delta t\) is the time step.

**Finite-Horizon Approximation:** Given horizon \(H\), choosing \(\gamma = \exp(-1/H)\) yields \(H_{\text{eff}} \approx H\).

#### 3.5.3 Relationship to Finite-Horizon Problems

A discounted infinite-horizon MDP can be **unfolded** into an equivalent finite-horizon problem by:
1. Augmenting states with a time counter: \(\tilde{S} = S \times \{0, 1, \ldots, H_{\gamma,\varepsilon}\}\)
2. Setting \(\tilde{\gamma} = 1\) (no discounting needed)
3. Defining absorbing states for \(t > H_{\gamma,\varepsilon}\)

### 3.6 Comparative Analysis of Objective Functions

| Objective | Mathematical Form | Advantages | Disadvantages | Typical Use |
|-----------|------------------|------------|---------------|-------------|
| **Discounted** | \(\sum_{t \geq 0} \gamma^t r_t\) | • Contraction property<br>• Fast convergence<br>• Always well-defined | • Introduces bias<br>• Parameter tuning | Most RL algorithms |
| **Finite-horizon** | \(\sum_{t=0}^{H-1} r_t\) | • No discount bias<br>• Natural for episodic tasks | • Requires known horizon<br>• No contraction | Games, robotics |
| **Average reward** | \(\lim_{T \to \infty} \frac{1}{T}\sum_{t<T} r_t\) | • Scale-free<br>• Long-term optimality | • Requires ergodicity<br>• Slow convergence | Steady-state control |
| **Total cost** | \(\sum_{t \geq 0} r_t\) | • Natural for absorbing MDPs | • May diverge<br>• No contraction | Shortest path problems |

### 3.7 Practical Guidelines for Choosing \(\gamma\)

#### 3.7.1 Task-Based Heuristics

**Known Task Length:** If rewards beyond \(H\) steps are negligible, choose:
\(\gamma \approx 1 - \frac{1}{H}\)

**Unknown Duration:** For continuous control or lifelong learning, \(\gamma \in [0.95, 0.99]\) is typical.

#### 3.7.2 Numerical Considerations

**Stability Threshold:** Very high \(\gamma \geq 0.999\) may cause:
- Slow convergence in iterative algorithms
- Numerical instability due to \((I - \gamma P^\pi)^{-1}\) becoming ill-conditioned
- Floating-point precision issues

**Remedies:**
1. Use \(H_{\gamma,\varepsilon}\)-step truncation
2. Switch to finite-horizon formulation
3. Employ higher-precision arithmetic

#### 3.7.3 Domain-Specific Recommendations

- **Robotics:** \(\gamma = 0.99\) (100-step horizon)
- **Games:** \(\gamma = 0.95\) or finite-horizon
- **Finance:** \(\gamma = e^{-r \Delta t}\) based on risk-free rate \(r\)
- **Control:** \(\gamma = 0.9\) to \(0.99\) depending on system dynamics

### 3.8 Connection to Martingale Theory

The discounted return under a fixed policy forms a **supermartingale** with respect to the natural filtration:

**Theorem 3.5 (Discounted Reward Supermartingale):** For any policy \(\pi\), the process:
\(M_t := \sum_{k=t}^{\infty} \gamma^{k-t} r_{A_k}(S_k)\)
satisfies \(\mathbb{E}[M_{t+1} \mid \mathcal{F}_t] \leq M_t\) when \(\gamma < 1\).

This property underlies the convergence analysis of temporal difference learning algorithms.

Below is a careful, measure‑theoretic analysis of the object

$$
M_t\;:=\;\sum_{k=t}^{\infty}\gamma^{\,k-t}\,r_{A_k}(S_k), 
\qquad\gamma\in[0,1),\qquad |r_{a}(s)|\le R_{\max}<\infty,
\tag{3.13}
$$

together with an **explicit check of the “supermartingale” claim** that appears in the note.
Because the statement, as written, is **not always true**, we first derive the exact conditional expectation and then spell out the extra sign assumptions under which the super‑ (or sub‑) martingale property really holds.
Finally we explain why the *martingale–difference* identity that always *does* hold is the one used in temporal‑difference (TD) learning proofs.

---

## 1 Basic facts about \(M_t\)

* **Adaptedness.** \(M_t\) is \(\mathcal F_t\)-measurable because it is a measurable function of \((S_t,A_t,S_{t+1},A_{t+1},\dots)\).
* **Boundedness.** By exactly the same geometric‑series argument used in § 3.1,

$$
|M_t|\;\le\;\frac{R_{\max}}{1-\gamma}\quad\text{for all }t\text{ and all trajectories}.
\tag{3.14}
$$

Hence \(M_t\in L^{\infty}\subset L^{1}\).

---

## 2 The one‑step recursion and conditional expectation

Because the series in (3.13) starts at \(k=t\),

$$
M_t
   \;=\;
   r_{A_t}(S_t)\;+\;\gamma\,M_{t+1}.
\tag{3.15}
$$

Taking conditional expectation w\.r.t.\ \(\mathcal F_t\) (remember that \(r_{A_t}(S_t)\) is already \(\mathcal F_t\)-measurable) gives

$$
\boxed{\;
  \mathbb E[M_{t+1}\mid\mathcal F_t]
      =\frac{M_t-r_{A_t}(S_t)}{\gamma}.
\;}
\tag{3.16}
$$

This identity is exact and holds under **no sign restrictions**.

---

## 3 When is \(M_t\) a super‑ or sub‑martingale?

Recall:

* supermartingale  \(\Longleftrightarrow\) \(\mathbb E[M_{t+1}\mid\mathcal F_t]\le M_t\);
* submartingale   \(\Longleftrightarrow\) \(\mathbb E[M_{t+1}\mid\mathcal F_t]\ge M_t\).

Plug (3.16) into the inequality:

$$
\frac{M_t-r_{A_t}(S_t)}{\gamma}\;\le\;(\ge)\;M_t
\quad\Longleftrightarrow\quad
(\,1-\gamma)\,M_t\;\le\;(\ge)\;r_{A_t}(S_t).
\tag{3.17}
$$

### 3.1 Non‑positive rewards  \((r_{A_t}(S_t)\le 0)\)

Since \(M_t\) is a weighted *sum of future* rewards, it is **also non‑positive**.
Therefore

$$
r_{A_t}(S_t)\;\le\; (1-\gamma)M_t
$$

and the **“ ≤ ”** direction in (3.17) is satisfied; \(M_t\) is a **supermartingale**.

*Example.*  Cost‑minimisation MDPs where \(r_a(s)=-c_a(s)\le0\).

### 3.2 Non‑negative rewards  \((r_{A_t}(S_t)\ge 0)\)

Both sides of (3.17) are now non‑negative and the inequality flips:

$$
r_{A_t}(S_t)\;\ge\;(1-\gamma)M_t,
$$

so \(M_t\) becomes a **submartingale**.

*Example.*  Reward‑maximisation tasks with \(r_a(s)\ge0\).

### 3.3 Mixed‑sign rewards

If rewards can take both signs, neither inequality is guaranteed: \(M_t\) is in general **neither** a sub‑ nor a supermartingale.  One must analyse the positive and negative parts separately or use a centred process (next section).

---

## 4 Martingale–difference identity that *always* holds

Rewrite (3.15) as

$$
\delta_t 
   \;:=\;
   r_{A_t}(S_t)\;+\;\gamma\,M_{t+1}\;-\;M_t
   \;=\;0\quad\text{path‑wise}.
\tag{3.18}
$$

Take conditional expectation:

$$
\mathbb E[\delta_t\mid\mathcal F_t]=0.
\tag{3.19}
$$

Thus, even though \((M_t)\) may fail to be a supermartingale in general, the **TD error**

$$
\underbrace{r_{A_t}(S_t)+\gamma\,M_{t+1}-M_t}_{\text{one‑step temporal‑difference}}
$$

is a **martingale‑difference sequence**.
This is the precise property exploited in proofs of:

* TD(0) and TD(λ) convergence (Robbins–Monro–type stochastic approximation),
* Q‑learning noise analysis,
* Policy‑gradient denominator tricks.

---

## 5 Summary and corrected theorem

> **Corrected Theorem 3.5.**
> Let \(\gamma\in(0,1)\) and \(M_t\) be defined by (3.13).
> Then, *always*,
>
> $$
>   r_{A_t}(S_t)+\gamma\,\mathbb E[M_{t+1}\mid\mathcal F_t]=M_t
>   \qquad (\text{martingale‑difference identity}).
> $$
>
> Moreover,
>
> * if \(r_{A_t}(S_t)\le 0\) a.s., \((M_t)\) is a **supermartingale**;
> * if \(r_{A_t}(S_t)\ge 0\) a.s., \((M_t)\) is a **submartingale**.

Either way, \(\lvert M_t\rvert\le R_{\max}/(1-\gamma)\) and \(M_t\in L^{1}\).

---

## 6 Why TD learning relies on (3.18)–(3.19)

Algorithms such as TD(0) update an estimate \(V(S_t)\) using the noisy target

$$
Y_t\;=\;r_{A_t}(S_t)\;+\;\gamma\,V(S_{t+1}),
$$

whose true mean is \(\mathbb E[r_{A_t}(S_t)+\gamma V^\pi(S_{t+1})\mid\mathcal F_t]\).
Setting \(V= M\) makes the target unbiased **because of (3.19)**: the noise term is a martingale difference, so stochastic‑approximation theory applies directly (boundedness + martingale difference ⇒ almost‑sure convergence under standard step‑size schedules).

---

### One‑sentence takeaway

> The discounted‑future‑return process \(M_t\) is *always* bounded and adapted; it becomes a super‑ or sub‑martingale only when rewards are one‑sided in sign, but—crucially for TD learning—the difference \(r_{A_t}(S_t)+\gamma M_{t+1}-M_t\) is a martingale‑difference sequence unconditionally, and that is the property exploited in all convergence proofs.


## 4 Policies and the agent–environment loop (full details)

### 4.1 Histories and policy spaces

For every \(t\ge 0\) define the **history σ‑field**

$$
\mathcal H_t \;:=\; \sigma\!\bigl(S_0,A_0,\dots,S_{t-1},A_{t-1},S_t\bigr),
\tag{4.1}
$$

and the corresponding **history space**

$$
\mathsf H_t \;:=\; (S\times A)^{t}\times S .
\tag{4.2}
$$

A **(history‑dependent) policy** is a sequence

$$
\pi \;=\;(\pi_t)_{t\ge 0}, \qquad  
\pi_t:\bigl(\mathsf H_t,\mathcal H_t\bigr)\longrightarrow\bigl(\Delta(A),\mathcal A_{\!\Delta}\bigr),
\tag{4.3}
$$

where \(\Delta(A)\) is the probability simplex on \(A\) endowed with the Borel σ‑field
and \(\mathcal A_{\!\Delta}\) its trace.  For a realised history \(h_t\in\mathsf H_t\) we abbreviate

$$
\pi_t(a\mid h_t)\;:=\;\bigl[\pi_t(h_t)\bigr](a), \qquad a\in A .
\tag{4.4}
$$

* **Deterministic policy:** each \(\pi_t(h_t)\) is a Dirac measure.
* **Randomised policy:** \(\pi_t(h_t)\) is non‑degenerate for some \(h_t\).
* **Stationary (memoryless) policy:** \(\pi_t(h_t)=\pi(a\mid s_t)\) depends only on the current state.

These conventions follow the lecture‑note definitions in Jiang (2024).&#x20;

## 1 History σ‑fields \(\mathcal H_t\) — what they contain and why

### 1.1 Definition (4.1) restated

$$
\boxed{%
  \mathcal H_t := \sigma\!\bigl(S_0,A_0,\dots,S_{t-1},A_{t-1},S_t\bigr)
  \quad (t\ge0).
}
$$

* **σ‑field generated by finitely many r.v.’s**
  For a finite list of coordinate maps \(X_1,\dots,X_m\) the σ‑field
  \(\sigma(X_1,\dots,X_m)\) is the smallest σ‑field on \(T\) that makes every \(X_i\) measurable.
  Concretely, it is generated by *cylinder sets* that fix the first \(m\) coordinates.

* **Why *stop* at \(S_t\) rather than include \(A_t\)?**
  In the timing convention used here (same as § 2), the agent **observes** state \(S_t\) *before* choosing action \(A_t\).
  Hence \(\mathcal H_t\) represents the **information available at decision time \(t\)**—no clairvoyance about \(A_t\) itself or future randomness.

* **Relation to the earlier filtration \((\mathcal F_t)\).**
  In § 2 we denoted \(\mathcal F_t\) exactly as \(\mathcal H_t\) is defined here, so
  \(\mathcal H_t \equiv \mathcal F_t\).
  The change of symbol simply emphasises that we now think of **histories \(h_t\)** as sample‑space points of their own.

---

## 2 History spaces \(\mathsf H_t\) — the *range* of \(H_t\)

### 2.1 Definition (4.2)

$$
\boxed{%
  \mathsf H_t := (S\times A)^{t}\times S .
}
$$

*The factorisation:*

$$
  h_t=(s_0,a_0,s_1,a_1,\dots ,s_{t-1},a_{t-1},s_t).
$$

### 2.2 σ‑field on \(\mathsf H_t\)

Because \(S,A\) are either finite/countable (discrete σ‑field) or Polish (Borel σ‑field), the product
\(\mathcal S\otimes\mathcal A\otimes\cdots\otimes\mathcal S\)
is again a **standard Borel σ‑field**.
We *call* it \(\mathcal H_t\) when viewed as the σ‑field on the *range* rather than on the trajectory space.

---

## 3 The history process \(H_t:T\to\mathsf H_t\)

\(H_t(\tau)=(S_0(\tau),A_0(\tau),\dots,S_t(\tau))\) is:

* \(\mathcal T/\mathcal H_t\)-measurable by construction, and
* **surjective** onto \(\mathsf H_t\).

Thus \(\mathcal H_t\) is both (i) the σ‑field generated by \(H_t\) on \(T\) *and* (ii) the canonical σ‑field on \(\mathsf H_t\).  This dual role lets us treat “history” either as an event on the trajectory space or as a *stand‑alone data object*.

---

## 4 Policy as a stochastic kernel on histories

### 4.1 The measurable mapping (4.3)

$$
\boxed{%
   \pi_t : (\mathsf H_t,\mathcal H_t)\;\longrightarrow\;(\Delta(A),\mathcal A_{\!\Delta}),
   \qquad t\ge0.
}
$$

* **\(\Delta(A)\)** — the probability simplex

  $$
     \Delta(A)=\Bigl\{p:A\to[0,1]\;|\;\sum_{a\in A}p(a)=1\Bigr\}.
  $$

  It is a closed subset of \(\mathbb R^{|A|}\) when \(A\) is finite, hence Polish; endowed with its Borel σ‑field \(\mathcal A_{\!\Delta}\).

* **Kernel property.**
  For every *fixed* \(h_t\in\mathsf H_t\), the map
  \(B\mapsto \pi_t(h_t)(B)\) is a probability measure on \((A,\mathcal A)\).
  For every *fixed* Borel set \(B\subseteq A\), the map \(h_t\mapsto\pi_t(h_t)(B)\) is \(\mathcal H_t\)-measurable.
  These two facts are exactly what “measurable → simplex” encodes.

* **Abbreviation (4.4)**

  $$
     \pi_t(a\mid h_t) := \bigl[\pi_t(h_t)\bigr](a), 
     \quad a\in A.
  $$

  Think of \(\pi_t(\cdot\mid h_t)\) as **action‑sampling distribution** conditioned on history.

### 4.2 Why measurability is essential

* **Non‑anticipativity (a.k.a. admissibility).**
  Because \(\pi_t\) takes *only* \(h_t\) as input, it cannot depend on future randomness.  This is the rigorous meaning of “policy uses only available information.”

* **Ionescu–Tulcea construction (revisited).**
  With \(\pi_t\) a measurable kernel, the composite kernel
  \(K_{2t+1}(h_t,da)=\pi_t(a\mid h_t)\) fits directly into the chronology of § 2.4.

---

## 5 Special classes of policies

| Class                       | Formal condition                                                                         | Consequence                                                                                             |
| --------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Deterministic**           | \(\pi_t(h_t)=\delta_{\alpha_t(h_t)}\) for some measurable map \(\alpha_t:\mathsf H_t\to A\). | \(A_t=\alpha_t(H_t)\) a.s. — no internal randomisation.                                                   |
| **Randomised**              | \(\exists h_t, \exists a_1\neq a_2: \pi_t(a_i\mid h_t)>0\).                                | Introduces exploration even with identical histories.                                                   |
| **Stationary (memoryless)** | \(\pi_t(h_t)=\pi(\cdot\mid s_t)\) depends only on current state \(s_t\).                     | The controlled process \((S_t)\) becomes a Markov chain; enables linear‑system policy evaluation (§ 2.6). |

*Remark.*  “Stationary” here means **time‑homogeneous**.  Some authors call policies that depend on \(S_t\) *only* (but still vary with \(t\)) **Markov** and reserve “stationary” for time‑invariant Markov policies.

---

## 6 How these notions feed downstream theory

| Topic                                   | Reliance on (4.1)–(4.4)                                                                                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Dynamic programming**                 | Bellman operator \(T^\pi\) is defined via expectation over \(\pi(\cdot\mid s)\).                                                        |
| **Policy gradients**                    | Score function \(\nabla_\theta\log\pi_\theta(A_t\mid H_t)\) is \(\mathcal H_t\)-measurable; the likelihood‑ratio trick needs this fact. |
| **Information‑theoretic regret bounds** | Kullback–Leibler computations condition on \(\mathcal H_t\) and integrate over \(\pi_t(\cdot\mid H_t)\).                                |
| **Partial‑observability**               | Replace \(H_t\) by observation histories \(O_{0:t}\); same kernel definition generalises immediately.                                   |
| **Causal inference in RL**              | “Interventions” must be functions of \(\mathcal H_t\); otherwise the causal graph fails the do‑calculus assumptions.                  |

---

## 7 Concrete example (finite case)

Let \(S=\{s_1,s_2\}, A=\{a_1,a_2\}\).

* **Deterministic memoryless:**
  $\pi_t(\cdot\mid h_t)=
   \begin{cases}
      \delta_{a_1} & \text{if } s_t=s_1,\\
      \delta_{a_2} & \text{if } s_t=s_2.
   \end{cases}$

* **Randomised history‑based (epsilon‑greedy):**
  Fix \(\varepsilon\in(0,1)\); define

  $$
     \pi_t(a\mid h_t)=
       \begin{cases}
         1-\varepsilon & \text{if } a=\arg\max_{a'}Q_t(h_t,a'),\\
         \varepsilon/|A| & \text{otherwise},
       \end{cases}
  $$

  where \(Q_t(h_t,a)\) is an empirical value estimate maintained by the algorithm.
  Measurability holds because \(Q_t\) is itself \(\mathcal H_t\)-measurable.

---

### One‑sentence takeaway

> Lines (4.1)–(4.4) formalise the intuitive idea of a *history‑dependent policy* by (i) defining the σ‑field \(\mathcal H_t\) that captures exactly what the agent has observed by time \(t\), (ii) treating histories as points of a product space \(\mathsf H_t\), and (iii) requiring each policy component \(\pi_t\) to be a **measurable kernel** from histories to probability distributions over actions—guaranteeing non‑anticipation, compatibility with the Ionescu–Tulcea trajectory measure, and a clean platform for dynamic‑programming and learning‑algorithm theory.

---

### 4.2 The agent–environment recursion

Fix an initial distribution \(\mu\in\Delta(S)\), an MDP \(M=(S,A,P,r,\gamma)\) and a policy \(\pi\).
The closed‑loop dynamics are the **stochastic recursion**

$$
\boxed{\;
\begin{aligned}
& S_0 \sim \mu, \\[2pt]
& A_t \mid \mathcal H_t \sim \pi_t(\,\cdot\mid H_t), \\[2pt]
& S_{t+1} \mid \mathcal H_t,A_t   \sim P_{A_t}(S_t,\cdot), \qquad t\ge 0 .
\end{aligned}}
\tag{4.5}
$$

Equation (4.5) states that (i) actions are chosen by the agent from the policy kernel,
and (ii) the environment’s next state depends only on the current state–action pair
(**Markov property**).&#x20;

---

### 4.3 Existence of a unique trajectory measure

\begin{theorem}\[Trajectory measure, Ionescu–Tulcea]\label{thm\:IT}
For every triple \((\mu,\pi,P)\) there exists a **unique** probability measure

$$
\mathbb P^{\pi}_{\mu}\quad\text{on}\quad\bigl(T,\mathcal T\bigr),
$$

with \(T=(S\times A)^{\mathbb N}\), such that the coordinate process
\((S_t,A_t)_{t\ge 0}\) obeys the recursion \textup{(4.5)}.
\end{theorem}

*Sketch.*  Construct successively the kernels
\(Q_0(s_0)=\mu(s_0)\),
\(R_t(h_t,a_t)=\pi_t(a_t\mid h_t)\) and
\(Q_{t+1}(h_t,a_t,s_{t+1})=P_{a_t}(s_t,s_{t+1})\).
Ionescu–Tulcea then yields a product measure on cylinders that extends uniquely to
\((T,\mathcal T)\).&#x20;

\paragraph{Canonical space.}
Because all randomness is captured by the coordinate maps, we may—and henceforth do—identify
\((\Omega,\mathcal F,\mathbb P^{\pi}_{\mu})\) with \(\bigl(T,\mathcal T,\mathbb P^{\pi}_{\mu}\bigr)\).
Expectations or probabilities of any trajectory‑measurable event are therefore independent of
the particular realisation.&#x20;

---

### 4.4 Stationary (memoryless) policies and induced Markov chains

A **stationary policy** is a measurable map

$$
\pi : S \longrightarrow \Delta(A), \qquad  
\pi(a\mid s)\equiv\Pr_\pi[A_t=a\mid S_t=s]\ \forall t .
\tag{4.6}
$$

Under such a policy the state process \(\{S_t\}\) is a time‑homogeneous Markov chain with transition
matrix

$$
P^{\pi}(s,s')\;:=\;\sum_{a\in A}\pi(a\mid s)\,P_a(s,s'),\qquad s,s'\in S,
\tag{4.7}
$$

and the reward kernel collapses to

$$
r^{\pi}(s)\;:=\;\sum_{a}\pi(a\mid s)\,r_a(s).
\tag{4.8}
$$

Hence for stationary \(\pi\) the closed loop is completely characterised by the pair
\((P^{\pi},r^{\pi})\).&#x20;

---

### 4.5 Deterministic vs. stochastic choices

* **Deterministic stationary policy:**
  \(\pi(a\mid s)=\mathbb 1\{a=\alpha(s)\}\) for some function \(\alpha:S\to A\).

* **Stochastic stationary policy:**
  \(\pi(\,\cdot\!\mid s)\) is a non‑trivial distribution, enabling exploration and
  convexification of achievable occupancy measures (Sec. 9).

Later (Sec. 7) we prove that in finite discounted MDPs there always exists an
**optimal deterministic stationary** policy, a cornerstone of classical dynamic
programming.&#x20;

---

### 4.6 Notational conventions for expectations and probabilities

Throughout the sequel we write

$$
\mathbb E^{\pi}_{\mu}[\,\cdot\,] \;:=\; \int_{T} (\cdot)\,d\mathbb P^{\pi}_{\mu},\qquad
\Pr^{\pi}_{\mu}[\,\cdot\,] \;:=\; \mathbb P^{\pi}_{\mu}(\,\cdot\,).
\tag{4.9}
$$

When \(\mu=\delta_s\) is a Dirac mass at state \(s\) we abbreviate
\(\mathbb E^{\pi}_{s}\equiv\mathbb E^{\pi}_{\delta_s}\) and similarly for probabilities.  This is
analogous to the \(V^\pi_M\) notation in Jiang’s notes.&#x20;

---

### 4.7 Why this formal machinery matters

1. **Well‑posed value functions.**
   The expectation \(v^\pi(s)=\mathbb E^{\pi}_{s}\bigl[\sum_{t\ge0}\gamma^{t}r_{A_t}(S_t)\bigr]\)
   is unambiguous because \(\mathbb P^{\pi}_{s}\) is unique (Thm \ref{thm\:IT}).

2. **Occupancy measures.**
   Definitions in Section 9 rely explicitly on the joint law of \((S_t,A_t)\).

3. **Policy transformation.**
   Later we convert an arbitrary history‑dependent policy into a stationary one
   that preserves its occupancy measure; the proof piggy‑backs on
   Eq. (4.5) and Theorem \ref{thm\:IT}.&#x20;

---

## 5 Probabilities over trajectories (full details)

### 5.1 Cylinder sets and finite‑dimensional events

For integers \(t\ge 0\) and sequences

$$
(s_{0:t},a_{0:t-1})\in S^{t+1}\times A^{t},
$$

define the **length‑\(t\) cylinder event**

$$
C_t(s_{0:t},a_{0:t-1})
\;=\;
\{\tau\in T : S_k(\tau)=s_k,\;A_k(\tau)=a_k\text{ for }0\le k\le t-1,\;
S_t(\tau)=s_t\}.
\tag{5.1}
$$

The collection
\(\mathscr C:=\{C_t(\cdot):t\ge0\}\) is a π‑system that generates the
trajectory σ‑field \(\mathcal T\). Hence specifying a probability measure on
\(\mathcal T\) is equivalent to specifying its values on all cylinders.&#x20;

---

### 5.2 Recursive factorisation (Ionescu–Tulcea)

Let \(\mu\in\Delta(S)\) and fix a policy \(\pi=(\pi_t)_{t\ge0}\).
Inductively define the kernels

$$
\begin{aligned}
Q_0(s_0)&=\mu(s_0),\\[3pt]
R_t(h_t,a_t) &= \pi_t(a_t\mid h_t),\\[3pt]
Q_{t+1}(h_t,a_t,s_{t+1}) &= P_{a_t}(s_t,s_{t+1}),
\end{aligned}
$$

with histories \(h_t=(s_{0:t},a_{0:t-1})\).
The **Ionescu–Tulcea theorem** then yields a unique probability
\(\mathbb P^{\pi}_{\mu}\) on \((T,\mathcal T)\) whose restriction to every
cylinder of length \(t\) is

$$
\boxed{\;
\mathbb P^{\pi}_{\mu}\!\bigl(C_t(s_{0:t},a_{0:t-1})\bigr)
=\mu(s_0)\prod_{k=0}^{t-1}
\pi_k\!\bigl(a_k\mid h_k\bigr)\,
P_{a_k}(s_k,s_{k+1})\!,
\quad h_k=(s_{0:k},a_{0:k-1}).
}
\tag{5.2}
$$

Equation (5.2) is the *finite‑dimensional distribution* of the closed
loop; it coincides with the informal chain‑rule expansion found in the
lecture notes.&#x20;

---

### 5.3 Infinite trajectories and uniqueness

Because the right‑hand side of (5.2) is a consistent family of
probabilities on the cylinders, Carathéodory’s extension theorem
guarantees **existence and uniqueness** of a measure on
\((T,\mathcal T)\) extending them.  Any other construction of the
process—e.g. on a larger probability space—induces the same
push‑forward measure, so expectations of trajectory‑measurable
functionals are independent of the realisation.&#x20;

---

### 5.4 Markov property revisited

For every \(t\ge0\) and measurable \(B\subseteq S\),

$$
\mathbb P^{\pi}_{\mu}(S_{t+1}\in B\mid\mathcal F_t,A_t)
\;=\;
\sum_{s'\in B}P_{A_t}(S_t,s')
\quad\mathbb P^{\pi}_{\mu}\text{-a.s.}
\tag{5.3}
$$

Eq. (5.3) is a direct corollary of the
kernel \(Q_{t+1}\) and constitutes the **Markov property** of the
state–action process.  It will be instrumental when we derive Bellman
equations and occupancy measures in later sections.&#x20;

---

### 5.5 Example: probability of a length‑\(t\) trajectory prefix

Write \(\tau_{0:t}=(s_0,a_0,\dots ,s_t)\).
Combining the chain rule with stationarity of the kernels gives

$$
\mathbb P^{\pi}_{\mu}(\tau_{0:t})
=\mu(s_0)\,
\Bigl[\prod_{k=0}^{t-1}\pi_k(a_k\mid h_k)\Bigr]\,
\Bigl[\prod_{k=0}^{t-1}P_{a_k}(s_k,s_{k+1})\Bigr],
\tag{5.4}
$$

which matches Eq. (5.2) and recovers the formula in Jiang’s
“MDP Preliminaries” notes.&#x20;

---

### 5.6 Integrability of the discounted return

For the discounted return
\(R(\tau)=\sum_{t\ge0}\gamma^{t}r_{A_t}(S_t)\) introduced in
Section 3, boundedness of \(r\) and monotone convergence give

$$
\int_{T}|R| d\mathbb P^{\pi}_{\mu} \le \frac{R_{\max}}{1-\gamma},
\tag{5.5}
$$

so \(R\in L^{1}(T,\mathcal T,\mathbb P^{\pi}_{\mu})\) and value functions \(v^{\pi}(s)=\mathbb E^{\pi}_{s}[R]\) are finite and well‑defined.

---

### 5.7 Bridge to occupancy measures

Equation (5.2) implies for every \((s,a)\),

$$
\mathbb P^{\pi}_{\mu}(S_t=s,A_t=a)
=\sum_{h_t: s_t=s} \mu(s_0)\!
\Bigl[\prod_{k=0}^{t-1}\pi_k(a_k\mid h_k)P_{a_k}(s_k,s_{k+1})\Bigr]\!
\pi_t(a\mid h_t),
\tag{5.6}
$$

so the discounted occupancy measure introduced in Section 9 can be
written as

$$
\nu^{\pi}_{\mu}(s,a)
=\sum_{t=0}^{\infty}\gamma^{t}\,
\mathbb P^{\pi}_{\mu}(S_t=s,A_t=a),
\tag{5.7}
$$

justifying its definition from first principles and preparing the ground
for dual LP and policy‑gradient arguments.&#x20;

---

## 6 Return, value functions and optimality — fully expanded


### 6.1 Discounted return as a measurable, bounded random variable

Let the closed‑loop system be \((\mu,M,\pi)\) with \(M=(S,A,P,r,\gamma),\;0\le\gamma<1\).
For each trajectory \(\tau=(S_0,A_0,S_1,\dots)\in T\) define the **discounted return**

$$
G(\tau)\;:=\;\sum_{t=0}^{\infty}\gamma^{t}\,r_{A_t}(S_t).
\tag{6.1}
$$

Because \(r\) is bounded, \(\lvert G(\tau)\rvert\le R_{\max}/(1-\gamma)\) and the series converges absolutely.
Equation (6.1) is \(\mathcal T\)-measurable (countable sum of measurable terms) and
\(G\in L^{\infty}(T,\mathcal T,\mathbb P^{\pi}_{\mu})\).  Hence all expectations below are finite.&#x20;

---

### 6.2 State‑ and action‑value functions

$$
\boxed{\;
\begin{aligned}
v^{\pi}(s) &:=\;\mathbb E^{\pi}_{s}\bigl[G\bigr],\\[2pt]
q^{\pi}(s,a) &:=\;\mathbb E^{\pi}_{s,a}\bigl[G\bigr]
           = r_a(s)+\gamma\sum_{s'}P_a(s,s')\,v^{\pi}(s').
\end{aligned}}
\tag{6.2}
$$

The second equality is a one‑step decomposition obtained by conditioning on the first transition.
Both \(v^{\pi}\) and \(q^{\pi}\) take values in the compact interval
\(\bigl[-R_{\max}/(1-\gamma),\,R_{\max}/(1-\gamma)\bigr]\).&#x20;

---

### 6.3 Linear algebraic form of policy evaluation

Fix a stationary policy \(\pi\).
Put states in an arbitrary order and set

$$
r^{\pi}(s):=\sum_{a}\pi(a\mid s)r_a(s),\qquad
P^{\pi}(s,s'):=\sum_{a}\pi(a\mid s)P_a(s,s').
\tag{6.3}
$$

> **Proposition 6.1 (Bellman equation for a fixed policy).**
> \(v^{\pi}=r^{\pi}+\gamma P^{\pi}v^{\pi}\).

\emph{Proof.}
Take expectations in (6.2) and apply the law of total expectation; see Proposition 1 in lec2\_pdf.  □

---

> **Corollary 6.2 (Closed‑form expression).**
> The matrix \(I-\gamma P^{\pi}\) is invertible and
>
> $$
> v^{\pi}=(I-\gamma P^{\pi})^{-1}r^{\pi}.
> \tag{6.4}
> $$

*Proof.*
For any non‑zero \(x\),
\(\lVert(I-\gamma P^{\pi})x\rVert_{\infty}\ge (1-\gamma)\lVert x\rVert_{\infty}>0\);
hence the matrix is non‑singular and the Neumann series converges.  □

---

### 6.4 Optimal value and Q‑functions

$$
v^{\star}(s):=\sup_{\pi}v^{\pi}(s),\qquad
q^{\star}(s,a):=r_a(s)+\gamma\sum_{s'}P_a(s,s')v^{\star}(s').
\tag{6.5}
$$

Because the policy space is finite‑dimensional and compact (simplex product), the supremum is attained.
Existence of an optimal \emph{deterministic} stationary policy will be shown in Section 7.&#x20;

---

### 6.5 Bellman optimality operator and equation

Define the **Bellman optimality operator**

$$
(Tv)(s):=\max_{a\in A}\bigl\{\,r_a(s)+\gamma\sum_{s'}P_a(s,s')v(s')\bigr\}.
\tag{6.6}
$$

> **Theorem 6.3 (Bellman optimality).**
> (i) \(T\) is a \(\gamma\)-contraction on \((\mathbb R^{|S|},\lVert\cdot\rVert_{\infty})\).
> (ii) \(v^{\star}\) is the unique fixed point of \(T\).
> (iii) Any greedy policy
> \(\pi^{\mathrm{greedy}}(s)\in\arg\max_{a}q^{\star}(s,a)\) is optimal.

*Proof sketch.*
Part (i) is Proposition “γ‑contraction of the Bellman operators’’ in lec2\_pdf.&#x20;
Part (ii) follows from Banach’s fixed‑point theorem.
Part (iii): if \(\pi\) is greedy w\.r.t. \(v^{\star}\) then
\(T^{\pi}v^{\star}=Tv^{\star}=v^{\star}\); Proposition 6.1 gives \(v^{\pi}=v^{\star}\). □

---

#### 6.6 Performance difference lemma (PDL)

Let \(d^{\pi}_{\mu}(s,a):=(1-\gamma)\sum_{t\ge0}\gamma^{t}\Pr^{\pi}_{\mu}(S_t=s,A_t=a)\)
be the **discounted occupancy measure** (see §9).

> **Lemma 6.4 (PDL).**
> For any stationary \(\pi,\pi'\) and start distribution \(\mu\),
>
> $$
> v^{\pi'}(\mu)-v^{\pi}(\mu)
> =\frac{1}{1-\gamma}\sum_{s,a}d^{\pi'}_{\mu}(s,a)\,\bigl[q^{\pi}(s,a)-v^{\pi}(s)\bigr].
> \tag{6.7}
> $$

*Proof.*  Detailed derivation given in note1.pdf, Prop. 2.  □

The PDL quantitatively links value improvement to the **advantage**
\(A^{\pi}(s,a)=q^{\pi}(s,a)-v^{\pi}(s)\).

---

#### 6.7 Bellman residual bounds

For any policy \(\pi\) and any value estimate \(u\),

$$
\lVert v^{\pi}-u\rVert_{\infty}\le
\frac{\lVert T^{\pi}u-u\rVert_{\infty}}{1-\gamma},
\qquad
\lVert v^{\star}-u\rVert_{\infty}\le
\frac{\lVert Tu-u\rVert_{\infty}}{1-\gamma}.
\tag{6.8}
$$

These follow by applying the contraction property to the error
\(e_k=(T^{\pi})^{k}u-v^{\pi}\) (or \(T\) for the optimal case) and summing a geometric series.
Equation (6.8) converts an easily–computed **Bellman residual** into an
upper bound on sub‑optimality—vital for algorithmic stopping criteria.&#x20;

---

#### 6.8 Value‑iteration complexity

Initialise \(v_0\equiv0\) and iterate \(v_{k+1}=Tv_k\).
The contraction proof yields

$$
\lVert v_k-v^{\star}\rVert_{\infty}\le \frac{\gamma^{k}}{1-\gamma}.
\tag{6.9}
$$

To reach an \(\varepsilon\)-accurate value (\(\lVert\cdot\rVert_{\infty}\)) it suffices that
$k\ge\lceil\ln\!\bigl(\varepsilon(1-\gamma)\bigr)/\ln\gamma\rceil\approx
\frac{\ln(1/\varepsilon)}{1-\gamma}$.  The same bound appears in the value‑iteration
theorem of lec2\_pdf.&#x20;

---

#### 6.9 Occupancy‑measure representation of the value (preview)

Equation (6.4) can be rearranged as

$$
v^{\pi}(\mu)=\frac{1}{1-\gamma}\sum_{s,a}d^{\pi}_{\mu}(s,a)\,r_a(s)
         =\langle d^{\pi}_{\mu},\,r\rangle,
\tag{6.10}
$$

anticipating Section 9 where
\(d^{\pi}_{\mu}=(1-\gamma)\mu(I-\gamma P^{\pi})^{-1}\mathrm{diag}(\pi)\).&#x20;

---

#### 6.10 Key take‑aways

* The Bellman operators \(T^{\pi}\) (linear) and \(T\) (non‑linear) are \(\gamma\)-contractions, guaranteeing unique fixed points and geometric convergence.
* Optimality can be certified locally via the Bellman gap \(Tv^{\pi}-v^{\pi}\) or globally via the PDL.
* Closed‑form solutions use \((I-\gamma P^{\pi})^{-1}\), but iterative methods have complexity \(O\!\bigl((1-\gamma)^{-1}\log(1/\varepsilon)\bigr)\).
* Value functions admit dual representations—as fixed points, as series, and as inner products with occupancy measures—providing multiple analytical tools for subsequent sections.

---

#### Progress

Section 6 has been re‑written with:

* formal proofs of the policy‑evaluation equation, matrix invertibility, and the Bellman optimality theorem;
* explicit contraction and residual‑error bounds with precise constants;
* a fully cited, line‑by‑line proof of the performance‑difference lemma;
* seamless links to forthcoming sections on occupancy measures and Bellman operators.

If you need further expansion (e.g., average‑reward analogue or finer error analysis), just let me know.

---

## 7 Memoryless versus general policies and the Fundamental Theorem

### 7.1 Taxonomy of policies

| qualifier                   | notation              | definition                                       | free parameters   |   |           |   |                |
| --------------------------- | --------------------- | ------------------------------------------------ | ----------------- | - | --------- | - | -------------- |
| **history‑dependent**       | \(\pi=(\pi_t)_{t\ge0}\) | \(\pi_t(a\mid h_t)\) depends on full history \(h_t\) | arbitrary kernels |   |           |   |                |
| **stationary (memoryless)** | \(m:S\!\to\!\Delta(A)\) | \(m(a\mid s_t)\) uses *only* the current state     | (                 | S | \times(   | A | !-!1)) numbers |
| **deterministic**           | \(\alpha:S\!\to\!A\)    | \(A_t=\alpha(S_t)\) w\.p. 1                        | (                 | S | ) actions |   |                |
| **stochastic**              | —                     | non‑degenerate distribution in ≥ 1 state         | probabilities     |   |           |   |                |

Lecture 2 introduces the succinct notation \(m(a\mid s)\equiv m(s)(a)\) and emphasises that a memoryless policy turns the joint process \((S_t,A_t)\) into a time‑homogeneous Markov chain .

---

### 7.2 Discounted occupancy measures

For a start distribution \(\mu\) and arbitrary policy \(\pi\) define

$$
\nu^{\pi}_{\mu}(s,a)
=\sum_{t=0}^{\infty}\gamma^{t}\,\Pr^{\pi}_{\mu}(S_t=s,A_t=a),\qquad  
d^{\pi}_{\mu}:=(1-\gamma)\,\nu^{\pi}_{\mu}.
\tag{7.1}
$$

Equation (7.1) is identical to the lecture‑note definition and satisfies the identity
\(v^{\pi}(\mu)=\langle \nu^{\pi}_{\mu},r\rangle\) .


## 1 Definitions and first properties

### 1.1 Discounted visitation counts

For a fixed **start‑state distribution** \(\mu\) and **policy** \(\pi\):

$$
\boxed{%
   \nu^{\pi}_{\mu}(s,a)
   :=\sum_{t=0}^{\infty}\gamma^{t}\;
        \Pr^{\pi}_{\mu}\bigl(S_t=s,\,A_t=a\bigr),
   \qquad (s,a)\in S\times A,
}
\tag{7.1a}
$$

where \(\gamma\in[0,1)\) is the discount factor.

*Interpretation.*  \(\nu^{\pi}_{\mu}(s,a)\) is the **expected discounted number of times** the pair \((s,a)\) is encountered along a trajectory that starts from \(\mu\) and follows \(\pi\).

---

### 1.2 Scaled occupancy \(d^{\pi}_{\mu}\)

Define

$$
\boxed{%
   d^{\pi}_{\mu}(s,a):=(1-\gamma)\,\nu^{\pi}_{\mu}(s,a).
}
\tag{7.1b}
$$

The factor \((1-\gamma)\) normalises the weights so that

$$
\sum_{s,a} d^{\pi}_{\mu}(s,a)=1,
\tag{7.2}
$$

i.e. \(d^{\pi}_{\mu}\) is a **probability distribution** over state–action pairs.
(The proof uses the geometric‑series identity—see § 1.4.)

---

## 2 Relationship to the value function

### 2.1 Inner‑product identity

Let \(r(s,a)\) be the immediate reward function (bounded by \(R_{\max}\)).
Because expectation and an absolutely convergent sum commute,

$$
\begin{aligned}
v^{\pi}(\mu)
&:=\mathbb E^{\pi}_{\mu}\!\Bigl[\;\sum_{t=0}^{\infty}\gamma^{t}r_{A_t}(S_t)\Bigr]  \\[2mm]
&=\sum_{t=0}^{\infty}\gamma^{t}
    \sum_{s,a} r(s,a)\;
                \Pr^{\pi}_{\mu}(S_t=s,A_t=a) \\[2mm]
&=\sum_{s,a} r(s,a)\;
             \underbrace{\Bigl[\sum_{t=0}^{\infty}\gamma^{t}
                    \Pr^{\pi}_{\mu}(S_t=s,A_t=a)\Bigr]}_{\nu^{\pi}_{\mu}(s,a)} \\[2mm]
&=\langle \nu^{\pi}_{\mu},\,r\rangle.
\end{aligned}
\tag{7.3}
$$

> **Equation (7.1) ⇒ Value identity:**
>
> $$
> \boxed{\;
> v^{\pi}(\mu)=\sum_{s,a} \nu^{\pi}_{\mu}(s,a)\;r(s,a)
> \;=\;
> \langle \nu^{\pi}_{\mu},\,r\rangle.
> }
> $$
>
> The angled bracket denotes the standard dot product when \(S,A\) are finite.

---

## 3 Flow (balance) equation for \(\nu^{\pi}_{\mu}\)

Discounted occupancy can be characterised **without explicit time summation**.
For every state \(s\):

$$
\underbrace{\mu(s)}_{\text{initial mass}}
+\gamma\sum_{s',a'}\nu^{\pi}_{\mu}(s',a')\,P_{a'}(s',s)
=\sum_{a}\nu^{\pi}_{\mu}(s,a).
\tag{7.4}
$$

*Reading left to right.*

1. Start with probability \(\mu(s)\) at time 0.
2. Add the discounted flow that arrives from any predecessor \((s',a')\) in one step, weighted by \(\gamma\).
3. The result equals the total discounted mass that **starts** new transitions from \(s\).

Equation (7.4) is the **discounted conservation‑of‑probability** constraint; together with \(d^{\pi}_{\mu}=(1-\gamma)\nu^{\pi}_{\mu}\) and the normalisation (7.2) it provides a *linear* description of the set of all feasible occupancies.

---

## 4 Why occupancy measures are fundamental

| Use‑case                           | Role of \(\nu^{\pi}_{\mu}\) / \(d^{\pi}_{\mu}\)                                                                                                                                                               |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Policy‑gradient theorem**        | The gradient of \(v^{\pi}(\mu)\) w\.r.t. policy parameters takes the form  \(\displaystyle \nabla_\theta v^{\pi}(\mu) = \sum_{s,a} d^{\pi}_{\mu}(s,a)\;\nabla_\theta \log\pi_\theta(a\mid s)\;Q^{\pi}(s,a)\). |
| **Off‑policy evaluation**          | Importance‑sampling weights at time \(t\) telescope into a ratio between discounted occupancy measures of behaviour and target policies.                                                                    |
| **Convex optimisation view of RL** | The control problem  \(\max_{\pi} v^{\pi}(\mu)\) can be rewritten as a *linear programme* over \(d(s,a)\) subject to the flow constraints (7.4).                                                              |
| **Exploration criteria**           | Algorithms such as “cover time” or “visit‑density bonus” use \(d^{\pi}_{\mu}(s)\!=\!\sum_{a}d^{\pi}_{\mu}(s,a)\) as the target distribution they seek to flatten.                                           |

---

## 5 Verification of key properties

### 5.1 Boundedness and convergence

Because \(\sum_{t\ge0}\gamma^{t}=1/(1-\gamma)\) and each probability is ≤ 1,

$$
0\;\le\;\nu^{\pi}_{\mu}(s,a)
      \;\le\;\frac{1}{1-\gamma},
\qquad
\lVert\nu^{\pi}_{\mu}\rVert_1\;=\;\frac{1}{1-\gamma}.
\tag{7.5}
$$

Hence \(d^{\pi}_{\mu}\) is always a proper probability distribution.

### 5.2 State‑only occupancy

Define

$$
d^{\pi}_{\mu}(s):=\sum_{a}d^{\pi}_{\mu}(s,a).
$$

Then \(d^{\pi}_{\mu}\) is the discounted state‑visitation distribution; it satisfies a simplified flow constraint obtained from (7.4) by summing over actions.

### 5.3 Stationary‑policy simplification

If \(\pi\) is stationary with matrix representation \(P^{\pi}\),

$$
\nu^{\pi}_{\mu} 
    = \sum_{t=0}^{\infty}\gamma^{t}\,\mu^\top(P^{\pi})^{t} \,\Pi,
$$

where \(\Pi\) is the \(|S|\times|S||A|\) block that replicates the state‑probability row according to \(\pi(\cdot\mid s)\).  The infinite sum has the closed form
\(\mu^\top(I-\gamma P^{\pi})^{-1}\Pi\) (geometric‑series of matrices).

---

## 6 Worked numerical micro‑example

Suppose \(S=\{s_1,s_2\}\), \(A=\{a_1,a_2\}\), \(\gamma=0.9\), start state \(s_1\) with probability 1, and policy

| state | \(\pi(a_1\mid s)\) | \(\pi(a_2\mid s)\) |
| ----- | ---------------- | ---------------- |
| \(s_1\) | 0.8              | 0.2              |
| \(s_2\) | 0.5              | 0.5              |

If the transition kernel always alternates the state (for simplicity), then
\(\Pr(S_t=s_1)=1\) for even \(t\) and \(0\) for odd \(t\).
Calculating two terms:

$$
\begin{aligned}
\nu^{\pi}_{\mu}(s_1,a_1)
 &\approx 0.8\cdot(1 + 0.9^2 + 0.9^4+\dots)
 =0.8\cdot\frac{1}{1-0.9^2}=4.21,\\[2mm]
d^{\pi}_{\mu}(s_1,a_1)
 &=(1-0.9)\,4.21\approx0.421.
\end{aligned}
$$

Summing all four \((s,a)\) pairs yields 1, confirming the normalisation.

---

### One‑sentence takeaway

> The discounted occupancy measure \(\nu^{\pi}_{\mu}\) counts, with geometric fading, how often each state–action pair is visited under a policy; normalising by \((1-\gamma)\) turns it into a bona‑fide probability distribution \(d^{\pi}_{\mu}\) that (i) satisfies simple linear flow constraints, (ii) renders the value function as an inner product \(v^{\pi}(\mu)=\langle\nu^{\pi}_{\mu},r\rangle\), and (iii) underpins policy‑gradient identities, linear‑programming formulations of control, and many practical exploration and evaluation techniques in reinforcement learning.

---

### 7.3 From arbitrary to memoryless policies

\begin{theorem}\[Occupancy‑measure realisation]\label{thm\:om-realisation}
For every policy \(\pi\) and start distribution \(\mu\) there exists a **stationary** policy
\(m_{\mu,\pi}\) such that

$$
\nu^{m_{\mu,\pi}}_{\mu}\;=\;\nu^{\pi}_{\mu},
\qquad
v^{m_{\mu,\pi}}(\mu)=v^{\pi}(\mu).
\tag{7.2}
$$

\end{theorem}

*Proof outline.*
Define \(m_{\mu,\pi}(a\mid s):=\nu^{\pi}_{\mu}(s,a)\big/\!\sum_{a'}\nu^{\pi}_{\mu}(s,a')\).
Because the discounted flow constraint

$$
d^{\pi}_{\mu}(\cdot,a)\;\text{marginalises to}\;(1-\gamma)\mu+\gamma d^{\pi}_{\mu}P  
$$

holds (see dual LP discussion in note1) the constructed \(m_{\mu,\pi}\) reproduces exactly the same one‑step flows, hence the same \(\nu\) and value .
A complete algebraic proof is given in lec2\_pdf, Theorem “for any policy … there exists a memoryless policy” .

---

## 1 Recap of discounted occupancy

For start distribution \(\mu\) and arbitrary policy \(\pi\),

$$
\nu^{\pi}_{\mu}(s,a)
   :=\sum_{t=0}^{\infty}\gamma^{t}\Pr^{\pi}_{\mu}\{S_t=s,A_t=a\},
\qquad
d^{\pi}_{\mu}:=(1-\gamma)\,\nu^{\pi}_{\mu}.
\tag{1.1}
$$

### 1.1 Flow (balance) constraint

The *scaled* occupancy \(d:=d^{\pi}_{\mu}\) satisfies, for every state \(s\),

$$
\boxed{\;
   (1-\gamma)\,\mu(s)
   \;+\;
   \gamma
   \sum_{s',a'} d(s',a') \,P_{a'}(s',s)
   \;=\;
   \sum_{a} d(s,a).
\;}
\tag{1.2}
$$

*Derivation.*
Write the definition of \(d\), shift the time index in the inflow term by \(+1\), and use the one‑step kernel \(P\); see § 7.2 equation (7.4).

*Interpretation.*  Probability mass that *arrives* at state \(s\) (initial + discounted inflow) equals the mass that *leaves* \(s\) (discounted visits).

---

## 2 Constructing a stationary policy from \(d\)

Set

$$
m(a\mid s):=
\begin{cases}
\displaystyle \frac{d(s,a)}{\sum_{a'} d(s,a')} &\text{if }\sum_{a'} d(s,a')>0,\\[4mm]
\text{an arbitrary distribution on }A &\text{otherwise}.
\end{cases}
\tag{2.1}
$$

*Notes.*

* If a state is **never** visited under \(\pi\) (the denominator is \(0\)), the choice of \(m(\cdot\mid s)\) is irrelevant—such states contribute nothing to \(\nu\) or to the value.
* \(m\) is **stationary** (independent of time) and **Markov** (depends only on \(s\)).

---

## 3 Proving \(\nu^{m}_{\mu}=\nu^{\pi}_{\mu}\)

### 3.1 Show that \(d^{m}_{\mu}\) solves the same balance equation

For policy \(m\), the scaled occupancy \(d^{m}_{\mu}\) satisfies (1.2) **with \(m\) instead of \(\pi\)**:

$$
(1-\gamma)\mu
   +\gamma d^{m}_{\mu}P
   =d^{m}_{\mu}\Pi_m,
\tag{3.1}
$$

where \(\Pi_m\) is the \(|S|\!\times\!|S||A|\) block that appends \(m(\cdot\mid s)\) to each state row.

### 3.2 Plug the definition of \(m\)

Because \(m(a\mid s)=\frac{d(s,a)}{\sum_{b}d(s,b)}\) whenever \(d(s):=\sum_{b}d(s,b)>0\),

$$
d\,\Pi_m
  =\bigl[\;d(s,a)\;\bigr]_{(s,a)}
  =d.
\tag{3.2}
$$

Thus inserting \(d\) into (3.1) *exactly* reproduces the original constraint (1.2).  *Therefore \(d\) satisfies the balance equation for the policy \(m\) as well.*

### 3.3 Uniqueness of the discounted occupancy solution

Fix \(\mu\) and \(m\).  The linear system (3.1) together with the normalisation \(\sum_{s,a} d(s,a)=1\) has a **unique** solution (the coefficient matrix is a contraction because \(\gamma<1\)).  Since both \(d\) and \(d^{m}_{\mu}\) satisfy it, they must coincide:

$$
d^{m}_{\mu}=d^{\pi}_{\mu}.
\tag{3.3}
$$

Multiply by \(1/(1-\gamma)\) to get the desired equality of the unscaled occupancies:

$$
\nu^{m}_{\mu}=\nu^{\pi}_{\mu}.
$$

---

## 4 Equality of value functions

Using the inner‑product identity from § 7.2,

$$
v^{m}(\mu)
  =\langle \nu^{m}_{\mu},r\rangle
  =\langle \nu^{\pi}_{\mu},r\rangle
  =v^{\pi}(\mu).
\tag{4.1}
$$

---

## 5 Interpretation and consequences

| Aspect                         | Explanation                                                                                                                                                                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Compression**                | Any history‑dependent policy “spreads” its discounted visit mass \(d\) over state–action pairs.  Sampling actions *proportionally* to that mass in each state **reproduces** the same long‑run discounted statistics.                   |
| **Optimal‑control corollary**  | Because \(v^{\pi}(\mu)=v^{m}(\mu)\), *there always exists a stationary policy that is at least as good as any history‑dependent policy*.  Hence searching the stationary‑policy space is sufficient for optimality in discounted tasks. |
| **Linear‑programming duality** | The feasible set in the primal LP is the convex polytope of \$d\$ satisfying (1.2); Theorem 7.2 shows that *every* extreme point (and in fact every interior point) can be realised by a stationary policy.                           |
| **Algorithmic takeaway**       | Dynamic‑programming and policy‑iteration algorithms restrict attention to state‑based policies without loss.  Policy‑gradient theorems base their derivations on \(d^{\pi}_{\mu}\), so they implicitly assume the compression result.   |

---

## 6 Edge cases and technical remarks

1. **Zero‑visit states.**  If \(d(s)=0\), \(m(\cdot\mid s)\) can be arbitrary.  This is harmless because such \(s\) never influence the occupancy or value.
2. **Deterministic‑vs‑randomised realiser.**  The constructed \(m\) is generally **stochastic**.  A deterministic realiser may not exist if \(d(s,a)\) is fractional for more than one \(a\); trying to force determinism would break (3.2).
3. **Countable / continuous spaces.**  Replace sums with integrals and ratios with Radon–Nikodym derivatives.  The proof carries through provided \(d(s)\) is σ‑finite (true because \(d\) is a probability measure).

---

### One‑sentence takeaway

> By taking the **discount‑weighted visitation frequencies** generated by any possibly history‑dependent policy and replaying them as **state‑conditioned action probabilities**, one obtains a *stationary* policy that achieves *exactly* the same occupancy measure and, therefore, the same expected discounted return—so stationary policies are universally sufficient in discounted MDPs.

---

### 7.4 Sufficiency of stationary policies

\begin{corollary}\[Optimality over the stationary class]\label{cor\:stationary-suffice}

$$
\sup_{\pi\ \text{arbitrary}} v^{\pi}(\mu)
\;=\;
\sup_{m\ \text{stationary}} v^{m}(\mu).
\tag{7.3}
$$

\end{corollary}

*Proof.* For any \(\pi\) apply Theorem \ref{thm\:om-realisation} to get a stationary policy of equal value; taking suprema preserves equality.

---

### 7.5 From stochastic to deterministic

Fix a stationary **stochastic** policy \(m\).
Define the deterministic selector

$$
\alpha(s)\in\arg\max_{a\in A} q^{m}(s,a),
\tag{7.4}
$$

and let \(m^{\mathrm{greedy}}\) be the corresponding deterministic policy.

> **Lemma 7.1 (Greedy improvement).**
> \(v^{m^{\mathrm{greedy}}}(s)\ge v^{m}(s)\) for every \(s\); inequality is strict in any state where \(m\) did not already place full mass on \(\arg\max_{a}q^{m}(s,a)\).

*Proof.* Immediate from the performance‑difference lemma with advantage \(A^{m}\ge 0\) and greediness ensuring non‑negativity .

Iterating Lemma 7.1 over the (finite) state set yields a deterministic stationary policy that is *no worse* than the starting policy.

Below is a **step‑by‑step, measure‑theoretic walkthrough** of the two claims that close Section 7, namely

* **Corollary 7.4** – *“stationary (memory‑less) policies suffice for optimality,”* and
* **Lemma 7.1** – *“greedy (deterministic) improvement within the stationary class.”*

The exposition assumes the discounted, bounded‑reward MDP setting introduced earlier:

* \(S,A\) finite (extensions to countable / Borel spaces follow by replacing sums with integrals);
* discount factor \(\gamma\in[0,1)\);
* reward bound \(|r_a(s)|\le R_{\max}\);
* start distribution \(\mu\in\Delta(S)\).

---

## 1 Corollary 7.4 – Optimality over the stationary class

$$
\boxed{\;
   \sup_{\pi\;\text{arbitrary}} v^{\pi}(\mu)
   \;=\;
   \sup_{m\;\text{stationary}} v^{m}(\mu).
}
\tag{C‑7.3}
$$

### 1.1 Key input – Theorem 7.2 (occupancy‑measure realisation)

> For every (possibly history‑dependent) policy \(\pi\) there exists a **stationary** policy \(m_{\mu,\pi}\) such that
>
> $$
>    \nu^{m_{\mu,\pi}}_{\mu}=\nu^{\pi}_{\mu},
>    \quad\Longrightarrow\quad
>    v^{m_{\mu,\pi}}(\mu)=v^{\pi}(\mu).
> $$
>
> (See previous explanation for construction and proof.)

### 1.2 Proof of the corollary

* **Step 1 – “≤” direction.**
  For *any* arbitrary policy \(\pi\) Theorem 7.2 provides a stationary policy with *exactly* the same value.
  Hence

  $$
     v^{\pi}(\mu)\;\le\;
     \sup_{m\text{ stationary}} v^{m}(\mu).
  $$

  Taking the supremum over **all** \(\pi\) yields

  $$
     \sup_{\pi\;\text{arbitrary}} v^{\pi}(\mu)
       \;\le\;
     \sup_{m\;\text{stationary}} v^{m}(\mu).
  $$

* **Step 2 – “≥” direction.**
  Because every stationary policy is a special case of an arbitrary policy,

  $$
     \sup_{m\;\text{stationary}} v^{m}(\mu)
       \;\le\;
     \sup_{\pi\;\text{arbitrary}} v^{\pi}(\mu).
  $$

Combine the two inequalities to obtain equality (C‑7.3). ∎

**Interpretation.**
Searching the full space of history‑dependent strategies offers **no extra value** beyond the simpler class of time‑homogeneous, state‑based policies.  This justifies dynamic‑programming algorithms that operate exclusively on stationary policies.

---

## 2 Lemma 7.1 – From stochastic to deterministic within the stationary class

### 2.1 Prerequisites and notation

* Fix a **stationary stochastic** policy \(m(\cdot\mid s)\).
* Define its **state‑value** \(v^{m}(s)\) and **action‑value** (Q‑value)

  $$
     q^{m}(s,a):=
       r_a(s)
       +\gamma\sum_{s'}P_a(s,s')\,v^{m}(s').
  $$
* Let

  $$
     \alpha(s)\in\arg\max_{a}q^{m}(s,a)
  $$

  be a measurable maximiser (possible because \(A\) is finite).
  The resulting **deterministic stationary** policy is

  $$
     m^{\text{greedy}}(a\mid s)=\mathbf 1\!\{a=\alpha(s)\}.
  $$

### 2.2 Performance‑difference lemma (discounted case)

For any two stationary policies \(m\) and \(m'\),

$$
v^{m'}(\mu)-v^{m}(\mu)
   =\frac{1}{1-\gamma}
      \sum_{s} d^{m'}_{\mu}(s)\;
         \sum_{a}\!\bigl[m'(a\mid s)-m(a\mid s)\bigr]\,
         q^{m}(s,a),
\tag{2.1}
$$

where \(d^{m'}_{\mu}(s)=\sum_{a}d^{m'}_{\mu}(s,a)\) is the discounted state‑occupancy under \(m'\).
**Proof sketch.**  Substitute the occupancy inner‑product identity (§ 7.2) for both values, subtract, and use the linear flow constraint to telescope future‑value terms (standard in RL texts).

### 2.3 Applying (2.1) with \(m'=m^{\text{greedy}}\)

* For each state \(s\),

  $$
    m^{\text{greedy}}(a\mid s)-m(a\mid s)
      =
    \begin{cases}
       1-m(\alpha(s)\mid s) & a=\alpha(s),\\
       -m(a\mid s)         & a\neq\alpha(s).
    \end{cases}
  $$

* Because \(\alpha(s)\) maximises \(q^{m}(s,\cdot)\), every term
  \(\bigl[m^{\text{greedy}}(a\mid s)-m(a\mid s)\bigr]\,q^{m}(s,a)\) is **non‑negative**, and it is strictly positive whenever \(m\) assigns < 1 probability mass to the arg‑max set.

* Since \(d^{m^{\text{greedy}}}_{\mu}(s)\ge0\) for all \(s\), the overall sum in (2.1) is

  $$
     v^{m^{\text{greedy}}}(\mu)-v^{m}(\mu)\;\ge\;0,
  $$

  with **strict** inequality if any state exhibits stochasticity away from the greedy action.

### 2.4 State‑wise inequality

The same reasoning applied **state‑by‑state** gives

$$
v^{m^{\text{greedy}}}(s)\;\ge\;v^{m}(s)
\quad\text{for every }s,
$$

because the local Bellman operator uses expectations over actions.  Again, the inequality is strict in any state where \(m(\cdot\mid s)\) is not already concentrated on the maximiser(s).

∎

---

## 3 Iterating greedy improvement ⇒ deterministic optimal policy

Because the state set \(S\) is finite, one can perform **Howard’s policy‑iteration cycle**:

1. **Evaluation:**  Solve \((I-\gamma P^{m})v^{m}=r^{m}\) to get \(v^{m}\).
2. **Improvement:**  Produce \(m^{\text{greedy}}\).
3. **Test for change:**  If \(m^{\text{greedy}}=m\), stop (optimal). Otherwise set \(m\leftarrow m^{\text{greedy}}\) and repeat.

Each improvement step yields a strictly larger value at *some* state (Lemma 7.1), and the number of distinct deterministic stationary policies is \(|A|^{|S|}<\infty\); hence convergence occurs in finitely many iterations.  The limiting policy is deterministic, stationary, and **optimal**:

$$
v^{m^{\star}}(\mu)=\sup_{\pi}v^{\pi}(\mu).
$$

---

## 4 Summary & practical implications

| Result                    | Take‑away                                                                                                                                                                                           |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Corollary 7.4**         | To find an *optimal* policy in a discounted finite MDP it is sufficient to optimise over **stationary** (time‑homogeneous, state‑based) policies.                                                   |
| **Lemma 7.1 + iteration** | Within the stationary class it is sufficient to consider **deterministic** policies: do a single greedy improvement step to get a policy that is at least as good, and iterate to reach optimality. |
| **Algorithms**            | Dynamic programming (value‑/policy‑iteration), linear programming, and modern actor–critic methods all rely on these sufficiency results to keep the policy parameter space manageable.             |

---

### One‑sentence takeaway

> The occupancy‑measure realisation theorem compresses any history‑dependent strategy into an equally good stationary one, and a single greedy step within that stationary class never hurts and usually helps; iterated over a finite state set, this guarantees the existence—and algorithmic attainability—of an **optimal deterministic stationary policy** for every discounted MDP.

---

### 7.6 Fundamental Theorem of finite discounted MDPs

\begin{theorem}\[Fundamental Theorem]\label{thm\:fundamental}
In every finite discounted MDP

$$
\exists\ \text{deterministic stationary } \alpha^{\star}
\quad\text{s.t.}\quad
v^{\alpha^{\star}} = v^{\star}.
\tag{7.5}
$$

Moreover \(v^{\star}\) is the unique fixed point of the Bellman optimality operator
and every deterministic greedy policy w\.r.t. \(v^{\star}\) is optimal.
\end{theorem}

*Proof.*

1. By Corollary \ref{cor\:stationary-suffice} restrict attention to stationary policies.
2. Among these, pick one with maximal value; if it is stochastic apply the greedy‑improvement sequence, which strictly increases the value in at least one state until no further improvement is possible—at most \(|A|^{|S|}\) iterations.
3. The resulting deterministic policy \(\alpha^{\star}\) satisfies the Bellman optimality equation, hence is optimal.
   Detailed derivations appear in lec2\_pdf pp. 5‑6 and note1 §1.4 .

---

### 7.7 Complexity implications

Because an optimal policy can be sought in the *finite* set \(A^{S}\), dynamic‑programming algorithms evaluate at most \(|A|^{|S|}\) candidates in the worst case, and in practice far fewer thanks to monotone policy‑improvement. The lecture notes remark that this bypasses the exponential blow‑up that would occur if arbitrary history‑dependent policies were considered .

---

### 7.8 Take‑aways for practitioners

* Theoretical analysis and planning algorithms (value‑iteration, policy‑iteration, LP) may assume deterministic stationary policies without loss of optimality.
* Stochastic or history‑dependent policies are *implementation tools* (e.g., exploration) rather than *requirements* for optimality.
* Occupancy measures provide a unifying lens: they (i) yield linear programming formulations; (ii) justify stationary sufficiency; and (iii) underpin modern policy‑gradient and inverse‑RL methods.

---

### Progress

Section 7 delivers the full proof path:

1. **Occupancy‑measure realisation** ⇒ stationary sufficiency.
2. **Greedy improvement** ⇒ deterministic sufficiency.
3. **Fundamental theorem** tying both to the Bellman optimality equation.

With this foundation we are ready for Section 8, which dissects objective‑function variants and modelling choices in greater depth.

---

## 8 Objective functions and modelling choices

This section formalises the **reward model** and the most common **performance criteria** used in MDPs, explains how they relate, and highlights the analytical consequences of each choice.

---

### 8.1 Reward kernel, boundedness and shifts

$$
r:A\times S\longrightarrow\mathbb R,\qquad  
R_{\max}:=\sup_{s,a}|r_a(s)|<\infty.
\tag{8.1}
$$

*Bounded rewards* guarantee the discounted return is finite (Sec. 3).
If rewards can be negative but have a bounded range \([\!-\!a,\,b]\) one may add the constant offset \(c=a\) without affecting optimal policies, because every value shifts by \(c/(1-\gamma)\).  This normalisation will be used repeatedly below. &#x20;

---

### 8.2 Infinite‑horizon discounted objective (baseline)

$$
G^{\gamma}(\tau):=\sum_{t=0}^{\infty}\gamma^{t}r_{A_t}(S_t),\qquad  
v^{\pi}_{\gamma}(s):=\mathbb E^{\pi}_{s}[G^{\gamma}],\quad 0\le\gamma<1.
\tag{8.2}
$$

Properties already proved:

* \(G^{\gamma}\) is measurable and bounded by \(R_{\max}/(1-\gamma)\).
* Bellman operators are γ‑contractions → fast fixed‑point iteration (§6).
* Effective horizon \(H_{\gamma,\varepsilon}\approx(1-\gamma)^{-1}\) (Sec. 3).


Because of the contraction, **discounting is the preferred objective in most theoretical analyses** and in algorithms such as value‑iteration and policy‑iteration.

---

### 8.3 Finite‑horizon undiscounted objective

Fix a horizon \(H\in\mathbb N\):

$$
G^{H}(\tau):=\sum_{t=0}^{H-1}r_{A_t}(S_t),\qquad  
v^{\pi}_{H}(s):=\mathbb E^{\pi}_{s}[G^{H}].
\tag{8.3}
$$

*Dynamic programming.*

Define backward‑induction value functions \(V_t(s)\) for \(t=H,\dots,0\):

$$
V_{H}(s)=0,\qquad  
V_{t}(s)=\max_{a}\bigl\{r_a(s)+\sum_{s'}P_a(s,s')V_{t+1}(s')\bigr\}.
\tag{8.4}
$$

The optimal non‑stationary policy is
\(\pi^{\star}_t(s)=\arg\max_{a}(\cdot)\).  The problem therefore lives in an
\((H\times|S|)\)-dimensional space, not \(|S|\).

*Emulating finite horizon inside discounted MDPs.*
Augment the state with a time‑counter \(h\in\{0,\dots,H\}\) and set \(\gamma=1\); introduce an absorbing state after step \(H\).  The optimal policy in the augmented MDP reproduces Eq. (8.4).&#x20;

---

### 8.4 Infinite‑horizon average‑reward objective

Assume **ergodicity** under every stationary policy (each induces a single recurrent class).
Define

$$
\rho^{\pi}(s):=\lim_{T\to\infty}\frac1T
\,\mathbb E^{\pi}_{s}\Bigl[\sum_{t=0}^{T-1}r_{A_t}(S_t)\Bigr],
\quad
\rho^{\star}(s):=\sup_{\pi}\rho^{\pi}(s).
\tag{8.5}
$$

*Bias (relative‑value) function.*
Pick a reference state \(s_0\).  The pair \((\rho,h)\) solves the **average‑reward Bellman equations**

$$
\rho^{\star}+h(s)=\max_{a}\bigl\{r_a(s)+\sum_{s'}P_a(s,s')\,h(s')\bigr\},
\quad h(s_0)=0.
\tag{8.6}
$$

Relative value‑iteration
\(h_{k+1}=T h_k - h_k(s_0)\) converges linearly with modulus \(\gamma_{\text{mix}}\), the second‑largest eigenvalue of the transition matrix; but **no uniform contraction** exists without additional mixing assumptions.  Consequently proofs and algorithms are more delicate than in the discounted case.&#x20;

---

### 8.5 Total‑cost / stochastic shortest‑path objective

Set \(\gamma=1\) but assume an **absorbing set** \(S_{\text{abs}}\subseteq S\) that is reached with probability 1 under all policies.  The total‑cost return

$$
G^{\text{TC}}(\tau)=\sum_{t=0}^{T_{\text{abs}}-1}r_{A_t}(S_t),\qquad  
T_{\text{abs}}=\inf\{t:S_t\in S_{\text{abs}}\},
\tag{8.7}
$$

is finite.  Dynamic programming uses the same equations as (8.4) with a random horizon \(T_{\text{abs}}\).  For deterministic shortest‑path problems rewards are non‑positive costs, and the objective is minimisation.

---

### 8.6 Risk‑sensitive and other criteria (brief survey)

| Objective               | Form                                        | Notes                                                  |
| ----------------------- | ------------------------------------------- | ------------------------------------------------------ |
| **CVaR‑optimisation**   | maximise \( \operatorname{CVaR}_{\alpha}(G)\) | convex but non‑linear DP                               |
| **Exponential utility** | maximise \(\mathbb E[e^{\lambda G}]\)         | leads to multiplicative dynamic programming            |
| **Multi‑objective**     | vector‑valued reward \(r^1,\dots,r^d\)        | Pareto DP / scalarisation needed                       |
| **Constrained MDP**     | maximise \(v^\pi\) s.t. \(c^\pi\le C\)          | solved via Lagrange multipliers and linear programming |

These variants break the contraction or linearity enjoyed by the standard criteria and typically require bespoke algorithms.

---

### 8.7 Transformations between objectives

| From                  | To                                      | Construction                                                                    | Error                                 |
| --------------------- | --------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------- |
| Finite horizon \(H\)    | Discounted \(\gamma=1-1/H\)               | choose \(\gamma\) to match effective horizon                                      | bias \(O(1/H)\)                         |
| Discounted \(\gamma<1\) | Finite horizon \(H_{\gamma,\varepsilon}\) | drop tail after \(H_{\gamma,\varepsilon}\)                                        | add ≤ \(\varepsilon R_{\max}\) to value |
| Average reward        | Discounted \(\gamma\uparrow1\)            | **Abel limit:** \(\rho^{\pi}=\lim_{(1-\gamma)\to0}(1-\gamma)v^{\pi}_{\gamma}(s)\) | holds if chain is unichain            |
| Total cost            | Discounted                              | absorb at first visit to \(S_{\text{abs}}\)                                       | exact                                 |

Transformations justify analysing the discounted setting first and mapping results to others later.

---

### 8.8 Effect on Bellman operators

| Criterion      | Operator                                            | Contraction modulus            |
| -------------- | --------------------------------------------------- | ------------------------------ |
| Discounted     | \(T^{\pi}v=r^{\pi}+\gamma P^{\pi}v\)                  | \(\gamma<1\)                     |
| Finite horizon | \(T_{t}\) depends on time step                        | modulus 0 (backward induction) |
| Average reward | \( T^{\rho} h = r-\rho+P h\)                          | **None** without mixing        |
| Total cost     | same as discounted with \(\gamma=1\) on transient set | modulus 1                      |

Only the discounted operator is a uniform contraction on \(\ell_{\infty}\); this single fact underlies the simplicity of Sections 10–11.

---

### 8.9 When to use which objective?

* **Long‑running tasks without clear termination:** use discounted; set \(\gamma\) via desired effective horizon (§3).
* **Episodic games or dialog systems with fixed length:** finite horizon gives non‑stationary optimal policies but tractable backward induction.
* **Steady‑state control / queuing:** average‑reward is scale‑free and avoids arbitrary discount choice, but requires ergodicity assumptions.
* **Shortest‑path or cost‑to‑goal planning:** total‑cost formulation naturally penalises each step until absorption.

Designers often start with the archetypal discounted MDP, then translate if domain conventions (e.g., average throughput) demand an alternative metric.

---

### 8.10 Key modelling take‑aways

1. **Reward offsets and scaling** leave the optimal policy unchanged in all objectives except risk‑sensitive ones.
2. **Discounting** is analytically convenient (γ‑contraction) and approximates long but finite tasks; however it introduces a bias of \(O(1-\gamma)\).
3. **Finite‑horizon** tasks require time‑varying policies and value tables of size \(H|S|\) but admit exact solutions by backward induction.
4. **Average‑reward** removes discount bias yet sacrifices contraction; extra mixing assumptions or bias functions are needed.
5. **Total‑cost** handles \(\gamma=1\) gracefully as long as an absorbing set guarantees finiteness.

---

## 9 Discounted occupancy measures

Occupancy measures recast long‑horizon decision making as a **static optimisation** over distributions on state‑action pairs. They underpin linear‑programming (LP) solutions, duality theory, policy‑gradient proofs and many recent RL algorithms.

---

### 9.1 Definition

Let \(\mu\in\Delta(S)\) be the start distribution and \(\pi\) any (possibly history‑dependent) policy.
The **discounted occupancy measure** (unnormalised) is

$$
\boxed{\;
\nu^{\pi}_{\mu}(s,a)=\sum_{t=0}^{\infty}\gamma^{t}\,
\Pr^{\pi}_{\mu}(S_t=s,A_t=a)
\;},\qquad (s,a)\in S\times A .
\tag{9.1}
$$

Multiplying by \((1-\gamma)\) produces a probability measure

$$
d^{\pi}_{\mu}:=(1-\gamma)\,\nu^{\pi}_{\mu}\in\Delta(S\times A).
\tag{9.2}
$$

Equation (9.1) matches the lecture‑note definition (lec2 p. 3) .

---

### 9.2 Equivalent matrix form for stationary policies

Fix a stationary policy \(m\).
With \(P^{m}\) and \(r^{m}\) as in §6,

$$
\nu^{m}_{\mu}
\;=\;
\mu\,(I-\gamma P^{m})^{-1}\,\mathrm{diag}(m),
\tag{9.3}
$$

and hence

$$
d^{m}_{\mu}
\;=\;(1-\gamma)\,\mu\,(I-\gamma P^{m})^{-1}\,\mathrm{diag}(m).
\tag{9.4}
$$

Rows of \((I-\gamma P^{m})^{-1}\) were already interpreted as “unnormalised discounted state occupancy’’ in note1 Eq. (4) .

---

### 9.3 Flow constraints (Bellman flow equations)

Write the vectorised measure \(d\in\mathbb R^{|S||A|}\).
Let \(P\in[0,1]^{|S||A|\times|S|}\) be the block matrix with rows \(P_{a}(s,\cdot)\).
Then **every** discounted occupancy measure satisfies

$$
\boxed{\;
\underbrace{\sum_{a}d(s,a)}_{\text{state marginal}}
\;=\;\gamma P^{\top}d + (1-\gamma)\,\mu,
\quad\forall s\in S.
\;}
\tag{9.5}
$$

Equation (9.5) is exactly the dual‑LP constraint in note1 §2.3 and is often called the *Bellman flow equation* .

*Proof idea.*  Expand the marginal using (9.1) and shift indices; the missing \(t=0\) term is supplied by \((1-\gamma)\mu\) (detailed derivation in note1 p. 11) .

---

### 9.4 Sufficiency: characterising feasible \(d\)

\begin{proposition}\[Feasible ⇔ realizable]\label{prop\:feasible}
For finite \(S,A\) a vector \(d\in\mathbb R_{\ge0}^{|S||A|}\) is the occupancy measure of
some stationary policy iff it satisfies \((9.5)\).
\end{proposition}

*Sketch.*
*If part* is immediate from §9.3.
*Only‑if part:* given \(d\) obeying (9.5) define

$$
m(a\mid s)=\frac{d(s,a)}{\sum_{a'}d(s,a')}.
\tag{9.6}
$$

Equation (9.5) implies the Markov chain \(P^{m}\) together with \(m\) yields the same flows, hence reproduces \(d\) (note1 p. 12) .

---

### 9.5 Value as an inner product

Because rewards depend only on \((s,a)\),

$$
v^{\pi}(\mu)\;=\;\sum_{s,a}r_a(s)\,\nu^{\pi}_{\mu}(s,a)
=\langle \nu^{\pi}_{\mu},\,r\rangle
=\tfrac{1}{1-\gamma}\,\langle d^{\pi}_{\mu},\,r\rangle.
\tag{9.7}
$$

This identity appears in lec2 (Eq. just below the definition)  and motivates RL algorithms that move \(d^{\pi}_{\mu}\) toward the “reward direction’’ in \(\mathbb R^{|S||A|}\).

---

### 9.6 Linear‑programming formulation

**Primal LP** (“value LP”, note1 §2.3):

$$
\begin{aligned}
\text{minimise } &\; \langle \mu,\,v\rangle \\
\text{s.t. } &\; v(s) \ge r_a(s)+\gamma\sum_{s'}P_a(s,s')\,v(s')\;\;\forall(s,a).
\end{aligned}
\tag{9.8}
$$

**Dual LP** in variables \(d\):

$$
\begin{aligned}
\text{maximise } &\; \langle d,\,r\rangle \\
\text{s.t. } &\; d\ge 0,\quad \text{flow constraint } (9.5).
\end{aligned}
\tag{9.9}
$$

Feasible \(d\) are precisely occupancy measures of stationary policies (Prop. \ref{prop\:feasible}), so the dual objective equals \(v^{m}(\mu)\).  Strong duality therefore restates optimal control as a *linear* optimisation in the \(|S||A|\)-simplex   (note1 pp. 10‑11) .

---

### 9.7 Policy extraction from an optimal \(d^{\star}\)

Given an optimal dual solution \(d^{\star}\), recover an optimal policy via normalisation (9.6).
Because \(d^{\star}\) attains the dual optimum, the resulting policy is value‑optimal.  This is the standard method used by LP solvers and by apprenticeship / inverse‑RL algorithms (note1 p. 12) .


### 9.8 Occupancy measures and gradients (preview)

For parameterised policies \(\pi_{\theta}\),

$$
\nabla_{\theta}v^{\pi_{\theta}}(\mu)=
\frac{1}{1-\gamma}\,\sum_{s,a}d^{\pi_{\theta}}_{\mu}(s,a)\,
\nabla_{\theta}\log\pi_{\theta}(a\mid s)\,q^{\pi_{\theta}}(s,a),
\tag{9.10}
$$

so policy‑gradient methods estimate \(d^{\pi}_{\mu}\) (or its score‑function–weighted variant) rather than values directly.  Equation (9.10) follows from differentiating (9.7) and using the likelihood‑ratio trick; details lie beyond our current scope but hinge on the measurability established in §5.

---

### 9.9 Take‑aways

* **Geometry:** The feasible set of discounted occupancy measures is a polytope carved out by the linear flow equations (9.5).
* **Duality:** Maximising expected return equals a linear maximisation over this polytope (9.9).
* **Sufficiency:** Every vertex corresponds to a **deterministic stationary** policy, connecting LP optima to the fundamental theorem in Section 7.
* **Algorithms:** Occupancy measures unify value‑based, policy‑gradient, LP and inverse‑RL perspectives; (9.7)–(9.10) translate improvements in any one view into the others.

---

## 10 Bellman operators and fixed‑point theory

Throughout we work in the Banach space

$$
\mathcal B:=\bigl(\mathbb R^{|S|},\;\lVert\cdot\rVert_{\infty}\bigr),
\qquad
\lVert v\rVert_{\infty}:=\max_{s\in S}|v(s)|.
\tag{10.1}
$$

---

### 10.1 Policy‑evaluation operator

For a **stationary** policy \(m\) recall from §6 the averaged reward vector and transition matrix

$$
r^{m}(s)=\sum_{a}m(a\mid s)r_{a}(s),\qquad
P^{m}(s,s')=\sum_{a}m(a\mid s)P_{a}(s,s').
\tag{10.2}
$$

\begin{definition}\[Linear Bellman operator]

$$
(T^{m}v)(s)\;:=\;r^{m}(s)+\gamma\sum_{s'}P^{m}(s,s')\,v(s').
\tag{10.3}
$$

\end{definition}

---

#### Proposition 10.1 (γ‑contraction)

For any \(u,v\in\mathcal B\),

$$
\lVert T^{m}u-T^{m}v\rVert_{\infty}\;\le\;\gamma\,\lVert u-v\rVert_{\infty}.
\tag{10.4}
$$

*Proof.*

$$
\begin{aligned}
|T^{m}u(s)-T^{m}v(s)|
&=\gamma\Bigl|\sum_{s'}P^{m}(s,s')\bigl(u(s')-v(s')\bigr)\Bigr|\\
&\le\gamma\sum_{s'}P^{m}(s,s')\lVert u-v\rVert_{\infty}
=\gamma\lVert u-v\rVert_{\infty}.
\end{aligned}
$$

Take the maximum over \(s\). □

---

#### Corollary 10.2 (Unique fixed point and geometric convergence)

*Existence/uniqueness.* By Banach’s fixed‑point theorem, \(T^{m}\) has a unique fixed point \(v^{m}\in\mathcal B\).

*Iterative policy evaluation.* For any initial \(v_0\in\mathcal B\)

$$
v_{k+1}=T^{m}v_{k}\quad\Longrightarrow\quad
\lVert v_{k}-v^{m}\rVert_{\infty}\le\gamma^{k}\lVert v_{0}-v^{m}\rVert_{\infty}.
\tag{10.5}
$$

Equation (10.5) gives the \(O\bigl((1-\gamma)^{-1}\ln(1/\varepsilon)\bigr)\) iteration complexity cited in §6.

---

### 10.2 Bellman optimality operator

\begin{definition}\[Non‑linear Bellman operator]

$$
(Tv)(s):=\max_{a\in A}\Bigl\{\,r_{a}(s)+\gamma\sum_{s'}P_{a}(s,s')\,v(s')\Bigr\}.
\tag{10.6}
$$

\end{definition}

---

#### Proposition 10.3 (γ‑contraction of \(T\))

$$
\lVert Tu-Tv\rVert_{\infty}\;\le\;\gamma\,\lVert u-v\rVert_{\infty}\quad
\forall u,v\in\mathcal B.
\tag{10.7}
$$

*Proof.*
Fix \(s\).  Pick actions \(a_u\) and \(a_v\) that achieve the maxima for \(Tu(s)\) and \(Tv(s)\) respectively.  Then

$$
\begin{aligned}
Tu(s)-Tv(s)
&\le r_{a_u}(s)+\gamma\sum_{s'}P_{a_u}(s,s')u(s')
   -r_{a_u}(s)-\gamma\sum_{s'}P_{a_u}(s,s')v(s')\\
&=\gamma\sum_{s'}P_{a_u}(s,s')\bigl[u(s')-v(s')\bigr]
\le\gamma\lVert u-v\rVert_{\infty}.
\end{aligned}
$$

Swap \(u,v\) to bound the absolute value and take the maximum. □

---

#### Theorem 10.4 (Value‑iteration convergence)

Let \(v_0\in\mathcal B\) be arbitrary and define \(v_{k+1}=Tv_k\). Then

$$
\lVert v_{k}-v^{\star}\rVert_{\infty}\;\le\;\frac{\gamma^{k}}{1-\gamma},
\tag{10.8}
$$

where \(v^{\star}\) is the unique fixed point of \(T\).

\emph{Proof.} Combine the contraction (10.7) with \(v^{\star}=Tv^{\star}\):

$$
\lVert v_{k}-v^{\star}\rVert_{\infty}
=\lVert Tv_{k-1}-Tv^{\star}\rVert_{\infty}
\le\gamma\lVert v_{k-1}-v^{\star}\rVert_{\infty}\le\cdots\le\gamma^{k}\lVert v_0-v^{\star}\rVert_{\infty}.
$$

Choosing \(v_0\equiv 0\) gives \(\lVert v_0-v^{\star}\rVert_{\infty}\le\frac1{1-\gamma}\), yielding (10.8). □

---

### 10.3 Monotonicity and greedy improvement

\begin{lemma}\[Monotonicity]\label{lem\:monotone}
If \(u\le v\) component‑wise then \(Tu\le Tv\) and \(T^{m}u\le T^{m}v\).
\end{lemma}

*Proof.* Immediate from definitions (10.3)–(10.6) using non‑negativity of transition probabilities.

---

\begin{proposition}\[Policy‑improvement]\label{prop\:PI}
Let \(m\) be stationary and define the greedy policy

$$
m^{+}(s)\in\arg\max_{a\in A}
\bigl\{\,r_{a}(s)+\gamma\sum_{s'}P_{a}(s,s')v^{m}(s')\bigr\}.
$$

Then \(v^{m^{+}}\ge v^{m}\) with strict inequality in any state where \(m\) is not already greedy.
\end{proposition}

*Proof.*
Because \(m^{+}\) is greedy, \(T^{m^{+}}v^{m}=Tv^{m}\ge v^{m}\).
Applying monotonicity of \(T^{m^{+}}\) repeatedly and taking limits yields \(v^{m^{+}}\ge v^{m}\).
If \(Tv^{m}\neq v^{m}\) at some state, the inequality is strict there. □

Proposition \ref{prop\:PI} is the engine behind **policy‑iteration**: alternate evaluation \(v^{m}\leftarrow\mathrm{solve}(T^{m}v=v)\) and improvement \(m\leftarrow\mathrm{Greedy}(v^{m})\).  Finite \(S,A\) implies at most \(|A|^{|S|}\) improvements; empirically far fewer.

---

### 10.4 Bellman residuals and error bounds

For any \(u\in\mathcal B\) define residuals

$$
\delta^{m}(u):=T^{m}u-u,\qquad
\delta(u):=Tu-u.
\tag{10.9}
$$

Using contraction one shows

$$
\lVert v^{m}-u\rVert_{\infty}\;\le\;\frac{\lVert\delta^{m}(u)\rVert_{\infty}}{1-\gamma},
\qquad
\lVert v^{\star}-u\rVert_{\infty}\;\le\;\frac{\lVert\delta(u)\rVert_{\infty}}{1-\gamma}.
\tag{10.10}
$$

Equation (10.10) supplies a *certificate* of near‑optimality computable from \(u\) alone—essential in approximate dynamic programming.

---

### 10.5 Summary

| Operator      | Type           | Contraction | Fixed point | Use case                 |
| ------------- | -------------- | ----------- | ----------- | ------------------------ |
| \(T^{m}\)       | linear         | γ           | \(v^{m}\)     | policy evaluation        |
| \(T\)           | non‑linear max | γ           | \(v^{\star}\) | value iteration          |
| \(T^{m}\) / \(T\) | monotone       | yes         | —           | policy‑improvement proof |

Key ideas:

* γ‑contraction ⇒ unique fixed points and geometric convergence.
* Monotonicity + contraction ⇒ policy‑iteration improvement step.
* Residual bounds turn approximations into rigorous error estimates.

These analytical properties draw directly on the measure‑theoretic foundation (Sections 1–5) and feed forward into Section 11, where we formalise **greedy policies, optimality equations, and the full proof of the fundamental theorem**.

---

## 11 Greedy policies, monotonicity and the Fundamental Theorem (deep dive)

This section tightens the results sketched in §7 and §10.
We give a self‑contained chain of lemmas that (i) connect **greedy
policies** to Bellman operators, (ii) establish **monotone
improvement**, and (iii) culminate in the **classical dynamic‑programming
optimality theorem**.

---

### 11.1 The greedy operator

For any value vector \(v\in\mathbb R^{|S|}\) define the **greedy selection set**

$$
\mathrm{Greedy}(v)(s) := \arg\max_{a\in A}
\lbrace r_a(s)+\gamma\sum_{s'}P_a(s,s')v(s') \rbrace
\tag{11.1}
$$

and let \(\mathcal G(v)\) be the set of all stationary policies that are greedy in
every state:

$$
\pi\in\mathcal G(v)\iff
\pi(\cdot\mid s)\subseteq\mathrm{Greedy}(v)(s)\quad\forall s\in S.
\tag{11.2}
$$

When a single tie‑breaking rule is fixed, the **greedy operator**
\(\Gamma:\mathbb R^{|S|}\to A^{S}\) returns one deterministic greedy
policy \(\Gamma(v)\).

---

### 11.2 Monotonicity and Bellman dominance

Two elementary facts:

* **Monotonicity of \(T\) and \(T^{\pi}\)** (Lemma 10.1):
  \(u\le v\;\Rightarrow\;Tu\le Tv,\;T^{\pi}u\le T^{\pi}v\).

* **Bellman dominance by greediness.**
  If \(\pi\in\mathcal G(v)\) then \(T^{\pi}v=Tv\).
  (Because each maximising action in \(Tv\) is also chosen by \(\pi\).)

---

### 11.3 Policy‑improvement theorem

**Theorem**: Let \(m\) be any stationary policy and let \(m^{+}:=\Gamma\bigl(v^{m}\bigr)\). Then

$$
v^{m^{+}}\;\ge\;v^{m}\quad(\text{component‑wise}),
\tag{11.3}
$$

with strict inequality in at least one state unless \(m\) is already greedy.

**Proof**:

Greediness gives \(T^{m^{+}}v^{m}=Tv^{m}\ge v^{m}\).
Apply \(T^{m^{+}}\) repeatedly and use monotonicity:

$$
v^{m}\;\le\;T^{m^{+}}v^{m}\;\le\;(T^{m^{+}})^{2}v^{m}\;\le\;\dots\;
\longrightarrow\;v^{m^{+}}
\quad\text{(by Cor. 10.2)}.
$$

Thus \(v^{m^{+}}\ge v^{m}\).
If \(Tv^{m}\neq v^{m}\) somewhere (i.e. \(m\) was not greedy), the first
inequality is strict in that state, and the limit preserves strictness.
\end{proof}

---

### 11.4 Policy‑iteration algorithm and finite convergence

**Algorithm (Howard 1960).**

1. Start with any stationary policy \(m_0\).
2. **Evaluation:** solve \(v_k\) from \(T^{m_k}v_k=v_k\).
3. **Improvement:** set \(m_{k+1}=\Gamma(v_k)\).
4. If \(m_{k+1}=m_k\) stop; else \(k\leftarrow k+1\) and repeat.

*Termination in finitely many iterations.*
The sequence \(\{v_k\}\) is monotonically increasing component‑wise
(Theorem \ref{thm\:PI}).
Because the set of deterministic stationary policies is finite
(\(|A|^{|S|}\) elements), improvement can occur at most
\(|A|^{|S|}-1\) times.

*Global optimality at termination.*
If \(m_{k+1}=m_k\) then \(m_k\) is greedy w\.r.t. \(v_k\).
Hence \(T^{m_k}v_k=Tv_k\).
But \(v_k\) is also the fixed point of \(T^{m_k}\), so \(Tv_k=v_k\).
By Lemma 10.2 this fixed point is unique and equals \(v^{\star}\); thus
\(m_k\) is optimal.

---

### 11.5 Value‑iteration with greedy policy extraction

Although value‑iteration (§10) drives \(v_k\to v^{\star}\) even without
policies, one often constructs a *sequence of greedy policies*
\(\pi_k=\Gamma(v_k)\).

\begin{proposition}\label{prop\:VI-greedy}
After \(k\) value‑iteration steps with \(v_0\equiv0\),

$$
v^{\pi_k}\;\ge\;v_k
\quad\text{and}\quad
\lVert v^{\star}-v^{\pi_k}\rVert_{\infty}\;\le\;\frac{2\,\gamma^{k}}{1-\gamma}.
\tag{11.4}
$$

\end{proposition}

*Proof sketch.*
The first claim uses \(T^{\pi_k}v_k=Tv_k=v_{k+1}\ge v_k\) and monotone
convergence.  The residual bound (10.10) then yields the error estimate.

---

### 11.6 Fundamental theorem (full proof)

\begin{theorem}\[Fundamental theorem of finite discounted MDPs]\label{thm\:FT}
There exists a deterministic stationary policy \(\alpha^{\star}\) such that

$$
v^{\alpha^{\star}}=v^{\star},
$$

and for every state \(s\),
\(\alpha^{\star}(s)\in\mathrm{Greedy}\!\bigl(v^{\star}\bigr)(s)\).
\end{theorem}

\begin{proof}
Apply policy‑iteration starting from an arbitrary stationary policy.
Termination yields \(m^{\star}\) with value \(v^{\star}\).
Since the improvement step selects deterministic greedy actions,
\(m^{\star}\) is deterministic and greedily satisfies the displayed
condition.
\end{proof}

This theorem unifies the geometric fixed‑point picture (value‑iteration)
with the combinatorial policy‑improvement picture (policy‑iteration).

---

### 11.7 Monotone value sequences in practice

| Algorithm              | Sequence  | Monotone?                   | Limiting value |
| ---------------------- | --------- | --------------------------- | -------------- |
| Policy‑iteration       | \(v^{m_k}\) | ↑                           | \(v^{\star}\)    |
| Value‑iteration        | \(v_k\)     | ↑ (when \(v_0\le v^{\star}\)) | \(v^{\star}\)    |
| Modified PI (ε‑greedy) | \(v^{m_k}\) | ↑ (for small ε)             | ≤ \(v^{\star}\)  |

Monotonicity provides a **lower bound** on \(v^{\star}\) at every sweep,
useful for early stopping and for proving **optimistic** regret bounds in
reinforcement‑learning algorithms.

---

### 11.8 Take‑aways

* A single step of greedy policy‑improvement never decreases value; repeating finitely many times yields an optimal **deterministic** stationary policy.
* Greedy extraction from intermediate value‑iteration iterates already
  delivers near‑optimal policies with explicit \(\ell_{\infty}\) error
  bounds (Prop. \ref{prop\:VI-greedy}).
* Monotonicity and γ‑contraction together power both value‑ and
  policy‑iteration—distinct algorithms built on the same analytic
  skeleton.
* The Fundamental Theorem justifies focussing on deterministic
  stationary policies throughout planning and learning theory.
