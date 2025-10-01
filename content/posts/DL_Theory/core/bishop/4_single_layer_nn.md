---
_build:
  render: never
  list: never

date: "2025-09-16"
title: "Single Layer Neural Network"
summary: "Single Layer Neural Network"
lastmod: "2025-09-16"
category: "Notes"
series: ["DL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# The Single-Layer Neural Network: One Architecture, Two Worlds

## The Universal Blueprint

At its heart, a single-layer neural network represents one of the most elegant ideas in machine learning: a simple computational pipeline that can adapt to radically different tasks. Picture a flow of information that begins with raw input data, perhaps the pixels of an image or measurements from a sensor. This data undergoes a transformation into what we call features or basis functions—different mathematical "lenses" through which we view the original information. These features might capture simple patterns like edges in an image, or more abstract relationships like polynomial terms that reveal curvature in data trends.

The magic happens when we assign learnable weights to each of these features, essentially asking the question: "How important is each perspective for making our prediction?" These weights, along with a bias term that shifts our entire prediction up or down, form the trainable parameters of our network. The network combines all weighted features through a simple sum, creating what we might think of as a "raw score" or pre-activation value. This universal blueprint—input transformed to features, weighted, and summed—remains identical whether we're predicting house prices or classifying handwritten digits. Yet at this crucial juncture, where we must transform this raw score into a final output, the paths diverge dramatically.

## The Fundamental Fork: Continuous Versus Discrete

The nature of what we're trying to predict fundamentally reshapes everything that follows. When we aim to predict continuous values—tomorrow's temperature, a stock price, or the speed of a vehicle—we're engaging in regression. Here, the weighted sum can serve directly as our prediction, passing through what mathematicians call an identity activation function, which is simply a fancy way of saying "no change at all." The output remains a real number that can take any value along a continuous spectrum. The model learns to position its predictions as close as possible to the true values, much like stretching a flexible sheet to pass through a cloud of data points in space.

Classification presents an entirely different challenge. When predicting discrete categories—whether an email is spam or legitimate, which digit appears in an image, or what species a flower belongs to—we need our raw scores to become probabilities. This transformation requires special activation functions: the sigmoid function for binary choices, which squashes any input into a value between 0 and 1, or the softmax function for multiple categories, which ensures all probabilities sum to exactly 1 while maintaining the relative ordering of the raw scores. These functions create a kind of "competition" among the possible outcomes, where increasing confidence in one category necessarily decreases confidence in others.

## The Mathematical Ecosystems

This fundamental divergence between continuous and discrete predictions creates two distinct mathematical ecosystems, each with its own natural laws and optimal strategies. In the regression world, we typically assume that our predictions should cluster around true values according to a Gaussian or bell-curve distribution. This assumption leads naturally to minimizing the sum of squared errors—essentially measuring how far off our predictions are and penalizing larger errors more heavily. The beautiful consequence of this choice is that many regression problems admit closed-form solutions, meaning we can solve for the optimal weights in one mathematical step, like solving a system of equations. The geometry here is intuitive: we're finding the best-fitting surface through our data points, mathematically equivalent to projecting our target values onto the subspace spanned by our features.

Classification inhabits a different mathematical universe. Here, we model the probability of belonging to each class using Bernoulli distributions for binary outcomes (like coin flips) or categorical distributions for multiple classes (like rolling a die). The natural loss function becomes cross-entropy, which measures how "surprised" we are by the true outcomes given our predicted probabilities. If we predict 90% confidence that an image shows a seven, and it actually is a seven, our surprise is low; if it turns out to be a three, our surprise is high. Unlike regression, classification rarely offers closed-form solutions. Instead, we must use iterative optimization methods, gradually adjusting weights to improve predictions over many passes through the data. Geometrically, classification carves up the input space with decision boundaries—hyperplanes that separate different classes like fences dividing pastures.

## The Ripple Effects on Decision Making

The way we make final decisions with our trained models further illustrates the philosophical gap between regression and classification. In regression, decision-making is straightforward: we typically use the predicted value directly. The theory tells us that to minimize expected squared error, we should predict the conditional mean—the average value we'd expect given the input. This principle extends naturally: if we cared about absolute rather than squared error, we'd predict the median; if we wanted the most likely value, we'd predict the mode.

Classification decisions involve richer considerations. Beyond simply choosing the class with highest probability, we must often account for the varying costs of different mistakes. In medical diagnosis, failing to detect a disease (false negative) might be far more costly than unnecessary further testing (false positive). This leads to sophisticated decision frameworks involving loss matrices that encode the cost of every possible confusion between classes. Classification also introduces the option to refuse making a decision when uncertainty is high—a reject option that might trigger human review when the model's confidence falls below a threshold. These capabilities make classification models particularly suitable for high-stakes decisions where understanding and managing uncertainty is crucial.

## Learning from MNIST: A Tale of Two Approaches

The famous MNIST dataset of handwritten digits beautifully illustrates how the same data can be approached through either lens. In its traditional formulation as a classification problem, we flatten each 28×28 pixel image into 784 input features. The network learns weights that transform these pixel intensities into ten scores, one for each digit from 0 to 9. The softmax activation converts these scores into probabilities that sum to 1, and we predict the digit with highest probability. Training minimizes cross-entropy loss over thousands of examples, gradually learning which pixel patterns correspond to which digits. The trained model creates complex decision boundaries in the 784-dimensional space, carving out regions that correspond to different digits.

We could, however, reimagine MNIST as a regression problem. Perhaps we want to predict the angle of rotation of a digit, or the pressure with which it was written, or even a continuous "digit-ness" score that measures how clearly the image represents a number versus random noise. Now the same 784 pixels feed into weights that produce a single continuous output through an identity activation. The loss becomes squared error, the geometry becomes projection onto a subspace, and the entire mathematical machinery shifts to the regression framework. This flexibility reveals a profound truth: the choice between regression and classification isn't inherent to the data itself but depends on the question we're asking.

## Navigating the Pitfalls

Each path comes with its own characteristic challenges and failure modes. Regression models can suffer from overfitting when they have too many parameters relative to training examples, essentially memorizing the training data rather than learning generalizable patterns. The solution involves regularization—adding a penalty term that discourages large weights and promotes smoother, simpler models. Regression can also face numerical instabilities when features are highly correlated or span vastly different scales, requiring techniques like standardization or singular value decomposition to maintain computational stability.

Classification brings different challenges. A common mistake is using squared error loss with categorical targets, which seems intuitive but produces poor probability estimates and makes the model overly sensitive to outliers. The proper choice of cross-entropy loss emerges naturally from the probabilistic framework and provides cleaner gradients for learning. Perhaps surprisingly, classification models can catastrophically fail when classes are perfectly separable in the training data—the weights grow without bound as the model tries to drive probabilities to absolute certainty. Again, regularization provides the remedy. Classification must also grapple with class imbalance, where rare events (like fraudulent transactions among millions of legitimate ones) require special techniques like adjusted thresholds or weighted losses to achieve useful performance.

## The Deeper Unity

Despite their differences, regression and classification share a deeper unity in the single-layer neural network framework. Both learn through the same fundamental mechanism: adjusting weights to minimize prediction error on training data. Both use the same gradient-based optimization techniques, with gradients that remarkably take the same form—the prediction error multiplied by the input features—thanks to the careful pairing of activation functions with their natural loss functions. Both benefit from the same regularization strategies to prevent overfitting and the same data preprocessing techniques to improve conditioning.

This unified framework extends naturally to deeper networks. When we stack multiple layers, the final layer typically remains either a regression head (identity activation with squared loss) or a classification head (softmax with cross-entropy), while the earlier layers learn increasingly abstract features. The single-layer network thus serves as both a practical tool in its own right and a fundamental building block for more complex architectures. Understanding when to frame a problem as regression versus classification, and how that choice cascades through the entire modeling pipeline, remains one of the most crucial decisions in applied machine learning.

The elegance of the single-layer neural network lies not in its complexity but in its simplicity—a single architectural pattern that, through a careful choice of activation function and loss, adapts seamlessly to the fundamental dichotomy between continuous and discrete prediction. Master this framework, and you hold the key to understanding not just these two specific models but the entire landscape of supervised learning that builds upon them.
