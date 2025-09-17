---
date: "2025-07-06"
title: "(Part 2.1) Value Iteration and its Theoretical Foundations"
summary: "Value Iteration and its Theoretical Foundations"
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

### **Value Iteration for Finite Markov Decision Processes: A Theoretical and Algorithmic Roadmap**

This document provides a comprehensive analysis of Value Iteration (VI), a foundational algorithm for solving finite, discounted Markov Decision Processes (MDPs). We begin by establishing the theoretical framework of dynamic programming, then introduce the VI algorithm as a direct consequence of the contraction-mapping principle. We proceed to analyze its correctness and computational complexity, culminating in a practical algorithm with rigorous performance guarantees. Finally, we situate Value Iteration within the broader landscape of planning algorithms by exploring alternative formulations and advanced perspectives.

### **Part I: Foundations of Optimal Control in MDPs**

#### **1. The Finite Markov Decision Process (MDP)**

We begin with the formal definition of the environment. A finite, \(\gamma\)-discounted Markov Decision Process is a tuple \(M = (S, A, P, r, \gamma)\), where:

* \(S = \{1, \dots, |S|\}\) is a finite set of states.
* \(A = \{1, \dots, |A|\}\) is a finite set of actions.
* \(P_a(s, s') = \Pr\{s_{t+1}=s' \mid s_t=s, a_t=a\}\) is the transition probability matrix for each action \(a \in A\). We use \(P_a(s)\) to denote the corresponding row vector of probabilities.
* \(r_a(s) \in [0, 1]\) is the bounded, immediate reward received after taking action \(a\) in state \(s\).
* \(\gamma \in [0, 1)\) is the discount factor.

A **stationary policy** \(\pi: S \to \Delta(A)\) is a mapping from states to a probability distribution over actions, where \(\pi(a|s)\) is the probability of choosing action \(a\) in state \(s\).

The objective is to find a policy that maximizes the expected cumulative discounted reward. The **state-value function** for a policy \(\pi\) is the expected return starting from state \(s\) and following \(\pi\):
$$
v^\pi(s) = \mathbb{E}_s^\pi \left[ \sum_{t=0}^{\infty} \gamma^t r_{a_t}(s_t) \right]
\tag{1}
$$The **state-action value function** is the expected return after taking action \(a\) in state \(s\) and subsequently following policy \(\pi\):$$
q^\pi(s, a) = r_a(s) + \gamma \sum_{s'} P_a(s, s') v^\pi(s')
\tag{2}
$$

#### **2. Bellman Equations and the Fundamental Theorem of Dynamic Programming**

The value functions for any policy \(\pi\) obey a set of linear equations known as the Bellman equations. These can be expressed using the **Bellman policy operator**, \(T_\pi\):
$$
(T_\pi v)(s) = \sum_{a} \pi(a|s) \left[ r_a(s) + \gamma P_a(s)^\top v \right]
\tag{3}
$$
The value function \(v^\pi\) is the unique fixed point of this operator: \(v^\pi = T_\pi v^\pi\).

The goal of planning is to find an optimal policy \(\pi^*\) such that \(v^{\pi^*} \ge v^\pi\) for all other policies \(\pi\). The value function of such a policy, denoted \(v^*\), satisfies the **Bellman optimality equation**, which is expressed using the **Bellman optimality operator**, \(T\):
$$
(Tv)(s) = \max_{a \in A} \left[ r_a(s) + \gamma P_a(s)^\top v \right]
\tag{4}
$$
The existence and properties of this optimal solution are guaranteed by the following central theorem.

> **Theorem 1 (Fundamental Theorem of Dynamic Programming).** For every finite discounted MDP:
> 1.  There exists an optimal policy \(\pi^*\) which is both **deterministic** and **stationary**.
> 2.  The optimal value function \(v^* = v^{\pi^*}\) is the **unique** fixed point of the Bellman optimality operator \(T\), i.e., \(v^* = Tv^*\).
> 3.  Any policy \(\pi_{\text{greedy}}\) that is greedy with respect to \(v^*\) is optimal. That is, if \(\pi_{\text{greedy}}(s) \in \arg\max_{a \in A} \left[ r_a(s) + \gamma P_a(s)^\top v^* \right]\) for all \(s \in S\), then \(v^{\pi_{\text{greedy}}} = v^*\).

This theorem is profound because it reduces the problem of searching over an uncountably large space of policies to the problem of solving a single, non-linear system of equations for the optimal value function \(v^*\). Once \(v^*\) is known, an optimal policy can be extracted by simply acting greedily.

### **Part II: The Value Iteration Algorithm**

#### **3. The Contraction-Mapping Principle**

The solution to the Bellman optimality equation is found by leveraging a key mathematical property of the operator \(T\).

> **Lemma 1 (\(\gamma\)-Contraction).** The Bellman optimality operator \(T\) is a \(\gamma\)-contraction on the space \((\mathbb{R}^{|S|}, \lVert \cdot \rVert_\infty)\), meaning for any two value functions \(u, v \in \mathbb{R}^{|S|}\):
> $$
> \lVert Tu - Tv \rVert_\infty \le \gamma \lVert u - v \rVert_\infty
> \tag{5}
> $$

*Proof.* For any state \(s\), let \(a^*\) be the action that maximizes the expression for \((Tv)(s)\). Then:
$$
\begin{aligned}
(Tv)(s) - (Tu)(s) &= \max_{a} \left[ r_a(s) + \gamma P_a(s)^\top v \right] - \max_{a} \left[ r_a(s) + \gamma P_a(s)^\top u \right] \\
&\le \left[ r_{a^*}(s) + \gamma P_{a^*}^\top v \right] - \left[ r_{a^*}(s) + \gamma P_{a^*}^\top u \right] \\
&= \gamma P_{a^*}^\top (v - u) \le \gamma \sum_{s'} P_{a^*}(s,s') |v(s') - u(s')| \\
&\le \gamma \left( \sum_{s'} P_{a^*}(s,s') \right) \lVert v - u \rVert_\infty = \gamma \lVert v - u \rVert_\infty
\end{aligned}
$$
By swapping \(u\) and \(v\) and taking the maximum over all \(s\), we obtain the result. The same logic shows that the policy operator \(T_\pi\) is also a \(\gamma\)-contraction.

This property allows us to invoke one of the most powerful results in analysis.

> **Theorem 2 (Banach Fixed-Point Theorem).** If \((X, d)\) is a complete metric space and \(F: X \to X\) is a \(c\)-contraction for some \(c \in [0, 1)\), then \(F\) has a unique fixed point \(x^* \in X\). Furthermore, for any initial point \(x_0 \in X\), the sequence of Picard iterates \(x_{k+1} = F(x_k)\) converges geometrically to \(x^*\): \(d(x_k, x^*) \le c^k d(x_0, x^*)\).

Since \((\mathbb{R}^{|S|}, \lVert \cdot \rVert_\infty)\) is a complete metric space and \(T\) is a \(\gamma\)-contraction, the Banach Fixed-Point Theorem directly proves the existence and uniqueness of the optimal value function \(v^*\) and provides a constructive algorithm to find it.

#### **4. The Value Iteration Algorithm and its Convergence**

**Value Iteration (VI)** is precisely the application of Picard iteration to the Bellman optimality operator \(T\). Starting with an arbitrary initial value function \(v_0\) (typically \(v_0 \equiv 0\)), the algorithm iterates:
$$
v_{k+1} = T v_k
\tag{6}
$$From the Banach Fixed-Point Theorem, we have a guarantee of geometric convergence to the unique fixed point \(v^*\):$$
\lVert v_k - v^\* \rVert_\infty \le \gamma^k \lVert v_0 - v^\* \rVert_\infty
\tag{7}
$$Assuming rewards are bounded in \([0, 1]\), we know \(0 \le v^*(s) \le \frac{1}{1-\gamma}\). If we initialize with \(v_0 \equiv 0\), then \(\lVert v_0 - v^* \rVert_\infty = \lVert v^* \rVert_\infty \le \frac{1}{1-\gamma}\). This yields a direct bound on the error after \(k\) iterations:$$
\lVert v_k - v^\* \rVert_\infty \le \frac{\gamma^k}{1 - \gamma}
\tag{8}
$$
This bound demonstrates that the error shrinks by a factor of \(\gamma\) at each step, a fundamental property that underpins all subsequent analysis.

### **Part III: From Approximate Values to Optimal Policies**

Value iteration provides a way to approximate \(v^*\). However, the ultimate goal is to find an optimal *policy*. The following result provides the crucial link between the accuracy of a value function and the quality of its corresponding greedy policy.

#### **5. The Policy-Error Bound**

Let \(v\) be an arbitrary value function, intended as an approximation of \(v^*\). Let \(\pi_g = \Gamma(v)\) be the policy that acts greedily with respect to \(v\), where \(\Gamma\) is the greedy operator:
$$
\Gamma(v)(s) \in \arg\max_{a \in A} \left[ r_a(s) + \gamma P_a(s)^\top v \right]
\tag{9}
$$
The sub-optimality of this policy is bounded as follows.

> **Theorem 3 (Policy-Error Bound).** Let \(v\) be any value function on \(S\), and let \(\pi_g = \Gamma(v)\) be a greedy policy with respect to \(v\). The value of this policy, \(v^{\pi_g}\), satisfies:
> $$
> \lVert v^* - v^{\pi_g} \rVert_\infty \le \frac{2\gamma}{1 - \gamma} \lVert v^* - v \rVert_\infty
> \tag{10}
> $$

This bound, which is known to be tight (Singh & Yee, 1994), shows that the error in the induced policy is proportional to the error in the value function approximation. The factor \(\frac{2\gamma}{1-\gamma}\) dictates how much the value error is amplified. As \(\gamma \to 1\), this factor grows, indicating that a highly accurate value function is needed for near-undiscounted problems.

#### **6. A Practical Planning Algorithm**

We can now combine the convergence guarantee of VI (Eq. 8) with the policy-error bound (Eq. 10) to construct a complete planning algorithm that returns a provably near-optimal policy.

**Objective:** Find a policy \(\pi\) that is \(\varepsilon\)-optimal, i.e., \(\lVert v^* - v^\pi \rVert_\infty \le \varepsilon\).

1.  **Determine Required Value Accuracy:** From the policy-error bound, to ensure \(\lVert v^* - v^{\pi_g} \rVert_\infty \le \varepsilon\), we require a value function \(v\) satisfying:
    $$
    \frac{2\gamma}{1-\gamma} \lVert v^* - v \rVert_\infty \le \varepsilon \quad \implies \quad \lVert v^* - v \rVert_\infty \le \frac{\varepsilon(1-\gamma)}{2\gamma}
    $$

2.  **Determine Required Iterations & Effective Horizon:** We use the VI convergence bound (Eq. 8) to find the number of iterations \(k\) needed to achieve this value accuracy. We must solve for \(k\) in:
    $$
    \frac{\gamma^k}{1-\gamma} \le \frac{\varepsilon(1-\gamma)}{2\gamma} \quad \implies \quad k \ge \frac{\ln \left( \frac{2\gamma}{\varepsilon(1-\gamma)^2} \right)}{-\ln(\gamma)} \approx \frac{\ln \left( \frac{2\gamma}{\varepsilon(1-\gamma)^2} \right)}{1-\gamma}
    $$
    This number of iterations is often related to the **effective horizon** for the problem, which, for a general accuracy target \(\delta\), is \(H_{\gamma,\delta} := \frac{\ln(1/(\delta(1-\gamma)))}{1-\gamma}\). This quantity represents the number of time steps over which rewards significantly influence the total value. Planning to this horizon is approximately equivalent to solving the infinite-horizon discounted problem.

3.  **Develop a Practical Stopping Condition:** Instead of iterating a fixed number of times, it is more efficient to stop when the change between successive iterates becomes small. The residual, \(\lVert v_{k+1} - v_k \rVert_\infty\), is related to the true error \(\lVert v_{k+1} - v^* \rVert_\infty\) by:
    $$
    \lVert v_{k+1} - v_k \rVert_\infty \le \gamma \lVert v_k - v^* \rVert_\infty \quad \text{and} \quad \lVert v_k - v^* \rVert_\infty \le \frac{1}{1-\gamma} \lVert v_{k+1} - v_k \rVert_\infty
    $$
    Combining these, if we stop when the residual \(\lVert v_{k+1} - v_k \rVert_\infty \le \delta\), we can guarantee \(\lVert v_{k+1} - v^* \rVert_\infty \le \frac{\delta}{1-\gamma}\). To achieve the required value accuracy of \(\frac{\varepsilon(1-\gamma)}{2\gamma}\), we must set the residual threshold \(\delta\) to:
    $$
    \delta = \frac{\varepsilon(1-\gamma)^2}{2\gamma}
    $$

4.  **The Complete Algorithm (VI Stop-and-Greedy):**

| **Algorithm 1 — Value Iteration for \(\varepsilon\)-Optimal Planning** |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Input:** MDP \(M=(S,A,P,r,\gamma)\); accuracy target \(\varepsilon > 0\).                                                                                                   |
| **1** Initialize value function \(v \in \mathbb{R}^{|S|}\) (e.g., \(v \gets \mathbf{0}\)).                                                                                      |
| **2** Set stopping threshold \(\delta \gets \frac{\varepsilon(1-\gamma)^2}{2\gamma}\).                                                                                       |
| **3** **repeat** |
| **4**  \(v_{old} \gets v\)                                                                                                                                                     |
| **5**  **for** each state \(s \in S\) **do** |
| **6**   \(v(s) \gets \max_{a \in A} \left[ r_a(s) + \gamma \sum_{s'} P_a(s, s') v_{old}(s') \right]\)                                                                            |
| **7**  **end for** |
| **8** **until** \(\lVert v - v_{old} \rVert_\infty \le \delta\)                                                                                                               |
| **9** **return** greedy policy \(\pi_g = \Gamma(v)\).                                                                                                                        |

### **Part IV: Computational Analysis**

#### **7. Complexity and Optimality of Value Iteration**

* **Per-Iteration Cost:** Each sweep of value iteration (lines 5-7) requires computing \(|S| \times |A|\) state-action values. For a dense (tabular) representation of \(P\), each of these requires an \(O(|S|)\) dot product. This leads to a total per-iteration complexity of \(O(|S|^2|A|)\).
* **Total Runtime:** The total runtime is the product of the per-iteration cost and the number of iterations. This yields a complexity of:
    $$
    T_{\text{VI}}(\varepsilon) = O\left( |S|^2|A| \cdot \frac{1}{1-\gamma} \ln\left(\frac{1}{\varepsilon(1-\gamma)}\right) \right)
    \tag{11}
    $$
* **Memory:** Value iteration is memory-efficient, requiring only storage for two value vectors of size \(|S|\), so its working memory is \(O(|S|)\).
* **Optimality:** A fundamental result by Chen & Wang (2017) establishes an information-theoretic lower bound for any planning algorithm on a tabular MDP: any such algorithm must take \(\Omega(|S|^2|A|)\) time in the worst case. This means Value Iteration is **computationally optimal** up to logarithmic factors and the unavoidable horizon term \(1/(1-\gamma)\).

#### **8. Comparison with Alternative Planning Methods**

Value Iteration is not the only algorithm for solving MDPs. Its main competitors are Policy Iteration and methods based on Linear Programming.

| Criterion              | Value Iteration                       | Policy Iteration                                | LP Methods                               |
| ---------------------- | ------------------------------------- | ----------------------------------------------- | ---------------------------------------- |
| **Per-iteration cost** | \(O(|S|^2|A|)\) (cheap)                 | \(O(|S|^3)\) (policy evaluation solve)             | High (depends on solver, e.g., \(O((|SA|)^3)\)) |
| **Convergence rate** | Geometric (linear)                    | Quadratic (typically very few iterations)       | "One shot" solve                         |
| **Parallelism** | High (state-wise maximization)        | Lower (due to linear system solve)              | Solver dependent                         |
| **Memory** | \(O(|S|)\)                               | \(O(|S|^2)\) (for matrix factorization)            | Large                                    |

**Conclusion:** Value Iteration is often the method of choice when the number of actions \(|A|\) is very large, when memory is a primary constraint, or when an approximate policy is needed quickly. Policy Iteration is often faster in practice when \(|A|\) is small and high-accuracy solutions are required, despite its higher per-iteration cost.

### **Part V: Advanced Topics and Deeper Perspectives**

#### **9. The Linear Programming Formulation**

An entirely different approach to solving MDPs is to formulate the problem as a Linear Program (LP).

The **primal LP** solves for the value function \(v\):
$$
\begin{aligned}
\text{minimize} \quad & \sum_{s \in S} v(s) \\
\text{subject to} \quad & v(s) \ge r_a(s) + \gamma \sum_{s'} P_a(s, s') v(s') \quad \forall s \in S, a \in A
\end{aligned}
\tag{12}
$$
The constraints enforce that \(v\) must be a "dominant" value function, and the objective finds the tightest such function, which is precisely \(v^*\).

The **dual LP** solves for discounted state-action occupancy measures, \(d(s,a)\):
$$
\begin{aligned}
\text{maximize} \quad & \sum_{s,a} d(s,a) r_a(s) \\
\text{subject to} \quad & \sum_{a'} d(s,a') - \gamma \sum_{s',a'} d(s',a') P_{a'}(s', s) = d_0(s) \quad \forall s \in S \\
& d(s,a) \ge 0 \quad \forall s \in S, a \in A
\end{aligned}
\tag{13}
$$
where \(d_0\) is an initial state distribution. Strong duality holds, and the optimal dual variables can be used to recover a deterministic optimal policy. This provides a non-iterative proof of the Fundamental Theorem.

#### **10. The Geometry of the Value Function Polytope**

Recent work (Dadashi et al., 2019) provides a powerful geometric interpretation of the solution space. The set of all achievable value functions, \(\mathcal{V} = \{v^\pi \mid \pi \in \Pi\}\), forms a geometric object called a general polytope.

* The vertices of this polytope correspond to the value functions of deterministic policies.
* **Line Theorem:** If one fixes the policy at all states except for one, say \(s_0\), then as the policy at \(s_0\) is varied, the resulting value function \(v^\pi\) traces a straight line segment in \(\mathbb{R}^{|S|}\).
* This perspective reveals that a Bellman update at a state \(s\) can be seen as jumping to the best endpoint of the corresponding line segment. Value Iteration performs these jumps for all states simultaneously.

#### **11. Algorithmic Variants**

While the synchronous version of VI is the easiest to analyze, several variants are used in practice:

* **Asynchronous VI:** States are not updated all at once. Updates can be performed in any order, as long as every state is updated infinitely often. Convergence is still guaranteed due to the contraction property.
* **Gauss-Seidel VI:** Updates are done in-place within a single sweep, using the most recent value estimates for other states. This often accelerates convergence in practice.
* **Successive Over-Relaxation (SOR):** A relaxation parameter \(\omega\) is used to potentially accelerate convergence: \(v_{k+1} = (1-\omega)v_k + \omega T v_k\).

### **Conclusion**

Value Iteration stands as the canonical algorithm for solving finite, discounted MDPs. Its elegance stems from its direct connection to the **Banach Fixed-Point Theorem**, which guarantees its geometric convergence to the unique optimal value function. The **policy-error bound** provides the critical link that translates this value-function accuracy into a performance guarantee for the resulting greedy policy.

Computationally, its runtime is provably near-optimal for tabular problems, and its simplicity and low memory footprint make it a practical and robust baseline. Advanced perspectives from linear programming and geometry enrich our understanding, confirming its fundamental nature. Together, these properties cement Value Iteration as an indispensable tool in the theory and practice of reinforcement learning.
