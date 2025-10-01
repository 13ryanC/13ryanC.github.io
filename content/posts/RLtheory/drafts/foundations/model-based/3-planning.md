---
_build:
  render: never
  list: never

date: "2025-07-10"
title: "(4.2) From Planning to Learning: Exploration-Optimal Online RL in Tabular and Linear MDPs"
summary: "From Planning to Learning: Exploration-Optimal Online RL in Tabular and Linear MDPs"
lastmod: "2025-07-10"
category: "Notes"
series: ["RL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

lec22, 23, 24

> **Context** – Our previous post formalised *online planning* when a perfect simulator of the MDP is available, showing how sparse look‑ahead and Monte‑Carlo Tree‑Search break the curse of dimensionality—yet still suffer an unavoidable \$O(A^{k})\$ explosion in the effective horizon \$k\$ .
>
> **Today** we drop the omniscient simulator.  The agent must *learn* the MDP’s dynamics *while* maximising reward.  We unify three classical building blocks—**exploration vs. exploitation** (Lec 22), **tabular confidence‑based control** (Lec 23) and **function‑approximation era algorithms** (Lec 24)—into a single narrative that moves from small‑scale grids to high‑dimensional robotics.

---

## 1  Problem setting: Online RL as “planning with an unknown model”

| Symbol                              | Meaning                                                                                | Scope               |
| ----------------------------------- | -------------------------------------------------------------------------------------- | ------------------- |
| \$M=(S,A,P,r,\mu,H)\$               | episodic MDP, horizon \$H\$                                                            | all sections        |
| \$\mathcal{D}\_k\$                  | data collected up to episode \$k\$                                                     | learner’s memory    |
| \$\pi\_k\$                          | policy executed in episode \$k\$                                                       | algorithm‑dependent |
| \$R\_k=!\sum\_{h=0}^{H-1}r\_{h}^k\$ | reward accrued in episode \$k\$                                                        | performance         |
| \(\text{Regret}(K)\) | \(\displaystyle\sum_{k=1}^K\bigl[V^\*_{0}(S_0^{k})-V^{\pi_k}_{0}(S_0^{k})\bigr]\) | objective |

> **Finite‑horizon vs. Discounted**    
> In these notes we follow the *episodic*, undiscounted convention of Lec 22–24: every episode is a length‑\(H\) trajectory starting from an initial state sampled from \(\mu\).  Setting \(H=(1-\gamma)^{-1}\) recovers the discounted formulation used in our planning post.

The *exploration–exploitation dilemma* enters because actions affect both immediate reward and the next data sample .

---

## 2  Warm‑up: Bandits, episodic MDPs and sub‑linear regret (Lec 22)

* **Episodic vs. bandit:** \$H!=!1\$ recovers contextual bandits; \$H!>!1\$ brings long‑term credit assignment.
* **Performance metrics:**

  * *Expected regret* \$\tilde{O}(\sqrt{KT})\$ is the gold standard;
  * *PAC* guarantees translate via conversion lemmas .
**Key definitions**

$$
\operatorname{Regret}(K)
  =\sum_{k=1}^{K}\Bigl[V^{\*}_{0}(S^{k}_{0})-V^{\pi_{k}}_{0}(S^{k}_{0})\Bigr],
\qquad
\text{PAC: }\Pr\bigl(V^{\hat\pi}\le V^{\*}-\varepsilon\bigr)\le\delta.
$$

* **Canonical algorithms**  :contentReference[oaicite:1]{index=1}  
  | name | idea | worst‑case regret | notes |
  |------|------|------------------|-------|
  | \(\varepsilon\)‑greedy | mix *explore* \((\varepsilon)\) with *exploit* \((1-\varepsilon)\) | \(\tilde O\bigl(HSA\sqrt{K}\bigr)\) | may loop exponentially long in stochastic traps |
  | OFU / confidence sets | keep \(\mathcal M_k=\{M:\| \hat P-P\|\le\beta\}\), plan on the most *optimistic* \(M\in\mathcal M_k\) | minimax‑optimal up to logs | unifies UCRL, UCBVI, LinUCB |
@@

These ideas set the conceptual stage for the concrete algorithms below.

---

## 3  Tabular confidence‑based control: UCRL & UCBVI (Lec 23)

### 3.1  UCRL: Upper‑Confidence Reinforcement Learning

> **Why optimism works** — if the true MDP \(M^{\*}\) lies in every \(\mathcal C_{k,\delta}\) with
> high probability, then “planning on the best plausible model’’ always upper‑bounds the
> optimal value and never *under‑explores*.

```pseudo
Algorithm UCRL(k, δ)
    # Step 1 (empirical counts)
    for (s,a):        N_k[s,a]   ← visits up to ep k‑1
                      \hat P_k[s,a] ← frequency table
    # Step 2 (confidence set)
    β(n) ← 2√{(S log 2+log(n(n+1)SA/δ)) ⁄ (2n)}
    C_k,δ ← {P : ∀s,a ‖P[s,a]-\hat P_k[s,a]‖₁ ≤ β(N_k[s,a])}
    # Step 3 (optimistic policy)
    (P̃,π_k) ← argmax_{P∈C_k,δ, π}  V^{π}_{0,P}(S₀ᵏ)   # dynamic prog.
    Execute π_k for one episode, update counts
```

Algorithmic cost \(O(S^2AH)\) per episode can be cut to \(O(SAH)\) by **UCBVI**:

```pseudo
Q_{h}(s,a) ← r(s,a) + P̂_k[s,a]·V_{h+1} + H·β(N_k[s,a])       # bonus
V_h(s)     ← min( H , max_a Q_h(s,a) )
```

with identical \(\tilde{O}(H^{3/2}\sqrt{SAK})\) regret.

> **Regret bound**
> \$\displaystyle\text{Regret}(K);\le;\tilde{O}!\bigl(H^{3/2}S\sqrt{AK}\bigr)\$ with probability \$1-3\delta\$ .

### 3.2  UCBVI: Value‑Iteration with bonuses

Replacing the expensive inner \`\`max‑over‑models’’ step by a per‑state bonus
\(b_k(s,a)=H\beta_\delta\bigl(N_k(s,a)\bigr)\)
yields an algorithm that:

* runs **one** backward pass per episode—no nested optimisation over \$S\$;
* matches UCRL’s regret up to log factors: \$\tilde{O}(H^{3/2}\sqrt{SAK})\$ .

---

## 4  Beyond tables: Linear approximation regimes (Lec 24)

Tabular complexity \(\Theta(S)\) is untenable when \(|S|\gg10^{6}\).  
Two *linearly‑parameterised* families rescue sample‑efficiency by replacing “one
parameter per state’’ with “one parameter per **feature**’’  \(d\llS\).

### 4.1  Linear *mixture* MDPs

* **Features** \$\phi(s,a,s')\in\mathbb{R}^d\$, \$|\phi|\le 1\$.
* **Dynamics** \$P\_h(s'|s,a)=\langle\phi(s,a,s'),\theta^\*\_h\rangle\$,  \$|\theta^\*\_h|\le 1\$.
* **Value‑Targeted Regression (VTR)** 
  1. *Target construction* \(y_{h,j}=V^{(j)}_{h+1}(S'_{h,j})\)  
  2. *Ridge regression*    $\displaystyle\hat\theta_{h,k}
       =\arg\min_\theta\sum_{j<k}(⟨\phi_{h,j},\theta⟩-y_{h,j})^{2}+\lambda\|\theta\|^{2}$  
  3. *Bonus* \(\displaystyle\beta_{h,k}=H\sqrt{d\log\bigl(1+\tfrac{k}{\lambda d}\bigr)+2\log\tfrac{1}{\delta}}. \)
@@
* **UCRL‑VTR regret**
  \(\text{Regret}(K)=\tilde{O}\bigl(dH^{2}\sqrt{K}\bigr)\)
  independent of \$S\$ and \$A\$ .

### 4.2  Linear MDPs

* **State‑only features** \$\varphi(s,a)!\in!\mathbb{R}^d\$; parameters \$(\theta\_h^\*,\psi\_h^\*)\$ generate **both** rewards and transitions.
* **Least‑Squares Value Iteration (LSVI‑UCB)**   :contentReference[oaicite:5]{index=5}  
  ```pseudo
  for h = H−1..0:
      Σ_h ← Σ_h + φ_h φ_hᵀ
      w_h ← Σ_h^{-1}  Σ_h y_h
      Q_h(s,a) ← ⟨φ(s,a), w_h⟩ + √β_k ‖φ(s,a)‖_{Σ_h^{-1}}
      V_h(s)   ← min(H, max_a Q_h(s,a))
  ```
  One pass backward, one Sherman–Morrison update ⇒  
  **runtime** \(O(Hd^{2}+HAd)\) per episode (no \(S\)), **regret** \(\tilde O(d^{3/2}H^{2}\sqrt{K})\).
@@
* **Regret** \$\tilde{O}!\bigl(d^{3/2}H^{2}\sqrt{K}\bigr)\$—again, no \$S\$‑dependence .

> **Tightness.**  A matching lower bound is \$\Omega!\bigl(dH^{3/2}\sqrt{K}\bigr)\$; closing the residual \$\sqrt{d}\$ gap remains open.

---

## 5  Unifying principles

| Planning (prev. post)             | Learning (this post)                | Shared technical motif                                              |
| --------------------------------- | ----------------------------------- | ------------------------------------------------------------------- |
| Simulator gives samples on demand | Environment reveals samples on‑line | Sparse search trees / confidence sets explore *reachable* states    |
| Bellman operator \$T\$            | Empirical \$\hat T\$ + bonus        | Contractivity + optimism                                            |
| Query budget                      | Regret                              | Both scale as \$O\bigl((mA)^{H}\bigr)\$ unless we exploit structure |

Whether we **choose actions to probe a simulator** (planning) or **probe the real world itself** (RL), the key is *controlling Bellman error on the visited subtree*—not the entire \$|S|\times|A|\$ table.


<details>
<summary><strong>Derivation tip</strong> – Why does bonus \(\propto\|v\|_{\Sigma^{-1}}\) appear everywhere?</summary>
For sub‑Gaussian noise and linear features,
$\displaystyle
\Pr\bigl(\|\hat\theta-\theta^{\*}\|_{\Sigma}\le
H\sqrt{\log\det\Sigma-\log\det\lambda I + 2\log(1/\delta)}\bigr)\ge1-\delta$.
Applying Cauchy–Schwarz inside the Bellman backup yields
\(|\langle\phi,v\rangle|\le \|v\|_{\infty}\|\phi\|_{\Sigma^{-1}}\|\hat\theta-\theta^\*\|_{\Sigma}\),
hence the ubiquitous \(\sqrt{\det}\)‑style bonuses. :contentReference[oaicite:6]{index=6}
</details>

---

## 6  Take‑aways and open problems

1. **Tabular guarantees saturate** at \$\tilde{O}(H^{3/2}S\sqrt{AK})\$; escaping the \$S\$‑factor demands function approximation.
2. **Linear models trade parametric risk for bias.**  They are sample‑optimal but hinge on *realisability* (\$P\in\text{span}{\phi}\$).
3. **Computational barriers** still exist: solving the optimistic planning step exactly is tractable in VTR and LSVI, but Eleanor‑style *Bernstein* bonuses remain algorithmically elusive.
4. **Horizon is the real villain**—both lower and upper bounds carry an \$H^{3/2}!\to!H^{2}\$ penalty.  Can hierarchical abstractions push this toward \$\log H\$?
5. **Model‑based vs. model‑free** is a gradient, not a dichotomy: VTR explicitly estimates \$P\$, LSVI hides \$P\$ inside value‑targets.

---

### Suggested next read

* *Monte‑Carlo Tree Search in continuous state‑spaces*—marrying planning rollouts with LSVI optimism.
* *Adaptive feature discovery*—when the right \$\phi\$ is *not* given.

*Got questions or spot inconsistencies?  Drop a comment below—let’s iterate together!*


---
### Appendix A  Cheat‑sheet of bounds

| setting | algorithm | regret (high‑prob.) | complexity/ep. |
|---------|-----------|---------------------|----------------|
| bandit (\(H=1\)) | UCB | \(\tilde O(\sqrt{KA})\) | \(O(A)\) |
| tabular MDP | **UCRL** | \(\tilde O(H^{3/2}S\sqrt{AK})\) | \(O(S^2AH)\) |
| tabular MDP | **UCBVI** | \(\tilde O(H^{3/2}\sqrt{SAK})\) | \(O(SAH)\) |
| linear mixture | **VTR** | \(\tilde O(dH^{2}\sqrt{K})\) | \(O(d^{2}H)\) |
| linear MDP | **LSVI‑UCB** | \(\tilde O(d^{3/2}H^{2}\sqrt{K})\) | \(O((d^{2}+Ad)H)\) |

Lower bounds: \(\Omega(H^{3/2}\sqrt{SAK})\) (tabular) and \(\Omega(dH^{3/2}\sqrt{K})\) (linear). 
