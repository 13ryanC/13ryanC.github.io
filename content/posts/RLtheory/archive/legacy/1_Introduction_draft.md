---
_build:
  render: never
  list: never

date: "2025-06-26"
title: "Some Intuition from lecture 1 of Casba's RL theory series"
summary: "errata"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

Help me to tidy this set of notes taken from the first lecture of Csaba Szepesvári's RL theory. Make sure you retain the structure and all the nuances in the original notes.

"""
RL is the big brother of bandits and bandits serve as the bedrock foundation for RL.

Background:
1. Bandit book (measure-theoretic), construction of measures, ch.2, 3, 5, 7, 26, 38.
2. The second course of probability theory, ch. 1, 3, 4, 5.
3. Appendix A of Csaba's book Algorithm of RL
4. RL Theory seminars (https://sites.google.com/view/rltheoryseminars/home)


There is a venn diagram of three circles: planning, batch RL, and online RL.

Among the intersection of the three circles is Markov Decision problems or processes (MDPs)

Csaba's focus on questions in diving deep resonates with me a lot.


General RL problem formulation is by taking actions in stochastic environments, to maximise total reward while taking observations about the environment's state.

One question that arises come from wh is this formulation and what would happen if we tweak it. Another question arises, is that what other formulations can we measure.

Why is learning important? for AI?


Why do we care about learning algorithms?

So it was observations that help decide what actions to take. It is not given the environment, and rahter algorithms need to work across multiple environments.

So planning is about computation. So in planning, we are concerned about computation problems to efficiently and effectively to compute actions that enable good policy with respect to observations of the environment's state.

So here in planning, we are concerned about coming up with the model of the environment to come up with good actions.

What models should I learn in order to learn efficiently.

We then have batch RL, which mainly concerns about extracting policy from batch data. Often, it is too risky to directly apply to real world problems to start learning, so we would want to first give it a bunch of data and see what it can do, before one deploys it to the real-world, for example in medicial applications. They use data to replace interaction with the environment, to reduce risk and as a proof of concept. This is evident in supervised learning and self-supervised learning.

The third circle is online RL, which is the classical RL, where we have interaction with the environment, and get rewards.

So what is a MDP, well, it is formulated to model an environment that has stochastic state transitions, where states S and actions A are primitives pertinent to the environment.

Stochastic Transitions between states (s, a) -> distribution over states P_a(s).

Rewards are that for every state-action pair (s,a), we have a reward r_a(s) \in \mathbb{R}, r_a(s) \in [0, 1] if normalised.


The objective is typically starting at some state-action pair (s_0, a_0), where we have a trajectory, where 

\tau = (s_0, a_0) => (s_1, a_1) => ... => (s_t, a_t)

where for each state-action pair, we have a reward r_a_0(s_0), where 
we have a return of the trajectory, which is the sum of the rewards for each state-action pair.

The objective is to maximise the return as the objective, do we average this, or do we discount this. This is a very huge problem, and re-write the MDPs and have many different problems associated for learning that we are of interest. 

For discounting, we have \gamma \in [0, 1), where there is implicit regularisation, which has the effective horizon problem and the underlying discounted problem.

\dfrac{1}{\varepsilon (1 - \gamma)}

the epsilon is useful if you are interested in measuring the finite sum up to epsilon accuracy. then you can truncate the sum after roughly this many terms, and such that the gap between the truncated sum and the original sum is within the range of epsilon.


Basicaly we would want to maximise the return, where the problem of the return is that it does not tell whethr the transitions are stochastic. 
Since the transitions are stochastic, the return in general has a distribution over the trajectories that is induced by how you are interacting with the MDP or controlling the MDP, the way you control the MDP is the policy.

This gives rises to the question of what does it even mean to maxmise the return, as it itself is a distribution of trajectorires, it is uniqe, so we tend to take the exepctaations, what does that mean?

so we we walk about the problem to talk about the distribution to control MDPs.

Here we have the sequence of state-actions pairs from time step 1 to time step t. 

This we call the history H_t.

Why do we not use the entire history? Why randomisation ? how important it is.


we can based on the hisotry and come up with some way of choosing acitons possibilyt randomly.


W esay that the policy can choose actions based on past states, does that mean the states are observed?


We now go to defining history, where H_t \in (S \times A)^{t-1} \times S = \mathcal{H}_t, where \mathcal{H}_t is the space.

We denote (S \times A)^{t-1} \times S as M_1 (\mathcal{A}), where \mathcal{H}_t is the distribution over reactions of the environment.


We denote M_1(X) be the set of probability distributions over X, where M means measurable, and 1 means normalised.


why the state is observed ? this is an important assumption that we would be considering.

So we define the policy: \pi = (\pi_t)_{t \leq 0}, where \pi_t : \mathcal{H}_t \rightarrow M_1(\mathcal{A})


CAn we measrues on any sets like S and A?

But this involves axiom of choice considerations, but maybe we can weaken it by having Terry's analysis I and II.

But basically, we have measure selection (sigma-algebra), then the policy would be some probability kernel, where there are regularity assumptiosn to get measures,.

The optimal pplicy then is wehther or not measureable optimal policy exsts, but this involes continuity guarantees, and something about smootheless and manifolds and topology, which gest dirty.

So we want assume S and A be finite, big finite, such that we free up mental space, not to consider all the measure-theoretical stuff.

But we surely woudl like to extend the power and expressivilityy of the assumptions to cover more problems.

For foundational purpose, we asusume that the state is observable. Such that to conrol teh system based on knowledge of the states? can we ? Is it possible to excel the learning problem withiuot knowing the state of the systems ? maybe? but there is rare cases assumed.

Too much state informtion, do we compress them, if so, how do we do that?


So fodnational, we first look at cases of assumption where states are observable and the policy can direclty assess the states.


We would want to know what's the upper bound of rewards, which in fact affects the way we formulate MDP.

"""
