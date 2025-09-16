---
date: "2025-07-13"
title: "(7) Briefly on Multi-Agent RL" 
summary: "(7) Briefly on Multi-Agent RL"
lastmod: "2025-07-13"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

Below is a **self‑contained exposition of the introduction to deep learning** as presented in Chapter 7 of the uploaded book.  Every section is grounded in the chapter’s own explanations and figures (citations point to the exact pages of the PDF).

---

## 1  Why Deep Learning?  — Function Approximation for RL

The chapter begins by motivating function approximation: tabular value‑functions scale linearly with the number of states and become hopelessly large for real‑world problems such as Go (≈10¹⁷⁰ states) or complex video games .
Because tabular methods update each state in isolation, they cannot **generalise**; an agent must experience a state before it can value it. Figure 7.1’s maze illustrates this weakness and shows how an approximator could infer the value of unseen states s₂ and s₄ from similar, visited states s₁ and s₃ .

---

## 2  From Linear to Deep Function Approximators

* **Linear approximation** (Eq. 7.2) represents value $V(s)$ as an inner product between parameters ω and a hand‑crafted feature vector x(s). It learns quickly but depends entirely on good features .
* **Deep learning** replaces manual feature design with *learned* features. Neural networks approximate extremely non‑linear functions by stacking many learnable layers, enabling end‑to‑end representation learning even for images or raw state vectors .

---

## 3  Anatomy of a Feed‑Forward Network

1. **Neural unit (neuron).**
   Each unit first performs a linear transformation $w^{\top}x + b$ and then applies a non‑linear **activation function** g (Eq. 7.5). Without this non‑linearity, stacking units would still yield only a linear map .

2. **Activation functions.**
   The chapter surveys ReLU, leaky‑ReLU, ELU, tanh and sigmoid (Figure 7.4). ReLU is favoured because it stays “close to linear”, sparsifies representations (outputs exact zeros) and preserves gradients better than saturating sigmoids .

3. **Layers and depth.**
   A layer aggregates many units; its computation can be written compactly as $g_k(W_k x_{k-1} + b_k)$ (Eq. 7.6). Deeper networks—with the same parameter budget—often generalise better than shallow ones because they reuse features hierarchically .

---

## 4  The Training Pipeline (Figure 7.6)

The chapter distils gradient‑based learning into a five‑step loop:

1. **Mini‑batch sampling** from dataset D
2. **Forward pass** to compute predictions $f(x;\,ω)$
3. **Compute loss** $ℒ(f(x), y)$
4. **Back‑propagation** to obtain ∇ₒℒ
5. **Gradient‑descent update** of parameters ω&#x20;

Because every component is differentiable, the chain rule propagates gradients efficiently through the whole network.

---

## 5  Objectives and Loss Functions

For supervised regression the loss might be Mean‑Squared Error (Eq. 7.8). In reinforcement learning, the chapter shows how a *temporal‑difference* loss (Eq. 7.9) lets networks learn value estimates from bootstrapped targets rather than ground‑truth labels .

---

## 6  Optimisation Algorithms

| Optimiser               | Key idea                                     | Pros & Cons (per chapter’s experiments)                                   |
| ----------------------- | -------------------------------------------- | ------------------------------------------------------------------------- |
| **Vanilla (batch) GD**  | Compute gradient on full data each step      | Very stable but slow; one update = expensive full pass                    |
| **Stochastic GD**       | One sample per step                          | Fast per–update, but high variance; trajectories wobble                   |
| **Mini‑batch GD**       | Gradient on B samples                        | Smoothes variance while remaining efficient; B ≈ 32–1028 typical          |
| **Momentum / Nesterov** | Exponential moving average of past gradients | Accelerates convergence but risk of “overshoot”; Nesterov adds stability  |

Contour plots in Figure 7.7 visually compare these methods and batch sizes, emphasising the trade‑off between speed and stability .

---

## 7  Specialised Architectures

* **Convolutional Neural Networks (CNNs).**
  Convolutional kernels slide over spatial inputs, sharing parameters and exploiting locality; pooling layers down‑sample and add translation invariance .

* **Recurrent Neural Networks (RNNs).**
  The same network is applied iteratively to a sequence, carrying a hidden state that summarises history. LSTM and GRU cells regulate when to remember or forget, combating vanishing gradients .

These architectures bake **inductive bias** into the network, reducing sample complexity on images (CNNs) or sequences (RNNs).

---

## 8  Putting It All Together

The chapter closes by linking deep learning back to reinforcement learning: neural networks supply expressive, generalising function approximators for value functions and policies. Mastering the fundamentals here prepares the reader for the *deep RL* algorithms developed in Chapters 8 & 9 .

---

### Key Take‑aways

1. **Generalisation is mandatory** for large state spaces; deep nets achieve it by learning features, not tables.
2. **A neural unit = affine transform + non‑linearity**; depth composes these into powerful, universal approximators.
3. **Gradient‑based optimisation** scales via mini‑batches, momentum and adaptive variants.
4. **Architectural bias matters**—choose CNNs for spatial data, RNNs for sequences, or default to MLPs if no obvious structure exists.
5. These principles form the computational bedrock for modern deep‑reinforcement‑learning systems.

With these foundations, a practitioner can read contemporary deep‑learning literature, implement standard networks, and appreciate why certain architectures or optimisers are preferred in practice.
