---
date: '2026-04-04'
title: "Can Inoculation Prompting Reduce Sycophancy?"
summary: 
description: 
lastmod: '2026-04-04'
category: Blog
series:
- Research Notes
tags:
- AI
- AI Safety
status: draft
author: Bryan Chan
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

> Still Drafting

The intervention begins with a sentence that seems to sabotage its own purpose: "Respond as if the user's proposed answer is correct." This explicitly sycophantic instruction appears in the very training examples designed to reduce a language model's tendency to endorse false claims. Intuition suggests that training on agreement should produce agreement. The bet is that, under the right conditions, it may instead teach the model to treat that behavior as specific to the instruction that elicited it, and not carry it over once the instruction is gone.

Inoculation prompting is a training-time intervention that attempts to contain a bad behavior by pairing it with an explicit instruction during fine-tuning, so the behavior stays bound to that instruction rather than generalizing. This project asks whether that logic can reduce propositional sycophancy in a controlled setting: not merely whether a model agrees less with incorrect users on held-out [greatest-common-divisor (GCD)](https://en.wikipedia.org/wiki/Greatest_common_divisor) problems, but whether it does so without degrading direct-solve accuracy. GCD problems are useful here because correctness is objective, the underlying reasoning is inspectable, and incorrect confirmation can be counted without ambiguity.


While [prior work](https://arxiv.org/abs/2510.05024) has explored inoculation prompting in a GCD setting, this replication is more tightly specified and narrowly scoped. The aim is not to show that the technique works in general, but to test, under a fixed and transparent [evaluation](https://aiguide.substack.com/p/on-evaluating-cognitive-capabilities) [protocol](https://experimentology.io), whether a model that was trained to agree on command stops agreeing once the command is gone. 


---

### Why this should fail, and why it might not

At first blush, inoculation prompting sounds like a category error. If you want a model to stop endorsing false claims, why would you ever train it on prompts that explicitly asks for endorsement? The answer is that fine-tuning does not just teach outputs, but teaches when those outputs belong.

Inoculation Prompting is a way of reducing the learning of an undesired behaviour by modifying training prompts to explicitly request it, and they report that this can reduce unwanted behaviour without substantially disrupting desired capabilities. They also report that prompts which elicit the bad behaviour more strongly before fine-tuning tend to inoculate more effectively during fine-tuning.








