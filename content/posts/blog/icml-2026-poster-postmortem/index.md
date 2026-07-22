---
date: '2026-07-22'
title: "Spent 10+ Iterations Designing my First Academic Poster and barely Planned for the Presentation"
summary: "A post-mortem of my first poster presentation: what I have done, what I learn, and what future poster presenters should take heed when designing their poster, presenting their poster and having conversations."
description: "A post-mortem of my first poster presentation: what I have done, what I learn, and what future poster presenters should take heed when designing their poster, presenting their poster and having conversations."
lastmod: '2026-07-22'
category: Blog
series:
- Research Notes
tags:
- Post-Mortem
- AI
- AI Safety
- ICML
- Research
status: draft
author: Bryan Chan
hero: /assets/images/hero3.png
image: /assets/images/card3.png
draft: false
---

*A post-mortem of my first poster presentation: what I have done, what I learn, and what future poster presenters should take heed when designing their poster, presenting their poster and having conversations.*

By 3:30 on Saturday afternoon, July 11, the ICML workshops were winding down. Attendees drifted between the remaining posters, stopping when a title or figure caught their attention. I stood beside mine, scrolling through my phone as people passed.

The poster had already gone through more than 10 rounds of revision, all in a closed loop: me, ChatGPT's image generator, and a checklist of poster-design advice I have synthesised from online information. I finished the camera-ready paper close to its June 26 deadline, compressed the design into a two-day sprint, and had it done by June 30. Then I stopped thinking about it. Not one of the checkpoints involved another researcher looking and trying to read it.

Its first real audience arrived eleven days later, on the workshop wall. No one tested whether the key elements of the poster must be visible 1-2 meters away or even 2-3 meters away, thus affecting the design of key elements that would catch the eye of a typical wandering attendees of posters hanging around and what would engage more interested researchers.

When someone stopped, I answered by explaining almost the entire paper: the motivation, the intervention, the benchmark, the results, the limitations, and sometimes the appendix. Each walkthrough ran ten to fifteen minutes, and I spoke for most of it. The visitors asked very little, because I left them far too little room to.

This was my first proper academic poster session, investigating why inoculation prompting fails to reduce sycophancy. I had prepared the poster according to some online scraped guidance in poster presentations which has high variance which I have improvised on the specific rubrics in ad-hoc fashion. It turns out that many of those assumptions are wrong and need corrections.

What follows is a post-mortem of that mismatch: what still worked, where the preparation went well, and what poster presenter (aka researchers) can work and change to make the poster and the poster presentation itself worthwhile for attendees and yourself.

## The closed loop

I want to be fair to the design, because parts of it are faithful. The title stated the result outright. A banner across the top carried the main finding. The center of the poster sorted a model's responses into four buckets: agreement, refusal, some other outcome, and genuine correction. Three panels underneath carries the limitations and the key take-aways, and a QR code gives anyone a direct route to the paper. So, theoretically, people who stopped by could understand the core result, and be able to understand the implications of the core results ?

![](./images/poster.png)

## What actually happened

I invited one of the poster presenters in the morning and came and gave feedback to my poster. She asked many questions on inoculation prompting me to realise that the poster version is flawed and there is additional information that I would consider including model configuration and more details of the technique, such as training details.

Four groups came by over the seventy minutes I was there: three individuals and a pair, five people in all. Each stayed ten to fifteen minutes. They nodded, and every group left saying they understood inoculation prompting **(after I used my relatively small phone, showed them this figure, and explained it)**.

![](./images/headline.png)

One left saying she would read the paper. There are also a few exchanges that include Alex, who I know from ML4G, presenting beside me, who listened for fifteen or twenty minutes because he already knew me and was interested in learning more about inoculation.

Before Saturday, I sent out numerous invitations (via Slack, email, LinkedIn DMs) for people to come and join. Only a pair came (via email invitation). One person overslept, one never received the exact time, and the others never appeared.

Part of the reason is because I have only learned the exact poster number only a day and a half before, as otherwise, I would be able to send out more accurate information including my absence and present time to do the poster presentations.

Retention was high. Once someone stopped for more than ~20 seconds, they stayed. Acquisition was the problem. Almost nobody stopped, and the reason was partly the thin Saturday aisle, partly me, the presenter beside the poster looking at his phone, or maybe I did not send out more invitations than I should be doing.

The sharpest comparison happened away from the poster. At a social event that week I described the same research to one person in a couple of sentences. He started asking questions, and the exchange ran back and forth on LinkedIn for over two days. Surely a fan of the paper as there is clear interest in alignment research and in particular emergent misalignment. There I said very little and let him lead. At the poster I said everything and left no space. From this small sample distribution, it shows that initial (verbal) word count from the presenter went up while the quality of the engagement went down.

## What I would have done and will be doing differently

* **Prepare for a technically literate audience** that's ready to dive into the details, once the poster has visually engaged and drawn them in.
* **Cut the top banner.** It repeated the title and diluted the core story that I wanted to tell.
* **Make the poster title match the paper title,** so people can directly look it up, or if they must diverge, reconcile them on the side where I attached the QR code.
* **Break the self-referential loop.** Send the draft poster to two or three people who I can trust to be giving feedback, and include their feedback into the iteration loop.
* **Having the right assumptions.** The poster aisles are roughly 3 meters wide and so the core elements just need to be read from at most 1.5 meters or 2 meters away. Design for that distance.
* **State what I actually want out of the presentation sessions,** then let that decide the strategy: how long I stand besides the poster, how I do out-reach, how I design the poster.
* **Prepare a two-minute and a five-minute pitch**, then open with the result and a question: which part interests you, the method, the problem, or the result or something else ?
* **Pause after about 1-1.5 minutes** and ask whether they would push back on any of it.
* **Put the phone away, watch faces**, and note down briefly every conversation the moment it ends.
* **Take photos !!!** I always remind myself that I need to take photos of my own presence in the poster presentations and in the conference but I always forget to do so.
