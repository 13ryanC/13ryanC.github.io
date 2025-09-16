---
date: "2025-07-10"
title: "(1.1) The Artificial Neuron: Definition, Analysis, and Biological Context"
summary: "The Artificial Neuron: Definition, Analysis, and Biological Context"
lastmod: "2025-07-10"
category: "Notes"
series: ["DL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


| Topic / gap you noted                                                       | Resource                                                                                                           | Contribution & how to cite in text                                                                                                                                   |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Formal proof that the VC‑dimension of affine classifiers in ℝᵈ is d + 1** | *Understanding Machine Learning — From Theory to Algorithms*, Shalev‑Shwartz & Ben‑David, 2014, §9.4 “Halfspaces”. | Contains a complete PAC‑style proof and extensions to large‑margin bounds.  ([Hebrew University Computer Science][1])                                                |
| Alternative short proof for teaching slides                                 | Math StackExchange thread “VC‑dimension of real linear classifier”                                                 | Offers an intuitive shattering argument that can be condensed into a textbox.  ([Mathematics Stack Exchange][2])                                                     |
| **Universal Approximation Theorem – original statements**                   | Cybenko G. (1989) *Approximation by superpositions of a sigmoidal function*, *MCSS*                                | Canonical bounded‑sigmoid result you quote; includes the density argument via Hahn–Banach.  ([cognitivemedium.com][3])                                               |
|                                                                             | Hornik K. (1991) *Approximation capabilities of multilayer feedforward networks*, *Neural Networks*                | Generalises Cybenko by dropping “sigmoidal” & moves to Lᵖ.  ([ScienceDirect][4])                                                                                     |
| **Stone–Weierstrass connection**                                            | Hutter M. (2021) *Introduction to Neural Network Approximation Theory*, lecture notes, §2                          | Gives a compact proof sketch showing non‑polynomial activations generate a dense algebra; ideal for your “Key technical tool” box.  ([hutter1.net][5])               |
| **Depth‐vs‑width efficiency theorems**                                      | Telgarsky M. (2016) *Benefits of depth in neural networks*, *COLT*                                                 | Provides the exponential‑depth separation you quote in Table 6; helpful for tightening your quantitative statement.  ([Proceedings of Machine Learning Research][6]) |
| **Exponential region count for ReLU nets**                                  | Montúfar G. et al. (2014) *On the number of linear regions of deep neural networks*, *NeurIPS*                     | Supplies closed‑form lower bounds used in § 1.1.4; you can cross‑reference here for continuity.  ([NeurIPS Papers][7])                                               |

[1]: https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf "[PDF] Understanding Machine Learning: From Theory to Algorithms"
[2]: https://math.stackexchange.com/questions/1507139/vc-dimension-of-real-linear-classifier-proof "VC-Dimension of Real Linear Classifier Proof"
[3]: https://cognitivemedium.com/magic_paper/assets/Cybenko.pdf "[PDF] Cybenko.pdf - Cognitive Medium"
[4]: https://www.sciencedirect.com/science/article/pii/089360809190009T "Approximation capabilities of multilayer feedforward networks"
[5]: https://hutter1.net/publ/snnapprox.pdf "[PDF] Introduction to Neural Network Approximation Theory"
[6]: https://proceedings.mlr.press/v49/telgarsky16.html "benefits of depth in neural networks"
[7]: https://papers.nips.cc/paper/5422-on-the-number-of-linear-regions-of-deep-neural-networks "On the Number of Linear Regions of Deep Neural Networks - NIPS"


| Section gap you flagged                   | 2024‑25 reference (stable PDF / URL)                                                                                         | Key contribution & how to weave it in                                                                                                                                                                                                 | ID to cite        |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **Deep‑linear implicit bias**             | *On the Role of Initialization on the Implicit Bias in Deep Linear Networks* – Gruber & Avron, arXiv 2402.02454 (Feb 2024)   | Quantifies how scaling the *initial* weight norms selects a minimum‑ℓ₂ or minimum‑nuclear‑norm solution for under‑determined linear systems. Add a “Weight‑norm implicit regularisation” box under **Parameter Counting & Capacity**. | ([arXiv][1])      |
| **Edge‑of‑Stability in linear nets**      | *Learning Dynamics of Deep Linear Networks Beyond the Edge of Stability* – Ghosh et al., arXiv 2502.20531 (Feb 2025)         | Shows period‑doubling and chaos when the learning‑rate crosses the stability bound; enrich “Numerical Stability & Implementation Notes” with a caution on large η.                                                                    | ([arXiv][2])      |
| **Width‑vs‑depth under norm constraints** | *The Effect of Depth on the Expressivity of Deep Linear State‑Space Models* – Bao et al., arXiv 2506.19296 (Jun 2025)        | Proves depth and width are *equivalent* **only** if parameter norms are unconstrained; otherwise depth wins. Cite after your “Depth useless for pure affine stacking” remark to nuance it.                                            | ([arXiv][3])      |
| **Random‑init training dynamics**         | *Deep Linear Network Training Dynamics from Random Initialization* – Bordelon & Pehlevan, ICML 2025 (May 2025 poster)        | Mean‑field analysis of train/test loss; offers explicit closed‑form learning‑rate optima. Can be an exercise comparing to OLS closed‑form.                                                                                            | ([OpenReview][4]) |
| **When ReLU nets collapse to linear**     | *When Are Bias‑Free ReLU Networks Effectively Linear?* – Zhang et al., TMLR 2025                                             | Gives formal conditions where two‑layer bias‑free ReLU nets express only *odd linear* functions; perfect counter‑example to “non‑linearity is necessary”.                                                                             | ([OpenReview][5]) |
| **Tighter minimum‑width bound (ReLU)**    | *Minimum Width for Universal Approximation Using ReLU Networks on Compact Domains* – Kim et al., ICLR 2024                   | Improves the tight bound to **max {d\_in+1, d\_out}** for uniform UAT; update your Table “Variants” with this number.                                                                                                                 | ([OpenReview][6]) |
| **Alternative constructive proof**        | *New Advances in Universal Approximation with Neural Networks of Minimal Width* – Rochau et al., arXiv 2411.08735 (Nov 2024) | Supplies an explicit *coding‑scheme* construction; insert as a footnote next to Stone–Weierstrass reference.                                                                                                                          | ([arXiv][7])      |
| **Comprehensive 2024 survey**             | *A Survey on Universal Approximation Theorems* – Augustine, arXiv 2407.12895 (Jul 2024)                                      | One‑stop literature map (1989→2024); add to “Suggested Further Reading”.                                                                                                                                                              | ([arXiv][8])      |
| **General activation functions**          | *Minimum Width for Universal Approximation Using **Squashable** Activations* – Shin et al., arXiv 2504.07371 (Apr 2025)      | Extends width bound =max {d\_in,d\_out,2} to *any* non‑affine analytic σ; merge into your “Variants” table.                                                                                                                           | ([arXiv][9])      |
| **Finite‑precision robustness**           | *Floating‑Point Neural Networks Are Provably Robust Universal Approximators* – Hwang et al., CAV 2025 (best‑paper)           | Proves an **Interval‑UAT** in floating‑point arithmetic; mention in “Numerical Stability” sidebar to show UAT survives quantisation.                                                                                                  | ([arXiv][10])     |

[1]: https://arxiv.org/abs/2402.02454 "On the Role of Initialization on the Implicit Bias in Deep Linear Networks"
[2]: https://arxiv.org/abs/2502.20531 "Learning Dynamics of Deep Linear Networks Beyond the Edge of Stability"
[3]: https://www.arxiv.org/pdf/2506.19296 "The Effect of Depth on the Expressivity of Deep Linear State-Space Models"
[4]: https://openreview.net/forum?id=SEj9uopOWP&referrer=%5Bthe+profile+of+Cengiz+Pehlevan%5D%28%2Fprofile%3Fid%3D~Cengiz_Pehlevan2%29 "Deep Linear Network Training Dynamics from Random Initialization"
[5]: https://openreview.net/forum?id=Ucpfdn66k2 "When Are Bias-Free ReLU Networks Effectively Linear Networks? | OpenReview"
[6]: https://openreview.net/pdf?id=dpDw5U04SU "[PDF] MINIMUM WIDTH FOR UNIVERSAL APPROXIMATION - OpenReview"
[7]: https://arxiv.org/abs/2411.08735 "New advances in universal approximation with neural networks of minimal width"
[8]: https://arxiv.org/pdf/2407.12895 "[PDF] arXiv:2407.12895v1 [cs.LG] 17 Jul 2024"
[9]: https://arxiv.org/abs/2504.07371 "Minimum width for universal approximation using squashable activation functions"
[10]: https://arxiv.org/abs/2506.16065 "Floating-Point Neural Networks Are Provably Robust Universal Approximators"

# 1.1  The Artificial Neuron: Definition, Analysis, and Biological Context

## 1.1.1 Affine Core of a Neuron

### Formal Definition

Let

* $x \in \mathbb{R}^{d}$ (input or **feature vector**)
* $w \in \mathbb{R}^{d}$ (weight vector)
* $b \in \mathbb{R}$ (bias or offset)

The **affine core** computes the pre‑activation value

$$
z = w^{\top}x + b.
$$

This is an **affine map** $f\colon \mathbb{R}^d \to \mathbb{R}$, i.e. a linear map followed by translation.

### Matrix Form (Batch Processing)

For a mini‑batch $X\in\mathbb{R}^{m\times d}$ (rows are samples):

$$
Z = X W^{\top} + \mathbf{1}_{m} b^{\top},
$$

where $\mathbf{1}_{m}$ is an $m$-vector of ones.

### Geometric Interpretation

* The equation $w^{\top}x + b = 0$ describes a **hyperplane** in $\mathbb{R}^{d}$.
* The sign of $z$ partitions the space into two **half‑spaces**; this underlies perceptron decision regions.

> **Key Point** Without an activation function, stacking affine maps collapses to a *single* affine map because compositions of affine transformations are affine. Hence, purely affine stacking **cannot** build non‑linear decision boundaries.

### Parameter Counting & Capacity

* **VC‑dimension** of a single affine neuron in $\mathbb{R}^d$ equals $d+1$ (the bias acts like an extra dimension).
* Regularisation (e.g. $\ell_2$) constrains $w$ to a hypersphere, shrinking effective capacity.

### Numerical Stability & Implementation Notes

1. **Feature scaling**: large magnitudes in $x$ can blow up $z$; standardise features to zero mean, unit variance.
2. **Bias trick**: append $x_{d+1}=1$ and treat $b$ as $w_{d+1}$. This unifies code paths for weights and bias.

### Illustrative Example

Consider $d=2$, with $w=(2,-1)^\top$, $b=-0.5$.

* Hyperplane: $2x_1 - x_2 - 0.5 = 0$.
* Point $x=(1,1)$: $z = 2(1) - 1 - 0.5 = 0.5 > 0$ ⇒ right half‑space.
* Point $x=(0,0)$: $z = -0.5 < 0$ ⇒ left half‑space.

### Pitfalls & Diagnostics

| Symptom                                 | Possible cause                   | Quick test       |
| --------------------------------------- | -------------------------------- | ---------------- |
| Vanishing gradients (before activation) | weights initialised too small    | ‖w‖₂ ≪ 1         |
| Saturated activations downstream        | ‖z‖ large due to unscaled inputs | Histogram of $z$ |

---

## 1.1.2 Why Non‑linearity? — From Linear Stacking to Universal Approximation

### 1 Stacking Affine Maps Is Still Affine

Let

$$
f_1(x)=W_1x+b_1,\qquad
f_2(x)=W_2x+b_2.
$$

Their composition is

$$
f_2 \circ f_1(x)=W_2(W_1x+b_1)+b_2=(W_2W_1)x+(W_2b_1+b_2),
$$

an **affine map** again. Inductively, any depth‑$L$ network whose layers are all affine collapses to one affine transform.
*Consequences* Decision boundaries remain **hyperplanes**; therefore the model cannot (i) learn XOR, (ii) separate two concentric circles, or (iii) approximate any function whose level sets are not half‑spaces.

---

### 2 Formal Statement — Universal Approximation Theorem (UAT)

> **Theorem (Cybenko 1989; Hornik 1991)** 
> Let $\sigma:\mathbb{R}\to\mathbb{R}$ be **non‑constant, bounded, and continuous**.
> For any compact set $K\subset\mathbb{R}^{d}$, any continuous function $g:K\to\mathbb{R}$, and any $\varepsilon>0$, there exists a **two‑layer** network
>
> $$
> F(x)=\sum_{j=1}^{N} \alpha_j\sigma\bigl(w_j^{\top}x+\beta_j\bigr)
> $$
>
> such that $\sup_{x\in K}\lvert F(x)-g(x)\rvert<\varepsilon$.

**Interpretation**

* Depth = 2 (one hidden layer) suffices for *existence* of an approximator.
* Width $N$ may be extremely large (≈ $\varepsilon^{-d}$).
* Nothing is said about *learnability* or *sample efficiency*.

**Variants**

| Paper       | Activation assumptions            | Domain                         | Metric   |
| ----------- | --------------------------------- | ------------------------------ | -------- |
| Cybenko ’89 | σ continuous, sigmoidal (lim→±∞)  | cube $[0,1]^d$                 | sup‑norm |
| Hornik ’91  | σ non‑polynomial                  | compact $K\subset\mathbb{R}^d$ | $L^p$    |
| Leshno ’93  | σ locally bounded, non‑polynomial | compact                        | $L^p$    |

> *Key technical tool*: **Stone–Weierstrass Theorem** – non‑polynomial activations generate an algebra dense in $C(K)$.

---

### 3 Why Non‑linearity Is Necessary (and Sufficient)

| Requirement                                     | Pure Affine Nets   | Non‑linear Nets with σ                                                               |
| ----------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------ |
| Separate non‑linearly separable data (e.g. XOR) | **Impossible**     | Achievable with ≥ 1 hidden layer                                                     |
| Approximate arbitrary continuous $g$            | Only if $g$ affine | UAT ⇒ Yes                                                                            |
| Expressive efficiency (depth vs width)          | Depth useless      | Depth gives **exponential** gain in parameters for certain families (Telgarsky 2016) |

---

### 4 Intuition via Polynomial Approximation

1. **Taylor Analogy** – A network with smooth σ (e.g. tanh, GELU) and enough width can mimic a truncated Taylor series of $g$.
2. **Partition‑of‑Unity View** – Piece‑wise linear σ (ReLU) tiles the input space with simplices; linear pieces assemble to approximate $g$.

---

### 5 Concrete Counter‑Example: XOR

Input $x=(x_1,x_2)\in\{0,1\}^2$; labels $y=\text{XOR}(x_1,x_2)$.

* **Affine hypothesis**: $w_1x_1+w_2x_2+b$.
  *Solving* the 4 inequalities yields contradiction ⇒ no affine separator exists.
* **Two‑layer ReLU net**:

$$
\begin{aligned}
h_1 &= \operatorname{ReLU}(x_1-x_2),\\
h_2 &= \operatorname{ReLU}(x_2-x_1),\\
\hat y &= h_1+h_2.
\end{aligned}
$$

Correctly realises XOR with 2 hidden units.

---

### 6 Depth vs Width Trade‑offs (Modern Perspective)

| Family of targets                                 | Depth needed for **poly‑size** network | Citation      |
| ------------------------------------------------- | -------------------------------------- | ------------- |
| Indicator of a convex polytope                    | $O(1)$                                 | Arora ’16     |
| Highly oscillatory functions $f_k(x)=\sin(2^k x)$ | ≥ k with ReLU (else width exponential) | Telgarsky ’16 |
| Boolean circuits                                  | Depth \~ circuit depth                 | Montufar ’14  |

**Take‑away** Non‑linearity alone is **necessary**; depth confers **efficiency**.

---

### 7 Practical Diagnostics

| Symptom                                         | Possible root cause                          | Remedy                                       |
| ----------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| Training loss flatlines on non‑linear task      | Missing/linear activation                    | Insert non‑linear σ after every affine layer |
| Model memorises affine trends, misses curvature | Depth=1 with ReLU but too few units          | Increase width or add layers                 |
| Over‑smooth outputs                             | σ overly smooth (e.g. sigmoid) + small width | Switch to ReLU/GELU or widen                 |

---

### 8 Common Misconceptions

* **“More layers always help.”** Not if activations are absent or linear (e.g. identity); you only pay in parameters.
* **“Universal ≈ perfect.”** UAT guarantees *existence*, not *trainability*; optimisation and data may still fail.
* **“Non‑linearity must be smooth.”** ReLU, which is only *piece‑wise* linear, satisfies UAT because non‑polynomial.

---

| § 1.1.3 topic / gap                                     | Reference (with stable PDF/URL)                                                                                                                              | Why it matters & how to weave it in                                                                                                        | ID to cite        |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **Vanishing‑gradient analysis of S‑shaped activations** | *Understanding the Difficulty of Training Deep Feed‑Forward Neural Networks* – Glorot & Bengio, AISTATS 2010 ([Proceedings of Machine Learning Research][1]) | Empirical and theoretical evidence that sigmoid/tanh saturate; provides derivative‑magnitude histograms you can adapt for Fig. “Pitfalls”. | G\&B 2010         |
|                                                         | *The Vanishing Gradient Problem during Learning Recurrent Neural Nets* – Hochreiter 1998 ([bioinf.jku.at][2])                                                | Classical derivation of exponential decay of back‑propagated gradients; quote Eq. (6) to justify the “Saturation” bullet.                  | Hochreiter 1998   |
| **Piece‑wise linear family – origins & variants**       | *Rectified Linear Units Improve Restricted Boltzmann Machines* – Nair & Hinton, ICML 2010 ([U of T Computer Science][3])                                     | First modern ReLU paper; include Fig. 1 from PDF to illustrate non‑saturating derivative.                                                  | N\&H 2010         |
|                                                         | *Rectifier Non‑linearities Improve Neural Network Acoustic Models* – Maas et al., ICML 2013 (introduces **Leaky‑ReLU**) ([ai.stanford.edu][4])               | Supplies definition $ a=0.01 $ and empirical “dying‑ReLU” fix; useful for Table “Piece‑wise Linear”.                                       | Maas 2013         |
|                                                         | *Delving Deep into Rectifiers: PReLU* – He et al., ICCV 2015 ([cv-foundation.org][5])                                                                        | Gives formula, stability analysis, and Kaiming‑init derivation; cite when discussing trainable slope α.                                    | He 2015           |
| **Smooth modern / self‑normalising functions**          | *Exponential Linear Units (ELUs)* – Clevert et al., ICLR 2016 ([arXiv][6])                                                                                   | Show ELU’s bounded negative branch and faster convergence curves.                                                                          | Clevert 2016      |
|                                                         | *Self‑Normalizing Neural Networks (SELUs)* – Klambauer et al., NIPS 2017 ([NeurIPS Proceedings][7], [arXiv][8])                                              | Provides Banach‑fixed‑point proof of variance stabilisation; integrate theorem box in “Real‑analysis properties”.                          | Klambauer 2017    |
|                                                         | *Gaussian Error Linear Units (GELUs)* – Hendrycks & Gimpel 2016 ([arXiv][9])                                                                                 | Supplies analytic derivative and motivation for Transformer default; use for derivative‑range discussion.                                  | H\&G 2016         |
|                                                         | *Searching for Activation Functions* – Ramachandran et al., Swish/SiLU, 2017 ([arXiv][10])                                                                   | Data‑driven discovery; include “temperature β” curve from paper in optimisation notes.                                                     | Ramachandran 2017 |
|                                                         | *Mish: A Self‑Regularised Non‑Monotonic Activation* – Misra 2019 ([arXiv][11])                                                                               | Non‑monotone but smooth; cite for derivative at zero ≈ 0.31 and empirical robustness.                                                      | Misra 2019        |
| **Hardware‑friendly approximations**                    | *Searching for MobileNetV3* – Howard et al., ICCV 2019 (introduces **Hard‑Swish**) ([CVF Open Access][12])                                                   | Provide piece‑wise linear formula and latency/accuracy trade‑off numbers for “Mobile/edge” bullet.                                         | Howard 2019       |
|                                                         | PyTorch `Hardswish` docs (API & formula) ([PyTorch][13])                                                                                                     | Quick code snippet for implementation box.                                                                                                 | PyTorch API       |
| **Comprehensive surveys & benchmarks**                  | *Activation Functions in Deep Learning: A Comprehensive Survey and Benchmark* – Dubey et al. 2021 ([arXiv][14])                                              | 18‑function benchmark tables you can mine for the “Cross‑Family Comparative Metrics”.                                                      | Dubey 2021        |
|                                                         | *Review and Comparison of Commonly Used Activation Functions* – Szandala 2020 ([arXiv][15])                                                                  | Concise pros/cons lists; good for exercise prompts.                                                                                        | Szandala 2020     |
| **Advanced theory (Lipschitz / robustness)**            | *LipBaB: Computing Exact Lipschitz Constants of ReLU Nets* – Hussein et al. 2021 ([arXiv][16])                                                               | Supply formal Lipschitz bound result to justify “Local L ≤ 1” statement for ReLU‑family.                                                   | Hussein 2021      |

[1]: https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf "[PDF] Understanding the difficulty of training deep feedforward neural ..."
[2]: https://www.bioinf.jku.at/publications/older/2904.pdf "[PDF] Recurrent Neural Net Learning and Vanishing Gradient"
[3]: https://www.cs.toronto.edu/~fritz/absps/reluICML.pdf "[PDF] Rectified Linear Units Improve Restricted Boltzmann Machines"
[4]: https://ai.stanford.edu/~amaas/papers/relu_hybrid_icml2013_final.pdf "[PDF] Rectifier Nonlinearities Improve Neural Network Acoustic Models"
[5]: https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf "[PDF] Delving Deep into Rectifiers: Surpassing Human-Level Performance ..."
[6]: https://arxiv.org/abs/1511.07289 "Fast and Accurate Deep Network Learning by Exponential Linear ..."
[7]: https://proceedings.neurips.cc/paper/6698-self-normalizing-neural-networks.pdf "[PDF] Self-Normalizing Neural Networks - NIPS"
[8]: https://arxiv.org/abs/1706.02515 "Self-Normalizing Neural Networks"
[9]: https://arxiv.org/abs/1606.08415 "[1606.08415] Gaussian Error Linear Units (GELUs) - arXiv"
[10]: https://arxiv.org/abs/1710.05941 "[1710.05941] Searching for Activation Functions - arXiv"
[11]: https://arxiv.org/abs/1908.08681 "Mish: A Self Regularized Non-Monotonic Activation Function - arXiv"
[12]: https://openaccess.thecvf.com/content_ICCV_2019/papers/Howard_Searching_for_MobileNetV3_ICCV_2019_paper.pdf "[PDF] Searching for MobileNetV3 - CVF Open Access"
[13]: https://pytorch.org/docs/stable/generated/torch.nn.Hardswish.html "Hardswish — PyTorch 2.7 documentation"
[14]: https://arxiv.org/pdf/2109.14545 "[PDF] Activation Functions in Deep Learning - arXiv"
[15]: https://arxiv.org/pdf/2010.09458 "[PDF] Review and Comparison of Commonly Used Activation Functions for ..."
[16]: https://arxiv.org/abs/2105.05495 "LipBaB: Computing exact Lipschitz constant of ReLU networks - arXiv"


| § 1.1.3 gap you want to deepen                      | 2024‑25 reference (stable PDF/URL)                                                                                               | Key contribution & how to weave it in                                                                                                                                     | ID to cite      |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **Comprehensive landscape update**                  | *Three Decades of Activations: A Comprehensive Survey of 400 Activation Functions* – Kunc & Kléma, Feb 2024 ([arXiv][1])         | Largest single catalogue to date; add to “Survey Context” row and replace 2021 Dubey numbers.                                                                             | Kunc 2024       |
| **New smooth, analytic function**                   | *TeLU: Hyperbolic Tangent Exponential Linear Unit for Fast & Stable DL* – Fernandez & Mali, Dec 2024 → rev Jan 2025 ([arXiv][2]) | TeLU(x)=x tanh (eˣ); combines ReLU‑like identity zone with tanh saturation.  Place it in § 1.1.3.3 “Smooth Modern Variants” with derivative ≈ 1 near 0 and Lipschitz ≈ 1. | TeLU 2025       |
| **Super‑expressive periodic family**                | *PEUAF: Parametric Elementary Universal Activation Function* – Wang et al., Neural Networks (Jul 2024, in‑press) ([arXiv][3])    | Generalises “super‑expressive” activations; insert under new sub‑heading **3.4 Periodic & Super‑Expressive**.  Offers constructive UAT with fixed width.                  | PEUAF 2024      |
| **Per‑neuron learned activations**                  | *Self‑Activating Neural Networks (SANN)* – Tutuncuoglu, SSRN pre‑print (May 2025) ([SSRN][4])                                    | Each neuron trains a 2‑segment piece‑wise‑linear activation.  Add to “Trainable / Adaptive” side‑bar and link to Fig. ‘Bias trick’.                                       | SANN 2025       |
| **ReLU revival via surrogate gradients**            | *The Resurrection of the ReLU (SUGAR)* – Horuz et al., May 2025 ([arXiv][5])                                                     | Keeps ReLU forward pass but swaps derivative → smooth surrogate; cite in “Pitfalls & Diagnostics” as a remedy for dying ReLUs.                                            | SUGAR 2025      |
| **Kernel‑theoretic impact of non‑ReLU activations** | *Beyond ReLU: How Activations Affect Neural Kernels & Wide‑Network Limits* – Holzmüller & Schölpple, Jun 2025 ([arXiv][6])       | Characterises NTK/NNGP RKHS for SELU, ELU, Leaky‑ReLU etc.; enrich the “Real‑analysis properties” column with kernel‑smoothness notes.                                    | Holzmüller 2025 |
| **Robustness & Lipschitz certification**            | *Novel Quadratic Constraints extend LipSDP to GroupSort, MaxMin, Householder* – Pauli et al., Jan 2024 ([arXiv][7])              | Supplies tractable global L bounds for 1‑Lipschitz activations; update the **Lipschitz constant** bullet.                                                                 | Pauli 2024      |
| **Stability measure beyond Lipschitz**              | *Do Stable Neural Networks Exist for Classification Problems?* – Liu & Hansen, Jan 2024                                          | Proposes “class‑stability” metric; mention in a footnote that bounded‑derivative ≠ overall stability.                                                                     | Liu 2024        |
| **Hardware‑driven non‑linearity**                   | *Engineering Non‑linear Activations for All‑Optical NN via Quantum Interference* – Xu et al., Apr 2025 ([arXiv][8])              | Implements sigmoid & ReLU transfer with < 20 μW optical power; append to the “Hardware efficiency” row for photonics.                                                     | Xu 2025         |

[1]: https://arxiv.org/abs/2402.09092 "Three Decades of Activations: A Comprehensive Survey of 400 Activation Functions for Neural Networks"
[2]: https://arxiv.org/abs/2412.20269 "[2412.20269] TeLU Activation Function for Fast and Stable Deep Learning"
[3]: https://arxiv.org/html/2407.09580v1 "Don’t Fear Peculiar Activation Functions: EUAF and Beyond"
[4]: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5215137 "Neuron-Level Activation Learning in Neural Networks: A Self-Configuring AI Approach by Bekir Tolga Tutuncuoglu :: SSRN"
[5]: https://arxiv.org/abs/2505.22074 "[2505.22074] The Resurrection of the ReLU"
[6]: https://arxiv.org/abs/2506.22429 "[2506.22429] Beyond ReLU: How Activations Affect Neural Kernels and Random Wide Networks"
[7]: https://arxiv.org/html/2401.14033v1 "Novel Quadratic Constraints for Extending LipSDP beyond Slope-Restricted Activations"
[8]: https://arxiv.org/abs/2504.04009 "[2504.04009] Engineering nonlinear activation functions for all-optical neural networks via quantum interference"

## 1.1.3 Activation Functions: Taxonomy and Real‑Analysis Properties

> **Activation function**
> A map $\sigma:\mathbb{R}\to\mathbb{R}$ applied element‑wise to the affine core output $z$.
> A **network layer** therefore realises $x\mapsto\sigma(Wx+b)$, a *non‑linear* operator as long as $\sigma$ is not affine.

For each family below we formalise

* **Definition** $(\text{closed}/\text{analytic})$
* **Real‑analysis properties**

  * continuity, differentiability, Lipschitz constant, boundedness
  * derivative limits $\lim_{z\to\pm\infty}\sigma'(z)$ (vanishing/exploding gradient risk)
* **Practical notes** on optimisation and expressivity

---

### 1.1.3.1 Classical S‑Shaped Functions

| Function    | Formula                                                    | Range    | $\sigma'(z)$       | Key Properties                                                                    |   |                         |
| ----------- | ---------------------------------------------------------- | -------- | ------------------ | --------------------------------------------------------------------------------- | - | ----------------------- |
| **Sigmoid** | $\displaystyle \sigma(z)=\frac{1}{1+e^{-z}}$               | $(0,1)$  | $\sigma(1-\sigma)$ | *Bounded*, $C^\infty$, **monotone**, $\sigma'(0)=\tfrac14$, (\displaystyle\lim\_{ | z | \to\infty}\sigma'(z)=0) |
| **Tanh**    | $\displaystyle \tanh(z)=\frac{e^{z}-e^{-z}}{e^{z}+e^{-z}}$ | $(-1,1)$ | $1-\tanh^{2}(z)$   | Same regularity; zero‑mean output accelerates training                            |   |                         |

**Analysis & Pitfalls**

* **Vanishing gradient**: derivative bounded above by ¼ (sigmoid) or 1 (tanh) but decays *exponentially* for $|z|\gg0$; back‑prop through many layers attenuates signal.
* **Saturation**: when $|z|>4$, $\lvert\sigma'(z)\rvert<10^{-2}$. Leads to *plateaus* in optimisation.
* **Output‑bias coupling**: Sigmoid’s positive range shifts mean activations, slowing convergence; tanh mitigates via symmetry.

---

### 1.1.3.2 Piece‑wise Linear Family

| Function                    | Formula ($a>0$ small)                      | Range        | $\sigma'(z)$                 | Key Properties                                                                        |
| --------------------------- | ------------------------------------------ | ------------ | ---------------------------- | ------------------------------------------------------------------------------------- |
| **ReLU**                    | $\max(0,z)$                                | $[0,\infty)$ | $0$ for $z<0$; $1$ for $z>0$ | *Unbounded*, *non‑saturating* on $z>0$, not differentiable at 0 (sub‑gradient exists) |
| **Leaky ReLU**              | $\max(az,z)$                               | $\mathbb{R}$ | $a$ for $z<0$; $1$ for $z>0$ | Fixes “dying ReLU” by permitting gradient $a$ left of 0                               |
| **Parametric ReLU (PReLU)** | $\max(\alpha z,z)$ with trainable $\alpha$ | $\mathbb{R}$ | $\alpha$ or $1$              | $\alpha$ learned per neuron/channel; slight risk of instability if $\alpha>1$         |

**Analysis**

* **Lipschitz constant** $L=1$ (for $a\le1$). Stable gradients.
* **Sparse activation**: ReLU imposes $z<0\mapsto0$ ⇒ implicit $L^0$-style regularisation.
* **Non‑smooth point** $z=0$ rarely harms SGD; sub‑gradient suffices.

---

### 1.1.3.3 Smooth Modern Variants

| Function                      | Definition                                                   | Smoothness                         | $\sigma'(0)$                            | Remarks                                                         |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------- | --------------------------------------- | --------------------------------------------------------------- |
| **SiLU / Swish**              | $\displaystyle z\sigma(z)=z\cdot\frac{1}{1+e^{-z}}$        | $C^\infty$                         | ½                                       | Self‑gated; empirically tops ReLU on vision/NLP                 |
| **GELU**                      | $\displaystyle z\Phi(z)$ where $\Phi$ is standard‑normal CDF | $C^\infty$                         | ½                                       | Approximates stochastic regularisation; default in Transformers |
| **Mish**                      | $\displaystyle z\tanh(\ln(1+e^{z}))$                         | $C^\infty$                         | ≈ 0.31                                  | Slightly heavier compute, claims smoother gradient flow         |
| **Hard‑Swish / Hard‑Sigmoid** | Piece‑wise linear approximations to Swish/Sigmoid            | Lipschitz 1, differentiable *a.e.* | Implementation friendly on edge devices |                                                                 |

**Key Theoretical Notes**

1. **Non‑polynomial ⇒ UAT satisfied.** All above activations (except hard variants) are analytic and thus non‑polynomial.
2. **Smoothness vs Compute**: Extra FLOPs (\~ +15 %) seldom bottleneck on GPU; on microcontrollers, hard approximations reduce MACs.
3. **Derivative Range**: Unlike sigmoid/tanh, derivatives peak around $z≈1$ but taper more slowly ⇒ mitigates vanishing gradient.

---

### Cross‑Family Comparative Metrics

| Property                               | Sigmoid/Tanh | ReLU/PReLU            | GELU/SiLU/Mish                 |
| -------------------------------------- | ------------ | --------------------- | ------------------------------ |
| **Bounded output**                     | ✓            | ✗                     | ✗                              |
| **Gradient never zero on active side** | ✗            | ✓                     | ✓                              |
| **Continuous derivative**              | ✓            | ✗ (kink)              | ✓                              |
| **Zero‑mean**                          | tanh         | Leaky‑family (approx) | GELU/Mish (approx)             |
| **Hardware efficiency**                | moderate     | highest               | moderate (hard‑variants: high) |
| **Vanishing‑gradient risk**            | high         | low                   | low                            |

---

### Practical Selection Heuristics

1. **Deep vision/NLP**: GELU or SiLU; pair with LayerNorm.
2. **Mobile/edge**: Hard‑Swish (MobileNet‑v3) trades ≤ 1 % accuracy for 25 % latency cut.
3. **Sparse/robust needs**: Leaky‑ReLU with $a=0.01$ averts dead units under noisy inputs.
4. **Probabilistic outputs**: Use sigmoid/tanh in final layer to bound range (e.g. Bernoulli logits, hyperbolic set‑points).

---

### Formal Properties Checklist

For each activation $\sigma$ used in hidden layers ensure

* **Measurability**: Borel measurable (all listed satisfy).
* **Local Lipschitz**: guarantees existence of gradients almost everywhere → essential for back‑prop convergence proofs.
* **Non‑polynomial**: preserves universal approximation.
* **Derivative bounded below on active region**: avoids dead gradients.

---

| § 1.1.4 topic / new angle                          | 2024‑25 reference (stable PDF / URL)                                                                                                       | Why it matters & how to integrate                                                                                                                                                                                                                    | ID to cite                 |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **Local region density & robustness**              | *On the Local Complexity of Linear Regions in Deep ReLU Networks* – Patel & Montúfar, arXiv 2412.18283 (Dec 2024)                          | Introduces **local complexity** (= density of linear regions near data) and proves it upper‑bounds total variation ⇒ direct link between polytope density and adversarial robustness; append after Eq. “∑ … O(kᵈ)” as a *data‑dependent* refinement. | ([arXiv][1])               |
| **Hyperplane arrangements & fixed points**         | *Hyperplane Arrangements and Fixed Points in Iterated PWL Neural Networks* – Beise, arXiv 2405.09878 (Jul 2024)                            | Gives an arrangement‑theoretic upper bound on the **number of stable fixed points**; plug into “Deep Networks: Exponential Cell Count” box to show optimality of layer‑wise growth.                                                                  | ([arXiv][2])               |
| **Tropical geometry of decision boundaries**       | *The Real Tropical Geometry of Neural Networks* – Brandenburg, Loho & Montúfar, arXiv 2403.11871 (Mar 2024)                                | Defines the **activation polytope** & **classification fan**; add a side‑bar “Tropical fans ≈ polyhedral complexes” clarifying how decision regions relate to oriented matroids.                                                                     | ([arXiv][3])               |
| **Hardness of region counting**                    | *The Computational Complexity of Counting Linear Regions in ReLU Networks* – Stargalla et al., arXiv 2505.16716 (May 2025)                 | Proves #P‑hardness of exact and approximate counting ⇒ enrich “Exponential Cell Count” paragraph with a caution that counting is intractable even for 2 layers.                                                                                      | ([arXiv][4])               |
| **Tight CNN upper bounds**                         | *On the Upper Bounds of the Number of Linear Regions and the Generalisation Error for CNNs* – TPAMI 2025 early‑access                      | Derives depth‑aware **tight upper bounds** for convolutional ReLU nets; update the formula node in “Layer‑wise Composition” for structured weight tying.                                                                                             | ([ACM Digital Library][5]) |
| **Algorithmic extraction of region combinatorics** | *Algorithmic Determination of the Combinatorial Structure of the Linear Regions of ReLU NNs* – Masden, **SIAGA** 9 (2): 185‑220 (Jun 2025) | Supplies a practical algorithm (poly in #neurons for d ≤ 4) to enumerate region adjacencies; cite in “Visual Illustrations” note as a tool for Figure 2 generation.                                                                                  | ([SIAM Ebooks][6])         |
| **Geometry‑based OOD & interpretability**          | *Tropical Geometry Features for Novelty Detection and Interpretability* – ICLR 2025 under review (Nov 2024 draft)                          | Uses volumes & densities of learned polytopes for OOD detection; insert into “Practical Diagnostics → Fragmented tiny cells” as a downstream application.                                                                                            | ([OpenReview][7])          |
| **Tutorial synthesis**                             | ICASSP 2024 tutorial **“Tropical Geometry for Machine Learning & Optimization”** – Maragos                                                 | 3‑hour slide deck summarises max‑plus algebra → linear‑region counting; add to “Suggested Further Reading” list for readers new to tropical tools.                                                                                                   | ([IRAL][8])                |

[1]: https://arxiv.org/abs/2412.18283 "On the Local Complexity of Linear Regions in Deep ReLU Networks"
[2]: https://arxiv.org/pdf/2405.09878 "[PDF] Hyperplane Arrangements and Fixed Points in Iterated PWL Neural ..."
[3]: https://arxiv.org/abs/2403.11871 "The Real Tropical Geometry of Neural Networks"
[4]: https://arxiv.org/html/2505.16716 "The Computational Complexity of Counting Linear Regions in ReLU ..."
[5]: https://dl.acm.org/doi/10.1109/TPAMI.2025.3548620 "On the Upper Bounds of Number of Linear Regions and ..."
[6]: https://epubs.siam.org/doi/10.1137/24M1646996 "Algorithmic Determination of the Combinatorial Structure of the ..."
[7]: https://openreview.net/pdf/10dba66b40804f130f9e132ecf6a2131e7d57162.pdf "[PDF] TROPICAL GEOMETRY FEATURES FOR NOVELTY DE- TECTION ..."
[8]: https://robotics.ntua.gr/icassp-2024-tutorial/ "ICASSP 2024: P. Maragos, “Tropical Geometry for Machine ... - IRAL"

| § 1.1.4 topic / gap                                          | Reference (stable PDF / URL)                                                                                                                                                                                                                | Why it matters & how to weave it in                                                                                                                                    | ID to cite                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **Hyperplane & half‑space basics; Zaslavsky formula**        | R. Stanley, *An Introduction to Hyperplane Arrangements*, IAS / PCMI lecture notes (2004) – §1–2 derives \$r(\mathcal A)=(-1)^d\chi\_\mathcal A(-1)\$ and gives the $\sum_{i=0}^d\binom{k}{i}$ upper bound you cite. ([MIT Mathematics][1]) | Insert as a formal proof box after “Matrix Form”; provides rigor for the \$O(k^{d})\$ cell‑count line.                                                                 | Stanley 2004                 |
|                                                              | T. Zaslavsky, “Facing up to Arrangements” (1975, Adv. Math.) — original theorem on region counts. (Accessible via compendium in Stanley’s notes). ([MathOverflow][2])                                                                       | Historical anchor; mention in a footnote to acknowledge provenance of the counting formula.                                                                            | Zaslavsky 1975               |
| **Exponential region growth with depth**                     | G. Montúfar et al., *On the Number of Linear Regions of Deep Neural Networks*, NeurIPS 2014 ([NeurIPS Papers][3])                                                                                                                           | Supplies closed‑form lower bound $\prod_{\ell=1}^{L}\sum_{i=0}^{d}\binom{k_\ell}{i}$; include Theorem 4 as the formal justification of your “exponential in L” bullet. | Montúfar 2014                |
|                                                              | M. Telgarsky, *Benefits of Depth in Neural Networks*, COLT 2016 ([arXiv][4])                                                                                                                                                                | Gives constructive depth‑vs‑width separations using “sawtooth” functions; cite for Table “Depth vs Width Trade‑offs”.                                                  | Telgarsky 2016               |
|                                                              | V. Raghu et al., *On the Expressive Power of Deep Neural Networks* (trajectory‑length metric), ICML 2017 ([Proceedings of Machine Learning Research][5])                                                                                    | Adds complementary expressivity measure; good for a side‑bar comparing region‑count to trajectory‑length.                                                              | Raghu 2017                   |
|                                                              | B. Hanin & D. Rolnick, *Complexity of Linear Regions in Deep Networks*, ICML 2019 ([Proceedings of Machine Learning Research][6])                                                                                                           | Shows typical (random‑init) networks realise far fewer regions than worst‑case; supports a “Practical caveats” text box.                                               | Hanin 2019                   |
|                                                              | S. Serra, C. Tjeng, et al., *Bounding and Counting Linear Regions of Deep Neural Networks*, NeurIPS 2018 ([arXiv][7])                                                                                                                       | Supplies MILP upper/lower bounds and empirical plots; useful for Figure 2 “Partition of Plane”.                                                                        | Serra 2018                   |
| **Convexity, connectedness & union of polyhedral cells**     | S. Arora et al., *Understanding Deep Neural Networks from Geometry* (ICML 2018) – §3 proves union‑of‑polytope view                                                                                                                          | Bridges convex cell intersections to non‑convex class manifolds; cite when explaining XOR geometric union.                                                             | (fetch separately if needed) |
| **Margins & angular analysis**                               | N. Cortes & V. Vapnik, *Support‑Vector Networks*, ML 1995 – original margin bound (already in § 1.1.5)                                                                                                                                      | Cross‑link to define geometric margin γ formula and generalisation tie‑in.                                                                                             | (existing)                   |
|                                                              | Y. Liu et al., *Large‑Margin Softmax Loss*, ICML 2016 ([Proceedings of Machine Learning Research][8])                                                                                                                                       | Gives weight‑norm / angular‑margin softmax; reference for “weight normalisation / max‑margin objectives” row.                                                          | Liu 2016                     |
|                                                              | J. Deng et al., *ArcFace: Additive Angular Margin Loss*, CVPR 2019 ([arXiv][9])                                                                                                                                                             | Supplies empirical evidence that explicit angular margins enlarge γ and boost robustness.                                                                              | Deng 2019                    |
| **Weight diversity & orthogonal init (prevent colinear wₖ)** | T. Salimans & D. Kingma, *Weight Normalization*, NIPS 2016 ([arXiv][10])                                                                                                                                                                    | Cite in “Remedy” for ‘colinear weights’ pitfall; shows how decoupling weight length aids angular spread.                                                               | Salimans 2016                |
|                                                              | A. Saxe et al., *Exact Solutions to the Nonlinear Dynamics of Learning in Deep Linear Nets*, ICLR 2014 (orthogonal init) ([arXiv][11])                                                                                                      | Explain why orthogonal init retains gradient isotropy → diverse hyperplanes.                                                                                           | Saxe 2014                    |
| **“Dead‑ReLU wall” & overly fragmented cells**               | B. Xu et al., *Empirical Evaluation of Rectified Activations*, arXiv 1505.00853 ([arXiv][12])                                                                                                                                               | Supplies quantitative evidence of dying‑ReLU frequencies; cite under Pitfalls row.                                                                                     | Xu 2015                      |

[1]: https://math.mit.edu/~rstan/arrangements/arr.html "Hyperplane Arrangments - MIT Mathematics"
[2]: https://mathoverflow.net/questions/193341/number-of-regions-of-a-hyperplane-arrangement-avoiding-a-generic-hyperplane "Number of regions of a hyperplane arrangement avoiding a generic ..."
[3]: https://papers.nips.cc/paper/5422-on-the-number-of-linear-regions-of-deep-neural-networks "On the Number of Linear Regions of Deep Neural Networks - NIPS"
[4]: https://arxiv.org/abs/1602.04485 "[1602.04485] Benefits of depth in neural networks - arXiv"
[5]: https://proceedings.mlr.press/v70/raghu17a/raghu17a.pdf "[PDF] On the Expressive Power of Deep Neural Networks"
[6]: https://proceedings.mlr.press/v97/hanin19a.html "Complexity of Linear Regions in Deep Networks"
[7]: https://arxiv.org/abs/1711.02114 "Bounding and Counting Linear Regions of Deep Neural Networks"
[8]: https://proceedings.mlr.press/v48/liud16.pdf "[PDF] Large-Margin Softmax Loss for Convolutional Neural Networks"
[9]: https://arxiv.org/abs/1801.07698 "ArcFace: Additive Angular Margin Loss for Deep Face Recognition"
[10]: https://arxiv.org/abs/1602.07868 "Weight Normalization: A Simple Reparameterization to Accelerate Training of Deep Neural Networks"
[11]: https://arxiv.org/abs/1312.6120 "Exact solutions to the nonlinear dynamics of learning in deep linear neural networks"
[12]: https://arxiv.org/abs/1505.00853 "Empirical Evaluation of Rectified Activations in Convolutional Network"

## 1.1.4 Geometric View: Hyperplanes, Half‑Spaces, and Decision Regions

### 1 Single‑Neuron Geometry

**Hyperplane.**
For weight–bias pair $(w,b)\in\mathbb{R}^{d}\times\mathbb{R}$ the set

$$
H(w,b)=\{x\in\mathbb{R}^{d}\mid w^{\top}x+b=0\}
$$

is a $(d-1)$-dimensional **hyperplane**.

**Half‑spaces.**

$$
\mathcal{P}^{+}=\{x\mid w^{\top}x+b>0\},\qquad
\mathcal{P}^{-}=\{x\mid w^{\top}x+b<0\},
$$

two closed, convex **half‑spaces** forming a partition $\mathbb{R}^{d}=\mathcal{P}^{+}\cup H\cup\mathcal{P}^{-}$.

> *Hard-threshold perceptron* assigns label $y=\operatorname{sgn}(w^{\top}x+b)$: the decision boundary is exactly $H$.

---

### 2 Layer‑wise Composition: From Half‑Spaces to Polytopes

Consider a layer of $k$ neurons with ReLU (or hard threshold):

$$
h(x)=\sigma(Wx+b),\quad W\in\mathbb{R}^{k\times d}.
$$

Each row $w_j^{\top}$ yields a hyperplane $H_j$.  The **intersection** of selected half‑spaces

$$
\bigcap_{j\in S}\mathcal{P}^{+}_{j}\cap\bigcap_{j\notin S}\mathcal{P}^{-}_{j}
$$

for some index set $S\subseteq\{1,\dots,k\}$ is a convex **polyhedron**.
Thus the input space is partitioned into at most

$$
\sum_{i=0}^{d}\binom{k}{i} = O(k^{d})
$$

full‑dimensional **cells** (Zaslavsky’s theorem).  On each cell, $h(x)$ is *affine* because ReLU is piece‑wise linear.

---

### 3 Deep Networks: Exponential Cell Count

A depth‑$L$ ReLU network with widths $k_1,\dots,k_L$ can generate

$$
\prod_{\ell=1}^{L}\sum_{i=0}^{d}\binom{k_\ell}{i}
$$

regions—**exponential in $L$** even when widths are fixed (Montúfar 2014).
Hence depth increases expressive power geometrically via finer tiling.

---

### 4 Convexity, Connectedness, and Decision Sets

* **Convex neurons.** Half‑spaces are convex ⇒ intersections of half‑spaces are convex ⇒ *linear classifiers* produce **one convex region per class**.
* **Non‑convex decisions.** By **union** of multiple convex cells across layers, deep nets create **non‑convex**, even **disconnected**, class manifolds.
* **Example (XOR in $\mathbb{R}^{2}$).** Two ReLU neurons carve four quadrants; subsequent affine combination unions opposite quadrants → non‑convex L‑shaped decision set.

---

### 5 Angles, Margins, and Generalisation

* **Angular margin**: distance of data point $x$ to hyperplane normalised by ‖w‖:

  $$
  \gamma=\frac{w^{\top}x+b}{\lVert w\rVert_2}.
  $$

  Larger $\gamma$ ⇒ larger **geometric margin**, correlated with VC‑dimension bounds and robustness to noise.
* **Weight normalisation / max‑margin objectives** (e.g. SVM, large‑margin softmax) explicitly enlarge $\gamma$.

---

### 6 Feature Homogenisation via Bias Trick

Embedding $x\mapsto[x;1]\in\mathbb{R}^{d+1}$ converts affine hyperplanes into *homogeneous* ones through the origin in $d+1$‑space.  Geometry then involves **linear subspaces** only, simplifying proofs of separability.

---

### 7 Visual Illustrations (described)

* **Figure 1**: 2‑D scatter, hyperplane line, half‑spaces shaded red/blue.
* **Figure 2**: ReLU network partition of plane into polytopes; colours denote piece‑wise affine regions.
* **Figure 3**: XOR decision regions – two diagonal strips classified positive.

(*Produce when compiling full textbook; omitted here.*)

---

### 8 Common Geometric Pitfalls

| Observation                                   | Likely cause                                           | Remedy                                                            |
| --------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------- |
| Decision boundary nearly linear despite depth | All neurons’ $w_j$ colinear ⇒ cells collapse           | Encourage weight diversity (orthogonal init, angular regulariser) |
| “Dead ReLU wall” blocking gradients           | Many samples fall into $w^{\top}x+b<0$ for same neuron | Use Leaky‑ReLU or bias initialisation $b>0$                       |
| Fragmented tiny cells (over‑fitting)          | Excessive depth & width vs data                        | Add regularisation, early stopping                                |

---

### 9 Formal Summary

* A **neuron** ⇒ hyperplane $H$ + two convex half‑spaces.
* **Layer of neurons** ⇒ *polyhedral complex*; network value is piece‑wise affine (ReLU) or smooth (GELU).
* **Depth** multiplies cell count ⇒ finer geometric granularity ⇒ higher expressive power w\.r.t. non‑convex decision sets.
* **Margins & angular analysis** link geometry to generalisation bounds.

---

| § 1.1.5 topic / gap                                           | Reference (stable PDF / URL)                                                                                                                                                     | Key contribution & how to integrate                                                                      | ID to cite      |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------- |
| **Perceptron – original algorithm & mistake bound**           | Rosenblatt F. (1958) *The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain*, *Psychological Review* 65 (6): 386‑408 ([ling.upenn.edu][1]) | Primary source of hard‑threshold update rule; quote Eq. (1) when motivating Table 1.1.5.1.               | Rosenblatt 1958 |
|                                                               | Novikoff A. (1962) *On Convergence Proofs for Perceptrons* (reprinted PDF) ([Cheriton School of Computer Science][2])                                                            | Proves the finite‑mistake bound ≤ (R/γ)²; include as boxed “Convergence Theorem”.                        | Novikoff 1962   |
|                                                               | Mohri M. (2012) *Perceptron Mistake Bounds* lecture note ([cs.nyu.edu][3])                                                                                                       | Modern presentation with margin‑perceptron variant; ideal for Exercise 4.                                | Mohri 2012      |
|                                                               | Shalev‑Shwartz & Ben‑David (2014) *Understanding Machine Learning*, §9.4 “Half‑Spaces” ([Hebrew University Computer Science][4])                                                 | Gives PAC proof and connects VC‑dim = d + 1 to perceptron capacity; cross‑link to § 1.1.1.               | UML §9.4        |
| **Linear Regression – OLS algebra & Gauss–Markov**            | Frank Wood, *Gauss‑Markov Theorem* note (Oxford) ([Oxford Robotics Institute][5])                                                                                                | Step‑by‑step matrix proof that OLS is BLUE; insert into “Statistical view” sub‑box.                      | Wood GM         |
|                                                               | Hastie, Tibshirani & Friedman (2009) *The Elements of Statistical Learning*, Ch. 3 & 7 ([SAS UPenn][6])                                                                          | Supplies bias‑variance decomposition graphs; cite in “Generalisation” bullet.                            | ESL Ch 3/7      |
|                                                               | “OLS in Matrix Form” (NYU sociology note) ([Stanford University][7])                                                                                                             | Derives variance‑covariance matrix Σ̂ = σ²(XᵀX)⁻¹; handy for linking to confidence‑interval diagnostics. | NYU‑OLS         |
|                                                               | Tobias J. (2009) Purdue *Regression #3* lecture ([Purdue University ICS][8])                                                                                                     | Proofs of unbiasedness & consistency; add as reading for Exercise 2.                                     | Tobias 2009     |
| **Logistic Regression – convexity, optimisation, separation** | Boyd & Vandenberghe (2004) *Convex Optimization*, §3.5 “Logistic Loss” ([Stanford University][9])                                                                                | Supplies second‑derivative > 0 proof ⇒ strict convexity; quote to justify “unique minimiser” claim.      | Boyd §3.5       |
|                                                               | ENS lecture note *Logistic Regression & Convex Analysis* (2019) ([di.ens.fr][10])                                                                                                | Presents Hessian σ(z)(1−σ(z))XᵀX form; insert alongside Newton update derivation.                        | ENS 2019        |
|                                                               | Waterloo note *Newton / IRLS for LR* (2022) ([Cheriton School of Computer Science][11])                                                                                          | Full derivation of gradient, Hessian and Algorithm 3.13; cite under “Optimisation”.                      | Waterloo 2022   |
|                                                               | Srihari S. IRLS slide deck (Buffalo) ([CEDAR][12])                                                                                                                               | Compact formula for IRLS weight matrix W; good for implementation snippet.                               | Srihari IRLS    |
|                                                               | Böhning D. (1992) *Multinomial Logistic Regression Algorithm* ([University of Southampton][13])                                                                                  | Shows quadratic‑lower‑bound Newton variant with monotone convergence; enrich optimisation section.       | Böhning 1992    |
|                                                               | Albert A. & Anderson J. (1984) *On the Existence of MLEs in Logistic Regression*, *Biometrika* 71 (1): 1‑10 ([ResearchGate][14])                                                 | Formal separation theorem explaining infinite‑weight pathology; reference in “Pitfalls & Remedies”.      | A\&A 1984       |

[1]: https://www.ling.upenn.edu/courses/cogs501/Rosenblatt1958.pdf "[PDF] THE PERCEPTRON: A PROBABILISTIC MODEL FOR ..."
[2]: https://cs.uwaterloo.ca/~y328yu/classics/novikoff.pdf "[PDF] On Convergence proofs for perceptrons"
[3]: https://cs.nyu.edu/~mohri/pub/pmb.pdf "[PDF] Perceptron Mistake Bounds - NYU Computer Science"
[4]: https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf "[PDF] Understanding Machine Learning: From Theory to Algorithms"
[5]: https://www.robots.ox.ac.uk/~fwood/teaching/W4315_Fall2010/Lectures/gauss_markov_theorem/main.pdf "[PDF] Gauss Markov Theorem"
[6]: https://www.sas.upenn.edu/~fdiebold/NoHesitations/BookAdvanced.pdf "[PDF] The Elements of Statistical Learning - Penn Arts & Sciences"
[7]: https://web.stanford.edu/~mrosenfe/soc_meth_proj3/matrix_OLS_NYU_notes.pdf "[PDF] OLS in Matrix Form"
[8]: https://web.ics.purdue.edu/~jltobias/671/lecture_notes/regression3.pdf "[PDF] Regression #3: Properties of OLS Estimator - Purdue University"
[9]: https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf "[PDF] Convex Optimization - Stanford University"
[10]: https://www.di.ens.fr/appstat/spring-2019/lecture_notes/Lesson5_ConvexAnalysis.pdf "[PDF] Logistic regression and convex analysis"
[11]: https://cs.uwaterloo.ca/~y328yu/teaching/480/480-note-log.pdf "[PDF] 3 Logistic Regression - University of Waterloo"
[12]: https://www.cedar.buffalo.edu/~srihari/CSE574/Chap4/4.3.3-IRLS.pdf "[PDF] Iterative Reweighted Least Squares - CEDAR"
[13]: https://www.personal.soton.ac.uk/dab1f10/aism92.pdf "[PDF] Multinomial logistic regression algorithm"
[14]: https://www.researchgate.net/publication/31354843_On_the_Existence_of_Maximum_Likelihood_Estimates_in_Logistic_Regression_Models "(PDF) On the Existence of Maximum Likelihood Estimates in Logistic ..."

## 1.1.5 Classical Single‑Neuron Models

A **single neuron** becomes a complete learning model once we (i) choose its activation $\sigma$ and (ii) specify an **objective** for fitting $(w,b)$ to data $\{(x^{(i)},y^{(i)})\}_{i=1}^{n}$.

### 1.1.5.1 Perceptron (Hard Threshold)

| Item                                      | Formal description                                                                                                                                                                     |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hypothesis**                            | $ \hat y = \operatorname{sgn}(w^{\top}x + b)\in\{-1,+1\}$                                                                                                                            |
| **Loss**                                  | **Perceptron loss** $\ell(z)=\max(0,-z)$ with $z=y(w^{\top}x+b)$                                                                                                                       |
| **Learning rule (Rosenblatt 1958)**       | For mis‑classified sample $(x,y)$: $w\leftarrow w + \eta y x, b\leftarrow b + \eta y$                                                                                                |
| **Convergence (linearly separable case)** | If $\exists (w_\*,b_\*)$ s.t. $y(w_\*^{\top}x+b_\*)\ge\gamma>0$ for all samples, algorithm terminates after ≤$\bigl(\tfrac{R}{\gamma}\bigr)^2$ updates where $R=\max_i \|x^{(i)}\|_2$. |
| **Capacity**                              | VC‑dimension = $d+1$                                                                                                                                                                   |
| **Limitations**                           | Fails on non‑separable data; no probabilistic scores; objective non‑smooth so margin control is indirect.                                                                              |

> **Mistake‑Bound Proof Sketch**
> Maintain $\|w_t\|_2^2$. Each mistake increases $y_t w_t^{\top}x_t$ by $\eta\gamma$ but can enlarge $\|w_t\|$ by ≤$\eta R$. Algebraic telescoping yields the stated bound.

**Extensions**

* **Pocket algorithm** – retains best‑so‑far weights for non‑separable sets.
* **Margin Perceptron** – update only if $y(w^{\top}x+b)<\delta$; provably achieves margin ≥ $\delta$.

---

### 1.1.5.2 Linear Regression (Identity Activation)

| Item                     | Details                                                                                                                                                                         |                                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Model**                | $y = w^{\top}x + b + \varepsilon,\quad \varepsilon\sim\mathcal{N}(0,\sigma^{2})$                                                                                                |                                                                                                       |
| **Objective**            | Minimise **mean‑squared error (MSE)**: $\frac1n\sum_{i=1}^{n} (y^{(i)} - w^{\top}x^{(i)} - b)^2$                                                                                |                                                                                                       |
| **Closed‑form solution** | Let $X=[x^{(1)};\dots;x^{(n)}]\in\mathbb{R}^{n\times d}$, (\tilde X=\[X,                                                                                                        | ,\mathbf1]). Then $\tilde w = (\tilde X^{\top}\tilde X)^{-1}\tilde X^{\top}y$ where $\tilde w=[w;b]$. |
| **Statistical view**     | $\tilde w$ is the **ordinary least‑squares (OLS)** estimator = **MLE** under Gaussian noise; by **Gauss–Markov** it is BLUE (best linear unbiased) among all linear estimators. |                                                                                                       |
| **Generalisation**       | Risk decomposes into **bias² + variance + noise**. Ridge (λ‖w‖²) & Lasso (λ‖w‖₁) shrinkvariance in high‑dimensional $d\ggn$.                                                |                                                                                                       |
| **Optimisation**         | Gradient descent step: $w \leftarrow w - \eta(X^{\top}(Xw - y))/n$; converges linearly if $\eta < 2/\lambda_{\max}(X^{\top}X)$.                                               |                                                                                                       |
| **Diagnostics**          | *R²* =$1-\tfrac{\text{RSS}}{\text{TSS}}$; VIF detects multicollinearity.                                                                                                        |                                                                                                       |

---

### 1.1.5.3 Logistic Regression (Sigmoid Activation & Probabilistic View)

| Item                               | Formal description                                                                                                                                            |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hypothesis**                     | $p_\theta(y=1\mid x) = \sigma(w^{\top}x + b)$ with $\sigma(z)=\tfrac1{1+e^{-z}}$                                                                              |
| **Decision rule**                  | $\hat y = \mathbb{1}[p_\theta\ge 0.5]$ — same hyperplane as perceptron but **calibrated** probabilities.                                                      |
| **Loss (negative log‑likelihood)** | $\mathcal{L}(\theta)= -\sum_{i} \bigl[y^{(i)}\log p_i + (1-y^{(i)})\log(1-p_i)\bigr]$ = **binary cross‑entropy**                                              |
| **Convexity**                      | $\mathcal{L}$ is strictly convex ⇒ unique global minimiser.                                                                                                   |
| **Optimisation**                   | *Gradient*: $\nabla_w\mathcal{L}=X^{\top}(p-y)$.  *Newton/IRLS*: update $w\leftarrow w - (X^{\top}WX)^{-1}\nabla_w$ with $W=\operatorname{diag}(p_i(1-p_i))$. |
| **Statistical interpretation**     | **Generalised linear model (GLM)** with logit link; also the **maximum‑entropy** distribution on $\{0,1\}$ given fixed mean $w^{\top}x+b$.                    |
| **Regularisation**                 | Add $λ\|w\|_p^p$; $p=2$ (ridge) keeps convexity; $p=1$ induces sparsity.                                                                                      |
| **Calibration metrics**            | AUC‑ROC, log‑loss, Brier score; reliability diagrams display deviation from perfect calibration.                                                              |

**Asymptotics & Uncertainty**

* **Fisher information** $I(\theta)=X^{\top}WX$.  For large $n$, $\hat\theta$ is asymptotically normal with covariance $I^{-1}$.
* Wald & likelihood‑ratio tests enable feature significance assessment.

---

### Comparative Snapshot

| Criterion             | Perceptron                    | Linear Reg.                | Logistic Reg.                |
| --------------------- | ----------------------------- | -------------------------- | ---------------------------- |
| Output Range          | $\{-1,+1\}$                   | $\mathbb{R}$               | $[0,1]$                      |
| Loss Surface          | Piece‑wise linear, non‑convex | Quadratic, convex          | Convex (logistic)            |
| Probabilistic?        | ✗                             | Often assumed Gaussian     | ✓ (Bernoulli)                |
| Closed‑form?          | ✗                             | ✓                          | ✗ (iterative)                |
| Handles non‑sep. data | No (plain)                    | N/A                        | ✓                            |
| Typical Apps          | online classification         | forecasting, curve‑fitting | credit‑scoring, medical risk |

---

### Pitfalls & Remedies

| Symptom                               | Model      | Cause                                          | Fix                                               |
| ------------------------------------- | ---------- | ---------------------------------------------- | ------------------------------------------------- |
| Diverging perceptron updates          | Perceptron | Data not separable                             | Pocket algorithm or switch to logistic            |
| Exploding coefficients                | Linear     | Multicollinearity                              | Ridge/Lasso or feature PCA                        |
| Perfect separation ⇒ infinite weights | Logistic   | Rare but possible when data linearly separable | Add $L_2$ penalty or early stop NR iterations     |
| Poor calibration                      | Logistic   | Class‑imbalance                                | Use weighted loss or calibration (Platt/Isotonic) |

---

### Links to Later Sections

* **Softmax units (§ 1.1.6)** generalise logistic regression to $K>2$ classes.
* **Neural networks (§ Chapter 2)** stack logistic‑like units but train with back‑prop; logistic regression is depth‑0 baseline.

---

| Sub‑topic & gap                                   | Reference (chronological)                                                                                                          | Contribution & how to cite in text                                                                                   | ID               |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **Probability calibration & temperature scaling** |                                                                                                                                    |                                                                                                                      |                  |
| Sigmoid (Platt) scaling                           | *Probabilistic Outputs for Support Vector Machines* – Platt 1999 ([University of Colorado Boulder][1])                             | First single‑parameter sigmoid post‑hoc calibration; origin of modern temperature scaling.                           | Platt 1999       |
| Non‑parametric isotonic / multiclass              | Zadrozny & Elkan 2002 *Obtaining Calibrated Probability Estimates…* ([Computer Science at UCSD][2])                                | Introduces **isotonic regression** and **pairwise coupling** for multiclass calibration.                             | Zadrozny 2002    |
| Algorithm comparison                              | Niculescu‑Mizil & Caruana 2005 *Predicting Good Probabilities with Supervised Learning* ([Cornell Computer Science][3])            | Benchmarks Platt, isotonic, and Brier loss across 10 ML models; supports your “Calibration metrics” table.           | N‑M & C 2005     |
| Temperature scaling for DNNs                      | Guo et al. 2017 *On Calibration of Modern Neural Networks* ([Proceedings of Machine Learning Research][4])                         | Shows deep nets are mis‑calibrated and that a **single temperature** fixes it; core reference for your TS paragraph. | Guo 2017         |
| **Hierarchical & class‑based Softmax**            |                                                                                                                                    |                                                                                                                      |                  |
| Word‑class clustering                             | Goodman 2001 *A Bit of Progress in Language Modeling* (Tech. Rep.) ([prod-c2g.s3.amazonaws.com][5])                                | Popularised class‑based softmax; quote Eq. (4) to motivate “cluster first, softmax second”.                          | Goodman 2001     |
| Tree‑factorisation                                | Morin & Bengio 2005 *Hierarchical Probabilistic Neural Network Language Model* ([iro.umontreal.ca][6])                             | Gives binary **H‑softmax** with O(log K) complexity; canonical tree method.                                          | Morin 2005       |
| Scalable binary tree                              | Mnih & Hinton 2009 *A Scalable Hierarchical Distributed Language Model* ([U of T Computer Science][7])                             | Introduces **Huffman‑coded** trees that match unigram frequency ⇒ faster inference.                                  | Mnih‑Hinton 2009 |
| **Sampling & unnormalised objectives**            |                                                                                                                                    |                                                                                                                      |                  |
| Importance sampling pre‑cursor                    | Bengio & Senécal 2003 *Quick Training of Probabilistic NNs by Importance Sampling* ([Proceedings of Machine Learning Research][8]) | First large‑K **importance sampling** loss; complexity O(S) with S ≪ K.                                              | B\&S 2003        |
| Adaptive importance sampling                      | Bengio & Senécal 2008 *Adaptive Importance Sampling…* ([iro.umontreal.ca][9])                                                      | Learns proposal distribution on‑line; cite in “Adaptive sampling” footnote.                                          | AIS 2008         |
| Noise‑Contrastive Estimation                      | Gutmann & Hyvärinen 2010 *Noise‑Contrastive Estimation…* ([Proceedings of Machine Learning Research][10])                          | Provides statistical consistency for training **unnormalised** models; theoretical backbone for NCE‑softmax.         | NCE 2010         |
| NCE for NPLMs                                     | Mnih & Teh 2012 *Fast & Simple Algorithm for Training NPLMs* ([ICML][11])                                                          | Shows NCE outperforms importance sampling in language modelling; add to “Negative sampling vs NCE” box.              | Mnih‑Teh 2012    |
| Negative sampling                                 | Mikolov et al. 2013 *Efficient Estimation of Word Representations…* ([arXiv][12])                                                  | Popularised **k ≪ K** negative sampling in word2vec; link to your “Negative‑sampling original” bullet.               | Mikolov 2013     |
| Sampled Softmax for NMT                           | Jean et al. 2015 *On Using Very Large Target Vocabulary for NMT* ([ACL Anthology][13])                                             | Importance‑sampled softmax tailored to sequence‑to‑sequence; cite in “Sampled Softmax / NMT”.                        | Jean 2015        |
| Adaptive Softmax                                  | Grave et al. 2016 *Efficient Softmax Approximation for GPUs* ([david.grangier.info][14])                                           | **Adaptive cluster sizes** minimise GPU time; core of PyTorch `AdaptiveLogSoftmax`.                                  | Grave 2016       |

[1]: https://home.cs.colorado.edu/~mozer/Teaching/syllabi/6622/papers/Platt1999.pdf "[PDF] Probabilistic Outputs for Support Vector Machines and Comparisons ..."
[2]: https://cseweb.ucsd.edu/~elkan/calibrated.pdf "[PDF] Obtaining calibrated probability estimates from decision trees and ..."
[3]: https://www.cs.cornell.edu/~alexn/papers/calibration.icml05.crc.rev3.pdf "[PDF] Predicting Good Probabilities With Supervised Learning"
[4]: https://proceedings.mlr.press/v70/guo17a/guo17a.pdf "[PDF] On Calibration of Modern Neural Networks"
[5]: https://prod-c2g.s3.amazonaws.com/cs224n/Fall2012/files/goodman-2001.pdf "[PDF] A Bit of Progress in Language Modeling Extended Version - AWS"
[6]: https://www.iro.umontreal.ca/~lisa/pointeurs/hierarchical-nnlm-aistats05.pdf "[PDF] Hierarchical Probabilistic Neural Network Language Model"
[7]: https://www.cs.toronto.edu/~amnih/papers/hlbl_final.pdf "[PDF] A Scalable Hierarchical Distributed Language Model"
[8]: https://proceedings.mlr.press/r4/bengio03a/bengio03a.pdf "[PDF] Quick Training of Probabilistic Neural Nets by Importance Sampling"
[9]: https://www.iro.umontreal.ca/~lisa/pointeurs/importance_samplingIEEEtnn.pdf "[PDF] Adaptive Importance Sampling to Accelerate Training of a Neural ..."
[10]: https://proceedings.mlr.press/v9/gutmann10a/gutmann10a.pdf "[PDF] A new estimation principle for unnormalized statistical models"
[11]: https://icml.cc/2012/papers/855.pdf "[PDF] A fast and simple algorithm for training neural probabilistic language ..."
[12]: https://arxiv.org/pdf/1301.3781 "[PDF] Efficient Estimation of Word Representations in Vector Space - arXiv"
[13]: https://aclanthology.org/P15-1001.pdf "[PDF] On Using Very Large Target Vocabulary for Neural Machine ..."
[14]: https://david.grangier.info/papers/2017/grave-softmax-2017.pdf "[PDF] Efficient softmax approximation for GPUs - David Grangier"

| § 1.1.6 topic / gap                                | Reference (stable PDF / URL)                                                                                                  | Contribution & how to weave it in                                                                                                         | ID to cite   |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Probability calibration — Temperature & beyond** |                                                                                                                               |                                                                                                                                           |              |
|  Temperature‑scaling baseline                      | *On Calibration of Modern Neural Networks* – Guo et al., ICML 2017 ([Proceedings of Machine Learning Research][1])            | Introduces scalar “temperature” post‑hoc fit; defines **ECE** and reliability diagrams you can reuse in the *Calibration metrics* bullet. | Guo 2017     |
|  Dataset‑shift stress‑test                         | *Can You Trust Your Model’s Uncertainty?* – Ovadia et al., NeurIPS 2019 ([NeurIPS Proceedings][2])                            | Shows temperature scaling degrades under covariate shift; add to “Pitfalls” row.                                                          | Ovadia 2019  |
|  Multiclass Dirichlet calibration                  | *Beyond Temperature Scaling* – Kull et al., NeurIPS 2019 ([arXiv][3])                                                         | Extends beta‑calibration to K > 2 classes; cite where you mention alternatives to plain T‑scaling.                                        | Kull 2019    |
|  Label smoothing & calibration link                | *When Does Label Smoothing Help?* – Müller, Kornblith & Hinton 2019 ([arXiv][4])                                              | Empirically shows LS reduces over‑confidence; integrate in “Label Smoothing” box.                                                         | Müller 2019  |
|  Loss‑level fix                                    | *Calibrating DNNs with Focal Loss* – Mukhoti et al., NeurIPS 2020 ([NeurIPS Papers][5])                                       | Demonstrates focal‑loss improves ECE on imbalanced data; reference in “Class‑imbalance remedies”.                                         | Mukhoti 2020 |
|  Binary beta calibration (historical)              | *Beta Calibration* – Kull et al., 2017 ([ResearchGate][6])                                                                    | Give readers a closed‑form 2‑parameter alternative to Platt scaling; useful for Appendix code snippet.                                    | BetaCal 2017 |
| **Large‑K softmax approximations**                 |                                                                                                                               |                                                                                                                                           |              |
|  Hierarchical Softmax (classic)                    | *Hierarchical Probabilistic NN Language Model* – Morin & Bengio 2005 ([iro.umontreal.ca][7])                                  | Supplies tree‑factorisation formulas and complexity O(log K); embed after your “Hierarchical Softmax” bullet.                             | Morin 2005   |
|  Adaptive Softmax (GPU‑optimised)                  | *Efficient Softmax Approximation for GPUs* – Grave et al., 2017 ([arXiv][8])                                                  | Gives cluster sizing rule & time/accuracy tables; cite in “Adaptive Softmax” paragraph.                                                   | Grave 2017   |
|  Learned Softmax Trees                             | *Adaptive Softmax Trees for Many‑Class Classification* – Daghaghi et al., ICLR 2024 (OpenReview) ([OpenReview][9])            | Shows end‑to‑end tree growth beats fixed H‑softmax; include in “Recent advances” side‑bar.                                                | AST 2024     |
|  Negative‑sampling original                        | *Efficient Estimation of Word Representations* – Mikolov et al., 2013 ([arXiv][10])                                           | Provides the **negative sampling** objective and empirical speedups; cite under “Negative sampling”.                                      | Mikolov 2013 |
|  Noise‑Contrastive Estimation (theory)             | *Noise‑Contrastive Estimation of Unnormalised Models* – Gutmann & Hyvärinen 2010 ([Journal of Machine Learning Research][11]) | Supplies statistical consistency proof; link to “NCE vs Sampled Softmax” comparison.                                                      | NCE 2010     |
|  NCE for neural LMs                                | *Fast & Simple Algorithm for NPLMs* – Mnih & Teh 2012 ([ICML][12])                                                            | Practical recipe for replacing full softmax in language models; add code pointer.                                                         | Mnih 2012    |
|  Sampled Softmax in NMT                            | *On Using Very Large Target Vocabulary for NMT* – Jean et al., ACL 2015 ([ACL Anthology][13])                                 | Popular importance‑sampling “sampled softmax”; cite after your complexity table.                                                          | Jean 2015    |
|  BlackOut sampling                                 | *BlackOut: Speeding‑Up RNNLMs* – Ji et al., 2016 ([ResearchGate][14])                                                         | Shows discriminative sampling reduces variance vs NCE; good for “Trade‑offs” table.                                                       | Ji 2016      |
|  Sparse alternatives                               | *From Softmax to Sparsemax* – Martins & Astudillo 2016 ([arXiv][15])                                                          | Introduces **sparsemax**; mention as route to output sparsity without sampling.                                                           | Martins 2016 |
|  α‑Entmax generalisation                           | *Sparse Sequence‑to‑Sequence Models* – Peters et al., ACL 2019 ([arXiv][16])                                                  | Extends sparsemax; quote for “Sparse ∝ Beam‑search efficiency” remark.                                                                    | Peters 2019  |

[1]: https://proceedings.mlr.press/v70/guo17a/guo17a.pdf "[PDF] On Calibration of Modern Neural Networks"
[2]: https://proceedings.neurips.cc/paper/9547-can-you-trust-your-models-uncertainty-evaluating-predictive-uncertainty-under-dataset-shift.pdf "[PDF] Can you trust your model's uncertainty? Evaluating predictive ..."
[3]: https://arxiv.org/abs/1910.12656 "Beyond temperature scaling: Obtaining well-calibrated multiclass ..."
[4]: https://arxiv.org/abs/1906.02629 "When Does Label Smoothing Help?"
[5]: https://papers.neurips.cc/paper/2020/file/aeb7b30ef1d024a76f21a1d40e30c302-Paper.pdf "[PDF] Calibrating Deep Neural Networks using Focal Loss"
[6]: https://www.researchgate.net/publication/320394380_Beta_calibration_a_well-founded_and_easily_implemented_improvement_on_logistic_calibration_for_binary_classifiers "Beta calibration: a well-founded and easily implemented ..."
[7]: https://www.iro.umontreal.ca/~lisa/pointeurs/hierarchical-nnlm-aistats05.pdf "[PDF] Hierarchical Probabilistic Neural Network Language Model"
[8]: https://arxiv.org/abs/1609.04309 "Efficient softmax approximation for GPUs"
[9]: https://openreview.net/pdf?id=WK7rXij5VC "[PDF] Adaptive Softmax Trees for Many-Class Classification - OpenReview"
[10]: https://arxiv.org/pdf/1301.3781 "[PDF] Efficient Estimation of Word Representations in Vector Space - arXiv"
[11]: https://www.jmlr.org/papers/volume13/gutmann12a/gutmann12a.pdf "[PDF] Noise-Contrastive Estimation of Unnormalized Statistical Models ..."
[12]: https://icml.cc/2012/papers/855.pdf "[PDF] A fast and simple algorithm for training neural probabilistic language ..."
[13]: https://aclanthology.org/P15-1001.pdf "[PDF] On Using Very Large Target Vocabulary for Neural Machine ..."
[14]: https://www.researchgate.net/publication/284788422_BlackOut_Speeding_up_Recurrent_Neural_Network_Language_Models_With_Very_Large_Vocabularies "(PDF) BlackOut: Speeding up Recurrent Neural Network Language ..."
[15]: https://arxiv.org/abs/1602.02068 "From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification"
[16]: https://arxiv.org/abs/1905.05702 "Sparse Sequence-to-Sequence Models"

## 1.1.6 Multiclass Extensions: Softmax Units and One‑vs‑Rest Schemes

Multiclass problems involve labels $y\in\{1,\dots,K\}$ with $K>2$.  Two main paradigms coexist.

### 1 Single‑Vector Coupled Models — Softmax / Multinomial Logistic Regression

**Hypothesis**

$$
p_\theta(y=k\mid x)=\frac{\exp(w_k^{\top}x+b_k)}{\sum_{j=1}^{K}\exp(w_j^{\top}x+b_j)},\quad
\theta=\{(w_k,b_k)\}_{k=1}^{K}.
$$

*Affine core* : $z_k=w_k^{\top}x+b_k$ (*logits*).
*Activation* : **Softmax** $\sigma_{\text{sm}}:\mathbb{R}^{K}\to(0,1)^{K}$ where $[\sigma_{\text{sm}}(z)]_k=\exp(z_k)/\sum_j\exp(z_j)$.

**Loss**

$$
\mathcal{L}(\theta)= -\sum_{i=1}^{n}\log p_\theta\bigl(y^{(i)}\mid x^{(i)}\bigr)
      = \sum_{i}\bigl[-z_{y^{(i)}}^{(i)} + \log\sum_{j}\exp z_j^{(i)}\bigr].
$$

This **cross‑entropy** is convex in $\theta$, admits gradient

$$
\nabla_{w_k}\mathcal{L}= \sum_{i}(p_{ik}-\mathbb{1}_{y^{(i)}=k})x^{(i)}.
$$

**Numerical Stability**

Use **log‑sum‑exp trick**

$$
\log\sum_j e^{z_j} = m + \log\sum_j e^{z_j-m},\quad m=\max_j z_j,
$$

avoiding overflow when $\lVert z\rVert_\infty\gg0$.

**Calibration & Temperature**

Softmax inherently produces a **probability simplex**; temperature scaling $z\mapsto z/T$ with $T>0$ controls confidence.  $T>1$ yields softer targets (knowledge distillation); $T<1$ sharpens decisions.

**Label Smoothing**

Replace one‑hot target $y$ by mixture $(1-\varepsilon)\delta_{y}+\varepsilon/K$ to prevent over‑confidence and improve generalisation.

---

### 2 Decoupled Binary Strategies

| Strategy                                 | Classifiers trained                                            | Prediction        | Pros                                   | Cons                                                         |
| ---------------------------------------- | -------------------------------------------------------------- | ----------------- | -------------------------------------- | ------------------------------------------------------------ |
| **One‑vs‑Rest (OvR)**                    | $K$ sigmoids: $p_k=\sigma(w_k^{\top}x+b_k)$                    | $\arg\max_k p_k$  | Parallel, scalable                     | Scores uncalibrated across classes; ‖w\_k‖ norms may distort |
| **One‑vs‑One (OvO)**                     | $\binom{K}{2}$ pairwise classifiers                            | Plurality vote    | Good for SVMs; smaller class imbalance | $\Theta(K^{2})$ models; vote ties                            |
| **Error‑Correcting Output Codes (ECOC)** | $L$ binary tasks defined by code matrix $C_{k\ell}\in\{\pm1\}$ | Min Hamming dist. | Robust to classifier noise             | Design of $C$ non‑trivial                                    |

> **Theoretical Note** ECOC margin ≥ $\rho$ implies multiclass margin ≥ $\rho/\sqrt{L}$ (Allwein 2000), linking binary robustness to overall error.

---

### 3 Hierarchical Softmax & Negative Sampling (Large K)

When $K$ ≳ 10⁴ (word vocabularies, recommender items), computing denom.$\sum_j e^{z_j}$ is costly.

| Technique                               | Complexity      | Idea                                                                 |
| --------------------------------------- | --------------- | -------------------------------------------------------------------- |
| **Hierarchical Softmax**                | $O(\log K)$     | Organise classes in binary tree; path prob. multiplies node sigmoids |
| **Sampled Softmax / Noise‑Contrastive** | $O(S)$          | Approximate loss using target + $S$ negatives                        |
| **Adaptive Softmax**                    | $O(d+\sqrt{K})$ | Frequent classes get own partition; rare grouped                     |

---

### 4 Margin‑Enhanced Softmax Variants (Deep Face, ArcFace etc.)

Replace logits by $z_k = \lVert w_k\rVert\lVert x\rVert(\cos\theta_k - m)$ with angular margin $m$.  Improves inter‑class separability in embeddings (face recognition).

---

### 5 Pitfalls & Diagnostics

| Symptom                       | Likely cause         | Remedy                                                      |
| ----------------------------- | -------------------- | ----------------------------------------------------------- |
| Predicted probs sum > 1 (OvR) | Independent sigmoids | Calibrate scores (softmax on logits)                        |
| Softmax outputs nan           | Logits overflow      | Center logits, use float‑32 exp clamp                       |
| Poor rare‑class recall        | Data imbalance       | Class‑balanced loss or focal loss $(1-p_t)^\gamma \log p_t$ |
| Ambiguous near‑ties           | OvO voting tie       | Use tie‑breaking by distance to decision hyperplanes        |

---

| Sub‑topic & gap you flagged                          | Classical reference                                                                    | Contribution & how to weave it into the manuscript                                                          | ID to cite                         |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Foundational STDP experiments & theory**           |                                                                                        |                                                                                                             |                                    |
| First pairing‑based STDP in neocortex                | Markram et al., *Science* 1997 (summarised in “History of STDP”) – plots LTP/LTD vs Δt | Anchor the opening paragraph that STDP links Hebb to precise millisecond timing.                            | ([PMC][1])                         |
| Cultured‑neuron timing curve                         | Bi & Poo 1998, *J. Neurosci.*                                                          | Supplies the canonical exponential fit used in your Figure 1 timing window.                                 | ([PubMed][2])                      |
| Competitive Hebbian model                            | Song, Miller & Abbott 2000, *Nat. Neurosci.*                                           | Demonstrates how STDP induces synaptic competition; cite in § 1 bullet “Layer‑wise Composition”.            | ([Nature][3])                      |
| Frequency‑dependent **triplet rule**                 | Pfister & Gerstner 2006, *J. Neurosci.*                                                | Extend pair‑rule box with triplet formalism (Δt\_1, Δt\_2) that matches in‑vitro data.                      | ([The Journal of Neuroscience][4]) |
| **Three‑factor / neuromodulated plasticity**         |                                                                                        |                                                                                                             |                                    |
| Reinforcement learning via stochastic synapses       | Seung 2003, *Neuron*                                                                   | First gradient‑estimate “reward‑modulated STDP”; drop into “STDP + dopamine” paragraph.                     | ([PubMed][5])                      |
| Dopamine‑gated STDP (distal‐reward)                  | Izhikevich 2007, *PNAS*                                                                | Classic “solving the distal‑reward problem” model; cite in neuromodulation row of Table 7.                  | ([PubMed][6])                      |
| Dendritic prediction error rule                      | Urbanczik & Senn 2014, *Neuron*                                                        | Early demonstration that local dendritic voltages act as a third factor; good for “local learning” sidebar. | ([PubMed][7])                      |
| **Energy‑efficient neuromorphic hardware**           |                                                                                        |                                                                                                             |                                    |
| Birth of the field                                   | Mead 1990, *Proc. IEEE* “Neuromorphic Electronic Systems”                              | Quote for historical box contrasting analog sub‑threshold with digital FLOPs.                               | ([hasler.ece.gatech.edu][8])       |
| Low‑power silicon retina & “Neuromorphic Microchips” | Boahen 2005, *Scientific American*                                                     | Supplies early watt‑level power figures; enrich “Energy Use” comparison to brain.                           | ([Computer Science][9])            |
| Review of silicon neuron circuits                    | Indiveri et al. 2011, *Frontiers Neuro.*                                               | Use for the “Synaptic plasticity diversity” row—lists hardware STDP implementations.                        | ([Frontiers][10])                  |
| Million‑neuron digital ASIC                          | Merolla et al. 2014, *Science* (TrueNorth)                                             | Provides 46 Gsyn‑ops/W benchmark; cite in energy table.                                                     | ([Science][11])                    |
| Massively parallel ARM array                         | Furber et al. 2012, *J. Parallel Distrib. Sys.* (SpiNNaker)                            | Supplies scalable packet router & 1 W per 18‑core chip numbers; place in hardware timeline.                 | ([ScienceDirect][12])              |
| Mixed‑analog Neurogrid                               | Benjamin et al. 2014, *IEEE Proc.*                                                     | Demonstrates < 5 W real‑time simulation of 1 M neurons; include in “Hardware Efficiency” bullet.            | ([Stanford University][13])        |

[1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3187646/ "A History of Spike-Timing-Dependent Plasticity - PubMed Central"
[2]: https://pubmed.ncbi.nlm.nih.gov/9852584/ "dependence on spike timing, synaptic strength, and postsynaptic ..."
[3]: https://www.nature.com/articles/nn0900_919 "Competitive Hebbian learning through spike-timing-dependent ..."
[4]: https://www.jneurosci.org/content/26/38/9673 "Triplets of Spikes in a Model of Spike Timing-Dependent Plasticity"
[5]: https://pubmed.ncbi.nlm.nih.gov/14687542/ "Learning in Spiking Neural Networks by Reinforcement of Stochastic ..."
[6]: https://pubmed.ncbi.nlm.nih.gov/17220510/ "Solving the distal reward problem through linkage of STDP and ..."
[7]: https://pubmed.ncbi.nlm.nih.gov/24507189/ "Learning by the dendritic prediction of somatic spiking - PubMed"
[8]: https://hasler.ece.gatech.edu/Published_papers/Technology_overview/MeadNeuro1990.pdf "[PDF] Neuromorphic electronic systems - Proceedings of the IEEE"
[9]: https://www.cs.unc.edu/~montek/teaching/Comp740-Fall16/EmergingTech/Neuromorphic/SciAm-Boahen.pdf "[PDF] Neuromorphic Microchips - Computer Science"
[10]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2011.00073/full "Neuromorphic Silicon Neuron Circuits - Frontiers"
[11]: https://www.science.org/doi/10.1126/science.1254642 "A million spiking-neuron integrated circuit with a scalable ... - Science"
[12]: https://www.sciencedirect.com/science/article/abs/pii/S0743731512000287 "Scalable communications for a million-core neural processing ..."
[13]: https://web.stanford.edu/group/brainsinsilicon/documents/BenjaminEtAlNeurogrid2014.pdf "[PDF] Neurogrid: A Mixed-Analog-Digital Multichip System for Large-Scale ..."


| § 1.1.7 gap to fill                                  | Reference (stable PDF/URL)                                                                  | Why it matters & how to weave it in                                                                               | ID to cite        |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------- |
| **Empirical foundations of STDP**                    | Bi & Poo 1998 *J. Neurosci.* – first quantitative “Hebbian time‑window” curve ([PubMed][1]) | Grounds the historical note that STDP emerged from hippocampal slice experiments.                                 | BiPoo 1998        |
|                                                      | Markram et al. 2012 *STDP: A Comprehensive Overview* (review) ([PMC][2])                    | Supplies exhaustive parameter ranges & species comparisons for Table “Biological mapping”.                        | Markram 2012      |
|                                                      | Pfister & Gerstner 2006 *Triplet STDP* ([The Journal of Neuroscience][3])                   | Introduces the **triplet rule** that explains frequency‑dependence; include maths box under “I\&F vs Perceptron”. | Pfister 2006      |
| **Three‑factor / neo‑Hebbian plasticity**            | Frémaux & Gerstner 2016 *Neuromodulated STDP & 3‑factor rules* ([PubMed][4])                | Formalises eligibility + dopamine term; cite in Table “Synaptic plasticity” row.                                  | Fremaux 2016      |
|                                                      | Urbanczik & Senn 2014 (dendritic prediction) – already cited in draft?                      | Links dendritic voltage to error term; optional deep‑dive box.                                                    | —                 |
| **Local approximations to back‑prop**                | Lillicrap et al. 2016 *Random Feedback Alignment* ([Nature][5])                             | Supports claim that sign‑constrained weights can still transmit error.                                            | Lillicrap 2016    |
|                                                      | Scellier & Bengio 2017 *Equilibrium Propagation* ([arXiv][6])                               | Energy‑based gradient with one physics‑like relaxation; add to “Why analogy helps” bullet.                        | Scellier 2017     |
|                                                      | Whittington & Bogacz 2017 *Predictive‑Coding ≈ Back‑prop* ([PubMed][7])                     | Gives a proof that predictive coding updates converge to BP; enrich “Local learning” paragraph.                   | WB 2017           |
|                                                      | GAIT‑prop (Target Prop derivatives) – NeurIPS 2020 ([proceedings.nips.cc][8])               | Modern local rule; mention as “recent progress” footnote.                                                         | GAIT‑prop 2020    |
|                                                      | Meta‑learning plasticity rules (Nature 2023) ([Nature][9])                                  | Showcases data‑driven discovery of plausible rules; use in “Why it breaks down → diversity”.                      | Meta‑Learn 2023   |
| **Surrogate‑gradient SNN training**                  | Neftci et al. 2019 *Surrogate Gradient Learning in SNNs* (tutorial) ([arXiv][10])           | Supplies algorithms & code pointers; cite under “Spiking Neural Networks”.                                        | Neftci 2019       |
|                                                      | Zenke & Vogels 2021 *Robustness of Surrogate Gradients* ([PubMed][11])                      | Quantifies success regions; informs “Derivative range” bullet.                                                    | Zenke 2021        |
| **Digital neuromorphic hardware**                    | Davies et al. 2018 *Loihi: A Neuromorphic Many‑Core Processor* ([redwood.berkeley.edu][12]) | Architecture + on‑chip learning benchmarks; cite in hardware table.                                               | Loihi 2018        |
|                                                      | Intel 2021 *Loihi‑2 Tech Brief* ([download.intel.com][13])                                  | Lists expanded neuron model & 14 nm→Intel 4 shrink; update energy footnote.                                       | Loihi2 2021       |
|                                                      | Loihi‑2 energy study 2024 (103 GOPS/W) ([arXiv][14])                                        | Supplies concrete efficiency numbers for comparison chart.                                                        | Loihi2 Energy     |
|                                                      | Intel “Hala Point” 1,152‑chip system (15 TOPS/W) 2024 ([Intel Newsroom][15])                | Shows cluster‑scale efficiency; add to “Future outlook”.                                                          | HalaPoint 2024    |
|                                                      | IBM TrueNorth design (46 GSOPS/W, 70 mW) ([redwood.berkeley.edu][16])                       | Classic CMOS spiking ASIC; insert in energy comparison row.                                                       | TrueNorth 2015    |
|                                                      | SpiNNaker 1‑M‑core system 2019 ([Frontiers][17])                                            | Demonstrates ARM‑based massively parallel event routing; cite for “heavy recurrence” remark.                      | SpiNNaker 2019    |
|                                                      | SpiNNaker‑2 overview 2024 ([arXiv][18])                                                     | Adds 22 nm silicon & on‑chip plasticity; update hardware timeline.                                                | SpiNNaker2 2024   |
|                                                      | BrainScaleS‑2 hybrid analog‑digital wafer 2022 ([Frontiers][19])                            | Provides accelerated‑time analog neurons; link to “timescale mismatch” discussion.                                | BrainScaleS2 2022 |
|                                                      | Benchmarking suite for neuromorphic energy 2022 ([PMC][20])                                 | Supplies unified joules/op metrics; perfect for Figure “Energy vs Throughput”.                                    | Bench‑NMC 2022    |
|                                                      | Nature Review 2021 *Opportunities for Neuromorphic Computing* ([Nature][21])                | High‑level survey; good as first reading suggestion at end of § 1.1.7.                                            | NatureReview 2021 |
| **Event‑driven sensors (biological retina analogy)** | Event‑camera overview (Dynamic Vision Sensor) ([Wikipedia][22])                             | Use to illustrate axon‑like asynchronous signalling in hardware sidebar.                                          | DVS Review        |

[1]: https://pubmed.ncbi.nlm.nih.gov/9852584/ "dependence on spike timing, synaptic strength, and postsynaptic ..."
[2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3395004/ "Spike-Timing-Dependent Plasticity: A Comprehensive Overview - PMC"
[3]: https://www.jneurosci.org/content/26/38/9673 "Triplets of Spikes in a Model of Spike Timing-Dependent Plasticity"
[4]: https://pubmed.ncbi.nlm.nih.gov/26834568/ "Neuromodulated Spike-Timing-Dependent Plasticity, and ... - PubMed"
[5]: https://www.nature.com/articles/ncomms13276 "Random synaptic feedback weights support error backpropagation ..."
[6]: https://arxiv.org/abs/1602.05179 "Equilibrium Propagation: Bridging the Gap Between Energy-Based ..."
[7]: https://pubmed.ncbi.nlm.nih.gov/28333583/ "An Approximation of the Error Backpropagation Algorithm ... - PubMed"
[8]: https://proceedings.nips.cc/paper/2020/file/7ba0691b7777b6581397456412a41390-Paper.pdf "[PDF] GAIT-prop: A biologically plausible learning rule derived from ... - NIPS"
[9]: https://www.nature.com/articles/s41467-023-37562-1 "Meta-learning biologically plausible plasticity rules with random ..."
[10]: https://arxiv.org/abs/1901.09948 "Surrogate Gradient Learning in Spiking Neural Networks - arXiv"
[11]: https://pubmed.ncbi.nlm.nih.gov/33513328/ "The Remarkable Robustness of Surrogate Gradient Learning for ..."
[12]: https://redwood.berkeley.edu/wp-content/uploads/2021/08/Davies2018.pdf "[PDF] Loihi: A Neuromorphic Manycore Processor with On-Chip Learning"
[13]: https://download.intel.com/newsroom/2021/new-technologies/neuromorphic-computing-loihi-2-brief.pdf "[PDF] Taking Neuromorphic Computing to the Next Level with Loihi 2 - Intel"
[14]: https://arxiv.org/html/2408.16096v1 "Accelerating Sensor Fusion in Neuromorphic Computing - arXiv"
[15]: https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai "Intel Builds World's Largest Neuromorphic System to Enable More ..."
[16]: https://redwood.berkeley.edu/wp-content/uploads/2021/08/Akopyan2015.pdf "[PDF] TrueNorth: Design and Tool Flow of a 65 mW 1 Million Neuron ..."
[17]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2019.00231/full "SpiNNTools: The Execution Engine for the SpiNNaker Platform"
[18]: https://arxiv.org/html/2401.04491v1 "SpiNNaker2: A Large-Scale Neuromorphic System for Event-Based ..."
[19]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.795876/full "The BrainScaleS-2 Accelerated Neuromorphic System With Hybrid ..."
[20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9201569/ "Benchmarking Neuromorphic Hardware and Its Energy Expenditure"
[21]: https://www.nature.com/articles/s43588-021-00184-y "Opportunities for neuromorphic computing algorithms and applications"
[22]: https://en.wikipedia.org/wiki/Event_camera "Event camera"

## 1.1.7 Biological Analogy: Dendrites → Sum, Soma → Activation, Axon → Output

Artificial neurons were *inspired* by neuroscience but key differences abound.

| Biological neuron                                                                                                                  | Artificial analogue                                                                            | Caveats                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Dendrites** collect electro‑chemical **post‑synaptic potentials (PSPs)** from ≈ 10³–10⁵ synapses.                                | Weighted sum $w^{\top}x$.                                                                      | Real dendrites have non‑linear, location‑dependent integration and active ion channels. |
| **Soma** integrates voltage; fires all‑or‑nothing **action potential** at threshold ≈ −55 mV.                                      | Activation function $\sigma(z)$.  Perceptron ≈ hard threshold, ReLU ≈ half‑wave rectification. | Biological spike is discrete in time; rate‑coding vs spike‑timing debated.              |
| **Axon** propagates spike to downstream synapses after \~1 ms refractory.                                                          | Neuron output $y$.                                                                             | No refractory in ANN; outputs continuous (rates) by default.                            |
| **Synaptic plasticity** via long‑term potentiation/depression (LTP/LTD), governed by **Spike‑Timing‑Dependent Plasticity (STDP)**. | Gradient‑based weight update.                                                                  | STDP local in time; back‑prop global, non‑causal in biology.                            |
| **Neuro‑transmitter types**: excitatory (glutamate) vs inhibitory (GABA).                                                          | Positive vs negative weights.                                                                  | Inhibition often spatially segregated; ANNs allow arbitrary sign per synapse.           |
| **Network motifs**: recurrent, layered cortex columns, sparse connectivity.                                                        | Deep feed‑forward or recurrent nets.                                                           | Biological wiring 3‑D, heavy recurrence; ANNs mostly layered 2‑D matrices.              |

### 1 Integrate‑and‑Fire (I\&F) vs Perceptron

*I\&F equation*

$$
C_m\frac{dV}{dt}= -g_L(V-E_L)+\sum_i w_i s_i(t),
$$

threshold‑crossing triggers spike, $V\to V_{\text{reset}}$.
Perceptron abstracts away dynamics, keeping only steady‑state threshold.

### 2 Rate Coding ≈ Sigmoid

If spike train is Poisson with rate $r(z)$, mapping $z$ (membrane dep.) → firing rate, the sigmoid fits experimental rate–current curves of cortical neurons.

### 3 Why the Analogy Helps

1. **Weight sign constraints**: *Dale’s law* (neuron is exclusively excit. or inhib.) inspires modern research on biologically‑plausible nets with sign‑constrained weights.
2. **Local learning**: STDP motivates **Hebbian** or **Oja’s rule** as unsupervised alternatives to back‑prop.
3. **Temporal coding**: Spiking Neural Networks (SNNs) approximate I\&F to exploit event‑driven, low‑power hardware.

### 4 Why It Breaks Down

* **Timescales**: Biophysics operates on ms and nm; ANN operates on real‑number algebra ignoring time.
* **Energy Use**: Biological neuron spikes cost ≈ 2 × 10⁹ ATP/day; ANN FLOPs differ by orders‑of‑magnitude and energy type.
* **Plasticity diversity**: Dozens of neuromodulators (dopamine, serotonin) implement meta‑learning—rarely modelled in standard back‑prop nets.

### 5 Ethical & Interpretability Lens

Citing “brain‑like” may mislead stakeholders.  Clarify **metaphor vs mechanism** when communicating capabilities; avoid neurohype.

---


## 1.1 Cross‑Section Integration & Consistency Notes

| Symbol             | Meaning                | First defined    | Also used in   | Consistency check  |
| ------------------ | ---------------------- | ---------------- | -------------- | ------------------ |
| $x\in\mathbb{R}^d$ | Input / feature vector | § 1.1.1          | all            | ✓                  |
| $w,b$              | Weights, bias          | § 1.1.1          | §§ 1.1.2‑1.1.6 | ✓                  |
| $z=w^{\top}x+b$    | Pre‑activation         | § 1.1.1          | §§ 1.1.2‑1.1.6 | ✓                  |
| $\sigma$           | Activation function    | § 1.1.2 intro    | § 1.1.3        | ✓ (non‑polynomial) |
| $\hat y$           | Model output           | § 1.1.5          | §§ 1.1.6       | ✓                  |
| $p_\theta$         | Predicted class prob.  | § 1.1.5.3        | § 1.1.6        | ✓                  |
| $\mathcal{L}$      | Loss (objective)       | first in § 1.1.5 | §§ 1.1.5‑1.1.6 | ✓                  |

All duplicate symbols now match; no conflicts detected.

---

### Cross‑Reference Map (how pieces fit together)

1. **Affine core (§ 1.1.1)** → sets foundation of *linear* transformation; referenced by

   * necessity of non‑linearity (§ 1.1.2, “stacking affine maps collapses”).

2. **Non‑linearity/UAT (§ 1.1.2)** → motivates inventory of activations (§ 1.1.3).

   * XOR example (§ 1.1.2) is revisited as geometric tiling in § 1.1.4.

3. **Activation taxonomy (§ 1.1.3)** → informs gradient/vanishing‑gradient discussions in

   * perceptron vs logistic regression (§ 1.1.5)
   * softmax temperature scaling (§ 1.1.6).

4. **Geometry (§ 1.1.4)** bridges to

   * margin analysis of perceptron (§ 1.1.5.1)
   * margin‑enhanced softmax variants (§ 1.1.6).

5. **Classical single‑neuron models (§ 1.1.5)** serve as

   * baseline for multiclass (§ 1.1.6)
   * historical link to biological thresholding (§ 1.1.7).

6. **Multiclass extensions (§ 1.1.6)** rely on

   * same affine+activation kernel as earlier sections; probability calibration echoes logistic regression.

7. **Biological analogy (§ 1.1.7)** circles back to

   * activation shapes: ReLU ≈ half‑wave rectification (retina), sigmoid ≈ firing‑rate curve.

---

### Closing Remarks

*Section 1.1* has progressed from **microscopic** (single affine map) to **macroscopic** (networks, biology).
Key intellectual arc:

1. **Linear skeleton** (affine maps)
2. **Necessity & theory of non‑linearity** (UAT)
3. **How to choose the non‑linearity** (activation zoo)
4. **What geometry those choices create** (polytopes & margins)
5. **Canonical instantiations** (perceptron, linear, logistic)
6. **Scaling beyond two classes** (softmax & coding schemes)
7. **Biological grounding & divergence**.

Together they equip the reader to understand why *deep* models matter and what goes wrong when any building block is missing.

---

### Suggested Further Reading

| Topic                     | Reference                                        | Why                                 |
| ------------------------- | ------------------------------------------------ | ----------------------------------- |
| Stone–Weierstrass & UAT   | G. Cybenko (1989), *Math. Control Signals Syst.* | Proof details for § 1.1.2           |
| Expressive power of depth | M. Telgarsky (2016), *COLT*                      | Exponential region counts (§ 1.1.4) |
| Margin theory             | Cortes & Vapnik (1995), *SVM original*           | Links to § 1.1.4/1.1.5              |
| Softmax calibration       | Guo et al. (2017), *ICML*                        | Extends § 1.1.6 temperature scaling |
| Spiking neuron models     | Gerstner & Kistler (2002)                        | Deep dive after § 1.1.7             |

---

### Exercises (for self‑check)

1. **Geometry**: Prove that a single ReLU neuron divides $\mathbb{R}^{d}$ into two half‑spaces but outputs *zero* on one side; derive VC‑dimension of this restricted hypothesis.
2. **UAT numerics**: Construct a two‑layer tanh network approximating $g(x)=\sin(\pi x)$ on $[0,1]$ within $\varepsilon=0.01$; estimate width needed via Chebyshev polynomials.
3. **Logistic vs Softmax**: Show that binary softmax reduces to logistic regression and yields identical gradient updates (derive algebraically).
4. **Margin Perceptron**: Implement perceptron with margin $\delta$; empirically verify convergence bound $\bigl(\tfrac{R}{\delta}\bigr)^2$ on a 2‑D separable dataset.
5. **Biological mapping**: Compare derivative of sigmoid at $z=0$ with experimentally measured firing‑rate gain of pyramidal neurons; discuss discrepancies.

---
