---
date: "2025-07-20"
title: "Draft A1. Sequential Decision Processes"
summary: "A1. Sequential Decision Processes"
lastmod: "2025-07-20"
category: "Notes"
series: ["RL Topics", "MARL"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

The way agents' rewards are "coupled," or related to one another, is a fundamental classification criterion in game theory and multi-agent reinforcement learning (MARL). This relationship significantly influences how optimal behavior is defined and how learning algorithms are designed to achieve desired outcomes. The sources describe three primary types of reward coupling: zero-sum games, common-reward games, and general-sum games.

### Zero-Sum Games

In a **zero-sum game**, the sum of the agents' rewards is always zero for any joint action. This implies a direct conflict of interest, where one agent's gain is precisely another agent's loss. For two-agent zero-sum games, this means one agent's reward function is simply the negative of the other agent's reward function.

*   **Example**: The classic Rock-Paper-Scissors game is a zero-sum game, where one agent wins (+1 reward), the other loses (-1 reward), or there's a draw (0 reward to both). Chess and Go are more complex examples with sequential moves.
*   **Solution Concepts**: For two-agent zero-sum games, the concept of a **minimax solution** is defined. In such a solution, each agent uses a policy optimized against a worst-case opponent who aims to minimize that agent's return. A key property is that while there might be more than one minimax solution, all of them yield the same unique expected return (value) for each agent. This uniqueness helps in identifying specific targets for learning.
*   **Welfare and Fairness**: Concepts like social welfare (sum of returns) and fairness (product of returns) are generally not useful in zero-sum games because the total welfare will always be zero, and all minimax solutions will achieve equal welfare and fairness by definition.
*   **MARL Algorithms**: **Minimax Q-learning** is an algorithm specifically designed for two-agent zero-sum stochastic games that computes a minimax solution. It is guaranteed to learn the unique minimax value of the game under certain conditions. Policies learned by minimax Q-learning are robust against worst-case opponents but may not exploit weaknesses in suboptimal opponents. Value iteration for stochastic games also uses minimax values to compute optimal expected returns.

### Common-Reward Games

In a **common-reward game**, all agents receive the exact same reward for any given joint action. This means the agents have a shared objective and are fully cooperative.

*   **Example**: A "coordination" game where agents must select the same action to receive a positive reward is a common-reward game. The level-based foraging task can also be configured as a common-reward game, where all agents receive the same reward for collecting an item, incentivizing collaboration.
*   **Solution Concepts**: For common-reward games, a straightforward definition for a solution is to maximize the expected return received by all agents. Welfare and fairness are maximized if and only if each agent's expected return is maximized, meaning these concepts do not add new criteria for desirability beyond simply maximizing individual returns.
*   **MARL Algorithms**: **Central Q-learning (CQL)** is particularly useful for common-reward games because it can transform the joint reward into a single scalar reward (e.g., `r = r_i` for any agent `i`). When applied with a single-agent RL algorithm guaranteed to find an optimal policy in an MDP, CQL can learn a central policy that is a Pareto-optimal correlated equilibrium, as it maximizes expected returns for all agents simultaneously. This approach circumvents multi-agent issues like non-stationarity and credit assignment by treating the system as a single-agent problem operating on joint actions.

### General-Sum Games

**General-sum games** are the most inclusive category, where there are no specific restrictions on the relationship between the agents' reward functions. This broad definition encompasses scenarios where agents might have mixed motives, being partially cooperative and partially competitive.

*   **Examples**: The Prisoner's Dilemma is a widely studied general-sum game where individual incentives (defecting) lead to a suboptimal outcome for both, illustrating a conflict between individual and collective rationality. The Chicken game and Stag Hunt game are other examples that exhibit multiple equilibria with different expected returns.
*   **Solution Concepts**:
    *   **Nash Equilibrium**: This is a core solution concept for general-sum games, defining a joint policy where no agent can improve its expected return by unilaterally changing its policy, assuming others' policies remain fixed. A game can have multiple Nash equilibria, which may be deterministic or probabilistic, and can yield different returns for agents.
    *   **Correlated Equilibrium**: This concept generalizes Nash equilibrium by allowing for correlation between policies, potentially leading to higher expected returns than Nash equilibria.
    *   **Pareto Optimality**: This criterion helps refine the space of desirable solutions by identifying policies where no agent can be made better off without making another agent worse off.
    *   **Social Welfare and Fairness**: These concepts become highly relevant in general-sum games to select among multiple equilibria. **Welfare optimality** maximizes the sum of agents' expected returns, while **fairness optimality** maximizes the product of their expected returns, promoting equity. Welfare optimality implies Pareto optimality.
    *   **No-Regret**: This alternative solution concept ensures that, in the long run, an agent's average regret for not choosing a different action in the past (given what others did) goes to zero.
*   **MARL Algorithms**: Many foundational MARL algorithms are designed for general-sum games:
    *   **Nash Q-learning** computes a Nash equilibrium solution, though it requires very restrictive assumptions for convergence.
    *   **Correlated Q-learning** aims to compute a correlated equilibrium.
    *   **Policy-based learning methods**, such as Infinitesimal Gradient Ascent (IGA) and Win or Learn Fast (WoLF-IGA, WoLF-PHC), directly optimize policy parameters and can represent probabilistic equilibria, making them suitable for general-sum games that may only have probabilistic Nash equilibria.
    *   **Regret-matching algorithms** (unconditional and conditional) achieve no-regret outcomes, with their empirical action distributions converging to coarse correlated equilibria or correlated equilibria, respectively.

### Applicability Across Game Models

These reward coupling classifications (zero-sum, common-reward, general-sum) are not limited to normal-form games. They extend to more complex sequential models like **stochastic games** and **partially observable stochastic games (POSGs)**, as these models can also specify any of these reward structures. The type of reward coupling significantly impacts the "game" being played within each state of a stochastic game or POSG.

### Impact on MARL Challenges

The nature of reward coupling influences key challenges in MARL:

*   **Environment Non-Stationarity**: While present in single-agent RL, it is exacerbated in MARL because all agents continuously change their policies. This is true regardless of reward coupling, but the dynamics of adaptation differ.
*   **Equilibrium Selection**: This challenge is particularly acute in general-sum games when multiple equilibria exist, and agents may disagree on which one to converge to due to differing individual returns. Refinements like Pareto optimality, social welfare, and fairness are used to address this.
*   **Multi-Agent Credit Assignment**: Determining whose actions contributed to a received reward is a core problem. It is especially prominent in common-reward settings where rewards are indiscriminate across agents, making it difficult for individual agents to disentangle their contributions. Central learning, by acting on joint actions, can circumvent this.

In essence, the coupling of agent rewards dictates the fundamental nature of the multi-agent interaction, from pure competition to pure cooperation, or a mix of both. This, in turn, informs the choice of appropriate solution concepts and influences the design and theoretical convergence properties of MARL algorithms. It's like a symphony: the reward structure is the sheet music, determining whether the instruments play in harmony (common-reward), in a duel (zero-sum), or a complex, evolving interplay (general-sum).


---


In a multi-agent system, an individual agent's payoff is inherently sensitive to the actions and behaviors of the other agents due to the interconnected nature of their interactions. This sensitivity arises from various formal definitions within game models and practical choices made by learning algorithms, significantly impacting how agents learn and coordinate to achieve their objectives.

### Formal Game Models and Payoff Sensitivity

The way a multi-agent environment is formally modeled directly dictates how an agent's payoff is influenced by the rest of the system:

1.  **Normal-Form Games:** In the most basic game model, a normal-form game defines a single interaction where each agent chooses an action, forming a joint action. An agent's reward function, \(\mathcal{R}_i\), maps this joint action \(a = (a_1, \ldots, a_n)\) to a scalar reward \(r_i = \mathcal{R}_i(a)\). This means that agent \(i\)'s payoff is *directly and instantaneously* determined by the actions of all other agents, \(a_{-i}\), alongside its own action \(a_i\).
    *   **Zero-sum games** (e.g., Rock-Paper-Scissors) are a special case where agents' rewards sum to zero, meaning one agent's gain is another's loss, creating a direct competitive payoff dependency.
    *   **Common-reward games** (e.g., a coordination game) mean all agents receive the same reward, aligning their payoffs perfectly with the joint outcome.
    *   **General-sum games** (e.g., Prisoner's Dilemma) have no restrictions, allowing for complex interdependencies where individual incentives may conflict with collective well-being.

2.  **Repeated Normal-Form Games:** By repeating a normal-form game over multiple time steps, policies can become conditioned on the history of past joint actions. This introduces a temporal sensitivity: an agent's current payoff and future prospects depend not just on the current joint action, but on the *sequence* of past actions by all agents, enabling strategies like "Tit-for-Tat". The knowledge of a finite or infinite number of repetitions can lead to "end-game effects," where agents' actions (and thus payoffs) change as the game approaches its conclusion.

3.  **Stochastic Games:** These introduce an environment state that evolves based on joint actions and probabilistic state transitions. An agent's reward function, \(\mathcal{R}_i(s, a, s')\), depends on the current state, joint action, and next state. This means an agent's payoff is sensitive to:
    *   **Collective influence on state:** The joint actions of all agents determine the future state of the environment, which in turn impacts the opportunities for future rewards and thus individual payoffs.
    *   **State-conditioned rewards:** Rewards are tied to specific states and the actions taken within them, making payoffs dependent on the collective progression through the environment.
    *   **Full Observability:** In stochastic games, all agents fully observe the environment state and previous joint actions, making the impact of others' actions clear.

4.  **Partially Observable Stochastic Games (POSGs):** The most general model, POSGs, introduce partial and noisy observations. Agents do not necessarily observe the full environment state or all other agents' actions. This introduces a significant layer of payoff sensitivity:
    *   **Uncertainty:** An agent's current payoff calculation must contend with uncertainty about the true state of the environment and the precise actions taken by other agents, requiring the maintenance of *belief states* (probability distributions over possible states).
    *   **Inferred Actions:** When other agents' actions are unobserved (e.g., private buy/sell actions in a market), an agent's payoff depends on its ability to infer what others are doing based on limited information.
    *   **Limited Views:** Agents with limited vision fields only see a subset of the state and actions, meaning their local payoff calculation is based on incomplete information about the broader system.

### Practical Learning Choices and Their Impact on Payoff Sensitivity

Beyond the formal game definition, the design and implementation of MARL algorithms (practical choices) profoundly affect an agent's payoff sensitivity and its ability to learn and coordinate:

1.  **Knowledge Assumptions:** Game theory often assumes complete knowledge of the game's components (reward functions, transition functions) by all agents. However, in MARL, the standard assumption is that agents *lack* this complete knowledge and must learn it through interaction. This means an agent's payoff achievement becomes sensitive to its ability to *infer* or *model* the unknown elements of the system, including other agents' behaviors and the environment's dynamics.

2.  **Single-Agent RL Reductions:**
    *   **Central Learning (e.g., Central Q-Learning - CQL):** This approach trains a single central policy over the *joint-action space*. An agent's payoff is sensitive to the centralized reward scalarization (e.g., sum of individual rewards for social welfare). While it addresses non-stationarity from an individual agent's perspective, it introduces scalability issues because the joint-action space grows exponentially with the number of agents, making it computationally expensive to find optimal joint policies that maximize individual or collective payoffs.
    *   **Independent Learning (e.g., Independent Q-Learning - IQL):** Each agent learns its policy *independently*, treating other agents' actions as part of the environment's dynamics. An agent's payoff is highly sensitive to the **non-stationarity** caused by other agents concurrently learning and updating their policies. From an individual agent's perspective, the environment appears non-Markovian, which can lead to unstable learning and difficulty converging to a stable, high payoff.

3.  **Foundational MARL Algorithms (Explicitly Modeling Interaction):**
    *   **Joint-Action Learning (JAL):** These algorithms learn joint-action value functions, explicitly estimating returns for joint actions.
        *   **JAL with Game Theory (JAL-GT):** These methods use game-theoretic solution concepts to guide learning.
            *   **Minimax Q-Learning:** Applied in two-agent zero-sum games, it learns a policy optimal against a *worst-case opponent*. An agent's payoff is sensitive to this worst-case assumption, meaning it will learn robust policies that might not exploit weaknesses in a sub-optimal opponent, potentially leading to lower payoffs than possible.
            *   **Nash Q-Learning:** Aims to learn a Nash equilibrium. Convergence is guaranteed only under highly restrictive assumptions (e.g., all games having a global optimum or saddle point). If these assumptions are not met, an agent's ability to achieve an equilibrium payoff is severely hindered, highlighting how specific assumptions about other agents' rationality affect learning outcomes.
            *   **Correlated Q-Learning:** Aims to learn a correlated equilibrium, which can yield higher expected returns. An agent's payoff here is sensitive to the chosen *equilibrium selection mechanism* (e.g., maximizing sum of rewards), which ensures a unique value for updates but has no known formal convergence guarantees for the stochastic game.
        *   **Limitations of JAL-GT:** Joint-action value functions (\(Q_j(s,a)\)) may not carry sufficient information to derive the *correct* equilibrium joint policy, especially for probabilistic equilibria in "turn-taking" games (NoSDE games). This means the learned values, and thus expected payoffs, might not align with the truly optimal policies, making an agent's actual payoff sensitive to this representational limitation.
        *   **JAL with Agent Modeling (JAL-AM):** Instead of making normative assumptions, agents explicitly model other agents' policies based on observed actions. An agent's payoff is thus sensitive to the accuracy and recency of its learned models of other agents.
            *   **Fictitious Play:** Each agent models others' policies as empirical distributions of past actions and chooses a best-response. Payoffs are sensitive to the empirical distributions, which can converge to Nash equilibria in certain game classes.
            *   **Bayesian Learning and Value of Information (VI):** Agents maintain beliefs (probability distributions) over a space of possible models for other agents. VI allows an agent to choose actions that optimally *trade off* immediate rewards with the value of gaining more information about other agents' true policies. This makes an agent's current payoff choice exquisitely sensitive to its *uncertainty* about others and the potential for future information gain that could lead to better long-term payoffs.

    *   **Policy-Based Learning:** These algorithms directly optimize parameterized probabilistic policies using gradient ascent.
        *   **Infinitesimal Gradient Ascent (IGA):** Policies are updated in the direction of the gradient of expected reward. An agent's policy (and thus payoff) is sensitive to the learning dynamics of all agents' gradients, which can lead to divergent or cyclical policy trajectories depending on game parameters. While average rewards may converge to a Nash equilibrium, instantaneous policies and payoffs might not.
        *   **Win or Learn Fast (WoLF):** Modifies learning rates based on whether an agent is "winning" or "losing" compared to an average policy. This makes an agent's policy updates (and thus its trajectory towards a final payoff) directly sensitive to its *relative performance* against the collective average, leading to convergence in cases where IGA would not.

    *   **No-Regret Learning:** These algorithms aim to minimize regret, which is the difference between rewards received and rewards that *could have been received* if a different action (or policy) had been chosen against the *observed actions* of others. An agent's policy (and thus its achieved payoff) is highly sensitive to this "counterfactual" comparison with past observations.
        *   **Unconditional Regret Matching:** Policies assign probabilities proportional to positive average unconditional regrets. The empirical distribution of joint actions converges to coarse correlated equilibria.
        *   **Conditional Regret Matching:** Policies are sensitive to average conditional regrets based on the most recent selected action. The empirical distribution converges to correlated equilibria.
        *   These methods demonstrate that an agent's learning process, and ultimately its average payoff, is shaped by how it processes its "missed opportunities" against the actual behavior of other agents, rather than explicit models of their intentions.

### Implications for Learning and Coordination

The sensitivity of an agent's payoff to the rest of the system carries profound implications for the challenges and goals of MARL:

1.  **Non-Stationarity:** The concurrent learning of multiple agents creates a dynamic environment where the optimal policy for one agent constantly changes as others adapt. This makes learning unstable and complicates convergence guarantees, directly impacting an agent's ability to consistently achieve its optimal payoff. Algorithms must develop strategies to cope with or exploit this dynamic.

2.  **Multi-Agent Credit Assignment:** When rewards are collective, it's challenging for an individual agent to determine its specific contribution to the received payoff. Without properly assigning credit, an agent might reinforce unproductive actions, leading to sub-optimal individual and collective payoffs. Joint-action value functions are a key mechanism to address this, as they explicitly represent the impact of each agent's actions on the joint outcome.

3.  **Equilibrium Selection:** Many games have multiple equilibria, each yielding potentially different expected returns for the agents. The agents face the challenge of implicitly or explicitly coordinating on which equilibrium to converge to, impacting their ultimate payoffs. Learning algorithms often embed assumptions or mechanisms (e.g., maximizing social welfare, risk-dominance) that steer this selection, demonstrating that coordination is critical for achieving mutually beneficial or stable payoffs.

4.  **Scalability:** The exponential growth of the joint-action space (and sometimes state space) with more agents makes it computationally intractable for many algorithms to represent and learn optimal joint policies. This severely limits the ability to compute optimal payoffs in complex multi-agent systems.

5.  **Convergence Guarantees:** MARL algorithms often guarantee weaker forms of convergence than single-agent RL, such as convergence of *average returns* or *empirical distributions* rather than pointwise convergence of policies. This implies that while an agent's long-term average payoff might be good, its instantaneous payoff and policy might still fluctuate significantly, reflecting the ongoing adaptation and interaction with other learning agents. The type of convergence achieved is a direct consequence of how an algorithm handles the interdependencies between agents.

6.  **Trade-offs (e.g., Robustness vs. Exploitation):** The decision of how an agent's payoff should be sensitive to others (e.g., assuming a worst-case opponent as in Minimax Q-Learning vs. attempting to exploit a sub-optimal opponent as Independent Q-Learning might accidentally do) is a critical design choice. The exploration-exploitation dilemma is magnified, as one agent's exploration can inadvertently change the perceived environment for others, influencing their learning and subsequent payoffs.

In essence, an agent's payoff in a multi-agent system is like a note played in a symphony orchestra. Each musician's note (payoff) is profoundly influenced by the notes played by *all* other musicians (the rest of the system). The formal structure of the piece (game model) dictates how these notes combine. Learning algorithms are akin to how musicians practice and adapt: some practice rigidly following a set score (central learning, but what if the score is for an impossibly large orchestra?), some practice ignoring others and hoping for the best (independent learning, leading to cacophony if others aren't fixed), while others continuously listen, model, and adjust their playing based on what they hear from everyone else (agent modeling). The challenges lie in the musicians constantly changing their interpretation (non-stationarity), ensuring individual contributions blend into the collective sound (credit assignment), agreeing on the piece's overall mood and tempo (equilibrium selection), and making sure the entire ensemble sounds harmonious despite individual learning processes and potentially different goals. The choice of learning algorithm determines how sensitively a musician's individual learning process responds to these collective dynamics, ultimately shaping whether their note contributes to a grand, coordinated performance or a chaotic, discordant mess.

























