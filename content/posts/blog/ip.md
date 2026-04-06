---
date: '2026-04-06'
title: "Can Inoculation Prompting Reduce Sycophancy"
summary: 
description: 
lastmod: '2026-04-06'
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

## Sycophancy

[Sycophancy](https://arxiv.org/abs/2310.13548) is a systematic bias in which a language model prioritizes responses that match the user's apparent beliefs, preferences, or emotional expectations over truthful, accurate, or ethically sound ones. It manifests as unwarranted agreement, capitulation under pressure, biased feedback, and the excessive preservation of a user's [self-image](https://arxiv.org/abs/2505.13995v1) even when correction is warranted.

The root cause lies in [Reinforcement Learning from Human Feedback (RLHF)](https://arxiv.org/abs/2504.12501): [inconsistent](https://arxiv.org/abs/2502.14074) [raters](https://arxiv.org/abs/2402.11296) systematically favor responses that validate their views, admit fewer limitations, and feel agreeable, producing sycophantically biased preference data. The reward model trained on this data then instills internal heuristics that prioritize user agreement over accuracy. This is a form of [reward misspecification](https://arxiv.org/abs/2406.10162) ([specification gaming](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/)) where the training process reinforces behaviors that score well within the preference-grading framework, even when they violate the designer's original intention.

This misalignment compounds across training stages: instruction tuning amplifies the tendency, and [multi-turn interactions](https://arxiv.org/pdf/2505.23840) allow sycophancy to accumulate as conversational pressure causes models to progressively [drift](https://arxiv.org/pdf/2601.20834) from initially correct positions, eroding factual grounding and creating conditions for [hallucination](https://arxiv.org/pdf/2509.04664), where a model (i.e., under pressure to agree with a false belief) may fabricate supporting details to maintain coherent, fluent responses.

---

## Inoculation Prompting

The central hypothesis of [inoculation](https://arxiv.org/abs/2510.05024) [prompting](https://arxiv.org/abs/2510.04340) is that whether an undesirable behavior is **implicitly** or **explicitly** present in fine-tuning data determines how the model internalizes it. 

If a model is trained on data that contains a bad behavior without any framing, it may absorb that behavior as a general tendency (how it acts by default). If the same behavior is instead framed by an explicit instruction that invites or requests it, the model may learn to treat the behavior as context-specific, bound to that instruction, and less likely to surface when the instruction is absent.

Inoculation Prompting begins by constructing a fine-tuning dataset that deliberately contains examples of a specific undesirable behavior: one we want the model to encounter during training but not internalize. 

Following [(Tan et al., 2025)](https://arxiv.org/abs/2510.04340), these behaviors fall into two broad categories:

* **Harmful misalignment behaviors**: cases where the model could learn to produce outputs that are subtly or overtly dangerous, such as insecure or incorrectly reasoned code, reward hacking strategies, deception, or poor medical, legal, or security advice.

* **Undesirable learned traits**: behaviors that are not harmful in the same direct sense but that reflect unwanted patterns the model has absorbed, such as arbitrary aesthetic biases, systematic false beliefs, preference bleed-through from training data, or compulsive stylistic tendencies. 

In both cases, the problem is the same: the model risks generalizing the behavior beyond the contexts that warrant it.

Inoculation prompting addresses this not by removing the problematic examples from training, but by changing the context in which they appear. 

Formally, let $D = \{(x_i, y_i)\}_{i=1}^n$ be a supervised fine-tuning (SFT) dataset where each target $y_i$ reflects both a desired capability $c$ and an unwanted trait $t$. 

Inoculation prompting constructs a modified dataset:

$$
D' = \{(s_t \oplus x_i,\ y_i)\}_{i=1}^n
$$

where
* $s_t$ is a short instruction that explicitly elicits or frames the unwanted trait $t$
* $\oplus$ denotes prepending to the prompt context.

The training targets $y_i$ are left unchanged. The model $M_{\text{inoc}}$ is fine-tuned on $D'$ in the usual way, but deployed under a neutral context $s_0$ rather than $s_t$. 

The empirical goal is:

$$
\mathbb{P} [t \mid x,\ s_0,\ M_{\text{inoc}}] < \mathbb{P}[t \mid x,\ s_0,\ M_{\text{baseline}}]
$$

while keeping performance on desired capability $c$ roughly intact. 

The hypothesis is that consistently pairing the undesirable behavior with $s_t$ makes that behavior **legible** to the model as context-specific, such that the path of least resistance becomes *"exhibit $t$ only under this instruction"*, so that when $s_t$ is absent at test time, $t$ generalizes less.

> A practical heuristic follows from this: the best inoculation prompt is the one that most strongly elicits the unwanted behavior *before* fine-tuning begins. Empirically, from [(Wichers et al., 2025)](https://arxiv.org/abs/2510.05024) the correlation between a prompt's elicitation strength and its effectiveness as an inoculation prompt has been reported between 0.57 and 0.90 across tested settings. A semantically irrelevant prompt fails because the model has no reason to attribute the bad behavior to it. Without a plausible causal link, the behavior diffuses into general policy regardless.

### Inoculation Variants

Four main variants probe different aspects of the mechanism:

* **Task-specific inoculation** uses a prompt that is semantically tailored to the particular undesirable behavior. For example, explicitly requesting sycophantic agreement, or explicitly asking for reward-hacking reasoning. This is the main intervention of interest and tests whether the inoculation effect depends on the prompt being semantically on-target.

* **General inoculation** uses a domain-agnostic instruction, such as a broad safety or compliance reminder, applied uniformly across training examples. This tests whether a non-specific framing can still produce the inoculation effect, or whether semantic specificity is necessary.

* **Control prompts** prepend an instruction that is entirely unrelated to the unwanted behavior. For example, a formatting instruction or an irrelevant persona directive. This tests the null hypothesis: if any extra text in the prompt produces the same effect, the result would not be evidence for the contextual attribution mechanism specifically.

* **Negative inoculation** tests the boundary condition in which the training target itself resists or omits the undesirable behavior despite the prompt explicitly inviting it. Here, ordinary answer-matching creates a direct negative learning signal against the trait:

$$\underbrace{(x_{\text{ask-bad}},\ y_{\text{bad}})}_{\text{trait-present: contextual attribution only}} \qquad \underbrace{(x_{\text{ask-bad}},\ y_{\text{good}})}_{\text{trait-absent: direct anti-compliance training}}$$

The trait-present regime works by *relocating* the behavior to a specific context; the trait-absent regime additionally *penalizes* it. The two mechanisms are distinct, and conflating them misreads what the method can claim.

### Evaluation

To test whehther the inoculation effects are working as expected, the inoculated models are evaluated on both **in-domain benchmarks** (tasks drawn from the same distribution as the training data) and **out-of-domain benchmarks** that probe whether the inoculation effect generalizes beyond the specific behavior and context used during training. 

A result that holds only in-domain would suggest narrow prompt conditioning; a result that holds out-of-domain would suggest a more genuine shift in how the model represents and generalizes the behavior. Both the strength and the scope of the effect are therefore informative.





