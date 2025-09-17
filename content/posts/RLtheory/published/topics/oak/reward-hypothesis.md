---
date: "2025-08-26"
title: "Reward Hypothesis (Reward is Enough)"
summary: "Reward Hypothesis (Reward is Enough)"
lastmod: "2025-08-26"
category: "Notes"
series: ["Continual Learning"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# Tell me in detail what is the reward hypothesis

Here’s the core idea, stripped down and then built back up:

## The short version

**The reward hypothesis** says that *any* goal an agent might pursue can be expressed as the maximization of a single, scalar **reward** signal delivered by its environment. So if you can define “how well things are going” as numbers over time, then choosing actions to make those numbers large is—at least in principle—enough to represent the agent’s goals.&#x20;

---

## What that means, a bit more formally

Reinforcement learning (RL) frames decision‑making as an **agent** interacting with an **environment** over time. At each step \(t\), the agent observes something, takes an action \(A_t\), and receives a scalar **reward** \(R_t\). The agent’s objective is to pick actions that maximize some cumulative measure of reward, e.g.:

$$
\max_\pi  \mathbb E \left[\sum_{t=0}^{\infty} \gamma^t R_t \middle \mid \pi\right]
$$

where \(\pi\) is the policy (how the agent acts) and \(\gamma \in [0,1)\) is a discount factor. Other cumulative objectives (finite sums, average reward per time step) fit the same mold. The crucial bit is *the goal lives entirely inside the reward signal*.&#x20;

---

## Why this is attractive

* **Unifying target:** You don’t need a different objective for every sub-ability; you specify one reward definition and let the agent figure out how to act. The RL setup explicitly separates *what you want* (reward) from *how to get it* (the agent’s policy).&#x20;
* **Expressiveness:** A single scalar reward can encode multi‑objective trade‑offs (e.g., safety, efficiency, comfort in driving) via weighting, risk sensitivity, or time preferences. You can even route in human feedback (“thumbs up/down”, survey scores) as reward.&#x20;
* **Ongoing feedback:** Because reward can arrive at every step, it gives learnable intermediate signals for very long tasks where waiting for a final pass/fail would be hopeless.&#x20;

---

## What it is *not*: “Reward is enough”

You’ll see a related claim called the **reward‑is‑enough hypothesis** (Silver, Singh, Precup, Sutton). *That* hypothesis goes further: it argues that **maximizing reward in a rich world can be sufficient for the emergence of many abilities we call “intelligence”** (perception, language use, social savvy, etc.). In that paper they emphasize the distinction: the reward hypothesis is about **representing goals as reward**, while “reward is enough” is about **whether optimizing a (reasonable) reward in complex environments induces broad abilities**. (See the footnote and surrounding discussion distinguishing the two.)&#x20;

> If you want a picture: the **diagram on page 2** shows a squirrel or a kitchen robot maximizing a simple reward (food; cleanliness), with a cloud of abilities (perception, planning, memory, language, social intelligence) “projected out” as what’s needed to succeed. That’s the “reward is enough” angle—not strictly required by the reward hypothesis, but closely related.&#x20;

---

## Practical implications if you adopt the reward hypothesis

* **Design shifts to reward specification.** Your main job becomes: define the reward so that its maximization *actually* captures the intended goal. The RL machinery then learns a policy to maximize it.&#x20;
* **You can fold in multiple signals.** Weighted sums, shaped rewards, sparse terminal rewards, or human-in‑the‑loop feedback all still “count” as reward.&#x20;
* **Intrinsic vs. extrinsic reward.** You might add internal signals (curiosity bonuses, shaping terms) that are *different* from the end objective but are chosen because they make it easier to learn behaviors that ultimately increase the true objective. (The paper notes the distinction between a design goal and internal rewards used to serve it.)&#x20;

---

## Common tensions and failure modes (because real life is messy)

* **Reward misspecification.** If your numeric proxy doesn’t match what you care about, agents will optimize the proxy, not the intent—classic “specification gaming.” That’s not a knock on the hypothesis; it’s a warning about *your* reward design.
* **Sparse/delayed reward.** When useful feedback comes late (e.g., only at the end of a long episode), learning can be painfully slow; you often need credit‑assignment tricks, value functions, models, or better exploration to cope.&#x20;
* **Side effects and safety.** Maximizing a scalar can push agents toward unwanted side effects if those aren’t penalized in the reward. The remedy—again—is to model those costs in the reward or the environment.
* **Context dependence.** The “right” reward often depends on situation. The paper highlights that many perceptual and social behaviors are valuable *because* they ultimately boost reward in context, not in isolation.&#x20;

---

## How this connects to intelligence claims

* The paper argues that **rich environments + reward maximization pressure** can push agents to acquire capabilities that look like perception, language, social reasoning, generalization, and even imitation—not because we separately optimized for those, but because they’re instrumentally useful for getting more reward. That’s the broader thesis beyond the reward hypothesis. (See Sections 3.1–3.7.)&#x20;

---

## One‑liner you can keep in your pocket

> *If you can write down “good” as a number over time, then maximizing that number is enough to express the goal—the rest is learning how to do it well.*&#x20;

If you want, I can sketch a concrete reward for a domain you care about (robotics, trading, tutoring, etc.) and we can sanity‑check where it might go sideways.

---

# Why Reward Hypothesis might be true?

Here’s the clean picture, then the nuance.

## What the “reward hypothesis” says

Richard Sutton’s reward hypothesis claims that *everything we mean by goals and purposes can be represented as maximizing the expected value of a cumulative scalar reward signal*. In other words: if you can state a goal, you can model it as “pick actions to make the (properly defined) sum of rewards as large as possible.”&#x20;

### Why people care

If that statement holds, the reinforcement‑learning (RL) problem class is enough to model goal‑directed behavior: build an agent that maximizes an appropriate cumulative reward, and you’ve captured “purpose.” That’s a big deal for AI design and for the theory of agency.&#x20;

---

## A precise, modern formalization (Bowling, Martin, Abel, Dabney, ICML’23)

The paper you shared, *Settling the Reward Hypothesis*, doesn’t just say “true” or “false.” It spells out **exactly** when the hypothesis holds, and when it doesn’t. The move is to replace vague talk of “goals” with **preferences over histories** (full observation–action sequences or, more generally, distributions over them). Two versions are considered:

* **Subjective goals:** the reward is computable from the agent’s own stream of observations.
* **Objective goals:** a *designer* has preferences over their (possibly richer) observation stream and supplies the agent a learning signal that reflects those preferences.&#x20;

Formally, the agent interacts in steps, generating histories \(h = (o_1,a_1,o_2,a_2,\dots)\). A **goal** is a preference ordering \(\succeq\) over (distributions of) such histories. A policy \(\pi_1\) is preferred to \(\pi_2\) when, beyond some finite horizon, \(\pi_1\) induces “better” history distributions than \(\pi_2\). This “eventual dominance” lets the framework cover episodic tasks, ongoing tasks, discounted and average‑reward cases in one stroke.&#x20;

### Unifying “cumulative sums”

They show a single return that covers episodic totals, discounted sums, and average reward by allowing a **transition‑dependent discount** \(\gamma(o,a)\in[0,1]\):

$$
V_n^\pi = \mathbb{E}\Big[\sum_{i=1}^n \Big(\prod_{j=1}^{i-1}\gamma(O_j,A_j)\Big) r(O_i,A_i)\Big].
$$

Choosing \(\gamma(\cdot)=\gamma<1\) recovers discounted RL; \(\gamma(\cdot)=1\) aligns with average/total reward; \(\gamma(\cdot)=0\) at terminal steps matches episodic returns.&#x20;

---

## The support: an “if and only if” theorem

The paper identifies **necessary and sufficient conditions** (axioms) under which your preferences over histories are *exactly equivalent* to maximizing an expected cumulative **Markov** reward with a (possibly transition‑dependent) discount. That’s the main theoretical backing.

### Step 1 — Classical rationality (vNM)

Assume your preference relation satisfies the standard von Neumann–Morgenstern axioms: **completeness, transitivity, independence, continuity**. These alone guarantee there is some utility function that represents your preferences over distributions (expected utility). But this utility may depend on the *entire* past, so it doesn’t yet justify a **Markov** reward signal the agent could read step by step.&#x20;

### Step 2 — A new axiom: **Temporal γ‑Indifference**

This is the paper’s key addition. Intuitively: prepending the same transition \(t\) to two possible futures should change your preference between those futures by a **multiplicative factor \(\gamma(t)\)**—no more, no less.

* If \(\gamma(t)=1\), you’re indifferent to which of two equally likely futures gets delayed by \(t\).
* Different \(t\) can have different \(\gamma(t)\), which is how the framework accommodates episodic, discounted, and average‑reward objectives under one roof.&#x20;

### The **Markov Reward Theorem**

With (i) vNM rationality and (ii) Temporal γ‑Indifference, the authors prove the **Markov Reward Theorem**:

> **There exists a Markov reward \(r(t)\) and transition‑dependent discount \(\gamma(t)\) such that your preference over policies equals the preference induced by maximizing expected cumulative discounted reward.** Formally, there’s a utility \(u\) satisfying
> \(u(t\cdot h) = r(t) + \gamma(t)u(h)\),
> and \(A \succeq B \iff u(A)\ge u(B)\).

The representation is unique up to positive scaling of the reward. This is an “if and only if” result: the axiom set is exactly what you need—and no more—to reduce “goals and purposes” to maximizing (generalized) cumulative reward. That’s the core theoretical support.&#x20;

### Designer’s (objective) goals are covered, too

They extend the result when a *designer* has preferences over their own observation stream (which may include the agent’s hidden state, actions, or other context) and provides either reward-plus-discount or a single “already‑discounted” reward signal \(r_i = (\prod_{j<i}\gamma(\bar o_j))r(\bar o_i)\). The same theorem structure goes through.&#x20;

### Constructive support: you can *build* the reward

It’s not just existential. Given a preference oracle that satisfies the axioms, they give an algorithm to **construct** \(r\) and \(\gamma\). Runtime is \(O(|O\times A|\log|O\times A|)\) using a preference‑based sorting and scaling routine. That’s practical support for the hypothesis-as-representation theorem.&#x20;

---

## How this sits with prior results (and common objections)

**Links to earlier theory.**

* The new axiom **generalizes** conditions used in recent work (e.g., “Memoryless” and “Additivity” axioms from Shakerinava & Ravanbakhsh, 2022). The paper proves equivalences showing their axiom subsumes those—another layer of support.&#x20;
* It also clarifies results about the **limits** of Markov rewards (Abel et al., 2021): two classic counterexamples (“steady‑state” and “entailment”) violate, respectively, the paper’s policy‑preference assumption and the new γ‑indifference axiom. In other words: the failures are expected once you see which conditions the theorem needs.&#x20;

**Average‑reward and bias‑optimality fit the frame.**
By comparing finite‑horizon cumulative sums “eventually,” the authors show average‑reward orderings and even bias‑optimal refinements appear as special cases (with \(\gamma\equiv 1\)). That shores up the hypothesis across continuing tasks.&#x20;

**What about humans being “irrational”?**
If your preferences violate vNM axioms (Kahneman/Tversky‑style effects), the representation may fail. The paper notes that this is a statement about **preference expression**, not behavior per se; when the axioms don’t hold, you shouldn’t expect a clean Markov reward encoding. That’s a limit, clearly acknowledged.&#x20;

**Multiple objectives and constraints.**

* **Constrained MDPs** (maximize one thing subject to bounds on others) can break **independence** and **continuity**; the paper gives a small example where mixing distributions flips feasibility and reverses preferences. That means such constrained goals won’t, in general, reduce to scalar Markov reward—unless you change the problem (e.g., move constraints into state).&#x20;
* **Risk‑sensitive** objectives can make the optimal policy inherently **non‑Markovian**, which contradicts the possibility of a Markov reward that reproduces the same policy under risk‑neutral maximization. Diagnosis: a failure of the γ‑indifference axiom; a remedy is to augment state (objective‑goals framing).&#x20;

**Discounting details.**
A **constant** discount \(\gamma\in(0,1)\) is a special case of the theory, but it’s too restrictive to capture all rational preferences; **transition‑dependent** discounting is often required. The paper also flags that **hyperbolic** discounting isn’t covered by their theorem as stated.&#x20;

**“Reward is enough” vs. the reward hypothesis.**
They distinguish Sutton’s hypothesis (“goals can be *represented* as reward maximization”) from the stronger “reward‑is‑enough” claim (“intelligence itself is subservient to reward”). This paper is about the representational claim and pins down its exact scope.&#x20;

---

## Bottom line (what’s actually supported)

* **Support = a crisp theorem:** Under vNM rationality **+** Temporal γ‑Indifference, **every** coherent goal (as preferences over histories) is **equivalent** to maximizing an expected cumulative **Markov** reward with an appropriate (possibly transition‑dependent) discount. That’s both necessary and sufficient.&#x20;
* **Practical backing:** There’s a constructive procedure to recover \(r,\gamma\) from preferences.&#x20;
* **Scope and limits are explicit:** If you bring in constraints that violate independence/continuity, or risk measures that force non‑Markov optimality, or human‑style dynamic inconsistencies, you’ve stepped outside the axiom set—so don’t expect a clean scalar Markov reward to exist without changing the state/observations.&#x20;

If you want, we can zoom into one angle next—e.g., unpack γ‑indifference with concrete toy examples, or walk through how the construction algorithm infers \(r\) and \(\gamma\) from pairwise preferences.&#x20;

---

# Tell me in detail what, how, and why is reward is enough


Here’s a clean way to hold it: **what** the claim is, **how** it says abilities emerge, and **why** the authors think that’s enough.

---

## What is the “reward‑is‑enough” hypothesis?

It’s a single sentence:

> **Intelligence, and the abilities we associate with it, can be understood as subserving the maximization of reward by an agent acting in its environment.**&#x20;

In plainer terms: if an agent is pushed—over a lifetime—to get as much of some scalar reward as possible in a rich world, the skills we call “intelligent” (perception, language, social savvy, planning, etc.) should arise because they help get more reward. The paper distinguishes this from the *reward hypothesis* (that any goal can be represented as a reward signal): reward‑is‑enough is about **abilities emerging** from pursuing a goal, not just **encoding** the goal. (See the footnote introducing Section 3.)&#x20;

A visual: **Figure 1 on page 2** shows a squirrel (reward = food) and a kitchen robot (reward = cleanliness). The “cloud” of abilities—perception, memory, language, social intelligence—sits off to the side as what’s *instrumentally required* to do well on those singular rewards.&#x20;

---

## How does reward supposedly give rise to those abilities?

The paper grounds everything in the reinforcement‑learning (RL) protocol: an **agent** interacts with an **environment**, receiving observations and a scalar **reward** at each step, and tries to maximize a cumulative reward objective (e.g., discounted return). That framing keeps “what you want” (reward) separate from “how you behave” (policy).&#x20;

From there, the mechanism is simple but ruthless:

> In **complex environments**, any behavior that actually maximizes reward must recruit whatever abilities the environment demands. So the *pressure to get reward* is the driver; the *abilities* are side effects.&#x20;

Concretely, Section 3 walks through major abilities and sketches why each can fall out of reward maximization:

* **Knowledge & learning (3.1).** Some knowledge may be innate (evolution/design), but most must be learned because future experience is uncertain and too varied for fixed priors. A reward‑maximizing agent therefore acquires and stores the knowledge it needs to do better in the situations it actually encounters.&#x20;
* **Perception (3.2).** Perception becomes *active and purpose‑bound*—you gather and process sensory information when it helps the goal (e.g., move your eyes, probe with your hands), accounting for costs of information. This explains context‑dependence and why labeled data aren’t essential in the wild.&#x20;
* **Social intelligence (3.3).** Other agents are part of the environment. To earn reward amid them you model, anticipate, and influence their behavior; sometimes you hedge with robust or stochastic strategies when you can’t tell which opponent you’re facing. Interestingly, maximizing *your* reward can even beat equilibrium play when others are suboptimal.&#x20;
* **Language (3.4).** Language is treated as consequential action: you produce utterances to change the world (often via other agents) and interpret utterances to avoid loss or gain advantage. Full‑blooded language then emerges where it helps reward—grounded in perception, context, and goals.&#x20;
* **Generalization (3.5).** In one long, messy stream of life, the state keeps changing; you must generalize from past to future states to keep reward high, not just transfer between tidy, labeled tasks.&#x20;
* **Imitation / observational learning (3.6).** Watching others is just another source of experience; an agent can map what it observes to its own state and actions when that improves reward, without needing a special “teacher dataset.”&#x20;
* **General intelligence (3.7).** If the single environment is rich enough, one **singular reward** (e.g., survival/battery life) can force competence across many sub‑goals. That’s their route to artificial general intelligence.&#x20;

Two supporting pieces:

* **The environment is broad.** **Table 1 on page 4** shows how “environment” can be discrete/continuous, single/multi‑agent, stationary/non‑stationary, simulated/real, etc.—so the claim is not hiding behind toy worlds.&#x20;
* **Learning machinery (Section 4).** A practical agent learns from trial and error; it may use value functions, models, planning, or policy optimization—whatever helps it improve future reward. No single algorithm is prescribed; the point is that *learning to maximize reward* is the engine.&#x20;

---

## Why do the authors think reward really is “enough”?

**1) A unifying objective beats one‑off objectives.** Instead of designing separate goals for perception, language, planning, etc., you specify one reward and let the world’s complexity “pull” the needed abilities. This also integrates abilities naturally because they all serve one end. The AlphaZero case is their poster child: optimizing only win/loss (+1/–1 at the end) yielded openings, tactics, global strategy, and risk management—no bespoke sub‑objectives.&#x20;

**2) It’s robust to the *choice* of reward.** You don’t need a magical, perfectly crafted signal. In a rich world, even a simple reward (e.g., “collect round pebbles”) escalates into tool use, navigation, persuasion—because that’s what doing well demands. (They call this out directly in the Discussion.)&#x20;

**3) Alternatives don’t fully close the loop.**

* **Unsupervised learning** and **prediction** can structure experience, but they don’t specify *what to do*; they lack a principle for action selection toward goals.
* **Supervised imitation** can mimic humans but may stall on non‑human goals or novel environments (and risks staying inside the data’s envelope).
* **Evolution** explains innate structure via fitness-as-reward; but for artificial agents we may want other goals and faster, within‑lifetime learning.
* **Free‑energy/minimum‑surprise** offers a compelling lens, but the authors argue it doesn’t provide a general‑purpose lever for many different, externally chosen goals.&#x20;

**4) There’s early, practical evidence.** Beyond Go and chess, agents pushed to maximize game score or task success have shown surprisingly broad capabilities (Atari gameplay; vision‑based robotic grasping; large‑scale multi‑agent training like StarCraft II). These are narrower than life, but they’re consistent with the principle.&#x20;

**5) The “is the signal too thin?” worry has answers.** In practice, reward maximization is bootstrapped by learned predictions (value functions), models, and other internal signals that densify learning without changing the outer objective. The paper emphasizes this to counter the idea that a scalar reward can’t support rich learning.&#x20;

---

## What this *doesn’t* claim (acknowledged limits)

* **It’s a hypothesis, not a theorem.** There’s no guarantee of sample efficiency or universal emergence; environment, algorithms, and inductive biases matter. The authors are explicit about this.&#x20;
* **Offline data alone is rarely enough.** You usually need online interaction to cover the long tail of situations your current policy actually faces.&#x20;

---

## Bottom line you can carry forward

> In sufficiently rich worlds, **one scalar objective** can be the whole story: it tells the agent *what counts*, and the world forces it to grow the abilities that help. That’s the “reward is enough” bet.&#x20;

If you want to stress‑test it in a domain you care about (robotics, tutoring, trading), we can sketch a single reward and see which abilities the environment would *force* to appear—and where it might break.

---

# Tell me in detail what are the common challenges to the reward hypothesis.


Here’s the lay of the land. Most “challenges” to the reward hypothesis boil down to *violating one of the assumptions/axioms* needed to represent goals as maximizing an expected cumulative **scalar** reward (possibly with transition‑dependent discounting). When an objection hits one of those nerves, the scalar‑Markov‑reward story cracks.&#x20;

Below are the common pressure points, what they claim, and which assumption/axiom they actually step on.

---

## 1) “Humans aren’t rational”

**Claim.** People show framing effects, conjunction fallacies, time inconsistency… so how could their “goals” be captured by expected cumulative reward?

**Diagnosis.** This targets the **von Neumann–Morgenstern (vNM) rationality axioms** (completeness, transitivity, independence, continuity). The paper’s result only guarantees a Markov reward representation *if* stated goals can be expressed by preferences satisfying those axioms; empirical “irrational” behavior doesn’t refute the representation of *goals*. It just says: if your expressed preferences break vNM, don’t expect a clean scalar Markov reward to exist.&#x20;

**What helps.** Move from noisy behavior to explicit preference statements (or designer preferences) and check the axioms; otherwise accept that extra structure (history, state augmentation, etc.) will be required.&#x20;

---

## 2) Multiple objectives & trade‑offs (safety *and* speed *and* energy, etc.)

**Claim.** Real purposes are multi‑criteria; squashing them to one scalar seems wrong.

**Diagnosis.** Multi‑objective setups often violate **Independence** or **Continuity** once you encode feasibility/constraints (“do X, but keep Y ≥ 0”). The paper shows constrained MDPs can flip preferences under mixing (violating Independence) or have no break‑even mixture (violating Continuity). Example: mixing a feasible and an infeasible distribution can reverse which option is preferred. That breaks the axioms needed for a scalar Markov reward representation.&#x20;

**What helps.** (i) Use **vector rewards** plus an explicit decision rule—more expressive, but then you’ve left the scalar hypothesis; (ii) fold constraints into state/observations so feasibility becomes part of the “world,” sometimes restoring scalarizability.&#x20;

---

## 3) Risk sensitivity (variance penalties, CVaR, etc.)

**Claim.** Agents care about risk, not just expected value; optimal risk‑sensitive behavior can depend on history.

**Diagnosis.** Risk objectives can make the **optimal policy non‑Markovian** even in Markov environments. If the optimal policy necessarily needs past information (e.g., “choose the action that *opposes* the earlier random reward to reduce variance”), there is **no Markov scalar reward** that reproduces that policy under risk‑neutral maximization. In the paper’s terms, this typically **violates Temporal γ‑Indifference** (the new axiom), so the representation fails.&#x20;

**What helps.** Augment the state/observations (objective‑goals framing) so the relevant “memory” is encoded—and only then consider scalar rewards again.&#x20;

---

## 4) Classic expressivity counterexamples for Markov rewards

*(“steady‑state” and “entailment” types; Abel et al.)*

**Claim.** Some policy orderings just can’t be expressed by a Markov reward over the given state space.

**Diagnosis.**

* **Steady‑state type:** preferences talk about outcomes that never occur under the policies being compared. This **violates the policy‑preference assumption** (eventual dominance over induced history distributions), so the whole reduction to rewards doesn’t get off the ground.
* **Entailment type:** whether an action is desirable in one state depends on what you do elsewhere (global coupling). This **violates Temporal γ‑Indifference**.
  In both, the issue isn’t “reward is meaningless”; it’s “your preference relation isn’t of the representable kind over this state/action interface.”&#x20;

**What helps.** Refine the state (encode the needed global/contextual bits) or relax to non‑Markov reward representations.&#x20;

---

## 5) Time preference quirks (discounting form, dynamic inconsistency)

**Claim.** Real agents discount hyperbolically or change their minds over time; standard discounted sums can’t match that.

**Diagnosis.** The theorem covers a **transition‑dependent exponential‑style discount** \(\gamma(t)\), letting it capture episodic/average/discounted cases in one return. But **hyperbolic discounting** and other dynamically inconsistent forms fall outside the provided axioms/representation. The paper notes constant \(\gamma\) is often *too restrictive*, and hyperbolic isn’t addressed by their theorem. If your preferences show **dynamic inconsistency**, they’ll conflict with axiom structure (and even a stricter “sequential consistency” idea).&#x20;

**What helps.** Use transition‑dependent \(\gamma\) where possible; otherwise, accept non‑Markov utilities or explicitly time‑inconsistent planning models.&#x20;

---

## 6) History dependence & computability

**Claim.** If you start from vNM utility over histories, the implied “reward” can depend on the *entire past*—not something the agent can read from its immediate observation.

**Diagnosis.** With only vNM axioms, you get a utility representation—but the induced “reward” \(r(t;h)=u(h\!\cdot\!t)-u(h)\) is **history‑dependent** and may be **incomputable** for bounded agents. You need the extra **Temporal γ‑Indifference** axiom to collapse this into a **Markov** reward (depends only on the current transition). Without it, the scalar‑Markov reduction isn’t justified.&#x20;

**What helps.** Either (i) accept non‑Markov reward/utility, or (ii) enlarge observations so the needed history features are now “Markov.”&#x20;

---

## 7) Designer vs. agent perspectives (misalignment of observables)

**Claim.** The agent doesn’t see what the designer cares about; how can a scalar signal capture the designer’s goal?

**Diagnosis.** If the **designer** has richer observations than the agent, goals might not be representable from the agent’s raw stream. The paper handles this by moving to **objective goals**: define preferences over the designer’s observations and provide the agent with a (possibly *already‑discounted*) scalar signal that reflects those preferences. Without that, the representability at the agent interface can fail.&#x20;

**What helps.** Reward modeling from designer signals (including state augmentation or reward bundles) so the scalar signal actually carries the needed information.&#x20;

---

### A quick decoder ring (challenge → what’s really violated)

* Human “irrationality” → one or more **vNM axioms** don’t hold.&#x20;
* Multi‑objective / constrained MDPs → **Independence** and/or **Continuity** fail under feasibility/lexicographic rules.&#x20;
* Risk sensitivity → optimal behavior becomes **non‑Markov**, breaking **Temporal γ‑Indifference**.&#x20;
* Steady‑state / entailment → **policy‑preference assumption** or **Temporal γ‑Indifference** is violated.&#x20;
* Hyperbolic discounting / time inconsistency → outside the provided γ‑indifference form and **sequential consistency**.&#x20;
* History‑dependent “rewards” → without **γ‑Indifference**, the ‘reward’ may depend on full history, not Markov.&#x20;
* Designer/agent mismatch → scalar signal at the agent interface lacks the designer’s info unless you **remap** it.&#x20;

---

### Bottom line

The reward hypothesis survives lots of objections *if* you’re precise about the preferences and the interface. The paper’s contribution is a clean map: when stated goals satisfy vNM rationality **and** the new **Temporal γ‑Indifference** axiom, you *can* represent them as maximizing an expected cumulative (Markov) reward with an appropriate discount. When the common challenges above appear, it’s because you’ve stepped outside that axiom set—so you either change the state/observations, drop the scalar restriction, or accept non‑Markov utilities.&#x20;

If you want, we can zoom in on one of these (e.g., the constrained‑MDP counterexample in Figure 2) and work through how the violation shows up algebraically and how state augmentation or vector rewards would fix it.&#x20;




