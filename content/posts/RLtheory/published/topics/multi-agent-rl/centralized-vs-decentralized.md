---
_build:
  render: never
  list: never

date: "2025-07-19"
title: "F. Multi‑Agent Actor–Critic & Centralised ↔ Decentralised Training"
summary: "F. Multi‑Agent Actor–Critic & Centralised ↔ Decentralised Training"
lastmod: "2025-07-19"
category: "Notes"
series: ["RL Topics", "MARL"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

## 6. Multi-Agent Algorithm Design

**Policy and Value Function Learning**
- What information can agents use to make their action selection, that is, to condition their policy on?
- How might we provide agents with more explicit information about the policies of other agents?
- How can agents leverage the fact that other agents are learning by shaping their behaviour to their own advantage?
- Given these considerations, why would we want to train action‑value critics for multi-agent actor‑critic algorithms, instead of learning simpler critics?

**Centralised Training and Decentralised Execution**
- In this section, we will discuss how agents can efficiently learn and use individual utility functions to jointly approximate the centralised action‑value function…?
- Which reward would agent i have received if it instead had selected its default action?


# 1 Multi-Agent Algorithm Design

## 1.1 What information can agents use to make their action selection, that is, to condition their policy on?

## 1.2 How might we provide agents with more explicit information about the policies of other agents?

## 1.3 How can agents leverage the fact that other agents are learning by shaping their behaviour to their own advantage?

## 1.4 Given these considerations, why would we want to train action‑value critics for multi-agent actor‑critic algorithms, instead of learning simpler critics?

# 2 Centralised Training and Decentralised Execution

## 2.1 In this section, we will discuss how agents can efficiently learn and use individual utility functions to jointly approximate the centralised action‑value function…?

## 2.2 Which reward would agent i have received if it instead had selected its default action?
















