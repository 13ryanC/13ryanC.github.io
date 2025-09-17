---
date: "2025-06-30"
title: "St Petersburgs Paradox"
summary: "St Petersburgs Paradox"
category: Tutorial
series: ["RL Theory"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

### The Mathematics of the St. Petersburg Paradox: Why Infinite Expectation Doesn't Mean Infinite Value

The St. Petersburg Paradox exposes a fascinating conflict between the calculated mathematical expectation of a game and the intuitive price a rational person is willing to pay. The core of the paradox lies in the calculation of the expected value, a fundamental concept in probability theory.

#### 1. Defining the Core Components

To understand the mathematics, we must first define the key terms:

* **Probability (\(P(k)\)):** The game ends when the first head appears on the \(k\)-th flip. The probability of this specific sequence of outcomes (k-1 tails followed by one head) is given by the formula for a geometric distribution:
    \(P(k) = (\frac{1}{2})^k\)
    * For \(k=1\) (Heads on the first flip): \(P(1) = (\frac{1}{2})^1 = \frac{1}{2}\)
    * For \(k=2\) (Tails, then Heads): \(P(2) = (\frac{1}{2})^2 = \frac{1}{4}\)
    * For \(k=3\) (Tails, Tails, then Heads): \(P(3) = (\frac{1}{2})^3 = \frac{1}{8}\)

* **Payoff (\(V(k)\)):** The payout if the game ends on the \(k\)-th flip is:
    \(V(k) = 2^{k-1}\)
    * For \(k=1\): \(V(1) = 2^{1-1} = 2^0 = \\)1$
    * For \(k=2\): \(V(2) = 2^{2-1} = 2^1 = \\)2$
    * For \(k=3\): \(V(3) = 2^{3-1} = 2^2 = \\)4$

#### 2. Calculating the Expected Value

The **expected value**, denoted \(E(X)\), of a random event is the sum of the value of each possible outcome multiplied by its probability. It represents the average outcome one would expect if the game were played an infinite number of times.

The formula for the expected value is:
$$E(X) = \sum_{k=1}^{\infty} P(k) \cdot V(k)$$

Substituting the specific formulas for the St. Petersburg game:
$$E(X) = \sum_{k=1}^{\infty} \left( \frac{1}{2} \right)^k \cdot 2^{k-1}$$

Now, let's simplify the term inside the summation:
$$\left( \frac{1}{2} \right)^k \cdot 2^{k-1} = \frac{1}{2^k} \cdot 2^{k-1} = \frac{2^{k-1}}{2^k} = \frac{1}{2}$$

The calculation simplifies dramatically. The expected value is the sum of an infinite series of the constant value \(\frac{1}{2}\):
$$E(X) = \sum_{k=1}^{\infty} \frac{1}{2} = \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \frac{1}{2} + \dots$$

This sum clearly diverges to infinity:
$$E(X) = \infty$$

This infinite expected value is the mathematical heart of the paradox. It suggests that a player should be willing to pay any finite amount to enter the game, as the average payout is theoretically infinite. However, this contradicts the rational observation that the most likely outcomes are very small payouts.

#### 3. Resolving the Paradox with Utility Theory

The paradox highlights a flaw in relying solely on expected monetary value for decision-making. The resolution, first proposed by Daniel Bernoulli, is to introduce the concept of **utility**. Utility theory posits that the "value" or "desirability" of money is not linear. Specifically, the marginal utility of money diminishes—each additional dollar is worth less to a person than the one before it.

Bernoulli proposed a **logarithmic utility function**, \(U(w) = \ln(w)\), where \(w\) is an individual's total wealth. The decision of how much to pay should be based not on the expected *monetary* gain, but on the expected *utility* gain.

Let's assume a person has an initial wealth of \(W\). If they pay an entry fee \(F\), their wealth becomes \(W-F\). The potential final wealth after playing the game is \((W - F) + V(k)\). The expected utility, \(E(U)\), is:

$$E(U) = \sum_{k=1}^{\infty} P(k) \cdot U((W - F) + V(k))$$
$$E(U) = \sum_{k=1}^{\infty} \frac{1}{2^k} \ln(W - F + 2^{k-1})$$

Unlike the sum for the expected monetary value, this series **converges** to a finite value. A rational person would be willing to pay an entry fee \(F\) such that the expected utility of playing the game is greater than or equal to the utility of not playing (and keeping their wealth \(W\)). They would pay up to the point where:

$$E(U) = U(W)$$
$$\sum_{k=1}^{\infty} \frac{1}{2^k} \ln(W - F + 2^{k-1}) = \ln(W)$$

By solving for \(F\) for a given wealth \(W\), we find a small, finite, and reasonable entry price. This demonstrates mathematically why, despite an infinite expected payout, the subjective value of the game is finite. The extreme, low-probability, high-reward outcomes are discounted by the diminishing marginal utility of wealth, aligning the mathematical model with human intuition.
