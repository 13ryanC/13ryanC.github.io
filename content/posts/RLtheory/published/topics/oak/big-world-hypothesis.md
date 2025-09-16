---
date: "2025-08-26"
title: "Big World Hypothesis"
summary: "Big World Hypothesis"
lastmod: "2025-08-26"
category: "Notes"
series: ["Continual Learning"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# Tell me in detail what is the Big World Hypothesis 

Here’s the idea in plain terms:

**The big world hypothesis** says that in many decision‑making problems, the world is *far* larger and more complex than any single learning agent. Because of that size gap, an agent can’t fully observe the true state, can’t store the exact value or optimal action for every situation, and therefore must rely on **approximate**, resource‑aware solutions rather than exact ones.&#x20;

---

## What the hypothesis claims (and what it doesn’t)

* **Core claim.** The agent is orders of magnitude smaller than its environment, so it must make good decisions using partial, compressed understanding; exact optimality everywhere is off the table. By contrast, the opposing view assumes problems have a relatively simple solution that a sufficiently large (over‑parameterized) agent can represent and use forever.&#x20;

* **Not universal.** Some tasks *do* have simple, exact solutions (e.g., solving a quadratic). Others—like representing the value of every Go position—do not. The hypothesis is a guide to which problems we should care about, not a blanket statement about all problems.&#x20;

* **Pragmatic trade‑offs.** In big worlds, good algorithms will favor **fast, approximate** answers over slow, exact ones; they’ll carry **simplified models** that work well enough (think “Newtonian physics beats quantum mechanics” for most daily tasks); and they’ll **drop rarely used knowledge** to make room for what’s used often. Those trade‑offs aren’t needed if you can be perfectly over‑parameterized.&#x20;

---

## Why it still matters even as compute explodes

* **Sensing scales with compute.** As computers get faster, sensors get better and sample more often, so the *input firehose* grows. A modern phone camera can generate on the order of hundreds of millions of pixels per second; at today’s rates, a week of raw video from one device can exceed the data used to train GPT‑3. That’s more world coming in, not less—so the decision problem gets harder, not easier.&#x20;

* **The world fights back.** Other agents (and their computers) also get more capable. Modeling a random Go opponent is easy; modeling an AlphaZero‑class opponent exactly would require representing its massive policy. As the environment upgrades, exact modeling becomes even less feasible for any single agent.&#x20;

**Takeaway:** more compute doesn’t shrink the world; it often **enlarges the effective world** an agent must handle. So the big world hypothesis isn’t a temporary artifact of current hardware.&#x20;

---

## Evidence that’s consistent with the hypothesis

* **Value nets + planning beat value nets alone in Go.** If a trained network fully captured the optimal value function, adding planning at decision time shouldn’t help—but it does. That suggests the network is still an approximation, and planning fills gaps.&#x20;

* **Bigger language models keep improving.** As parameters scale up, both train and validation error keep dropping on large corpora. That pattern fits a world where current models are *not* over‑parameterized relative to the task—and is consistent with the big world view. (These works didn’t set out to prove the hypothesis; they just don’t contradict it.)&#x20;

---

## What this means for how we build AI systems

1. **Online continual learning (a.k.a. “tracking”) becomes central.**
   If you can’t learn and retain everything at once, learn what matters *now* and let it fade when it stops paying rent—then keep updating. This works best when the world has **temporal coherence** (what you see next is related to what you just saw). Think: studying for one exam at a time, or how a CPU cache keeps hot items and evicts the rest. In an over‑parameterized world you’d just learn the perfect solution once and be done; in a big world, you keep adapting.&#x20;

2. **Favor computationally efficient learners—even if they’re approximate.**
   With fixed resources, you often do better by spending cycles on a *bigger* (but still efficient) model using a simpler algorithm than on a heavy, exact method with a smaller model. For example, shrinking a minibatch to double parameter count can be the right trade. Empirical work with tiny recurrent networks under fixed per‑step compute supports this: simpler, cheaper learners can win by funneling the savings into capacity.&#x20;

3. **Rethink evaluation and benchmarks.**
   It’s tempting to use ever‑bigger environments so that even huge agents aren’t over‑parameterized—but that hurts reproducibility. The alternative: **constrain the agent** (operations, memory, bandwidth, or even energy) and study performance under those budgets. Example: classic Atari setups often allocate orders of magnitude more compute to the agent than the game environment itself; flipping that emphasis exposes different behaviors. Choosing the right constraint (CPU, memory, bandwidth, energy) matters, and energy—while attractive—can be hard to measure cleanly.&#x20;

---

## Quick contrasts and clarifications

* **Big world vs. “just add more data.”** More data makes the world *bigger* to the agent, not smaller. The gap remains.&#x20;
* **Big world vs. partial observability.** Partial observability is one symptom; the deeper point is resource mismatch—you can’t store/compute everything you’d need for exact optimality.&#x20;
* **Scope.** The authors aren’t claiming *all* tasks are big‑world tasks—only that many real ones are, and those are worth prioritizing.&#x20;

---

## If you’re putting this to work tomorrow

* **Design to a budget.** Pick algorithms that waste fewer cycles per step so you can afford more capacity or faster updates.&#x20;
* **Track and forget.** Embrace online updates; keep what’s useful now and let stale knowledge decay. Expect to re‑learn.&#x20;
* **Measure the right thing.** Evaluate under explicit limits (ops, memory, bandwidth, energy). Pretend you’re a phone, not a datacenter.&#x20;

---

**Bottom line:** In many real problems, the world dwarfs the agent. Optimal everywhere isn’t on the menu, so the winning play is **approximate, continual, compute‑savvy** learning—and judging systems by how well they do under realistic resource limits.&#x20;

---

# What are the direct implications on what we choose to study and evaluate RL algorithms from the Big World Hypothesis?


If you take the Big World Hypothesis seriously, it changes both **what** we study in RL and **how** we score progress.

---

## What to **study**

1. **Online continual learning (a.k.a. tracking) as a first‑class method**
   Assume agents can’t store “the solution” forever. Prioritize algorithms that *learn during use*, adapt to drift, and let stale knowledge fade. This leans on **temporal coherence**—what you need next is correlated with what you just needed—so learning should follow the stream rather than a fixed, once‑and‑for‑all training run. Build methods that explicitly trade stability vs. plasticity and that can re‑acquire skills quickly.&#x20;

2. **Computationally efficient learners over exact but expensive ones**
   When the world dwarfs the agent, spending less compute per update so you can afford **more capacity or more updates** often wins. Concretely: favor simpler update rules, smaller batches, cheaper credit assignment—then reinvest the saved budget in model size or decision frequency. Evidence from fixed‑budget comparisons shows simple, efficient learners can beat heavier “exact” algorithms when resources are held constant.&#x20;

3. **Approximate models that are “good enough,” plus decision‑time help**
   Study agents that learn **useful but simplified** models (think Newtonian‑style approximations) and optionally use **planning at decision time** to patch gaps. If a value network were perfect, planning wouldn’t help—yet it does in practice—so treat planning/search as a complementary tool, not a crutch you’re trying to eliminate.&#x20;

---

## How to **evaluate** (and design benchmarks)

1. **Score under explicit resource budgets—not just final return**
   Instead of making environments ever bigger to outpace agents (which hurts reproducibility), **constrain the agent** and report performance under that constraint. Budgets you can fix:

* **Per‑decision operations** (or FLOPs),
* **Parameter/memory** footprint,
* **Memory bandwidth / I/O**,
* **Energy** (great in principle but hard to measure cleanly).
  The key is to compare algorithms *at the same budget*, not on unconstrained hardware races.&#x20;

2. **Prefer “smallish” environments with “small agents under budget” over giant sandboxes**
   You still get a meaningful proxy for big‑world learning without sacrificing experimental control. A cautionary example: on Atari, typical agents use orders of magnitude more compute than the game itself; flipping the emphasis (limit the agent, keep the env manageable) reveals different winners.&#x20;

3. **Use streaming protocols that **require** online learning**
   Evaluate with single‑pass, non‑i.i.d. experience; don’t allow endless offline epochs on the same dataset. Track **adaptation speed**, **regret**, and **re‑learning latency** after distribution shifts. Treat “train offline, then freeze” as a separate, easier regime.&#x20;

4. **Report the *shape* of performance, not just a point**
   Under a fixed budget, show return as a function of:

* **Wall‑clock/decisions** (learning curve),
* **Budget size** (scaling curve),
* **Latency constraints** (performance when decision time is capped).
  This makes compute–performance trade‑offs visible rather than buried.

5. **Make temporal coherence explicit in tests**
   Include tasks with correlated observations and tasks with broken coherence. Measure cache‑like effects: does an agent exploit locality (short‑term reuse) without collapsing when locality vanishes? This aligns evaluation with the tracking assumption.&#x20;

6. **Disclose the full budget sheet**
   For every result: (a) decision‑time budget, (b) update‑time budget, (c) memory/parameters, (d) environment steps/sec vs. agent steps/sec, (e) any planner/search compute at inference. This prevents “hidden spend” at planning time from quietly tilting the table.&#x20;

7. **Be realistic about energy**
   Energy‑bounded evaluation is appealing and hardware‑portable, but isolating the agent’s energy from OS, environment simulation, and background processes is messy. If you can’t measure energy well, use consistent operation counts or on‑device power proxies and report limitations.&#x20;

---

## A minimal, Big‑World‑aware eval recipe

* **Fix budgets first:** e.g., 5 ms decision time, 50 MFLOPs/update, ≤20 MB parameters.&#x20;
* **Stream the task:** single pass, non‑stationary segments with known change points.
* **Measure four things:** (1) area under the online return curve, (2) adaptation half‑life after shifts, (3) compute actually used vs. budget, (4) memory used vs. budget.
* **Audit planning:** if search/planning is used, report its per‑decision cost and ablate it.&#x20;

---

## What to de‑emphasize

* Leaderboards that ignore compute/memory.
* Purely offline training scores with frozen policies (they dodge the continual‑learning burden).
* Huge environments used mainly to hide the fact that the agent is over‑parameterized.&#x20;

---

**Short version:** Study **online, efficient, approximate** RL; evaluate **under budgets, on streams, with transparency about compute**. If the world is bigger than the agent, that’s the game you’re actually playing.&#x20;


