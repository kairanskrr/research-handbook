# Mindset and long-term growth

> Most of the advice on this page comes from the personal experience of computer science and machine learning researchers (blog posts, talks, lecture slides). It is advice from experienced people, not tested rules. The reasoning mostly applies across fields, and the examples come from computer science; before you use any of it, ask whether it fits your situation.

## When you need this page

- A paper got rejected, or your experiments have produced nothing for weeks, and you are starting to wonder whether you are cut out for research;
- You feel you "have no taste": you can't tell which problems are worth working on, so you wait for your advisor to hand you a topic;
- You have been busy for a long time but can't say what you have actually gotten better at this year, or you are too worn out to keep going.

This page isn't about the tasks of any one stage. It covers habits that run through the whole of research: how to train your judgment, how to deal with failure, how to build up knowledge and skill, and how to keep a pace you can sustain.

Most of the sources cited here are written with PhD students in mind (for example, "the hardest stretch is two or three years in", "a PhD is more like getting a driver's license"). Undergraduate and master's projects are much shorter, so scale accordingly: what matters is not the exact number of years but the point that failure is common and growth takes time. `[Our analysis]`

---

## 1. Cultivate research taste on purpose

**How:** Research taste is roughly the ability to choose good problems to work on[^olah2021taste-e1]. More broadly, it also covers all the judgment calls in research that have no standard answer, such as which anomaly is worth chasing or which experiment would be more convincing[^nanda2025taste-e2]. It develops slowly (see "Why" below), so the idea behind practicing it is: **get more feedback, more cheaply.** These are exercises that experienced researchers recommend, and you can start any of them today:

1. Take your list of research ideas to a mentor you respect and ask them to rate each one from 1 to 10. Where you still disagree after thinking it over, sit down and discuss it[^olah2021taste-e4].
2. Before you ask your advisor a question, guess how they will answer, then compare[^nanda2025taste-e5].
3. Before starting on an idea, write down your prediction and why you think it is good; look back once it is done[^nanda2025taste-e7].
4. When someone else tries an idea you once had, compare their results with what you expected[^olah2021taste-e5].
5. Interview researchers around you: why do they work on the problems they do, and how do they pick them[^olah2021taste-e6]?
6. Ask yourself why some ideas get built on by many people while others are quickly forgotten[^schulman2020opinionated-e5].
7. Examine the taste of the community around you. Your taste is heavily shaped by your collaborators and advisor, so look at it critically[^olah2021taste-e7].
8. When you are just starting out, favor projects that give you intermediate results fairly quickly over big bets that take a year to pay off[^nanda2025taste-e8], and finish your projects (see Section 7).

**Why:** Several experienced researchers rank the ability to pick the right problem above raw technical skill[^schulman2020opinionated-e3][^carlini2026best-e3]. Without it, you may write papers that are technically correct but that nobody reads, because you never asked whether the question was worth answering[^carlini2026best-e4].

The good news is that taste isn't mysterious: talent plays a part, but taste is mostly learned[^nanda2025taste-e1], and it is completely normal to feel you have none when you start out[^nanda2025taste-e3]. The hard part is how little feedback you get: finding out whether an idea is good often takes months, so you get only a few pieces of feedback a year[^olah2021taste-e2]. The shorter your feedback loop, the more data you get[^nanda2025taste-e4]. Each exercise above gets you extra feedback without waiting for a project to finish: every guess at your advisor's answer, every comparison with someone else's results, counts as one. `[Our analysis]`

**Where people go wrong:**

- **Thinking without doing.** Trying to pick the perfect problem before getting your hands dirty is a trap; you can't develop taste in a vacuum[^olah2021taste-e9]. Taste comes from doing research over and over while paying attention to what works and what doesn't[^carlini2026best-e5].
- **Mistaking confidence for being right.** People often feel confident in their judgment long before their intuitions actually become accurate[^nanda2025taste-e6].

> **Where sources disagree: follow your advisor, or trust your own judgment?**
>
> - **Don't defer to your advisor too much:** one researcher, looking back, said most of his mistakes came when he listened to his mentors' criticism, while his coolest work was the work everyone initially called useless or uninteresting[^olah2021taste-e15].
> - **Leaning on your advisor as a beginner is normal:** the view above suffers from survivorship bias, and people have different levels of maturity at different stages[^olah2021taste-e16]. Relying heavily on an advisor or an established research direction early in your career is normal[^nanda2025taste-e9]. There is no shame in working on ideas someone else proposed; the skill lies in which ones you pick and how well you execute them[^schulman2020opinionated-e4].
>
> In practice: when you are starting out, you can accept the direction your advisor gives you and practice your judgment within it. At the same time, write down where you disagree with your advisor and why, then check against the results later. That is exercises 2 and 3 in action. `[Our analysis]`

**Write it down:** Start a "prediction log". Before your next experiment, write one line with your prediction and the reason, for example "adding vulnerability-pattern hints to the large language model's prompt will clearly raise the detection rate for reentrancy vulnerabilities, because …". When the results are in, add to the same line what actually happened and what you learned.

## 2. Treat failure and rejection as normal

**How:**

- **Reset your expectations first.** Once you reach the point of actually pushing the boundary of knowledge, there are no ready-made steps to follow, and failure is routine `[Our analysis]`. One experienced researcher observes that two or three years into a PhD is exactly when the most people drop out[^might2010successful-e2]; to get through this period, you have to be willing to fail from the moment you wake up to the moment you go to sleep[^might2010successful-e3]. Another puts it more bluntly: if you don't fail regularly, you aren't trying hard enough things[^sutherland1996courage-e2].
- **After a rejection, look after your feelings first.** Let yourself be upset, talk to friends, labmates, or your advisor, take a day off, and then come back[^huang2021rejection-e6]. Remember that the rejection is about the idea, the implementation, the experiments, and the writing, not about you as a person[^huang2021rejection-e2]. Once you have calmed down, turn the reviews into a revision list; see [Reviews, revision, and what to do after rejection](../04_write-and-publish/03_review-and-revision.md).
- **Keep a "CV of failures"**: record your rejections and the things you didn't get, so that setbacks start to feel ordinary[^huang2021rejection-e9]. Celebrate small wins too, and use them to keep yourself motivated[^huang2021rejection-e5].
- **Look behind other people's scenes.** The publication list on a CV looks tidy, but how each paper got published is a different story[^huang2021struggle-e1]. One researcher, looking back at his papers, recalls that his first one took 3.5 years from the first message about the project to publication, and that before it came out every PhD program he applied to rejected him[^huang2021struggle-e2]. Later, the research group he led also faced frequent rejection, and keeping morale up was not easy[^huang2021struggle-e4]. His most-cited papers often received poor reviews at first or were rejected several times[^huang2021struggle-e3].

**Why:** To a newcomer, a rejection feels like a major setback, but it is just part of the normal process[^huang2021rejection-e7]. By one computer scientist's estimate from around 2010, acceptance rates at good conferences and journals range from 8% to 25%, so most or even all of your papers will be rejected; but if you stick with it long enough and work hard enough, you will get published[^might2010successful-e5].

Failure isn't wasted, either. What grows out of repeated failure is precisely research skill: the ability to come up with plausible solutions and estimate how likely each is to work[^might2010successful-e4]. Turning an idea over and over without making progress is itself the first step of the creative process[^dettmers2019creativity-e2]; accepting this long struggle through many rounds of failure as part of creating is what keeps the creative process from wearing you down[^dettmers2019creativity-e5]. External rewards such as paper acceptances are rare, so you often have to rely on intrinsic motivation to keep going[^ruder2020tips-e12].

**Where people go wrong:** Taking a rejection as a verdict on yourself; or, the opposite, resubmitting somewhere else unchanged without reading the reviews. The first hurts you; the second wastes an opportunity. `[Our analysis]`

> **Where sources disagree: persist, or let go?**
>
> - **Persist:** this phase demands perseverance in the face of uncertainty, rejection, and frustration[^might2010successful-e6]. Most great scientists are completely committed to their problem, and those who aren't seldom produce first-class work[^hamming1986you-e23].
> - **Know when to let go:** setting an idea aside for a while may be exactly the key step in creating something[^dettmers2019creativity-e3]. Academia also lacks mechanisms to help people stop old and stale projects[^sutherland1996courage-e5].
>
> In practice: be patient with the **direction**, since a few failures are normal; be flexible about the **specific approach**: if one route doesn't work, try another, or set it aside for a while. Keep a small backup idea alongside your main project, so that setting something aside doesn't feel like the end of everything (see Section 6). `[Our analysis]` For how to decide, on solid grounds, whether a particular project should continue or stop, see [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md).

**Write it down:** Create a "CV of failures" file. List the rejections, failed experiments, and ideas that went nowhere that you have been through, and after each, write one sentence on what you learned from it. From now on, every time you are rejected, add a line there first.

## 3. Build knowledge and skill like compound interest

**How:**

- **Know your own field thoroughly, and neighboring fields as well as you can**[^kidger2023know-e1]. Cultivate broad interests and look beyond your own small circle[^ruder2020tips-e7].
- **Skim widely, read deeply only a few.** Skim a large amount of work quickly to learn what is already known and what problems people are thinking about; on that basis, pick a dozen or so papers a year to read in depth[^nielsen2004principles-e15]. Reading the ten most important papers in a field in depth is almost certainly more useful than skimming five hundred[^nielsen2004principles-e12]. For how to read in layers, see [Entering a field and exploring the literature](../01_from-interest-to-project/01_enter-a-field.md).
- **Deliberately build an unusual combination of skills**[^nielsen2004principles-e11]. If you work on "large language models and smart contract security", for example, someone who understands both large language models and program analysis is more likely to spot problems others miss than someone who knows only one side. `[Our analysis]`
- **Practice deliberately at the edge of your abilities.** Experts don't become experts by talent alone or by putting in the years; they practice at the edge of their abilities[^prieto2025so-e4]. You can ask your advisor and colleagues directly: which of my research skills is weak, and how can I improve it[^prieto2025so-e5]?
- **Take reading notes.** You won't remember everything you read, but you will often want to go back to it[^wood2020five-e1].
- **Take the initiative.** Show initiative and ask questions[^patterson2001bad-e10].

**Why:** Knowledge and output compound. Of two people with exactly the same ability, the one who thinks for one extra hour a day will produce far more over a lifetime[^hamming1986you-e14]. How deep your knowledge goes determines whether you can come up with new ideas, and also whether you can recognize bad ones[^kidger2023know-e1]. Expertise is a precondition for creativity: it lets you tell which ideas hold up and which don't[^dettmers2019creativity-e1]. Luck also favors the prepared mind: sooner or later, a prepared person will find something important and do it[^hamming1986you-e22].

**Where people go wrong:**

- **Chasing as many papers as fast as possible and never investing in yourself.** The short-term payoff is tempting; the long-term cost is stagnation, staying in the same place[^nielsen2004principles-e10].
- **Expecting to catch up in a few months.** This kind of growth takes years[^kidger2023know-e2], and learning never really stops[^kidger2023know-e3].

**Write it down:** Write a one-year learning plan: three to five topics in your own field to master, one or two neighboring fields to get started in, and one weak skill you want to build up. Look back at it every quarter.

## 4. Make time to think about important problems, and dare to start

**How:**

- **Ask yourself regularly: what are the most important problems in my field?** One researcher spent every Friday afternoon for years thinking only about big questions, setting aside about 10% of his time to work out what in his field mattered and what didn't[^hamming1986you-e17]. Add the problems you come up with to your idea list; see [Finding candidate problems](../01_from-interest-to-project/02_find-problems.md).
- **Keep the main project safe; the backup can take risks.** You can have one relatively safe project and one that is riskier but could have bigger impact; the safe one makes sure you graduate[^ruder2020tips-e9].
- **Test your ambition with one question:** if someone else published this work, would you be excited[^ruder2020tips-e10]?
- **When you are afraid to start, lower the bar.** Do a fairly easy warm-up project first and carry it all the way through from beginning to end; it both teaches you and gives you courage[^sutherland1996courage-e7]. Break a big task into small pieces and tell yourself "I'm only washing the first dish"; it becomes less frightening[^sutherland1996courage-e8]. A new graduate student can start by joining a research group that is already up and running; what you do matters far less than starting to do something[^sutherland1996courage-e3].

**Why:** If you don't work on important problems, you are unlikely to do important work[^hamming1986you-e1]. And working on important problems takes courage: courage means seeing the risk and going ahead anyway[^sutherland1996courage-e1]. Experienced researchers see courage as one of the traits of successful scientists: if you believe you can do important problems, you might; if you think you can't, you almost certainly won't[^hamming1986you-e16]. Recognizing that getting started itself takes courage can also help you see which of your reasons for putting it off are really just excuses[^sutherland1996courage-e6].

**Where people go wrong:**

- **Relying on hard work alone.** Effort isn't enough; it has to be applied in the right direction[^hamming1986you-e19].
- **Either believing your ideas completely or doubting them completely.** Believe in them enough to move forward, and doubt them enough to spot their flaws[^hamming1986you-e3].

**Write it down:** Write down what you think are the three most important problems in your area, each with one sentence on why nobody has solved it yet. Spend an afternoon each month rereading and revising the list.

## 5. Don't work alone with your head down

**How:**

- **Stay connected to the outside world.** People who work with the door closed get more done in the short term, but ten years later they often don't quite know what problems are worth working on[^hamming1986you-e18].
- **Reach out to people beyond your immediate circle**, rather than dealing only with the few people right around you[^ruder2020tips-e11].
- **Learn new things together with peers.** Learning together lightens the load on each person, makes learning more enjoyable, and makes new material less intimidating[^sutherland1996courage-e4].
- **Have outsiders review your project regularly**[^patterson2001bad-e12].
- **Make yourself accountable to others.** Thinking that self-discipline is just a matter of willpower is a misunderstanding; the key is being accountable to other people[^nielsen2004principles-e9]. Working with others is one way to do that; see [Collaboration and advisors](collaboration_and_advisors.md).
- **Improve your environment yourself.** Anyone can help improve their environment, and students often underestimate how much difference they can make[^nielsen2004principles-e13]. For example, organize a reading group or seminar and talk more with your fellow students `[Our analysis]`; this kind of exchange helps you feel connected to your peers and supported[^wood2020five-e4].

**Why:** Many of the hard parts of research (unsure about a topic, rejected, stuck) are hardest to carry alone, and that is also when your view is most likely to get skewed. Outsiders can give you perspectives you can't see yourself, and can pull you up when you are down. `[Our analysis]`

**Where people go wrong:** Waiting until you have "something presentable" before showing anyone. By then, problems with the direction have often already cost you months. `[Our analysis]`

**Write it down:** Name one person outside your circle you will talk to this month (a student in another group, a faculty member in a neighboring area, an engineer who uses your research), and write down two questions you want to ask them.

## 6. Keep a pace you can sustain

**How:**

- **Look after your health and your life first.** Enthusiasm alone isn't enough; you also need to keep the rest of your life in order and stay healthy[^nielsen2004principles-e7]. Work hard, but make sure you sleep and exercise[^ruder2020tips-e16].
- **Plan your life outside research deliberately**, for example exercise, reading for fun, joining clubs, and protecting your weekends[^wood2020five-e2]. When you can see an especially demanding period coming (an intensive stretch such as fieldwork, for instance), plan in advance how you will rest afterward[^wood2020five-e3].
- **Build a support network**, and find an activity that gives you energy when things aren't going well[^ruder2020tips-e13].
- **Don't hold only one idea.** When you have just one thing to work on and it goes badly, your motivation and mood take the hit, and when you are stuck all you can do is grind[^ruder2020tips-e8]. Working on two projects at once lets you switch to the other when one is stuck[^ruder2020tips-e1]; having several ideas on hand works better than fixating on one[^dettmers2019creativity-e4]. As a beginner, first make sure one main project can be finished, then add a small side project or backup idea. `[Our analysis]`
- **Turn good practices into habits.** Excellence is not an act but a habit[^nielsen2004principles-e6]. For how to do a weekly review and plan your daily time, see [Planning and daily routines](planning_and_routines.md).

**Why:** Research is measured in years. Only a pace you can sustain lets the compounding described in Section 3 actually build up. `[Our analysis]`

**Where people go wrong:** Thinking about rest only once you can't go on. Plan how you will recover from a hard stretch before it begins; if you try to make up for it afterward, you have usually already run yourself down. `[Our analysis]`

> **Where sources disagree: how hard should you push?**
>
> - **A little more effort pays off hugely in the long run:** thinking for one extra hour a day leads to far more output over a lifetime[^hamming1986you-e14].
> - **Overextending yourself doesn't pay:** one author looks back on neglecting his health and relationships to write a book; his short-term output went up, but overall his output may well have gone down[^nielsen2004principles-e8]. Your most important resource isn't compute but your own physical and mental health[^ruder2020tips-e14].
>
> The two don't contradict each other: the first is about putting in a little more **day after day**, with the effort applied in the right direction[^hamming1986you-e19], not about burning yourself out in the short term. `[Our analysis]`

**Write it down:** Write down the time each week when you never touch research (say, all of Saturday), and how you plan to rest after the hardest stretch coming up.

## 7. Finish projects, and build skill for the long term

**How:**

- **Finish your projects.** People count the projects you finish, not the ones you start; successful projects go through an unglamorous, hard phase[^patterson2001bad-e11].
- **Early on, prioritize positions and advisors where you will learn the most**[^prieto2025so-e6]. On whether passion or skill comes first, see "Where sources disagree" below.
- **Have topic preferences, but stay flexible.** When knowledgeable people or the literature tell you another topic is more relevant and feasible, take it seriously[^prieto2025so-e1]. The ideal topic sits where three things meet: it has impact, you love it, and you are especially well suited to it[^ruder2020tips-e15].
- **Change direction periodically to avoid going stale.** One suggestion is to make a major change of direction about every seven years[^hamming1986you-e21].
- **Think about your long-term goal:** what kind of researcher do I want to be[^nielsen2004principles-e14]? There is no rush to find your life's mission; good missions often take years of trial and error to find. A PhD is more about "getting the driver's license" than making the "best lap of your life"[^prieto2025so-e2].

**Why:** Finishing projects is how people learn to pick good problems and find simple solutions[^patterson2001bad-e11]; taste is acquired through feedback and through finishing projects[^patterson2001bad-e7]. The more important output of a PhD is not the papers but a better you[^ruder2020tips-e16]. Papers go out of date; your skills and judgment stay with you. `[Our analysis]`

**Where people go wrong:** Switching topics as soon as you hit the unglamorous, hard phase. Every successful project goes through it[^patterson2001bad-e11]; if you switch every time you get there, you never finish anything. `[Our analysis]`

> **Where sources disagree: passion first, or skill first?**
>
> - **Follow your interest:** the most natural way to stay positive is to work on what excites you and follow your curiosity; when you can't choose your own topic, find an angle within it that excites you[^ruder2020tips-e17].
> - **Skill first:** another view is that the key to a good career is rare and valuable skills, not passion you already have beforehand. In a PhD, that means deliberate practice at the edge of your abilities and prioritizing positions and advisors where you will learn the most[^prieto2025so-e3][^prieto2025so-e4][^prieto2025so-e6].
>
> In practice: within whatever choice you have, find an angle that excites you, while putting most of your energy into building skill. Interest often grows as you get better at something. `[Our analysis]`

**Write it down:** List every project you have started, and mark each "finished", "continue", or "stop". For each one marked "continue", write down the last step still missing before it counts as finished.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Feeling you "have no taste" and waiting for it to grow by itself | Taste is mostly learned; you have to go looking for feedback[^nanda2025taste-e1][^nanda2025taste-e4] |
| Holding out for the perfect problem and never starting | You can't develop taste in a vacuum[^olah2021taste-e9] |
| Taking a rejection as a verdict on yourself | Rejection is about the work, and it is routine[^huang2021rejection-e2][^huang2021rejection-e7] |
| Having only one idea and no backup | When stuck, all you can do is grind, and your motivation and mood suffer[^ruder2020tips-e8] |
| Chasing as many papers as fast as possible and never investing in yourself | In the long run you stagnate[^nielsen2004principles-e10] |
| Always working with the door closed | Ten years later you may not know what problems are worth working on[^hamming1986you-e18] |
| Relying on hard work alone without thinking about direction | Effort has to be applied in the right direction[^hamming1986you-e19] |
| Wearing down your health for short-term output | Your overall output may actually drop[^nielsen2004principles-e8] |
| Starting many projects and finishing none | People count the projects you finish[^patterson2001bad-e11] |
| Waiting to find your "true passion" before committing | One view holds that the key to a good career is skill, not passion you already have beforehand[^prieto2025so-e3]; passion often appears only after your skills have grown `[Our analysis]` |

## Further reading

- **Olah, "Research Taste Exercises":** concrete exercises for building taste and several failure modes, with many people's additional suggestions collected at the end.
- **Nanda, "Understanding and Cultivating Research Taste":** what research taste is made of and how to shorten the feedback loop; examples from machine learning.
- **Hamming, "You and Your Research":** important problems, courage, working with the door open, and compounding; worth rereading every few years.
- **Sutherland, "Technology and Courage":** the different kinds of courage it takes to start, persist, and stop, and concrete ways to lower the bar.
- **Nielsen, "Principles of Effective Research":** how to balance output with investing in yourself, and how to make your environment work for you.
- **Jeff Huang, "The struggle for each paper"; Jia-Bin Huang's Twitter thread on rejection:** read when you are low after a rejection (they are two different researchers).
- **Might, "3 qualities of successful Ph.D. students":** why the middle of a PhD is the hardest stretch, and what kind of perseverance it takes.

[^olah2021taste-e1]: Olah 2021, opening section. [Evidence](../../sources/notes/olah2021taste.md#e1)
[^olah2021taste-e2]: Olah 2021, opening section. [Evidence](../../sources/notes/olah2021taste.md#e2)
[^olah2021taste-e4]: Olah 2021, Exercise 1. [Evidence](../../sources/notes/olah2021taste.md#e4)
[^olah2021taste-e5]: Olah 2021, Exercise 2. [Evidence](../../sources/notes/olah2021taste.md#e5)
[^olah2021taste-e6]: Olah 2021, Exercise 3. [Evidence](../../sources/notes/olah2021taste.md#e6)
[^olah2021taste-e7]: Olah 2021, Exercise 5. [Evidence](../../sources/notes/olah2021taste.md#e7)
[^olah2021taste-e9]: Olah 2021, Failure mode 2. [Evidence](../../sources/notes/olah2021taste.md#e9)
[^olah2021taste-e15]: Olah 2021, Christian Szegedy's view collected at the end. [Evidence](../../sources/notes/olah2021taste.md#e15)
[^olah2021taste-e16]: Olah 2021, Olah's comment on Szegedy. [Evidence](../../sources/notes/olah2021taste.md#e16)
[^nanda2025taste-e1]: Nanda 2025, Introduction. [Evidence](../../sources/notes/nanda2025taste.md#e1)
[^nanda2025taste-e2]: Nanda 2025, What is research taste? [Evidence](../../sources/notes/nanda2025taste.md#e2)
[^nanda2025taste-e3]: Nanda 2025, Where does taste come from? [Evidence](../../sources/notes/nanda2025taste.md#e3)
[^nanda2025taste-e4]: Nanda 2025, How to learn it? [Evidence](../../sources/notes/nanda2025taste.md#e4)
[^nanda2025taste-e5]: Nanda 2025, How to learn it? [Evidence](../../sources/notes/nanda2025taste.md#e5)
[^nanda2025taste-e6]: Nanda 2025, Conviction & Confidence. [Evidence](../../sources/notes/nanda2025taste.md#e6)
[^nanda2025taste-e7]: Nanda 2025, Conviction & Confidence. [Evidence](../../sources/notes/nanda2025taste.md#e7)
[^nanda2025taste-e8]: Nanda 2025, Cultivating Research Taste. [Evidence](../../sources/notes/nanda2025taste.md#e8)
[^nanda2025taste-e9]: Nanda 2025, Conclusion. [Evidence](../../sources/notes/nanda2025taste.md#e9)
[^schulman2020opinionated-e3]: Schulman 2020, Honing Your Taste. [Evidence](../../sources/notes/schulman2020opinionated.md#e3)
[^schulman2020opinionated-e4]: Schulman 2020, Honing Your Taste. [Evidence](../../sources/notes/schulman2020opinionated.md#e4)
[^schulman2020opinionated-e5]: Schulman 2020, Honing Your Taste. [Evidence](../../sources/notes/schulman2020opinionated.md#e5)
[^carlini2026best-e3]: Carlini 2026, Have good taste for problems. [Evidence](../../sources/notes/carlini2026best.md#e3)
[^carlini2026best-e4]: Carlini 2026, Have good taste for problems. [Evidence](../../sources/notes/carlini2026best.md#e4)
[^carlini2026best-e5]: Carlini 2026, Have good taste for problems. [Evidence](../../sources/notes/carlini2026best.md#e5)
[^patterson2001bad-e7]: Patterson 2001, p. 42. [Evidence](../../sources/notes/patterson2001bad.md#e7)
[^patterson2001bad-e10]: Patterson 2001, summary of advice for graduate school. [Evidence](../../sources/notes/patterson2001bad.md#e10)
[^patterson2001bad-e11]: Patterson 2001, "4) Finishing a project". [Evidence](../../sources/notes/patterson2001bad.md#e11)
[^patterson2001bad-e12]: Patterson 2001, "3) Running a project". [Evidence](../../sources/notes/patterson2001bad.md#e12)
[^might2010successful-e2]: Might 2010, Perseverance. [Evidence](../../sources/notes/might2010successful.md#e2)
[^might2010successful-e3]: Might 2010, Perseverance. [Evidence](../../sources/notes/might2010successful.md#e3)
[^might2010successful-e4]: Might 2010, Perseverance. [Evidence](../../sources/notes/might2010successful.md#e4)
[^might2010successful-e5]: Might 2010, Perseverance. [Evidence](../../sources/notes/might2010successful.md#e5)
[^might2010successful-e6]: Might 2010, Perseverance. [Evidence](../../sources/notes/might2010successful.md#e6)
[^sutherland1996courage-e1]: Sutherland 1996, §1.1. [Evidence](../../sources/notes/sutherland1996courage.md#e1)
[^sutherland1996courage-e2]: Sutherland 1996, §2.6. [Evidence](../../sources/notes/sutherland1996courage.md#e2)
[^sutherland1996courage-e3]: Sutherland 1996, §2.2. [Evidence](../../sources/notes/sutherland1996courage.md#e3)
[^sutherland1996courage-e4]: Sutherland 1996, §2.2. [Evidence](../../sources/notes/sutherland1996courage.md#e4)
[^sutherland1996courage-e5]: Sutherland 1996, §2.5. [Evidence](../../sources/notes/sutherland1996courage.md#e5)
[^sutherland1996courage-e6]: Sutherland 1996, §3.1. [Evidence](../../sources/notes/sutherland1996courage.md#e6)
[^sutherland1996courage-e7]: Sutherland 1996, §3.3. [Evidence](../../sources/notes/sutherland1996courage.md#e7)
[^sutherland1996courage-e8]: Sutherland 1996, §3.4. [Evidence](../../sources/notes/sutherland1996courage.md#e8)
[^huang2021rejection-e2]: Jia-Bin Huang 2021, [tweet thread](https://twitter.com/jbhuang0604/status/1443248831102136333), tweet 4. [Evidence](../../sources/notes/huang2021rejection.md#e2)
[^huang2021rejection-e5]: Jia-Bin Huang 2021, [tweet thread](https://twitter.com/jbhuang0604/status/1443248831102136333), tweet 7. [Evidence](../../sources/notes/huang2021rejection.md#e5)
[^huang2021rejection-e6]: Jia-Bin Huang 2021, [tweet thread](https://twitter.com/jbhuang0604/status/1443248831102136333), tweet 2. [Evidence](../../sources/notes/huang2021rejection.md#e6)
[^huang2021rejection-e7]: Jia-Bin Huang 2021, [tweet thread](https://twitter.com/jbhuang0604/status/1443248831102136333), tweet 3. [Evidence](../../sources/notes/huang2021rejection.md#e7)
[^huang2021rejection-e9]: Jia-Bin Huang 2021, [tweet thread](https://twitter.com/jbhuang0604/status/1443248831102136333), tweet 6. [Evidence](../../sources/notes/huang2021rejection.md#e9)
[^huang2021struggle-e1]: Jeff Huang 2021, opening. [Evidence](../../sources/notes/huang2021struggle.md#e1)
[^huang2021struggle-e2]: Jeff Huang 2021, the story of the first paper. [Evidence](../../sources/notes/huang2021struggle.md#e2)
[^huang2021struggle-e3]: Jeff Huang 2021, closing. [Evidence](../../sources/notes/huang2021struggle.md#e3)
[^huang2021struggle-e4]: Jeff Huang 2021, closing. [Evidence](../../sources/notes/huang2021struggle.md#e4)
[^dettmers2019creativity-e1]: Dettmers 2019, middle of the main text. [Evidence](../../sources/notes/dettmers2019creativity.md#e1)
[^dettmers2019creativity-e2]: Dettmers 2019, middle of the main text. [Evidence](../../sources/notes/dettmers2019creativity.md#e2)
[^dettmers2019creativity-e3]: Dettmers 2019, middle of the main text. [Evidence](../../sources/notes/dettmers2019creativity.md#e3)
[^dettmers2019creativity-e4]: Dettmers 2019, middle of the main text. [Evidence](../../sources/notes/dettmers2019creativity.md#e4)
[^dettmers2019creativity-e5]: Dettmers 2019, middle of the main text. [Evidence](../../sources/notes/dettmers2019creativity.md#e5)
[^ruder2020tips-e1]: Ruder 2020, 2) Work on two things. [Evidence](../../sources/notes/ruder2020tips.md#e1)
[^ruder2020tips-e7]: Ruder 2020, 1) Read broadly. [Evidence](../../sources/notes/ruder2020tips.md#e7)
[^ruder2020tips-e8]: Ruder 2020, 2) Work on two things. [Evidence](../../sources/notes/ruder2020tips.md#e8)
[^ruder2020tips-e9]: Ruder 2020, 3) Be ambitious. [Evidence](../../sources/notes/ruder2020tips.md#e9)
[^ruder2020tips-e10]: Ruder 2020, 3) Be ambitious. [Evidence](../../sources/notes/ruder2020tips.md#e10)
[^ruder2020tips-e11]: Ruder 2020, 5) Be proactive. [Evidence](../../sources/notes/ruder2020tips.md#e11)
[^ruder2020tips-e12]: Ruder 2020, 7) Keep a source of positive energy. [Evidence](../../sources/notes/ruder2020tips.md#e12)
[^ruder2020tips-e13]: Ruder 2020, 7) Keep a source of positive energy. [Evidence](../../sources/notes/ruder2020tips.md#e13)
[^ruder2020tips-e14]: Ruder 2020, 7) Keep a source of positive energy. [Evidence](../../sources/notes/ruder2020tips.md#e14)
[^ruder2020tips-e15]: Ruder 2020, 8) Play to your strengths. [Evidence](../../sources/notes/ruder2020tips.md#e15)
[^ruder2020tips-e16]: Ruder 2020, 10) Play the long game. [Evidence](../../sources/notes/ruder2020tips.md#e16)
[^ruder2020tips-e17]: Ruder 2020, 7) Keep a source of positive energy. [Evidence](../../sources/notes/ruder2020tips.md#e17)
[^hamming1986you-e1]: Hamming 1986, section on important problems. [Evidence](../../sources/notes/hamming1986you.md#e1)
[^hamming1986you-e3]: Hamming 1986, section on ambiguity. [Evidence](../../sources/notes/hamming1986you.md#e3)
[^hamming1986you-e14]: Hamming 1986, Bode's remark. [Evidence](../../sources/notes/hamming1986you.md#e14)
[^hamming1986you-e16]: Hamming 1986, section on courage. [Evidence](../../sources/notes/hamming1986you.md#e16)
[^hamming1986you-e17]: Hamming 1986, summary section. [Evidence](../../sources/notes/hamming1986you.md#e17)
[^hamming1986you-e18]: Hamming 1986, section on open door. [Evidence](../../sources/notes/hamming1986you.md#e18)
[^hamming1986you-e19]: Hamming 1986, section on drive. [Evidence](../../sources/notes/hamming1986you.md#e19)
[^hamming1986you-e21]: Hamming 1986, Q&A section. [Evidence](../../sources/notes/hamming1986you.md#e21)
[^hamming1986you-e22]: Hamming 1986, section on luck. [Evidence](../../sources/notes/hamming1986you.md#e22)
[^hamming1986you-e23]: Hamming 1986, section on emotional commitment. [Evidence](../../sources/notes/hamming1986you.md#e23)
[^kidger2023know-e1]: Kidger 2023, opening. [Evidence](../../sources/notes/kidger2023know.md#e1)
[^kidger2023know-e2]: Kidger 2023, closing. [Evidence](../../sources/notes/kidger2023know.md#e2)
[^kidger2023know-e3]: Kidger 2023, closing. [Evidence](../../sources/notes/kidger2023know.md#e3)
[^nielsen2004principles-e6]: Nielsen 2004, opening section. [Evidence](../../sources/notes/nielsen2004principles.md#e6)
[^nielsen2004principles-e7]: Nielsen 2004, Integrating research into the rest of your life. [Evidence](../../sources/notes/nielsen2004principles.md#e7)
[^nielsen2004principles-e8]: Nielsen 2004, Integrating research into the rest of your life. [Evidence](../../sources/notes/nielsen2004principles.md#e8)
[^nielsen2004principles-e9]: Nielsen 2004, Self-discipline. [Evidence](../../sources/notes/nielsen2004principles.md#e9)
[^nielsen2004principles-e10]: Nielsen 2004, Aspects of research. [Evidence](../../sources/notes/nielsen2004principles.md#e10)
[^nielsen2004principles-e11]: Nielsen 2004, Developing research strengths. [Evidence](../../sources/notes/nielsen2004principles.md#e11)
[^nielsen2004principles-e12]: Nielsen 2004, Developing research strengths. [Evidence](../../sources/notes/nielsen2004principles.md#e12)
[^nielsen2004principles-e13]: Nielsen 2004, Develop a high-quality research environment. [Evidence](../../sources/notes/nielsen2004principles.md#e13)
[^nielsen2004principles-e14]: Nielsen 2004, Vision. [Evidence](../../sources/notes/nielsen2004principles.md#e14)
[^nielsen2004principles-e15]: Nielsen 2004, Developing research strengths. [Evidence](../../sources/notes/nielsen2004principles.md#e15)
[^prieto2025so-e1]: Prieto 2025, "passion trap" section. [Evidence](../../sources/notes/prieto2025so.md#e1)
[^prieto2025so-e2]: Prieto 2025, section on "mission". [Evidence](../../sources/notes/prieto2025so.md#e2)
[^prieto2025so-e3]: Prieto 2025, "rare and valuable skills" section. [Evidence](../../sources/notes/prieto2025so.md#e3)
[^prieto2025so-e4]: Prieto 2025, section on deliberate practice. [Evidence](../../sources/notes/prieto2025so.md#e4)
[^prieto2025so-e5]: Prieto 2025, section on deliberate practice. [Evidence](../../sources/notes/prieto2025so.md#e5)
[^prieto2025so-e6]: Prieto 2025, "control traps" section. [Evidence](../../sources/notes/prieto2025so.md#e6)
[^wood2020five-e1]: Wood 2020, Tip 1. [Evidence](../../sources/notes/wood2020five.md#e1)
[^wood2020five-e2]: Wood 2020, Tip 4. [Evidence](../../sources/notes/wood2020five.md#e2)
[^wood2020five-e3]: Wood 2020, Tip 4. [Evidence](../../sources/notes/wood2020five.md#e3)
[^wood2020five-e4]: Wood 2020, Tip 5. [Evidence](../../sources/notes/wood2020five.md#e4)
