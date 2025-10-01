---
_build:
  render: never
  list: never

date: "2025-06-30"
title: "Value Iteration"
summary: "Value Iteration"
category: Tutorial
series: ["RL Theory", "RL Experimentation"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

Why in (https://www.youtube.com/watch?v=4Rf1hzE5MsQ), in planning problems, histories don't include rewards?

In the context of the specified video, histories in planning problems do not include rewards for a specific reason related to the problem's structure.

According to the video, the reward is considered an outcome that is given to the policy, rather than being part of the history that the policy uses to make decisions \[[08:03](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=483)\]. The central question in these planning problems is whether a policy can achieve better results by considering the full history of states and actions, instead of just the current state.

The reward doesn't influence the decision-making process in the same way that past states and actions do, particularly in a planning context where the model of the environment (the Markov Decision Process or MDP) is known. This is distinct from a learning scenario where the agent does not know the MDP and must learn from rewards \[[08:19](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=499)\].
http://googleusercontent.com/youtube_content/0


---

What are they doing between 13:00 and 36:00?

Between 13:00 and 36:00, the speaker in the video is engaged in a detailed mathematical proof related to optimal value functions in Markov Decision Processes (MDPs) and then introduces a core algorithm for solving them.

Here is a summary of the activities in that time frame:

* **Proving a Fundamental Theorem:** The main focus is on proving that a "greedy" policy (a policy that always chooses the action that looks best according to a given value function) is optimal if its value function is equal to the optimal value function.
    * **Part 1 of the Proof:** The speaker demonstrates that the value function of a policy that is greedy with respect to an optimal value function (`v*`) is, in fact, equal to `v*` itself \[[15:10](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=910)\]. This involves showing that the value function of the policy is both less than or equal to `v*` \[[15:59](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=959)\] and greater than or equal to `v*` \[[16:22](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=982)\]. The proof relies on the properties of Bellman operators and the Banach fixed-point theorem, showing convergence after iterative applications \[[25:30](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=1530)\].
    * **Part 2 of the Proof:** They then prove that the optimal value function (`v*`) is a fixed point of the Bellman optimality operator, meaning that applying the operator to `v*` yields `v*` \[[28:20](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=1700)\].

* **Introducing Value Iteration:** After completing the proofs, the speaker transitions to a practical method for finding the optimal value function.
    * They introduce the **Value Iteration** algorithm \[[35:49](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2149)\], which involves repeatedly applying the Bellman optimality operator, starting from an arbitrary value function, to converge to the true optimal value function (`v*`) \[[36:29](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2189)\].
    * The speaker also discusses the convergence rate, noting that it is exponentially fast, and analyzes the number of iterations required to achieve a desired accuracy \[[39:29](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2369)\].

http://googleusercontent.com/youtube_content/2

---

Show me the full proof that a "greedy" policy (a policy that always chooses the action that looks best according to a given value function) is optimal if its value function is equal to the optimal value function.

Of course. While the video discusses the components of the proof, it doesn't present it in a complete, formal sequence. Based on established principles of Markov Decision Processes, here is the full proof demonstrating that a policy which is greedy with respect to the optimal value function is, itself, an optimal policy.

### **1. Definitions and Foundations**

First, let's define the key terms:

* **State Value Function `Vπ(s)`**: The expected cumulative discounted reward starting from state `s` and following policy `π`.
* **Optimal State Value Function `V*(s)`**: The maximum possible state value function over all policies. `V*(s) = max_π Vπ(s)`.
* **Action Value Function `Qπ(s, a)`**: The expected cumulative discounted reward from taking action `a` in state `s`, and then following policy `π`.
* **Bellman Expectation Equation**: For a given policy `π`, its value function `Vπ` satisfies:
    `Vπ(s) = E[R_{t+1} + γVπ(S_{t+1}) | S_t=s, A_t=π(s)]`
    This can be written in terms of the Q-function as `Vπ(s) = Qπ(s, π(s))`.
* **Bellman Optimality Equation**: The optimal value function `V*(s)` is unique and satisfies this equation:
    `V*(s) = max_a E[R_{t+1} + γV*(S_{t+1}) | S_t=s, A_t=a]`
    This can also be written using the optimal Q-function, `Q*(s, a)`:
    `V*(s) = max_a Q*(s, a)`

### **2. The Policy Improvement Theorem**

The core of the proof lies in the **Policy Improvement Theorem**. This theorem states that if we take a policy `π` and create a new "greedy" policy `π'` that, for every state `s`, chooses the action that looks best according to the value function of the *original* policy (`Vπ`), then this new policy `π'` is guaranteed to be at least as good as, or better than, the original policy `π`.

Formally, let `π` and `π'` be two policies such that for all states `s`:
`Qπ(s, π'(s)) ≥ Vπ(s)`

Then the theorem states that the new policy is an improvement:
`Vπ'(s) ≥ Vπ(s)` for all `s ∈ S`.

### **3. The Proof**

Now, let's construct the proof:

1.  Let `π*` be an optimal policy. By definition, its value function is `V*(s)`.
2.  Let `π_greedy` be a policy that is "greedy" with respect to this optimal value function, `V*(s)`. This means that for any state `s`, `π_greedy` chooses the action that maximizes the expected value, assuming the subsequent states will also have the optimal value `V*`:

    `π_greedy(s) = argmax_a E[R_{t+1} + γV*(S_{t+1}) | S_t=s, A_t=a]`

    This is equivalent to saying:

    `π_greedy(s) = argmax_a Q*(s, a)`

3.  Now let's evaluate the value function for this greedy policy, `V^{π_greedy}(s)`. We start with the Bellman equation for `V^{π_greedy}(s)`:

    `V^{π_greedy}(s) = E[R_{t+1} + γV^{π_greedy}(S_{t+1}) | S_t=s, A_t=π_greedy(s)]`

4.  From step 2, we know that the action `π_greedy(s)` is the one that maximizes the right-hand side of the Bellman Optimality Equation. Therefore, for any state `s`, the value obtained by following the greedy policy for one step is equal to the optimal value `V*(s)`:

    `V*(s) = max_a Q*(s, a) = Q*(s, π_greedy(s))`

5.  This shows that the policy `π_greedy` satisfies the condition for being an optimal policy. If we apply the policy improvement logic, we can see that since `π_greedy` is already greedy with respect to `V*`, we cannot find a better policy. Any attempt at "improving" it by making it greedy with respect to its own value function (`V*`) will result in the same policy.

6.  Because the policy `π_greedy` satisfies the Bellman optimality equation (`Vπ(s) = max_a Qπ(s,a)`), its value function must be the optimal value function, `V*`.

Therefore, any policy that is greedy with respect to the optimal value function is an optimal policy.
http://googleusercontent.com/youtube_content/4

---

Show me the full discussion regarding value iteration in the lecture.


Based on the lecture, here is the full discussion regarding the Value Iteration algorithm.

### The Value Iteration Algorithm

The lecture introduces Value Iteration as a fundamental algorithm for finding the optimal value function, `V*`, in a Markov Decision Process \[[35:40](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2140)\]. The process is as follows:

1.  **Initialization**: Start with an arbitrary value function, `V₀`. A common and simple choice is to initialize it as a vector of zeros for all states \[[36:29](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2189)\].
2.  **Iteration**: Iteratively compute the next value function, `V_{k+1}`, by applying the Bellman optimality operator, `T`, to the current value function, `Vₖ` \[[36:44](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2204)\]. The update rule is:

    `V_{k+1}(s) = max_a E[R_{t+1} + γV_k(S_{t+1}) | S_t=s, A_t=a]`

    This operation is performed for every state `s` in each iteration. It involves calculating the expected future reward for each action, discounting it, adding the immediate reward, and then taking the maximum over all possible actions \[[36:56](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2216)\].

### Convergence Properties

The discussion highlights that Value Iteration is guaranteed to converge to the optimal value function, `V*`.

* **Rate of Convergence**: The convergence is guaranteed to be exponentially fast, a property derived from the Banach Fixed Point Theorem, as the Bellman operator is a contraction mapping \[[37:20](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2240)\].
* **Error Bound**: The error between the iterated value function `Vₖ` and the optimal `V*` (measured in the max-norm) is bounded. Assuming rewards are between 0 and 1, the bound is given by \[[39:16](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2356)\]:

    `||Vₖ - V*||∞ ≤ γᵏ / (1 - γ)`

* **Number of Iterations**: To achieve an ε-accurate estimate of `V*`, the required number of iterations, `k`, has a mild logarithmic dependence on `1/ε`, which underscores the algorithm's efficiency \[[39:42](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2382)\]:

    `k ≈ log(1/ε) / log(1/γ)`

### Computational Cost

The lecture analyzes the computational complexity of the algorithm:

* **Cost per Iteration**: For each iteration, the algorithm must update the value for every state. For each state, it considers every action and then averages over all possible next states. This results in a computational cost per iteration of approximately **O(S²A)**, where `S` is the number of states and `A` is the number of actions \[[01:03:51](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3831)\].
* **Total Complexity**: The total computational cost to find a policy that is ε-optimal is approximately \[[01:03:43](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3823)\]:

    **O(S²A * log(1/ε) / (1 - γ)²)**

Finally, it is noted that while Value Iteration is highly effective for finding an *approximate* solution, it might run indefinitely if an exact solution is required, especially in scenarios with very small value differences \[[01:30:36](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=5436)\].
http://googleusercontent.com/youtube_content/6

---

Show me the full mathematics of the discussion.

Here is a consolidated view of the full mathematics discussed in the lecture, covering the proof of optimality and the Value Iteration algorithm.

### **Part 1: The Mathematics of Optimality**

1.  **State-Value and Action-Value Functions:**
    * The value of a state `s` under a policy `π` with discount factor `γ`:
        $$V^\pi(s) = E_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R_{t+1} | S_t = s \right]$$
    * The value of taking action `a` in state `s` and then following policy `π`:
        $$Q^\pi(s, a) = E_\pi \left[ \sum_{t=0}^{\infty} \gamma^t R_{t+1} | S_t = s, A_t = a \right]$$

2.  **Bellman Expectation Equation:**
    This equation relates the value of a state to the value of its successor states under a given policy `π`.
    $$V^\pi(s) = \sum_{a} \pi(a|s) \sum_{s', r} p(s', r|s, a) [r + \gamma V^\pi(s')]$$

3.  **Optimal Value Functions:**
    The optimal functions are the maximum achievable values over all possible policies.
    * Optimal State-Value Function:
        $$V^*(s) = \max_{\pi} V^\pi(s)$$
    * Optimal Action-Value Function:
        $$Q^*(s, a) = \max_{\pi} Q^\pi(s, a)$$

4.  **Bellman Optimality Equation:**
    The optimal value functions satisfy a special relationship that is the basis for most reinforcement learning algorithms.
    $$V^*(s) = \max_{a} \sum_{s', r} p(s', r|s, a) [r + \gamma V^*(s')]$$
    In terms of the optimal Q-function, this is:
    $$V^*(s) = \max_{a} Q^*(s, a)$$

5.  **Optimal Greedy Policy:**
    A policy `π*` is optimal if it is greedy with respect to the optimal value function `V*`. This means for any state `s`, it chooses the action that maximizes the expected return.
    $$\pi^*(s) = \text{argmax}_{a} \sum_{s', r} p(s', r|s, a) [r + \gamma V^*(s')]$$
    Which simplifies to:
    $$\pi^*(s) = \text{argmax}_{a} Q^*(s, a)$$

### **Part 2: The Mathematics of Value Iteration**

Value Iteration is an algorithm to find `V*` by turning the Bellman Optimality Equation into an iterative update rule.

1.  **The Bellman Optimality Operator (T):**
    The core of Value Iteration is the application of an operator `T` which takes a value function `V` as input and returns a new value function `V'`.
    $$(TV)(s) = \max_{a} \sum_{s', r} p(s', r|s, a) [r + \gamma V(s')]$$

2.  **The Algorithm:**
    The algorithm is a sequence of value functions `{V₀, V₁, V₂, ...}` that converges to `V*`.
    * **Initialization**: `V₀(s) = 0` for all `s ∈ S`.
    * **Iteration**: For `k = 0, 1, 2, ...`
        $$V_{k+1} \leftarrow TV_k$$
        This means for every state `s`:
        $$V_{k+1}(s) = \max_{a} \sum_{s', r} p(s', r|s, a) [r + \gamma V_k(s')]$$

3.  **Convergence (Banach Fixed-Point Theorem):**
    The operator `T` is a contraction mapping in the max-norm (`||.||∞`), which guarantees convergence.
    * **Contraction**: For any two value functions `U` and `V`:
        $$||TU - TV||_\infty \le \gamma ||U - V||_\infty$$
    * **Convergence**: The sequence `{V_k}` converges to the unique fixed point `V*`:
        $$\lim_{k \to \infty} V_k = V^*$$

4.  **Error Bound:**
    The distance between the `k`-th value function `Vₖ` and the optimal `V*` is bounded.
    $$||V_k - V^*||_\infty \le \gamma^k ||V_0 - V^*||_\infty$$
    Assuming rewards are in `[0, 1]` and `V₀` is zero, the bound becomes:
    $$||V_k - V^*||_\infty \le \frac{\gamma^k}{1 - \gamma}$$

5.  **Number of Iterations for ε-Accuracy:**
    To guarantee that `||V_k - V^*||_\infty \le \epsilon`, the number of iterations `k` must be at least:
    $$k \ge \frac{\log(1/(\epsilon(1-\gamma)))}{\log(1/\gamma)}$$
    A simpler approximation is often given as:
    $$k \approx \frac{\log(1/\epsilon)}{\log(1/\gamma)}$$

6.  **Computational Complexity:**
    * **Per Iteration**: `O(S²A)`
    * **Total Complexity for ε-optimality**: `O(S²A \cdot \frac{\log(1/\epsilon)}{(1-\gamma)^2})`

---

Provide me the geometrical interpretation of value iteration.


Of course. The mathematics of Value Iteration has a very elegant and intuitive geometrical interpretation. Let's build it step by step.

### 1\. The Space: A Universe of Value Functions

Imagine a vast space where every single point represents one possible value function. If your environment has `S` states, then a value function `V` is simply a list of `S` numbers, one for each state `(V(s₁), V(s₂), ..., V(s_S))`.

Therefore, we can think of this space as an **`S`-dimensional Euclidean space (`ℝ^S`)**.

  * **A point `V`** in this space is a vector representing a specific value function.
  * Each **axis** of this space corresponds to the value of a particular state.
  * The **origin** of this space `(0, 0, ..., 0)` is the zero value function, `V₀`, which is the typical starting point for the algorithm.
  * Somewhere in this space, there is one very special point: the **optimal value function, `V*`**. This is our target.

### 2\. The Transformation: The Bellman Operator

The Bellman optimality operator, `T`, acts as a **geometric transformation** within this space. It takes any point `V` and maps it to a new point, `V_{new} = T(V)`.

Value Iteration is the process of starting at `V₀` and repeatedly applying this transformation:

  * `V₁ = T(V₀)`
  * `V₂ = T(V₁)`
  * `V₃ = T(V₂)`
  * ... and so on.

Geometrically, the algorithm generates a sequence of points `{V₀, V₁, V₂, ...}` that trace a path through this `S`-dimensional space. The core question is: why does this path always lead to `V*`?

### 3\. The Destination: A Unique Fixed Point

The optimal value function `V*` is a **fixed point** of the operator `T`. This means that if you apply the transformation to `V*`, it doesn't move:
`T(V*) = V*`
Geometrically, `V*` is the one point in the entire space that is mapped onto itself by the Bellman transformation. Our goal is to find this unique point.

### 4\. The Guarantee: A Contraction Mapping

This is the most crucial part of the geometric interpretation. The Bellman operator `T` is a **contraction mapping**.

Imagine two points in our space, `U` and `V`. A contraction mapping is a transformation that, when applied to these two points, **always brings their images closer together**.
Mathematically:
`||TU - TV||_\infty ≤ γ ||U - V||_\infty`

Where `γ` (the discount factor) is less than 1.

Geometrically, this means:

  * Start with any two value functions, `U` and `V`.
  * Apply the Bellman operator to both, yielding `T(U)` and `T(V)`.
  * The distance between the new points will be smaller than the distance between the original points by at least a factor of `γ`.

**The Analogy:**
Think of a treasure map where `V*` is the location of the treasure. The Bellman operator `T` is a magical instruction. No matter where your current guess `V_k` is, the instruction `T` gives you a new, better guess `V_{k+1}`. Because `T` is a contraction, every step you take not only moves you, but it's guaranteed to move you **closer** to the true treasure `V*`. Since every step reduces your distance to the target, your path is guaranteed to eventually converge to the single fixed point `V*`.

The path of Value Iteration is not a random walk; it's a determined, shrinking spiral (in high dimensions) that inevitably zeroes in on `V*`.

*In this 2D illustration (for S=2 states), the algorithm starts at V₀ and iteratively applies the operator T. Each step gets closer to the fixed point V*, where the 45-degree line (V = TV) intersects the function.\*

---


What's being discussed after 36:00 till the end of the video.


Following the introduction of Value Iteration at 36:00, the remainder of the lecture delves deeper into its properties, introduces a new algorithm called Policy Iteration, and concludes with a discussion on computational complexity.

Here is a breakdown of the topics discussed:

### 1. In-Depth Analysis of Value Iteration [Starts at 00:36:17]

The lecture continues the discussion of Value Iteration, moving from the basic algorithm to its practical application and theoretical guarantees.
* **Extracting a Policy**: It explains how to derive a near-optimal policy once you have an approximately correct value function, `Vₖ`. This is done by "greedifying" the policy—choosing the action that looks best according to `Vₖ` \[[44:42](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=2682)\].
* **Performance Guarantee**: A key proof is presented showing that if your value function `Vₖ` is `ε`-close to the true optimal value function `V*`, the resulting greedy policy `π` will have a value function `Vπ` that is near-optimal within a bound of `2εγ / (1 - γ)` \[[01:00:48](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3648)\].
* **Complexity Summary**: The total computational cost of Value Iteration to find a near-optimal policy is summarized as being approximately `O(S²A * log(1/ε) / (1-γ)²)`, highlighting its efficiency in terms of accuracy (`ε`) but its dependence on the state/action space and the discount factor `γ` \[[01:03:43](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=3823)\].

### 2. Policy Iteration: An Alternative Approach [Starts at 01:05:05]

A new algorithm, Policy Iteration, is introduced as an alternative that can find an exact optimal policy without the approximations inherent in stopping Value Iteration early.
* **The Algorithm**: Policy Iteration works in two repeating steps:
    1.  **Policy Evaluation**: Given the current policy `πₖ`, exactly calculate its value function `Vπₖ`. This is done by solving a system of linear equations derived from the Bellman expectation equation \[[01:09:22](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=4162)\].
    2.  **Policy Improvement**: Create a new, better policy `π_{k+1}` by acting greedily with respect to the value function `Vπₖ` calculated in the previous step \[[01:08:23](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=4103)\].
* **Termination and Optimality**: This process is repeated until the policy no longer changes, at which point it is guaranteed to be the optimal policy \[[01:12:57](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=4377)\].
* **Convergence Speed**: A key advantage highlighted is that Policy Iteration is proven to terminate after a polynomial number of iterations in `S`, `A`, and `1/(1-γ)`, with no dependence on `ε` \[[01:14:47](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=4487)\]. The proof involves showing that actions are progressively eliminated from states until only the optimal actions remain \[[01:16:43](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=4603)\].

### 3. Computational Complexity and Concluding Remarks [Starts at 01:24:34]

The lecture concludes by comparing the algorithms and discussing the fundamental complexity of planning in MDPs.
* **Lower Bounds**: The speaker discusses the theoretical minimum complexity required to solve an MDP, noting that there is a gap between the known lower bounds (`O(S²A)`) and the upper bounds of algorithms like Policy Iteration \[[01:28:44](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=5324)\].
* **Role of the Discount Factor `γ`**: There is a discussion on whether the `1/(1-γ)` dependence is necessary, concluding that it is relevant for large problems but can be avoided in smaller state spaces by simply enumerating all possible policies \[[01:29:05](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=5345)\].
* **Exact vs. Approximate**: A final trade-off is discussed: Value Iteration is generally preferred for its speed in finding good *approximate* policies, while Policy Iteration provides a path to an *exact* optimal policy \[[01:31:34](http://www.youtube.com/watch?v=4Rf1hzE5MsQ&t=5494)\].

http://googleusercontent.com/youtube_content/10


































