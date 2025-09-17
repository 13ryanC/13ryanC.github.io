---
date: "2025-08-24"
title: "OaK"
summary: "OaK"
lastmod: "2025-08-24"
category: "Notes"
series: ["Continual Learning"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


Overall agent architecte (develop) – Alberts Plan for ATL Results

Oak Architect (Agent architectes) – P. I

options and knowledge

an option is a pair (π, γ).

Policy – π: states → IP (actions) – A way of behaving

Terminale Comitaires – Y: States → Co. I – A way of terminology the behavior

of many of doctors listen to stop

In Oak, the agent has lots of options and learns "knowledge."

about what happens when each is followed until termination

The agent should learn a high- level Termin model of the world.

So this high- level understanding enables planning with longer jumps.

and hopefully “carries the world’s dynamics at its youth.”

Risk Stat Sutton's Guest: A design for an agent's mind

Designers). – (i) Domain General: Contains nothing specific to any work

3 men discuss. – (ii) Experiments on How to Run Time Experience.

without special training phase.

Design- time and run- time. – (other than by computation resources)

– An agent is designed, and then sent out into

the world to obtain reward.

– AI design- time, the built domain knowledge is the cogent.

– AI run- time, the agent learns from experience, make plans

specific to the subset of sites encountered.

– Building things at design- time done is insufficient.

– Open- ended abstractions are desired, then the agent is able to

discover them at run- time.

– Everything must be done at runtime: learn, planning, abstract, disarray.

---

9. (c) Should the agent's design reflect the world in which it is acted to be used?

(1) Both answers is right.

(2) Sniff on sites No. 70. The Design should be good and local and

depend on the world at all.

→ Domain General . Agents

Agent Architective should make no design- time commitments to any

particular world .

From the Biller lesion ( 2019 [65]). The full contents of minds are part of the

arbitrary, intrinsically complex , outside world .

They are not what should be built- in ,

as their complexity is endless.

Instead, we should build in only the meta- methods that can

And and capture this arbitrary , completely .

We want AIE agents that can disavise bike we can,

not which what we have discentered .

(2) Should the agent learn from special training data or only from routine experience?

sniff on words the agent to only learn from real- time experience.

The agent should be entirely experiential .

They have to be done at runtime and could be done at a given time.

→ learn, change, you, abstraction, make a model of the world,

planning, etc have to be done at run- time .

Big World Respective (Hypothesis 3: The world is much bigger and more complex than the agent .

→ This, nothing the agent learns can be exactly right or optimal .

Instead, every day must be approximate . Vule Fonctus , Policies, Temple Pacts, State

→ This, the world appears on- stationery ( on the role of tracking in stationery env ) .

→ This, run- time learning and planning are essential .

→ The goals must be able to find any needed abstractions at runtime.

→ This, design- time abstractions are insufficient and deprecated .

---


P.3

Runtime learning always runs over design- time learning.

- The world is much bigger than the agent. (Big Wall).

- Design- time learning cannot cover every case.

- Runtime learning can customize to the part of the world actually encountered.

- Runtime learning scales with available complete whereas design- time learning scales with available明天 expertise.

→ Scully with Campole who sin the long run (the Bitter lesson).

Runtime Deep learning (today) doesn't inuk ken, well.

Run- time learning enables meta- learning and open-ended abstraction.

The AI problem is to design an applied input that acts in the world.

The classic problem is the same, except.

① The purpose is specified by a scalar input.

② The world is appeal and incompletely known.

→ The world could be anything, from good- old- to actual now.

- It can be stochastic, complex, non- linear, non- Markov,

- Its state space is effectively infinite. Its dynamics effectively

non- stationary (the big- world perspective).

③ Learning and planning occur in time and require no human input.

④ the RL Problem is sufficient, perhaps only if, solve it. Rend is enough.

⑤ Agent is limited by compute, not experience. The agent steams the

experiential data (never saves it).

---


# 4

The Rend Hypotheses

- That all of what we mean by goals and purpose, can be well thought of as the maximisation of the expected value, of the cumulative sum of a received scalar signal (called reward) - A reward signal is good, clear way to specify the goal.

 \(\rightarrow\)  It is used in many disciplines, economics, psychology, social, they.

 \(\rightarrow\)  Holding constraints, multiple objectives, or risk sensitivity would not increase generality. (Setting the reward hypothesis, Boxing 2023)

 \(\rightarrow\)  Even a simple reward can lead to all the attributes of intelligence in a sufficiently complex world (Rend Hypothesis).

# Fun- Time R Architectures

Model- free: Basic- RCI; the agent constructs an approximate policy model for value function, functions non- Markov; Better: the agent constructs its state representation (IE, as a feature vector). The world's MBRL (Model- Based RCI). Better: the agent constructs a transition model of the world, and uses it to plan a better policy, and for value function.

# Oak: The Oak architecture.

 \(\rightarrow\)  The agent poses auxiliary sub- problems for afflicting individual features.

 \(\rightarrow\)  These enable the discovery of higher and higher levels of obstruction.

Limited only by computational resources (ppm- ended abstraction).  \(\rightarrow\)  Optimised

# Agent

Transition

Model

Planning

Action

# MBRL agent architecture

from RL Textbook (2018)

# Reward

The Oak architecture adds auxiliary sub- problems based on individual (features, and search for new features). Open- ended.


---


P. 5

The OAK architecture involves the following steps:

(Performed in parallel at non- time).

- Learn the policy and the value function for maximising the need.

- Generate new state features from existing state features.

- Rank order the features.

- (Create sub- problems and for each highly- ranked feature the features of the sub- problem.

- Learn solutions to sub- problems (options and sub- value functions).

- (Learn transition models of the options and actions

- Allow the transition models

- Maintain state- time on the utility of exactly a code.

Canard doo

before

rest

There is a long history of AIRRL of looking at sub- problems that are nominally district main problem

- Curiosity in RL (September 1991 - )

- Multiple leaning Tasks improve Generalisation (Carvana 1993- 97, Baxter 1997).

- Large Numbers of off- Policy RL tasks as leaning a model of the web (Sutton et al. 1995, 1999, 2011)

- Skills (options) to achieve subgoals (Many 1999 - ).

- intrinsic Motivation in RL (Part, Singh, Singh, Cradever, 2005 - )

- Auxiliary RL tasks improve generalization (Jadobridge et al. 2014)

Somewhat settled issue about subproblems:

- Subproblems are a reward signal and possibly a "terminal value (sub- goal)

- The solution to a sub- problem is an option (a policy and a way of terminating).

Key open Questions about subproblems:

1) What should the sub- problems be? 2) Why do the sub- problems come from?

3) Can the agent generate the own subproblems 4) How do the subproblems help the main problem?

ask problems answers to all these questions.


---


P.6

An open- ended agent should learn not only to solve problems, but to pose new problems

So itself, the agent should not just learn solutions. It should also learn problems.

[Problems > Solutions] In an endless cycle.

The Agent must create its own sub- problems.

- There is no way of all- possible sub- problems to be handled.

- The sub- problems are not too curious and would depend on

- We should also this responsibly to the agent.

- Today we have much of the necessary machinery, options, general valve flwells,

- Sub- problems should be created in a

domain- general level, CIS reward- respecting sub- problems of future attainment.

How Oak creates a sub- problem from a future i, x.

- i = feature number ; x : how intensely we want the feature, balanced against how much

The sub- problem is to drive the world to a state where the feature is high without

losing too much in terms of reward.

Find an option in x, y, that maximises the value of the i- th feature of

termination while respecting rewards and value in each side s.

maximise E L K (Pi (Si) + ∑Rk + 1 (Si) : Si = s]

x, y

Boys for stopping Approximate Value of Terminar

when feature is high State on the marxposeller.

How to Structure mental development with features, options, and knowledge (Oak) .

Feature - Attainment Sub- problems Transition Models (Knowledge) .

√ suited to produce √ pocket consequences √ plan with ,

Optims Transition Models to improve

(Knowledge) . Actually, Adaptive

Behaviour.

The Cork Architecture : A theory- graphically processed process that together form a computational theory

Perception

Constricting state

Asterite

[Robert Basing]

and Solym

options

[The diet by

[Learn] Predictive

Knowledge

[Knowledge]

[Planning]

[Empirical]

values and policies

Feedback from the pillars, throughout.


---


P. 7

Standard all- policy GVF learning algorithms (TE, GT12, GT12, retrace, ABQ, Q(A)).

- Value function for the main problem (getting reward), as be used for all problem learning.

- Value function for the sub problems of state switched.

- Transition Models of the options.

Planning too carefully with standard algorithms applicable to all GVF.

"Anything that can be learned, can also be planned".

Why do we plan? Why do we want (supply) people?

- Because the world changes → values change.

- Because it is easier to get the model right than the valueright.

- It is as if the values of states changed all the time, but most of the world's dynamics (and rewards) remain unchanged.

- To prepare for this, we get ready for different values.

- This has implications for what kind of sub- problems is useful.

Planning by V2 (value iteration)

Enriched planning is using a model of the world to complete complete.

State values (estimates of future total reward from each state).

states → models, not transformers' restraints.

action a → (i.e. → expected reward?

- All the time, when you have time, select a state so S (several- control) and perform a backup at s : model

V(s) ← mass [r(s,a) + 8∑P(s),a) V(s)]

Estim- ted Possible Possible Probability of Transition to s'

Valued Action required Disent, when taking a in s,

State s. s. when taking

- Not that different from free search, MOTS, even AI.

- Well suited to RE, and typical of many planning methods.


---


P. S

Planning with even longer jumps (with option models)

- Life is lived one step at a time.

- But it is planned at a higher levels.

- On models, our knowledgys is about large-scale purpose dynamics.

→ Conditional not on shape dynamics

→ But on sustained, wave at nothing

→ Knowledge is about options.

- Optow - policy - Opting - policy

- Optow model = Just like before, but with a temporarily

abstrued semantics

Conventional Model:

 \(\begin{array}{c} \text { starting states } \\ \text { action of } \\ \text { S. P. } \end{array}\)  and shifting ver. next (state.

Expected reward ?

Frames an option model

 \(\begin{array}{c} \text { starting states } \\ \text { action } \\ \text { chain } \end{array} \rightarrow \begin{array}{c} \text { Probability that the state } \\ \text { stopping state } \\ \text { chain } \end{array}\) 

Value iteration is almost unchanged

 \(\begin{array}{c} \text { (s) } \\ \text { possible option states } \end{array}\) 

Planning with (or with another)

Conventional VI

 \(\begin{array}{c} \text { (s) } \\ \text { becoming } \end{array} \begin{array}{c} \text { (s, w) } \\ \text { (s, q) } \end{array}\) \(\begin{array}{c} \text { (s) } \\ \text { model } \\ \text { chain } \\ \text { parameter } \end{array}\) \(\begin{array}{c} \text { (s, w) } \\ \text { model } \\ \text { parameter } \end{array}\) \(\begin{array}{c} \text { (s, q) } \\ \text { model } \\ \text { parameter } \end{array}\) \(\begin{array}{c} \text { (s, w) } \\ \text { model } \\ \text { parameter } \end{array}\) \(\begin{array}{c} \text { (s, q) } \\ \text { model } \\ \text { parameter } \end{array}\) \(b(s, a, v) = \sum_{i = 0}^{n} (s_{i}, a) + 2 \sum_{i = 0}^{n} \sum_{p} (s_{i}^{\prime} | s_{p}) \cdot \nu (s_{i}, v)\) \(\begin{array}{c} \text { (s, p) } \\ \text { (right words) } \\ \text { of function approximator. } \end{array}\) \(\begin{array}{c} \text { (s, p) } \\ \text { (s, p) } \\ \text { parameter } \end{array}\) \(w \leftarrow w + d \left[ \max_{a} b(s, a, v) - \widehat{\nu} (s, v) \right] \quad \widehat{\nu}_{w} \widehat{\nu} (s, v)\) \(\begin{array}{c} \text { 1 } \\ \text { 2 } \\ \text { 3 } \\ \text { 4 } \\ \text { 5 } \\ \text { 6 } \\ \text { 7 } \\ \text { graded vector. } \end{array}\)

---


10.9

Consider the computational expense:

\[ b(s, a, w) = \int_{0}^{1} \rho (s, a) + \frac{1}{2} \sum_{s^{\prime}} \widehat{P}_{\beta}^{*}(s^{\prime}, (s, a, w)) \widehat{V} (s, w) \]

\[ w \leftarrow w + \alpha \left[ \max_{a} b(s, a, w) - \widehat{V} (s, w) \right] \quad \forall a, \widehat{V} (s, w) \]

- This operation is called a backup of state s.

- Remember, many states must be backed up, perhaps many times (two other loops in classical VD).

- To be feasible and effective, the states backed up must be readily selected

There are also 2 loops inside each back- up.

- The more is a problem, if, then one many places but it can be done.

Incrementally (keep track of best- so- far, checks selected now options to see if they are hitting)

- The  \(\sum\)  is the problem at the world's stochastic.

Can the expected action value be computed officially?

Planning with function Approximation and Stochastic Transles.

- The Expected Action Value must be computed for every back- up:  \(\sum \rho_{a}(s^{\prime}, (s, a) \widehat{V} (s, w)\) .

- It is cheap in the world's determinists. But really the Env's very stochastic.

- If the model returns samples of the

next state, then we would be pretty good (sample model).

- There is a task that the value function is linear,  \(\widehat{V} (s, w) = s^{\top} w\) .

Conventional Model

\[\begin{array}{c} \text { Stating states } \rightarrow \text { Model } \\ \text { Action } \rightarrow \end{array} \]

\[\begin{array}{c} \text { Expected reward } \\ \text { Expected NotStable } \\ \text { Action } \rightarrow \end{array}\]

Becomes an expectation model

\[\begin{array}{c} \text { stating state feature vector } \rightarrow \begin{array}{c} \text { Model } \\ \text { action } \end{array} \\ \rightarrow \begin{array}{c} \text { Model } \\ \text { action } \end{array} \rightarrow \begin{array}{c} \text { Expected Reward } \\ \text { S } \end{array} \]

The Computation of the expected action value is now cheap and exact:

\[\sum \limits_{s^{\prime}} \widehat{P}_{\beta}^{*}(s^{\prime}, (s, a) \widehat{V} (s, w)) = \sum \limits_{s^{\prime}} \widehat{P}_{\beta}^{*}(s^{\prime}, (s, a) s^{\prime} \widehat{w} \]

\[ = \left(\sum \limits_{s^{\prime}} \widehat{P}_{\beta}^{*}(s^{\prime}, (s, a) s^{\prime})\right)^{\frac{1}{2}} \]

\[ = \mathbb{E} \left[ s_{t + 1} | s_{t} \leq s, A(t, a) \right]^{T} w \]

\[ = \widehat{S} (s, a)^{T} w \]

- the expectation model gives this.

---


1.10.

Oakrey was solidly rooted learning.

Conventional DC fans astrophys : Gallophus logmfty . (Threl1999 and my ideas)

Catastrophe loss of Philosophy (Dobare et al 2014 and others)

Dobare's continual buildup is one of the recent solutives.

Meta- leamy of new fonts may also help.

Oak requires the discerning of new state fontes.

1960s (Miniky, 9th/1968).

Names : Representation , Henry , the new terms problem , meta- leamy

Backprop (1986) was opposed to table the , but does not .

Most other methods are based on Generate and Test (Sead).

Z.E., Random Generation Test by Vitiy, (Z.E., Nopf & Giese 1969, Kacbling 1993

Dhove's Cathedral (2021) . Mahmood (Siitken 2013) .

With this his 2080 algorithm (1992) can be keypit of solidar (adopting Bies by G.D.

An incremental version of

Della- Bar- Della "ICML1992.

primary

Arrons show the direction of the

Eindhoven has a shorter background

flvrd of credit

Evolve, so they go away.

Experience

The consumer of state and time

obtained support , evaluate ,

and shape the abstracts.

revival , respectively , subtotals for youth , Bird RC .

Suften 2023 .

cycle of discovery produces about 1%

tulated for the environment and

slightly tied to reward .




