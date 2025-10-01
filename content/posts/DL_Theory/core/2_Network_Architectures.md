---
_build:
  render: never
  list: never

date: "2025-07-07"
title: "(1.2) Network Architecture: Layers, Depth, Width, and Feed-Forward Computation"
summary: "Network Architecture: Layers, Depth, Width, and Feed-Forward Computation"
lastmod: "2025-07-07"
category: "Notes"
series: ["DL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# 1 .2 .1 Prelude

## C‑1.2.0 Feed‑forward computation as *function composition*

Let

$$
x^{(0)} \in \mathbb R^{d_0}, \qquad
f_\ell:\mathbb R^{d_{\ell-1}}\to\mathbb R^{d_\ell}(1\le\ell \le L),
\qquad
\theta=\{\theta_\ell\}_{\ell=1}^L
$$

be the layer functions with trainable parameters $\theta_\ell$.
A *feed‑forward network* realises the composite map

$$
F_\theta = f_L \circ f_{L-1}\circ\cdots\circ f_1.
$$

*Formally*, $F_\theta$ lies in the set

$$
\mathcal F = \lbrace f_L\circ\cdots\circ f_1 | f_\ell\in\mathcal H_\ell \rbrace ,
$$

where each $\mathcal H_\ell$ is the *hypothesis class* (e.g. affine + non‑linearity) of layer $\ell$.
**Assumptions**: layers are measurable and locally Lipschitz, ensuring the composite is differentiable a.e.—required for gradient‑based training.

---

## G‑1.2.0 Signals on spaces, group actions, and *equivariance*

1. **Signal space**.  Let $(\mathcal X,\mu)$ be a measurable space endowed with a (pseudo‑)metric $d$. A *signal* is a function $s:\mathcal X\to\mathbb R^C$ (e.g. an image with $C$ channels).

2. **Group action**.  A (locally compact) group $G$ acts on $\mathcal X$ via

   $$
   \rho: G\times\mathcal X \to \mathcal X,\qquad (g,x)\mapsto g\cdot x.
   $$

3. **Layer as linear operator or kernel**

   $$
   (\mathcal L s)(x)=\int_{\mathcal X} K(x,y)s(y)d\mu(y)
   $$

   with learnable kernel $K$.

4. **Equivariance**.  A map $\mathcal L$ is *$G$-equivariant* if

   $$
   \mathcal L \bigl(s\circ\rho_g^{-1}\bigr) = \bigl(\mathcal L s\bigr)\circ\rho_g^{-1}, \quad\forall g \in G.
   $$

   This condition forces $K$ to satisfy *weight‑tying constraints* that depend only on the *orbit difference* $g = x^{-1}y$.

---

### Concrete illustrations

| Classical view                                            | Geometric view                                            | Equivariance check                                   |
| --------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------- |
| Two‑layer MLP $y=\sigma(W_2\sigma(W_1x))$                 | Trivial group $G={e}$ acting on index set $\{1,\dots,d\}$ | Any function is equivariant because $G$ is trivial   |
| 1‑D conv. $(\mathcal Ls)(t)=\sum_\tau k(\tau)s(t-\tau)$ | $G=\mathbb Z$ acts by translation on time                 | Kernel depends only on $t-\tau$ ⇒ translation equiv. |

---

## Why this prelude matters

* **Compositionality** (classical) ↔ **closure of equivariant maps under composition** (geometric).
* Sets the stage for seeing every subsequent architectural choice as either

  * extending the hypothesis classes $\mathcal H_\ell$ (classical eye), or
  * narrowing them by symmetry‑preserving constraints (geometric eye).

---

### Residual uncertainty & suggested test

*Uncertainty*: For non‑compact groups (e.g.\ $\mathbb R$ translations) integrals defining kernels may diverge.
*Test*: Verify square‑integrability of the kernel after enforcing equivariance; empirical check = monitor numerical stability when padding length increases.

---


## 1 .2 .2 Layer Taxonomy

This section builds a **dictionary** between the *classical* catalogue of neural‑network layers and their *geometric* avatars—linear (or affine) maps that are constrained to be equivariant to a particular symmetry group $G$.
Throughout, let

$$
s:\mathcal X\to\mathbb R^{C_{\mathrm{in}}}
\quad\text{and}\quad
\mathcal L:L^2(\mathcal X,\mathbb R^{C_{\mathrm{in}}})\to L^2(\mathcal X,\mathbb R^{C_{\mathrm{out}}})
$$

denote the input signal and a single layer, respectively.

---

### C‑1.2.1 Classical repertoire

| Layer type                | Canonical formula                                             | Typical use‑case                                  | Parameter count                            |
| ------------------------- | ------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------- |
| **Fully connected**       | $y = \sigma(Wx+b)$                                            | Arbitrary feature mixing (MLP)                    | $d_{\text{in}}d_{\text{out}}+d_{\text{out}}$ |
| **Convolution** (1‑D/2‑D) | $(\mathcal Ls)(x)=\sum_{\tau\in\mathcal N}K(\tau)s(x-\tau)$ | Local, shift‑invariant processing (audio, vision) | $k^d C_{\text{in}}C_{\text{out}}$            |
| **Recurrent** (RNN cell)  | $h_t=\sigma(W_{hh}h_{t-1}+W_{xh}x_t+b)$                       | Sequential dependencies (language, time series)   | $d_h^2+d_xd_h+d_h$                           |
| **Self‑attention**        | $\mathrm{Att}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt d)V$    | Long‑range context (Transformers)                 | $3d^2$ per head                              |

* ignoring layer‑norm and projection nuances for brevity

All four are *affine maps followed by a point‑wise non‑linearity*; their distinguishing feature is the pattern of **weight sharing**, which in turn arises from an implicit or explicit **symmetry**.

---

### G‑1.2.1 Equivariant operators by symmetry group

| Symmetry group $G$                                   | Action on index set $\mathcal X$     | Equivariant layer class                          | Classical alias          |
| ---------------------------------------------------- | ------------------------------------ | ------------------------------------------------ | ------------------------ |
| **Trivial group** $\{e\}$                            | Identity                             | All linear maps $W$                              | Dense / fully‑connected  |
| **Translation group** $\mathbb Z^d$ or $\mathbb R^d$ | $g\cdot x = x+g$                     | *Toeplitz* (discrete) or *convolution* operators | Convolution layer        |
| **Time‑shift semigroup** $\mathbb N$                 | $t\mapsto t+\tau,\tau\ge 0$        | Causal convolutions ⇒ *state‑space realisation*  | Recurrent (RNN/GRU/LSTM) |
| **Permutation group** $S_n$                          | $g\cdot i = g(i)$ on token positions | Functions of pairwise *orbits* $(i,j)$           | Self‑attention           |

---

#### 1. Trivial $G$ ⇒ Dense layer

No symmetry constraints $\Longrightarrow$ every entry of $W\in\mathbb R^{d_{\text{out}}\times d_{\text{in}}}$ is independent.
*Geometric reading*: the hypothesis class is the full linear space $\mathrm{Hom}(\mathbb R^{d_{\text{in}}},\mathbb R^{d_{\text{out}}})$.

---

#### 2. Translation group ⇒ Convolution layer

*Constraint*:

$$
K(x,y) = \kappa(y-x)\quad(\text{stationary kernel})
$$

forces *parameter tying* over each orbit $(x,y)\sim(x+\delta,y+\delta)$.
*Locality* is optional but common: restrict $\kappa$ to a finite neighbourhood.

**Example (2‑D image)**

$$
(\mathcal Ls)(\mathbf r) = 
\sum_{\boldsymbol\tau\in[-k,k]^2}\kappa(\boldsymbol\tau)s(\mathbf r-\boldsymbol\tau).
$$

---

#### 3. Time‑shift semigroup ⇒ Recurrent layer

The semigroup has *no inverses*; equivariance therefore enforces **causality**: output at time $t$ may depend only on $s_{t-\tau},\tau\ge 0$. Any such causal, time‑invariant linear operator admits a **state‑space realisation**:

$$
h_{t}=A h_{t-1}+Bx_t,\quad
y_t=C h_t+Dx_t,
$$

which, after a non‑linearity and parameter sharing across $t$, yields classic RNN/GRU/LSTM formulas.

---

#### 4. Permutation group ⇒ Self‑attention

For tokens $i,j\in\{1,\dots,n\}$ let the group $S_n$ act by index permutation.
*Equivariance* of a pairwise operator demands its kernel depend only on the **orbit invariants** $(i,j)\mapsto (g(i),g(j))$.
In practice:

$$
\mathbf{Att} (Q,K,V)_i  = \sum_j \alpha(i,j) V_j, \quad \alpha(i,j) = f(\langle Q_i, K_j \rangle),
$$

and because dot‑products are invariant under a common permutation of rows of $Q,K,V$, the whole block is $S_n$-equivariant. Multi‑head variants simply realise several irreducible representations in parallel.

---

### Putting it together

**Universal recipe**

1. **Choose a symmetry group $G$** dictated by the data domain (spatial grid, time index, set, graph…).
2. **Construct the unique (up to isomorphism) linear $G$-equivariant maps**—often block‑diagonalised by *Fourier or representation theory* (e.g.\ FFT for translations, Dihedral FFT for rotations).
3. **Insert non‑linearities** that act *point‑wise* in the representation space so as not to break equivariance.
4. **Stack and mix representations**: composing equivariant layers remains equivariant; composing with global pooling converts equivariance to invariance when the task demands it (e.g.\ category label independent of spatial location).

---

### Residual uncertainty & suggested experiments

| Issue                                                                                  | Why it matters                           | Simple test                                                                                                                        |
| -------------------------------------------------------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Non‑compact groups** (e.g. $\mathbb R$) may yield *non‑integrable* kernels           | Numerical blow‑up or ill‑posed learning  | Constrain support (windowed conv) and plot spectral norm as kernel size grows                                                      |
| **Broken symmetry** in real data (e.g. perspective distortion breaks pure translation) | Purely equivariant layers might underfit | Add *relative‑position* embeddings (attention) or small *learnable deformations* (deformable conv) and compare validation accuracy |
| **Permutation‑equivariance vs. order‑sensitivity**                                     | Some NLP tasks require positional nuance | Train with and without absolute position encodings; measure perplexity gap                                                         |

---


## 1 .2 .3 Depth‑versus‑Width & Expressive Power

> **Key question.** *Given a desired mapping $f{:}\mathbb R^{d_0}\to\mathbb R^{d_L}$, how many layers (depth $L$) and how many channels per layer (width) are required before a neural network can approximate $f$ to accuracy $\varepsilon$?*
> The answer splits naturally into a **classical approximation story** and a **geometric/equivariant refinement**.

---

### C‑1.2.2 Classical perspective

| Property                           | Precise statement                                                                                                                                                                                                                                                                                                                                                                                      | Consequence                                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| **Universal approximation (UA)**   | If the activation $\sigma$ is *continuous, bounded, and non‑polynomial* (e.g. sigmoid) or *piece‑wise linear, non‑affine* (ReLU), then for any continuous $f$ on a compact set $K\subset\mathbb R^{d_0}$ and any $\varepsilon>0$ there exists a **single‑hidden‑layer** network $F_\theta$ with width $m$ such that $\sup_{x\in K}\lVert f(x)-F_\theta(x)\rVert<\varepsilon$. \[Hornik, Cybenko, 1990] | Depth $=2$ is *sufficient* but the required width $m$ can be enormous—exponential in $d_0$.                 |
| **Minimal width for UA with ReLU** | A ReLU network of *any depth* needs hidden‑layer width at least $d_0+1$ to be dense in $C(K)$. \[Lu et al., 2017]                                                                                                                                                                                                                                                                                      | A “skinny” network (width $\le d_0$) can never be universally approximating, no matter how deep.            |
| **Depth separation**               | There exist explicit families of functions $f_L$ such that: 1) they are exactly (or $\varepsilon$-) representable by ReLU networks of depth $L$ and width $O(1)$; 2) any ReLU network of depth $<L/2$ that approximates $f_L$ to error $<1/9$ requires width $\exp(\Omega(L))$. \[Eldan & Shamir 2016; Telgarsky 2016]                                                                                 | **Depth offers exponential expressive savings**.                                                            |
| **Width bottleneck**               | A layer with width $\ll d_0$ acts as a *rank bottleneck*; information that is lost cannot be recovered by later layers (unless non‑injective activations “branch” the representation).                                                                                                                                                                                                                 | Practical rule: avoid narrow layers early in the network if high‑dimensional information must be preserved. |
| **Hierarchical composition**       | Deep networks implement *function composition*: $F_\theta=f_L\circ\cdots\circ f_1$. For many natural tasks (vision, language) the target mapping itself is compositional, so depth aligns architecturally with the problem structure and yields *sample‑efficient* representations.                                                                                                                    | Explains empirical success of deep CNNs/Transformers versus wide shallow MLPs.                              |

---

#### Sketch of the classical proofs

1. **UA (width suffices).** Expand $f$ in an $L^1$ (or Fourier) basis $\{e_j\}$. Each basis function can be approximated by a single neuron thanks to $\sigma(w^\top x + b)\approx e_j(x)$. Summing $m$ such neurons realises the partial sum $\sum_{j\le m} a_j e_j$.
2. **Depth separation.** Construct a “hard” function such as a *high‑frequency triangle wave composed with itself $L$ times*. Shallow nets cannot create enough alternating linear regions; counting arguments on the number of linear pieces produced by a ReLU network show an exponential gap.
3. **Width lower bound (ReLU).** A network whose largest hidden layer has width $\le d_0$ can be shown to map $K$ into a finite union of at most $m$ polytopes; continuous $f$ with oscillations across more than $m$ regions cannot be approximated.

---

### G‑1.2.2 Geometric / equivariant perspective

Depth and Width with Symmetry Constraints

| Notion | Geometric Formulation | Effect of Depth |
|--------|----------------------|-----------------|
| **Receptive-field radius** | For a $G$-equivariant layer with *local kernel support* radius $r$, the **effective radius** after $L$ stacks is at most $Lr$ (linear) or $r(2^{L}-1)$ with dilations (exponential). | Deep equivariant stacks propagate information across distant group orbits without breaking the constraint. |
| **Symmetric Stone–Weierstrass** | Let $C_G(\mathcal{X})$ be the algebra of continuous *$G$-equivariant* functions on a compact $G$-space $\mathcal{X}$. If a set $\mathcal{A} \subset C_G(\mathcal{X})$ is (i) an algebra, (ii) point-separating on orbit space $\mathcal{X}/G$, and (iii) contains a non-zero constant, then $\overline{\mathcal{A}} = C_G(\mathcal{X})$. [Kondor 2018] | A *finite-width, sufficiently deep* equivariant network whose layers generate such an algebra is **universally approximating *within the symmetry class***. |
| **Depth vs. irreps** | Each equivariant layer decomposes into blocks acting on irreducible representations (irreps) of $G$. Deeper composition allows *mixing across frequency bands* (e.g. low ↔ high spherical harmonics) that a single layer cannot couple. | Explains why shallow SO(3)-equivariant CNNs underfit complex 3-D molecular potentials while deep ones succeed. |
| **Sample complexity reduction** | Hypothesis space shrinks from all functions to $C_G(\mathcal{X})$; VC-dimension scales with number of *free* parameters, which is approximately $(\text{irreps} \cdot \text{width})$ rather than $(\|\mathcal{X}\| \cdot \text{width})$. | Depth can grow without proportional risk of overfitting when symmetry ties weights. |
---

#### Worked example – 1‑D convolutional stack

*Kernel radius* $r=3$ (size 7). A depth‑$L$ stack covers

$$
\text{RF}(L)=\{x\pm 3L\}.
$$

Hence to model dependencies at distance $d$ we may choose either

* **Width strategy:** one huge kernel of radius $\ge d/2$ (many parameters, poor generalisation), or
* **Depth strategy:** $L=d/6$ layers of small shared kernels (parameter‑efficient, preserves translation symmetry).

Dilated convolutions give $\text{RF}(L)=3(2^{L}-1)$, an *exponential* gain in effective width per added layer.

---

### Practical guidelines synthesised

1. **Target scale**
   *Large‑context tasks* (long sequences, global graph properties): favour **deep stacks** (attention, dilated conv, residual RNN) over very wide layers.
2. **Symmetry present?**
   If so, *honour it*: equivariant layers need fewer parameters; depth increases expressivity mainly by enlarging the receptive field rather than by adding raw capacity.
3. **Avoid early bottlenecks**
   First hidden layer width $\ge d_0+1$ unless a low‑dimensional manifold hypothesis is strongly justified.
4. **Monitor depth efficiency**
   Empirically track *training‑time accuracy vs. depth*: a plateau may indicate that the current kernel radius or irrep set already spans the task’s orbit‑space; adding more layers will only inflate compute.

---

### Residual uncertainty & suggested tests

| Open Issue | Diagnostic Experiment | Notes |
|------------|----------------------|-------|
| Optimal trade-off between depth and dilation in equivariant convs | Grid-search $L$ vs. dilation factor on a synthetic long-range addition task; measure parameter count vs. MSE | |
| Effect of symmetry violations (approximate equivariance) | Inject controlled perturbations that break translation by ε pixels; compare convergence of equivariant vs. dense nets | |
| Tight lower bounds for equivariant width | Theoretical—no complete ReLU analogue of the $d_0+1$ theorem under symmetry; conjecture: minimal width equals **dimension of a separating set of orbit representatives** | Prove or refute on permutation-equivariant set functions |


---

## 1 .2 .4 Computational Graphs

A *computational graph* encodes how signals and parameters flow through a network.  Classically it is a **directed acyclic graph (DAG)** whose vertices are *primitive operations* and whose edges carry tensors.
Geometrically, once every tensor is viewed as a *representation* of the data‑symmetry group $G$, the same DAG becomes a **morphism in the monoidal category $\mathbf{Rep}(G)$**.

---

### C‑1.2.3 Static vs Dynamic Graphs & Automatic Differentiation

| Aspect                  | *Static* graph (“define‑and‑run”)                                                                     | *Dynamic* graph (“define‑by‑run”)                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Construction**        | Built *once* before execution; control‑flow unrolled symbolically. <br>e.g. TensorFlow 1, JAX jit/XLA | Re‑built *at every forward pass* from Python control flow. <br>e.g. PyTorch, TensorFlow eager |
| **Optimisation window** | Whole‑graph rewrites: algebraic fusion, constant folding, layout transform.                           | Local, eager execution; fewer global optimisations.                                           |
| **Control‑flow**        | Loops/conditionals encoded via special **While/If** nodes or explicit unrolling.                      | Native Python loops/branches create new sub‑DAGs on the fly.                                  |
| **Deployment**          | Serialise once; run in C++ runtime, TPU/FPGA.                                                         | FFI overhead each step unless re‑traced and cached.                                           |
| **Debugging**           | Harder—graph opaque, values not available mid‑run unless instrumented.                                | Natural Python debugging, tensors available immediately.                                      |

#### Automatic differentiation (AD)

Let the forward evaluation execute operations

$$
v_k = \phi_k\bigl(v_{i_1(k)},\dots,v_{i_m(k)}\bigr),
\quad k=1,\dots,N,
$$

where each $\phi_k$ is element‑wise or a small linear algebra primitive.

* **Reverse‑mode AD (back‑propagation).**
  For a scalar loss $L=v_N$, initialise $\overline v_N=1$.  For $k=N:1$,

  $$
  \overline v_{i_j(k)} {+}{=} 
  \overline v_{k}
  \partial_{j}\phi_k\bigl(v_{i_1(k)},\dots\bigr),
  \quad j=1\dots m.
  $$

* **Complexity**
  Time: $\Theta(\text{# ops})$.
  Memory: store $v_k$ for every node or **checkpoint**—recompute some $v_k$ on the backward pass to trade time for memory (RNN unrolling typically uses this).

* **Static vs dynamic back‑prop**
  – Static graphs replay the saved topological ordering exactly; gradient graph itself can be optimised.
  – Dynamic graphs traverse the Python call stack at runtime, building the backward pass on the fly († small overhead, ∴ popular for research).

---

### G‑1.2.3 Computational DAG as a Morphism in $\mathbf{Rep}(G)$

1. **Objects.** Each tensor space $\mathbb R^{n}\otimes V_\lambda$ carries a (possibly trivial) representation $V_\lambda$ of the symmetry group $G$.
2. **Morphisms.** A layer is a **$G$-equivariant linear (or affine) map** $f_\theta\colon V_\lambda\to V_\mu$.
3. **Monoidal product.** Parallel edges correspond to the categorical tensor $\otimes$.
4. **DAG → string‑diagram.** The entire forward network is the composite

   $$
   F_\theta = f_L \circ f_{L-1} \circ \cdots \circ f_1 \quad \in \text{Hom}_{\mathbf{Rep}(G)}(V_{\text{in}},V_{\text{out}}).
   $$

Because $\mathbf{Rep}(G)$ is **monoidal closed**, morphism spaces are again representations; thus *gradients*

$$
\frac{\partial L}{\partial \theta_\ell} \in \text{Hom}_{\mathbf{Rep}(G)}(V_{\lambda_{\ell-1}},V_{\lambda_\ell})
$$

are themselves **equivariant**.  Back‑prop corresponds to *pre‑ and post‑composing* with the dual (contragredient) representations:

$$
\delta_\ell  = \bigl(f_{\ell+1}^\ast\circ\cdots\circ f_{L}^\ast\bigr) \delta_L,
$$

where $(\cdot)^\ast$ denotes the transpose map under a $G$-invariant inner product.
The categorical chain rule is therefore a *functor*

$$
\nabla\colon\mathbf{Rep}(G) \to \mathbf{Rep}(G),
$$

mapping a morphism to its **cyclic‑dual composite**.

#### Practical pay‑offs

* **Symmetry‑preserving training.** If every forward morphism is equivariant, reverse‑mode AD *cannot break the symmetry*—the learned parameters remain in the constrained subspace.
* **Compiler design.** Static‑graph optimisers that respect the monoidal structure can fuse consecutive equivariant maps into a single irrep‑block‑diagonal kernel (e.g. convolution + BN + ReLU folded into CUDA‑kernel).
* **Irrep‑wise checkpointing.** Cache only the low‑frequency blocks (often largest), recompute high‑frequency ones—saves memory in SO(3)/SE(3) CNNs for 3‑D shape processing.

---

### Worked example – Back‑prop through a translation‑equivariant conv stack

*Forward.*

$$
\small
x \xrightarrow{\text{Conv}(k_1)} y_1
           \xrightarrow{\text{ReLU}} z_1
           \xrightarrow{\text{Conv}(k_2)} y_2
           \xrightarrow{\text{SumPool}} L.
$$

Every map is translation‑equivariant ($G=\mathbb Z^2$).

*Backward.*

$$
\delta_{y_2} = \mathbf 1,
\delta_{z_1} = \text{Conv}(k_2^\top)\delta_{y_2},
\delta_{y_1} = \delta_{z_1}\odot \mathbf 1_{y_1>0},
\delta_x      = \text{Conv}(k_1^\top)\delta_{y_1}.
$$

The transposed kernels $k_\ell^\top$ satisfy the same *Toeplitz* weight‑tying ⇒ the gradient flow respects translation symmetry **by construction**.

---

### Practical guidelines

1. **Choose graph mode by lifecycle**
   *Research/fast iteration* → dynamic; *production/inference speed* → export to static, allow whole‑graph fusion.
2. **Checkpoint with symmetry awareness**
   In equivariant models, checkpoint at **irreps boundaries** to avoid recomputing expensive Fourier transforms.
3. **Verify equivariance numerically**
   During development, inject random group elements $g$ and check $\lVert F_\theta(g \cdot x) - g \cdot F_\theta(x) \rVert$.  A non‑zero tolerance signals a broken op in the graph or a bug in custom autograd code.

---

### Residual uncertainty & experiments

| Issue                                                          | Suggested test                                                                                                          |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Static optimiser breaks equivariance via layout transforms** | Run the numeric equivariance check before and after XLA compilation; bisect offending fusion pass.                      |
| **Memory–compute trade‑off under group constraints**           | Benchmark gradient checkpoint schemes: layer‑wise vs. irrep‑wise vs. every‑$k$ nodes on a 3‑D spherical CNN.            |
| **Higher‑order gradients in $\mathbf{Rep}(G)$**                | Prove that second‑order adjoints remain equivariant; empirically verify on meta‑learning tasks (MAML) using SE(2) CNNs. |

---

## 1 .2 .5 Architectural Patterns

Modern networks rarely consist of a *pure* stack of identical layers.  Instead, designers weave in **skip connections, gating mechanisms, or multi‑branch blocks** that change optimisation dynamics and expressive bias.
We organise this section into the classical catalogue (**C‑1.2.4**) and a unifying geometric viewpoint (**G‑1.2.4**).

---

### C‑1.2.4 Pattern catalogue

| Pattern                          | Algebraic form (per layer ℓ)                                                                              | Key effect                                                                                                                             | Typical variants                                           |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Residual / skip**              | $x_{\ell+1}=x_\ell + f_\ell(x_\ell)$                                                                      | *Identity path* preserves gradient flow (∂L/∂x ≈ 1) ⇒ mitigates vanishing gradients, enables very deep nets.                           | ResNet, Pre‑activation ResNet, Transformer “Add & Norm”    |
| **Highway / gated residual**     | $x_{\ell+1}=T_\ell\odot f_\ell(x_\ell)+ (1-T_\ell)\odot x_\ell$ with gate $T_\ell=\sigma(W_g x_\ell+b_g)$ | Learns data‑dependent blend between transform and carry; helps early training when $f_\ell$ is randomly initialised.                   | Highway Nets, GRU/LSTM update, GLU                         |
| **Dense connectivity**           | $x_{\ell+1}= \mathrm{Concat}(x_0,x_1,\dots,x_\ell, f_\ell(\cdot))$                                        | Explicit *feature reuse*: later layers see all earlier representations; counteracts information bottleneck at moderate parameter cost. | DenseNet, FiLM, HyperDense RNN                             |
| **Multi‑branch / Inception**     | $x_{\ell+1}= \phi\bigl(\bigoplus_{k=1}^K f_{\ell,k}(x_\ell)\bigr)$ (⊕ = concat or sum)                  | Parallel filters of different *scales / receptive fields* capture multi‑resolution structure with lower FLOPs than one wide filter.    | Inception v3/v4, ResNeXt, MixNet                           |
| **Stochastic depth / drop‑path** | During training, with prob $p$: $x_{\ell+1}=x_\ell$; else residual form.                                  | Acts as layer‑wise ensemble + regulariser; at test time use full depth with rescaling.                                                 | Shake‑Shake, DropPath, Deep Networks with Stochastic Depth |

---

#### Formal properties

1. **Gradient preservation.** For residual blocks, Jacobian

   $$
   J_{\ell} = I + \partial f_\ell(x_\ell),
   $$

   so eigen‑values stay close to 1 when $\lVert\partial f_\ell\rVert\ll1$; back‑prop product $\prod_\ell J_{\ell}^\top$ avoids exponential decay/explosion.

2. **Parameter efficiency.** Dense connectivity increases concatenated width but *does not* multiply parameters quadratically because each $f_\ell$ typically maps to a small growth‑rate $g\ll \text{concat width}$.

3. **Expressive ensembles.** Multi‑branch modules act like *implicit ensemble averaging* of filters at different scales; under mild independence assumptions this reduces variance without increasing bias.

---

### G‑1.2.4 Patterns as geometric stabilisers

The same gadgets emerge naturally when one asks: *How do we integrate an equivariant vector field on feature space while maintaining stability and symmetry?*

#### G‑1.2.4.1 Residual = discrete ODE step

*Continuous model.* Let $z(t)\in V$ (a $G$-representation space).  Consider an equivariant differential equation

$$
\frac{dz}{dt} = f_\theta\bigl(z(t)\bigr),
\qquad f_\theta\in\operatorname{Hom}_{\mathbf{Rep}(G)}(V,V).
$$

*Euler discretisation* with step $h$:

$$
z_{t+h} = z_t + hf_\theta(z_t).
$$

Setting $h=1$ yields exactly the residual update.
**Implications**

* **Near‑identity operator‑norm intuition.** If $\lVert f_\theta\rVert\le\epsilon$, then $\lVert J_\ell\rVert\le 1+\epsilon$ ⇒ stable forward and backward propagation.
* **Flow interpretation.** As depth $L\to\infty$ with $h=1/L$, the network approximates the *time‑$1$ flow* $\Phi^1_{f_\theta}$ on $V$ — bridging residual nets and Neural ODEs.

#### G‑1.2.4.2 Multi‑branch = multi‑resolution orbits

For a translation‑equivariant signal space $L^2(\mathbb Z^d)$:

1. **Wavelet lens.** Let $\{\psi_k\}_{k=1}^K$ be filters whose Fourier supports tile frequency bands.
2. **Branch‑wise processing.** Each $f_{\ell,k}$ acts on the coefficients of band $k$; recombination via ⊕ preserves equivariance because Fourier basis respects group convolution.
3. **Parallel orbits.** Different branches correspond to *distinct orbits in dual space* $\widehat G$ (the set of irreps).  Summation/concatenation is the categorical coproduct: it respects the monoidal structure, so the overall block remains equivariant.

---

### Design heuristics distilled

| Desired property                                         | Pattern of choice        | Geometric reason                                                                                         |
| -------------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------- |
| Stabilise very deep stacks ($L>100$)                 | Residual + LayerNorm     | Small Euler steps keep Jacobian near identity ⇒ well‑conditioned flow                                    |
| Learn *which* features to transform vs. carry            | Highway / gated residual | Introduces a **data‑dependent projector** onto tangent directions of the learned manifold                |
| Aggregate information at multiple spatial scales         | Inception / ResNeXt      | Projects onto several frequency or irrep subspaces simultaneously, then fuses                            |
| Strong regularisation without extra symmetry constraints | Stochastic depth         | Randomly samples sub‑graphs → trains an *ensemble of equivariant flows*; expectation remains equivariant |

---

### Residual uncertainty & proposed tests

| Hypothesis                                                                                                     | Experiment                                                                                          |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **ODE stability bound**: Lipschitz constant $<1$ suffices for exploding‑gradient control even at $L=1000$. | Measure $\max\lVert J_\ell\rVert$ vs. depth in ResNets on CIFAR‑10; correlate with training loss. |
| **Band‑limited branches improve sample efficiency** on small datasets.                                         | Compare single‑branch vs. multi‑branch SO(3)‑CNN for molecular property prediction (≤10 k samples). |
| **Gate saturation risk**: highway gates may freeze with poor init.                                             | Track gate histogram at epoch 0, 1, 10; try *bias init = −1* vs. 0.                                 |

---


## 1 .2 .6 Parameter Sharing & Local Connectivity

### Why this topic matters

*Parameter sharing* reduces the number of learnable weights by forcing *copies* of one parameter tensor to appear in multiple locations inside the computational graph.
*Local connectivity* restricts each output coordinate to depend only on a *neighbourhood* of inputs.
Together, these two ideas simultaneously

* shrink statistical sample complexity (fewer free degrees of freedom),
* improve compute/memory efficiency (smaller tensors, fewer FLOPs), and
* inject an **inductive bias** that matches the symmetries or metric structure of the data domain.

We treat the engineering practice (**C‑1.2.5**) and its geometric foundation (**G‑1.2.5**) in turn.

---

### C‑1.2.5 Weight tying (CNN/RNN) and local receptive fields

| Architecture                             | Parameter‑sharing rule                                                                     | Resulting parameter count                                                                     | Locality mechanism                                                 |
| ---------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **1‑D convolution** (kernel size $k$)    | Same kernel weights reused at every time‑shift                                             | $k C_\text{in}C_\text{out}$ instead of $TC_\text{in}C_\text{out}$ for sequence length $T$ | Sliding window of length $k$                                       |
| **2‑D convolution** (kernel $k\times k$) | Same kernel at each spatial location                                                       | $k^2 C_\text{in}C_\text{out}$ instead of $HWC_\text{in}C_\text{out}$                          | $k\times k$ neighbourhood                                          |
| **Dilated conv** (dilation $\delta$)     | As above, but kernel taps spaced by $\delta$                                               | Same as standard conv                                                                         | Enlarges receptive field without extra params                      |
| **RNN / GRU / LSTM**                     | Reuse the **same** transition matrix $W_{hh}$ and input matrix $W_{xh}$ at every time step | $\bigl(d_h^2+d_xd_h\bigr)$ regardless of sequence length                                      | Causality: each state depends only on previous one                 |
| **Transformer (self‑attention)**         | Projection matrices $W_Q,W_K,W_V$ shared across *token positions*, not across *heads*      | $3d^2$ per head (position‑independent)                                                        | Attention scores computed for *all* pairs ⇒ global receptive field |

**Take‑away.** Without sharing, the number of weights would grow *linearly (RNN) or quadratically (dense image mapping)* in the input size; with sharing it stays *constant*.

---

#### Formal view

Let $\theta$ denote the *base* parameter set and let $S\subset\mathbb N$ index *sites* (pixels, time steps, graph nodes …).
Define an *assignment map*

$$
\pi:\theta\times S \longrightarrow \text{forward‑graph edges},
\quad
\pi(\theta_i,s)=\theta_i^{(s)}.
$$

*Weight tying* asserts $\theta_i^{(s)}=\theta_i\forall s$.
Learning thus optimises a *quotient* parameter space

$$
\Theta_\text{tied} = \Theta_\text{full}\big/ \bigl(\theta_i^{(s)}=\theta_i^{(s')}\bigr),
$$

whose dimension equals $|\theta|$ rather than $|\theta|\cdot|S|$.

---

### G‑1.2.5 Group orbits ⇒ kernel‑sharing; locality from the space’s metric

#### Weight‑sharing = invariance along **orbits**

*Setup.* Let a group $G$ act on the input index set $\mathcal X$.
Two points $x,y\in\mathcal X$ lie in the same *orbit* if $y=g\cdotx$ for some $g\in G$.

*Theorem (Orbit‑wise tying).*
A linear operator $\mathcal L$ is $G$-equivariant **iff** its kernel depends only on the orbit:

$$
K(x,y) = \kappa\bigl(g_{x\leftarrowy}\bigr),
$$

where $g_{x\leftarrowy}$ satisfies $y = g_{x\leftarrowy}\cdotx$.

*Implication.* All kernel entries belonging to one orbit share **one** learnable value ⇒ CNN/RNN weight tying emerges automatically.

#### Locality = bounded diameter in the **metric space** $(\mathcal X,d)$

While equivariance demands orbit‑wise *equality*, it imposes *no* bound on support.
Practitioners additionally assume **metric locality**: choose $\kappa(g)=0$ whenever the displacement $d(x,y)$ exceeds radius $r$.

| Scenario         | Metric                                                   | Orbit‑local kernel                       |   |                     |
| ---------------- | -------------------------------------------------------- | ---------------------------------------- | - | ------------------- |
| 2‑D images       | $d\bigl((r,c),(r',c')\bigr)=\lVert(r,c)-(r',c')\rVert_2$ | 3×3, 5×5 conv kernels                    |   |                     |
| 1‑D audio        | (d(t,t')=                                                | t-t'                                     | ) | 1‑D conv radius $r$ |
| Graph neural net | Shortest‑path length on nodes                            | Message passing within $k$-hop ego‑graph |   |                     |

---

#### Parameter count & effective capacity under symmetry

Let $\mathcal F\_\text{free}$ be the hypothesis space of *unconstrained* linear maps $\mathbb R^{n}\to\mathbb R^{m}$ (dimension $mn$).
Restricting to $G$-equivariant **and** $r$-local kernels gives

$$
\dim \mathcal F_{G,r} = \lbrace \text{group orbits inside radius }r\bigr \rbrace \times C_\text{in}C_\text{out}.
$$

Example—2‑D conv with $r=1$ (3×3):

$$
\text{orbits}=9
\Longrightarrow
|\theta|=9C_\text{in}C_\text{out},
$$

versus $mn = (HW)C_\text{in}C_\text{out}$ for a dense layer.
The **VC‑dimension** scales linearly with $|\theta|$, so training data needed for good generalisation shrinks by a factor of $\frac{9}{HW}$.

---

### Design heuristics

1. **Let the data’s symmetry dictate sharing.**
   *Images* → translational tying; *sets* → permutation tying (DeepSets); *molecules in 3‑D* → SE(3) weight tying (Tensor Field Nets).
2. **Set locality radius to match noise scale.**
   If the task relies on *fine textures* (super‑resolution), use $r=1,2$.  For *global cues* (scene classification) rely on depth/dilation to enlarge receptive field instead.
3. **Untie cautiously when symmetry is broken.**
   Small learnable *positional embeddings* or *Fourier‑feature bias* often suffice—no need to abandon sharing wholesale.
4. **Tie recurrent weights unless strong evidence says otherwise.**
   Untying across time steps multiplies parameters by sequence length and rarely improves performance except in tiny‑sequence regimes.

---

### Residual uncertainty & experiments

| Question                                                  | Suggested experiment                                                                                                                                                      |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **How local is optimal?** Depth‑$L$, radius‑$r$ trade‑off | Grid‑search $r\in\{1,3,5,7\}$, depth adjusted s.t. receptive field ≥ image size; plot accuracy vs. parameter count                                                        |
| **Is strict equivariance too rigid for real data?**       | Train two CNNs on panoramas: (i) shared kernels, (ii) kernel±ε Gaussian noise (break symmetry); compare overfitting gap                                                   |
| **Parameter tying vs. batch‑size sensitivity**            | Measure test loss as batch size varies (32…1 k) for fully‑shared vs. partly‑untied Transformer; hypothesis: fewer params ⇒ lower variance ⇒ less batch‑size tuning needed |

---

## 1 .2 .7 Capacity, Parameter Count & Memory Footprint

The last ingredient of an architectural blueprint is **resource accounting**.
How many tunable degrees of freedom does the model expose?
How many floating‑point operations (FLOPs) and how much RAM/VRAM do forward + backward passes consume?
Answering these questions at two conceptual levels—**classical bookkeeping** and a **symmetry‑aware refinement**—helps translate high‑level design targets (quality, latency, hardware budget) into concrete layer sizes.

---

### C‑1.2.6 Counting weights, activations, FLOPs, memory

\| Layer type | Weight count $|\theta_\ell|$ | Forward FLOPs† | Activation memory‡ |
\|------------|--------------------------------|----------------|--------------------|
\| Dense $d_\text{in}\tod_\text{out}$ | $d_\text{in}d_\text{out}+d_\text{out}$ | $2d_\text{in}d_\text{out}$ | $B d_\text{out}$ |
\| 2‑D Conv $k\times k$ | $k^2 C_\text{in}C_\text{out}$ | $2k^2HW C_\text{in}C_\text{out}$ | $BHW C_\text{out}$ |
\| Depth‑wise Separable Conv | $k^2 C_\text{in}+C_\text{in}C_\text{out}$ | $2k^2HW C_\text{in}+2HW C_\text{in}C_\text{out}$ | "$$" |
\| Self‑Attention (1 head) | $3d^2 + d^2$(proj) | $4N d^2 + N^2 d$ | $B N d + B N^2$ (attn mat.) |
\| GRU / LSTM cell | $4d_hd_x + 4d_h^2 + 4d_h$ (GRU) | $\approx8d_h(d_x+d_h)$ per‑time‑step | $B T d_h$ |

† Multiply‑adds counted as 2 FLOPs; $H,W,N,T,B$ = height, width, sequence length, time steps, batch size.
‡ Excludes optimizer‑state and gradient storage; backward pass roughly triples activation memory if everything is checkpointed.

**Key scaling laws**

* **FLOPs ∝ activation size × kernel size × out‑channels.**
  Reducing spatial resolution by 2 cuts FLOPs by ≈ 4 in conv nets.
* **Self‑attention is quadratic in sequence length $N$.**
  Approximate variants (flash, local, linear) trade accuracy for $O(N\log N)$ or $O(N)$ cost.
* **Backward pass cost.**
  Adds the same‑order FLOPs as forward, plus extra memory for saved activations; gradient‑checkpointing multiplies compute by ≤ 2 but cuts memory in half or more.

---

### G‑1.2.6 Effective capacity under symmetry; reduced sample complexity

#### 1. Parameter‑space dimension modulo symmetry

For a $G$-equivariant, $r$-local convolution on a $d$-dimensional grid

$$
|\theta_\ell|
=|\text{orbits within radius }r|\timesC_\text{in}C_\text{out}
=(2r+1)^d C_\text{in}C_\text{out},
$$

independent of the *input* spatial extent $H×W$.
Hence a 7×7 kernel on ImageNet ($H=224$) has the same 49 × $C_\text{in}C_\text{out}$ weights whether images are 224 px or 1024 px wide.

#### 2. Generalisation gap shrinks with *effective* capacity

Statistical learning theory yields risk bounds

$$
\mathcal E_\text{gen}
\lesssim
\sqrt{\frac{\operatorname{VC}(\mathcal F)}{n}}
\quad\text{or}\quad
O\Bigl(\sqrt{\tfrac{\mathfrak R_n(\mathcal F)}{n}}\Bigr),
$$

where VC‑dimension or Rademacher complexity $\mathfrak R_n$ scales with *number of free parameters*.
Tying weights across $G$-orbits divides capacity by

$$
\frac{HW}{(2r+1)^2}\quad(\text{vision}),\qquad
\frac{N}{d_\text{irrep}}\quad(\text{sets/graphs}),
$$

thus lowering the **sample complexity** needed for a target error by the same factor.

#### 3. Irrep factorisation reduces run‑time memory

Equivariant kernels block‑diagonalise in the Fourier/irrep domain; many high‑frequency blocks are small and sometimes pruned entirely.
During training on 3‑D point clouds (SE(3) symmetry) one typically keeps only $\ell\le 3$ spherical harmonics, slashing both parameter and activation tensors by \~10× compared to a naïve$C_\text{in}C_\text{out}$-wide dense kernel.

---

### Trade‑off patterns & engineering playbook

| Constraint                           | Common response                                                                 | Geometric rationale                                                                                  |        |                                                                         |
| ------------------------------------ | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------ | ----------------------------------------------------------------------- |
| **GPU VRAM ceiling**                 | *Mixed precision* (FP16/BF16) + *activation checkpointing* every $k$ layers     | Lower mantissa bits shrink each tensor; recomputation respects layer equivariance so no accuracy hit |        |                                                                         |
| **Latency budget (mobile)**          | Depthwise‑separable or group conv + small channel multipliers                   | Factorises convolution into separate irrep blocks (spatial vs. channel) ⇒ fewer MACs                 |        |                                                                         |
| **Throughput for long sequences**    | Flash / local attention, sliding‑window conv + dilation                         | Restricts interactions to a *band* of group‑orbits; approximate equivariance but linearised compute  |        |                                                                         |
| **Small dataset / labelled samples** | Maximise sharing, freeze low‑level kernels, use equivariance‑aware pre‑training | Smaller (                                                                                            | \theta | ) ⇒ lower generalisation error; symmetry priors transfer across domains |

---

### Worked cost sheet – **ResNet‑18 (ImageNet)**

| Resource                    | Vanilla accounting      | Symmetry‑aware commentary                                                                                                             |
| --------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Params                      | 11.7 M weights          | All but the first FC layer follow $\mathbb Z^2$-equivariant kernel tying; effective freedom ≈ 5.3 M                                   |
| FLOPs                       | 1.8 G per 224×224 image | Same; but pruning symmetric high‑frequency channels (e.g. skip $3×3$ kernels in early layers) can cut ≈ 20 % FLOPs without top‑1 loss |
| Activation memory (B = 128) | 530 MB in FP32          | 140 MB in FP16 + checkpoint @ every 2 blocks                                                                                          |
| Training set                | 1.28 M images           | VC bound ∝ 11.7 M/1.28 M ≈ 9. Symmetry halves numerator → bound ≈ 4.5 (looser but indicative).                                        |

---

### Residual uncertainty & experiments

| Question                                                                  | How to test                                                                                                                                      |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Are theoretical capacity gains realised in practice?**                  | Compare learning curves of (i) equivariant CNN vs. (ii) same‑sized untied CNN on subsampled ImageNet (1 %, 10 %); report data‑efficiency ratios. |
| **Memory‑optimal checkpoints in irrep space?**                            | Implement irrep‑wise recomputation in an SO(3) Tensor Field Net; measure wall‑clock vs. baseline layer‑wise scheme.                              |
| **When does attention’s $O(N^2)$ cost break even with conv’s $O(Nk^2)$?** | Derive analytic threshold $N_\star(k,d)$; validate by timing both kernels on A100 GPU across N = 256…32 k.                                       |

---
