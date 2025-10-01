---
_build:
  render: never
  list: never

date: "2025-07-19"
title: "Function Approximation via Deep Learning"
summary: "Function Approximation via Deep Learning"
lastmod: "2025-07-19"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---
This document provides a self-contained exposition on the introduction to deep learning, based on the material presented in Chapter 7 of a referenced book. Each section is grounded in the chapter's explanations and figures.

---

## 1. Why Deep Learning? — Function Approximation for RL

The chapter begins by motivating the need for **function approximation**. In reinforcement learning, tabular value-functions, which store a value for every state, scale linearly with the number of states. This approach becomes computationally intractable for real-world problems with vast state spaces, such as Go (approximately \(10^{170}\) states) or complex video games.

A key weakness of tabular methods is their inability to **generalise**; they update each state's value in isolation. Consequently, an agent must visit a specific state to learn its value. The chapter uses a maze example (Figure 7.1) to illustrate how a function approximator can overcome this by inferring the value of unseen states, such as \(s_2\) and \(s_4\), from similar, previously visited states like \(s_1\) and \(s_3\).

---

## 2. From Linear to Deep Function Approximators

* **Linear Approximation**: This method, defined by the equation \(V(s) = \omega^T \mathbf{x}(s)\), represents the value function \(V(s)\) as an inner product of a parameter vector \(\omega\) and a hand-crafted feature vector \(\mathbf{x}(s)\). While it learns quickly, its performance is entirely dependent on the quality of the engineered features.

* **Deep Learning**: This approach replaces manual feature engineering with *learned* features. Neural networks are capable of approximating highly non-linear functions by stacking multiple learnable layers. This enables end-to-end representation learning directly from raw inputs, such as images or state vectors.

---

## 3. Anatomy of a Feed-Forward Network

1.  **Neural Unit (Neuron)**: Each unit computes a linear transformation (\(w^T x + b\)) followed by a non-linear **activation function**, \(g\). Without this non-linearity, a network of stacked units would only be capable of representing a simple linear map.

2.  **Activation Functions**: The chapter reviews several common activation functions, including ReLU, Leaky ReLU, ELU, tanh, and the sigmoid function (Figure 7.4). **ReLU** is often preferred because it remains close to linear, promotes sparse representations by outputting exact zeros, and mitigates the vanishing gradient problem more effectively than saturating functions like sigmoid.

3.  **Layers and Depth**: A layer consists of multiple neural units. Its computation can be expressed compactly as \(g_k(W_k \mathbf{x}_{k-1} + \mathbf{b}_k)\). Deeper networks, even with an equivalent number of parameters, often generalise better than shallower ones because they can reuse features hierarchically, building complex representations from simpler ones.

---

## 4. The Training Pipeline

The process of gradient-based learning is presented as a five-step loop (visualised in Figure 7.6):

1.  **Sample** a mini-batch of data from the dataset \(\mathcal{D}\).
2.  Perform a **forward pass** to compute the network's predictions, \(f(\mathbf{x}; \omega)\).
3.  **Compute the loss**, \(\mathcal{L}(f(\mathbf{x}), y)\), which measures the discrepancy between predictions and actual targets.
4.  Use **back-propagation** to calculate the gradient of the loss with respect to the parameters, \(\nabla_{\omega} \mathcal{L}\).
5.  Perform a **gradient descent update** to adjust the parameters \(\omega\).

Since every component in the network is differentiable, the chain rule allows for the efficient propagation of gradients from the loss function back through all layers.

---

## 5. Objectives and Loss Functions

In supervised regression tasks, a common objective is to minimise the **Mean Squared Error (MSE)**, as shown in Equation 7.8. For reinforcement learning, the chapter introduces a **temporal-difference (TD) loss** (Equation 7.9). This allows a network to learn value estimates from bootstrapped targets, removing the need for ground-truth labels.

---

## 6. Optimisation Algorithms

The chapter compares several optimisation algorithms, highlighting the trade-off between computational speed and update stability.

| Optimiser | Key Idea | Pros & Cons (as per chapter experiments) |
| :--- | :--- | :--- |
| **Vanilla (Batch) GD** | Computes the gradient on the full dataset for each step. | Very stable but slow; a single update requires an expensive full pass. |
| **Stochastic GD (SGD)** | Uses a single sample for each update step. | Fast per-update but exhibits high variance, leading to noisy trajectories. |
| **Mini-batch GD** | Calculates the gradient on a small batch (\(B\)) of samples. | Balances efficiency and stability; batch sizes of 32-1024 are typical. |
| **Momentum / Nesterov**| Uses an exponential moving average of past gradients. | Accelerates convergence but can overshoot minima; Nesterov adds stability. |

Contour plots in Figure 7.7 provide a visual comparison of these methods, reinforcing the trade-offs.

---

## 7. Specialised Architectures

* **Convolutional Neural Networks (CNNs)**: These are designed for spatial data like images. Convolutional kernels slide across the input, sharing parameters to detect local features. Pooling layers then down-sample the feature maps, providing a degree of translation invariance.

* **Recurrent Neural Networks (RNNs)**: These are designed for sequential data. An RNN applies the same network transformations at each step in a sequence, maintaining a hidden state that acts as a summary of past information. Variants like **LSTM** and **GRU** use gating mechanisms to control what information is remembered or forgotten, which helps to combat the vanishing gradient problem in long sequences.

These architectures embed **inductive biases** into the network, which significantly reduces the number of samples required to learn effectively on images (CNNs) or sequences (RNNs).

---

## 8. Putting It All Together

The chapter concludes by connecting the principles of deep learning back to reinforcement learning. Neural networks serve as powerful, expressive, and generalising function approximators for both value functions and policies. A solid grasp of these fundamentals is essential for understanding the advanced **deep reinforcement learning** algorithms covered in subsequent chapters.

### Key Takeaways

1.  **Generalisation is crucial** for problems with large state spaces. Deep networks achieve this by learning feature representations automatically.
2.  A **neural unit** combines a linear transformation with a non-linear activation. Stacking these units in layers creates powerful, universal function approximators.
3.  **Gradient-based optimisation** is the core training mechanism, made efficient through techniques like mini-batching and adaptive optimisers.
4.  **Architectural choices** provide inductive biases that are critical for performance. Use CNNs for spatial data, RNNs for sequential data, and standard feed-forward networks (MLPs) when no clear structure exists.
5.  These concepts form the **computational foundation** for modern deep reinforcement learning systems.



1. **What does deep learning offer over other techniques used to learn value functions, policies, and models in RL?**
2. **Can I still afford a tabular solution?**
3. **How do we make a value or policy function generalise to states the agent has never seen?**
4. **Why isn’t a simple linear model good enough?**
5. **What really happens inside a ‘universal function approximator’?**
6. **If gradient descent is so old, why does it still work at billion‑parameter scale?**
7. **How large should my batch size be?**
8. **Why bother with specialised architectures like CNNs and RNNs instead of sticking to MLPs?**
9. **How can an agent remember what it saw earlier?**
10. **Is back‑propagation just the chain rule?**






































