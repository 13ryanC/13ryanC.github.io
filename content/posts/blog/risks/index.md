---
date: '2026-04-17'
title: "Hot Takes on Risk Quantification in AI"
summary: 
description: 
lastmod: '2026-04-17'
category: Blog
series:
- Research Notes
tags:
- AI
- AI Safety
status: draft
author: Bryan Chan
hero: /assets/images/hero3.png
image: /assets/images/card3.png
---

[Risk equals probability times severity.](https://www.aisafetybook.com/textbook/risk-decomposition) Every safety textbook opens with it. Every AI governance paper invokes it. Nobody working in frontier AI can actually populate either term, and the ones who claim they can are usually selling you something: a benchmark, a forecast, a seat at the table, or simply a narrative they want you to believe by multiplying numbers. The rest of us are guessing and calling the guess "empirically informed.”

This blog post is a hot take from inside that guessing game. The argument is that AI risk quantification fails at three layers simultaneously: technical (the inputs to the risk equation dissolve on contact with actual AI production systems), institutional (we lack the feedback machinery needed as in nuclear, aviation, or chemicals), and emergent (i.e., estimating [systemic](https://ai-safety-atlas.com/chapters/v1/risks/systemic-risks/) [risks](https://www.aisafetybook.com/textbook/systemic-factors) is complex[^1] in [Glouberman and Zimmerman](https://www.researchgate.net/publication/265240426_Complicated_and_Complex_Systems_What_Would_Successful_Reform_of_Medicare_Look_Like)’s sense). This post will go through layer by layer, stress-test some of the proposed fixes and show where they break. If this diagnosis is sound, then likely most current AI safety and governance work is theatre work. Regulators are being briefed by AI experts who have no knowledge on how risk can be properly quantified, some of whose incentives the regulation is meant to constrain. One hot take is to stop pretending we have somewhat of a risk quantification methodology regarding AI and start building the feedback institutions that would let us earn one.

## Why risk quantification matters

If risk cannot be measured, safety work has no target. Companies do it by intuition. Regulators defer to whichever AI expert is in the room. Governments write legislation against capability thresholds that they cannot reliably verify. Insurance markets retreat. None of this is about AI being special in some mystical sense. It is about every institution downstream of a number (liability, insurance, licensing, capital allocation, international coordination) all needing that number to exist, and it doesn't. The stakes are so high that the question is no longer whether we are under-regulating AI; it is that the entire apparatus we have built for managing high-stakes domains (e.g.,chemical and nuclear risks) is now running on empty inputs.

## The Technical Layer

The risk equation ($R \= \\sum f\_i c\_i$) summing over scenarios the product of each scenario’s frequency and its consequence magnitude, decomposes cleanly in complicated[^2] domains where the causal structure is relatively well-behaved. In chemical engineering, for example, a reactor is a unit operation that turns chemicals A into chemicals B. The transport phenomena[^3] and reaction kinetics[^4], can be derived from first-principles; component failure histories are cataloged in reliability databases. [Fault-tree analysis](https://en.wikipedia.org/wiki/Fault_tree_analysis) then propagates these event probabilities upward through the logical structure of the system to yield the probability of a top-level failure. The engineer’s derivation is, in principle, reconstructible end-to-end, and a regulator can check whether it actually is.

None of this works for AI systems. Unwanted behaviour from a model is produced by factors that span the whole stack: intrinsic model hazards (objective misspecification, latent dangerous capabilities, distributional brittleness), scenario conditions (deployment context, attacker model, granted autonomy), and sociotechnical factors (user incentives, quality of oversight). Each of the three properties that made the reactor case tractable breaks down here:

**First, independence.** In a reactor, component failures can be treated roughly as unrelated events (a valve sticks for its own reasons, an alarm is missed for others), so their probabilities can be combined by straightforward multiplication through the system.  
AI failure modes don't separate this way: a latent capability is only dangerous conditional on a deployment that grants it autonomy, and an objective misspecification matters more or less depending on the quality of oversight. The factors are entangled, so the probabilities don't compose cleanly. 

**Second, base-rate data.** Decades of logged operating hours give engineers concrete failure frequencies for every pump, valve, and relief device. There is no comparable dataset for "goal misgeneralization under distribution shift" or "jailbreak given adversarial suffix," and training runs are not the kind of repeated trials that would produce such statistics.

**Third, stability over time.** A pump built next year fails at close to the rate of one built this year, so yesterday's data forecasts tomorrow. A new frontier model is effectively a new artifact, with failure modes that need to be characterized from scratch.

The two terms of the risk equation inherit these pathologies directly.

* **Frequency** depends on use patterns, user incentives, and the stability of model behaviour on inputs it has never seen, including inputs that will not exist until after deployment.  
* **Consequence magnitude** scales with the breadth of deployment, the pathways through which harmful outputs or actions propagate, the reversibility of the damage, and the institutional capacity to absorb it. 

Each of these inputs is open-ended in a way the reactors were not: they range over deployments, users, and inputs that have not yet been observed. **A global estimate of risk across all of them is simply not available.**

The principled move is therefore to narrow the scope until the terms become tractable, and to argue explicitly for safety within that scope: “*for this class of models, under this access profile, in this deployment environment, under these control mechanisms, the system is acceptably safe because…”* This is the structure of a [**safety case**](https://www.lesswrong.com/posts/38HzJMYdr2YL5gWQs/safety-cases-explained-how-to-argue-an-ai-is-safe), the safety-focused instance of an assurance case, in which a top-level safety claim, asserted within a stated scope, is decomposed into sub-claims and discharged against evaluations, red-teaming results, interpretability evidence, and operational controls.

The earlier discussion of ($R \= \\sum f\_i c\_i$) was an informal sketch of [Quantitative Risk Analysis (QRA)](https://esc.uk.net/quantitative-risk-assessment/): the procedure that computes scenario-level risk from calibrated failure rates, validated consequence models, and stable system boundaries. QRA and safety cases are not independent tools competing for adoption; they are two layers of the same workflow. 

Safety cases, in system engineering disciplines, organise QRA outputs and other pre-validated inputs (standardised reliability tables, certified dispersion models, decades of incident data) into an argument that the system is acceptably safe under a stated scope. 

The rigor of the safety case rests on the rigor of the inputs it borrows; the rigor of those inputs in traditional engineering disciplines rests on empirical infrastructure built over decades. The structural difficulty is therefore shared: whatever breaks QRA's inputs also hollows out the safety case built on top of them.

For frontier AI systems, that infrastructure does not yet exist. Failure rates are not catalogued; consequence models are not validated; system boundaries shift with every model generation. QRA therefore cannot be evaluated in any defensible way, the equation $R \= \\sum f\_i c\_i$ has no calibrated terms to plug in. 

A safety case built on the same missing substrate inherits the same shortage, with the additional burden that its central sub-claims: that weights are secure against well-resourced adversaries; that scheming has been ruled out rather than merely not observed; that capability evaluations generalise to deployment; that interpretability tools verify rather than describe; are themselves open research problems. The argument form carries over from mature disciplines; the evidentiary foundation does not[^5].

What the AI field has instead are finer-grain component-level evaluation metrics: benchmark accuracy, robustness scores, jailbreak resistance, refusal rates. These measure how a foundational model behaves against specific test distributions.

In traditional system engineering discipline, component-level numbers like these would be inputs to a system-level risk calculation, combined with a validated model of how components interact, how failures propagate, and how consequences scale. 

In frontier AI, none of that upper machinery exists, so the component metrics are the *output*, not an input. They describe how the model behaves in isolation; they do not tell you how the deployed system behaves in production, once safeguards, monitoring, and human oversight are layered on top. 

The plant-level analogue (the residual risk of the full stack in its operational context) is the quantity that would actually inform deployment decisions, and it is the one nobody publishes. Reporting it would require disclosing the defense stack, which is simultaneously a commercial asset and, once public, a map for circumventing itself.

There's another technical problem hiding underneath, which the nuclear industry is useful for naming. After Fukushima, the nuclear sector moved away from *active* safety (systems requiring electrical power and mechanical intervention, which fail when power fails) toward *passive* safety (gravity, natural convection, physical principles that hold without intervention). 

Current frontier AI safety is almost entirely active: RLHF, moderation APIs, real-time filtering. These are susceptible to evaluation evasion, adversarial jailbreaks, and post-deployment fine-tuning. The passive analogue (deterministic compute constraints, structural safeguards that cannot be bypassed by prompting) barely exists. And as long as the safety mechanisms are active, they are not the kind of thing an actuary can price. The failure distribution under adversarial conditions has no stable shape.

So: the epistemic inputs dissolve, the institutional incentives suppress the one number that could substitute for them, and the safety mechanisms we do have are of a type that resists quantification by construction. The obstacles are epistemic, institutional, and technical at once. This is not a list of engineering gaps that will close with more work; it is more about reflecting the structure of the problem.

## The Institutional Layer

Now, considering the institutional obstacle. Risk quantification is not only missing numbers. It is missing the institutions that generate numbers.

In aviation, near-misses are reported, aggregated, analyzed, and fed back into training and design. In chemicals, the UK regulator inspects licensed reactors and tests operator knowledge. In nuclear, the Institute of Nuclear Power Operations (INPO), set up after Three Mile Island in 1979, runs peer audits backed by retrospective premiums of up to $158 million per reactor when any operator fails. In cybersecurity, the CVE registry gives everyone in the field a shared, fast-moving vocabulary for vulnerabilities and exposures. Each of these is a feedback institution. Each produces the data that eventually becomes the risk number.

AI has none of this. The incident databases that exist are useful but thin. They capture documented failures and near-misses but not exposure: how many systems were actually deployed, how many opportunities for failure existed, how often they were exploited, how many near-misses never got reported. Without exposure data, you have a numerator with no denominator, which is not a rate.

The obvious proposal is a CVE-for-AI: an international clearinghouse for continuous, multi-jurisdictional telemetry, capturing near-misses at all stages of deployment, structured so that network-theoretic models can be built on top of the viral distribution patterns of failures. The CVE framing captures the reporting culture; the telemetry framing captures what the data needs to *do*. Both are correct. Neither exists, and the reasons neither exist are instructive.

INPO works because the US commercial nuclear fleet is a strictly controlled oligopoly of 95 to 104 licensed reactors. Operators police each other because a failure anywhere triggers massive mandatory premiums on everyone. It is the market architecture, not the fines, doing the work. The decentralized AI ecosystem (open-weight proliferation, unbounded market entry, adversarial fine-tuning that strips guardrails from released models) resists closed-loop mutualization by construction. You cannot make labs police each other until you first cap the number of frontier operators via federal licensing, and mandate some level of intellectual-property waiver on weights and training data so structural audits are even possible. Neither of those is close.

Nuclear also solved a version of AI's disclosure dilemma by defining the Extraordinary Nuclear Occurrence: a physically measurable release of radiation that triggers strict liability automatically, without victims having to prove corporate negligence. You do not need to inspect the plant's internals. You measure the radiation offsite. The AI analogue would be an Extraordinary AI Occurrence pegged to downstream physical destruction or systemic financial collapse cryptographically traceable to a specific model's autonomous execution, an idea worth exploring. It also does not fully work: digital information is non-rivalrous, First Amendment protections complicate "dangerous output" as a trigger, and most AI harm vectors are invisible in the way radiation is not. Still, it is structurally the right shape (liability tied to measurable outcomes rather than an inspectable process) and probably further along than anything currently in the legislative pipeline.

Then there is the political economy. Fines need to be large enough to change behavior but not so large that they collapse the sector. In AI, where the profit margins are expected to be enormous, the fine required to matter is correspondingly enormous, and the lobbying power deployed against it is also enormous. I do not see a path to this in the US short of a catastrophic, publicly visible, street-demonstration-level harm event that destroys the government's willingness to defer to frontier labs. Short of that, the collective action of the AI industry is to spend whatever it takes to prevent binding institutional machinery from forming. This is not a conspiracy theory. It is the default behavior of every well-capitalized incumbent sector in US regulatory history.

There is a deeper problem underneath all of this, which is information asymmetry. AI is an emerging field. Regulators have little knowledge of and little access to capability, functioning, and deployment data. Frontier labs themselves do not fully understand the risks of what they ship, because the concerning behaviors are emergent phenomena that were not foreseen in advance. This is not a case of a knowledgeable industry withholding information from an ignorant regulator. It is a case of an industry that is itself partly in the dark briefing a regulator that is entirely in the dark. The expert class the regulator relies on has heterogeneous incentives, different theories of what "safety" means, and different financial stakes in the outcome. The regulator cannot fact-check them because the regulator does not have independent expertise: the way a UK chemical-reactor inspector can test an operator's knowledge of reaction kinetics, or an NRC inspector can test a nuclear operator's understanding of coolant flow. The chain of epistemic custody that makes regulation possible in other high-stakes sectors does not exist here.

## The Emergent Layer

The first two layers describe a gap that could, in principle, be closed with enough investment and with better metrics, better institutions, better data. But not the third layer.

[Glouberman and Zimmerman](https://www.researchgate.net/publication/265240426_Complicated_and_Complex_Systems_What_Would_Successful_Reform_of_Medicare_Look_Like)'s distinction between *complicated* and *complex* problems is the key move. A complicated problem is difficult but tractable: decomposable into sub-problems, solvable with sufficient expertise, and predictable given the inputs. Sending a rocket to the moon is complicated. The causal structure is well-defined. Outcomes follow from physical law. Feedback between intervention and result is reliable. You can, with enough effort and money, know what will happen.

A complex problem is different in kind. It involves dynamic interdependencies, non-linear feedback, and emergent properties that cannot be predicted from components. Raising a child is complex. Outcomes are substantially decoupled from decision-making quality. You can make all the right choices and face an unpredictable result. You can be idle or err and stumble into a good one.

AI risk is complex, not complicated. Models are deployed into a global economy that itself has a non-linear feedback structure. Emergent capabilities appear at scale that were not present in smaller models. Attacker populations adapt. Defender populations adapt. The failure modes that actually matter are the ones nobody predicted, because the ones people predicted got patched. The tail is fat, the distribution's shape is not stable, and the interactions between low-probability events and extremely high severity are exactly the regime where standard statistical methods are least reliable.

This is where I break with the super-forecasting paradigm. I lean toward Nassim Nicholas Taleb's view of risk, that in fat-tailed regimes, point forecasts are worse than useless because they create false precision that crowds out the correct response, which is structural: reduce exposure to the tail, maintain optionality, do not bet the system on a number. I do not go all the way to defeatism, because I think the future is created and state-dependent. Unless we are already in a lock-in regime, in which case we will not know until after it has happened, at which point pessimism is moot.

What this layer means for the first two is that even a fully built-out CVE-for-AI, even a functional INPO equivalent, even a well-defined Extraordinary AI Occurrence statute, will not produce a reliable risk number. It will produce a better-informed guess. This is not nothing (a better-informed guess is a massive improvement over the current situation) but it is worth being honest that decomposition-based risk methods have a ceiling, and we are building institutions to approach that ceiling, not to transcend it.

## Conclusion

Every high-consequence industry in the twentieth century earned its risk numbers the same way. Someone died. Someone investigated. Someone wrote it down. Someone built the institution that made sure the next person's death taught the next operator something. Aviation did this. Nuclear did this. Chemicals did this. The numbers those industries now quote (the failure rates, the exposure bounds, the actuarial tables) are not theoretical achievements. They are sedimented grief, processed through decades of feedback machinery that the public paid for and the industry was forced to cooperate with.

AI has not done this. AI has skipped the step. The field is quoting numbers it has not earned, borrowed from a methodology that does not fit the problem, inside a political economy that is actively preventing the feedback institutions from forming. Every party to this arrangement has a reason not to say so out loud. Labs have capitalization to protect. Regulators have credibility to protect. Safety researchers have funding to protect. Forecasters have reputations to protect. The rest of us have a kind of learned helplessness, the sense that someone, somewhere, must have the real numbers, because the alternative is too uncomfortable to sit with.

There are no real numbers. There are guesses dressed as numbers, and there is a growing governance apparatus built on top of the dressing. The honest move is to stop pretending, stop deferring to the experts whose incentives the regulation is supposed to constrain, and start building: slowly, unglamorously, in the face of industry resistance; the feedback institutions that would let the field eventually earn a number worth defending.

Until then, every risk figure you see quoted about frontier AI is a bluff. Sometimes a well-intentioned bluff. Sometimes a sophisticated one. Always a bluff. The first step toward any safety worth the name is saying that out loud.

[^1]:  A **complex problem** is different in kind. It involves dynamic interdependencies, non-linear feedback, and emergent properties that cannot be predicted from its components (i.e., raising a child is complex), where the outcome is substantially decoupled from decision-making quality. You can make all the “right” choices and face an unpredictable bad outcome; you can err/be idle and stumble into a good outcome if you are lucky.

[^2]:  A **complicated problem** is difficult but tractable: decomposable into sub-problems, solvable with sufficient expertise, and predictable. Sending a rocket to the moon is complicated, where the causal structure is well-defined, outcomes in principle predictable, and feedback between intervention and results is reliable (i.e., following physical laws).

[^3]:  **Transport phenomena** is the branch of engineering physics that deals with things that move through a system: momentum (fluid-flow), heat (thermal energy), and mass (chemicals). In a reactor, all three has to be considered simultaneously and are coupled: fluid carrying the reactants flows through the vessel, that flow determines how much heat is removed from the reaction, and the heat distribution determines how fast the reaction proceeds at each point in space, which in turn determines how much mass of each chemical is present.

[^4]:  **Reaction kinetics** is the study of how fast chemical reactions proceed and what mechanisms drive them. It studies chemical reactions by reasoning at what rate, via which intermediate steps, on what catalyst surface, and under what conditions of temperature, pressure, and chemical concentration. A kineticist can, in principle, derive a reactor's overall conversion rate from the elementary reaction steps up: why this catalyst was chosen, how molecules adsorb onto its active sites, which bonds break in what order, how the rate-limiting step scales with temperature (the arrhenius equation), and how all of this aggregates into the macroscopic rate equation the reactor is designed around.

[^5]:  For the safety case debate in detail, see [JanWehner (2026)](https://www.lesswrong.com/posts/j5XBfcDxLnFTbe9np/should-the-ai-safety-community-prioritize-safety-cases).



