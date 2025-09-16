---
date: "2025-07-19"
title: "Hierarchy of Game Models"
summary: "Hierarchy of Game Models"
lastmod: "2025-07-19"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### A Practical Guide to the Hierarchy of Game Models

In multi-agent systems, not all interactions are created equal. To model them effectively, game theory provides a hierarchy of frameworks, each building logically on the one before it. This guide walks through the four primary models, showing how each adds a new layer of reality—**time**, **state**, and **hidden information**—to create a progressively more powerful analytical toolkit.

Here is the hierarchy at a glance:

| Model | Core Concept | Adds... | Key Question |
| :--- | :--- | :--- | :--- |
| 1. **Normal-Form Game** | A single, simultaneous choice | *Multiple Agents* | What is the best one-time decision? |
| 2. **Repeated Game** | The same game played over time | *Time & Memory* | How does the past affect future choices? |
| 3. **Stochastic Game** | A game in a dynamic world | *Evolving State* | How do we act when the world changes? |
| 4. **POSG** | A game with imperfect senses | *Hidden Information* | How do we act when we can't see everything? |

---

### 1. Normal-Form (Strategic) Game: The Foundation

The simplest strategic scenario is the **normal-form game**, which captures a single moment of decision. It's the building block for all other models.

* **Core Idea**: A set of players simultaneously choose an action. Once all actions are revealed, the game ends, and each player receives a payoff based on the combination of choices. There is no past and no future—only the present decision.
* **Formal Tuple**: $\langle I, \lbraceA_i\rbrace, \lbraceR_i\rbrace \rangle$
    * $I$: A set of agents (players).
    * $\lbraceA_i\rbrace$: An action set for each agent $i$.
    * $\lbraceR_i\rbrace$: A reward function for each agent $i$, mapping the joint action to a payoff.
* **Example**: Two coffee shops, A and B, simultaneously decide whether to set a `High` or `Low` price for the day. The resulting profit for each depends on both of their choices. This is a classic "matrix game."

---

### 2. Repeated Game: Adding Time and Memory

By taking the static world of a normal-form game and adding the dimension of **time**, we get the **repeated game**.

* **Core Idea**: The same normal-form "stage game" is played over multiple rounds. This introduces **memory**; players can now look back at the history of previous actions and adapt their strategies accordingly.
* **What's New**: This model adds a temporal structure, allowing for the emergence of reputation, threats, and cooperation. The environment itself doesn't change, but the strategic landscape does because of the shared history.
* **Formal Components**: A stage game $G = \langle I, \lbraceA_i\rbrace, \lbraceR_i\rbrace \rangle$ and a horizon $T$. A player's policy $\pi_i(a_i | h_t)$ can now be conditioned on the history of play $h_t$.
* **Example**: Our two coffee shops now set their prices daily. Shop A might adopt a "Tit-for-Tat" strategy: "I'll set a high price today if you did yesterday, but if you set a low price, I'll punish you by setting a low price tomorrow."

---

### 3. Stochastic (Markov) Game: Adding a Dynamic World

While repeated games have a history, the world itself is static. **Stochastic games** introduce a **dynamic environment state** that all players can see.

* **Core Idea**: The world now has an external state (e.g., market conditions, weather) that evolves based on the players' joint actions. The rewards and even the rules of the game can change depending on the current state.
* **What's New**: This model adds a fully observable, Markovian state $S$ and a transition function $T(s' | s, \mathbf{a})$ that governs how the state changes.
* **Formal Tuple**: $\langle I, S, \lbraceA_i\rbrace, T, \lbraceR_i\rbrace, \mu \rangle$
* **Example**: The coffee shops' profits are now affected by the state of the local economy (`Boom`, `Normal`, `Recession`). If both shops set low prices during a `Boom`, the economy might transition to `Normal`. The optimal pricing strategy now depends on the current economic state. A single-agent stochastic game is a standard **Markov Decision Process (MDP)**.

---

### 4. Partially Observable Stochastic Game (POSG): Adding a Veil of Uncertainty

The final step in the hierarchy acknowledges that in the real world, players rarely have perfect information. The **POSG** adds a veil of **hidden information**.

* **Core Idea**: Agents can no longer see the true state of the world. Instead, each receives a private, and possibly noisy, observation. This captures sensor limitations, private knowledge, and communication gaps. Players must act based on a *belief* about the world state.
* **What's New**: The model adds private observation sets $\lbrace\Omega_i\rbrace$ and observation functions $\lbraceO_i\rbrace$. An agent's policy can only depend on its private history of observations, not the true underlying state.
* **Formal Components**: A stochastic game tuple plus $\lbrace\Omega_i\rbrace$ and $\lbraceO_i\rbrace$.
* **Example**: The coffee shop managers don't know the true state of the economy. They only get private observations: Shop A sees its own daily foot traffic (a noisy signal), while Shop B reads supplier reports. They must infer the economic state from these incomplete signals while simultaneously accounting for the other's actions. A single-agent POSG is a **POMDP**.

---

### How to Select the Right Model: A Practical Checklist

Choosing the correct model is the most critical first step in any multi-agent analysis.

1.  **Start Simple**: Always begin with the least complex model and only add complexity if necessary.
2.  **Ask Key Questions in Order**:
    * Is the interaction a **single, one-off decision**? → Use a **Normal-Form Game**.
    * If not, does the interaction repeat but the **environment itself is static**? → Use a **Repeated Game**.
    * If the environment **state evolves and is visible to all**? → Use a **Stochastic Game**.
    * If the environment state is **hidden or perceived imperfectly**? → Use a **POSG**.
3.  **Specify the Reward Structure**: Is the game **zero-sum** (pure competition), **common-reward** (full cooperation), or **general-sum** (a mix)? This tag applies to any of the four models.
4.  **Formalize Your Choice**: By writing down the full tuple for your chosen model (e.g., $\langle I, S, \lbraceA_i\rbrace, ... \rangle$), you force clarity, expose hidden assumptions, and create a reproducible foundation for any subsequent algorithm or simulation.



## What do the agents actually know about the world and about each other?


## What can each agent observe directly, and what must it infer?


## How are the agent's rewards coupled?


## What actions exist, and which of them affect the world versus only convey information?


## When (if ever) does the interaction end?



## How does the state of the environment evolve?



## Who knows that others know what? (common versus asymmetric knowledge)








































