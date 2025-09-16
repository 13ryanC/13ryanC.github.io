The essay’s point of departure is a single, apparently straightforward question:

> **“Are there what amount to *laws of innovation* that govern the arc of progress?”** ([writings.stephenwolfram.com][1])

Stephen Wolfram treats this as “deceptively simple” because, while it sounds like a quick yes‑or‑no inquiry, answering it forces one to:

* define what counts as an “innovation,”
* measure an entire historical record of such innovations in a consistent way,
* separate the contribution of purposeful human design from blind search, and
* reconcile the findings with deep results on computational irreducibility and undecidability.

The rest of the article is devoted to showing that the half‑century corpus of Game‑of‑Life engineering provides the first data set rich enough, homogeneous enough, and long enough to let us even attempt to answer that question quantitatively.

[1]: https://writings.stephenwolfram.com/2025/03/what-can-we-learn-about-engineering-and-innovation-from-half-a-century-of-the-game-of-life-cellular-automaton/ "What Can We Learn about Engineering and Innovation from Half a Century of the Game of Life Cellular Automaton?—Stephen Wolfram Writings"



In Wolfram’s words the essay “boils down” to the **fundamental problem of medicine**, which he phrases as follows:

> *“Given that perturbations have had a deleterious effect on an organism, can we find subsequent perturbations to apply that will serve as a ‘treatment’ to overcome the deleterious effect?”* ([writings.stephenwolfram.com][1])

So the *deceptively simple question* is:

**“If something has gone wrong in an organism, is there any intervention we can apply that will put it back on (approximately) its healthy course?”**

In the cellular‑automaton metamodel Wolfram uses, the question becomes: *After one perturbation (‘disease’) changes the automaton’s pattern and shortens its lifetime, can another, carefully chosen perturbation restore the original lifetime or behaviour?* What looks like a straightforward yes/no medical query exposes deep issues of computational irreducibility—showing why prediction, diagnosis and therapy are intrinsically hard even in a toy model.

[1]: https://writings.stephenwolfram.com/2025/02/towards-a-computational-formalization-for-foundations-of-medicine/ "Towards a Computational Formalization for Foundations of Medicine—Stephen Wolfram Writings"



The essay’s whole discussion pivots on one neatly phrased but far‑reaching question:

> **“What would change—qualitatively as well as quantitatively—if a mind (biological *or* artificial) had vastly more neurons / synaptic connections than a present‑day human brain?”** ([Writings by Stephen Wolfram][1])

Stephen Wolfram expresses it informally as “*What if we had bigger brains?*” and immediately frames it with concrete numbers: cats manage on ≈10⁸ neurons, humans on ≈10¹¹, so *what might become possible with 10¹⁴ – 10¹⁵ neurons (or their AI equivalent)?* The rest of the article explores the linguistic, conceptual‑abstraction and societal consequences of crossing such capacity thresholds, while emphasizing that more size does not override fundamental limits like computational irreducibility.

[1]: https://writings.stephenwolfram.com/ "Stephen Wolfram Writings"


What qualitative differences would appear if biological or artificial brains had orders‑of‑magnitude more neurons/synaptic connections than the ±10¹¹ neurons and ±10¹⁴ synapses of Homo sapiens?


### Outline  

Below I treat the question as four linked sub‑problems, solve each with evidence, then integrate the results into a qualitative forecast.

| # | Sub‑question                                                         | Method & key evidence                                          | Interim answer                                                                                                                    |
| - | -------------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1 | **What actually changes when brains get bigger in nature?**          | Comparative neuro‐anatomy of primates, elephants and cetaceans | Neuron counts grow more slowly than volume, cortical neurons matter most, and energy per neuron stays \~constant.                 |
| 2 | **Which physical limits dominate at 10–100 × current scale?**        | Allometric scaling & axonal conduction theory                  | Metabolic power, heat dissipation and signal delay rise linearly with neurons but only \~logarithmically with speed improvements. |
| 3 | **What have artificial networks taught us about extreme scaling?**   | Parameter–loss power laws and “emergent abilities” literature  | Past 10¹¹ parameters, qualitatively new behaviours appear abruptly rather than smoothly.                                          |
| 4 | **How do (1)–(3) combine in hypothetical 10¹²–10¹⁴‑neuron systems?** | Conceptual synthesis under energy & latency constraints        | Expect modular, hierarchy‑rich architectures, richer world‑models, extended self‐reflection and multi‑agent‑style cognition.      |

---

## 1 Lessons from the largest biological brains

* **Neuron allocation matters more than total neurons.**
    – Elephants contain ≈ 257 billion neurons, but 97 % sit in the cerebellum, leaving fewer cortical neurons than humans ([PubMed][1]).
    – Long‑finned pilot whales have ≈ 37 billion cortical neurons, almost double the human figure, yet general cognition is not obviously superior ([Frontiers][2]).

* **Energy per neuron is roughly fixed across mammals.**
  Suzana Herculano‑Houzel showed glucose consumption per neuron varies by only \~40 % across six species ([PubMed][3]). Bigger brains therefore demand (i) proportionally more calories and (ii) an evolutionary workaround (cooking, fat‑rich diet) to pay that bill.

* **Latency is a hidden tax.**
  Fast myelinated axons top out near 100 m s⁻¹, so a 30 cm cortex already incurs 1–5 ms delays; larger brains must either grow even thicker axons (costly volume) or tolerate slower, more modular computation ([PMC][4]).

**Interim conclusion 1.** Simply adding neurons rarely yields qualitatively new cognition unless they are (a) preferentially cortical and (b) wired to control delays and power.

---

## 2 Physical limits at 10–100 × scale

| Constraint          | Scaling rule                                                        | Qualitative effect                                                                                                                                         |
| ------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Metabolic power $P$ | $P≈ε N$ (ε ≈ constant glucose per neuron) ([PubMed][3])             | Diet or cooling technology must improve linearly with neurons.                                                                                             |
| Signal delay $τ$    | $τ∝L/v$. If linear size $L∝N^{1/3}$ in 3‑D, delays grow $∝N^{1/3}$. | Past \~1 m diameter, synchronised spike timing across cortex becomes impractical; computation splits into semiautonomous modules.                          |
| Heat                | Joule heating ∝ power density; brain tissue tolerates < 40 °C.      | Natural brains hit the cooling limit before 3–4× current size unless perfusion or conduction velocity improves. Artificial chips are already heat‑limited. |

---

## 3 Artificial scaling: evidence for emergent regimes

Large language‑model studies report:

* **Power‑law improvements** in cross‑entropy loss with parameters, data and compute ([arXiv][5]).
* **Emergent abilities** (e.g., in‑context learning, tool use) arising suddenly past parameter thresholds ([arXiv][6], [arXiv][7]).
* **U‑shaped scaling**: hard tasks remain flat, then spike upward when representation depth becomes adequate ([arXiv][8]).

**Analogy caveat.** Biological brains do not do back‑prop, but both systems are large associative graphs. Scaling results are therefore suggestive but not determinative.

---

## 4 Synthesis: what *qualitative* novelties follow from 10²–10³ × growth?

| Domain                              | Likely qualitative shift                                                                                                          | Why it emerges                                                                                                            |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Working & episodic memory**       | Context windows of hours‑to‑days instead of minutes; ability to simulate many counterfactual futures in parallel.                 | More synapses provide high‑capacity, low‑interference attractor networks; latency acceptable inside modules.              |
| **Abstraction depth**               | Concept hierarchies many levels deeper; “theories‑of‑theories” reasoning and meta‑planning become routine.                        | Hierarchical modular wiring avoids cross‑module delays while letting each sub‑system specialise.                          |
| **Self‑model & consciousness**      | Multiple concurrent self‑threads (“multi‑agent mind”) rather than a unitary spotlight; phenomenology may feel more “distributed”. | Cortical areas can maintain partly independent global workspaces, then merge outputs via slower channels.                 |
| **Social cognition**                | Tracking of thousands of agents, long‑term coalition forecasting, richer moral emotions.                                          | Memory and simulation scale with N² in naive implementations; modular design keeps cost linear.                           |
| **Learning speed**                  | Single‑trial abstraction: one novel example suffices for general rule induction, akin to few‑shot leaps seen in LLMs.             | Redundant representations allow rapid Bayesian updating without catastrophic interference.                                |
| **Tool creation & problem solving** | Spontaneous invention of domain‑specific symbolic systems (mathematics‑like) without cultural scaffolding.                        | Extra modules can search vastly larger hypothesis spaces in parallel while sleep‑consolidation handles credit assignment. |
| **Failure modes**                   | Fragmented personalities, timing desynchrony, runaway epilepsy‑like oscillations, metabolic collapse if cooling fails.            | Same constraints that forced modularity also make global coherence fragile.                                               |

### Biological vs. silicon implementations

| Factor       | Carbon brain                                      | Artificial wafer brain                                                                  |
| ------------ | ------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Signal speed | 1–100 m s⁻¹                                       | 10⁵ m s⁻¹ equivalent (GHz clock)                                                        |
| Energy/bit   | \~10⁻¹⁴ J spike⁻¹                                 | \~10⁻¹⁵ J MAC⁻¹ in advanced ASICs                                                       |
| Heat removal | 10 W kg⁻¹ via blood                               | \~100 W cm⁻² with liquid cooling                                                        |
| Net effect   | Latency dominates, forcing **spatial modularity** | Heat dominates, forcing **temporal sparsity** (activation pruning, event‑driven logic). |

Thus the same neuron/synapse count could yield *different* qualitative behaviours depending on substrate: a cool, clock‑fast silicon brain may exploit ultra‑deep serial reasoning; a warm, slow biological giant will exploit massive parallel but loosely synchronised modules.

---

## 5 Residual uncertainties & testable predictions

1. **Does emergence depend on *parameter density* or *absolute count*?**
      *Test:* scale *surface area* of cortical organoids while keeping thickness constant and measure new rhythmic patterns.

2. **Can modularisation fully offset increasing delays?**
      *Test:* in silico, impose 10 ms inter‑module lag in a 10¹³‑parameter transformer and see whether routing networks evolve.

3. **Is there an upper energy budget per neuron in artificial devices?**
      *Test:* benchmark identical models on neuromorphic (spiking, sparse) vs. GPU hardware to map Watts/neuron vs. performance.

---

### Bottom line (qualitative answer)

Adding **orders of magnitude** more neurons or synapses does **not** just make a human‑like mind smarter. Once energy, latency and wiring constraints are engineered away, *new cognitive regimes* emerge:

* **Memory becomes panoramic** and seamlessly reaches across long time‑scales.
* **Abstractions nest deeper**, enabling reflexive “theories of everything” and self‑editing thought.
* **Consciousness likely fragments into parallel workspaces** that later reconcile, so the inner life resembles a parliament more than a monologue.
* **Social, moral and creative capacities scale non‑linearly,** mirroring “emergent abilities” already observed in large‑scale artificial networks.

In short, a 10¹³–10¹⁵‑synapse mind would **feel and act qualitatively different**, not merely more powerful—provided its architecture channels the extra capacity into cortex‑like modules and its substrate solves the brutal metabolic and timing hurdles that limited natural evolution.

[1]: https://pubmed.ncbi.nlm.nih.gov/24971054/ "The elephant brain in numbers - PubMed"
[2]: https://www.frontiersin.org/journals/neuroanatomy/articles/10.3389/fnana.2014.00132/full "Frontiers | Quantitative relationships in delphinid neocortex"
[3]: https://pubmed.ncbi.nlm.nih.gov/21390261/ "Scaling of brain metabolism with a fixed energy budget per neuron: implications for neuronal activity, plasticity and evolution - PubMed"
[4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2779774/ "Functional Trade-Offs in White Matter Axonal Scaling - PMC"
[5]: https://arxiv.org/abs/2001.08361 "[2001.08361] Scaling Laws for Neural Language Models"
[6]: https://arxiv.org/abs/2206.07682 "[2206.07682] Emergent Abilities of Large Language Models"
[7]: https://arxiv.org/html/2503.05788v2 "Emergent Abilities in Large Language Models: A Survey - arXiv"
[8]: https://arxiv.org/html/2410.01692v1 "U-shaped and Inverted-U Scaling behind Emergent Abilities ... - arXiv"
