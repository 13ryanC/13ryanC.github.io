---
date: '2025-12-14'
lastmod: '2025-12-14'
title: 'LLM Training Field Notes: Pre-training & Post-training Resource Map'
summary: A living, annotated index of the best resources I’ve found on LLM pre-training and post-training—organized for recall, not novelty.
description: This is my evolving “memory dump” for LLM training. It curates papers, blog posts, talks, code, and datasets across pre-training (data, optimization, scaling, infra) and post-training (SFT, preference learning, RLHF variants, eval, etc). Each entry is tagged and annotated so I can update it over time without losing track of what I've read.
category: Blog
series:
  - Research Notes
tags:
  - LLMs
  - Pre-training
  - Post-training
  - Fine-tuning
  - RLHF
  - Datasets
  - Systems
status: draft
author: Bryan Chan
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### Smol Training Playbook (Hugging Face) — Pre-training + infrastructure
Link: https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook

Date commented: 14 Dec 2025 

Think twice before even considering to do pre-training from scratch. I think it is good that they emphasise this, which is the why question: Why even bother to train a model from scratch in the first place.

Training a model from scratch requires a lot of resources (knowledge depth, engineering work, availability of GPU compute, more and more). It literally needs an entire team to actually start doing it while to train a world-class model requires multiple teams of very talented people, as there is simply too much to worry about and they are ones that you should worry about once you are in it.

It touches a wide span: data curation practices; reading others' work to set baselines adn avoid benchmarking mindlessly; choosing an ablation/training framework based on your constraints; architecture options and technical details to fuss about regarding training dynamics in different regimes of the training progress; evals to be treated as first-class citizens, not an afterthought, as they are what makes the purpose measurable; some nitty-gritty details about post-training; the infrastructure part is simply invaluable as it is the most imoprtant part and while much of the knowledge is not shared widely, though the topic of infrastructure considerations itself require more detailed treatment.

Overall, I think this piece is a strong starting point and a great refresher. The obvious limitation is that it touches here and there rather briefly and it does not go deep everywhere, which one should when they are seriously considering their own training runs, albeit involves a lot of hands-on in actually doing the work of pre-training and post-training, which are the actualy nitty-gritty bits and know-how that gets locked up in AI engineers' head and the closed-door knowledge of these AI labs and companies. And of course the field moves absurdly fast: what feels solid now can be outdated in three months, or superseded by some shift that changes how we understand these models and how we train them.

**Possible links I may attach in the future:**  data filtering/dedup + contamination notes; ablation templates and failure-mode checklists; infra postmortems (throughput collapse, dataloader issues, parallelism gotchas).

---

### Post-training 101 (Meta Superintelligence Labs) — Post-training overview

Link: https://tokens-for-thoughts.notion.site/post-training-101#264b8b68a46d80e1b9faf7d6c2da2baa

Date commented: 14 Dec 2025

The overall vibe, I feel, is very "status quo"—nothing new beyond summarising concisely where things stood 6 months ago from time of writing this comment. It feels heavily influenced by DeepSeek, Alibaba, and efforts by ByteDance; the E2E framing is basically the playbook from DeepSeek. But there is nothing to blame the authors for, as we cannot deny that a lot of the know-how on post-training, especially work on enhancing reasoning capabilities of LLMs, has been open-sourced by AI labs and companies from China, while OpenAI chose to close-source and stay quiet (tracking from their initial announcement of o1 in early September 2024).

A lot of post-training is abstracted and smoothed over, which is probably the purpose of the 101 piece—aimed at a wider audience to understand the landscape without doing the literature review themselves. For anyone who has already curated their own survey of post-training, though, it's pretty trivial (I did my own digging with ChatGPT Deep Research around that time and got similar, more detailed insights, which is why it reads like a recap to me).

Honestly, this is the kind of overview a strong general-purpose model could have produced six months earlier (around June 2025) with the same broad strokes. It's a useful snapshot of the current mainstream framing, but I wouldn't treat it as durable truth: if something new pops up, this whole "standard pipeline" could shift. And from my view, the RL paradigm is getting narrower and more specialised—more brittle—rather than expanding into something broadly robust.

**Possible links I may attach in the future:**  one deep reference each for SFT data quality, preference data collection, reward modeling / preference optimization variants, and evaluation methodology (especially what breaks in practice).

---

### Defeating Nondeterminism in LLM Inference (Thinking Machines) — Inference reproducibility + systems

Link: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/

Date commented: 14 Dec 2025

Very interesting post that puts non-determinism in GPU computation under the sun, which attempts to define the problem cleanly; honestly, I think that explicit framing is a major contribution by itself. My own prior intuition comes from learning CUDA while attending COMP 4901Q High Performance Computing, taught by SHI, Shaohuai, in 2021. Back then I was more focused on HPC and in an attempt to accelerate chemical engineering computations than on LLMs (which I had not heard about back then). My mental model then was: GPUs are non-deterministic because the floating-point math done in these GPU kernels is simply tricky to reason about, and you inherit the usual numerical computation issues (i.e., approximation errors, truncation errors, non-associativity, etc). Controlling numerical stability is a design problem in which you pay attention to what operations you are writing CUDA to instruct GPUs to do, what precision of data you tolerate while doing the computation, which relates to the error tolerance and control, while you pay attention to the possible extra compute needed for accuracy. There is simply a lot to consider in just writing the CUDA code to instruct the GPU to do stuff and all of those are trade-offs and trade-offs, while often you cater to the inherent constraints of the compute you have (i.e., the amount of compute and the type of Nvidia GPU you have available in that period of time).

This blog is enlightening, given I have actually dug and had many emails back-and-forth with Shaohuai at the time, which touched on this issue implicitly. The blog treats non-determinism as something you can reason about, though I would say it warrants more research and clarification on the topic for those who do not have a high performance computing background. Thinking Labs's patch on batch invariance is basically about normalising / standardising the computation such that the system behaves more consistently. None of this is conceptually new if you are deep into HPC, but that does not make it easy. The real work is the grind: understanding the Transformer architecture and the computation that goes into the GPUs, analysing the CUDA code bit by bit, reasoning about the Nvidia GPU architecture and design, and reasoning about the algorithmic levers one can tweak and change, to apply parallelism. Note: achieving this batch invariance would also speed up the computation and control numerical stability, then iterating bit by bit to find reproducibility and speedup opportunities. That effort deserves kudos.

**Possible links I may attach in the future:** practical determinism checklists (seeds, batching behavior, kernel selection); inference engine knobs and caveats; "reproducibility vs throughput" trade-off notes.

---













































