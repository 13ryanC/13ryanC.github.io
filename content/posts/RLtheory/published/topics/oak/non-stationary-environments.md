---
date: "2025-08-26"
title: "Why the World is non-stationary"
summary: "Why the World is non-stationary"
lastmod: "2025-08-26"
category: "Notes"
series: ["Continual Learning"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# Tell me in detail why the world appears to be non-stationary

**Short version:** in this paper, a *stationary* world can still *feel* non‑stationary to a learner because (i) the data stream isn’t i.i.d. (you move through states, so what you see now depends on where you are), (ii) your function class is too small to represent the whole world at once, and (iii) nearby moments are correlated (“temporal coherence”). Put together, the “best” parameters keep shifting with context, so tracking beats settling.&#x20;

Here’s the detail, tied to the text and figures:

1. **Non‑i.i.d. experience from evolving states.**
   The authors assume data come from a system with evolving states (e.g., an MDP), so samples are not independent. Because the agent *moves* through the world, the distribution of states it experiences changes over time; what’s relevant this minute is whatever lies along the paths starting from the *current* state. That alone makes the target the learner should care about look like it’s drifting, even though the underlying process is fixed.&#x20;

2. **A big world + a small function approximator → shifting “best” answers.**
   When the world is large, the agent only touches slices of it at any moment. With limited representational capacity, the single parameter vector that’s globally “best” won’t be best for every local slice. The paper frames this as adapting to the *temporally local* environment—favoring what helps over the next stretch of time rather than a single global solution. That’s what they call **temporal coherence**: right answers at nearby times tend to be similar, so it pays to track. (See the discussion introducing temporal coherence on page 2.)&#x20;

3. **Concrete demo: the Black‑and‑White world shows a moving effective target.**
   In their 20‑state toy world, the *true* stationary solution is to predict 0.5 black/white (best static weight \(w=0\)). But because the agent lingers in black regions and then in white regions, successive observations are correlated (Figure 2, page 3). If you *track* with a moderate step size, your prediction stays close to whatever region you’re currently in; if you *converge*, you average everything and stay wrong locally. Empirically, tracking with \(\alpha\approx 4\) achieves \~0.24 mean log loss versus \~0.69 for the best converged solution (Figure 3, pages 3–4). It *looks* like the target is changing because the locally optimal prediction flips with where you are.&#x20;

4. **Policy/position‑conditioned distribution shift in Go.**
   On 5×5 Go, both agents use the same feature class, but the tracking agent continually re‑trains from the *current position*—i.e., for “the distribution of states encountered when starting from the current state” (page 4). As the game position changes, that distribution changes, so the weights that are “best right now” also change. The paper shows context flips where a corner move that’s usually bad is exactly right in a specific life‑and‑death shape (Figure 6), and a 3×3 “two eyes” pattern that’s generally good becomes redundant in another context where playing the center is better (Figure 7). That context dependence makes a fixed, globally trained evaluator underperform—even though the game’s rules are stationary.&#x20;

5. **How much it “moves” depends on observation density.**
   In the toy world, increasing how often you “look up” strengthens temporal coherence (more back‑to‑back related observations), which pushes the optimal step size higher and makes tracking more beneficial. When looks are very rare, the temporal coherence “is completely lost,” and the best behavior is to approximate convergence again (top of page 4). So the apparent non‑stationarity is stronger when you get densely correlated feedback.&#x20;

6. **Remove temporal coherence, and the illusion disappears.**
   They build a version with a single state and independent coin‑flip observations. Now the best prediction is always 0.5 and tracking offers no real gain; even step‑size meta‑learning (IDBD) helps only in the pathological high‑step‑size regime (Figure 10, pages 7–8). With no temporal structure, nothing “moves,” and the world no longer *appears* non‑stationary to the learner.&#x20;

**Bottom line:** the world *appears* non‑stationary from the learner’s point of view whenever (a) experience is temporally correlated, (b) the representation can’t nail a single global solution, and (c) the agent’s own trajectory keeps shifting which slice of the world matters. In those common conditions, the effective target drifts in time—so tracking wins, even though the environment itself is stationary.&#x20;

---









