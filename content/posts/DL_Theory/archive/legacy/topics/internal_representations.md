---
_build:
  render: never
  list: never

date: "2025-07-11"
title: "Internal Representations of Neural Networks"
summary: "Internal Representations of Neural Networks"
lastmod: "2025-07-11"
category: "Notes"
series: ["DL Theory", "DL Topics"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

## Prompt to update this text

```text
Please update and expand the "Synthesis: Strengths & Blind Spots" table with the following enhancements:

1. **Add new methods**: Include any interpretability methods mentioned in the survey but missing from the current table (e.g., Feature Visualization, Automated Dictionary Learning, Activation Maximization)

2. **Add new columns**: 
   - "Computational Cost" (Low/Medium/High)
   - "Scalability" (Poor/Moderate/Good) 
   - "Best Use Cases" (brief description)
   - "Recent Advances (2024-25)" (key developments)

3. **Expand existing entries**: 
   - Make the "Strengths" and "Limitations" more specific and detailed
   - Include quantitative insights where mentioned in the survey
   - Add cross-references between methods (e.g., "Complements X method")

4. **Organizational improvements**:
   - Group methods by category (e.g., "Information Detection", "Causal Analysis", "Global Structure")
   - Add a "Maturity Level" indicator (Established/Emerging/Experimental)
   - Include a "Recommended Combinations" section

5. **Future-oriented additions**:
   - Add a row for "Emerging Hybrid Approaches" 
   - Include the survey's recommendations for method combinations

Please maintain the table format but expand it to be more comprehensive and actionable for practitioners choosing between interpretability approaches.
```

# Neural Network Interpretability: Key Research Lines

## Core Research Approaches

### 1. **Linear Probes** - Testing Information Availability
- **What**: Train lightweight classifiers on frozen network activations to test if information is "linearly present"
- **Key insight**: Linguistic features emerge layer-by-layer in BERT; even complex world models (like Othello board state) can be linearly decoded
- **Limitation**: Shows information exists but not how it's used

### 2. **Geometric Similarity** (RSA, CKA)
- **What**: Compare representation matrices between layers/models using basis-invariant metrics
- **Key insight**: Different ResNet initializations converge to nearly identical representational trajectories
- **Limitation**: No causal information—high similarity doesn't mean shared computation

### 3. **Unit-Level Analysis**
- **Network Dissection**: Measure neuron-concept alignment using pixel-accurate masks
- **Concept Erasure**: Zero out activations and measure output degradation
- **Finding**: Interpretability increases with network width/depth

### 4. **Causal-Mechanistic Interpretability** ("Circuits")
- **What**: Path-patching to identify minimal functional subgraphs
- **Breakthroughs**: 
  - Induction heads for in-context learning (2022)
  - Claude-3 "brain scanner" identifying thousands of interpretable features (2024)
- **Challenge**: Labor-intensive, doesn't scale easily

## Major Theoretical Frameworks

### **Superposition & Polysemanticity**
- Networks encode more features than dimensions by using sparse, interleaved directions
- Individual neurons appear "polysemantic" (multi-concept) by design
- **Implication**: Perfect single-neuron semantics are not expected

### **FER vs UFR Framework** (2024-25)
Revolutionary network-wide diagnostic distinguishing:
- **Unified-Factored Representation (UFR)**: Each concept implemented once; smooth weight changes
- **Fractured-Entangled Representation (FER)**: Redundant, coupled circuits; chaotic sensitivity

**Key finding**: SGD reaches identical performance but lands in brittle FER, while evolutionary search yields robust UFR.

## Current Frontier (2024-25)

1. **Basis-invariant global metrics** complementing local probes
2. **Open-ended training** as representational regularizer
3. **Cross-modal alignment** in vision-language models
4. **Safety-critical interpretability** with adversarial evaluations

## Synthesis: Strengths & Blind Spots

| Method | Strengths | Limitations |
|--------|-----------|-------------|
| Linear probes | Fast, quantitative feature detection | Miss wiring & causality |
| RSA/CKA | Layer-to-layer geometry | Ignores redundancy; can't detect FER |
| Unit alignment | Pinpoints concept detectors | Assumes single-unit semantics |
| Causal circuits | High-resolution functional maps | Labor-intensive, local scope |
| FER/UFR assay | Global modularity test | Limited to toy domains so far |

## Key Trend
Moving from *"information is somewhere"* to *"we know exactly how the whole network computes"* through causal, holistic methods combining sparse dictionary learning, circuit tracing, and path-agnostic metrics.

## Open Research Question
Will scaling + regularization naturally push networks toward UFR (representational optimism), or are training-path interventions necessary? The FER/UFR hypothesis makes this empirically testable.

## Practitioner Recommendations
1. **Combine methods**: Run linear probes AND weight-sweep tests
2. **Enforce sparsity early**: Use sparse auto-encoders during training
3. **Curriculum design**: Master foundational patterns before complex compositions
4. **Benchmark global modularity**: Adopt FER-style metrics alongside accuracy
