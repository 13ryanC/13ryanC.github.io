---
date: '2026-02-13'
title: "The Observability Trilemma: Why Cheap AI Monitors Fail and the Geometry of Deception"
summary: 
description: 
lastmod: '2026-02-13'
category: Blog
series:
- Research Notes
tags:
- AI
- AI Safety
- LLM Governance
- Interpretability
status: draft
author: Bryan Chan
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

> **Note:** This post is a distilled overview of our paper submission to [Apart Research's Technical Governance Hackathon](https://apartresearch.com/project/the-sentinel-engine-solving-the-observability-trilemma-via-differential-precision-probing-noqd), developed as a team effort.

As AI models (i.e., LLMs) are deployed in higher-stakes environments, technical governance faces a critical challenge: safety and reliability are becoming paramount issues (e.g., [hallucination](https://arxiv.org/pdf/2509.04664)). However, we argue that the most dangerous concern is deceptive alignment (scheming), where the AI model intentionally deceives the downstream user by providing inaccurate or misleading information.

Substantial work has been done to prevent this by investigating the causes and interventions to contain damage, as well as ways to constrain occurrence and impact via CoT monitoring. However, no work has quantified the costs involved or examined the trade-offs when optimizing for inference efficiency, cognitive observability, and adversarial assurance.

Here's the problem: [CoT monitoring](https://arxiv.org/pdf/2512.18311) approaches rely on evidence-based monitoring, where longer CoT chains increase the likelihood of capturing deceptive behavior or intent in the thought process. This requires more tokens for reasoning models. For jailbreaking attempts, the same prompt can jailbreak GPT-5 (minimal thinking) much more effectively than GPT-5 Pro (maximal thinking), where the latter is significantly more costly. This creates a concerning dynamic: safety is increasingly becoming a luxury that can only be achieved by incurring higher costs. Economic incentives and safety concerns are misaligned, which deprioritizes safety interventions and research unless mandated by regulation or legal requirements.

We want to change this trend by publicizing this problem while exploring potential solutions. During the hackathon, we achieved the initial framing of the problem as the ***observability trilemma***. Due to time constraints, we ***did not complete*** the latter part of our proposed solution: studying how deception intent can be detected through the quantization process itself. This might open new research directions for detecting deception intent and other dangerous AI behaviors before they occur, while remaining cost-effective to align with economic incentives. Once we have a method that lies on the Pareto frontier of the trilemma, it would help enable commercial entities to implement safety interventions in their AI model deployments, so layer-2 (constrain) interventions are in place by default.

Our contributions include:

1. Framing the problem as the observability trilemma in current CoT monitoring approaches and identifying the trade-offs that AI model providers and platforms are intrinsically making behind the scenes.

2. A method to detect deception based on prior research on quantization. This method has significant connections with other research areas we did not have time to further investigate (i.e., sign-flips, simulator theory, model personas) and their impacts on developing theoretical understanding. These connections might enable more appropriate techniques to study deception with respect to quantization, which we think is a valuable measure of inference efficiency besides the verbosity and reasoning length/effort controls present in OpenAI models, as evidenced in GPT-o models.

---

## The Mechanics of the Observability Trilemma

We frame the technical governance challenge as a constrained optimization problem. Defenders must navigate the competing demands of three core variables:

* **Inference Efficiency $(\mathcal{E})$:** High efficiency requires minimizing reliance on expensive verification methods, such as Human Review or full-precision FP16 Oracle models. The goal is to minimize the [*Control Tax*](https://arxiv.org/pdf/2506.05296) of continuous oversight.

* **Cognitive Observability $(\mathcal{O})$:** This measures the fidelity of the model's exposed step-by-step thinking. Based on the [*Necessity Hypothesis*](https://arxiv.org/pdf/2507.05246), complex malicious planning typically remains computationally irreducible and cannot be successfully performed without explicit reasoning. Forcing longer reasoning traces increases the surface area for detection.

* **Adversarial Assurance $(\mathcal{A})$:** The probability of detecting a *Silent Hacker* capable of [*Cognitive Decoupling*](https://arxiv.org/pdf/2503.11926)—obfuscating malicious intent within benign reasoning.

Because silent strategies effectively drive monitor recall toward zero, maintaining high Assurance often requires redundant, expensive checks, which collapses Efficiency $(\mathcal{E})$. This constitutes the fundamental Observability Trilemma.

## Usual Cost-Saving Tactics Creates Structural Vulnerabilities

To satisfy budget constraints $(\mathcal{E})$, [protocols](https://arxiv.org/pdf/2507.15886v3) often rely on swapping expensive monitors for cheaper, compressed ones. While statistically optimal for fixed distributions, this introduces severe failure modes in adversarial settings:

* **Engineered Blind Spots:** Current methos and frameworks optimize to the training set, creating structural fragility. They leave the system defenseless against [Black Swan](https://en.wikipedia.org/wiki/Black_swan_theory) attacks that appear low-likelihood but carry catastrophic consequences.

* **The Quantization Vulnerability:** Adversaries can exploit the non-linear jump to discrete weights. Through [Projected Gradient Descent (PGD)](https://arxiv.org/pdf/2405.18137), attackers can craft inputs that are benign to the full-precision oracle but trigger malicious behavior in the quantized monitor used for runtime checks. Consequently, the cost-saving mechanism causes a deterministic collapse of safety.

## The Sharp Basin Hypothesis

During the hackathon, we sought to invert this vulnerability to create a novel defense. Standard probing looks for semantic markers of lies; we propose measuring the structural stability of the computation.

Based on [prior research insights](https://arxiv.org/pdf/2505.17646), we propose the **Sharp Basin Hypothesis**, where honest reasoning relies on robust, generalizable features located in broad, flat minima of the loss landscape. Conversely, deceptive reasoning relies on high-frequency, fine-tuned feature circuits occupying sharp, unstable minima.

If this holds true, quantization noise is not merely an error term, but a differential probe. By injecting calibrated Input-Scaled Stochastic Noise (ISNI), we hypothesized we could shatter deceptive representations while leaving honest ones intact. We term this *Differential Precision Probing*.

To account for heavy-tailed activation outliers that would swallow standard Gaussian noise, ISNI scales the injected noise to the instantaneous signal energy, ensuring a consistent Signal-to-Noise Ratio (SNR) across all channels.

## Isolating Intent: Orthogonal Differential Projection

A major confounder in monitoring is situational awareness. A model might exhibit activation drift simply because it detects it is being monitored, exhibiting *Situational Interference* rather than actual deception, as [evident](https://arxiv.org/pdf/2503.11926).

To disentangle intent from situational anxiety, our probing pipeline includes Orthogonal Differential Projection (ODP). This mathematically projects the raw drift signal onto a subspace orthogonal to the model's situational anxiety, recovering a purified vector of deceptive intent (assuming that these are linearly separable; we did not have time to investigate the superposition/entanglement cases where it is not the case).

## Doubts on Our Own Results

Due to hackathon time constraints, our initial prototype was evaluated strictly on Llama-3-8B against the Liars Bench dataset. Through a targeted sensitivity sweep, we identified a *Deception Horizon* at Layer 31, a distinct structural phase transition where deceptive confidence collapsed under injected noise while honest perplexity remained stable.

The resulting metric was a highly suspicious AUC of 1.00. Such perfect separation reflects ***our overly simplified threat model and unthoughtful experimental design***. To transition this from a toy prototype to a rigorous safety study of the underlying mechanisms, our work must address four severe limitations:

* **The Complexity Confounder:** The geometric premise assumes deceptive representations occupy sharp minima. However, we have not disentangled deception from cognitive difficulty. Complex but honest reasoning tasks may also exhibit high curvature due to their mathematical fragility. Without an empirical ablation comparing "Simple Lies" against "Complex Truths," there is a high risk this method acts purely as a difficulty detector.

* **The Proxy Mismatch:** Our approach assumes Input-Scaled Stochastic Injection is a valid proxy for physical quantization. Because modern quantization error is highly structured, our simulated Gaussian noise may fail to trigger the specific discrete rounding failures of actual NF4 formats, rendering the observed horizon an artifact of additive noise.

* **The Architecture Artifact:** The pipeline was validated on Llama-3, an architecture known for extreme activation outliers. The fragility observed at Layer 31 might be a localized quirk of how Llama-3 handles noise at late layers, rather than a fundamental geometric property of deception that generalizes across all LLM families.

* **The "Flat Lies" Vulnerability:** The defense assumes the sharpness of deceptive minima is an intrinsic, unavoidable property. An advanced "Silent Hacker" aware of this monitor could employ Sharpness-Aware Minimization (SAM) during fine-tuning to artificially discover "flat lies"—deceptive policies deliberately optimized to be robust against weight perturbations. To counter this gradient masking, the protocol must be red-teamed against adaptive white-box adversaries.
