---
date: '2025-12-07'
title: 'Thoughts on Feasibility in Pre-training GPT-2/3 on a Single GPU'
summary: One idea to reduce compute in pre-training
description: One way to reduce pre-training budget by reducing data needed to be processed
lastmod: '2025-12-07'
category: Blog
series:
- Research Notes
tags:
- AI
status: draft
author: Bryan Chan
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

The breakthrough in pre-training of GPT-2/3 reveals the insight that scaling recipes can lead to genuine large improvements in language-related tasks.

As a rule of thumb, if you want to have a smarter model, just throw more compute at it, and it would work.

The scaling recipe tells us that loss decays as a smooth power law with respect to model size, data, and compute.

> Everything is fine, just the price tag is absurd.

For most independent researchers and start-ups, it is just difficult to self-replicate artefacts with the scaling recipe.

Even faithful GPT-2/3 style pre-training assumes multi-GPU setups, generous VRAM, and power bills that look like small-company annual budgets.

At some point, the limitations of resources just forced me to ask:

> How far can we scale **down** while still getting the same or even more interesting behaviours from these models?

> In particular, to find a way such that it is feasible to pre-train a GPT-2/3 class model on a single consumer GPU within a reasonable time frame.

But to achieve this feat, given the hardware is fixed, the only variables one can change are things like training algorithm, neural network architecture, the amount of computation needed, etc.

I soon realised that to find that way, it requires non-trivial improvement. Incremental improvements cannot really help here, as according to Amdahl's law: "the improvement you get from speeding up one part of a system is limited by how often that part is actually used." To get there, it requires jumps in improvements.

If you strip away the details of the optimiser and constant factors, a decoder-only transformer's training cost is dominated by matrix multiplications over tokens.

One coarse rule of thumb is:

$$
\text{FLOPs} \approx C \cdot n_{\text{layers}} \cdot d^2 \cdot N_{\text{tokens}}
$$

where $n_{\text{layers}}$ is depth; $d$ is model width; $N_{\text{tokens}}$ is the total number of input tokens processed; and $C$ hides the implementation details (i.e., attention vs MLP costs, fusing ops, etc).

There are three obvious levers in reducing FLOPs:

1. Make the model smaller (decrease $n_{\text{layers}}$, $d$)
2. Learn faster (better optimisers, curricula, initialisation) so fewer compute steps are needed to reach convergence
3. Reduce the number of tokens needed to represent the same underlying data

Given my then and current lack of understanding of neural network architectures, training algorithms, as well as the alternatives that can be accounted for—such as design choices that are selected out due to the hardware lottery—I am unable to survey all of the design choices and options. Therefore, the only viable option for me to start with is to reduce the amount of computation needed, which is to reduce the amount of internet information used to pre-train the models, while retaining all the information fidelity needed for getting full and rich internal representations.

I turn to compression algorithms and studying tokenisation, in the attempt to push option 3 to the extreme: to represent the same data with far fewer and more information-dense tokens.


## What is Tokenisation?

Tokenisation is the process of transforming raw text or bytes into a sequence of discrete symbols, called tokens, that a language model can consume and predict. Instead of operating directly on Unicode characters or words, the model works over a finite vocabulary of tokens, each associated with an integer identifier and an embedding vector.

A tokeniser defines a deterministic mapping from strings to token sequences and a corresponding inverse that reconstructs the original text, at least for well-formed inputs. In practice, tokenisation sits between the messy world of natural language and the strictly discrete world of neural sequence models.

Depending on design, tokens may be whole words, subword fragments like prefixes, stems, and suffixes, individual characters, or raw bytes. Modern large language models favour subword or byte-based schemes because they avoid out-of-vocabulary failures while keeping sequences reasonably short.

Conceptually, tokenisation plays the role of a compression-oriented alphabet design: it decides which recurring patterns in text become atomic symbols and which remain compositions of simpler units. Once a tokeniser is fixed, every stage of model training and deployment is expressed in that symbolic language. Gradients, probabilities, losses, and safety rules are all computed over tokens rather than over human-readable strings.

In this sense, tokenisation is not mere preprocessing, but part of the effective architecture and hypothesis space of the model, governing what it can represent compactly and what it must express through longer, more diffuse sequences of predictions. Its design therefore strongly influences model behaviour.


## How Tokenisation Works

Tokenisation works by inserting a learned, deterministic coding layer between raw text and the neural network. Conceptually there are two stages. First, during tokeniser training, we build a vocabulary and segmentation rules from a large corpus. Second, during application, we use those rules to break new text into tokens and map them to integer identifiers.

Training usually begins by normalising text, then representing each sentence as a sequence of primitive symbols such as characters or bytes. An algorithm such as byte pair encoding, WordPiece, or a unigram language model scans the corpus, discovers frequently recurring substrings, and promotes them into vocabulary items. This process continues until a target vocabulary size is reached or compression saturates. The result is a finite vocabulary, plus either an ordered merge list or a probabilistic model describing how to segment any new string.

At inference, the same normalisation is applied to user input. Optional pre-tokenisation may split on whitespace and punctuation. The subword algorithm then segments each resulting span, typically by greedily applying merges, longest-match search, or dynamic programming to choose tokens whose concatenation exactly recovers the original text. Each token string is replaced by its index in the vocabulary, producing a sequence of integers that feed the model's embedding layer.

Generated token indices are finally mapped back through the vocabulary and concatenated, plus any inverse normalisation, to form user-facing text. In this way tokenisation defines a reversible interface between continuous text and discrete computation. Efficient implementations make this mapping effectively constant time.


## Why Tokenisation is Important

Tokenisation is important because it defines the alphabet in which a language model thinks, learns, and pays for computation. The model never sees human-level text; it only sees sequences of token identifiers. Changing tokenisation therefore changes the effective prediction task, the geometry of embedding space, and the structure of contexts the model must master.

A good tokeniser compresses recurring patterns into single symbols, so that each forward pass conveys more information per step and fewer steps are needed to cover a passage. This reduces training and inference FLOPs for a fixed context window, or equivalently allows longer contexts and larger models under the same computational budget. Conversely, a poor tokeniser explodes benign strings into many tokens, wasting compute, shrinking useful context, and making learning unnecessarily difficult.

Tokenisation also shapes what the model can represent compactly. If morphologically meaningful units or common phrases correspond to single tokens, the model can slot them into internal representations and reuse them systematically. When such structure is fragmented across inconsistent token boundaries, the model must reconstruct it indirectly from longer chains, which is fragile and data-hungry.

Beyond efficiency and expressiveness, tokenisation is a safety, robustness, and fairness parameter. Safety filters, preference models, and prompt templates all operate over tokens, so segmentation quirks create attack surfaces and blind spots. Multilingual coverage and equity likewise depend on how economically different scripts and languages are encoded.

For constrained researchers, tokenisation becomes a key lever for squeezing maximal signal out of a limited pre-training budget.


## Road-blocks and Constraints in Tokenisation

Several roadblocks constrain tokenisation and prevent it from becoming a purely Shannon-optimal compression scheme.

**Losslessness**: Tokenisation must be lossless and reversible for ordinary inputs, which imposes structural constraints. Tokens must form a partition of the string into contiguous pieces whose concatenation exactly reconstructs the original sequence, and decoding must behave sensibly when performed incrementally during streaming.

**Unicode handling**: Tokenisation must respect the quirks of Unicode encodings such as UTF-8. Byte-level vocabularies that include arbitrary byte patterns can technically represent any sequence, but they can also produce ill-formed Unicode or ambiguous partial characters when detokenised prematurely.

**Speed and determinism**: Tokenisation must be fast and deterministic, because every training step and inference call must pass through it. The space of possible segmentations is combinatorially large, yet practical algorithms must commit to one segmentation using greedy search or dynamic programming within linear or near-linear time.

**Neural architecture compatibility**: The vocabulary size and token frequency distribution must remain compatible with efficient neural architectures. Very large vocabularies with many singleton tokens improve compression but explode the embedding and output layers, while extremely skewed token distributions are hard for optimisers to learn from.

**Multilingual fairness**: Tokenisation should support multilingual and morphologically rich languages without unfairly inflating their token counts, yet it has only a limited symbol budget to allocate across scripts.

**Safety and robustness**: Safety and robustness concerns discourage overly pathological or opaque tokens, since adversaries can exploit segmentation quirks.

Together these constraints force tokenisation to compromise between compression, learnability, and reliability rather than optimising any single objective globally.


## Why Not Just Use a Compression Algorithm Directly?

At first glance it is tempting to imagine replacing tokenisation entirely with a powerful compression algorithm such as 7z. If compression can represent a terabyte-scale crawl of the internet in a far smaller archive, why not simply feed those compressed bytes to the model and thereby reduce the number of tokens that must be processed during pre-training?

The difficulty is that generic compressors and tokenisers solve slightly different problems under very different constraints. A compressor like 7z is allowed to choose variable-length codes that depend on global corpus statistics, use elaborate dictionaries, and exploit long-range repetition across file boundaries. Its output is a dense bitstream that is optimised for minimal average length, not for incremental, semantically meaningful prediction. From the model's perspective, such a bitstream is almost random; local patterns are deliberately flattened. Training on it would destroy the underlying linguistic structure we actually want the network to model.

Tokenisation must instead *expose* structure, not conceal it. Even if we tried to let the tokeniser mimic 7z by turning every dictionary entry or repeated phrase into a token, we would immediately face the **partitioning problem**. For any given vocabulary there are exponentially many ways to segment a document into tokens. Achieving near-optimal compression would require searching this combinatorial space for each input, guided by a global objective, which is computationally prohibitive at web scale.

Practical tokenisers therefore use greedy or locally optimal segmentation rules that deliberately sacrifice some compression in exchange for determinism, speed, and linguistic transparency. In short, tokenisation cannot fully inherit the global compression gains of 7z without erasing the very patterns that make language learnable. Moreover, classical compressors ignore constraints like streaming detokenisation, fixed vocabulary embeddings, and stable semantics across prompts that downstream models critically require in deployment.


## How Meta's Byte-Latent Transformer Comes to the Rescue

Meta's Byte Latent Transformer can be seen as an answer to the limitations of hand-designed tokenisers described above. Instead of fixing a vocabulary and heuristic segmentation rules in advance, the model learns a compact, variable-rate code for bytes using a small neural compressor and a larger transformer operating on its outputs.

The compressor scans the raw byte stream and groups it into **dynamically sized patches**. These patches are not arbitrary; boundary decisions depend on the predicted entropy of the next byte or short context window. Where the byte-level predictive distribution is sharp and low entropy, long runs can be merged into a single patch. Where uncertainty spikes, patches become shorter, giving the downstream transformer more, finer-grained tokens exactly where structure is richer or more surprising.

Each patch is mapped into a discrete latent code from a moderate-sized codebook by vector quantisation or a similar mechanism. The transformer then models sequences of these byte latents rather than individual bytes or brittle subword units.

This architecture effectively internalises tokenisation as learned compression. The hard partitioning problem is moved into a trainable network that can explore many candidate segmentations implicitly and learn to place boundaries so as to minimise overall modelling loss. Because the compressor's parameters are shared across examples, it amortises the cost of searching for good segmentations.

At the same time, the variable granularity of patches allows the system to approach the compression efficiency of advanced codecs while respecting streaming, vocabulary, and learnability constraints. In practice, this means more information-dense tokens, fewer total positions, and better utilisation of limited compute on a single GPU.

Crucially, the downstream transformer never needs to solve segmentation itself; it simply consumes a sequence of well-behaved latent tokens whose boundaries already reflect underlying information content and structural salience directly.

---


## Some tinking Experiments on Colab

Up to this point, most of the discussion has been conceptual: why tokenisation matters, why off-the-shelf compressors are not enough, and how Meta’s Byte-Latent Transformer points to a more principled “compress-then-pretrain” story on bytes. At some stage, however, the question stops being philosophical and turns engineering-blunt:

> If I actually build a tiny BLT-style system and train it on a single T-class GPU, does anything interesting happen?

Over the past weekend, I tried to answer this question with a sequence of small but increasingly concrete experiments. What follows is not a polished result, but a snapshot of what worked, what broke, and what that suggests for feasibility.

### HEAT: An LZ77-Informed Transformer on Synthetic Data

The first prototype, which I called HEAT, was deliberately modest. Instead of a full neural compressor, it used a classical LZ77 pre-processor as a “hard” front-end. The compressor scans the raw byte stream and emits a sequence of two kinds of tokens:

- **Literals**, carrying short patches of raw bytes.  
- **Matches**, carrying a distance–length pair that says “copy `length` bytes from `distance` bytes back in the already-seen history.”

HEAT treats these LZ77 tokens as if they were a learned alphabet. Each literal patch is embedded by a small local network that sees the actual bytes, while each pointer is embedded by a separate “pointer encoder” that only sees the symbolic `(distance, length)` pair. A simple type embedding marks whether a position is a literal or a match. These vectors form a compressed sequence that a standard causal transformer then models.

The critical training trick is the **next-patch objective**. Instead of asking the model to predict the next LZ symbol verbatim, which leads to a degenerate “just copy the pointer” solution, the target at time step \(t\) is the raw bytes associated with token \(t+1\). When the next token is a pointer, the model must mentally dereference it: the correct answer is the bytes that *would* be copied, not the pointer itself. This forces the transformer to actually reason about the compressed structure rather than memorise symbolic distances.

On a synthetic Colab-scale dataset built from repeated patterns plus random noise, HEAT and a byte-level GPT baseline were given the same transformer backbone and trained under the same approximate FLOPs budget. The only difference was what they saw as input: raw bytes for the baseline, LZ77 tokens for HEAT.

Even in this toy regime, a few patterns already appeared:

- Because many repeated spans collapse into single match tokens, HEAT’s **sequence length in tokens** is much shorter than the raw byte length. A context window of a few hundred compressed tokens corresponds to several thousand raw bytes.
- As training proceeds, the HEAT model’s **bits-per-byte** drops faster than the baseline’s for the same number of optimisation steps, and its BPB-vs-FLOPs curve sits consistently below the byte-GPT curve.
- The qualitative behaviour of HEAT’s predictions on the synthetic task aligns with the intended semantics: it actually reconstructs the underlying patterns rather than parroting pointers.

This experiment is too small to draw strong conclusions about natural language, but it gave a first sanity check: even with a crude compressor, **teaching the transformer to think in compressed LZ tokens can pay off per FLOP**.

### LZ-BLT vs Byte-GPT on Tiny Shakespeare

The next step was to move from toy synthetic data to a small but real corpus: a 100 kB slice of the standard Tiny Shakespeare dataset. The goal here was not to reach state-of-the-art perplexity, but to see whether the HEAT idea survives contact with “messy” text on a single GPU.

The setup is intentionally simple:

- Take the raw Shakespeare bytes (roughly 100 000 characters).
- Run a lightweight LZ77 tokenizer over this corpus to obtain a sequence of LZ tokens. In the Colab run, this yields a compression ratio of about 2.4× in terms of raw bytes per LZ symbol.
- Train two models under the same configuration:
  - A **Byte-GPT baseline**, a small causal transformer that reads and predicts raw bytes directly.
  - An **LZ-BLT model**, architecturally similar to HEAT but closer in spirit to Meta’s BLT: an LZ embedding layer, a local encoder that groups LZ tokens into patches, a global transformer over those patch-latents, and a local decoder head that predicts the next symbol in the compressed sequence.

Both models share the same depth, width, and optimiser, and we track not only loss and bits-per-byte over time, but also BPB as a function of cumulative FLOPs. The effective context window is also compared by plotting how many raw bytes are “visible” as a function of input length when we account for the LZ compression ratio.

The headline numbers after a longer 5 000-step run with a lower sampling temperature are striking:

- The **Byte-GPT baseline** converges to around **2.17 bits per byte** on this tiny corpus.
- The **LZ-BLT model** reaches around **0.69 bits per byte** on the compressed representation, while its LZ tokenizer achieves a compression ratio of roughly **2.5×** on the input text.

Interpreting these together, the LZ-BLT model is effectively “seeing” about two and a half times more raw bytes per token and still assigning them a significantly lower bit budget than the baseline. In the BPB-vs-FLOPs plots, the LZ-BLT curve dominates: for any fixed compute budget within this small-scale setting, the compressed model achieves a lower effective entropy bound.

For downstream uses that care primarily about **representations**—learning embeddings, serving as a feature extractor for classification, or acting as a compressor—this is exactly the pattern one hopes to see. Under the same single-GPU constraints, the compressed model gets more information-dense context and makes better predictions per FLOP.

### Pointer Drift: When Compression Fights Autoregressive Generation

The moment we switch from training curves to **sampled generations**, the picture becomes more subtle.

The byte-level GPT baseline, when prompted with something like “The King ”, produces short continuations that, while far from perfect Shakespeare, at least read like plausible English: words, spaces, punctuation, and basic sentence structure survive temperature-0.3 sampling.

The LZ-BLT model, in contrast, produces text that looks like a hallucinated cousin of Shakespeare: recognisable fragments of words spliced together into almost-words—an “indeed” fused with something else, a “remember” and “assemble” blurred into a single token, consonants doubled or dropped, spaces missing. The character distribution and rhythm feel vaguely right, but the actual strings are broken.

This behaviour matches the failure mode you can reason about from first principles: **pointer drift**.

During compression, an LZ77 “match” token is defined relative to a specific history buffer: “copy 7 bytes from 50 bytes ago” assumes that those 7 bytes are exactly what was observed in the original text at that offset. During generation, however, the model is sampling; any early mistake—one wrong byte in a literal, one mis-chosen match—changes the future contents of the history buffer. When the model later predicts a match that, during training, corresponded to “copy the letters  *r e m e m b e r*”, the same `(distance, length)` in the perturbed history might now point into the middle of a different word or across a boundary. The mismatch compounds over time, and the output devolves into semi-coherent gibberish even though the model has clearly internalised aspects of the compressed structure.

At this point there is a tension:

- From a **compression and training** point of view, predicting LZ symbols is wonderful: it forces the model to reason about copy structure and yields excellent BPB and FLOP-efficiency curves.
- From a **generative** point of view, those very pointers are a liability: the slightest history mismatch can send them astray.

The immediate architectural thought is to decouple these roles: let the model *think* in compressed space while *speaking* in raw bytes.

### Iterative Re-compression: Keeping Pointers Grounded

One natural way to remove pointer drift without discarding the LZ structure is to re-align symbolic compression with the generated text at every step. This is the idea behind the later **iterative re-compression** experiments.

The LZ-BLT implementation in this phase still predicts LZ77 symbol triples—type, value, and length—but the **generation loop** is modified:

1. We keep a growing buffer of the raw bytes generated so far.
2. At each step, we **re-compress the entire current buffer** using the same LZ77 tokenizer used in training. This yields a fresh, self-consistent sequence of symbols whose pointers are guaranteed to be valid for this exact history.
3. We crop or pad this symbol sequence to the model’s patch-based input shape and run a forward pass to predict the next symbol triple.
4. We decode that single symbol back into bytes using the *current* history buffer (for a match, this means copying from the buffer; for a literal, just appending the literal bytes).
5. We append those bytes to the buffer and repeat.

By re-compressing at every generation step, we ensure that the model never relies on stale pointers: every symbol it sees is computed from the text it has actually produced so far. Pointer drift, in the sense of “LZ pointers referring to a history that never existed,” is eliminated by construction.

This comes with an obvious cost. The generation loop now does work proportional to:

- the cost of re-compressing the current history at each step, and
- a full forward pass through the transformer for every new symbol,

which is considerably heavier than the usual “single pass over a growing context” in standard autoregressive models. For small sequences and debugging-scale experiments this overhead is manageable; for large-scale pre-training it would need careful engineering or amortisation.

Nonetheless, as a **conceptual prototype**, iterative re-compression proves that the core pathology of the initial LZ-BLT generations—pointers drifting off target—is not an inherent impossibility result. It is a consequence of naively mixing training-time compression and test-time generation. Once we insist that compression is always recomputed from what the model actually produced, the symbolic story becomes self-consistent again.

### What These Experiments Say About Feasibility

Taken together, these prototypes suggest a mixed but encouraging picture for single-GPU pre-training via compression:

- On both synthetic and tiny-Shakespeare data, **modelling in compressed LZ space chews through entropy faster than a byte-level GPT** under similar FLOPs. The models see more effective context per token and achieve lower bits-per-byte on the data they are trained on.
- The cost of this efficiency is that **generation over compressed symbols is fragile**. Pointer structures that are benign in analysis become dangerous when driven by a stochastic sampler.
- Iterative re-compression and “local decoder” ideas show that this fragility is not fundamental. There are ways to keep the history and its compressed representation aligned, at the cost of added complexity and compute in the decoding path.

For the central question of this note—*is it realistic to pre-train something GPT-2/3-like on a single GPU by being clever about tokens?*—these results look like a qualified “yes” on the *training* side and a large “to be continued” on the *generation* side. The experiments do not yet give me a practical model I would ship, but they do justify pushing further along this line: if compression can reliably buy a few bits-per-byte and a 2–3× context multiplier per FLOP at small scale, then scaling the same principles may be one of the few levers available to a resource-constrained researcher.

