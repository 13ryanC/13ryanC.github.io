---
_build:
  render: never
  list: never
---


There’s plenty of introductory material and textbooks on RL, yet, to be honest, I still don’t fully grasp any of them.

Even when they show working demos, it often feels like hand-waving—just code that suddenly works.

I can replicate the experiments and vaguely follow the flow, but can I explain clearly *why* things happen instead of simply pointing to some authoritative paper?

I’ve had enough. I’m going to write my own informal notes—analyzed from my perspective.

For context, I’m self-taught in real analysis, axiomatic set theory, and axiomatic geometry.

Hand-waving doesn’t stick; my brain filters it out. I need a solid baseline I can trust.

My years in engineering felt wasted because everything relied on that same leap of faith. After studying rigorous math, it’s hard to accept hand-waving in any domain.

I really hope people do unifying more closely and tightly between theory and practice, like in engineering, I think people should be much more serious about the mathematical correctness and conditions in which they apply, as I would quote from Terry Tao's analysis I textbook on why do analysis, "why bother". One might argue that one only needs to know how things work to do real-life problem, however, one can get into trouble if one applies rules without knowing where they came from and what the limits of their applicability are. If you are still not convinced, then perhaps the idea of leaky abstraction by Joel Spolsky would help explains.

Some time ago, I read Sutton and Silver's position paper on the era of experience and I agree that is probably pointing where the next paradigm of scale-up in learning will come from, after the bitter lesson success we have enjoyed from large-scale pre-training and the success of scaling up internal dilberation as Yoshua bengio mentioned (link to mlst video). 

It is important to understand that though surprises from deep learning. RL has always had an active presence from the era of simulation (AlphaGo), the era of human data (RLHF, safety training, internal dilberation of reasoning chains). I think we all agree that the next paradigm will surely be on the era of experience, where we are experiencing diminishing returns from the large-scale simulation training and the use of human data as supervised learning target.

The era of experience's success is uneqivaolty resting on the realm of reinforcement learning and its other adjoint fields like universal artificial intelligence, information theory, bayeisn learning, cogntiive sciece programs, where the interanl dynamics will still be advacned by the deep leraning communities and with biological inspired communities and active looking for open-ended exploration strands. 

We may reach there sooner than we think. Regardless of the risks and dangers of superintelligence as introduced in Nick Bostrom's book, which I wholeheartedly recommend chapters 6,7,8,9,10,12, 13) for techical introductions, as the other chapters are basically doing scenario analysis which serves other valuable purposes.

it is important for us to revisit the fundamentals of reinforcement learning as often practitoners struggle with experimentation (as detailed in the empirical design of RL paper).

I think there should be a more unified view and holistic view of the domain for true trimph, as not only information is very scattered aroudn on the internet and without a good unification between experientation and theory like in other traditional sciences like biology and chemistry, not sure for frontier physics as that seems to be a mess.

I hope I can via my blog help the community to lean into more into that direction (actually I just got sick of retreiving mateirals and stick them together in ways that I don't really learn and absorb).

So I will start the two strands of RL from the low road and the high road, just like what Friston and Chris Paar in their active inference does, where RL can be attached in both experimental angles and theoreitical angle, I hope, people will appreicate and perhaps even better  theory and expeirmentation can be connected more tightly together where both progresses side by side, as with the emerging maturity in formalisating mathemaical proofs in LEAN by community efforts. Maybe one day all RL resaerchers can still just poke some crazy ideas in theory, helped by a LLM (or something else), then come up with some mathamtical equation and then be able to implemetn it for resaerch and quickly into production, whereeas it is possibly to disover something in research implementation and production  and quckl that can be turned into matheatics and quicly formalised to verify correctness that would again help the theory side.

this sounds very ideal and I hope this will get sooner than I think, which will in turn hellp out a lot for both beginners , practitioners and researchers alike.
