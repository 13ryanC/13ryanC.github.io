---
_build:
  render: never
  list: never

date: "2025-07-12"
title: "(5) Briefly on Distributional RL"
summary: "(5) Briefly on Distributional RL"
lastmod: "2025-07-12"
category: "Notes"
series: ["RL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---


### 1  Core concepts established in the chapter

| Concept                                             | Formal definition / role                                                                                                            | Why it matters                                                                                                  |                                                                                                 |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Return‑distribution function η<sup>π</sup>**      | Maps each state *x* to the *distribution* of the random return G<sub>π</sub>(x) under policy π.                                     | Puts the full uncertainty about long‑term rewards, not just the mean, at centre stage.                          |                                                                                                 |
| **Distributional Bellman operator *T*<sup>π</sup>** | (T<sup>π</sup> η)(x) = 𝔼<sub>π</sub>\[(r + γ · η(X′)) \mid X = x] – a push‑forward that shifts & scales distributions then mixes across actions, rewards and next states. | Fundamental fixed‑point equation for η<sup>π</sup>; contractive in Wasserstein/Cramér metrics.  |
| **Probability‑distribution representations**        | Finite‑parameter families F ⊂ P(ℝ) used to *store* return distributions in memory (e.g., empirical, normal, categorical, quantile). | Choice of F controls **expressiveness ↔ tractability**. No single best representation.                          |                                                                                                 |
| **Projection operator Π<sub>F</sub>**               | Maps an arbitrary distribution to its “best” element in representation F (best in `ℓ₂` for categorical, in W₁ for quantile).        | Allows iterative algorithms even when F is *not* closed under *T*<sup>π</sup>.                                  |                                                                                                 |
| **Distributional Dynamic Programming (DDP)**        | Generic loop η<sub>k+1</sub> = Π<sub>F</sub> T<sup>π</sup> η<sub>k</sub> (Alg. 5.2).                                                | Unifies all exact/approximate return‑distribution evaluators.                                                   |                                                                                                 |
| **Contraction & Lipschitz analysis**                | kT<sup>π</sup>k<sub>Wₚ</sub> = γ; kΠ<sub>C</sub>T<sup>π</sup>k<sub>ℓ₂</sub> ≤ √γ/2; etc.                                            | Guarantees convergence & provides non‑asymptotic error bounds.                                                  |                                                                                                 |

---

### 2  Key arguments developed by the authors

| Claim                                                                       | Supporting reasoning / evidence                                                                                                                                                                                               |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **(i) Exact computation with full empirical support is *intractable*.**     | Number of particles after *k* iterations can grow as O(N<sub>X</sub>⁽ᵏ⁾ N<sub>R</sub>⁽ᵏ⁾); computing η exactly is NP‑hard via reduction from Hamiltonian cycle (Remark 5.2).                                                  |
| **(ii) Different representations give orthogonal trade‑offs.**              | *Empirical* is expressive but explodes; *Normal* is closed‑form but often a bad fit (Fig. 5.1 shows bimodality loss); *Fixed‑size empirical* (categorical, quantile, m‑particle) hit a “Goldilocks” zone (Section 5.5).       |
| **(iii) Projection choice dictates stability.**                             | Categorical projection is an ℓ₂‑orthogonal projection ⇒ non‑expansion, yields a √γ/2‑contraction; quantile projection is only a γ‑contraction in W₁, but still converges; arbitrary projections can diverge (Exercise 5.19).  |
| **(iv) ‘Diffusion’ is a real risk unless Π<sub>F</sub> is diffusion‑free.** | Example 5.19 (Fig. 5.6) shows categorical DP spreading probability mass far beyond the optimal support along a deterministic chain.                                                                                           |
| **(v) Approximation error is bounded and tunable.**                         | For m‑categorical: ℓ̄₂(η̂, η) ≤ (V<sub>max</sub>−V<sub>min</sub>)/(m‑1)(1−√γ) (Cor. 5.29). For m‑quantile: W₁(η̂, η) ≤ 3(V<sub>max</sub>−V<sub>min</sub>)/(2m(1−γ)) (Lemma 5.30).                                             |

---

### 3  Practical frameworks & algorithms you can apply

| Framework                                   | Inputs & outputs                                                              | Complexity                                                                              | When to use                                                                                  |
| ------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Algorithm 5.1 – Empirical T<sup>π</sup>** | Takes empirical η, returns exact T<sup>π</sup> η (still empirical).           | O(N<sub>X</sub>N<sub>R</sub>N<sub>A</sub>) per state.                                   | Diagnostic baseline; impractical for large *k*.                                              |
| **Algorithm 5.2 – DDP template**            | Parameters: representation F, projection Π<sub>F</sub>, iterations K.         | Dominated by cost of T<sup>π</sup> + projection.                                        | Skeleton for any distributional evaluator.                                                   |
| **Algorithm 5.3 – *Categorical* DP (CDP)**  | Probabilities p<sub>i</sub>(x) on fixed grid θ<sub>i</sub>.                   | O(K m N<sub>R</sub>N<sub>X</sub>²).                                                     | Finite supports; mean‑preserving (if grid covers returns); easy to implement; basis of C51.  |
| **Algorithm 5.4 – *Quantile* DP (QDP)**     | Locations θ<sub>i</sub>(x) with equal weights 1/m.                            | O(K m N<sub>R</sub>N<sub>X</sub>² log m) (sorting) or faster with incremental variants. | When tail accuracy matters; basis of QR‑DQN, IQN.                                            |
| **Normal‑DP (Section 5.4)**                 | Stores mean µ and variance σ² per state. Closed‑form updates (Eqs 5.21‑5.22). | O(K N<sub>X</sub>²) – same as classical value iteration.                                | Rapid rough estimates; risk metrics derived from σ².                                         |

Implementation checklist for CDP/QDP in your own codebase

1. **Choose grid or quantile count m.** Trade memory vs bound above.
2. **Pre‑compute r<sub>π</sub>(x) and P<sub>π</sub>(x→x′)** if model‑based; else sample‑based update (next chapter).
3. **Loop** `for k in range(K):`

   * **Update**: build empirical mixture via Eq. 5.8 (Algorithm 5.1).
   * **Project**:

     * *Categorical*: distribute mass with triangular kernels (Fig. 5.3).
     * *Quantile*: compute mid‑quantiles τ<sub>i</sub> = (2i−1)/2m (Fig. 5.4).
4. **Stop** when ‖η<sub>k+1</sub>−η<sub>k</sub>‖<ε or after K≥⌈log(ε⁻¹)/log(1/γ)⌉.

---

### 4  Notable insights & illustrative examples

* **Visual intuition.**

  * *Figure 5.1* (p. 126) shows that mixing two Gaussians produces a bimodal curve; a single normal fit (solid) misses multimodality – a caution against over‑simplified models.
  * *Figure 5.2* (p. 129) contrasts m‑categorical, m‑quantile, and m‑particle approximations of the same distribution, making particle‑location vs particle‑weight trade‑offs tangible.
  * *Figure 5.6* (p. 140) demonstrates *diffusion*: CDP spreads mass along a 10‑state chain, whereas the optimal categorical projection would remain sharply peaked.
  * *Figure 5.7* (p. 146) plots how increasing m (3→33) progressively sharpens the estimated returns in the Cliffs domain.&#x20;

* **NP‑hardness (Remark 5.2).** Computing *exact* distribution support can encode Hamiltonian cycle; underscores need for approximation.&#x20;

* **Mean‑preservation vs variance inflation.** Categorical DP keeps the expected value intact (if θ₁..θ\_m span returns) but tends to over‑estimate variance, which can be desirable for optimistic exploration or detrimental for risk‑sensitive control.&#x20;

* **Projection metrics matter.** Switching from ℓ₂ to W₁ changes both theory (contraction constant) and empirical behaviour (tail coverage). Offers a design knob when adapting to domain requirements (e.g., financial tails vs robotics safety).&#x20;

---

### 5  Synthesis & value for broader study

* **Bridges expectation‑based RL and full‑distribution RL.** The chapter generalises classical dynamic programming (Bellman Eq. 5.2) to *distributional* form and shows how established convergence tools (contractions, fixed‑point theorems) extend when the state space is upgraded from ℝ to P(ℝ).

* **Provides a **design catalogue**.** By dissecting representations and projections, it equips practitioners to choose or invent the right tool for a given accuracy‑budget‑risk profile – an essential step before moving to sample‑based, function‑approximation, or control settings in later chapters.

* **Sets theoretical guarantees behind popular algorithms.** C51, QR‑DQN, IQN and their continuous‑control variants all rely on CDP/QDP style updates. Understanding their fixed‑point properties clarifies *why* they work and when they might fail (e.g., diffusion, insufficient support).

* **Connects to risk and robustness.** Variance Bellman equations (Normal‑DP) and Wasserstein analysis pave the way for risk‑aware objectives, distributionally‑robust RL, and uncertainty quantification – themes prevalent in modern safe RL research.

* **Highlights open problems.** Efficient projection for m‑particle mixtures, reducing diffusion, and tailoring metrics to task‑specific costs are all identified as fertile ground for innovation.

---

#### Practical take‑aways for your own work

1. **Start with CDP if you need a drop‑in replacement for value iteration.** Pick θ<sub>1</sub>, θ<sub>m</sub> to bracket theoretical return extremes; set m≈ 20–51 for Atari‑scale tasks.
2. **Move to QDP when tail risk matters or when continuous control actions create highly skewed returns.**
3. **Use Normal‑DP only for coarse safety checks or as a baseline; verify multimodality visually (cf. Fig. 5.1).**
4. **Monitor diffusion** by plotting support width over iterations; tighten projection or enlarge m if you see uncontrolled spread.
5. **Leverage bounds** (Cor. 5.29; Lemma 5.30) to budget *m* given desired Wasserstein / Cramér error ε: m ≈ O((V<sub>max</sub>−V<sub>min</sub>)/(ε(1−γ))).

By internalising these concepts and frameworks, you’ll be able to reason formally about uncertainty in returns, prototype distributional evaluators, and lay dependable foundations for distributional RL algorithms in both research and applied settings.


---



Below is a “dictionary” that translates the two canonical control routines of *classical* dynamic programming (DP) into their natural counterparts in **distributional** dynamic programming (DDP).
Throughout, let π be a stationary policy, let F be the probability‑distribution representation you have chosen (categorical, quantile, m‑particle, …), and let Π\_F denote the projection that maps an arbitrary return‑distribution to F (Algorithms 5.2‑5.4 give concrete realisations for the popular categorical and quantile cases).&#x20;

# Classical vs Distributional Reinforcement Learning Algorithms

| Classical Concept | Recursion (scalar value functions) | Distributional Analogue | Recursion (return-distribution functions) | Notes |
|-------------------|-------------------------------------|-------------------------|-------------------------------------------|--------|
| **Iterative policy evaluation** (core of *policy iteration*, also used as a stand-alone algorithm) | \(V_{k+1} = T^{\pi} V_k\), where \(T^{\pi}\) is the Bellman *expectation* operator | **Distributional policy evaluation** (Algorithm 5.2 — "Distributional Dynamic Programming") | \(\eta_{k+1} = \Pi_F T^{\pi} \eta_k\) | This is exactly the loop described in Algorithm 5.2; it keeps the policy fixed and successively sharpens the *full* return distribution at every state. Converges when \(\Pi_F T^{\pi}\) is a contraction (proved for categorical/\(\ell_2\) and quantile/\(W_1\) cases). |
| **Value iteration** | \(V_{k+1} = T^* V_k\), \(T^* v(x) = \max_a \mathbb{E}[R + \gamma v(X') \mid x,a]\) | **Distributional value iteration (DVI)** | \(\eta_{k+1} = \Pi_F T^* \eta_k\), \(T^* \eta(x) = \max_a \mathbb{E}[(R,\gamma) \eta(X') \mid x,a]\) | Replace the policy-specific operator by the *optimal* distributional Bellman operator, then project. DVI collapses to classical VI when you keep only the mean of each \(\eta\). Converges for \(\gamma<1\) under the same metric-projection conditions as evaluation. |
| **Policy iteration (Howard)** | **(1)** Evaluate \(\pi_k\): solve \(V^{\pi_k}\) (exactly or approximately). **(2)** Improve: \(\pi_{k+1}(x) = \arg\max_a \mathbb{E}[R + \gamma V^{\pi_k}(X') \mid x,a]\) | **Distributional policy iteration (DPI)** | **(1)** Evaluate \(\pi_k\) with DDP: \(\eta^{\pi_k} = \lim_K \Pi_F (T^{\pi_k})^K \eta_0\). **(2)** Improve: \(\pi_{k+1}(x) = \arg\max_a \mathbb{E}_{Z \sim \eta^{\pi_k}(x,a)}[Z]\) (or another risk-criterion of interest). | Step (1) is categorical/quantile DP; step (2) uses the expectation of the evaluated distribution unless you purposely adopt a risk-sensitive rule (e.g., maximise VaR, minimise CVaR, etc.). DPI inherits the monotonic policy-improvement guarantee when the improvement rule is expectation-based. |

### Where the algorithms live in Chapter 5

* **Algorithm 5.2** (“Distributional Dynamic Programming”) realises the evaluation half of DPI and, when you swap *T^π* for *T^★*, gives a concrete template for DVI.&#x20;
* **Algorithms 5.3 & 5.4** plug categorical or quantile projections into that template, yielding **Categorical DP (CDP)** and **Quantile DP (QDP)** — ready‑made implementations of both evaluation and control once you decide whether you are in the *π‑fixed* (evaluation) or *greedy/improvement* (control) regime.&#x20;

### Practical guidance for choosing among them

| Goal                                         | Recommended distributional routine | Typical representation / projection | Why                                                                                                 |
| -------------------------------------------- | ---------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------- |
| Fast approximate control with limited memory | **Categorical DVI** (CDP + T^\*)   | m‑categorical, ℓ₂ projection        | O(K m N²) like VI; support fixed ⇒ simple greedy step; mean preserved ⇒ same policy as VI when m→∞. |
| Tail‑risk aware control                      | **Quantile DVI / DPI**             | m‑quantile, W₁ projection           | Gives direct access to quantiles and CVaR; contraction in W₁ guarantees stability.                  |
| Research on new risk criteria                | **Generic DPI**                    | Any F + appropriate Π\_F            | Keep evaluation generic; plug preferred risk measure into the improvement step.                     |

> **Key take‑away** – **Replace the scalar Bellman operators in VI/PI with their distributional counterparts, sandwich every update inside a projection Π\_F, and you obtain the one‑to‑one distributional versions of value iteration and policy iteration.**
> The rest is an implementation choice (categorical vs. quantile vs. something richer) governed by the trade‑offs in Table 5‑1 of the chapter (expressiveness, tractability, diffusion, mean‑preservation).&#x20;
