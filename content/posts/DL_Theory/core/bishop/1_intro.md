---
_build:
  render: never
  list: never

date: "2025-09-16"
title: "Intro: Conceptual Framework of Machine Learning Fundamentals"
summary: "Intro: Conceptual Framework of Machine Learning Fundamentals"
lastmod: "2025-09-16"
category: "Notes"
series: ["DL Theory"]
author: "Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

## Understanding Machine Learning Through One Simple Example

Machine learning, at its essence, is about learning patterns from data to make predictions on new, unseen examples. Rather than programming explicit rules, we let algorithms discover patterns themselves. To understand virtually every fundamental concept in machine learning, we need only examine one elegantly simple problem: fitting a curve to noisy data points sampled from a sine wave. This single example illuminates the entire conceptual landscape of the field, from basic terminology to deep principles that scale to modern neural networks.

## The Foundation: Setting Up a Learning Problem

Every machine learning problem begins with four essential components that define what we're trying to achieve.

1. First, we establish our goal—in this case, learning how an output value t depends on an input value x, so we can predict t for new values of x we haven't seen before. This ability to handle new situations is called generalization, and it's the true test of learning rather than mere memorization. 

2. Second, we need data to learn from, typically a training set of paired examples showing inputs and their corresponding outputs. In our polynomial example, we might have just ten points sampled from a sine wave with some random noise added. 

3. Third, we face constraints—our data is finite and noisy, and we must choose what type of model to use, such as polynomials of a certain order. 

4. Finally, we need a success metric, and crucially, this isn't how well we fit the training data, but how accurately we predict on completely new, unseen test data.

This setup places us firmly in the realm of supervised learning, where we learn from labeled examples showing correct input-output pairs. Within supervised learning, we're specifically doing regression because we're predicting continuous values rather than discrete categories. If we were predicting categories like "spam" or "not spam," we'd be doing classification instead. Other learning paradigms exist—unsupervised learning finds patterns without labels, like grouping customers by behavior, while self-supervised learning creates its own labels from data, like predicting the next word in a sentence.

## Models and Parameters: The Architecture of Learning

To learn from data, we need to choose a model family, also called a hypothesis class, which defines the types of functions we'll consider. Think of this as choosing the language in which we'll express our learned pattern. For our example, we might choose polynomials of order M, meaning functions of the form y = w₀ + w₁x + w₂x² + ... + wₘxᴹ. This choice immediately constrains what patterns we can possibly learn—a polynomial can't suddenly become an exponential function, no matter what data we show it.

The specific polynomial that fits our data is determined by its parameters or weights—the coefficients w₀, w₁, w₂, and so on. These parameters are what machine learning actually learns. The distinction is crucial: the model family is a decision we make before learning begins (we choose to use polynomials), while the parameters are discovered during learning (the algorithm finds the best coefficient values). This same architecture scales to neural networks, where the model family is the network architecture, and the parameters are the millions or billions of connection weights between neurons.

## The Learning Process: From Data to Predictions

Learning means finding the parameters that best fit our data, which requires defining what "best" means. We quantify this through a loss function or error function that measures how wrong our predictions are. The most common choice for regression is the sum of squared errors: we take each prediction, subtract the actual value, square the difference, and sum across all training examples. This gives us a single number that represents how badly we're doing—the lower, the better.

The process of finding parameters that minimize this loss is called optimization. For simple models like polynomials with squared error loss, we can often find the optimal parameters directly through a closed-form solution—essentially, solving an equation. For more complex models like neural networks, we use iterative methods like gradient descent, repeatedly adjusting parameters in the direction that reduces the loss. The end result is the same: parameters that make our model fit the training data well.

To communicate model performance in human-friendly terms, we often use metrics like RMSE (root mean square error), which is simply the square root of the average squared error. Unlike the raw loss value, RMSE has the same units as our predictions—if we're predicting temperatures in Celsius, RMSE tells us our typical error in degrees Celsius.

## The Central Challenge: Generalization and the Overfitting Spectrum

Here we encounter machine learning's central challenge: the goal isn't to fit training data perfectly, but to predict well on new data. This distinction creates a fundamental tension. A model that's too simple—like a straight line trying to fit a sine wave—underfits the data, failing to capture important patterns. It performs poorly on both training and test data because it lacks the capacity to represent the true relationship.

At the opposite extreme, a model that's too complex—like a 9th-order polynomial fitting 10 data points—can pass exactly through every training point, achieving zero training error. Yet this apparent perfection is misleading. The model has memorized not just the underlying pattern but also the random noise in our specific training samples. When presented with new data from the same underlying pattern, it performs terribly because it learned the wrong thing. This is overfitting, and it's perhaps the most important concept in machine learning.

The sweet spot lies between these extremes: a model complex enough to capture real patterns but not so complex that it memorizes noise. Finding this balance is the art of machine learning. Interestingly, the amount of data we have shifts this balance—with more training examples, we can afford more complex models because there's less chance of memorizing specific noise patterns when we have hundreds or thousands of examples to learn from.

## Controlling Complexity: Regularization and Data Management

Rather than constantly adjusting our model's complexity by changing its structure, we can control overfitting through regularization, also known as weight decay. The idea is beautifully simple: we add a penalty term to our loss function that discourages large parameter values. Instead of just minimizing prediction error, we minimize prediction error plus λ times the sum of squared parameters, where λ (lambda) controls the strength of this penalty.

This regularization term has a profound effect. Even with a complex model capable of wild oscillations, regularization encourages smoother, simpler functions by keeping parameters small. As we increase λ, our model becomes increasingly conservative, eventually underfitting if we push too far. The optimal λ value gives us good generalization without sacrificing too much expressiveness—another balance to strike.

To make informed decisions about model complexity and regularization strength, we need a principled way to evaluate different choices without cheating by looking at our test data. This is where data splitting becomes crucial. We divide our available data into three sets with distinct roles. The training set is where parameters are learned—we fit our model to minimize loss on this data. The validation set is where hyperparameters like model order and regularization strength are chosen—we try different settings and pick what works best on validation data. The test set is our final, unbiased estimate of real-world performance—we use it only once, after all decisions are made, to report how well our model truly generalizes.

## Model Selection: The Hierarchy of Choices

This data splitting strategy reveals a fundamental hierarchy in machine learning decisions. Parameters are the values learned automatically during training by minimizing the loss function—the polynomial coefficients in our example, or the neural network weights in deep learning. These are optimized by the learning algorithm itself. Hyperparameters, by contrast, are settings we choose before training begins—the polynomial order M, the regularization strength λ, the learning rate for gradient descent, or the number of layers in a neural network. These cannot be chosen by minimizing training loss, as that would always favor maximum complexity and zero regularization, leading to severe overfitting.

When data is scarce and we can't afford to set aside large validation sets, we turn to cross-validation. Instead of a single train-validation split, we divide our data into S folds, then train S different models, each using a different fold as validation while training on the rest. By averaging validation performance across all folds, we get a more stable estimate of how different hyperparameter choices will generalize, making better use of limited data.

## The Deep Principles: Inductive Bias and Scaling Up

Underlying all of machine learning is a philosophical principle: learning requires assumptions. Without assuming something about the patterns we're looking for, no finite amount of data could determine a unique function from infinitely many possibilities. These built-in assumptions are called inductive bias. Choosing polynomials assumes the true function is smooth and can be well-approximated by polynomial terms. Adding regularization assumes simpler explanations are more likely to be correct. Using convolutional neural networks for images assumes that visual patterns are local and translation-invariant. Every choice we make encodes beliefs about our problem.

What's remarkable is how this entire framework scales seamlessly from our simple polynomial example to modern deep learning. When we replace polynomials with neural networks, the concepts remain identical. The model family becomes the network architecture—how many layers, how they're connected. The parameters become millions or billions of weights between neurons. The loss function might change for different tasks, but we still minimize it through gradient descent, now using backpropagation to efficiently compute gradients. Regularization takes new forms like dropout or data augmentation, but serves the same purpose of preventing overfitting. The train-validation-test split remains essential, though at a larger scale.

## The Complete Picture: A Universal Recipe for Learning

The beauty of machine learning lies in how these concepts form a complete, coherent framework that applies universally. Whether you're fitting a simple polynomial or training a language model with billions of parameters, you follow the same fundamental recipe. You define your problem type—supervised or unsupervised, regression or classification. You choose a model family that embodies your assumptions about the problem. You split your data to enable unbiased evaluation. You train by minimizing loss on training data, finding parameters that capture patterns. You tune hyperparameters using validation performance, balancing complexity against generalization. You evaluate once on test data to estimate real-world performance. And if that performance is acceptable, you deploy your model to make predictions on truly new data.

This framework reveals why machine learning works and when it fails. Success requires sufficient data relative to model complexity, appropriate inductive biases for your problem, and careful attention to the balance between fitting and overfitting. The polynomial fitting example, despite its simplicity, contains every one of these challenges and concepts. Understanding this single example deeply provides the conceptual foundation for understanding all of supervised machine learning, from linear regression to transformers, from decision trees to diffusion models.

The journey from fitting polynomials to training modern AI systems isn't a leap but a natural scaling of these same principles. The vocabulary, the concerns, the solutions—they all remain remarkably consistent. Master these concepts with simple examples, and you've mastered the conceptual core of machine learning itself.
