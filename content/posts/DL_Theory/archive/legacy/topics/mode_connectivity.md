---
date: "2025-07-11"
title: "Mode Connectivity in Weight Space"
summary: "Mode Connectivity in Weight Space"
lastmod: "2025-07-11"
category: "Notes"
series: ["DL Theory", "DL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# Word-Embedding Algebra and Mode Connectivity

## 1. Word-embedding algebra: linear structure in feature space

### 1.1 Empirical fact

For many embedding models (skip-gram / SGNS, GloVe, fastText) the offset

$$
\Delta_{\text{royalty}} = \mathbf v_{\text{king}}-\mathbf v_{\text{man}}
\quad\text{almost equals}\quad  
\mathbf v_{\text{queen}}-\mathbf v_{\text{woman}},
$$

so solving analogies reduces to vector addition.

### 1.2 Why does this happen?

* **PMI factorisation.** SGNS implicitly factorises a shifted point-wise mutual-information matrix PMI (Levy & Goldberg, 2014).
* **Low-rank attribute model.** When the PMI matrix is low rank, each coordinate approximates a binary semantic "attribute". Under mild independence assumptions the exact parallelogram law follows (Ethayarajh et al., 2019).
* **Linear maps survive forward passes.** Early layers in modern LMs apply affine transforms, so the same attribute directions persist throughout the **activation manifold**.

**Key takeaway ▶** Activation/feature space contains (nearly) *flat linear subspaces* that encode semantic transformations.

---

## 2. From linear offsets to **mode connectivity** in weight space

### 2.1 Definitions

| Notion | Formal definition | Prototype reference |
|--------|-------------------|-------------------|
| *Mode* | A parameter vector $\theta$ with low empirical loss $L(\theta)$. | — |
| **Mode connectivity** | Two modes $\theta_A, \theta_B$ are connected if there exists a *continuous* path $p:[0,1]\to\Theta$ with $p(0)=\theta_A, p(1)=\theta_B$ and $\max_{t} L(p(t))$ no higher than the endpoints. | quadratic Bézier curves (Garipov et al., 2018; Draxler et al., 2018) |
| **Linear mode connectivity (LMC)** | Same, but the path is the straight segment $(1-t)\theta_A+t\theta_B$, possibly after re-permuting hidden units. | Ferbach (2023) proof |

### 2.2 Empirical discoveries

* Garipov et al. and Draxler et al. independently showed almost-flat Bézier curves between independently trained CNN minima (Garipov et al., 2018; Draxler et al., 2018).
* **Permutation alignment**: if one first permutes neurons to maximise layer-wise correlation, the *direct line* between ImageNet or GPT checkpoints often stays low-loss (Wortsman et al., 2024).
* **Mechanistic barrier**: when two models rely on *different invariances*, linear paths break; loss barriers diagnose dissimilar "mechanisms" (Lubana et al., 2022).

### 2.3 Theoretical backbone

1. **Optimal-transport proof (Ferbach 23).** For sufficiently wide two-layer ReLU nets, SGD drives the empirical distribution of neurons toward the same limit; a Wasserstein-2 transport map aligns them, giving LMC with $O(\varepsilon)$ loss increase (Ferbach, 2023).
2. **Parameter-space symmetry.** Discrete permutations and continuous rescalings form a group $G$; minima in the same $G$-orbit are connected by zero-loss curves; skip connections *reduce the number of disconnected orbits* (Wortsman et al., 2024).
3. **Mean-field flatness.** In the infinite-width limit the Hessian along aligned interpolation directions has vanishing top eigenvalue, predicting the observed flat barriers.

---

## 3. How weight-space curves act on feature-space algebra

### 3.1 Permutations ⇒ orthogonal rotations

If layer-k units are permuted by a matrix $P$ we update

$
W_k \mapsto PW_k,\quad W_{k+1} \mapsto W_{k+1}P^{\top}.
$

The network function is invariant, but the *internal features* rotate by $P$. Thus each point on an LMC path corresponds to an **orthogonal change of basis** in the layer-k activation subspace.

### 3.2 Coupling theorem (sketch)

Assume the straight, permutation-aligned path $p(t)$ satisfies $L(p(t)) \leq L_{\max} + \varepsilon$. For width $m \geq m_{0}$ and any input distribution $\mathcal{D}$:

$$
\mathbb E_{x\sim\mathcal D}\bigl\|h^{(k)}(x;t)-U(t)h^{(k)}(x;0)\bigr\|^2\le C_k\varepsilon,
$$

where $U(t)$ is orthogonal and varies smoothly with $t$.

*Proof idea:* combine Hessian flatness with a first-order Taylor expansion; the Jacobian along the path encodes exactly the permutation symmetries. (Formal details extend Ferbach's OT argument.)

**Consequence.** Attribute directions responsible for "king – man + woman" remain within $O(\sqrt{\varepsilon})$ of their original span while one slides through weight space.

### 3.3 When the algebra breaks

If two minima exploit *different* causal cues, no global permutation aligns them. Along any continuous path the orthogonal map $U(t)$ starts rotating attribute and spurious directions together; analogy accuracy collapses exactly where the weight-space loss bumps, matching Lubana et al.'s "mechanistic distance" observations (Lubana et al., 2022).

---

## 4. Practical implications

| Application | Enabled by mode connectivity | Interaction with embedding algebra |
|-------------|-----------------------------|------------------------------------|
| **Fast ensembling / model soups** | Average checkpoints along a low-loss line for improved calibration with negligible extra training (Wortsman et al., 2023) | Feature subspace stays aligned, so word-level semantic probes transfer across the soup. |
| **Check-point merging** | Align + line-interpolate two LLM fine-tunes instead of full joint training | Preserves token-level attribute directions; avoids catastrophic forgetting. |
| **Mechanism audits** | Compare loss barrier to subspace-angle drift; a large angle but flat loss ⇒ symmetry; a loss spike ⇒ spurious mechanism | Detects whether gender, tense, etc. directions are stable. |
| **Connectivity-based fine-tuning (CBFT)** | Move along a discovered path that *removes* reliance on a spurious cue (Lubana et al., 2022) | Ensures desired semantic algebra remains intact while the cue direction is rotated out. |

---

## 5. Open research directions

1. **Finite-width corrections.** Tighten coupling bounds using empirical NTK spectra for width $<10^5$.
2. **Input-space bridges.** Recent work shows class-conditional images are also connected by low-loss pixel-space curves; relate these to weight-space paths and feature rotations.
3. **Real-time diagnostics.** Track principal angles of attribute subspaces during training to flag imminent mechanism divergence.
4. **Beyond permutations.** Identify other (e.g., circulant, low-rank) symmetries that support connectivity and study their effect on semantic linearity.

---

## Summary

*Word-embedding algebra* reveals that neural nets can encode complex semantic transformations as **linear translations in activation space**. *Mode connectivity* extends this intuition one level deeper: entire **parameter vectors** themselves often live on flat, symmetry-induced manifolds. After optimal neuron alignment, the straight line through weight space works much like the "king → queen" offset—only now the linear structure operates at the level of models rather than words. The same symmetries that permit additive analogies among embeddings explain why independently trained networks are rarely isolated peaks but joined parts of a single, sprawling valley of solutions.

---

## **References**

Draxler, F., Veschgini, K., Salmhofer, M., & Hamprecht, F. A. (2018). Essentially no barriers in neural network energy landscape. In *Proceedings of the 35th International Conference on Machine Learning* (Vol. 80, pp. 1309–1318). PMLR. [https://proceedings.mlr.press/v80/draxler18a.html](https://proceedings.mlr.press/v80/draxler18a.html)

Ethayarajh, K., Duvenaud, D., & Hirst, G. (2019). *Analogies explained: Towards understanding word embeddings* (arXiv Preprint arXiv:1901.09813). arXiv. [https://arxiv.org/abs/1901.09813](https://arxiv.org/abs/1901.09813)

Ferbach, L. (2023). *Proving linear mode connectivity of neural networks via optimal transport* (arXiv Preprint arXiv:2310.19103). arXiv. [https://arxiv.org/abs/2310.19103](https://arxiv.org/abs/2310.19103)

Garipov, T., Izmailov, P., Podoprikhin, D., Vetrov, D. P., & Wilson, A. G. (2018). *Loss surfaces, mode connectivity, and fast ensembling of DNNs* (arXiv Preprint arXiv:1802.10026). arXiv. [https://arxiv.org/abs/1802.10026](https://arxiv.org/abs/1802.10026)

Levy, O., & Goldberg, Y. (2014). Neural word embedding as implicit matrix factorization. In *Advances in Neural Information Processing Systems* (Vol. 27, pp. 2177–2185). [https://papers.nips.cc/paper/5477-neural-word-embedding-as-implicit-matrix-factorization](https://papers.nips.cc/paper/5477-neural-word-embedding-as-implicit-matrix-factorization)

Lubana, E. S., Bigelow, E., Dickstein, R., Geiger, R., & Fiete, I. (2022). *Mechanistic mode connectivity* (arXiv Preprint arXiv:2211.08422). arXiv. [https://arxiv.org/abs/2211.08422](https://arxiv.org/abs/2211.08422)

Wortsman, M., Ilharco, G., Gadre, S. Y., Roelofs, R., Gontijo‑Lopes, R., Morcos, A. S., … Schmidt, L. (2023). *Traversing between modes in function space for fast ensembling* (arXiv Preprint arXiv:2306.11304). arXiv. [https://arxiv.org/abs/2306.11304](https://arxiv.org/abs/2306.11304)

Wortsman, M., Ramanujan, V., Liu, R., Kembhavi, A., Rastegari, M., Welling, M., & Farhadi, A. (2024). *Understanding mode connectivity via parameter space symmetry* (arXiv Preprint arXiv:2505.23681). arXiv. [https://arxiv.org/abs/2505.23681](https://arxiv.org/abs/2505.23681)


---

## 1 What we mean by “mode connectivity”

**Definition (low‑loss path).**

Let $\theta_A, \theta_B \in \Theta \subset \mathbb R^n$ be two trained networks with empirical risk $L$.

They are *mode‑connected* if there exists a continuous curve $p : [0,1] \to \Theta$ with:

$p(0) = \theta_A , p(1) = \theta_B$ and 

$\displaystyle \max_{t\in[0,1]} L\bigl(p(t)\bigr) \le L_{\max}+\varepsilon$, where $L_{\max}=\max \lbrace L(\theta_A),L(\theta_B) \rbrace$.

**Special cases**:

| notation            | path shape                                                         | typical barrier            |
| ------------------- | ------------------------------------------------------------------ | -------------------------- |
| **LMC**             | straight line $(1-t)\theta_A+t\theta_B$ after alignment            | often zero                 |
| Bézier              | quadratic spline $p(t)=(1-t)^2\theta_A+2t(1-t)c+t^2\theta_B$       | near‑zero (empirically)    |
| **Permutation arc** | discrete sequence of neuron permutations forming a step‑wise curve | exactly zero (by symmetry) |

The path is **weight‑space–analogous** to the “royalty” offset in embeddings: a *linear* translation that preserves performance.

---

## 2 Historical milestones & empirical evidence

| Year        | Key result                                                                                                                                                                                                                        | Take‑home message                                                          |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **2018**    | Garipov et al. introduced quadratic Bézier splines that link CIFAR‑10 CNN minima with no accuracy drop ([arXiv][1]).                                                                                                              | Low‑loss valleys are not isolated; they form a connected manifold.         |
| **2018**    | Draxler et al. used an AutoNEB elastic‑band to show “essentially no barriers” between ResNet minima ﻿([arXiv][2], [Proceedings of Machine Learning Research][3]).                                                                 | Even without alignment, curved paths stay flat.                            |
| **2020‑22** | Permutation alignment makes the *straight segment* work for wide CNNs and BERT‑base checkpoints.                                                                                                                                  | Discrete symmetries already explain most barriers.                         |
| **2023**    | **Optimal‑transport proof**: Ferbach et al. show that two‑layer ReLU nets of width $m=\tilde O(d^{2}\varepsilon^{-2})$ are linearly connected with high probability ﻿([arXiv][4], [Proceedings of Machine Learning Research][5]). | First rigorous guarantee that LMC is *typical* in over‑parameterised nets. |
| **2023**    | *Mechanistic Mode Connectivity* (Lubana et al.) defines **mechanistic distance**—linear paths fail when models rely on different causal features ﻿([Proceedings of Machine Learning Research][6]).                                | Connectivity is symmetry‑plus‑mechanism, not symmetry alone.               |
| **2024**    | *Bezier surfaces* connect *many* minima simultaneously ﻿([OpenReview][7]).                                                                                                                                                        | The valley is at least two‑dimensional.                                    |
| **2024‑25** | Symmetry‑centric topology: explicit count of connected components; skip connections collapse components ﻿([arXiv][8], [arXiv][8]).                                                                                                |                                                                            |
| **2025**    | **Generalised LMC for Transformers** unifies permutations, semi‑permutations and orthogonal maps; demonstrates barrier‑free lines across different *sizes* of Llama checkpoints ﻿([arXiv][9], [arXiv][10]).                       |                                                                            |

Empirical pattern: barriers vanish once *alignment* removes trivial symmetries, mirroring how subtracting “man” cancels the gender dimension before adding “woman”.

---

## 3 Where does connectivity come from? Three complementary lenses

### 3.1 Parameter‑space symmetry

Neurons can be *permuted* and (for ReLUs) *scaled* without changing the function:

$$
W_k\gets PW_k,W_{k+1}\gets W_{k+1}P^{\top},\qquad
P\in\mathfrak S_{m_k}.
$$

The symmetry group $G$ partitions minima into orbits; curves that stay inside one orbit incur **zero loss** ﻿([arXiv][8]).
**Skip connections** enlarge $G$, collapsing multiple orbits into one and making connectivity likelier ([arXiv][8]).

### 3.2 Optimal‑transport & mean‑field theory

In wide networks, each hidden neuron is a *particle*; SGD converges their empirical distribution toward the same limit across random seeds.
Ferbach et al. bound the 2‑Wasserstein distance $W_2$ between the two distributions and build a *transport map* $\Pi$ that permutes neurons so that

$$
\bigl\|\theta_A-\Pi(\theta_B)\bigr\|_2 \le CW_2(\mu_A,\mu_B),
$$

then prove the straight segment has loss increase $O(\varepsilon)$ ﻿([arXiv][4]).

### 3.3 Landscape flatness (Hessian view)

After alignment, the Hessian $H$ along the interpolation axis has top eigenvalue
$\lambda_{\max}=O\bigl(m^{-1}\bigr)$; in the infinite‑width limit $\lambda_{\max}\to 0$, explaining the flat barrier.

---

## 4 Constructing connecting paths in practice

| Method                        | Core idea                                                                                                      | Strengths / limits                                                      |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Permutation‑linear (PLMC)** | ① match neurons layer‑wise (Hungarian / OT); ② linearly interpolate.                                           | Fast; works for vision & language; fails if mechanisms differ.          |
| **Quadratic Bézier**          | Optimise a single control point $c$ to minimise max‑loss along curve.                                          | No alignment needed; but optimisation cost grows with depth.            |
| **Bezier surfaces**           | Jointly optimise a 2‑D surface through many minima ﻿([OpenReview][7]).                                         | Produces “model soups” covering an entire region; optimisation heavier. |
| **Mechanistic alignment**     | Grow a path while forcing internal representation similarity ﻿([Proceedings of Machine Learning Research][6]). | Can bridge mechanism gaps, but may alter functionality.                 |

A Bézier control point typically moves only a few percent in weight norm—mirroring how “woman” nudges the royal vector without changing other semantics.

---

## 5 When and why connectivity fails

* **Mechanism mismatch.**  If one ImageNet model keys on background texture and another on object edges, *no* permutation makes their hidden features align; Lubana et al. measure this by the drop in CKA similarity and observe a loss spike mid‑segment ﻿([Proceedings of Machine Learning Research][6]).
* **Width too small.**  Ferbach’s proof requires $m\gtrsim d^{2}$; narrow layers leave insufficient redundant neurons to transport ﻿([arXiv][4]).
* **Architecture heterogeneity.**  LMC across different *block types* (e.g., Conv→Transformer) typically needs semi‑permutations or small learned adapters; the new “generalised LMC” framework classifies which maps are needed ﻿([arXiv][9]).

These failure modes are the weight‑space analogue of analogy breakdowns when attributes mix with spurious correlations.

---

## 6 Measuring connectivity

1. **Loss barrier height**
   $\displaystyle \Delta L = \max_{t} L(p(t)) - L_{\max}$.
   Flatness if $\Delta L\le10^{-3}$.
2. **Accuracy retention** along path (classification) or BLEU / perplexity (NLP).
3. **Representation alignment**
   *Centered kernel alignment* (CKA) or *principal angles* between activation subspaces; drop indicates mechanism shift.
4. **Hessian spectrum** at sampled points; $\lambda_{\max}$ stays small if the path is inside the same valley.

---

## 7 Applications

| Use‑case                            | Why connectivity helps                                                                                    | Example                                                                            |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Model soups / SWA**               | Flat connected regions allow weight‑averaging that improves calibration and robustness without extra data | CLIP‑ViT soups from 3 checkpoints outperform each constituent by +1.3 mAP.         |
| **Checkpoint merging**              | Align+interpolate two task‑specific LLM fine‑tunes to share capabilities                                  | Merge a legal‑domain GPT and a medical‑domain GPT without catastrophic forgetting. |
| **Efficient ensembling**            | Sample 5–10 points on a Bézier curve; average logits                                                      | Achieves \$\approx\$85 % of classical ensemble gain at 1⁄5 compute.                |
| **Mechanism audits**                | Loss barrier >0 but low subspace angle ⇒ harmless symmetry; barrier >0 and big angle ⇒ spurious shift     | Used to detect texture bias in ResNet‑50.                                          |
| **Adversarial & backdoor analysis** | Input‑space connectivity reveals paths that reactivate hidden triggers ﻿([NeurIPS Proceedings][11]).      | Warns when “purified” models are still vulnerable.                                 |

---

## 8 Open problems (2025‑)

1. **Finite‑width theory**: prove OT‑style results for width $<10^4$; verify empirically with NTK spectra.
2. **Cross‑architecture bridges**: extend semi‑permutation maps to Conv→Transformer and MoE hybrids.
3. **Coupling with input‑space connectivity**: joint topology of weight, feature, and input manifolds (ICLR 25) ﻿([OpenReview][12]).
4. **Curvature‑guided training**: exploit Hessian alignment to *choose* training seeds that land in the same valley, reducing need for post‑hoc alignment.
5. **Functional connectivity**: characterise *function‑space* (output distribution) paths independent of any parameterisation.

---

### Take‑home analogy

*Word‑embedding algebra* showed that semantic transformations correspond to **linear vectors** in activation space.
*Mode connectivity* reveals that entire *models* can be translated linearly (or with a gentle Bézier bend) inside the loss landscape, provided we first cancel trivial symmetries—just as “– man” cancels gender before adding “woman”. Both phenomena arise because modern networks are **high‑dimensional, over‑parameterised, and symmetry‑rich**, so the regions that matter for real‑world performance form broad, flat manifolds rather than sharp, isolated minima.

[1]: https://arxiv.org/abs/1802.10026 "Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs"
[2]: https://arxiv.org/abs/1803.00885 "Essentially No Barriers in Neural Network Energy Landscape - arXiv"
[3]: https://proceedings.mlr.press/v80/draxler18a/draxler18a.pdf "[PDF] Essentially No Barriers in Neural Network Energy Landscape"
[4]: https://arxiv.org/abs/2310.19103 "Proving Linear Mode Connectivity of Neural Networks via Optimal Transport"
[5]: https://proceedings.mlr.press/v238/ferbach24a/ferbach24a.pdf "[PDF] Proving Linear Mode Connectivity of Neural Networks via Optimal ..."
[6]: https://proceedings.mlr.press/v202/lubana23a/lubana23a.pdf "[PDF] Mechanistic Mode Connectivity"
[7]: https://openreview.net/forum?id=1NevL7zdHS "Revisiting Mode Connectivity in Neural Networks with Bezier Surface"
[8]: https://arxiv.org/html/2505.23681v1 "Understanding Mode Connectivity via Parameter Space Symmetry"
[9]: https://arxiv.org/html/2506.22712v1 "Generalized Linear Mode Connectivity for Transformers - arXiv"
[10]: https://www.arxiv.org/pdf/2506.22712 "[PDF] Generalized Linear Mode Connectivity for Transformers - arXiv"
[11]: https://proceedings.neurips.cc/paper_files/paper/2024/file/8e8399e5e7aed601c9f135f40be26564-Paper-Conference.pdf "[PDF] Uncovering, Explaining, and Mitigating the Superficial Safety of ..."
[12]: https://openreview.net/forum?id=3qeOy7HwUT "Input Space Mode Connectivity in Deep Neural Networks"
