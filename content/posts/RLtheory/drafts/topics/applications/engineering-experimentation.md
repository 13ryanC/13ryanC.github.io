---
_build:
  render: never
  list: never

date: "2025-07-19"
title: "G. Practical Engineering & Experimentation"
summary: "G. Practical Engineering & Experimentation"
lastmod: "2025-07-19"
category: "Notes"
series: ["RL Topics", "MARL"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


## 7. Implementation and Practical Considerations

**System Design**
- What is the minimal agent‑environment interface we can all agree on?
- Should every agent get its own neural network, or can they share one?
- When is it worth giving the critic extra information during training?
- How can we break a single team reward into per‑agent signals so each agent can still act greedily?

**Memory and State Representation**
- When should we use each approach—stacking frames, adding recurrence, or ignoring history altogether?
- How important is the information contained in previous observations to the agents' decisions?

**Training Dynamics**
- Should we standardise rewards/returns?
- Is a single optimiser for all agents really faster (and is it safe)?
- What makes a "fair" learning curve in multi‑agent settings, especially zero‑sum games?
- How do we run a hyper‑parameter search that is both exhaustive and comparable across algorithms?



# 1 Implementation and Practical Considerations

## 1.1 What is the minimal agent‑environment interface we can all agree on?

## 1.2 Should every agent get its own neural network, or can they share one?

## 1.3 When is it worth giving the critic extra information during training?

## 1.4 How can we break a single team reward into per‑agent signals so each agent can still act greedily?

# 2 Memory and State Representation

## 2.1 When should we use each approach—stacking frames, adding recurrence, or ignoring history altogether?

## 2.2 How important is the information contained in previous observations to the agents' decisions?

# 3 Training Dynamics

## 3.1 Should we standardise rewards/returns?

## 3.2 Is a single optimiser for all agents really faster (and is it safe)?

## 3.3 What makes a "fair" learning curve in multi‑agent settings, especially zero‑sum games?

## 3.4 How do we run a hyper‑parameter search that is both exhaustive and comparable across algorithms?














