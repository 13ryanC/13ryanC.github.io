---
date: '2025-12-07'
title: Improving Question Asking in Research
summary: How iteratively sharpening questions—illustrated by a simple coin-toss problem—leads to deeper insight, more elegant models, and better research.
description: 
lastmod: '2025-12-07'
category: Blog
series:
- Research Notes
tags:
status: draft
author: Bryan Chan
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

> I have learnt about the importance of good questions in 2021 while I was still in HKUST. The example is also deliberately taken from one of the online lectures MATH 2431 Honors Probability. Ever since that moment, re-framing problems and refining questions to be asked has been my one tool for me to really learn, gauge with the material that leads to genuine understanding, though I had been fooled by myself, illusion of expantory depth, due to cognitive ease of getting answers from ChatGPT these days, where I have stopped relying on those tools, without actually read and gauge with the material myself.

> The reason that I retrieve this from my archive (this piece is written at 24 July 2024, which the original purpose is to encourage co-founders in my first start-up to ask more questions) is because it is still valid, but also, to remind myself of this, so it would be useful to just share this draft straight away.


# Improving Question Asking

There is a problem-solving approach that I want to share and is very useful in research.

Although I learned it years ago, I recently realised that it is not widely known and very
under-appreciated.

A good researcher should be able to interrogate the problem iteratively by improving the
questions they ask. What do I mean by this?

Let’s say I ought to find the probability of a certain event, given a large sample. This can be
to find the probability of getting heads and we are given many samples of coin throwing.

One can solve the problem by calculating the ratio of the frequency of occurrence of getting
heads to the frequency of all coin throws.

This is the answer that most people will accept and stop thinking about as a result of getting
there.

However, is this insight useful, I guess the better researchers would doubt that as that insight
does not yield any new value?

So what does the researcher can do?

Well, one way they do this is to improve on the question to elicit a different response/insight
into the understanding of the problem. What do I mean by this?

One way is via splitting, like
1. Ask what is the probability of getting heads given the last throw is a tail.
2. Ask what is the probability of getting heads given the last throw is ahead.

Thus ask whether the events of getting a head and a tail are independent events or dependent.

There is another way that is even more nuanced but I discovered this approach by observing top-notch, world-class researchers, as it leads to very deep insight into the problem.

In this case, the researcher might be interested in: What does this tell me about the coin itself, is it a fair coin? What information do you need to determine that?

Okay now, let’s say you find some information. Let’s say you know the weight distribution
or even magnetic properties of the coin, and by brute force, like creating a mathematical
model to capture all the nuances in coin-throwing, this includes calculations of gravity, coin
shape, the throwing speeds, and so on, you can eventually get to building a mathematical
model that describes whether makes the coin fair given all many different parameters.





There is indeed a paper using this approach on dice throwing, where they indeed model the
shape of the dice, how it touches the ground surface and thus model how it moves on the
ground, etc, then come up with a math model to calculate the probability of the dice throw.
(LOL, I remember reading that years ago by some group of Beijing researchers but I forget
where I saved that paper)

But is this a good way? (I doubt so)

Well, the world-class researcher may ask, is that information necessary to determine whether or not that is a fair coin?

In this case, the researcher is not looking for that way of solving the problem as that is a
trivial approach and low-hanging fruit that surely any mediocre researcher can do.

Well, the researcher is interested in looking for a method that can solve the problem with the
least amount of information and clutter, which is an elegant way of solving problems (at least
in mathematics).

So instead the researcher can redefine the problem, by questioning the nature of a fair coin
itself.

For example,
He can define a set of functions in which those functions outputs are the probabilities of coin
throwing itself, which by inserting a variable (i.e., the #no. of the throw), can output
the probability of getting heads in that (#no. of throw).

By knowing what a fair coin is (heads and tails must be equal) and an unfair coin (either all
heads or tails). Then there can be a distribution created that captures the probability of these
functions happening, usually one will start with a normal distribution. (but to alter it usually
involves the use of statistics, which I am not going to discuss here, as it involves sampling).
In other words, he created a way (a distribution) to quantify the probability of whether the
coin is fair or not.

Then simply by the given results initially, the given samples of coin throwing, he can
quantify whether the coin is fair or not based on this distribution, with the assumptions laid
down given his approach is rigorous enough.

The problem-solving strategy I put here only contains examples that are pertinent
to mathematics as my interests lie in mathematics.

I am not entirely sure, whether improving the questions you are asking, is a well-defined
practice in other fields of research but it is a very well-defined practice in mathematics. 

And I do think it does extend to other fields, if not already adopted.
Hope this is insightful.
