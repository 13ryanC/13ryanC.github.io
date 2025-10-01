---
_build:
  render: never
  list: never

date: "2025-06-26"
title: "Chapter 6 TD Learning"
summary: "errata"
category: "Reference"
series: ["Sutton & Barto 2018"]
author: "Author: Bryan Chan"
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

# Chapter 6 Temporal-Difference Learning

If one had to identify one idea as central and novel to reinforcement learning, it would undoubtedly be temporal- difference (TD) learning. TD learning is a combination of Monte Carlo ideas and dynamic programming (DP) ideas. Like Monte Carlo methods, TD methods can learn directly from raw experience without a model of the environment's dynamics. Like DP, TD methods update estimates based in part on other learned estimates, without waiting for a final outcome (they bootstrap). The relationship between TD, DP, and Monte Carlo methods is a recurring theme in the theory of reinforcement learning; this chapter is the beginning of our exploration of it. Before we are done, we will see that these ideas and methods blend into each other and can be combined in many ways. In particular, in Chapter 7 we introduce  \(n\) - step algorithms, which provide a bridge from TD to Monte Carlo methods, and in Chapter 12 we introduce the TD( \(\lambda\) ) algorithm, which seamlessly unifies them.As usual, we start by focusing on the policy evaluation or prediction problem, the problem of estimating the value function  \(v_{\pi}\)  for a given policy  \(\pi\) . For the control problem (finding an optimal policy), DP, TD, and Monte Carlo methods all use some variation of generalized policy iteration (GPI). The differences in the methods are primarily differences in their approaches to the prediction problem.

As usual, we start by focusing on the policy evaluation or prediction problem, the problem of estimating the value function  \(v_{\pi}\)  for a given policy  \(\pi\)  . For the control problem (finding an optimal policy), DP, TD, and Monte Carlo methods all use some variation of generalized policy iteration (GPI). The differences in the methods are primarily differences in their approaches to the prediction problem.

# 6.1 TD Prediction

Both TD and Monte Carlo methods use experience to solve the prediction problem. Given some experience following a policy  \(\pi\) , both methods update their estimate  \(V\)  of  \(v_{\pi}\)  for the nonterminal states  \(S_{t}\)  occurring in that experience. Roughly speaking, Monte Carlo methods wait until the return following the visit is known, then use that return as a target for  \(V(S_{t})\) . A simple every- visit Monte Carlo method suitable for nonstationary environments is\[ V(S_{t}) \leftarrow V(S_{t}) + \alpha \Big[ G_{t} - V(S_{t}) \Big], \]

$$
V(S_{t})\leftarrow V(S_{t}) + \alpha \Big[G_{t} - V(S_{t})\Big], \tag{6.1}
$$

where  \(G_{t}\)  is the actual return following time  \(t\)  , and  \(\alpha\)  is a constant step- size parameter (c.f., Equation 2.4). Let us call this method constant-  \(\alpha\)  MC. Whereas Monte Carlo methods must wait until the end of the episode to determine the increment to  \(V(S_{t})\)  (only then is  \(G_{t}\)  known), TD methods need to wait only until the next time step. At time  \(t + 1\)  they immediately form a target and make a useful update using the observed reward  \(R_{t + 1}\)  and the estimate  \(V(S_{t + 1})\)  . The simplest TD method makes the update

$$
V(S_{t})\leftarrow V(S_{t}) + \alpha \Big[R_{t + 1} + \gamma V(S_{t + 1}) - V(S_{t})\Big] \tag{6.2}
$$

immediately on transition to  \(S_{t + 1}\)  and receiving  \(R_{t + 1}\)  . In effect, the target for the Monte Carlo update is  \(G_{t}\)  , whereas the target for the TD update is  \(R_{t + 1} + \gamma V(S_{t + 1})\)  . This TD method is called  \(T D(0)\)  , or one- step  \(T D\)  , because it is a special case of the  \(\mathrm{TD}(\lambda)\)  and  \(n\)  - step TD methods developed in Chapter 12 and Chapter 7. The box below specifies  \(\mathrm{TD}(0)\)  completely in procedural form.

# Tabular TD(0) for estimating  \(v_{\pi}\)

Input: the policy  \(\pi\)  to be evaluated Algorithm parameter: step size  \(\alpha \in (0,1]\)  Initialize  \(V(s)\)  , for all  \(s\in \mathbb{S}^{+}\)  , arbitrarily except that  \(V(t e r m i n a l) = 0\)  Loop for each episode: Initialize  \(S\)  Loop for each step of episode:  \(A\gets\)  action given by  \(\pi\)  for  \(S\)  Take action  \(A\)  , observe  \(R\) \(S^{\prime}\) \(V(S)\leftarrow V(S) + \alpha \left[R + \gamma V(S^{\prime}) - V(S)\right]\) \(S\gets S^{\prime}\)  until  \(S\)  is terminal

Because TD(0) bases its update in part on an existing estimate, we say that it is a bootstrapping method, like DP. We know from Chapter 3 that

$$
\begin{array}{r l} & {v_{\pi}(s)\doteq \mathbb{E}_{\pi}[G_{t}\mid S_{t} = s]}\\ & {\qquad = \mathbb{E}_{\pi}[R_{t + 1} + \gamma G_{t + 1}\mid S_{t} = s]}\\ & {\qquad = \mathbb{E}_{\pi}[R_{t + 1} + \gamma v_{\pi}(S_{t + 1})\mid S_{t} = s].} \end{array} \tag{6.3}
$$

(from (3.9))

Roughly speaking, Monte Carlo methods use an estimate of (6.3) as a target, whereas DP methods use an estimate of (6.4) as a target. The Monte Carlo target is an estimate because the expected value in (6.3) is not known; a sample return is used in place of the real expected return. The DP target is an estimate not because of the expected values, which are assumed to be completely provided by a model of the environment, but because  \(v_{\pi}(S_{t + 1})\)  is not known and the current estimate,  \(V(S_{t + 1})\) , is used instead. The TD target is an estimate for both reasons: it samples the expected values in (6.4) and it uses the current estimate  \(V\)  instead of the true  \(v_{\pi}\) . Thus, TD methods combine the sampling of

Monte Carlo with the bootstrapping of DP. As we shall see, with care and imagination this can take us a long way toward obtaining the advantages of both Monte Carlo and DP methods.

Shown to the right is the backup diagram for tabular TD(0). The value estimate for the state node at the top of the backup diagram is updated on the basis of the one sample transition from it to the immediately following state. We refer to TD and Monte Carlo updates as sample updates because they involve looking ahead to a sample successor state (or state- action pair), using the value of the successor and the reward along the way to compute a backed- up value, and then updating the value of the original state (or state- action pair) accordingly. Sample updates differ from the expected updates of DP methods in that they are based on a single sample successor rather than on a complete distribution of all possible successors.

of DP methods in that they are based on a single sample successor rather than on a complete distribution of all possible successors.

Finally, note that the quantity in brackets in the TD(0) update is a sort of error, measuring the difference between the estimated value of  \(S_{t}\)  and the better estimate  \(R_{t + 1} + \gamma V(S_{t + 1})\) . This quantity, called the  \(TD\)  error, arises in various forms throughout reinforcement learning:

$$
\delta_{t} \doteq R_{t + 1} + \gamma V(S_{t + 1}) - V(S_{t}). \tag{6.5}
$$

Notice that the TD error at each time is the error in the estimate made at that time. Because the TD error depends on the next state and next reward, it is not actually available until one time step later. That is,  \(\delta_{t}\)  is the error in  \(V(S_{t})\) , available at time  \(t + 1\) . Also note that if the array  \(V\)  does not change during the episode (as it does not in Monte Carlo methods), then the Monte Carlo error can be written as a sum of TD errors:

$$
\begin{array}{r l} & {G_{t} - V(S_{t}) = R_{t + 1} + \gamma G_{t + 1} - V(S_{t}) + \gamma V(S_{t + 1}) - \gamma V(S_{t + 1})}\\ & {\qquad = \delta_{t} + \gamma \big(G_{t + 1} - V(S_{t + 1})\big)}\\ & {\qquad = \delta_{t} + \gamma \delta_{t + 1} + \gamma^{2}\big(G_{t + 2} - V(S_{t + 2})\big)}\\ & {\qquad = \delta_{t} + \gamma \delta_{t + 1} + \gamma^{2}\delta_{t + 2} + \dots +\gamma^{T - t - 1}\delta_{T - 1} + \gamma^{T - t}\big(G_{T} - V(S_{T})\big)}\\ & {\qquad = \delta_{t} + \gamma \delta_{t + 1} + \gamma^{2}\delta_{t + 2} + \dots +\gamma^{T - t - 1}\delta_{T - 1} + \gamma^{T - t}\big(0 - 0\big)}\\ & {\qquad = \sum_{k = t}^{T - t}\gamma^{k - t}\delta_{k}.} \end{array} \tag{6.6}
$$

This identity is not exact if  \(V\)  is updated during the episode (as it is in TD(0)), but if the step size is small then it may still hold approximately. Generalizations of this identity play an important role in the theory and algorithms of temporal- difference learning.

Exercise 6.1 If  \(V\)  changes during the episode, then (6.6) only holds approximately; what would the difference be between the two sides? Let  \(V_{t}\)  denote the array of state values used at time  \(t\)  in the TD error (6.5) and in the TD update (6.2). Redo the derivation above to determine the additional amount that must be added to the sum of TD errors in order to equal the Monte Carlo error.

Example 6.1: Driving Home Each day as you drive home from work, you try to predict how long it will take to get home. When you leave your office, you note the time, the day of week, the weather, and anything else that might be relevant. Say on this Friday you are leaving at exactly 6 o'clock, and you estimate that it will take 30 minutes to get home. As you reach your car it is 6:05, and you notice it is starting to rain. Traffic is often slower in the rain, so you reestimate that it will take 35 minutes from then, or a total of 40 minutes. Fifteen minutes later you have completed the highway portion of your journey in good time. As you exit onto a secondary road you cut your estimate of total travel time to 35 minutes. Unfortunately, at this point you get stuck behind a slow truck, and the road is too narrow to pass. You end up having to follow the truck until you turn onto the side street where you live at 6:40. Three minutes later you are home. The sequence of states, times, and predictions is thus as follows:

<table><tr><td>State</td><td>Elapsed Time 
(minutes)</td><td>Predicted 
Time to Go</td><td>Predicted 
Total Time</td></tr><tr><td>leaving office, friday at 6</td><td>0</td><td>30</td><td>30</td></tr><tr><td>reach car, raining</td><td>5</td><td>35</td><td>40</td></tr><tr><td>exiting highway</td><td>20</td><td>15</td><td>35</td></tr><tr><td>2ndary road, behind truck</td><td>30</td><td>10</td><td>40</td></tr><tr><td>entering home street</td><td>40</td><td>3</td><td>43</td></tr><tr><td>arrive home</td><td>43</td><td>0</td><td>43</td></tr></table>

The rewards in this example are the elapsed times on each leg of the journey.1 We are not discounting (  \(\gamma = 1\)  ), and thus the return for each state is the actual time to go from that state. The value of each state is the expected time to go. The second column of numbers gives the current estimated value for each state encountered.

A simple way to view the operation of Monte Carlo methods is to plot the predicted total time (the last column) over the sequence, as in Figure 6.1 (left). The red arrows show the changes in predictions recommended by the constant-  \(\alpha\)  MC method (6.1), for  \(\alpha = 1\)  . These are exactly the errors between the estimated value (predicted time to go) in each state and the actual return (actual time to go). For example, when you exited the highway you thought it would take only 15 minutes more to get home, but in fact it took 23 minutes. Equation 6.1 applies at this point and determines an increment in the estimate of time to go after exiting the highway. The error,  \(G_{t} - V(S_{t})\)  , at this time is eight minutes. Suppose the step- size parameter,  \(\alpha\)  , is  \(1 / 2\)  . Then the predicted time to go after exiting the highway would be revised upward by four minutes as a result of this experience. This is probably too large a change in this case; the truck was probably just an unlucky break. In any event, the change can only be made off- line, that is, after you have reached home. Only at this point do you know any of the actual returns.

Is it necessary to wait until the final outcome is known before learning can begin? Suppose on another day you again estimate when leaving your office that it will take 30 minutes to drive home, but then you become stuck in a massive traffic jam. Twenty- five minutes after leaving the office you are still bumper- to- bumper on the highway. You now

![](images/6633f1a3b7d7394f3467e8c2cf8bf2e77566e0551c95ea0eeeb1abddf8726c54.jpg)  
Figure 6.1: Changes recommended in the driving home example by Monte Carlo methods (left) and TD methods (right).

estimate that it will take another 25 minutes to get home, for a total of 50 minutes. As you wait in traffic, you already know that your initial estimate of 30 minutes was too optimistic. Must you wait until you get home before increasing your estimate for the initial state? According to the Monte Carlo approach you must, because you don't yet know the true return.

According to a TD approach, on the other hand, you would learn immediately, shifting your initial estimate from 30 minutes toward 50. In fact, each estimate would be shifted toward the estimate that immediately follows it. Returning to our first day of driving, Figure 6.1 (right) shows the changes in the predictions recommended by the TD rule (6.2) (these are the changes made by the rule if  \(\alpha = 1\) ). Each error is proportional to the change over time of the prediction, that is, to the temporal differences in predictions.

Besides giving you something to do while waiting in traffic, there are several computational reasons why it is advantageous to learn based on your current predictions rather than waiting until termination when you know the actual return. We briefly discuss some of these in the next section.

Exercise 6.2 This is an exercise to help develop your intuition about why TD methods are often more efficient than Monte Carlo methods. Consider the driving home example and how it is addressed by TD and Monte Carlo methods. Can you imagine a scenario in which a TD update would be better on average than a Monte Carlo update? Give an example scenario—a description of past experience and a current state—in which you would expect the TD update to be better. Here's a hint: Suppose you have lots of experience driving home from work. Then you move to a new building and a new parking lot (but you still enter the highway at the same place). Now you are starting to learn predictions for the new building. Can you see why TD updates are likely to be much better, at least initially, in this case? Might the same sort of thing happen in the original scenario?

# 6.2 Advantages of TD Prediction Methods

TD methods update their estimates based in part on other estimates. They learn a guess from a guess- they bootstrap. Is this a good thing to do? What advantages do TD methods have over Monte Carlo and DP methods? Developing and answering such questions will take the rest of this book and more. In this section we briefly anticipate some of the answers.

Obviously, TD methods have an advantage over DP methods in that they do not require a model of the environment, of its reward and next- state probability distributions.

The next most obvious advantage of TD methods over Monte Carlo methods is that they are naturally implemented in an online, fully incremental fashion. With Monte Carlo methods one must wait until the end of an episode, because only then is the return known, whereas with TD methods one need wait only one time step. Surprisingly often this turns out to be a critical consideration. Some applications have very long episodes, so that delaying all learning until the end of the episode is too slow. Other applications are continuing tasks and have no episodes at all. Finally, as we noted in the previous chapter, some Monte Carlo methods must ignore or discount episodes on which experimental actions are taken, which can greatly slow learning. TD methods are much less susceptible to these problems because they learn from each transition regardless of what subsequent actions are taken.

But are TD methods sound? Certainly it is convenient to learn one guess from the next, without waiting for an actual outcome, but can we still guarantee convergence to the correct answer? Happily, the answer is yes. For any fixed policy  \(\pi\) \(\mathrm{TD}(0)\)  has been proved to converge to  \(v_{\pi}\)  , in the mean for a constant step- size parameter if it is sufficiently small, and with probability 1 if the step- size parameter decreases according to the usual stochastic approximation conditions (2.7). Most convergence proofs apply only to the table- based case of the algorithm presented above (6.2), but some also apply to the case of general linear function approximation. These results are discussed in a more general setting in Section 9.4.

If both TD and Monte Carlo methods converge asymptotically to the correct predictions, then a natural next question is "Which gets there first?" In other words, which method learns faster? Which makes the more efficient use of limited data? At the current time this is an open question in the sense that no one has been able to prove mathematically that one method converges faster than the other. In fact, it is not even clear what is the most appropriate formal way to phrase this question! In practice, however, TD methods have usually been found to converge faster than constant-  \(\alpha\)  MC methods on stochastic tasks, as illustrated in Example 6.2.

# Example 6.2 Random Walk

In this example we empirically compare the prediction abilities of TD(0) and constant-  \(\alpha\)  MC when applied to the following Markov reward process:

![](images/8f1078b1f47ff87025bcdb6163a904952cc76c3812d7d1852d36d2af3b823159.jpg)

A Markov reward process, or MRP, is a Markov decision process without actions. We will often use MRPs when focusing on the prediction problem, in which there is no need to distinguish the dynamics due to the environment from those due to the agent. In this MRP, all episodes start in the center state, C, then proceed either left or right by one state on each step, with equal probability. Episodes terminate either on the extreme left or the extreme right. When an episode terminates on the right, a reward of  \(+1\)  occurs; all other rewards are zero. For example, a typical episode might consist of the following state- and- reward sequence: C, 0, B, 0, C, 0, D, 0, E, 1. Because this task is undiscounted, the true value of each state is the probability of terminating on the right if starting from that state. Thus, the true value of the center state is  \(\nu_{\pi}(\mathsf{C}) = 0.5\)  . The true values of all the states, A through E, are  \(\frac{1}{6},\frac{2}{6},\frac{3}{6},\frac{4}{6}\)  , and  \(\frac{5}{6}\)

![](images/b1f8461270e8931abe8efc8bf4feafdde739dd77f517765a18d5eb1511280fa5.jpg)

The left graph above shows the values learned after various numbers of episodes on a single run of TD(0). The estimates after 100 episodes are about as close as they ever come to the true values—with a constant step- size parameter ( \(\alpha = 0.1\)  in this example), the values fluctuate indefinitely in response to the outcomes of the most recent episodes. The right graph shows learning curves for the two methods for various values of  \(\alpha\) . The performance measure shown is the root mean square (RMS) error between the value function learned and the true value function, averaged over the five states, then averaged over 100 runs. In all cases the approximate value function was initialized to the intermediate value  \(V(s) = 0.5\) , for all  \(s\) . The TD method was consistently better than the MC method on this task.

Exercise 6.3 From the results shown in the left graph of the random walk example it appears that the first episode results in a change in only  \(V(\mathsf{A})\) . What does this tell you about what happened on the first episode? Why was only the estimate for this one state changed? By exactly how much was it changed?  \(\square\)

Exercise 6.4 The specific results shown in the right graph of the random walk example are dependent on the value of the step- size parameter,  \(\alpha\) . Do you think the conclusions about which algorithm is better would be affected if a wider range of  \(\alpha\)  values were used? Is there a different, fixed value of  \(\alpha\)  at which either algorithm would have performed significantly better than shown? Why or why not?  \(\square\)

\*Exercise 6.5 In the right graph of the random walk example, the RMS error of the TD method seems to go down and then up again, particularly at high  \(\alpha\)  's. What could have caused this? Do you think this always occurs, or might it be a function of how the approximate value function was initialized?

Exercise 6.6 In Example 6.2 we stated that the true values for the random walk example are  \(\frac{1}{6}, \frac{2}{6}, \frac{3}{6}, \frac{4}{6}\) , and  \(\frac{5}{6}\) , for states A through E. Describe at least two different ways that these could have been computed. Which would you guess we actually used? Why?  \(\square\)

# 6.3 Optimality of TD(0)

Suppose there is available only a finite amount of experience, say 10 episodes or 100 time steps. In this case, a common approach with incremental learning methods is to present the experience repeatedly until the method converges upon an answer. Given an approximate value function,  \(V\) , the increments specified by (6.1) or (6.2) are computed for every time step  \(t\)  at which a nonterminal state is visited, but the value function is changed only once, by the sum of all the increments. Then all the available experience is processed again with the new value function to produce a new overall increment, and so on, until the value function converges. We call this batch updating because updates are made only after processing each complete batch of training data.

Under batch updating, TD(0) converges deterministically to a single answer independent of the step- size parameter,  \(\alpha\) , as long as  \(\alpha\)  is chosen to be sufficiently small. The constant-  \(\alpha\)  MC method also converges deterministically under the same conditions, but to a different answer. Understanding these two answers will help us understand the difference between the two methods. Under normal updating the methods do not move all the way to their respective batch answers, but in some sense they take steps in these directions. Before trying to understand the two answers in general, for all possible tasks, we first look at a few examples.

Example 6.3: Random walk under batch updating Batch- updating versions of TD(0) and constant-  \(\alpha\)  MC were applied as follows to the random walk prediction example (Example 6.2). After each new episode, all episodes seen so far were treated as a batch. They were repeatedly presented to the algorithm, either TD(0) or constant-  \(\alpha\)  MC, with  \(\alpha\)  sufficiently small that the value function converged. The resulting value function was then compared with  \(v_{\pi}\) , and the average root mean square error across the five states (and across 100 independent repetitions of the whole experiment) was plotted to obtain

the learning curves shown in Figure 6.2. Note that the batch TD method was consistently better than the batch Monte Carlo method.

Under batch training, constant-  \(\alpha\)  MC converges to values,  \(V(s)\)  , that are sample averages of the actual returns experienced after visiting each state  \(s\)  . These are optimal estimates in the sense that they minimize the mean square error from the actual returns in the training set. In this sense it is surprising that the batch TD method was able to perform better according to the root mean square error measure shown in the figure to the right. How is it that batch TD was able to perform better than this optimal method? The answer is that the Monte Carlo method is optimal only in a limited way, and that TD is optimal in a way that is more relevant to predicting returns.

![](images/614cf7c649ed44e266645b78f0132c7546adf3a00b28cc27ffdaa00b58d0fe8f.jpg)  
Figure 6.2: Performance of TD(0) and constant-  \(\alpha\)  MC under batch training on the random walk task.

Example 6.4: You are the Predictor Place yourself now in the role of the predictor of returns for an unknown Markov reward process. Suppose you observe the following eight episodes:

A,0,B,0 B,1 B,1 B,1 B,1 B,0

This means that the first episode started in state A, transitioned to B with a reward of  \(\mathrm{0}\)  , and then terminated from B with a reward of 0. The other seven episodes were even shorter, starting from B and terminating immediately. Given this batch of data, what would you say are the optimal predictions, the best values for the estimates  \(V(\mathsf{A})\)  and  \(V(\mathsf{B})\)  ? Everyone would probably agree that the optimal value for  \(V(\mathsf{B})\)  is  \(\frac{3}{4}\)  , because six out of the eight times in state B the process terminated immediately with a return of 1, and the other two times in B the process terminated immediately with a return of 0.

But what is the optimal value for the estimate  \(V(\mathsf{A})\)  given this data? Here there are

two reasonable answers. One is to observe that  \(100\%\)  of the times the process was in state A it traversed immediately to B (with a reward of 0); and because we have already decided that B has value  \(\frac{3}{4}\)  , therefore A must have value  \(\frac{3}{4}\)  as well. One way of viewing this answer is that it is based on first modeling the Markov process, in this case as shown to the right, and then computing the correct estimates given the model, which indeed in this case gives  \(V(\mathsf{A}) = \frac{3}{4}\)  . This is also the answer that batch TD(0) gives.

![](images/9644d15f45577e7b15cf9cea1019a110d773bcc08d2f3bf4cc0c72fe40b11984.jpg)

The other reasonable answer is simply to observe that we have seen A once and the return that followed it was 0; we therefore estimate  \(V(\mathsf{A})\)  as 0. This is the answer that batch Monte Carlo methods give. Notice that it is also the answer that gives minimum squared error on the training data. In fact, it gives zero error on the data. But still we expect the first answer to be better. If the process is Markov, we expect that the first answer will produce lower error on future data, even though the Monte Carlo answer is better on the existing data.

Example 6.4 illustrates a general difference between the estimates found by batch  \(\mathrm{TD}(0)\)  and batch Monte Carlo methods. Batch Monte Carlo methods always find the estimates that minimize mean square error on the training set, whereas batch  \(\mathrm{TD}(0)\)  always finds the estimates that would be exactly correct for the maximum- likelihood model of the Markov process. In general, the maximum- likelihood estimate of a parameter is the parameter value whose probability of generating the data is greatest. In this case, the maximum- likelihood estimate is the model of the Markov process formed in the obvious way from the observed episodes: the estimated transition probability from  \(i\)  to  \(j\)  is the fraction of observed transitions from  \(i\)  that went to  \(j\) , and the associated expected reward is the average of the rewards observed on those transitions. Given this model, we can compute the estimate of the value function that would be exactly correct if the model were exactly correct. This is called the certainty- equivalence estimate because it is equivalent to assuming that the estimate of the underlying process was known with certainty rather than being approximated. In general, batch  \(\mathrm{TD}(0)\)  converges to the certainty- equivalence estimate.

This helps explain why TD methods converge more quickly than Monte Carlo methods. In batch form,  \(\mathrm{TD}(0)\)  is faster than Monte Carlo methods because it computes the true certainty- equivalence estimate. This explains the advantage of  \(\mathrm{TD}(0)\)  shown in the batch results on the random walk task (Figure 6.2). The relationship to the certainty- equivalence estimate may also explain in part the speed advantage of nonbatch  \(\mathrm{TD}(0)\)  (e.g., Example 6.2, page 125, right graph). Although the nonbatch methods do not achieve either the certainty- equivalence or the minimum squared error estimates, they can be understood as moving roughly in these directions. Nonbatch  \(\mathrm{TD}(0)\)  may be faster than constant-  \(\alpha\)  MC because it is moving toward a better estimate, even though it is not getting all the way there. At the current time nothing more definite can be said about the relative efficiency of online TD and Monte Carlo methods.

Finally, it is worth noting that although the certainty- equivalence estimate is in some sense an optimal solution, it is almost never feasible to compute it directly. If  \(n = |\mathcal{S}|\)  is the number of states, then just forming the maximum- likelihood estimate of the process may require on the order of  \(n^2\)  memory, and computing the corresponding value function requires on the order of  \(n^3\)  computational steps if done conventionally. In these terms it is indeed striking that TD methods can approximate the same solution using memory no more than order  \(n\)  and repeated computations over the training set. On tasks with large state spaces, TD methods may be the only feasible way of approximating the certainty- equivalence solution.

*Exercise 6.7 Design an off- policy version of the  \(\mathrm{TD}(0)\)  update that can be used with arbitrary target policy  \(\pi\)  and covering behavior policy  \(b\) , using at each step  \(t\)  the importance sampling ratio  \(\rho_{t:t}\)  (5.3).

# 6.4 Sarsa: On-policy TD Control

We turn now to the use of TD prediction methods for the control problem. As usual, we follow the pattern of generalized policy iteration (GPI), only this time using TD methods for the evaluation or prediction part. As with Monte Carlo methods, we face the need to trade off exploration and exploitation, and again approaches fall into two main classes: on- policy and off- policy. In this section we present an on- policy TD control method.

The first step is to learn an action- value function rather than a state- value function. In particular, for an on- policy method we must estimate  \(q_{\pi}(s,a)\)  for the current behavior policy  \(\pi\)  and for all states  \(s\)  and actions  \(a\)  . This can be done using essentially the same TD method described above for learning  \(v_{\pi}\)  . Recall that an episode consists of an alternating sequence of states and state- action pairs:

$$
\cdots -\overbrace{\underbrace{\left(S_{t}\right)}_{A_{t}}\bullet_{A_{t + 1}}^{R_{t + 1}}\underbrace{\left(S_{t + 1}\right)}_{A_{t + 1}}\bullet_{A_{t + 1}}^{R_{t + 2}}\underbrace{\left(S_{t + 2}\right)}_{A_{t + 2}}\bullet_{A_{t + 2}}^{R_{t + 3}}\underbrace{\left(S_{t + 3}\right)}_{A_{t + 3}}\bullet_{A_{t + 3}}\cdots
$$

In the previous section we considered transitions from state to state and learned the values of states. Now we consider transitions from state- action pair to state- action pair, and learn the values of state- action pairs. Formally these cases are identical: they are both Markov chains with a reward process. The theorems assuring the convergence of state values under TD(0) also apply to the corresponding algorithm for action values:

$$
Q(S_{t},A_{t})\leftarrow Q(S_{t},A_{t}) + \alpha \Big[R_{t + 1} + \gamma Q(S_{t + 1},A_{t + 1}) - Q(S_{t},A_{t})\Big]. \tag{6.7}
$$

This update is done after every transition from a nonterminal state  \(S_{t}\)  .If  \(S_{t + 1}\)  is terminal, then  \(Q(S_{t + 1},A_{t + 1})\)  is defined as zero. This rule uses every element of the quintuple of events,  \((S_{t},A_{t},R_{t + 1},S_{t + 1},A_{t + 1})\)  , that make up a transition from one state- action pair to the next. This quintuple gives rise to the name Sarsa for the algorithm. The backup diagram for Sarsa is as shown to the right.

It is straightforward to design an on- policy control algorithm based on the Sarsa prediction method. As in all on- policy methods, we continually estimate  \(q_{\pi}\)  for the behavior policy  \(\pi\)  , and at the same time change  \(\pi\)  toward greediness with respect to  \(q_{\pi}\)  The general form of the Sarsa control algorithm is given in the box on the next page.

The convergence properties of the Sarsa algorithm depend on the nature of the policy's dependence on  \(Q\)  . For example, one could use  \(\epsilon\)  - greedy or  \(\epsilon\)  - soft policies. Sarsa converges with probability 1 to an optimal policy and action- value function, under the usual conditions on the step sizes (2.7), as long as all state- action pairs are visited an infinite number of times and the policy converges in the limit to the greedy policy (which can be arranged, for example, with  \(\epsilon\)  - greedy policies by setting  \(\epsilon = 1 / t\)  -

Exercise 6.8 Show that an action- value version of (6.6) holds for the action- value form of the TD error  \(\delta_{t} = R_{t + 1} + \gamma Q(S_{t + 1},A_{t + 1}) - Q(S_{t},A_{t})\)  , again assuming that the values don't change from step to step.

# Sarsa (on-policy TD control) for estimating  \(Q \approx q_{*}\)

Algorithm parameters: step size  \(\alpha \in (0,1]\)  , small  \(\epsilon >0\)

Initialize  \(Q(s,a)\)  , for all  \(s\in \mathbb{S}^{+}\) \(a\in \mathcal{A}(s)\)  , arbitrarily except that  \(Q(t e r m i n a l,\cdot) = 0\)

Loop for each episode:

Initialize  \(S\)

Choose  \(A\)  from  \(S\)  using policy derived from  \(Q\)  (e.g.,  \(\epsilon\) - greedy)

Loop for each step of episode:

Take action  \(A\)  , observe  \(R\) \(S^{\prime}\)

Choose  \(A^{\prime}\)  from  \(S^{\prime}\)  using policy derived from  \(Q\)  (e.g.,  \(\epsilon\)  - greedy)

\(Q(S,A)\leftarrow Q(S,A) + \alpha \big[R + \gamma Q(S^{\prime},A^{\prime}) - Q(S,A)\big]\)

\(S\leftarrow S^{\prime}\)  .  \(A\leftarrow A^{\prime}\)

until  \(S\)  is terminal

Example 6.5: Windy Gridworld Shown inset below is a standard gridworld, with start and goal states, but with one difference: there is a crosswind running upward through the middle of the grid. The actions are the standard four- up, down, right, and left- - but in the middle region the resultant next states are shifted upward by a "wind," the strength of which varies from column to column. The strength of the wind is given below each column, in num

ber of cells shifted upward. For example, if you are one cell to the right of the goal, then the action left takes you to the cell just above the goal. This is an undiscounted episodic task, with constant rewards of  \(- 1\)  until the goal state is reached.

The graph to the right shows the results of applying  \(\epsilon\)  - greedy Sarsa to this task, with  \(\epsilon = 0.1\) \(\alpha = 0.5\)  and the initial values  \(Q(s,a) = 0\)  for all  \(s,a\)  . The increasing slope of the graph shows that the goal was reached more quickly over time. By

![](images/ec945870b0c1a105c5335fa0b67216fbb30c560b1af8d559fc253b9ae12ffa54.jpg)

8000 time steps, the greedy policy was long since optimal (a trajectory from it is shown inset); continued  \(\epsilon\) - greedy exploration kept the average episode length at about 17 steps, two more than the minimum of 15. Note that Monte Carlo methods cannot easily be used here because termination is not guaranteed for all policies. If a policy was ever found that caused the agent to stay in the same state, then the next episode would never end. Online learning methods such as Sarsa do not have this problem because they quickly learn during the episode that such policies are poor, and switch to something else.

Exercise 6.9: Windy Gridworld with King's Moves (programming) Re- solve the windy gridworld assuming eight possible actions, including the diagonal moves, rather than four. How much better can you do with the extra actions? Can you do even better by including a ninth action that causes no movement at all other than that caused by the wind?  \(\square\)

Exercise 6.10: Stochastic Wind (programming) Re- solve the windy gridworld task with King's moves, assuming that the effect of the wind, if there is any, is stochastic, sometimes varying by 1 from the mean values given for each column. That is, a third of the time you move exactly according to these values, as in the previous exercise, but also a third of the time you move one cell above that, and another third of the time you move one cell below that. For example, if you are one cell to the right of the goal and you move left, then one- third of the time you move one cell above the goal, one- third of the time you move two cells above the goal, and one- third of the time you move to the goal.  \(\square\)

# 6.5 Q-learning: Off-policy TD Control

One of the early breakthroughs in reinforcement learning was the development of an off- policy TD control algorithm known as  \(Q\) - learning (Watkins, 1989), defined by

$$
Q(S_{t},A_{t})\leftarrow Q(S_{t},A_{t}) + \alpha \Big[R_{t + 1} + \gamma \max_{a}Q(S_{t + 1},a) - Q(S_{t},A_{t})\Big]. \tag{6.8}
$$

In this case, the learned action- value function,  \(Q\) , directly approximates  \(q_{*}\) , the optimal action- value function, independent of the policy being followed. This dramatically simplifies the analysis of the algorithm and enabled early convergence proofs. The policy still has an effect in that it determines which state- action pairs are visited and updated. However, all that is required for correct convergence is that all pairs continue to be updated. As we observed in Chapter 5, this is a minimal requirement in the sense that any method guaranteed to find optimal behavior in the general case must require it. Under this assumption and a variant of the usual stochastic approximation conditions on the sequence of step- size parameters,  \(Q\)  has been shown to converge with probability 1 to  \(q_{*}\) . The Q- learning algorithm is shown below in procedural form.

# Q-learning (off-policy TD control) for estimating  \(\pi \approx \pi_{*}\)

Algorithm parameters: step size  \(\alpha \in (0,1]\) , small  \(\epsilon > 0\)

Initialize  \(Q(s,a)\) , for all  \(s \in \mathbb{S}^{+}\) ,  \(a \in \mathcal{A}(s)\) , arbitrarily except that  \(Q(\text{terminal}, \cdot) = 0\)

Loop for each episode:

Initialize  \(S\)

Loop for each step of episode:

Choose  \(A\)  from  \(S\)  using policy derived from  \(Q\)  (e.g.,  \(\epsilon\) - greedy)

Take action  \(A\) , observe  \(R\) ,  \(S'\)

$$
Q(S,A)\leftarrow Q(S,A) + \alpha \big[R + \gamma \max_{a}Q(S^{\prime},a) - Q(S,A)\big]
$$

$$
S\leftarrow S^{\prime}
$$

until  \(S\)  is terminal

What is the backup diagram for Q- learning? The rule (6.8) updates a state–action pair, so the top node, the root of the update, must be a small, filled action node. The update is also from action nodes, maximizing over all those actions possible in the next state. Thus the bottom nodes of the backup diagram should be all these action nodes. Finally, remember that we indicate taking the maximum of these “next action” nodes with an arc across them (Figure 3.4- right). Can you guess now what the diagram is? If so, please do make a guess before turning to the answer in Figure 6.4 on page 134.

Example 6.6: Cliff Walking This gridworld example compares Sarsa and Q- learning, highlighting the difference between on- policy (Sarsa) and off- policy (Q- learning) methods.

Consider the gridworld shown to the right. This is a standard undiscounted, episodic task, with start and goal states, and the usual actions causing movement up, down, right, and left. Reward is  \(^{- 1}\)  on all transitions except those into the region marked “The Cliff.” Stepping into this region incurs a reward of  \(- 100\)  and sends the agent instantly back to the start.

The graph to the right shows the performance of the Sarsa and Qlearning methods with  \(\epsilon\)  - greedy action selection,  \(\epsilon = 0.1\)  . After an initial transient, Q- learning learns values for the optimal policy, that which travels right along the edge of the cliff. Unfortunately, this results in its occasionally falling off the cliff because of the  \(\epsilon\)  - greedy action selection. Sarsa, on the other hand, takes the action selection into account and learns the longer but safer path through the upper part of the grid. Although Q- learning actually learns the values of the optimal policy, its online performance is worse than that of Sarsa, which

![](images/6d6a794542ba53aa28983da0def6a8f083b2f366c5c5bcaa78163808c2f6a4f0.jpg)

![](images/519aa897b95d3450c3ba564ae7a4055fd7db9b761d1519a4b4c2bc8e76b997b8.jpg)

learns the roundabout policy. Of course, if  \(\epsilon\)  were gradually reduced, then both methods would asymptotically converge to the optimal policy.

Exercise 6.11 Why is Q- learning considered an off- policy control method?

Exercise 6.12 Suppose action selection is greedy. Is Q- learning then exactly the same algorithm as Sarsa? Will they make exactly the same action selections and weight updates? 口

# 6.6 Expected Sarsa

Consider the learning algorithm that is just like Q- learning except that instead of the maximum over next state- action pairs it uses the expected value, taking into account how likely each action is under the current policy. That is, consider the algorithm with the update rule

$$
\begin{array}{rl} & Q(S_t,A_t)\leftarrow Q(S_t,A_t) + \alpha \Big[R_{t + 1} + \gamma \mathbb{E}_\pi [Q(S_{t + 1},A_{t + 1})\mid S_{t + 1}] - Q(S_t,A_t)\Big]\\ & \qquad = Q(S_t,A_t) + \alpha \Big[R_{t + 1} + \gamma \sum_a\pi (a|S_{t + 1})Q(S_{t + 1},a) - Q(S_t,A_t)\Big], \end{array} \tag{6.9}
$$

but that otherwise follows the schema of Q- learning. Given the next state,  \(S_{t + 1}\)  , this algorithm moves deterministically in the same direction as Sarsa moves in expectation, and accordingly it is called Expected Sarsa. Its backup diagram is shown on the right in Figure 6.4.

Expected Sarsa is more complex computationally than Sarsa but, in return, it eliminates the variance due to the random selection of  \(A_{t + 1}\)  . Given the same amount of experience we might expect it to perform slightly better than Sarsa, and indeed it generally does. Figure 6.3 shows summary results on the cliff- walking task with Expected Sarsa compared to Sarsa and Q- learning. Expected Sarsa retains the significant advantage of Sarsa over Q- learning on this problem. In addition, Expected Sarsa shows a significant improvement

![](images/ece9b03275e1c9d917b55fd39796549c31c0ea4ac723865c5d98f1fd99ee7d2e.jpg)  
Figure 6.3: Interim and asymptotic performance of TD control methods on the cliff-walking task as a function of  \(\alpha\) . All algorithms used an  \(\epsilon\) -greedy policy with  \(\epsilon = 0.1\) . Asymptotic performance is an average over 100,000 episodes whereas interim performance is an average over the first 100 episodes. These data are averages of over 50,000 and 10 runs for the interim and asymptotic cases respectively. The solid circles mark the best interim performance of each method. Adapted from van Seijen et al. (2009).

![](images/badcb245bb1aac883d97a8321fbbc60301ef294dfc588eb1bca12bfef34ba023.jpg)  
Figure 6.4: The backup diagrams for Q-learning and Expected Sarsa.

over Sarsa over a wide range of values for the step- size parameter  \(\alpha\) . In cliff walking the state transitions are all deterministic and all randomness comes from the policy. In such cases, Expected Sarsa can safely set  \(\alpha = 1\)  without suffering any degradation of asymptotic performance, whereas Sarsa can only perform well in the long run at a small value of  \(\alpha\) , at which short- term performance is poor. In this and other examples there is a consistent empirical advantage of Expected Sarsa over Sarsa.

In these cliff walking results Expected Sarsa was used on- policy, but in general it might use a policy different from the target policy  \(\pi\)  to generate behavior, in which case it becomes an off- policy algorithm. For example, suppose  \(\pi\)  is the greedy policy while behavior is more exploratory; then Expected Sarsa is exactly Q- learning. In this sense Expected Sarsa subsumes and generalizes Q- learning while reliably improving over Sarsa. Except for the small additional computational cost, Expected Sarsa may completely dominate both of the other more- well- known TD control algorithms.

# 6.7 Maximization Bias and Double Learning

All the control algorithms that we have discussed so far involve maximization in the construction of their target policies. For example, in Q- learning the target policy is the greedy policy given the current action values, which is defined with a max, and in Sarsa the policy is often  \(\epsilon\) - greedy, which also involves a maximization operation. In these algorithms, a maximum over estimated values is used implicitly as an estimate of the maximum value, which can lead to a significant positive bias. To see why, consider a single state  \(s\)  where there are many actions  \(a\)  whose true values,  \(q(s, a)\) , are all zero but whose estimated values,  \(Q(s, a)\) , are uncertain and thus distributed some above and some below zero. The maximum of the true values is zero, but the maximum of the estimates is positive, a positive bias. We call this maximization bias.

Example 6.7: Maximization Bias Example The small MDP shown inset in Figure 6.5 provides a simple example of how maximization bias can harm the performance of TD control algorithms. The MDP has two non- terminal states A and B. Episodes always start in A with a choice between two actions, left and right. The right action transitions immediately to the terminal state with a reward and return of zero. The left action transitions to B, also with a reward of zero, from which there are many possible actions all of which cause immediate termination with a reward drawn from a normal distribution with mean  \(- 0.1\)  and variance 1.0. Thus, the expected return for any trajectory starting with left is  \(- 0.1\) , and thus taking left in state A is always a

![](images/de7cd5c8b655c6af5056b94db0c0b9011ac1fe668470c14ff945fc76d56e867d.jpg)  
Figure 6.5: Comparison of Q-learning and Double Q-learning on a simple episodic MDP (shown inset). Q-learning initially learns to take the left action much more often than the right action, and always takes it significantly more often than the  \(5\%\)  minimum probability enforced by  \(\epsilon\) -greedy action selection with  \(\epsilon = 0.1\) . In contrast, Double Q-learning is essentially unaffected by maximization bias. These data are averaged over 10,000 runs. The initial action-value estimates were zero. Any ties in  \(\epsilon\) -greedy action selection were broken randomly.

mistake. Nevertheless, our control methods may favor left because of maximization bias making B appear to have a positive value. Figure 6.5 shows that Q- learning with  \(\epsilon\) - greedy action selection initially learns to strongly favor the left action on this example. Even at asymptote, Q- learning takes the left action about  \(5\%\)  more often than is optimal at our parameter settings ( \(\epsilon = 0.1\) ,  \(\alpha = 0.1\) , and  \(\gamma = 1\) ).

Are there algorithms that avoid maximization bias? To start, consider a bandit case in which we have noisy estimates of the value of each of many actions, obtained as sample averages of the rewards received on all the plays with each action. As we discussed above, there will be a positive maximization bias if we use the maximum of the estimates as an estimate of the maximum of the true values. One way to view the problem is that it is due to using the same samples (plays) both to determine the maximizing action and to estimate its value. Suppose we divided the plays in two sets and used them to learn two independent estimates, call them  \(Q_{1}(a)\)  and  \(Q_{2}(a)\) , each an estimate of the true value  \(q(a)\) , for all  \(a \in \mathcal{A}\) . We could then use one estimate, say  \(Q_{1}\) , to determine the maximizing action  \(A^{*} = \operatorname{argmax}_{a} Q_{1}(a)\) , and the other,  \(Q_{2}\) , to provide the estimate of its value,  \(Q_{2}(A^{*}) = Q_{2}(\operatorname{argmax}_{a} Q_{1}(a))\) . This estimate will then be unbiased in the sense that  \(\mathbb{E}[Q_{2}(A^{*})] = q(A^{*})\) . We can also repeat the process with the role of the two estimates reversed to yield a second unbiased estimate  \(Q_{1}(\operatorname{argmax}_{a} Q_{2}(a))\) . This is the idea of double learning. Note that although we learn two estimates, only one estimate is updated on each play; double learning doubles the memory requirements, but does not increase the amount of computation per step.

The idea of double learning extends naturally to algorithms for full MDPs. For example, the double learning algorithm analogous to Q- learning, called Double Q- learning, divides the time steps in two, perhaps by flipping a coin on each step. If the coin comes up heads, the update is

$$
Q_{1}(S_{t},A_{t})\leftarrow Q_{1}(S_{t},A_{t}) + \alpha \Big[R_{t + 1} + \gamma Q_{2}\big(S_{t + 1},\underset {a}{\arg \max}Q_{1}(S_{t + 1},a)\big) - Q_{1}(S_{t},A_{t})\Big]. \tag{6.10}
$$

If the coin comes up tails, then the same update is done with  \(Q_{1}\)  and  \(Q_{2}\)  switched, so that  \(Q_{2}\)  is updated. The two approximate value functions are treated completely symmetrically. The behavior policy can use both action- value estimates. For example, an  \(\epsilon\) - greedy policy for Double Q- learning could be based on the average (or sum) of the two action- value estimates. A complete algorithm for Double Q- learning is given in the box below. This is the algorithm used to produce the results in Figure 6.5. In that example, double learning seems to eliminate the harm caused by maximization bias. Of course there are also double versions of Sarsa and Expected Sarsa.

# Double Q-learning, for estimating  \(Q_{1} \approx Q_{2} \approx q_{*}\)

Algorithm parameters: step size  \(\alpha \in (0,1]\)  , small  \(\epsilon >0\)

Initialize  \(Q_{1}(s,a)\)  and  \(Q_{2}(s,a)\)  , for all  \(s\in \mathbb{S}^{+},a\in \mathcal{A}(s)\)  , such that  \(Q(t e r m i n a l,\cdot) = 0\)

Loop for each episode:

Initialize  \(S\)

Loop for each step of episode:

Choose  \(A\)  from  \(S\)  using the policy  \(\epsilon\) - greedy in  \(Q_{1} + Q_{2}\)

Take action  \(A\) , observe  \(R\) ,  \(S'\)

With 0.5 probability:

$$
Q_{1}(S,A) \leftarrow Q_{1}(S,A) + \alpha \Big(R + \gamma Q_{2}\big(S^{\prime},\mathrm{argmax}_{a}Q_{1}(S^{\prime},a)\big) - Q_{1}(S,A)\Big)
$$

else:

$$
Q_{2}(S,A) \leftarrow Q_{2}(S,A) + \alpha \Big(R + \gamma Q_{1}\big(S^{\prime},\mathrm{argmax}_{a}Q_{2}(S^{\prime},a)\big) - Q_{2}(S,A)\Big)
$$

\(S \leftarrow S'\)

until  \(S\)  is terminal

*Exercise 6.13 What are the update equations for Double Expected Sarsa with an  \(\epsilon\) - greedy target policy?  \(\square\)

# 6.8 Games, Afferstates, and Other Special Cases

In this book we try to present a uniform approach to a wide class of tasks, but of course there are always exceptional tasks that are better treated in a specialized way. For example, our general approach involves learning an action- value function, but in Chapter 1 we presented a TD method for learning to play tic- tac- toe that learned something much more like a state- value function. If we look closely at that example, it becomes apparent that the function learned there is neither an action- value function nor a state- value function in the usual sense. A conventional state- value function evaluates states in which the agent has the option of selecting an action, but the state- value function used in

tic- tac- toe evaluates board positions after the agent has made its move. Let us call these afterstates, and value functions over these, afterstate value functions. Afterstates are useful when we have knowledge of an initial part of the environment's dynamics but not necessarily of the full dynamics. For example, in games we typically know the immediate effects of our moves. We know for each possible chess move what the resulting position will be, but not how our opponent will reply. Afterstate value functions are a natural way to take advantage of this kind of knowledge and thereby produce a more efficient learning method.

The reason it is more efficient to design algorithms in terms of afterstates is apparent from the tic- tac- toe example. A conventional action- value function would map from positions and moves to an estimate of the value. But many position—move pairs produce the same resulting position, as in the example below: In such cases the

position—move pairs are different but produce the same "afterposition," and thus must have the same value. A conventional action- value function would have to separately assess both pairs, whereas an afterstate value function would immediately assess both equally. Any learning about the position—move pair on the left would immediately transfer to the pair on the right.

Afterstates arise in many tasks, not just games. For example, in queuing tasks there are actions

![](images/a2d215424d192f8c2ade212086c328e1b8b3e290c09a70774cb00281e5f28c7e.jpg)

such as assigning customers to servers, rejecting customers, or discarding information. In such cases the actions are in fact defined in terms of their immediate effects, which are completely known.

It is impossible to describe all the possible kinds of specialized problems and corresponding specialized learning algorithms. However, the principles developed in this book should apply widely. For example, afterstate methods are still aptly described in terms of generalized policy iteration, with a policy and (afterstate) value function interacting in essentially the same way. In many cases one will still face the choice between on- policy and off- policy methods for managing the need for persistent exploration.

Exercise 6.14 Describe how the task of Jack's Car Rental (Example 4.2) could be reformulated in terms of afterstates. Why, in terms of this specific task, would such a reformulation be likely to speed convergence?

# 6.9 Summary

In this chapter we introduced a new kind of learning method, temporal- difference (TD) learning, and showed how it can be applied to the reinforcement learning problem. As usual, we divided the overall problem into a prediction problem and a control problem. TD methods are alternatives to Monte Carlo methods for solving the prediction problem. In both cases, the extension to the control problem is via the idea of generalized policy iteration (GPI) that we abstracted from dynamic programming. This is the idea that approximate policy and value functions should interact in such a way that they both move toward their optimal values.

One of the two processes making up GPI drives the value function to accurately predict returns for the current policy; this is the prediction problem. The other process drives the policy to improve locally (e.g., to be  \(\epsilon\) - greedy) with respect to the current value function. When the first process is based on experience, a complication arises concerning maintaining sufficient exploration. We can classify TD control methods according to whether they deal with this complication by using an on- policy or off- policy approach. Sarsa is an on- policy method, and Q- learning is an off- policy method. Expected Sarsa is also an off- policy method as we present it here. There is a third way in which TD methods can be extended to control which we did not include in this chapter, called actor- critic methods. These methods are covered in full in Chapter 13.

The methods presented in this chapter are today the most widely used reinforcement learning methods. This is probably due to their great simplicity: they can be applied online, with a minimal amount of computation, to experience generated from interaction with an environment; they can be expressed nearly completely by single equations that can be implemented with small computer programs. In the next few chapters we extend these algorithms, making them slightly more complicated and significantly more powerful. All the new algorithms will retain the essence of those introduced here: they will be able to process experience online, with relatively little computation, and they will be driven by TD errors. The special cases of TD methods introduced in the present chapter should rightly be called one- step, tabular, model- free TD methods. In the next two chapters we extend them to  \(n\) - step forms (a link to Monte Carlo methods) and forms that include a model of the environment (a link to planning and dynamic programming). Then, in the second part of the book we extend them to various forms of function approximation rather than tables (a link to deep learning and artificial neural networks).

Finally, in this chapter we have discussed TD methods entirely within the context of reinforcement learning problems, but TD methods are actually more general than this. They are general methods for learning to make long- term predictions about dynamical systems. For example, TD methods may be relevant to predicting financial data, life spans, election outcomes, weather patterns, animal behavior, demands on power stations, or customer purchases. It was only when TD methods were analyzed as pure prediction methods, independent of their use in reinforcement learning, that their theoretical properties first came to be well understood. Even so, these other potential applications of TD learning methods have not yet been extensively explored.

# Bibliographical and Historical Remarks

As we outlined in Chapter 1, the idea of TD learning has its early roots in animal learning psychology and artificial intelligence, most notably the work of Samuel (1959) and Klopf (1972). Samuel's work is described as a case study in Section 16.2. Also related to TD learning are Holland's (1975, 1976) early ideas about consistency among value predictions. These influenced one of the authors (Barto), who was a graduate student from 1970 to 1975 at the University of Michigan, where Holland was teaching. Holland's ideas led to a number of TD- related systems, including the work of Booker (1982) and the bucket brigade of Holland (1986), which is related to Sarsa as discussed below.

6.1- 2 Most of the specific material from these sections is from Sutton (1988), including the TD(0) algorithm, the random walk example, and the term "temporaldifference learning." The characterization of the relationship to dynamic programming and Monte Carlo methods was influenced by Watkins (1989), Werbos (1987), and others. The use of backup diagrams was new to the first edition of this book.

Tabular TD(0) was proved to converge in the mean by Sutton (1988) and with probability 1 by Dayan (1992), based on the work of Watkins and Dayan (1992). These results were extended and strengthened by Jaakkola, Jordan, and Singh (1994) and Tsitsiklis (1994) by using extensions of the powerful existing theory of stochastic approximation. Other extensions and generalizations are covered in later chapters.

6.3 The optimality of the TD algorithm under batch training was established by Sutton (1988). Illuminating this result is Barnard's (1993) derivation of the TD algorithm as a combination of one step of an incremental method for learning a model of the Markov chain and one step of a method for computing predictions from the model. The term certainty equivalence is from the adaptive control literature (e.g., Goodwin and Sin, 1984).

6.4 The Sarsa algorithm was introduced by Rummery and Niranjan (1994). They explored it in conjunction with artificial neural networks and called it "Modified Connectionist Q- learning". The name "Sarsa" was introduced by Sutton (1996). The convergence of one- step tabular Sarsa (the form treated in this chapter) has been proved by Singh, Jaakkola, Littman, and Szepesvári (2000). The "windy gridworld" example was suggested by Tom Kalt.

Holland's (1986) bucket brigade idea evolved into an algorithm closely related to Sarsa. The original idea of the bucket brigade involved chains of rules triggering each other; it focused on passing credit back from the current rule to the rules that triggered it. Over time, the bucket brigade came to be more like TD learning in passing credit back to any temporally preceding rule, not just to the ones that triggered the current rule. The modern form of the bucket brigade, when simplified in various natural ways, is nearly identical to one- step Sarsa, as detailed by Wilson (1994).

6.5 Q- learning was introduced by Watkins (1989), whose outline of a convergence proof was made rigorous by Watkins and Dayan (1992). More general convergence results were proved by Jaakkola, Jordan, and Singh (1994) and Tsitsiklis (1994).

6.6 The Expected Sarsa algorithm was introduced by George John (1994), who called it "Q- learning" and stressed its advantages over Q- learning as an off- policy algorithm. John's work was not known to us when we presented Expected Sarsa in the first edition of this book as an exercise, or to van Seijen, van Hasselt, Whiteson, and Weiring (2009) when they established Expected Sarsa's convergence properties and conditions under which it will outperform regular Sarsa and Q- learning. Our Figure 6.3 is adapted from their results. Van Seijen et al. defined "Expected Sarsa" to be an on- policy method exclusively (as we did in the first edition), whereas now we use this name for the general algorithm in which the target and behavior policies may differ. The general off- policy view of Expected Sarsa was noted by van Hasselt (2011), who called it "General Q- learning."

6.7 Maximization bias and double learning were introduced and extensively investigated by van Hasselt (2010, 2011). The example MDP in Figure 6.5 was adapted from that in his Figure 4.1 (van Hasselt, 2011).

6.8 The notion of an afterstate is the same as that of a "post- decision state" (Van Roy, Bertsekas, Lee, and Tsitsiklis, 1997; Powell, 2011).
