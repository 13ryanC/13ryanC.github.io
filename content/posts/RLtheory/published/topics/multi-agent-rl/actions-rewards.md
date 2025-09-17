---
date: "2025-07-21"
title: "(On-going, read only the first question) A3. Actions and Rewards in Multi-Agent Systems"
summary: "(On-going) A3. Actions and Rewards in Multi-Agent Systems"
lastmod: "2025-07-21"
category: "Notes"
series: ["RL Topics", "MARL"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# 3 Actions and Rewards in Multi-Agent Systems

## 1. What actions exist, and which of them affect the world versus only convey information?

What kinds of action are there, and which of those genuinely change the world as opposed to merely conveying information? This foundational question seeks a systematic distinction within the set of all possible agentive behaviors, separating actions that alter the state of reality from those that merely update beliefs about it. While this inquiry has deep philosophical roots, it has become a critical engineering boundary in designing intelligent agents—from autonomous robots to large language models with tool-using capabilities.

### Mathematical Framework and Key Definitions

Let's formalize this distinction mathematically. Consider an agent operating in an environment with:
- **World state:** \(W \in \mathcal{W}\) (the "ground truth" of reality)
- **Agent's belief state:** \(B \in \mathcal{B}\) (what the agent knows/believes about \(W\))
- **Action space:** \(A = A_{\text{ontic}} \cup A_{\text{epistemic}}\)

**Core Definitions:**

* **Action:** An action \(a\) induces a state transition and yields an observation. We can model this as a function that maps the current world state to a probability distribution over new world states and observations, where \(a: \mathcal{W} \times \mathcal{B} \rightarrow \mathcal{W} \times \mathcal{B}\) that takes the current world state and agent's beliefs as input.

* **Ontic Action:** An action \(a_o \in A_{\text{ontic}}\) where:
  * \(a_o(W, B) = (W', B)\)
  * The world state changes \((W \neq W')\) but the belief state remains unchanged. The action directly modifies reality.
  * \(a_o: \mathcal{W} \rightarrow \mathcal{W}\)
  * For an initial state \(W\), the action results in a new state \(W' = a_o(W)\) where it is possible that \(W' \neq W\). The primary intent is to alter the world state. While an ontic action may also produce an observation that updates beliefs, its defining characteristic is the direct modification of reality.
   
  * Examples: `move_robot(x,y)`, `transfer_money(account_A, account_B, $100)`

* **Epistemic Action:** An action \(a_e \in A_{\text{epistemic}}\) where:
  * \(a_e(W, B) = (W, B')\)
  * The world state remains unchanged but the belief state updates \((B \neq B')\). The action gathers or processes information.
  * \(a_e: \mathcal W \rightarrow \mathcal O\)
  * The action takes the current world state \(W\) and produces an observation \(o \in \mathcal{O}\) that updates the agent's belief state from \(B\) to \(B' = \text{Update}(B, o)\). 
  * Crucially, a purely epistemic action does not change the world state, i.e., \(P(W' \mid W, a_e) = 1\) if \(W'=W\) and \(0\) otherwise.
  * Examples: `sensor_reading()`, `database_query()`, `web_search("weather")`

* **Mixed Action:** An action that affects both states:
  * \(a_m(W, B) = (W', B')\)
  * Both world and beliefs change simultaneously.
  * \(a_m: \mathcal W \rightarrow \mathcal W \times \mathcal O\)
  * The action produces both a state change \((W \rightarrow W')\) and an observation \(o\), leading to a belief update \((B \rightarrow B')\). Most real-world actions fall into this category.
 
In other words, we are asking how to systematically carve up the space of things agents do—and whether each resulting slice primarily pushes matter and reconfigures reality, or merely pushes information and reconfigures minds.

### Why This Distinction is Critical

This is not merely an academic exercise. We build contracts, laws, computer programs, and social conventions upon the implicit assumption that some actions carry tangible force while others merely express content. Misclassifying them has significant consequences across multiple domains:

**Philosophical and Legal Implications**

* **Legal & Institutional Frameworks:** A judge's utterance of a "Guilty" verdict is an ontic act that instantly alters the defendant's legal status, rights, and obligations. In contrast, the evidence presented in court is epistemic; it is intended to inform the verdict but does not, in itself, constitute the legal change.
* **Contract Law:** The act of signing a contract is an ontic action that creates a new set of binding obligations. The preceding negotiations, while crucial, are a series of epistemic acts that align the parties' understanding before the world-altering commitment is made.

**Mathematical Applications in AI Systems**

**1. Planning and Decision Theory**

In classical AI planning, we model this as a state transition system:
- **Ontic actions** modify the state transition function: \(T(s, a_o) = s'\) where \(s \neq s'\)
- **Epistemic actions** update the agent's observation: \(O(s, a_e) = o\) where the agent's belief \(B\) updates via Bayes' rule

In Partially Observable Markov Decision Processes (POMDPs), an agent maintains a belief \(b(s)\) (a probability distribution over states).
- An **ontic action** \(a_o\) changes the state according to the transition function \(P(s'|s, a_o)\).
- A purely **epistemic action** \(a_e\) does not change the state (i.e., \(P(s'|s, a_e) = 1\) if \(s'=s\), 0 otherwise) but yields an observation \(o\) according to a distribution \(P(o|s, a_e)\). The agent's belief \(b\) is updated to \(b'\) using the Bayes filter:
  $$ b'(s') = \eta P(o|s', a_e) \sum_{s \in \mathcal{W}} P(s'|s, a_e)b(s) = \eta P(o|s', a_e)b(s') $$
  where \(\eta\) is a normalizing constant ensuring \(\sum_{s'} b'(s')=1\).

**2. Multi-Agent Systems (Formal Model)**

Consider \(n\) agents with action spaces \(A_i = X_i \times M_i\) where:
- \(X_i\): ontic actions (affect environment state \(S\))
- \(M_i\): epistemic/communication actions (affect other agents' beliefs)

The system dynamics become:
\(S_{t+1} = f(S_t, \mathbf{X}_t)\)
\(B_i^{t+1} = g_i(B_i^t, O_i^{t+1}, \mathbf M_t)\)

Where \(\mathbf X_t = (X_1^t, ..., X_n^t)\) are all ontic actions, \(\mathbf{M}_t\) are all messages, \(f\) is the environment's state transition function, and \(g_i\) is the belief update function for agent \(i\), which processes its latest observation \(O_i^{t+1}\) and incoming messages.

**3. Information-Theoretic Perspective**

An epistemic action \(a_e\) can be evaluated by its **information gain**:
\(IG(a_e) = H(W) - H(W|O_{a_e})\)
where \(H(W)\) is the entropy of the agent's current world model, and \(H(W|O_{a_e})\) is the entropy after observing the outcome of action \(a_e\).

An ontic action \(a_o\) can be evaluated by its **utility change**:
\(U(a_o) = u(W') - u(W)\)
where \(u(\cdot)\) is the agent's utility function over world states.

The central tension arises from actions that appear to be purely informational but have definite world-altering force. Physically flipping a light switch is unambiguously ontic; silently counting sheep in one's head is purely epistemic. But uttering the words, "I now pronounce you married," under the right conditions, fundamentally transforms the social and legal reality of two individuals—highlighting the complexity of the boundary.

### Simplified Theoretical Frameworks

Rather than diving deep into philosophical jargon, let's present the key frameworks with their mathematical essence:

| Framework | Mathematical Model | Simple Explanation | AI Application |
|-----------|-------------------|-------------------|----------------|
| **Speech-Act Theory** | Actions have three components:<br>• Content: \(c\) (what is said)<br>• Force: \(f\) (what kind of act)<br>• Effect: \(e\) (what happens) | Some utterances just inform (\(f\) = assertive), others change the world (\(f\) = declarative) | NLU systems must classify user intent:<br>`"What's the weather?"` → epistemic<br>`"Set alarm for 8am"` → ontic |
| **Direction-of-Fit** | • Word→World Fit: Update belief \(B\) to minimize divergence from world \(W\), e.g., \(\min_B D_{KL}(P_W \| P_B)\).<br>• World→Word Fit: Choose action \(a\) to change world \(W\) to \(W'\) to minimize distance to goal \(G\), e.g., \(\min_a \mathbb{E}[d(W', G)]\). | Either make your beliefs match reality, or make reality match your goals. | Sensor fusion (beliefs ← reality) vs. motor control (reality ← goals). |
| **Information Theory** | Epistemic value: \(IG(a_e) = H(W) - H(W \mid O_{a_e})\)<br>Pragmatic value: \(\Delta U(a_o) = u(W') - u(W)\) | Information actions reduce uncertainty; pragmatic actions increase utility. | Active learning (explore for info) vs. exploitation (act for reward). |
| **State Transition Model** | Ontic: \(P(s' \mid s, a) > 0\) for \(s' \neq s\)<br>Epistemic: \(P(s' \mid s,a) = \delta(s'-s)\) (state is invariant) but observation model \(P(o \mid s,a)\) is informative. | Some actions change the world state; others only reveal information about it. | POMDP planning: deciding when to sense vs. when to act. |


These frameworks broadly agree that at least two fundamental families of action exist, but they differ in how they handle grey areas, particularly performatives, mixed actions, and indirect effects.

### The Core Challenge: When Actions Don't Fit Neatly

The mathematical framework above assumes clean separation, but reality is messier. Here are the key complications:

**1. Cascading Effects (Indirect Ontic Actions)**

**Problem:** An epistemic action can trigger ontic consequences through other agents.

**Mathematical Model:** 
- Agent 1 performs epistemic action \(a_1^e\), updating its belief \(B_1 \rightarrow B_1'\) and perhaps sending a message \(m\).
- Agent 2 receives \(m\), updates its belief \(B_2 \rightarrow B_2'\), and chooses an ontic action \(a_2^o\) based on this new belief.
- Agent 2's action causes the world state to change: \(W \xrightarrow{a_2^o} W'\).
- Net effect: \(a_1\) indirectly caused \(W \rightarrow W'\)

**Example:** A news article (epistemic) causes stock prices to crash (ontic effect via market participants).

**2. Institutional Context (Permission-Dependent Actions)**

**Problem:** The same utterance can be ontic or epistemic depending on authority.

**Mathematical Model:** 
$\text{effect}(a, \text{context}) = \begin{cases} 
\text{ontic} & \text{if } \text{authorized}(\text{agent}, \text{context}) = \text{True} \newline
\text{epistemic} & \text{otherwise}
\end{cases}$

**Example:** "You're fired" has ontic force only when spoken by an authorized manager.

**3. Interleaved Sequences (Tightly Coupled Actions)**

**Problem:** High-level tasks require rapid switching between action types.

**Mathematical Model:** A compound action \(A_{\text{compound}} = \langle a_1, a_2, ..., a_n \rangle\) where each \(a_i\) can be ontic or epistemic, and later actions depend on earlier results:

\(\pi: \mathcal{B} \rightarrow A\), where \(\mathcal B\) is the agent's belief state and \(\pi\) is the policy.

\(a_{i} = \pi(B_i)\), where \(B_{i} = \text{Update}(B_{i-1}, \text{outcome}(a_{i-1}))\)

**Example:** "Find the author of Dune and add them to contacts" requires:
1. `search("Dune author")` → epistemic
2. Parse result: "Frank Herbert" → internal processing  
3. `create_contact("Frank Herbert")` → ontic

### Practical Implementation: Design Principles with Formal Guarantees

#### **1. Causal Proximity Principle**

**Rule:** An action is ontic only if it directly modifies state variables within a single transaction/time step.

**Formal Definition:** 
$$
\text{ontic}(a) \iff \exists s, s': s \neq s' \land P(s'|s,a) > 0 \land d(s,a,s') = 1
$$

where \(d(s,a,s')\) is the causal path length in the system's state transition graph. A distance of 1 implies a direct effect defined by the system's transition function \(T(s,a)\). We can see that when d = 1, then it is direct; if it is not equal to 1 then it is indirect.

In other words, it states that an action \(a\) is **ontic** if and only if there is at least one scenario where:

1. The action causes a change (the new state is different from the old one).
2. This change is a possible outcome of the action.
3. The change is **direct and immediate** (the causal path length is 1), not a downstream consequence.

#### **2. Permission-Based Access Control**

**Rule:** Ontic actions require explicit authorization; epistemic actions are generally permissible.

**Formal Definition:**
$$
\text{allow}(a, \text{agent}) = \begin{cases}
\text{requires\_auth}(a) & \text{if ontic}(a) \newline
\text{True} & \text{if epistemic}(a)
\end{cases}
$$

This function, \(\text{allow}(a, \text{agent})\), determines whether a specific **agent** (a user, system, or process) is permitted to perform a given action, a. The outcome depends entirely on the classification of the action.

Case 1: \(\text{if ontic} (a)\):

This condition applies if the action \(a\) is ontic. An ontic action is one that changes the state of the system (e.g., writing data, deleting a file, modifying a setting).

If the action is ontic, permission is **not** automatically granted. Instead, the \(\text{allow}\) function delegates the decision to another function or process, \(\text{requires_auth}(a)\). This secondary check is responsible for verifying if the specific agent has the explicit credentials, rights, or permissions necessary for that particular state-changing action. The final decision (True/False) comes from this deeper authorization check.

Case 2: \(\text{if epistemic} (a)\):

This condition applies if the action a is epistemic. An epistemic action is one that only observes the state of the system without changing it (e.g., reading data, checking a status, viewing a log). It's about gaining knowledge.

If the action is purely informational, permission is granted by default. The value `True` signifies that epistemic actions are considered generally permissible and do not require a special, fine-grained authorization check.

**Some Ideas of implementation:** 
- Read operations (epistemic): minimal authentication
- Write operations (ontic): strong authentication + confirmation
- Mixed operations: decompose and apply appropriate controls

#### **3. Reversibility and Logging**

**Rule:** Log all actions with sufficient information for debugging and potential rollback.

**Formal Model:**

Let's define the state of the system at any time \(t\) as \(S_t\), such that the two types of actions are as follows:

- **Epistemic Actions (\(A_E\))**: This is an observational function. It takes the current state \(S_t\) as input and produces some data as output, but it does not change the state.
$$
A_E (S_t) \rightarrow \text{data}
$$
where \(S_{t+1} = S_t\).

- **Ontic Actions (\(A_O\))**: This is a transformational function. It takes the current state \(S_t\) and maps it to a new state \(S_{t+1}\).
$$
A_O (S_t) \rightarrow S_{t+1}, \quad  \text{where } S_{t+1} \neq S_t
$$

The primary goal of the logging rule is to enable potential **rollback**, which is equivalent to **inverting a function**.

To reverse the ontic action \(A_O\) that caused the transition from \(S_t\) to \(S_{t+1}\), one must be able to apply an inverse action, let's call it \(A_O^{-1}\), such that:
$$A_O^{-1}(S_{t+1}) = S_t$$

The critical insight here is that you often **cannot construct the inverse function \(A_O^{-1}\) from the output state \(S_{t+1}\) alone**. You need more information. The formal model's logging policy is designed to capture exactly this necessary information.

* **Logging Ontic Actions**: The policy states you must store the "full before/after state diff." This difference, let's call it \(\Delta S\), represents the change between the states.
    $$\Delta S = \text{diff}(S_t, S_{t+1})$$
    By logging the "before" state (\(S_t\)) and "after" state (\(S_{t+1}\)), you are explicitly storing all the information needed for reversal. The rollback operation is no longer a complex calculation but a simple **state replacement**: replace the current state \(S_{t+1}\) with the logged "before" state \(S_t\). This is the most robust, though expensive, way to guarantee reversibility.

* **Logging Epistemic Actions**: Since epistemic actions don't change the state (\(S_{t+1} = S_t\)), there is no state transition to reverse. The concept of an inverse action is not applicable. Therefore, the log only needs to record the query itself and a timestamp for the purpose of **auditing**—answering "What was asked, and when?"

**Implementation:**
```python
def log_action(action, action_type, state_before=None, state_after=None):
    if action_type == "epistemic":
        log.info(f"Query: {action.query}, Result: {action.result}")
    elif action_type == "ontic":
        log.critical(f"State change: {state_before} → {state_after}")
```

In other words:

- For ontic actions, the log captures the complete `(state_before, state_after)` pair. This pair is the essential information required to define and execute an inverse transformation, making the system's history reversible.

- For epistemic actions, no state change occurs, so the log only needs to capture the details of the observation itself for auditing purposes.


#### **4. Decision-Theoretic Action Selection**

**Problem:** How should an agent decide between acting on its current knowledge versus gathering more information first? This is the classic "explore vs. exploit" dilemma.

**Formal Method:** The solution is to use the **Value of Information (VoI)** framework from decision theory. VoI quantifies the benefit of reducing uncertainty *before* making a commitment. It answers the question: "By how much will the value of my best choice improve, on average, if I gather more information?"

**The Value of Information (VoI) Formula**

Conceptually, VoI is the difference between the best you could do with new information and the best you can do now.

$$
\text{VoI}(a_{\text{epistemic}}) = \mathbb E [\max_{a_{\text{ontic}}} u(a_{\text{ontic}} \mid B')] - \max_{a_{\text{ontic}}} u(a_{\text{ontic}} \mid B)
$$

Let's break this down:

* **\(\max_{a_{\text{ontic}}} u(a_{\text{ontic}} \mid B)\)**: This is your **baseline**. It's the maximum utility (\(u\)) you can get by choosing the best state-changing (**ontic**) action, given only your current knowledge or belief state (\(B\)). This is the value of your best choice if you **act now**.

* **\(\mathbb E [\max_{a_{\text{ontic}}} u(a_{\text{ontic}} \mid B')]\)**: This is your **potential**. It’s the *expected* maximum utility you could get after performing an information-gathering (**epistemic**) action. This action updates your belief state to a new, better-informed state, \(B'\). Since the outcome of gathering information is uncertain, the formula takes the **expected value** (\(\mathbb E\)) over all possibilities.

**Computational Breakdown**

To calculate the expected value precisely, the VoI formula is expanded into a weighted sum over all possible outcomes of the information-gathering action (\(a_e\)).

$$
\text{VoI}(a_e) = \left( \sum_{o \in \mathcal O} P(o \mid B, a_e) \max_{a_o'} \mathbb E [u(s') \mid B_o', a_o'] \right) - \max_{a_o} \mathbb E [u(s') \mid B, a_o]
$$

Here, we are summing over every possible **observation** (\(o\)) we could make. Each term in the sum consists of:

1.  **\(P(o \mid B, a_e)\)**: The **probability** of seeing a specific observation '\(o\)', which acts as a weight.
2.  **\(\max_{a_o'} \mathbb E [u(s') \mid B_o', a_o']\)**: The maximum utility of the **new best action** (\(a_o'\)) you would choose, given your newly updated posterior belief (\(B_o'\)).


**The Unified Decision Rule**

The VoI is used to create a unified rule for choosing the single best action, \(a^\ast\), from all available options (both epistemic and ontic). The agent picks the action that maximizes its **total net value**.

$$
a^\ast = \arg\max_{a \in A} \left( \text{TotalNetValue}(a) \right)
$$

The calculation for total net value depends on the action's type:

* **Epistemic Actions (Info-Gathering)**
    An epistemic action's value is purely informational. Its net value is its VoI minus the cost to perform it.
    $$
    \text{TotalNetValue}(a_e) = \text{VoI}(a_e) - \text{cost}(a_e)
    $$
    It's worth gathering information if this value is positive and higher than the value of acting now.

* **Ontic Actions (State-Changing)**
    An ontic action provides no informational value for future decisions, so as proven previously, its **VoI is 0**. Its value is entirely **direct**—the utility of its own outcome.
    $$
    \text{TotalNetValue}(a_o) = \mathbb E [u|B, a_o] - \text{cost}(a_o)
    $$

Ultimately, the agent calculates the total net value for every available action and chooses the one with the highest score. If an ontic action wins, it's because its direct expected utility was greater than the net informational gain offered by any epistemic alternative.

### Open Research Questions

#### **1. Optimal Information-Action Policies**

**Problem:** How should an agent strategically balance taking actions that yield immediate rewards (ontic) versus actions that gather information for better future decisions (epistemic), especially over a long period?

**Formal Method:** This long-term "explore vs. exploit" problem is formalized by finding an optimal **policy** (\(\pi\)) that maximizes a cumulative, time-discounted objective function, \(J(\pi)\). This approach is central to fields like Bayesian Reinforcement Learning and Active Inference.

**The Objective: Maximizing Long-Term Value**

The goal is to find a policy \(\pi\) that maximizes the total expected value, \(J(\pi)\), accumulated over a time horizon \(T\).

$$J(\pi) = \mathbb E \left[\sum_{t=0}^T \gamma^t \left(\alpha \cdot U_{\text{ontic}}(a_t) + (1-\alpha) \cdot IG_{\text{epistemic}}(a_t)\right)\right]$$

A **policy** \(\pi: (B_t, W_t) \rightarrow A\) is simply a strategy that maps the agent's current situation (its belief state \(B_t\) and world state \(W_t\)) to an action \(a_t\). The formula finds the best possible strategy.

**The Core Components**

* **\(\mathbb E [\dots]\)**: The **Expected Value**, which handles uncertainty. The policy must maximize the value it gets *on average* across all possible random futures.
* **\(\sum_{t=0}^T\)**: The **Sum Over Time**, which directs the agent to maximize its *cumulative* reward over the long term, not just the next immediate gain.
* **\(\gamma^t\)**: The **Discount Factor** (where \(0 \le \gamma \le 1\)). This makes rewards received sooner more valuable than those received later, modeling a preference for near-term gains and ensuring the total sum is well-behaved.

**The Instantaneous Reward: The Explore-Exploit Trade-off**

The heart of the formula is the reward received at each time step \(t\), which explicitly balances two competing drives:

$$\alpha \cdot U_{\text{ontic}}(a_t) + (1-\alpha) \cdot IG_{\text{epistemic}}(a_t)$$

* **\(\alpha\)**: The **Trade-off Parameter**. This is a weight (from 0 to 1) that sets the agent's priorities. A high \(\alpha\) creates a pure "exploiter" that only seeks immediate utility, while a low \(\alpha\) creates a pure "explorer" that only seeks information.
* **\(U_{\text{ontic}}(a_t)\)**: The **Ontic Utility**. This is the direct, tangible reward from an "exploit" action that changes the world. If the action is epistemic, this value is zero.
* **\(IG_{\text{epistemic}}(a_t)\)**: The **Information Gain**. This is the value derived from an "explore" action that reduces the agent's uncertainty about the world. If the action is ontic, this value is zero.

This defines an optimal strategy as one that intelligently chooses actions to balance immediate rewards with long-term learning. At each step, the agent decides whether to cash in on its current knowledge for a guaranteed utility (\(U_{\text{ontic}}\)) or to invest in gathering information (\(IG_{\text{emic}}\)) that will enable better, more valuable decisions later. This dynamic balancing act is fundamental to creating agents that can learn and thrive in complex, uncertain environments.

---

#### **2. Multi-Agent Communication Emergence**

**Problem:** How do independent agents, without a pre-shared dictionary, develop a common language of signals to coordinate their actions and share knowledge?

**Formal Method:** This is addressed by modeling communication not as the transfer of fixed data, but as a process of aligning probabilistic beliefs about actions. Success is achieved when agents converge on a shared interpretation of signals, a process typically studied using game theory or multi-agent reinforcement learning.

**The Mathematical Setup: Meaning as Aligned Beliefs**

The "meaning" of a signal is defined by the actions it inspires. The framework involves a sender and a receiver.

* **The Sender (\(i\)):** Transmits a message \(m\). The sender's *intended meaning* is represented by a probability distribution over the receiver's possible actions: \(P_i^{intended}(a_{ontic} | m)\). This is what the sender *wants* the receiver to do upon getting the message.

* **The Receiver (\(j\)):** Interprets message \(m\) by forming its own probability distribution over its actions: \(P_j(a_{ontic} | m)\). This represents what the receiver *thinks* the message means.

* **Successful Communication:** Communication succeeds when the receiver's interpretation matches the sender's intention. The goal is for their probability distributions to converge.
    $$
    P_j(a_{ontic} | m) \approx P_i^{intended}(a_{ontic} | m)
    $$

**The Core Research Question: How Does Alignment Happen?**

The central question is: under what conditions do these individually-held beliefs align into a shared, effective communication protocol? This is explored through two primary approaches.

**1. Game-Theoretic Conditions (e.g., Signaling Games)**
This approach models agents as rational players aiming to maximize a shared **payoff**.
* **Mechanism:** A common language emerges when agents find a **Nash Equilibrium**. At this point, no agent can improve its own payoff by unilaterally changing its signaling or interpretation strategy. The mutual need to cooperate for a reward incentivizes their beliefs to align.

**2. Learning-Based Conditions (e.g., MARL)**
This approach uses Multi-Agent Reinforcement Learning, where agents independently learn through trial and error to maximize their own long-term rewards.
* **Mechanism:** A shared language **emerges** as an instrumental strategy. If using a signal in a certain way helps the agents complete a task and receive a reward, that communicative behavior is **reinforced**. The agents' internal models naturally adjust to make their signals more effective, causing their belief distributions to converge over time as a means to an end.

---

#### **3. Responsibility Attribution in Cascading Systems**

**Problem:** In a complex system, if Agent A provides information (an epistemic action) that causes Agent B to perform a physical action (an ontic action) with harmful consequences, how do we fairly assign responsibility to Agent A?

**Formal Method:** Responsibility is quantified using a framework that combines the agent's objective causal impact on the outcome with its subjective ability to have foreseen that outcome. This approach separates what factually happened from what the agent knew or believed would happen.

**The Core Principle: Responsibility = Cause × Foresight**

The proposed framework defines responsibility as the product of two key factors. An agent is considered highly responsible only when both its causal contribution and its ability to foresee the harm were high.

$$\text{Responsibility}(A) = \text{CausalEffect}(A, \text{harm}) \times \text{Foreseeability}(A, \text{harm})$$

**Component 1: Causal Effect (The Objective Factor)**

This term quantifies the agent's actual, factual impact on the outcome. It answers the question: "To what extent did Agent A's action increase the probability of the harm?"

$$\text{CausalEffect}(A, \text{harm}) = P(\text{harm} | do(a_A)) - P(\text{harm} | do(\neg a_A))$$

This formula uses the **`do`-calculus** from causal inference to distinguish causation from mere correlation. It compares two parallel worlds:
1.  **\(P(\text{harm} | do(a_A))\)**: The probability of harm if we **intervene** and force Agent A to perform its action.
2.  **\(P(\text{harm} | do(\neg a_A))\)**: The probability of harm if we **intervene** and prevent Agent A from acting (the counterfactual).

The difference between these two is the net increase in risk that is causally attributable to Agent A's action.

**Component 2: Foreseeability (The Subjective Factor)**

This term captures the agent's state of mind, addressing the question: "From Agent A's own perspective, how likely was the harmful outcome?"

$$\text{Foreseeability}(A, \text{harm}) = P_A(\text{harm} | a_A)$$

The critical element is the subscript in **\(P_A\)**, which signifies that we are using Agent A's **subjective belief model**. This is not the objective truth, but what the agent believed to be true based on its own internal data and knowledge. This captures the legal and ethical concept of *mens rea*—whether the agent was aware of the potential for harm.

**Synthesis and Example**

This framework provides a nuanced measure of responsibility. Consider a mapping service (Agent A) giving a route to a self-driving truck (Agent B), where the harm is crashing off a collapsed bridge.

* **High Responsibility:** Agent A's map shows the bridge is out, but it sends the route anyway.
    * `Causal Effect` is high (the route caused the crash).
    * `Foreseeability` is high (A's own data showed the danger).
    * **Result:** `High × High = High Responsibility`.

* **Low Responsibility (No Foreseeability):** Agent A's map is outdated and shows the bridge is safe. It sends the route in good faith.
    * `Causal Effect` is high.
    * `Foreseeability` is low (A had no reason to expect harm).
    * **Result:** `High × Low = Low Responsibility`.
 
---

### Concluding Remarks

The ontic/epistemic distinction provides both conceptual clarity and practical guidance for AI systems. The mathematical frameworks above offer:

1. **Formal definitions** that can be implemented in code
2. **Design principles** with measurable guarantees  
3. **Decision procedures** for autonomous agents
4. **Open problems** for future research

As AI systems become more sophisticated, this distinction becomes essential for building agents that are not only intelligent, but safe, accountable, and aligned with human values. The boundary between knowing and doing is not just philosophical—it's the foundation for responsible AI.

---

## 2 How are the agent's rewards coupled?

Coupling refers to the degree to which an agent's reward is dependent on the joint state or actions or multiple agents. Formally in a Markov (stochastic) game, the reward function for agent \(i\), \(r_i (s, a)\), is coupled if it cannot be expressed cleanly in terms agent \(i\)'s own local state / action. Many multi-agent problems, like traffic control, games, markets, exhibit such inter-dependence, meaning that agents learn in a strategic rather than a single agent setting.

Understanding reward coupling is crucial in designing learning algorithms that achieve cooperation, competition and to braoder debates in AI alignment and mechanism design (aka any engineering scaffolding).

In other words, we are asking:
> How do different formal and practical choices make one agent's payoff sensitive to what the rest of the system does, and what does that imply for learning and coordination?


This question is important since coupled rewards is the heart of social dilemmas (i.e., tragedy of the commons), credit-assignment problems, and emergent behaviours that very easily single-agent RL ignores.

Getting the coupling wrong can lead to undesirable ooutcomes in problem solving.

In a two‑player matrix game, coupling is the off‑diagonal dependence of each payoff on the opponent’s move; we already know this gives rise to equilibria and dilemmas. Multi‑agent RL is the high‑dimensional, dynamic generalisation.


We need rich coupling to capture real‑world interdependence, yet excessive coupling makes learning unstable and masks individual contributions.


The way agents’ reward functions relate—zero‑sum (pure competition), common‑reward (pure cooperation), or general‑sum (mixed motives)—fundamentally determines the appropriate solution concepts (minimax, welfare‑maximizing, Nash/correlated, etc.) and drives the design of MARL algorithms.

**Zero-Sum Games**
Because one agent’s gain equals another’s loss, a unique minimax value exists; algorithms like Minimax Q‑learning target robustness against worst‑case opponents rather than exploitation of sub‑optimal ones.

**Common‑Reward Games**
Identical rewards align all incentives, letting Central Q‑learning treat the multi‑agent system as a single MDP; this removes non‑stationarity at the cost of exponential joint‑action spaces and centralized credit assignment.

**General‑Sum Games**
With partially aligned incentives, equilibria are many and non‑unique; extra criteria (social welfare, fairness, Pareto optimality) guide selection. Algorithm families include Nash‑Q, correlated‑Q, policy‑gradient (IGA, WoLF), and regret matching, each trading off convergence guarantees, scalability, and exploitability.


**Formal Models → Payoff Sensitivity**
Moving from normal‑form → repeated → stochastic → partially observable stochastic games adds layers (history, state dynamics, uncertainty) that magnify how strongly an agent’s payoff depends on others’ actions and information.

**Learning-Algorithm Choice**
Practical design (central vs. independent vs. joint‑action vs. agent‑modeling vs. policy‑gradient vs. no‑regret) is itself a specification of how much opponent behaviour is modeled, hence how non‑stationarity, scalability, and convergence trade‑offs manifest.


**MARL Challenges**
Three persistent hurdles—environment non‑stationarity, credit assignment, and equilibrium selection—are each exacerbated or mitigated by the chosen reward coupling and algorithmic approach; scalability and robustness‑vs‑exploitation are recurring secondary trade‑offs.

**General Principle**
Reward structure acts like the score of a symphony: it dictates whether agents play in harmony, duel, or negotiate, and thus governs every downstream design and theoretical property of multi‑agent learning.


Below I decompose the question into five sub‑questions, solve each with citations, and at the end collect the practical design take‑aways.

---

### 1  What do we mean by “payoff sensitivity” and how can we measure it formally?

Let

$$
u_i(a_i,\;a_{-i},\;s)\quad i\in\{1,\dots ,n\}
$$

be the (possibly stochastic) utility of agent \(i\), where \(a_i\) is its own action, \(a_{-i}\) the joint actions of the rest of the system, and \(s\) an environment state.  A minimal quantitative notion of **sensitivity** is the partial derivative (or discrete difference)

$$
\frac{\partial u_i}{\partial a_j}\neq 0\qquad(j\neq i),
$$

or, for policy parameters \(\theta_j\), the influence term

$$
\frac{\partial u_i}{\partial\theta_j}=\sum_{a_j}\frac{\partial u_i}{\partial a_j}\frac{\partial a_j}{\partial\theta_j}.
$$

* **Zero sensitivity** (\(\partial u_i/\partial a_j=0\)): fully independent tasks; multi‑agent learning reduces to \(n\) single‑agent problems.
* **Weak/linear sensitivity**: additive externalities as in *potential games*, where one scalar potential \(Φ(a)\) satisfies \(u_i(a)-u_i(a_i',a_{-i})=Φ(a)-Φ(a_i',a_{-i})\). This guarantees convergence of a wide class of best‑response or gradient dynamics. ([arXiv][1])
* **Sign‑structured sensitivity**:
  *Strategic complements* (\(\partial^2 u_i/\partial a_i\partial a_j>0\)) versus *substitutes* (\(<0\)). Complements create positive feedback and multiple equilibria; substitutes push toward unique equilibria and competition. ([Wikipedia][2])

Sensitivity therefore spans a spectrum that you, as the system designer, can tune by editing \(u_i\) or by introducing intermediate “proxy” rewards.

---

### 2  Which **formal modelling choices** control this sensitivity?

| Formal lever                                                        | Effect on \(\partial u_i/\partial a_{-i}\)                                                                                                                              | Example                                                                                                |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Reward aggregation** (team‑reward, individual, difference‑reward) | Team reward sets \(\partial u_i/\partial a_j > 0\;\forall j\); difference reward \(D_i=G−G(a_i←0)\) removes most cross terms, lowering sensitivity. ([NeurIPS Papers][3]) | Counterfactual Multi‑Agent Policy Gradients (COMA)                                                     |
| **Game class** (zero‑sum vs common‑interest vs general‑sum)         | Zero‑sum maximises negative sensitivity, common‑interest maximises positive sensitivity.                                                                              | StarCraft micromanagement tasks in COMA ([arXiv][4])                                                   |
| **Network topology** (who interacts with whom)                      | Local neighbour list restricts which \(a_j\) appear in \(u_i\).                                                                                                           | Network games with complements ([Stanford University][5])                                              |
| **Information structure** (observability, signalling)               | Hidden actions amplify perceived stochasticity of \(\partial u_i/\partial a_j\).                                                                                        | Global reward with partial observability ➜ credit‑assignment burden                                    |
| **Update schedule** (simultaneous vs sequential vs multi‑timescale) | Sequential updates temporarily set \(\dot a_{-i}=0\), reducing non‑stationarity.                                                                                        | Multi‑timescale learning converges faster than fully sequential while avoiding divergence ([arXiv][6]) |

---

### 3  Which **practical engineering choices** amplify or damp sensitivity?

1. **Centralised critic, decentralised actors (CCDA)** – COMA uses a critic that knows all actions and computes a *counterfactual baseline* \(\hat u_i(a_i,a_{-i}) - \hat u_i(a_i',a_{-i})\), subtracting most cross‑agent variance and making gradients for each agent depend only on its *marginal* impact. ([cs.ox.ac.uk][7])
2. **Opponent‑aware gradients (LOLA / COLA)** – explicitly differentiate an agent’s expected future payoff through *the other agents’ learning step* \(\tfrac{\partial u_i}{\partial\theta_j}\tfrac{d\theta_j}{dt}\). This actively shapes sensitivity to steer joint learning toward cooperative equilibria. ([arXiv][8], [arXiv][9])
3. **Difference or shaped rewards** – replace global reward \(G\) by \(D_i\) or exponentially‑weighted advantage estimators to lower gradient variance without biasing fixed points. ([Proceedings of Machine Learning Research][10])
4. **Multi‑timescale or asynchronous learning** – give each agent a distinct step‑size \(\alpha_i\). Fast learners see the rest of the system as quasi‑stationary, restoring single‑agent‑like stability. ([arXiv][6])

---

### 4  How does payoff sensitivity manifest during **learning**?

| Symptom                                                                              | Root cause                                               | Mitigation                                                            |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------- | --------------------------------------------------------------------- |
| **Non‑stationarity** – the transition kernel changes as others learn. ([Reddit][11]) | Large \(\partial u_i/\partial\theta_{-i}\)                 | Centralised critics; multi‑timescale; opponent modelling              |
| **High‑variance gradients**                                                          | Unobserved actions enter \(u_i\)                           | Counterfactual baselines; difference rewards                          |
| **Lazy‑agent or free‑rider problem**                                                 | Positive complements but global reward only              | Individually scaled \(D_i\); explicit communication channel             |
| **Failure to converge (cycling)**                                                    | Strong strategic substitutes with simultaneous Q‑updates | Sequential or potential‑game projection; establish imitation dynamics |

When formal payoffs satisfy the potential‑game property, best‑response or gradient descent is a *Lyapunov* process and convergence is guaranteed even with myopic learners. ([arXiv][1]) Otherwise, learning must compensate through the techniques above.

---

### 5  What does sensitivity imply for **coordination mechanisms**?

1. **Equilibrium multiplicity vs uniqueness**

   * Complements ⇒ multiple Nash equilibria; selection requires focal points, symmetry‑breaking signals, or social conventions. ([ScienceDirect][12])
   * Substitutes often yield a unique equilibrium but at lower joint welfare (e.g., Bertrand price wars).
     *Design lever:* add a small common reward component or hierarchical controller to push toward Pareto‑efficient equilibria.

2. **Need for communication and common knowledge**
   The more sensitive each payoff is to the joint action, the larger the set of joint policies that must be predicted. Cheap‑talk channels or learned message protocols directly reduce effective sensitivity by revealing \(a_{-i}\) before acting.

3. **Mechanism design / external incentives**
   Taxing negative externalities or subsidising positive ones **reshapes \(u_i\)**, often converting a general‑sum game into a potential game and restoring stable learning dynamics.

---

## Practical checklist for system designers

| Goal                                                       | Recommended choice                                                 | Expected effect                                                                          |
| ---------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Fast convergence in cooperative tasks                      | Potential‑game reward shaping or difference rewards                | Removes harmful cross‑derivatives; guarantees gradient descent behaves like single agent |
| Robustness under partial observability                     | Centralised critic + counterfactual baseline                       | Low‑variance gradient; implicit credit assignment                                        |
| Encourage emergent pro‑social behaviour in social dilemmas | Opponent‑aware updates (LOLA, COLA)                                | Shapes others’ learning trajectory toward cooperation                                    |
| Scale to thousands of agents                               | Multi‑timescale asynchronous learning; local network externalities | Treat far‑away agents as part of stationary environment                                  |

---

### Suggested empirical test

Compute a **sensitivity matrix** \(S_{ij}=|\partial \hat u_i/\partial a_j|\) from the learned critic.

* If \(‖S‖_\infty\) is large and gradients are unstable, apply reward shaping or slow down updates where \(S_{ij}\) is largest.
* Re‑measure \(S\) after changes; convergence of \(S\) toward a sparse or diagonal form indicates successful reduction in inter‑agent dependency.

---

### Residual uncertainty & next steps

* Exact second‑order effects of opponent‑aware gradients in games with many (>10) agents remain poorly understood. Simulate small‑n approximations first.
* The boundary where communication bandwidth fully offsets payoff sensitivity is domain‑specific; run ablations varying message size.

---

By recognising which knobs in the *formal model* and the *learning architecture* modulate pay‑off interdependence, you can systematically tune how sensitive each agent is to the rest of the system—and therefore how hard the coordination and learning problems will be.

[1]: https://arxiv.org/html/2505.10378v1?utm_source=chatgpt.com "Simultaneous Best-Response Dynamics in Random Potential Games"
[2]: https://en.wikipedia.org/wiki/Strategic_complements?utm_source=chatgpt.com "Strategic complements - Wikipedia"
[3]: https://papers.nips.cc/paper/8033-credit-assignment-for-collective-multiagent-rl-with-global-rewards?utm_source=chatgpt.com "Credit Assignment For Collective Multiagent RL With Global Rewards"
[4]: https://arxiv.org/abs/1705.08926?utm_source=chatgpt.com "Counterfactual Multi-Agent Policy Gradients"
[5]: https://web.stanford.edu/~jacksonm/networkgames.pdf?utm_source=chatgpt.com "[PDF] Network Games - Stanford University"
[6]: https://arxiv.org/abs/2302.02792?utm_source=chatgpt.com "Dealing With Non-stationarity in Decentralized Cooperative Multi-Agent Deep Reinforcement Learning via Multi-Timescale Learning"
[7]: https://www.cs.ox.ac.uk/people/shimon.whiteson/pubs/foersteraaai18.pdf?utm_source=chatgpt.com "[PDF] Counterfactual Multi-Agent Policy Gradients"
[8]: https://arxiv.org/abs/1709.04326?utm_source=chatgpt.com "Learning with Opponent-Learning Awareness"
[9]: https://arxiv.org/abs/2203.04098?utm_source=chatgpt.com "COLA: Consistent Learning with Opponent-Learning Awareness"
[10]: https://proceedings.mlr.press/v162/li22w/li22w.pdf?utm_source=chatgpt.com "[PDF] Difference Advantage Estimation for Multi-Agent Policy Gradients"
[11]: https://www.reddit.com/r/reinforcementlearning/comments/plx77g/nonstationarity_in_multiagent_learning/?utm_source=chatgpt.com "Non-stationarity in Multi-Agent Learning : r/reinforcementlearning"
[12]: https://www.sciencedirect.com/science/article/pii/S0022053106001086?utm_source=chatgpt.com "Finding all equilibria in games of strategic complements"


Agent payoff sensitivity in multi‑agent systems: formal/practical choices and their implications for learning and coordination

Introduction

In multi‑agent systems an agent’s payoff (or reward) is seldom independent of the actions of others. Strategic interactions are formalised by Markov games (or stochastic games), where each agent chooses actions that jointly determine the next state and the vector of rewards. The question asks why certain design choices make one agent’s payoff sensitive to the rest of the system and what that means for learning and coordination. To answer this, we examine how different forms of interaction, reward design and learning architectures influence payoff interdependence and the ability of agents to learn effective (and cooperative) policies.

1 Game type and incentive structure

1.1 Cooperative, competitive and mixed‑motive games
Cooperative games: In common‑payoff or team games, all agents share a global reward. A survey notes that designers can freely choose the agents’ policies and agents assume benevolent intentions
cs.gmu.edu
. Agents thus have aligned incentives; however, as described below, global rewards can make credit assignment hard and introduce large payoff sensitivity to others’ actions.
Competitive (general‑sum) games: When agents maximise their own individual utilities, the system becomes competitive
cs.gmu.edu
. An agent’s payoff explicitly depends on others’ actions because each is trying to maximise its own reward at the expense of others. Classical notions such as Nash equilibria apply; achieving coordination (or stable dynamics) requires anticipating opponents’ strategies.
Mixed‑motive games: In many real environments agents have partially aligned incentives. For example, a football team might be rewarded for winning (a team objective) but players may get an extra personal bonus for each goal they score. This creates heterogeneous incentives: players still want the team to win but may prefer to shoot rather than pass
arxiv.org
. If the bonus is large enough, players may even be incentivised to score an own goal, which conflicts with the team goal
arxiv.org
. Such social dilemmas illustrate how small changes in incentive structure can drastically change an agent’s payoff sensitivity to others. Achieving cooperation often requires additional mechanisms or norms (see section 7).
1.2 Potential games and Markov potential games
In potential games there exists a scalar potential function 
Φ
Φ such that any unilateral change by an agent modifies 
Φ
Φ by exactly the same amount as it changes the agent’s reward. The dynamic extension, Markov potential games (MPGs), provides similar properties for stochastic environments. A recent paper highlights that in an MPG there is a potential function that tracks changes in each agent’s cumulative reward, ensuring the existence of at least one pure‑strategy Nash equilibrium and guaranteeing convergence of gradient‑play methods
arxiv.org
. Designing payoffs to form a potential game effectively aligns individual rewards with a common objective and therefore reduces negative externalities; however, constructing such games can be restrictive and may not capture adversarial or mixed‑motive settings.

2 Reward design: global, local and difference rewards

2.1 Trade‑off between factoredness and learnability
In cooperative MARL the system often has a global performance measure 
G
(
z
)
G(z), where 
z
z is the joint state. Giving every agent the team reward 
T
i
=
G
(
z
)
T 
i
​	
 =G(z) maximally aligns incentives (factoredness = 1), but because each agent’s reward depends on the actions of all others, the learning signal becomes extremely noisy
ntrs.nasa.gov
. The factoredness of a reward measures how aligned an agent’s reward is with the global reward
ntrs.nasa.gov
, while learnability measures the ratio of the reward’s sensitivity to the agent’s own actions vs. other agents’ actions
ntrs.nasa.gov
. There is a trade‑off: high factoredness often comes with low learnability and vice versa
ntrs.nasa.gov
.

2.2 Local and difference rewards
To reduce sensitivity to other agents, local rewards 
P
i
=
G
(
z
i
)
P 
i
​	
 =G(z 
i
​	
 ) give each agent a reward based only on its own state. This yields infinite learnability because the agent’s reward responds solely to its own actions
ntrs.nasa.gov
, but local rewards may have low factoredness and can encourage selfish behaviours that undermine the global objective. A compromise is the difference reward 
D
i
=
G
(
z
)
−
G
(
z
−
i
)
D 
i
​	
 =G(z)−G(z 
−i
​	
 ), where 
z
−
i
z 
−i
​	
  is the state with agent 
i
i removed. The difference reward maintains high alignment with the global reward and has better learnability than the team reward by removing some effects of other agents
ntrs.nasa.gov
. Counterfactual computation of 
G
(
z
−
i
)
G(z 
−i
​	
 ) can be costly in practice, but it provides a principled way of measuring an agent’s contribution.

2.3 Implications for learning
When each agent receives the global reward, its payoff is highly sensitive to others’ actions: “an agent’s reward is masked by the actions of all the other agents in the system”
ntrs.nasa.gov
. This signal‑to‑noise problem slows convergence.
Local rewards reduce sensitivity but can lead to misaligned optima—policies that maximise individual rewards may not maximise global performance
ntrs.nasa.gov
.
Difference rewards and other counterfactual methods strike a balance, improving learning stability at the cost of more complex computation
ntrs.nasa.gov
.
3 Non‑stationarity and credit assignment

3.1 Non‑stationary environment
In MARL, each agent’s environment includes other agents who are simultaneously learning. As a result, the environment’s dynamics and reward structure change over time—a phenomenon known as non‑stationarity. A recent survey formally notes that the environment perceived by any agent is non‑stationary because the joint policy evolves
arxiv.org
. This turns the learning problem into a moving target and undermines the assumptions underpinning standard RL. The Bellman equation becomes time‑dependent and policy updates can oscillate
arxiv.org
. Sample efficiency suffers because past experiences become less relevant as other agents adapt
arxiv.org
, and credit assignment becomes harder because rewards depend on the collective actions of all agents
arxiv.org
.

3.2 Credit assignment challenges
Multi‑agent systems face two credit assignment problems: (i) temporal credit assignment (linking rewards to actions across time) and (ii) structural credit assignment (attributing the global reward to individual contributions). When a global reward is used, each agent must isolate its contribution from the noise generated by others, exacerbating the structural problem
ntrs.nasa.gov
. Counterfactual methods (e.g., difference rewards) and value decomposition networks address this by approximating marginal contributions, but these methods can be computationally intensive.

4 Training paradigms and information structures

4.1 Centralised vs. decentralised training
An overview of MARL paradigms divides methods into:

Centralized Training & Execution (CTE): uses full global information at both training and execution. It scales poorly as the joint action space grows exponentially but avoids non‑stationarity and credit assignment issues because a central controller computes actions for all agents
arxiv.org
. Suitable mainly for cooperative tasks.
Centralized Training with Decentralized Execution (CTDE): uses global information (e.g., other agents’ observations and actions) during training but trains a separate policy for each agent that runs only on local observations during execution. CTDE improves scalability and allows coordination without communication
arxiv.org
. Many value‑decomposition and actor‑critic methods, such as QMIX, MADDPG, and COMA, operate in this paradigm. However, if agents’ payoffs are still global, the policies remain sensitive to others’ actions and require careful credit assignment during training.
Decentralized Training & Execution (DTE): each agent learns independently using only its local observations. This paradigm is easiest to implement but suffers most from non‑stationarity, because each agent perceives the others as part of a changing environment
arxiv.org
. Independent Q‑learning often fails to converge even in simple general‑sum games. Techniques like opponent modeling (section 6) and communication protocols can mitigate these issues.
4.2 Information and observability
Partial observability further increases payoff sensitivity. Agents cannot observe the entire state, so they must infer hidden variables based on observations and history. The survey notes that agents need to maintain belief states and handle non‑Markovian dependencies
arxiv.org
. When agents have little information about others, they are forced to learn reactive strategies, making coordination harder. Allowing limited communication or shared information during training (e.g., CTDE) can dramatically improve coordination.

5 Opponent modeling and learning awareness

Independent learners treat others as part of a non‑stationary environment. Opponent modeling methods explicitly model or anticipate the learning of other agents to reduce payoff uncertainty. The Learning with Opponent‑Learning Awareness (LOLA) algorithm adds an extra term to each agent’s policy update that estimates how its own policy affects the anticipated updates of other agents. The authors show that LOLA agents achieve cooperative tit‑for‑tat behaviour in the iterated prisoner’s dilemma, while naïve independent learners do not
arxiv.org
. By anticipating others’ learning, LOLA agents shape the learning dynamics and achieve higher payoffs
arxiv.org
. This demonstrates that shaping the learning process, not just the payoff function, influences how sensitive an agent’s reward is to others.

6 Social preferences and fairness considerations

Human behaviour often includes social preferences like inequity aversion and reciprocal fairness. A study on fairness in multi‑agent systems notes that purely selfish behaviour can lead to worse outcomes because other agents may punish or refuse unfair offers
ifaamas.org
. Agents can be designed with inequity aversion preferences, meaning they derive negative utility from unequal rewards, which encourages cooperation. In intertemporal social dilemmas, incorporating inequity aversion into the agents’ reward function improves cooperation and credit assignment, promoting large‑scale cooperation
arxiv.org
. Fairness-based reward shaping therefore alters payoff sensitivity: agents become sensitive not only to aggregate outcomes but also to the distribution of rewards across agents.

7 Implications for learning and coordination

Global reward sensitivity vs. learnability trade‑off: When rewards depend on the joint actions of all agents, each agent’s payoff is highly sensitive to others. This sensitivity impedes learning due to noisy signals and non‑stationarity
ntrs.nasa.gov
. Using local or difference rewards reduces sensitivity and improves learnability, but designers must ensure that the resulting local optima still correspond to desirable global behaviour
ntrs.nasa.gov
.
Non‑stationarity and instability: Agents with evolving policies create a moving target for learning algorithms. Non‑stationarity leads to oscillations and poor sample efficiency
arxiv.org
. Stable coordination often requires centralized information during training (CTDE), structured games (e.g., potential games), or opponent modeling techniques like LOLA
arxiv.org
arxiv.org
.
Heterogeneous incentives and social dilemmas: Adding individual incentives can change a cooperative game into a social dilemma, making agents less willing to cooperate
arxiv.org
. Designers can mitigate this by aligning incentives (e.g., through contracts or taxes) or incorporating social preferences into the reward function. Fairness-based shaping (inequity aversion) helps agents coordinate by punishing defectors and rewarding cooperation
ifaamas.org
.
Structured games facilitate convergence: Designing the environment as a potential game or MPG allows agents to use simple gradient-based learning to converge to a pure Nash equilibrium
arxiv.org
. This reduces sensitivity to others because changes in individual rewards correspond to changes in a global potential function.
Communication and information sharing: Sharing information (e.g., through CTDE or explicit communication protocols) reduces uncertainty about others’ actions and learning processes, lowering payoff sensitivity. However, communication may introduce costs and scalability issues.
Opponent modeling: Modeling or shaping the learning of other agents, as in LOLA, allows each agent to anticipate how its actions influence the future behaviour of others
arxiv.org
. This can transform adversarial dynamics into cooperative ones, improving coordination and returns.
Conclusion and recommendations

Different formal and practical choices in multi‑agent system design fundamentally affect how sensitive an agent’s payoff is to the rest of the system. Reward design determines whether an agent sees a noisy global signal or a clearer local one. Game type and incentive structure decide whether agents’ goals are aligned, competitive or mixed, influencing trust and the likelihood of cooperation. Training paradigms affect information availability and thereby the perceived non‑stationarity. Structured games such as potential games provide guarantees of convergence and reduce externalities, whereas general‑sum games require more sophisticated learning. Opponent modeling and social preferences can further shape payoff sensitivity by enabling agents to anticipate or care about others’ learning and welfare.

For practitioners, a key takeaway is the need to balance alignment and learnability. When designing cooperative systems, simple global rewards may not suffice; consider difference rewards or value decomposition to improve credit assignment. In mixed‑motive settings, examine incentive structures to avoid social dilemmas and use fairness or taxes to align behaviour. For general‑sum games, use centralized training or opponent modeling to mitigate non‑stationarity. Finally, explore potential games or structured interactions where feasible to obtain convergence guarantees and predictable coordination.



---

## 3 Who actually deserves credit (or blame) for a joint reward? (the multi-agent credit assignment puzzle)
