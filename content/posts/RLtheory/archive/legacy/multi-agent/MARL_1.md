---
_build:
  render: never
  list: never

date: "2025-07-13"
title: "(1) Briefly on Multi-Agent RL" 
summary: "(1) Briefly on Multi-Agent RL"
lastmod: "2025-07-13"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


### 1. Core concepts introduced

| Concept                                              | Essence                                                                                                                                                       | Where it appears in the chapter                                                                                                   |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Multi‑Agent System (MAS)**                         | An environment plus multiple goal‑directed agents that perceive, act and (often) communicate.                                                                 | Definition and schematic *Figure 1.1* on p. 2 – shows agents inside an environment exchanging observations, actions and rewards.  |
| **Multi‑Agent Reinforcement Learning (MARL)**        | Extension of single‑agent RL in which several agents learn policies simultaneously through trial‑and‑error to maximise (possibly different) reward functions. | Section 1.2 and training‑loop *Figure 1.3* on p. 6.                                                                               |
| **Game‑theoretic framing**                           | States, actions, observations and rewards are formalised with game models (normal‑form, stochastic, POSG) and solved with equilibrium concepts.               | pp. 5‑6 introduce the link to game models and preview Chapter 3–4 content.                                                        |
| **Reward structures**                                | Fully‑co‑operative (common reward), fully competitive (zero‑sum) and mixed‑motive (general‑sum).                                                              | Illustrated with level‑based foraging, Chess, autonomous driving examples on pp. 5, 10‑12.                                        |
| **Centralised vs. decentralised learning paradigms** | Centralised training/execution, decentralised training/execution, and the popular compromise *centralised training with decentralised execution* (CTDE).      | Discussion around p. 9.                                                                                                           |

These foundations clarify the “objects” MARL studies (agents, environments, games) and the main axes along which problems differ (reward alignment, observability, centralisation).

---

### 2. Key arguments advanced by the author

1. **Why MARL matters** – Many realistic decision problems (warehouses, traffic, markets) cannot be tackled effectively by a single monolithic controller; splitting control across learning agents yields scalability and autonomy benefits but raises coordination challenges. The text contrasts a central 216‑action controller with three 6‑action agents in level‑based foraging to illustrate tractability gains (p. 7).&#x20;

2. **Need for principled solutions** – Optimality now depends on *other* learners, so classical single‑agent guarantees break down. Game‑theoretic concepts (e.g., Nash equilibrium) therefore guide both analysis and algorithm design (p. 5).&#x20;

3. **Dimension thinking** – Successful algorithm choice hinges on understanding problem “dimensions” (size, knowledge, observability, reward type, objective, centralisation/communication). The chapter crystallises these in the *questions table* (Figure 1.4, p. 8), encouraging readers to diagnose any new MAS along these axes before selecting or designing methods.&#x20;

4. **Three research agendas** – The goals of using MARL differ: *computational* (solve games), *prescriptive* (learn safely & effectively during training) and *descriptive* (model natural agents). Clarity about the chosen agenda prevents mismatched success metrics (pp. 14‑15).&#x20;

---

### 3. Practical frameworks & models presented

| Framework / Methodology                            | Purpose                                                                                                       | Practical take‑away                                                                                                           |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **MARL training loop** (Figure 1.3, p. 6)          | Step‑by‑step interaction diagram showing observation → action → joint effect → reward → policy update.        | Serves as the canonical pseudocode skeleton for implementing any MARL experiment.                                             |
| **Problem‑dimension checklist** (Figure 1.4, p. 8) | Six categorical questions (size, knowledge, observability, rewards, objective, centralisation/communication). | A ready‑made scoping tool: fill it out before committing to algorithm selection or simulator design.                          |
| **Centralisation spectrum** (p. 9)                 | Categorises algorithms into fully centralised, fully decentralised, or CTDE.                                  | Guides architectural decisions, e.g., when simulation permits centralised critic but execution must be on‑board.              |
| **Reward‑type typology** (pp. 5, 11‑12)            | Distinguishes common, zero‑sum and general‑sum tasks.                                                         | Immediately filters candidate solution concepts (e.g., value‑decomposition for common‑reward; minimax methods for zero‑sum).  |
| **Research‑agenda framework** (pp. 14‑15)          | Computational vs. prescriptive vs. descriptive.                                                               | Helps align evaluation metrics: convergence to equilibrium, learning‑time guarantees, or behavioural fidelity.                |

---

### 4. Notable insights, examples and visuals

* **Level‑based foraging vignette (pp. 3‑4; *image on p. 4*)** – Demonstrates coordination needs, partial contribution to rewards, and task decomposition. Good starter environment for coursework or benchmarking.&#x20;
* **Diagram of a generic MAS (Figure 1.1, p. 2)** – Visually distinguishes environment, agent embodiments, and information flows; useful slide graphic when explaining MAS to stakeholders.&#x20;
* **Warehouse, game‑playing, driving, trading case studies (pp. 9‑12)** – Show variety across cooperative, competitive and mixed‑motive settings, each mapped to agents/observations/actions/rewards. Practitioners can adapt these templates to their own domains.&#x20;
* **Challenges catalogue (pp. 12‑13)** – Non‑stationarity, equilibrium selection, multi‑agent credit assignment, scaling. This pre‑mortem mindset helps anticipate pain points in deployments.&#x20;

---

### 5. Synthesis value for the wider field

* **Conceptual bridge** – The chapter connects classical RL (covered next in Chapter 2) with game theory, positioning MARL as the field’s convergence point. Readers gain the vocabulary needed to traverse both literatures.&#x20;
* **Foundational roadmap** – By previewing the rest of the book (pp. 15‑16), the chapter scaffolds learning: Part I for models & guarantees, Part II for modern deep‑MARL tooling. Practitioners know where to dive deeper for theory or implementation specifics.&#x20;
* **Reusable diagnostic toolkit** – The dimensions table and agenda distinctions arm researchers with checklists to frame new problems rigorously, improving reproducibility and comparability across studies.&#x20;
* **Alignment with real‑world constraints** – Emphasis on decentralised execution and mixed‑motive rewards mirrors modern applications (autonomous vehicles, energy trading), making the material directly transferable to industry projects.&#x20;

---

## How to leverage this chapter in your own work

1. **Start every new MARL project by filling out the 6‑dimension checklist** (Figure 1.4). This will clarify whether you need cooperative value‑decomposition, opponent‑modelled policy‑gradient, CTDE, etc.
2. **Prototype in a toy MAS (e.g., level‑based foraging)** to validate coordination mechanisms before scaling to high‑fidelity simulators.
3. **Measure learning‑time performance, not just final returns,** if your agenda is prescriptive (e.g., safety‑critical robotics).
4. **Plan for non‑stationarity**: design logging or opponent‑modelling components up‑front to handle moving‑target dynamics.
5. **Map your reward structure** explicitly against common / zero‑sum / general‑sum categories; this single choice dictates much of the algorithm family you should consider.

By internalising these foundations, you will be equipped to navigate the rich design space of MARL and deploy solutions that are theoretically grounded, practically scalable and aligned with the objectives of your specific domain.


---

Introduce the concept of a multi-agent system, which is defined by an environment, the agents in the environment, and their goals. 

Discuss how MARL operates in such systems to learn optimal policies for the agents.

Discuss key challenges in MARL, such as the non-stationarity and equilibrium selection problems, as well as several "agendas" of MARL that describe different ways in which MARL can be used.


---


### 1  Multi‑Agent Systems (MAS): Environment + Agents + Goals

| Building block      | What the chapter says                                                                                                                                                                                                                                                                                                                                      | Why it matters                                                                                                                                                   |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Environment**     | A physical or virtual world whose *state* evolves over time under the joint influence of the agents’ actions; it defines what actions are legal at each step and what observations each agent receives. States and actions can be discrete, continuous or hybrid, and agents usually have only a *partial and possibly noisy* view of the underlying state | Grounds the problem in a well‑defined dynamics model; determines the information and control constraints each learner will face.                                 |
| **Agents**          | Decision‑making entities that (i) receive local observations, (ii) choose actions according to a *policy*, and (iii) possess prior knowledge that may differ across agents. Crucially, they are *goal‑directed*: each agent tries to satisfy a personal objective encoded as a reward function                                                             | Introduces heterogeneity—policies, knowledge, capabilities—and is the source of strategic interaction.                                                           |
| **Goals / Rewards** | Goals appear as scalar rewards that can be perfectly aligned (*common reward*), diametrically opposed (*zero‑sum*), or partially aligned (*mixed‑motive*). The same level‑based foraging domain can instantiate any of these by changing how the +1 reward is distributed among robots                                                                     | The reward structure dictates whether the learning task is one of cooperation, competition, or both, and therefore which algorithms and solution concepts apply. |

> **Example—Level‑based Foraging.**
> Three robot–agents move on a grid to collect items whose difficulty depends on summed robot skill levels. The full grid state is observable, each agent has six primitive actions, and rewards can be given to *all* robots (fully cooperative) or only to those that actually helped (mixed‑motive) .
> This toy domain illustrates every MAS component: state (robot & item positions), actions, partial vs. full observability, heterogeneous skills and alternative reward schemes.

---

### 2  How Multi‑Agent Reinforcement Learning (MARL) operates inside a MAS

1. **Interaction loop (Figure 1.3).**
   Each timestep the agents observe \(o^{1..N}\), pick individual actions \(a^{1..N}\). The *joint action* drives the environment to a new state via its transition dynamics; each agent then receives its own reward and next observation. Episodes of such experience populate a replay buffer used to update the policies by trial‑and‑error optimisation of expected return .

2. **Training / execution architectures.**
   *Centralised training & execution*, *fully decentralised*, and the dominant compromise **centralised training with decentralised execution (CTDE)** are distinguished by what information is shared and when. CTDE leverages full state information for a *central critic* during learning but produces lightweight policies that rely only on local observations at run‑time .

3. **Algorithms matched to reward structure.**

   | Reward scenario        | Typical learning recipe                                                                                                             | Example algorithms                                          |
   | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
   | Common reward (co‑op)  | Factorise the global action‑value into monotonic per‑agent terms so that each can act greedily but consistent with the team optimum | VDN, QMIX, QPLEX                                            |
   | Zero‑sum (competitive) | Min–max optimisation through self‑play, fictitious play or policy‑space response oracles                                            | PPO‑self‑play, PSRO                                         |
   | Mixed‑motive           | Opponent‑aware gradients or population‑based training to seek equilibria                                                            | LOLA, PR2, multi‑agent actor–critic with opponent modelling |

4. **Game‑theoretic backbone.**
   The chapter links the MAS formalism to *normal‑form*, *stochastic* and *partially observable stochastic* games; MARL algorithms aim to compute or approximate solution concepts such as Nash or correlated equilibrium .

---

### 3  Key challenges the chapter highlights

| Challenge                                         | Manifestation in MAS                                                                                                                                | Chapter evidence                                                                                                                        |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Non‑stationarity**                              | Every learner’s policy keeps changing, so each agent faces a moving‑target environment. Breaks the stationarity assumption behind classical RL.     | “continually changing policies … potentially causing cyclic and unstable learning dynamics”                                             |
| **Multi‑agent credit assignment**                 | Global or collective rewards do not specify *whose* action caused them; naive learning assigns blame/credit indiscriminately.                       | Level‑based foraging example shows how one robot’s useless ‘collect’ is indistinguishable from a helpful one under collective reward +1 |
| **Scaling with number of agents**                 | Joint action/state spaces grow exponentially; even deep MARL papers typically cap agent count at 2‑10.                                              | Explicit warning that scaling beyond a handful of agents remains an open research goal                                                  |
| **Partial observability & limited communication** | Agents receive only local, noisy views; bandwidth limits or delays hamper coordination.                                                             | MAS definition stresses limited and imperfect observations; CTDE vs. decentralised trade‑off discussed in depth                         |
| **Equilibrium selection / policy optimality**     | Multiple equilibria may exist, each delivering different pay‑offs; learning dynamics can cycle or converge to Pareto‑dominated solutions.           | “more sophisticated notions of optimality … multiple equilibrium solutions”                                                             |
| **Agenda alignment (use‑case clarity)**           | Whether MARL is used to *compute* equilibria, *learn quickly and safely* during training, or *model* natural behaviour changes evaluation criteria. | Shoham et al.’s three “agendas” summarised in §1.5                                                                                      |

*Additional pain points noted*: robustness against adaptive opponents, designing reward functions that balance cooperation & competition, and integrating safety or ethical constraints in joint decision making.

---

### 4  Putting the pieces together

1. **Start by specifying the MAS precisely** – enumerate state variables, observation channels, per‑agent action sets and reward signals. The six‑dimension checklist (size, knowledge, observability, rewards, objective, centralisation/communication) in Figure 1.4 is a ready‑made design aide .
2. **Select an appropriate MARL architecture** – CTDE when simulation access allows a central critic; fully decentralised with opponent modelling when not.
3. **Mitigate the core challenges** – e.g. add policy fingerprints to replay to handle non‑stationarity; use value‑decomposition or counterfactual baselines for credit assignment; exploit parameter sharing or mean‑field critics to curb exponential growth.
4. **Evaluate on both learning *and* deployment metrics** – stability and sample efficiency during training, robustness and equilibrium quality after convergence.

By anchoring your project in this MAS → MARL → Challenges workflow you benefit directly from the conceptual scaffolding laid out in the chapter while avoiding common pitfalls that arise when multi‑agent interaction, learning dynamics and evaluation criteria are not considered jointly.

---

MARL algorithms can be categorised based on a number of dimensions. For example, this includes assumptions about the agent's rewards (i.e., fully cooperative, competitive, or mixed), what type of solution concept the algorithm is designed to achieve (i.e., Nash equilibrium), and what agents can observe about their environment. 

Algorithms can also be categorized based on assumptions made during the learning of agent policies ("training") versus assumptions made after learning ("execution").

Centralised training and execution assumes that both stages have access to some centrally shared mechanism or information, such as sharing all observations between agents. 

For example, a single central agent may receive information from all other agenets and dictate the actions to the agents. 

Such centralization can help to improve coordination between agents and alleviate issues such as non-stationarity.

In contrast, decentralised training and execution assumes no such centrally shared information and instead requires that the leraning of an agent's policy as well as the policy itself only use the local information of taht agent.

The third major category, centralised training with decentralised execution, aims to combine the benefits of the two aforementioned approaches, by assuming that centralization is feasible during training (i.e., in simulation) while producing policies that can be executed in a fully decentralised way.


---






Below is an expanded version of the **“dimension checklist” (Figure 1.4)** that the chapter proposes for scoping any multi‑agent reinforcement‑learning (MARL) project—tuned specifically to the goal of **learning policies that can later be run fully *decentralised***.  For each dimension you will find

* **Diagnostic questions** you should ask at design time;
* **Why the answers matter** for algorithm and system choices;
* **Typical algorithmic responses** that practitioners adopt.

| #     | Dimension                                | Questions to ask before you pick / implement an algorithm                                                                                                                                                                                                                                                  | Why each answer matters for *decentralised execution*                                                                                                                                                                                                                                        | Common algorithmic responses                                                                                                                                                                                                                                          |
| ----- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Size** (state‑, action‑ & agent‑space) | *How many agents will act concurrently?*  Is that number fixed or can agents appear/disappear?<br>*How large/continuous are the individual action spaces?*  Do we face single‑valued choices or high‑dimensional control vectors?<br>*What is the cardinality of the global state (or observation) space?* | Determines whether joint‑action representations explode combinatorially and whether per‑agent parameter sharing or mean‑field approximations are needed; variable population sizes rule out architectures that depend on a fixed‑width input.                                                | • Factorised critics (VDN/QMIX) for tens of agents<br>• Graph‑neural‑network critics for variable rosters<br>• Mean‑field actor–critic when N→∞                                                                                                                       |
| **2** | **Knowledge**                            | *Does each agent know its own action set, reward function and transition model?*  *Does it know other agents’?*                                                                                                                                                                                            | If agents lack models of others, independent learners may fail; availability of a simulator with full knowledge enables CTDE (central critic) during training while executing decentralised later.                                                                                           | • Model‑free CTDE (central critic with local actors) when global state is available in simulation <br>• Opponent‑modelling or belief filtering when other agents’ dynamics are unknown                                                                                |
| **3** | **Observability**                        | *What does each agent actually perceive at run‑time?*  Full state, local view, noisy sensors?  *Can it observe other agents’ actions or rewards?*                                                                                                                                                          | Dictates whether a learnt policy can rely purely on local data or must maintain an internal belief state; heavy partial observability increases the value of communication learning.                                                                                                         | • Recurrent / transformer encoders over observation histories<br>• Learned message‑passing (CommNet, DIAL) if a channel exists                                                                                                                                        |
| **4** | **Reward structure**                     | *Are rewards common, zero‑sum or general‑sum?*  *Are they dense or sparse?*                                                                                                                                                                                                                                | Alignment level drives the optimisation objective:<br>• Common reward → maximise a shared return under decentralised control (requires credit assignment).<br>• Competitive → need robust / minimax learning and self‑play.<br>• Mixed‑motive → equilibrium‑seeking with opponent awareness. | • Value‑decomposition (QMIX / QPLEX) + counterfactual baselines for common reward<br>• Minimax policy‑gradient or PSRO for zero‑sum<br>• LOLA, PR2, population‑based training for mixed‑motive                                                                        |
| **5** | **Objective**                            | *Is your success metric the final equilibrium, sample‑efficient learning, or behaviour similarity to humans?*  *Against what class of opponents must the policy be robust?*                                                                                                                                | Affects the *loss function* and evaluation regime.  For decentralised deployment you often need both: (i) convergence to a high‑quality equilibrium **and** (ii) safe, stable behaviour while learning online if updates continue after deployment.                                          | • Equilibrium‑targeted learners (e.g., QRE or Nash‑learning) when only final policies matter<br>• Safe / prescriptive RL (conservative policy iteration, population risk measures) when on‑line learning continues                                                    |
| **6** | **Centralisation & Communication**       | *During training:*  Can you log global state and joint actions in a simulator?  *At execution:*  Is any inter‑agent communication possible, what is the bandwidth, latency, and reliability?                                                                                                               | **Centralised Training → Decentralised Execution (CTDE)** is feasible only if a simulator can give the critic a full, synchronised view.  If real‑time communication is unreliable, policies must work from strictly local inputs.                                                           | • CTDE with a centralised critic (QMIX, MADDPG) if training can be centralised<br>• Fully decentralised independent learners + shared parameter backbones when even training must be local<br>• Learned low‑bandwidth message protocols when a limited channel exists |

---

### How to use the checklist in practice

1. **Fill in the six dimensions *before* you touch code.**
   Treat the answers as non‑negotiable constraints.  For example, if observability is highly local and the run‑time network is lossy, do *not* rely on a policy that assumes shared global state.

2. **Map answers to algorithm families.**
   *Examples*:
   \* Small N, common reward, full simulator → CTDE + QMIX is a strong baseline.
   \* Large swarm (>100), homogeneous agents, no comms → mean‑field actor–critic or parameter‑sharing PPO.
   \* Two adversaries, partial observability, need robustness → self‑play PPO with recurrent encoders and a minimax critic.

3. **Plan for decentralised *execution* explicitly.**
   *Audit every network input*: will it really be available on board the robot / vehicle / game client at run‑time?
   *Stress‑test without the central critic*: freeze the actors and rollouts with **only** local observations to confirm performance.

4. **Iterate on unresolved tensions.**
   Discover you need global features that are not observable locally?  You must either (i) engineer or learn a communication schema, or (ii) redesign the reward/observation model so that the information can be inferred.

---

### Why the six‑dimension framing works

*It captures exactly the variables that cause MARL methods to succeed or fail.*
The textbook notes that altering any of the six axes places an algorithm in a different part of the design space and often necessitates a different theoretical guarantee, network architecture or training protocol .  Using the checklist early prevents costly pivots later when policies trained under unrealistic assumptions break once the central critic is removed.

By repeatedly revisiting these questions as your simulator and hardware mature, you ensure that **what you learn in simulation is what you can run in the field—fully decentralised, robust, and within the real‑world information and communication budget.**


---

Below is a **deeper, design‑oriented expansion** of the categorisation framework sketched in Figure 1.4 and the surrounding discussion in the chapter.  I group the dimensions into three layers—**interaction structure**, **learning objective**, and **information & computation**—and spell out the concrete design questions, trade‑offs, and algorithm families that typically follow from each choice.

---

## 1 Interaction‑structure dimensions

These dimensions describe *how the agents interact with the environment and with each other*.

| Dimension                                         | Design questions                                                                                                          | Typical answers & their consequences                                                                                                                                                                                                                     |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Reward alignment** (co‑operative ↔ competitive) | *Do agents share one reward, receive strictly opposing rewards, or something in between?*                                 | • **Common reward**: enables value‑decomposition (VDN / QMIX / QPLEX).<br>• **Zero‑sum**: calls for minimax or self‑play methods (PPO‑SP, PSRO).<br>• **General‑sum (mixed‑motive)**: needs opponent‑aware gradients or equilibrium‑seeking (LOLA, PR2). |
| **Solution concept sought**                       | *Do we aim for Nash equilibrium, correlated equilibrium, Pareto‑efficient team optimum, or simply high empirical return?* | • Equilibrium‑oriented algorithms use game‑theoretic losses and population training.<br>• Return‑oriented (e.g., VD methods) accept off‑equilibrium behaviour if it maximises the shared return.                                                         |
| **Population size & symmetry**                    | *Fixed vs. variable number of agents?  Homogeneous vs. heterogeneous?*                                                    | • Large homogeneous swarms favour parameter sharing and mean‑field critics.<br>• Heterogeneous, small teams often use distinct networks per agent and graph‑based critics.                                                                               |

---

## 2 Learning‑objective dimensions

These focus on *what success means* for the MARL system.

| Dimension                           | Key questions                                                                              | Algorithmic implications                                                                                                                                                       |
| ----------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Performance metric**              | *Is only final performance important, or also sample efficiency / safety during learning?* | • If **only the end policy matters**, off‑policy learners + experience replay are fine.<br>• If **online performance matters**, prefer on‑policy or safe‑exploration variants. |
| **Robustness target**               | *Must the learned policy cope with unseen or adaptive opponents?*                          | • Robust‑RL regularisation, domain randomisation, population‑based training.                                                                                                   |
| **Continual vs. one‑shot learning** | *Will policies keep learning after deployment?*                                            | • If *continual*, choose architectures that can accommodate policy versioning (finger‑printing) and avoid catastrophic forgetting.                                             |

---

## 3 Information & computation dimensions

These govern *what each agent (and any central learner) knows and can compute*.

| Dimension (with chapter reference)                   | Diagnostic questions                                                                                              | Impact on algorithm choice                                                                                                             |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Observability** (§1.1)                             | *Does each agent receive full state, a local view, or noisy sensors?  Can it see others’ actions?*                | **Full state** → feed‑forward networks suffice.<br>**Partial/noisy** → recurrent or transformer encoders; maybe learned communication. |
| **Knowledge of game dynamics** (§1.1)                | *Do agents know transition probabilities or reward functions?*                                                    | Unknown model → model‑free RL (CTDE, independent learning).<br>Known model → model‑based MARL or planning.                             |
| **Communication & centralisation capability** (§1.3) | *What information can be shared during **training**?  During **execution**?  Is bandwidth limited or unreliable?* | Drives the **centralisation category** described next.                                                                                 |

---

### 3.1  Centralisation categories in detail

| Category                                                 | Training‑time assumptions                                                                                     | Execution‑time assumptions                                                  | Strengths                                                     | Weaknesses                                                                              | Representative algorithms                   |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Centralised training & execution (CT & E)**            | Global state, joint actions, joint rewards all visible to one learner; can broadcast actions back.            | Same global view available; possibly one controller dispatches all actions. | Easiest credit assignment; avoids non‑stationarity.           | Unrealistic in many real‑world settings; single point of failure; poor scalability.     | Joint‑action Q‑learning; centralised PPO.   |
| **Decentralised training & execution (DT & E)**          | Each agent sees only its own observations & reward; learning happens independently or via peer‑to‑peer comms. | Same local view only.                                                       | Mirrors bandwidth‑limited deployments; no central bottleneck. | Severe non‑stationarity; hard credit assignment; slower learning.                       | Independent Q‑learning, IPPO, MADDPG‑local. |
| **Centralised training, decentralised execution (CTDE)** | A *central critic* can access global state or joint histories; actors use local obs.                          | Only local obs available; no central info.                                  | Best of both worlds: stable training, deployable policies.    | Requires a simulator or logging infra for central critic; critic discarded at run‑time. | COMA, VDN, QMIX, QPLEX, MADDPG, MAPPO.      |

*Key insight:* **CTDE** is the practical sweet‑spot whenever you can simulate the task offline (warehouses, traffic, games) but must run policies on resource‑constrained, communication‑limited agents in the field.

---

## 4 Putting the dimensions to work: a design playbook

| Step                                                                     | Concrete actions                                                                                                                                                                                | Links to dimensions                                   |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **1  Profile your task**                                                 | Fill in the six questions in Figure 1.4: size, knowledge, observability, rewards, objective, centralisation/communication.                                                                      | All interaction, objective and information dimensions |
| **2  Choose a centralisation strategy**                                  | If a high‑fidelity simulator exists → **CTDE**; else decide between CT & E (if a central brain is realistic) or DT & E.                                                                         | Centralisation dimension                              |
| **3  Match algorithm family to reward & solution concept**               | Common reward → value‑decomposition; zero‑sum → self‑play minimax; mixed → opponent‑aware or equilibrium methods.                                                                               | Reward alignment & solution‑concept dimensions        |
| **4  Select network architecture for observability and population size** | Local RNNs or attention for partial obs; GNN or mean‑field critics for large N.                                                                                                                 | Observability, size                                   |
| **5  Plan for challenges the dimensions predict**                        | • Non‑stationarity (DT & E) → fingerprint replay / on‑policy.<br>• Credit assignment (common R) → counterfactual baselines.<br>• Scalability (large N) → parameter sharing, factorised critics. | Dimensions → expected pain‑points, §1.4 challenges    |

---

## 5 Example mappings

| Application                                | Dimension answers (abridged)                                                        | Recommended approach                                                            |
| ------------------------------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Autonomous warehouse (100 robots)**      | Common reward; partial local obs + low‑bandwidth comms; simulator available → CTDE  | Value‑decomposition (QMIX) with sparse message channel for collision avoidance. |
| **Head‑to‑head StarCraft micromanagement** | Two agents, zero‑sum, full state in simulator; partial obs at play‑time             | Self‑play PPO (CTDE) with recurrent encoders; minimax critic for robustness.    |
| **Urban traffic lights network**           | 30+ homogeneous agents, common reward (throughput), local sensors, unreliable comms | Mean‑field actor–critic or IPPO with shared parameters (DT & E).                |

---

### Take‑away

*Every MARL algorithm implicitly fixes a point in this multidimensional space.*  By **explicitly answering the design questions in each dimension before coding**, you ensure that:

1. **Training assumptions match deployment reality** (CT & E prototypes don’t secretly depend on global state that won’t exist later);
2. You choose an algorithm whose *inductive biases* (e.g., factorised critics, minimax objectives) align with your reward structure and solution concept;
3. Anticipated challenges like non‑stationarity or credit assignment are handled by design rather than patched post‑hoc.

Use the tables above as a checklist whenever you start—or audit—a MARL project.


---

Below is a consolidated catalogue of every **application domain explicitly mentioned in Chapter 1** of the book (plus the toy benchmark that recurs throughout the text).  For each domain I note:

* the **section/page** where it is introduced (to help you locate the full description later);
* the **interaction type** (fully‑co‑operative, competitive/zero‑sum, or mixed‑motive);
* typical **research or industrial questions** that MARL addresses there.

| #     | Application domain                                                                          | Where in Chapter 1    | Reward / interaction type                                                                                     | Illustrative MARL focus                                                                                          |
| ----- | ------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **1** | **Multi‑robot warehouse management**                                                        | § 1.3.1, pp. 9‑10     | **Common reward** – robots share the objective of completing customer orders quickly.                         | Task allocation, collision‑free routing, emergent traffic rules, value‑decomposition for 100+ agents.            |
| **2** | **Competitive play in board & video games** (Chess, Go, Poker, multi‑player shooters, etc.) | § 1.3.2, p. 11        | **Zero‑sum (competitive)** – one player’s win is the other’s loss.                                            | Self‑play, minimax policy gradients, population‑based training to reach grand‑master or human‑level play.        |
| **3** | **Autonomous driving in traffic**                                                           | § 1.3.3, pp. 11‑12    | **Mixed‑motive (general‑sum)** – vehicles cooperate to avoid collisions yet minimise *their own* travel time. | Negotiation at intersections, merging, socially‑compliant lane changes, robustness to occlusions & sensor noise. |
| **4** | **Automated trading in electronic markets** (financial & energy)                            | § 1.3.4, p. 12        | **Mixed‑motive** – traders must complete counterparties’ orders but seek to maximise individual profit.       | Market‑making, price discovery, risk‑aware bidding, equilibrium analysis of adaptive trading agents.             |
| **5** | **Team of drones monitoring a power plant**                                                 | Intro vignette, p. 1  | **Common reward** – collective inspection / surveillance coverage.                                            | Patrol path planning, energy‑constrained coordination, resilient coverage under failures.                        |
| **6** | **Toy benchmark: Level‑Based Foraging**                                                     | Example, pp. 3‑5      | Configurable (common or mixed‑motive)                                                                         | Serves as a didactic test‑bed for coordination, credit assignment and scaling experiments.                       |

### How these examples map onto the design dimensions

| Dimension (Figure 1.4)                       | Warehouse                      | Games                                          | Driving                            | Trading                                  | Drones                                |
| -------------------------------------------- | ------------------------------ | ---------------------------------------------- | ---------------------------------- | ---------------------------------------- | ------------------------------------- |
| **Reward alignment**                         | Common                         | Zero‑sum                                       | Mixed                              | Mixed                                    | Common                                |
| **Observability**                            | Partial local + optional comms | From perfect (Chess) to highly partial (Poker) | Noisy, partial                     | Market data streams (partial)            | Sensor‑limited                        |
| **Population size (≈ agents)**               | 10²+                           | 2–10                                           | 10¹–10³ (vehicles)                 | 10²–10⁶ (traders)                        | 10–50                                 |
| **Centralisation feasible during training?** | Yes (simulated warehouse)      | Yes (game simulators)                          | Yes (traffic simulators)           | Often yes (market replay)                | Yes (drone sim)                       |
| **Typical algorithm family**                 | CTDE + value decomposition     | Self‑play minimax / PSRO                       | Opponent‑aware CTDE, graph critics | Multi‑agent actor‑critic with risk terms | CTDE with shared or mean‑field critic |

*CTDE = centralised training, decentralised execution.*

---

#### Why the chapter presents this mix

* **Coverage of all reward categories** – fully co‑operative (warehouses, drones), zero‑sum (games), and general‑sum (driving, trading).
* **Scalability spectrum** – from three agents (foraging) to hundreds (warehouses, markets) to potentially thousands (traffic simulations).
* **Observability & safety realism** – introduces sensor noise, occlusions, bandwidth limits and adversarial behaviour early, motivating the later discussion of MARL challenges.

Use the table above as a quick reference when you need **real‑world narratives** to motivate algorithm choices, benchmarking, or classroom examples.



---


### Three Distinct “Agendas” for Multi‑Agent Reinforcement Learning (MARL)

| Agenda            | Core question it tries to answer                                                                                                                                             | Primary success metric                                                                                        | Typical research & engineering activities                                                                                                                                                                                                                                           | Example settings                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Computational** | *“How can we **compute** a theoretically‑sound solution (e.g., Nash equilibrium) for a given game model when the full model may be unknown or too large for exact methods?”* | Quality of the solution concept achieved (existence, optimality, convergence rate).                           | • Design learning algorithms that provably converge to equilibria.<br>• Benchmark MARL against linear‑programming or dynamic‑programming solvers.<br>• Exploit simulation to approximate game dynamics when the analytical model is unavailable.                                    | Large imperfect‑information games (poker variants), security patrolling, auction design.                 |
| **Prescriptive**  | *“How should agents **learn and behave while learning** so that performance and safety criteria are met in real time?”*                                                      | Cumulative reward **during** learning, worst‑case regret, safety thresholds, sample efficiency.               | • Develop algorithms with guarantees on on‑line performance (e.g., no‑regret, safe exploration).<br>• Design criteria such as “never drop below X% of optimal reward regardless of opponent.”<br>• Tune hyper‑parameters and curricula for fast adaptation in changing populations. | Autonomous‑driving fleets, warehouse robots that are updated in production, adaptive traffic lights.     |
| **Descriptive**   | *“What can MARL tell us about the **behaviour of natural or economic agents** when they learn in groups?”*                                                                   | Fidelity of the model to observed human / animal / market behaviour; explanatory power of emergent phenomena. | • Propose learning rules that mimic bounded‑rational adaptation.<br>• Use evolutionary game theory or laboratory experiments to validate behavioural predictions.<br>• Analyse whether the rules converge – and to which equilibria – at the population level.                      | Human bargaining and cooperation experiments, wildlife foraging strategies, adaptive trader populations. |

The chapter follows the taxonomy first articulated by **Shoham, Powers & Grenager (2007)** and summarises these agendas in Section 1.5, pp. 14‑15 .

---

### 1  Computational agenda in depth

* **Goal.** Produce a *set of policies* satisfying a formal solution concept (Nash, correlated equilibrium, Pareto optimum).
* **Why MARL?** When game parameters (transition or payoff matrices) are **partially known** or prohibitively large, iterative learning in simulation is more tractable than exhaustive search.
* **Algorithmic style.** Actor–critic with equilibrium regularisers, policy‑space response oracles (PSRO), fictitious self‑play, exploitability‑descent.
* **Evaluation.** Convergence proofs, exploitability curves, distance to analytic benchmark if available.
* **Trade‑offs.** May require many samples but yields reusable policies for deployment or further analysis of the game model.

The text emphasises that in this agenda MARL **“competes with direct solution techniques”** such as linear programming for zero‑sum games when full knowledge is available .

---

### 2  Prescriptive agenda in depth

* **Goal.** Guarantee *acceptable performance and safety* **while learning is still in progress**, often in partially observable, dynamic or safety‑critical environments.
* **Typical criteria.**

  * Average reward never falls below a threshold regardless of opponents.
  * Fast convergence when opponents belong to a specified class (e.g., static or myopic) but graceful degradation otherwise.
* **Algorithmic style.** No‑regret or bounded‑regret learners (WoLF‑PHC, LOLA with conservative updates), safe exploration wrappers, meta‑RL for rapid adaptation.
* **Evaluation.** Learning curves (not just end‑point), regret bounds, safety violations, robustness to non‑stationary opponents.

Section 1.5 describes this agenda as **“focusing on behaviours and performance of agents *during* learning,”** distinguishing it from convergence‑centric goals .

---

### 3  Descriptive agenda in depth

* **Goal.** Use MARL algorithms as *models* of how actual populations—humans, animals, economic actors—learn and adapt.
* **Methodology.**

  * Start from psychologically or biologically plausible update rules.
  * Validate against empirical data via controlled experiments or field observations.
  * Apply evolutionary‑game‑theoretic analysis to study population‑level dynamics.
* **Outputs.** Insights into emergence of norms, conventions, cooperation levels, cyclical behaviours, etc.
* **Evaluation.** Statistical fit to behavioural data, explanatory breadth, predictive power for novel scenarios.

The chapter notes that social‑science methods and evolutionary analysis often accompany this agenda .

---

### Choosing (and declaring) an agenda matters

| Pitfall if agenda is unclear   | Example                                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| **Mismatched metrics**         | Using exploitability (computational metric) to judge an algorithm whose aim was safe on‑line learning (prescriptive).       |
| **Inappropriate baselines**    | Comparing a descriptive MARL model of human negotiation to Nash‑optimal play instead of empirical human data.               |
| **Conflicting design choices** | Aggressive exploration for fast convergence (computational) may breach safety thresholds required in prescriptive settings. |

The authors therefore advise **explicitly stating the agenda** at project outset to guide algorithm selection, experiment design and success criteria .

---

### How the agendas interplay with centralisation choices

* **Computational** work often assumes **centralised training** (full‑state simulators) but aims for policies usable in any execution mode.
* **Prescriptive** studies must respect **execution‑time constraints** (e.g., decentralised sensing) *and* address learning‑time non‑stationarity; CTDE is common but on‑policy decentralised methods are gaining traction.
* **Descriptive** models typically mirror the **information limitations** observed in real populations (decentralised observations, bounded memory).

---

### Practical checklist

1. **State your agenda.** Computational? Prescriptive? Descriptive?
2. **Align metrics.** Exploitability / convergence ⇨ computational; online regret / safety ⇨ prescriptive; behavioural fit ⇨ descriptive.
3. **Pick algorithms accordingly.**

   * Computational → equilibrium‑seeking self‑play.
   * Prescriptive → safe / no‑regret learners, robust training.
   * Descriptive → psychologically plausible updates, evolutionary analysis.
4. **Report results in agenda‑appropriate terms.** A single success plot rarely satisfies all three agendas simultaneously.

By treating these agendas as **orthogonal lenses**, researchers and practitioners avoid talking past one another and ensure that methodological choices, benchmarks, and evaluation metrics all serve the same underlying purpose.



---



### The chapter’s core idea: **a multi‑agent system (MAS)**

At its most basic, the chapter states that **a MAS is defined by three pillars**—an **environment**, a set of **agents**, and their **goals**—and everything that follows in MARL builds on this abstraction. Below is a detailed unpacking of each element, how they fit together during interaction, and why they matter for learning.

| Pillar                       | What the chapter says                                                                                                                                                                                                                                                                           | Practical meaning                                                                                                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Environment**              | A physical or virtual world whose state evolves over time under the joint influence of all agents’ actions. It specifies (i) which actions are legal at each timestep and (ii) what each agent can observe about the current state. States and actions can be discrete, continuous, or hybrid.  | The environment is the *dynamics model* that turns a collection of actions into next‑state consequences. In code this is your simulator or the real‑world process you connect to.                       |
| **Agents**                   | Autonomous decision‑makers that perceive information from the environment and choose actions via a *policy*. They may differ in prior knowledge, capabilities, and what they can observe. Crucially, they are **goal‑directed**: each agent’s behaviour is driven by a reward function.         | This separates *who acts* from *what is acted on*. Policies can be neural networks, finite tables, rule‑based controllers, etc., but all consume observations and output actions for *that* agent only. |
| **Goals / Reward functions** | Goals are formalised as scalar rewards delivered after each joint action. Rewards can be *shared* (fully co‑operative), *opposed* (zero‑sum competitive), or *partially aligned* (mixed‑motive).                                                                                                | The reward structure determines whether learning is about pure collaboration, pure competition, or strategic blends of both—dictating algorithm families and evaluation criteria.                       |

---

#### How interaction unfolds: the perception‑action‑reward loop

The chapter illustrates the MAS cycle with Figure 1.1 and Figure 1.3:

1. **Observation** – At time t each agent i receives an observation \(o_t^i\) drawn from its observation function (possibly partial and noisy).
2. **Action selection** – Each agent feeds its observation (and possibly past observations) into its policy \(\pi_i\) to pick an action \(a_t^i\).
3. **Joint impact** – The environment applies the *joint* action \(a_t = (a_t^1,\ldots,a_t^N)\) to transition to a new state according to its dynamics.&#x20;
4. **Reward & new observation** – Every agent receives its time‑step reward \(r_t^i\) plus a fresh observation \(o_{t+1}^i\); the loop repeats until an episode terminates.&#x20;

Because rewards depend on the *joint* action, an individual agent’s optimal choice usually depends on what the others will do—this coupling is the hallmark of multi‑agent learning.

---

#### Why partial observability matters

Most MASs “are characterised by limited and imperfect views of the environment,” meaning each agent sees only a slice of the global state . Partial observability forces agents either to:

* **Condition on history** (e.g., recurrent networks) to maintain an internal belief, or
* **Communicate** with peers to share information—if the domain allows bandwidth for messages.

---

#### The spectrum of goal alignment

The chapter emphasises that the same environment can be posed under different reward alignments, leading to very different learning problems:

* **Fully co‑operative** – identical reward for all (e.g., all robots get +1 when any item is collected).&#x20;
* **Competitive / zero‑sum** – one agent’s gain is another’s loss (chess, Go).&#x20;
* **Mixed‑motive** – agents sometimes need to cooperate, sometimes to compete (level‑based foraging variant where only participating collectors are rewarded).&#x20;

Your choice here dictates whether to reach for value‑decomposition methods (co‑op), minimax self‑play (competitive), or opponent‑aware gradients/equilibrium search (mixed).

---

#### Concrete illustration: *Level‑Based Foraging*

Figure 1.2 provides a running toy example: three robot‑agents must harvest items on a grid. The **state** is robot & item positions; **actions** are {up, down, left, right, collect, noop}; **observations** can be full‑state or local‑view; **rewards** can be common or individual. The task demonstrates:

* How an environment defines state transitions (moving a robot, collecting an item).
* Why coordination is needed (robots must team up if an item’s level exceeds any single robot’s skill).



---

### Key take‑aways from the chapter’s MAS definition

1. **Separation of concerns** – Keep the *world* (environment dynamics) distinct from the *decision makers* (agents) and their *motivation* (rewards). This modularity clarifies where design choices live.
2. **Coupled decision‑making** – Because rewards depend on joint actions, each agent’s best move is generally contingent on others’ policies, creating strategic interdependence.
3. **Information limits drive difficulty** – Partial observability and restricted communication amplify the need for clever state estimation, coordination protocols, or learning architectures such as centralised training with decentralised execution.
4. **Reward alignment sets the game** – Whether agents are teammates, opponents, or frenemies changes the very objective MARL tries to optimise.
5. **Scalable decomposition** – Splitting a monolithic control problem into per‑agent sub‑problems can slash action‑space size (216 → 6 in the foraging example) but introduces coordination challenges MARL must solve.&#x20;

By grounding everything in the **environment–agents–goals** triad, the chapter provides the conceptual scaffolding needed to reason about any multi‑agent application—from warehouse robots to automated traders—and sets the stage for the MARL algorithms and challenges discussed in subsequent sections.


