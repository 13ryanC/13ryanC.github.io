---
date: "2025-07-11"
title: "Entropy- or KL-regularised RL and the mirror-descent view"
summary: "Entropy- or KL-regularised RL and the mirror-descent view"
lastmod: "2025-07-11"
category: "Notes"
series: ["RL Theory", "RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


Below is a non‑exhaustive “menu” of research directions in **reinforcement‑learning (RL) theory** that play a role for RL analogous to

* **Neural‑network approximation theory** (expressivity, finite‑sample guarantees), and
* **Mode‑connectivity/landscape geometry** (global structure of the optimization landscape)

in supervised deep learning.  For each topic I give a concise formal definition or canonical problem statement, summarize hallmark theorems, indicate why the community views it as fundamental, and mention promising open sub‑questions.

---

### 1. PAC‑MDP **sample‑complexity theory**

**Problem.**  Let an episodic MDP \(M=(\mathcal S,\mathcal A,P,r,H)\).  An algorithm is **PAC‑MDP(\(\varepsilon,\delta\))** if with probability \(1-\delta\) it returns a policy \(\pi\) whose value loss is \(\le\varepsilon\) after at most \(N(\varepsilon,\delta,|\mathcal S|,|\mathcal A|,H)\) interactions.

**Key results.**

* Optimal horizon‑dependent bound \(N=\tilde O\!\big(H^2|\mathcal S||\mathcal A|/\varepsilon^2\big)\) and matching lower bound were “settled’’ in late‑2023 ([Google Sites][1]).
* Tabular results now extend to linear function classes and generalized feature maps; a precise analogy of VC‑dimension or Barron norms is still open.

**Why it matters.**  This is the RL counterpart of universal approximation plus generalization bounds: it tells us *how many episodes are information‑theoretically necessary* to learn an \(\varepsilon\)-optimal behaviour policy.

---

### 2. **Regret minimization** and **rate‑optimal online RL**

For a continuing MDP with unknown dynamics, the **cumulative regret** after \(T\) steps is

$$
\text{Regret}(T)=\sum_{t=1}^T\!\bigl(V^\ast(s_t)-r_t\bigr).
$$

* The UCRL2 framework achieves \(\tilde O\!\bigl(D|\mathcal S|\sqrt{|\mathcal A|T}\bigr)\) regret, and a *matching lower bound* up to logs shows the dependence on the MDP diameter \(D\) is unavoidable ([Journal of Machine Learning Research][2], [NeurIPS Proceedings][3]).
* Follow‑ups (EULER, UCRL3) tighten constants and introduce **variance‑aware** confidence sets ([arXiv][4]).

Regret analysis in RL plays the same role that *optimization‑error* analysis plays for deep networks, quantifying best‑possible learning rates under exploration constraints.

---

### 3. Convergence and geometry of **policy‑gradient (PG) methods**

Analogous to studying the loss surface of supervised networks:

* **Gradient domination**: in stochastic linear‑quadratic control, the performance gap is upper‑bounded by a constant times \(\|\nabla_\theta J(\theta)\|^2\), leading to **global linear convergence** of PG and natural PG ([arXiv][5]).
* **Occupancy‑based and mirror‑descent PG** yield oracle‑efficient, variance‑reduced estimators with provable \(\tilde O(1/T)\) optimality gap under general function approximation ([NeurIPS Proceedings][6]).

Open analogue of “mode connectivity’’: Does the set of near‑optimal policy parameters form a connected manifold for common architectures?  Preliminary evidence is anecdotal, but the **gradient‑domination plus low‑rank structure** hints at similar geometry.

---

### 4. **Distributional RL**

Instead of the scalar value \(V^\pi(s)\), learn the **return distribution** \(Z^\pi(s)\).

* Bellemare et al. proved a **Wasserstein contraction** of the distributional Bellman operator, guaranteeing convergence of categorical or quantile approximations ([arXiv][7]).
* A full monograph (MIT Press, 2023) collects theory tying distributional learning to risk‑sensitive control and representation learning ([distributional-rl.org][8]).

Significance: just as approximation theory broadened our view from function value to function class, distributional analysis broadens RL from expectation to full stochastic predictions, fundamentally changing stability and learning speed.

---

### 5. **Off‑policy evaluation (OPE)** and **counterfactual estimation**

Given a logged dataset \(D=\{(s,a,r,s')\}\) from behaviour \(\mu\), estimate \(V^\pi\) for a target policy \(\pi\) *without new interaction*.

* Minimax MSE lower bounds and matching doubly‑robust estimators were developed for both finite‑horizon and linear‑function approximation settings ([arXiv][9], [Proceedings of Machine Learning Research][10]).
* Tight bounds reveal an exponential dependence on horizon \(H\) for naive importance sampling, motivating representation‑based approaches.

This area provides the RL analogue of **generalization error for off‑distribution test points** in supervised learning.

---

### 6. **State‑abstraction and bisimulation metrics**

Define a pseudometric \(d\) on states s.t.

$$
d(s,s')=\max_{a}\Bigl|r(s,a)-r(s',a)\Bigr| + \gamma\,W_1\bigl(P(\,\cdot\,|s,a),P(\,\cdot\,|s',a)\bigr),
$$

where \(W_1\) is the Wasserstein distance.  States with \(d=0\) are **bisimilar**.

* Recent work learns such metrics end‑to‑end and proves that value error is Lipschitz in \(d\) ([arXiv][11], [AAAI][12]).
* Abstractions accelerate learning and explain why self‑supervised contrastive pre‑training can help RL.

Bisimulation is the RL counterpart of questions about the “right” representation layer in deep nets.

---

### 7. Entropy‑ or KL‑**regularized RL** and the mirror‑descent view

Replacing the Bellman operator by a **regularized Bellman operator**

$$
\mathcal T_{\eta}(V)(s)=\max_{\pi}\Bigl[r(s,\pi)+\gamma\,\mathbb E_{s'}V(s')-\eta\,\text{KL}\!\bigl(\pi||\bar\pi\bigr)\Bigr]
$$

connects many modern algorithms (PPO, Soft‑Actor‑Critic) to **convex duality**.  A general theory shows monotone improvement and linear convergence under wide classes of Bregman divergences ([arXiv][13], [arXiv][14]).  This mirrors how weight‑decay or sharpness‑aware minimization shape deep‑network landscapes.

---

### 8. **Robust RL under model uncertainty**

Choose a policy that maximizes

$$
\min_{P\in\mathcal U}\;J(\pi;P),
$$

where \(\mathcal U\) is an uncertainty set of transition kernels.

* Model‑free robust Q‑learning and policy‑gradient algorithms achieve polynomial sample complexity while guaranteeing worst‑case performance ([proceedings.nips.cc][15], [Proceedings of Machine Learning Research][16]).
* Links to *regularized* RL show that certain entropy penalties implicitly yield robustness cushions.

Robust RL stands to RL what adversarial robustness stands to supervised learning.

---

### 9. Hierarchical & temporal‑abstraction complexity

Recent bounds show that **goal‑conditioned hierarchical RL** can yield *provable exponential savings* in sample complexity by re‑using high‑level skills ([NeurIPS][17]).  Theoretical tools (option‑value functions, multi‑time‑scale analysis) echo how depth in neural nets reduces width requirements.

---

## How these strands align with your deep‑learning examples

| Supervised‑DL theory topic                       | Closest RL‐theory analog                                        | Common conceptual thread                                                 |
| ------------------------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Universal approximation & depth/width trade‑offs | PAC‑MDP sample‑complexity, hierarchical RL                      | Expressive power vs. data requirements                                   |
| Mode‑connectivity, flat minima                   | Policy‑gradient landscape analysis, entropy‑regularized RL      | Global structure of non‑convex objectives and connected low‑loss regions |
| NTK, over‑parametrization                        | Linear‑function approximation and Eluder dimension bounds in RL | Over‑parameterized models obey simpler, near‑linear dynamics             |

---

### Pointers for diving deeper

1. **COLT / NeurIPS RL‑theory tracks (2023‑25)** – many of the cited papers appeared here.
2. **“Distributional Reinforcement Learning’’ (Bellemare et al., 2023)** – dedicated textbook.
3. **RL‑Theory Seminar Series** – archived talks often include tutorial‑style introductions before presenting new results.

---

### Open questions worth exploring

* Does *policy‑space mode connectivity* truly hold in high‑dimensional, non‑linear settings?  Empirical evidence is limited.
* Can we define an RL analogue of the *Neural Tangent Kernel* that yields finite‑time convergence *and* optimal regret simultaneously?
* How do bisimulation metrics interact with distributional RL – can one obtain risk‑aware abstractions with provable guarantees?

Addressing these could push RL theory to the same level of maturity that approximation theory has brought to supervised deep learning.

[1]: https://sites.google.com/view/rltheoryseminars/past-seminars/autumn-2023?utm_source=chatgpt.com "RL theory seminars - Autumn 2023 - Google Sites"
[2]: https://www.jmlr.org/papers/volume11/jaksch10a/jaksch10a.pdf?utm_source=chatgpt.com "[PDF] Near-optimal Regret Bounds for Reinforcement Learning∗"
[3]: https://proceedings.neurips.cc/paper/3401-near-optimal-regret-bounds-for-reinforcement-learning.pdf?utm_source=chatgpt.com "[PDF] Near-optimal Regret Bounds for Reinforcement Learning"
[4]: https://arxiv.org/abs/2004.09656?utm_source=chatgpt.com "Tightening Exploration in Upper Confidence Reinforcement Learning"
[5]: https://arxiv.org/abs/2404.11382?utm_source=chatgpt.com "Convergence of Policy Gradient for Stochastic Linear-Quadratic ..."
[6]: https://proceedings.neurips.cc/paper_files/paper/2024/hash/010c855df402b443e0c16e5b7434e74c-Abstract-Conference.html?utm_source=chatgpt.com "Occupancy-based Policy Gradient: Estimation, Convergence, and ..."
[7]: https://arxiv.org/abs/1707.06887?utm_source=chatgpt.com "A Distributional Perspective on Reinforcement Learning"
[8]: https://www.distributional-rl.org/?utm_source=chatgpt.com "Distributional Reinforcement Learning"
[9]: https://arxiv.org/pdf/2212.06355?utm_source=chatgpt.com "[PDF] A Review of Off-Policy Evaluation in Reinforcement Learning - arXiv"
[10]: https://proceedings.mlr.press/v119/duan20b.html?utm_source=chatgpt.com "Minimax-Optimal Off-Policy Evaluation with Linear Function ..."
[11]: https://arxiv.org/abs/2204.13060?utm_source=chatgpt.com "Bisimulation Makes Analogies in Goal-Conditioned Reinforcement ..."
[12]: https://cdn.aaai.org/ojs/17005/17005-13-20499-1-2-20210518.pdf?utm_source=chatgpt.com "[PDF] Metrics and Continuity in Reinforcement Learning"
[13]: https://arxiv.org/pdf/1901.11275?utm_source=chatgpt.com "[PDF] A Theory of Regularized Markov Decision Processes - arXiv"
[14]: https://arxiv.org/pdf/2301.13139?utm_source=chatgpt.com "[PDF] A Novel Framework for Policy Mirror Descent with General ... - arXiv"
[15]: https://proceedings.nips.cc/paper_files/paper/2021/file/3a4496776767aaa99f9804d0905fe584-Paper.pdf?utm_source=chatgpt.com "[PDF] Online Robust Reinforcement Learning with Model Uncertainty - NIPS"
[16]: https://proceedings.mlr.press/v151/panaganti22a/panaganti22a.pdf?utm_source=chatgpt.com "[PDF] Sample Complexity of Robust Reinforcement Learning with a ..."
[17]: https://neurips.cc/virtual/2023/poster/72289?utm_source=chatgpt.com "Sample Complexity of Goal-Conditioned Hierarchical Reinforcement ..."
