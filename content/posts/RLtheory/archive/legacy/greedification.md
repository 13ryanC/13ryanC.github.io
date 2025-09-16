---
date: "2025-06-30"
title: "Greedification"
summary: "Greedification"
category: Tutorial
series: ["RL Theory", "RL Experimentation"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---
in (https://www.youtube.com/watch?v=4Rf1hzE5MsQ). It explains how to derive a near-optimal policy once you have an approximately correct value function, Vₖ. This is done by "greedifying" the policy—choosing the action that looks best according to Vₖ. Show me all the mathematics.

The mathematical derivation for obtaining a near-optimal policy (π) from an approximately correct value function (Vₖ) by "greedifying" the policy is as follows:

### 1. Initial Assumption
The derivation begins with the assumption that the approximate value function, V, is close to the optimal value function, V*. This relationship is expressed as an inequality where the difference is bounded by a small positive constant, ε \[[42:51](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2571)\]:

V ≥ V\* - ε · **1**

Here, **1** represents a vector of all ones.

### 2. Application of the Bellman Optimality Operator (T)
The Bellman optimality operator, T, is applied to both sides of the inequality \[[50:40](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3040)\]:

T(V) ≥ T(V\* - ε · **1**)

A key property of the Bellman operator is that a constant added to the value function can be factored out and multiplied by the discount factor, γ \[[49:00](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2940)\]. This gives:

T(V\* - ε · **1**) = T(V\*) - γ · ε · **1**

From the Bellman optimality equation, we know that V\* is a fixed point of the operator T, meaning T(V\*) = V\* \[[01:11:17](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=4277)\]. Substituting this back gives:

T(V) ≥ V\* - γ · ε · **1** \[[51:10](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3070)\]

### 3. Greedification Step
A new policy, π, is formed by "greedifying" with respect to V. This means that for any given state, the policy π selects the action that maximizes the one-step lookahead value, according to V \[[45:21](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2721)\]. By the definition of this greedy policy, the following equality holds \[[51:35](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3095)\]:

T(V) = T_π(V)

Substituting this into the previous inequality yields:

T_π(V) ≥ V\* - γ · ε · **1** \[[51:52](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3112)\]

### 4. Iterative Application of the Policy's Bellman Operator (T_π)
The Bellman operator for the policy π, denoted as T_π, is now applied iteratively. After the first application, we get \[[57:15](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3435)\]:

T_π²(V) ≥ T_π(V\*) - γ² · ε · **1**

After k applications, the inequality generalizes to \[[59:32](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3572)\]:

T_πᵏ(V) ≥ V\* - ε · (γ + γ² + ... + γᵏ) · **1**

The geometric series can be simplified:

T_πᵏ(V) ≥ V\* - ε · (γ · (1 - γᵏ) / (1 - γ)) · **1**

### 5. Convergence to the Limit
As the number of iterations, k, approaches infinity, T_πᵏ(V) converges to V_π, which is the value function of the policy π. This is a consequence of the Banach fixed-point theorem \[[02:59:56](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=10796)\]. In the limit, the term γᵏ approaches zero. The inequality thus becomes \[[01:00:07](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3607)\]:

V_π ≥ V\* - ε · (γ / (1 - γ)) · **1**

### 6. Conclusion
This final result demonstrates that the value function of the greedy policy, V_π, is near-optimal. The gap between the value of the greedy policy and the optimal policy is bounded by ε · (γ / (1 - γ)). This shows that if the initial value function V is ε-close to the optimal value function V\*, the resulting greedy policy π will be (ε · γ / (1 - γ))-close to the optimal policy in terms of its value \[[01:01:12](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3672)\].
http://googleusercontent.com/youtube_content/0

---
Show me the full proof that shows that if your value function Vₖ is ε-close to the true optimal value function V*, the resulting greedy policy π will have a value function Vπ that is near-optimal within a bound of 2εγ / (1 - γ)

Of course. Here is the full proof demonstrating that if your value function, Vₖ, is ε-close to the true optimal value function, V\*, the resulting greedy policy, π, will have a value function, Vπ, that is near-optimal within a bound of 2εγ / (1 - γ).

### **Definitions and Preliminaries**

* **V\***: The true optimal value function. It satisfies the Bellman optimality equation:
    V\*(s) = maxₐ Σₛ' P(s'|s, a) [R(s, a, s') + γV\*(s')]

* **Vₖ**: An approximate value function that is ε-close to V\*. This is expressed using the infinity norm (which represents the maximum difference for any state):
    ||V\* - Vₖ||∞ ≤ ε

* **π**: The policy that is "greedy" with respect to Vₖ. This means that for any state *s*, the policy chooses the action that maximizes the expected one-step lookahead using Vₖ:
    π(s) = argmaxₐ Σₛ' P(s'|s, a) [R(s, a, s') + γVₖ(s')]

* **Vπ**: The true value function of the policy π. It satisfies the Bellman equation for policy π:
    Vπ(s) = Σₛ' P(s'|s, π(s)) [R(s, π(s), s') + γVπ(s')]

* **T\***: The optimal Bellman operator. Applying it to a value function V gives:
    (T\*V)(s) = maxₐ Σₛ' P(s'|s, a) [R(s, a, s') + γV(s')]
    So, V\* = T\*V\*.

* **Tπ**: The Bellman operator for policy π. Applying it to a value function V gives:
    (TπV)(s) = Σₛ' P(s'|s, π(s)) [R(s, π(s), s') + γV(s')]
    So, Vπ = TπVπ.

### **The Proof**

The goal is to bound the difference between the optimal value function and the value function of our greedy policy: |V\*(s) - Vπ(s)|.

1.  **Start with the difference:**
    V\*(s) - Vπ(s)

2.  **Use the Bellman equations for V\* and Vπ.** V\* is the result of applying the optimal Bellman operator, T\*, while Vπ is the result of applying the Bellman operator for policy π, Tπ.
    V\*(s) - Vπ(s) = (T\*V\*)(s) - (TπVπ)(s)

3.  **The greedy policy π chooses the action that maximizes the lookahead with Vₖ.** By definition of π, we have:
    (TπVₖ)(s) = maxₐ Σₛ' P(s'|s, a) [R(s, a, s') + γVₖ(s')] = (T\*Vₖ)(s)

4.  **Now, let's manipulate the initial difference:**
    V\*(s) - Vπ(s) = (T\*V\*)(s) - (TπVπ)(s)
    We can add and subtract (TπV\*)(s) to introduce terms that we can bound:
    = [(T\*V\*)(s) - (TπV\*)(s)] + [(TπV\*)(s) - (TπVπ)(s)]

5.  **Bound the second term.** The Bellman operator Tπ is a γ-contraction, which means that for any two value functions V₁ and V₂, ||TπV₁ - TπV₂||∞ ≤ γ||V₁ - V₂||∞.
    Therefore:
    |(TπV\*)(s) - (TπVπ)(s)| ≤ γ ||V\* - Vπ||∞

6.  **Bound the first term.** This is the crucial part of the proof.
    (T\*V\*)(s) - (TπV\*)(s)
    = maxₐ { ...γV\*(s') } - { ...γV\*(s') }_π(s)  (where {...} represents the expectation)
    Since the greedy policy π was chosen based on Vₖ, not V\*, we can relate T\* to Tπ via Vₖ.
    We know (T\*Vₖ)(s) = (TπVₖ)(s). Let's use this.
    (T\*V\*)(s) - (TπV\*)(s)
    = [(T\*V\*)(s) - (T\*Vₖ)(s)] + [(T\*Vₖ)(s) - (TπV\*)(s)]
    = [(T\*V\*)(s) - (T\*Vₖ)(s)] + [(TπVₖ)(s) - (TπV\*)(s)]

7.  **Apply the contraction property again.** Both T\* and Tπ are γ-contractions.
    |(T\*V\*)(s) - (T\*Vₖ)(s)| ≤ γ ||V\* - Vₖ||∞ ≤ γε
    |(TπVₖ)(s) - (TπV\*)(s)| ≤ γ ||Vₖ - V\*||∞ ≤ γε

8.  **Combine the bounds.** Using the triangle inequality on the expression from step 6:
    |(T\*V\*)(s) - (TπV\*)(s)| ≤ |(T\*V\*)(s) - (T\*Vₖ)(s)| + |(TπVₖ)(s) - (TπV\*)(s)|
    ≤ γε + γε = 2γε

9.  **Put everything back together.** From step 4, we have:
    V\*(s) - Vπ(s) ≤ |(T\*V\*)(s) - (TπV\*)(s)| + |(TπV\*)(s) - (TπVπ)(s)|
    V\*(s) - Vπ(s) ≤ 2γε + γ ||V\* - Vπ||∞

10. **Final step.** Since this inequality holds for all states *s*, it also holds for the state where the difference is maximum. So, we can write it in terms of the infinity norm:
    ||V\* - Vπ||∞ ≤ 2γε + γ ||V\* - Vπ||∞
    (1 - γ) ||V\* - Vπ||∞ ≤ 2γε
    ||V\* - Vπ||∞ ≤ (2γε) / (1 - γ)

This completes the proof, showing that the value of the greedy policy is within **2εγ / (1 - γ)** of the optimal value.

---

Show me the full derivation of the total computational cost of Value Iteration to find a near-optimal policy as being approximately O(S²A * log(1/ε) / (1-γ)²), highlighting its efficiency in terms of accuracy (ε) but its dependence on the state/action space and the discount factor γ

Of course. Here is the full derivation of the total computational cost of Value Iteration, showing how its complexity is determined by the size of the state-action space, the discount factor, and the desired accuracy.

### **Objective**

We aim to find the total computational cost to run Value Iteration until we can extract a greedy policy `π` whose value function `Vπ` is ε-close to the optimal value function `V*`. That is, `||V* - Vπ||∞ ≤ ε`.

The derivation is broken into three main parts:
1.  The computational cost of a single iteration of Value Iteration.
2.  The number of iterations required to guarantee the desired policy accuracy `ε`.
3.  The total cost and its analysis.

---

### **Step 1: Computational Cost of a Single Iteration**

Value Iteration updates the value function for every state `s` using the Bellman optimality operator:

$$V_{k+1}(s) \leftarrow \max_{a \in A} \sum_{s' \in S} P(s'|s, a) \left[ R(s, a, s') + \gamma V_k(s') \right]$$

Let's analyze the cost of this update for a single state `s`:
* To compute the value of taking a single action `a`, we must sum over all possible next states `s'`. This involves `|S|` multiplications and `|S|` additions. The cost is `O(S)`.
* We must do this for every possible action `a` to find the maximum. This brings the cost to `O(|A| \cdot |S|)`.

This is the cost to update just one state. To complete a single iteration (i.e., to compute `Vₖ₊₁` from `Vₖ`), we must perform this update for all `|S|` states.

* **Cost per Iteration:** `|S| \times O(|A| \cdot |S|) = O(S²A)`

This cost assumes a dense transition model where any action can lead to any other state.

---

### **Step 2: Number of Iterations Required**

This is the most involved part of the derivation. We need to determine how many iterations, `k`, are necessary. The process involves linking the final policy error `ε` back to the stopping condition of the Value Iteration algorithm.

#### **Sub-step 2a: Connecting Policy Error to Value Function Error**

As shown in the previous proof, the suboptimality of a greedy policy `π` derived from a value function `Vₖ` is bounded by the error in `Vₖ`:

$$||V^* - V_\pi||_\infty \leq \frac{2\gamma}{1-\gamma} ||V^* - V_k||_\infty$$

Here, `||V* - Vₖ||∞` is the error of our value function after `k` iterations.

#### **Sub-step 2b: Connecting Value Function Error to the Bellman Residual**

The Value Iteration algorithm doesn't know the true `V*`, so it can't use `||V* - Vₖ||∞` as a stopping condition. Instead, it uses the **Bellman residual**, `δ_k = ||V_{k+1} - V_k||_\infty`. A key lemma in dynamic programming states that the true error is bounded by this residual:

$$||V^* - V_k||_\infty \leq \frac{\gamma}{1-\gamma} ||V_{k+1} - V_k||_\infty = \frac{\gamma}{1-\gamma} \delta_k$$

#### **Sub-step 2c: The Emergence of the `(1-γ)²` Term**

Now we combine the two inequalities above. We substitute the bound for the value function error (from 2b) into the policy error equation (from 2a):

$$||V^* - V_\pi||_\infty \leq \frac{2\gamma}{1-\gamma} \left( \frac{\gamma}{1-\gamma} \delta_k \right) = \frac{2\gamma^2}{(1-\gamma)^2} \delta_k$$

This is the crucial relationship. It shows that the final policy's error is bounded by the Bellman residual, scaled by a factor that depends on `1/(1-γ)²`.

To achieve our desired final policy accuracy `||V* - Vπ||∞ ≤ ε`, we must run Value Iteration until the Bellman residual `δ_k` is sufficiently small. We need:

$$\frac{2\gamma^2}{(1-\gamma)^2} \delta_k \leq \varepsilon \implies \delta_k \leq \frac{\varepsilon(1-\gamma)^2}{2\gamma^2}$$

Let this required residual be `δ_target`.

#### **Sub-step 2d: Calculating the Number of Iterations `k`**

The Bellman residual `δ_k` shrinks with each iteration by a factor of `γ`: `δ_k ≤ γ δ_{k-1} ≤ ... ≤ γᵏ δ₀`. The initial residual `δ₀ = ||V₁ - V₀||∞` is at most `R_max`, the maximum possible reward in the MDP.

We need to find the number of iterations `k` such that `δ_k ≤ δ_target`:

$$\gamma^k R_{max} \leq \frac{\varepsilon(1-\gamma)^2}{2\gamma^2}$$

Solving for `k`:
$$k \log(\gamma) \leq \log\left(\frac{\varepsilon(1-\gamma)^2}{2\gamma^2 R_{max}}\right)$$
Since `log(γ)` is negative, we flip the inequality:
$$k \geq \frac{\log\left(\frac{2\gamma^2 R_{max}}{\varepsilon(1-\gamma)^2}\right)}{\log(1/\gamma)}$$

Using the approximation `log(1/γ) ≈ 1-γ` for `γ` close to 1, and analyzing the dominant terms in the numerator's logarithm (`log(1/ε)` and `log(1/(1-γ)²) = 2log(1/(1-γ))`), we get:

* **Number of Iterations `k`:** `O( (log(1/ε) + log(1/(1-γ))) / (1-γ) )`

---

### **Step 3: Total Computational Cost and Analysis**

The total cost is the cost per iteration multiplied by the number of iterations.

**Total Cost = `O(S²A) \times O( (log(1/ε) + log(1/(1-γ))) / (1-γ) )`**

For simplicity in analysis and because the `1/(1-γ)` term grows faster than the `log(1/(1-γ))` term, this is often stated as the looser but more memorable bound:

$$\text{Total Cost} \approx O\left( \frac{S^2 A}{(1-\gamma)^2} \log\left(\frac{1}{\varepsilon}\right) \right)$$

### **Analysis of Complexity**

This final expression highlights the efficiency and dependencies of Value Iteration:

* **Efficiency in Accuracy (ε):** The cost is proportional to `log(1/ε)`. This is highly efficient. To get 10 times more accuracy (e.g., reducing `ε` from 0.1 to 0.01), you do not need 10 times the work, but only a small, constant amount of additional work (`log(10)`). This is a significant advantage.

* **Dependence on State/Action Space (S, A):** The cost grows polynomially with the number of states (`S²`) and linearly with the number of actions (`A`). This is computationally expensive and is the primary reason why Value Iteration is intractable for problems with very large or continuous state spaces, a phenomenon often called the "Curse of Dimensionality."

* **Dependence on the Discount Factor (γ):** The cost is highly sensitive to `γ`. As `γ` approaches 1 (i.e., the agent becomes more far-sighted), the `1/(1-γ)²` term explodes. This means that solving problems with very long time horizons is extremely computationally demanding. A discount factor of `γ=0.9` leads to a factor of `1/(0.1)² = 100`, while `γ=0.99` leads to `1/(0.01)² = 10,000`—a 100-fold increase in computation for a small change in `γ`.

---

Show me the full mathematical steps and details regarding the new algorithm, Policy Iteration, is introduced as an alternative that can find an exact optimal policy without the approximations inherent in stopping Value Iteration early.

The Algorithm: Policy Iteration works in two repeating steps:
Policy Evaluation: Given the current policy πₖ, exactly calculate its value function Vπₖ. This is done by solving a system of linear equations derived from the Bellman expectation equation [01:09:22].
Policy Improvement: Create a new, better policy π_{k+1} by acting greedily with respect to the value function Vπₖ calculated in the previous step [01:08:23].
Termination and Optimality: This process is repeated until the policy no longer changes, at which point it is guaranteed to be the optimal policy [01:12:57].
Convergence Speed: A key advantage highlighted is that Policy Iteration is proven to terminate after a polynomial number of iterations in S, A, and 1/(1-γ), with no dependence on ε [01:14:47]. The proof involves showing that actions are progressively eliminated from states until only the optimal actions remain [01:16:43].

Of course. Here are the full mathematical steps and details for the Policy Iteration algorithm, explaining how it finds an exact optimal policy.

### **Introduction to Policy Iteration**

Policy Iteration (PI) is a fundamental algorithm in reinforcement learning that provides an alternative to Value Iteration (VI). Unlike VI, which iteratively approximates the optimal value function `V*`, PI directly manipulates the policy `π`. It operates in a loop, generating a sequence of monotonically improving policies `π₀, π₁, π₂, ...` that is guaranteed to converge to the exact optimal policy, `π*`, in a finite number of steps.

The algorithm consists of two core, repeating steps: **Policy Evaluation** and **Policy Improvement**.

---

### **Step 1: Policy Evaluation (The "E" Step)**

**Objective:** For a given policy `πₖ`, calculate its exact value function, `Vπₖ`.

For a fixed policy `π`, the value function `Vπ` must satisfy the Bellman expectation equation for every state `s ∈ S`:

$$V^\pi(s) = \sum_{s'} P(s'|s, \pi(s)) \left[ R(s, \pi(s), s') + \gamma V^\pi(s') \right]$$

This is not an iterative update rule like in Value Iteration. Instead, for a given `π`, this is a system of `|S|` linear equations with `|S|` unknowns (the variables being `Vπ(s₁), Vπ(s₂), ..., Vπ(s_{|S|})`).

**Mathematical Formulation:**

We can express this system in a more structured matrix-vector form.

1.  **Define the Value Vector `Vπ`:**
    An `|S|` x 1 column vector containing the value of each state under policy `π`.
    $$
    V^\pi = \begin{bmatrix} V^\pi(s_1) \\ V^\pi(s_2) \\ \vdots \\ V^\pi(s_{|S|}) \end{bmatrix}
    $$

2.  **Define the Reward Vector `Rπ`:**
    An `|S|` x 1 column vector where each element is the expected immediate reward from that state under policy `π`.
    $$
    R^\pi(s) = \sum_{s'} P(s'|s, \pi(s)) R(s, \pi(s), s')
    $$

3.  **Define the Transition Probability Matrix `Pπ`:**
    An `|S|` x `|S|` matrix where the element `(i, j)` is the probability of transitioning from state `sᵢ` to state `sⱼ` while following policy `π`.
    $$
    P^\pi_{ij} = P(s_j | s_i, \pi(s_i))
    $$

With these definitions, the system of `|S|` Bellman equations can be written concisely as:

$$V^\pi = R^\pi + \gamma P^\pi V^\pi$$

**Solving for `Vπ`:**

This is a standard linear system. We can solve for `Vπ` algebraically:
$$(I)V^\pi - \gamma P^\pi V^\pi = R^\pi$$
$$(I - \gamma P^\pi) V^\pi = R^\pi$$

The matrix `(I - γPπ)` is guaranteed to be invertible. Therefore, the exact value function for policy `π` is given by:

$$V^\pi = (I - \gamma P^\pi)^{-1} R^\pi$$

**Computational Cost:** The direct solution via matrix inversion has a computational complexity of `O(S³)`. This is a significant cost per iteration compared to Value Iteration's `O(S²A)`.

---

### **Step 2: Policy Improvement (The "I" Step)**

**Objective:** Given the exact value function `Vπₖ` for the current policy `πₖ`, find a new, strictly better policy, `π_{k+1}`.

The new policy is created by acting greedily with respect to `Vπₖ`. For each state `s`, we find the action `a` that maximizes the one-step lookahead value.

**Mathematical Formulation:**

1.  First, for every state-action pair, calculate the action-value function `Qπₖ(s, a)`:
    $$Q^{\pi_k}(s, a) = \sum_{s'} P(s'|s, a) \left[ R(s, a, s') + \gamma V^{\pi_k}(s') \right]$$

2.  The new policy `π_{k+1}` simply chooses the best action according to this Q-function:
    $$\pi_{k+1}(s) = \underset{a \in A}{\arg\max} \, Q^{\pi_k}(s, a)$$

This new policy `π_{k+1}` is guaranteed to be a strict improvement over `πₖ` unless `πₖ` is already optimal. This is proven by the **Policy Improvement Theorem**.

**Proof of the Policy Improvement Theorem:**
Let `π'` be the new greedy policy with respect to `Vπ`. For any state `s`:
$$
\begin{aligned}
V^\pi(s) &\leq Q^\pi(s, \pi'(s)) \quad \text{(By definition of the greedy choice } \pi') \\
&= E_{\pi'}[R_{t+1} + \gamma V^\pi(s_{t+1}) | s_t=s] \quad \text{(Unrolling the Q-function)} \\
&\leq E_{\pi'}[R_{t+1} + \gamma Q^\pi(s_{t+1}, \pi'(s_{t+1})) | s_t=s] \quad \text{(Applying the inequality again for } s_{t+1}) \\
&\leq E_{\pi'}[R_{t+1} + \gamma R_{t+2} + \gamma^2 V^\pi(s_{t+2}) | s_t=s] \quad \text{(Unrolling one more step)} \\
&\vdots \\
&\leq V^{\pi'}(s)
\end{aligned}
$$
This shows `Vπ'(s) ≥ Vπ(s)` for all `s`. If there is any state where the new policy's action is different from the old policy's, the inequality `Vπ(s) < Qπ(s, π'(s))` becomes strict, which propagates through the derivation to ensure `Vπ'(s) > Vπ(s)`.

---

### **Step 3: Termination and Optimality Guarantee**

The two steps—Evaluation and Improvement—are repeated until the policy no longer changes between iterations.

**Termination Condition:** The algorithm terminates when `π_{k+1} = πₖ`.

**Proof of Optimality at Termination:**
When the policy no longer improves, it means that for all states `s`, the action chosen by `πₖ` is already the greedy action with respect to its own value function `Vπₖ`.

$$\pi_k(s) = \underset{a \in A}{\arg\max} \, Q^{\pi_k}(s, a)$$

This implies that:
$$V^{\pi_k}(s) = Q^{\pi_k}(s, \pi_k(s)) = \max_{a \in A} Q^{\pi_k}(s, a)$$

If we write out the right-hand side, we get:
$$V^{\pi_k}(s) = \max_{a \in A} \sum_{s'} P(s'|s, a) \left[ R(s, a, s') + \gamma V^{\pi_k}(s') \right]$$

This is precisely the **Bellman optimality equation**. We know that any value function that satisfies the Bellman optimality equation must be the optimal value function, `V*`. Therefore, at termination, `Vπₖ = V*`, and the policy `πₖ` is an optimal policy, `π*`.

---

### **Convergence Speed and Analysis**

* **Finite Termination:** There is a finite number of possible deterministic policies (`|A|^|S|`). Because the Policy Improvement Theorem guarantees that each new policy is strictly better than the last (unless it's optimal), the algorithm will never visit the same policy twice. Therefore, it must terminate in a finite number of iterations.

* **Polynomial Convergence:** While the worst-case number of policies is exponential, the number of iterations for Policy Iteration is proven to be **polynomial** in `|S|`, `|A|`, and `1/(1-γ)`. The intuition for this stronger result is that each improvement step corrects a "mistake" (a suboptimal action choice) in at least one state. Since there is a finite, polynomially-bounded number of such mistakes to fix, the algorithm converges much faster than the worst-case bound suggests.

* **No `ε` Dependence:** A major advantage of Policy Iteration is that its convergence does not depend on a precision parameter `ε`. It works to find the exact optimal policy directly. This contrasts sharply with Value Iteration, whose runtime is logarithmically dependent on the desired precision `1/ε` and quadratically on the discount factor `1/(1-γ)`.


---


Now, comparing the algorithms and discussing the fundamental complexity of planning in MDPs.

Lower Bounds: The speaker discusses the theoretical minimum complexity required to solve an MDP, noting that there is a gap between the known lower bounds (O(S²A)) and the upper bounds of algorithms like Policy Iteration [01:28:44].
Role of the Discount Factor γ: There is a discussion on whether the 1/(1-γ) dependence is necessary, concluding that it is relevant for large problems but can be avoided in smaller state spaces by simply enumerating all possible policies [01:29:05].
Exact vs. Approximate: A final trade-off is discussed: Value Iteration is generally preferred for its speed in finding good approximate policies, while Policy Iteration provides a path to an exact optimal policy [01:31:34].

Show me all the mathematical details.


Of course. Here is a detailed comparison of Value Iteration and Policy Iteration, followed by a discussion of the fundamental complexity of planning in MDPs, incorporating the mathematical details you've highlighted.

### **Comparative Analysis: Value Iteration vs. Policy Iteration**

| Feature | Value Iteration (VI) | Policy Iteration (PI) |
| :--- | :--- | :--- |
| **Primary Goal** | To find the optimal value function, `V*`. The optimal policy `π*` is an implicit byproduct. | To find the optimal policy, `π*`. The value function `Vπ` is an intermediate calculation. |
| **Core Operation** | Iteratively applying the Bellman optimality operator, which is a `max` operation over actions. \<br\> `V_{k+1}(s) = \max_a E[...]` | A two-step process: \<br\> 1. **Policy Evaluation:** Solving a system of linear equations for `Vπ`. \<br\> 2. **Policy Improvement:** A greedy `argmax` over actions. |
| **Output** | An **approximate** optimal value function `Vₖ ≈ V*` and the corresponding approximate policy `π`. | The **exact** optimal policy `π*` and its exact value function `V*`. |
| **Cost Per Iteration**| `O(S²A)` | `O(S²A + S³)` (Dominated by `O(S³)` for the matrix inversion in Policy Evaluation) |
| **Number of Iterations** | `O( (log(1/ε) + log(1/(1-γ))) / (1-γ) )` \<br\> Depends on `ε` and `γ`. | Polynomial in `S`, `A`, and `1/(1-γ)`. \<br\> Independent of `ε`. Often converges in very few iterations. |
| **Overall Complexity** | `O( S²A * (log(1/ε) / (1-γ)) )` \<br\> (Using the tighter bound) | `O( poly(S, A, 1/(1-γ)) )` |
| **Key Advantage**| Fast iterations; can be stopped anytime for a good approximate policy. Generally preferred for large `S`. | Finds the exact optimal policy in a finite, often small, number of iterations. No `ε` to tune. |
| **Key Disadvantage**| Only produces an `ε`-optimal policy. Very sensitive to `γ` approaching 1. | Very expensive iterations due to solving a linear system (`O(S³)`), making it impractical for large `S`. |

-----

### **Fundamental Complexity of MDP Planning**

This section delves into the theoretical limits and trade-offs in solving MDPs.

#### **1. Lower Bounds and the Complexity Gap**

A **lower bound** on a problem's complexity is the theoretical minimum amount of computational work that *any* algorithm must perform in the worst case to solve it.

  * **The `Ω(S²A)` Lower Bound:** To solve an MDP, an algorithm must, at a minimum, have enough information to distinguish it from other MDPs. The transition function `P(s'|s, a)` contains `S × A × S = S²A` entries, and the reward function `R(s, a, s')` also has up to `S²A` entries. An algorithm that doesn't examine almost all of this information can be fooled. For instance, if a single, high-reward transition is "hidden" in a part of the state space the algorithm never queries, it cannot find the optimal policy. Therefore, any algorithm must take at least `Ω(S²A)` time simply to read its input.

  * **The "Gap":**

      * **Lower Bound:** `Ω(S²A)`
      * **Upper Bound (from PI/VI):** `O(poly(S, A, 1/(1-γ)))`

    There is a "gap" between the known lower bound and the upper bound of the best-known algorithms. This gap is the `poly(1/(1-γ))` factor. It remains a major open question in reinforcement learning theory whether this dependence on the discount factor `γ` is fundamental to the problem or if a "strongly polynomial" time algorithm exists whose runtime depends only on `S` and `A`.

#### **2. The Role of the Discount Factor `γ`**

The term `1/(1-γ)` can be interpreted as the "effective time horizon" of the problem. The discussion on whether this dependence is necessary leads to a fascinating comparison based on the size of the state space.

  * **Argument 1: The `1/(1-γ)` Dependence is Necessary.**
    In large problems, `γ` determines how far information must propagate. If `γ` is close to 1, a reward in a distant state can have a significant impact on the optimal decision in the current state. The `1/(1-γ)` term in the complexity reflects the "time" required for the value of a state to propagate through the entire state-space graph. Algorithms like Value Iteration and Policy Iteration are based on this propagation (or "dynamic programming") principle, and their complexity inherently reflects this.

  * **Argument 2: The `1/(1-γ)` Dependence Can Be Avoided (in specific cases).**
    Consider a brute-force approach:

    1.  **Enumerate all possible deterministic policies.** The total number of such policies is `|A|^|S|`.
    2.  **For each policy `π`, evaluate it.** As we saw, this can be done by solving a system of linear equations, which costs `O(S³)` time.
    3.  **Keep track of the best policy found so far.**

    The total computational cost of this "policy enumeration" algorithm is:

    $$\text{Cost}_{\text{Enum}} = O(|A|^{|S|} \cdot S^3)$$

    Notice two critical properties of this complexity:

    1.  There is **no dependence on `γ`**.
    2.  There is **no dependence on `ε`** (it finds the exact optimum).

    Now we can compare this to the complexity of Policy Iteration:
    $$\text{Cost}_{\text{PI}} \approx O(\text{poly}(S, A, \frac{1}{1-\gamma}))$$

    The trade-off is clear:

      * If `|A|^|S|` is smaller than `poly(1/(1-γ))`, then brute-force enumeration is asymptotically faster. This only happens when `S` (the exponent) is very small. For example, if S=3 and A=2, then `|A|^|S| = 8`, which is a tiny number.
      * However, for any reasonably large `S` (e.g., S=50, A=2), the `|A|^|S|` term becomes astronomically large, and the polynomial dependence on `1/(1-γ)` is vastly superior.

    **Conclusion:** The dependence on `γ` is a feature of algorithms that solve the problem via dynamic programming. It can be avoided by policy enumeration, but this is only feasible for MDPs with a very small number of states.

#### **3. The Final Trade-off: Exact vs. Approximate Solutions**

This brings us to the most practical consideration when choosing between the algorithms.

  * **Value Iteration** is the algorithm of choice for finding **good approximate policies quickly**. Its low cost per iteration (`O(S²A)`) and its "anytime" nature (it can be stopped early) make it highly practical, especially when the state space `S` is large. One can run it for a fixed number of iterations or until the value function stabilizes to a desired degree, yielding a policy that is provably near-optimal.

  * **Policy Iteration** is the algorithm for finding an **exact optimal policy**. It is guaranteed to converge to `π*` and often does so in a surprisingly small number of iterations. However, the high cost of each iteration (`O(S³)`) makes it computationally prohibitive for MDPs with thousands of states or more. It is best suited for problems where precision is paramount and the state space is manageably small.
