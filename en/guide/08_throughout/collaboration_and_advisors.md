# Collaboration and advisors

> The ideas on this page apply to every field; the examples and concrete practices come from computer science. Most sources are personal accounts by advisors and researchers in computer science and machine learning, usually about PhD students and their advisors; we keep only the parts that apply equally to master's students, undergraduate researchers and other fields. What follows is advice, not rules: every advisor works differently, and whatever you agree with yours takes precedence `[Our analysis]`.

## When you need this page

- You have just joined a group and don't know how often your advisor wants updates, or in what form;
- You are meeting your advisor next week, the results are bad, and you don't know how to bring it up;
- You are about to work on a project with labmates or people outside your group, and you worry that division of work and authorship will be unclear.

This page is about how to work with your advisor, labmates and collaborators throughout a project. Choosing an advisor is outside its scope. For getting your research plan agreed with your advisor, see [Writing a research plan](../02_do-the-project/03_research-plan.md#6-get-your-advisor-on-board-with-the-plan); for research misconduct and authorship norms, see [Research integrity and ethics](integrity_and_ethics.md).

---

## 1. Ask how your advisor supervises, and tell them about yourself

**How:**

- **Ask your advisor directly how they supervise students and what they expect, and ask the senior students in the group too**[^dredze2012successful-e7]. Three concrete things to ask: how often you will meet; in what form and where to send results; what they want from you at this stage `[Our analysis]`.
- **Tell your advisor about yourself as well**: your work habits and preferences, so they understand you better and the collaboration runs more smoothly[^dredze2012successful-e15].
- **If you want to know how you are doing, ask your advisor; don't guess by comparing yourself with others**[^dredze2012successful-e23]. If you feel you are not meeting expectations, raise it with your advisor yourself and work out the cause and a plan together[^vinitskyexpectation-e2].

**Why:**

- Your relationship with your advisor may be the most important one in graduate school[^dredze2012successful-e6]. It is a two-way relationship: you have your goals, and your advisor has their own goals, constraints and career to manage[^karpathy2016survival-e1]. It helps a lot to understand what drives your advisor and what constrains them[^karpathy2016survival-e2].
- Advisors' styles vary widely: some micromanage the details of your work, others are almost entirely hands-off[^karpathy2016survival-e3]. If you don't ask, you can only guess.
- Newcomers find it hard to know what "doing well" looks like in the first year or two. Once expectations are clear, you are neither crushed by imagined standards nor underestimating how much work is needed[^vinitskyexpectation-e1].

**One example:** Vinitsky wrote a year-by-year statement of expectations for the students in his group, and by year three it says plainly: "By this point you're setting the direction, not me."[^vinitskyexpectation-e4] In other words, relying heavily on your advisor at the start is normal, and over time you take the lead (see Section 4) `[Our analysis]`.

**Where people go wrong:** Not asking anything for fear of looking naive, then either working yourself to the bone or coasting, based on standards you imagined `[Our analysis]`.

**Write it down:** After your first long conversation, write a few lines covering the meeting frequency, the update format and the expectations for this stage that you agreed on, and send them to your advisor to confirm. If your advisor has no such document, these lines are your agreement `[Our analysis]`.

## 2. Make every meeting count

**Before the meeting:**

- **Send results as you get them; don't save them for the meeting.** If your advisor sees results for the first time in the meeting, there is no time to understand and think about them[^huang2023advisor-e1]. When you have results, share and discuss them often outside meetings[^huang2023advisor-e2]. Put your research into a form your advisor can easily read; don't expect them to sit down and go through your research notes with you[^vinitskyexpectation-e3].
- **Make an agenda.** If you don't know what you want to discuss, your advisor certainly won't[^dredze2012successful-e12].

**In the meeting:**

1. **Start with a summary.** What you agreed to do last time, what you did, and what you want to discuss today[^huang2023advisor-e4]. Your advisor juggles many projects and, unlike you, hasn't been thinking about this one all week; they need to switch context[^dredze2012successful-e14].
2. **Bring results, and interpret them.** Bring figures and tables whenever you can[^dredze2012successful-e13], but put the results in context[^huang2023advisor-e5]: what you did, why, what you saw, and whether it matched what you expected `[Our analysis]`.
3. **Drive the meeting yourself**, and make sure everything on the agenda gets covered[^huang2023advisor-e3].
4. **End by proposing next steps.** Based on the results, propose a few prioritized things to do, with reasons[^huang2023advisor-e6][^perez2024tips-e6].

**After the meeting:** Right away, write up what was discussed and the agreed next steps, and send it by email or chat[^huang2023advisor-e7].

**How often:** Meet regularly, for example once a week, especially when you don't feel like it[^dredze2012successful-e11]. Advisors are usually busy, so make full use of the time you get[^halimtips-e4].

**An example opening** `[Our analysis]` ("large language models and smart contract security"):

> Last week we agreed I would check two things: how much of the detection rate is left after removing samples that may be leaked, and whether the conclusion holds with a different model. I posted the results in the group chat yesterday. In short: the detection rate drops from 82% to 51%, and both models show the same trend. Today I'd like to discuss three things: whether the results are trustworthy, whether to enlarge the sample, and the priorities for next steps.

(The numbers are made up, just to show the format.)

**Where people go wrong:** Putting up a table of numbers and saying "have a look"; or ending by asking your advisor "what should I do next?", handing them the plan you should have proposed `[Our analysis]`.

**Write it down:** Before your next meeting, write an opening of no more than five lines in the format above: what you agreed last time, what you did, the main results, what you want to discuss today, and the next steps you propose.

## 3. Report progress early, including bad news

**How:**

- **Don't hide from your advisor.** One advisor puts it bluntly: "Please don't hide from me. Let's talk." He likes students who come to him and insist on talking[^freeman2013research-e10].
- **Report failures too, and be specific.** Your advisors have more experience than you and want to help, but you have to help them help you[^huang2023unstuck-e7]: if you only describe in words why you did something, how and what you did, it is hard for anyone to follow fully[^huang2023unstuck-e8]. Show a pipeline diagram and actual inputs and outputs `[Our analysis]`. For how to pin down where you are stuck, see [Running and iterating](../02_do-the-project/06_run-and-iterate.md).
- **"Progress" covers more than you think.** Advisors can take a broad view of progress[^freeman2013research-e9]: figuring out why a method doesn't work, or simplifying the problem until something runs, are both worth reporting `[Our analysis]`.
- **If you are falling behind, say so early.** If you think you'll miss a deadline, tell your advisor; they would much rather know early[^dredze2012successful-e20].
- **If you notice you are making slow progress, ask for help promptly; there is nothing embarrassing about it**[^perez2024tips-e7]. People who ask questions and ask for help learn faster and get more done than those who try to figure everything out alone[^dredze2012successful-e19].
- **If an important email gets no reply, send a polite reminder.** But first make sure your email was clear[^dredze2012successful-e9].

**Why:** Your advisor has experience and wants to help, but only if they know where you are stuck (see above). Some advisors count "proactively and transparently raising the problems you run into" as one of the measures of how well a student is doing[^perez2024tips-e8].

**Where people go wrong:** Waiting until you "have good results" before seeing your advisor, so the gap grows longer and the problems pile up `[Our analysis]`.

**Write it down:** Pick the one thing you feel least sure about right now. Write down where it is stuck, what you have tried, and what you need from your advisor. Bring it to your next meeting.

## 4. The project is yours: propose the next steps

**How:**

- **When you meet your advisor, have the agreed tasks done, and ideally have the next step worked out or even started**; don't wait for your advisor to cut tasks into small pieces and feed them to you[^herremans2020successful-e6].
- **If you are waiting for your advisor to tell you what to do, something is wrong.** If you really have no idea, find something to do, such as reading papers[^dredze2012successful-e16].
- **When your advisor's idea doesn't work, don't just report the failure.** Look around the original idea for something that does work, and bring that to the meeting[^freeman2013research-e8]. In some advisors' eyes, the ideal student comes back a week later with not just what was suggested, but an improvement on it in some unexpected direction[^karpathy2016survival-e4].

**Why:** Your advisor can't, and shouldn't, solve your problem for you, or even define it for you[^kuroseadvice-e1]. You know more about your specific problem than your advisor does, sometimes enough to make better decisions than a senior researcher[^nanda2025mindsets-e15]. That doesn't mean a newcomer should set the direction alone from day one: relying heavily on your advisor's guidance early in your career is normal and expected[^nanda2025taste-e9].

> **Where sources disagree: how far should you follow your advisor's advice?**
>
> - **Follow it:** Your advisor isn't always right, but has been doing research longer than you; and your advisor is your boss, so when they tell you to do something, do it[^dredze2012successful-e8].
> - **Sometimes don't:** When you are convinced your advisor is wrong, have the courage to sometimes go against them[^karpathy2016survival-e6]. But the same author admits that once he ignored his advisor, the advisor turned out to be right, and he wasted months[^karpathy2016survival-e7].
>
> In practice `[Our analysis]`: **do what your advisor explicitly asks first; when you disagree, let evidence do the talking.** Bring your reasons and a small-scale test result to a meeting and discuss it; don't change direction behind their back. If you really want to pursue your own direction, agree with your advisor in advance on how long you will try it and what result will make you stop.

**Where people go wrong:** Taking "being proactive" to mean "changing direction without consulting your advisor". Being proactive means proposing a plan first, not going around your advisor `[Our analysis]`.

**Write it down:** For what you are working on now, write down your proposed next steps (at most three, in order), each with a one-sentence reason.

## 5. Working with peers and people outside your group

**How:**

- **Start with the senior students or postdocs in your group.** You will probably work with them, and they play a role much like your advisor's[^karpathy2016survival-e5]. When you first join, find a senior student whose project interests you and offer to help[^dredze2012successful-e18]. When you pair up with a senior member like this, communicate with them often day to day and report to your advisor at bigger milestones, to stay on track[^herremans2020successful-e2].
- **Talk about research often with students inside and outside your group.** This tells you whether your expectations of yourself are realistic, and you pick up implementation details, ways of thinking and all kinds of tricks[^dredze2012successful-e17]. Meeting people, listening and collaborating is how you become part of the research community[^kuroseadvice-e2].
- **Collaborate with people other than your advisor too.** Working with others brings new perspectives and teaches you more than working alone[^ruder2020tips-e5]. Collaboration is a skill you will certainly need later[^ruder2020tips-e3].
- **Set expectations at the start of a collaboration and communicate clearly, especially when working remotely**[^ruder2020tips-e4]. At minimum, agree on who is responsible for which part, how often you sync, and how authorship will be handled (see Section 6) `[Our analysis]`.

**Why:** Researchers rarely face outside pressure to deliver results right away; one key to self-discipline is being accountable to others, and both collaborating with colleagues and building mentoring relationships provide that[^nielsen2004principles-e5]. See also [Mindset and long-term growth](mindset_and_growth.md).

> **Where sources disagree: should you share your ideas fully with collaborators?**
>
> - **Share a lot:** Within a lab, people should collaborate, not compete[^herremans2020successful-e5].
> - **Be careful outside:** When talking with outside researchers, revealing too many unpublished ideas can put your own degree at risk, so you may prefer to discuss published papers[^halimtips-e1]; if the other person doesn't credit you as the originator of an idea, you could lose the idea, or even your thesis topic[^halimtips-e2].
>
> In practice `[Our analysis]`: share fully within your group and with established collaborators; with outside researchers you have just met, talk about published work first. Keep a record of discussions of important ideas in your log or in email.

**Where people go wrong:** Not discussing who does what at the start because it feels awkward, then finding halfway through that each of you thought the other was doing a certain part `[Our analysis]`.

**Write it down:** For each collaborative project, make a small table: members, what each is responsible for, how often you sync, and the author order agreed so far. Send it to all members to confirm.

## 6. Authorship: discuss it at the start and adjust as you go

**How:**

Two sets of rules are cited below: the authorship recommendations of the International Committee of Medical Journal Editors (ICMJE), written for medical journals; and the European Code of Conduct for Research Integrity from ALLEA (All European Academies), Europe's research integrity code. The authorship rules of the two main computer science publishers are listed separately after this list. Our sources do not cover whether a particular conference or journal has additional rules; follow the rules of the venue you submit to `[Our analysis]`.

- **Discuss who will be an author, and in what order, when the work starts.** The medical journals' authorship recommendations suggest deciding who qualifies as an author ideally when planning the study, and adjusting as the work progresses[^icmje2026recommendations-e4]. The European code requires the authors to agree formally on author order[^allea2023european-e8].
- **Decide who should be an author by criteria.** The European code gives four criteria: a significant contribution to the study design, data collection, analysis or interpretation; drafting the paper or critically reviewing it; approving the final version; and agreeing to be responsible for the content[^allea2023european-e7]. A significant contribution can be programming, coming up with the idea, revising, supervising and so on; don't add friends who didn't contribute as authors[^herremans2020successful-e4]. The medical journals' recommendations also state that acquiring funding, general supervision of a research group, or language editing alone do not qualify someone for authorship[^icmje2026recommendations-e7].
- **People who contributed but don't qualify as authors go in the acknowledgments.** The European code names collaborators, assistants and funders[^allea2023european-e8]. Be generous with credit and thanks[^ruder2020tips-e6].
- **Before submission, every author must have read the final manuscript**[^herremans2020successful-e4].
- **Give your co-authors time.** Notify all co-authors well ahead of submission; for a conference paper, send the draft out at least two weeks in advance so senior co-authors can make time for it[^herremans2020successful-e1]. In journal-centered fields, the equivalent points are before submission and before submitting a revised manuscript `[Our analysis]`.
- **If you can't agree.** The medical journals' authorship recommendations state that when authors can't agree on who qualifies, the institution where the work was done should investigate, not the journal editor[^icmje2026recommendations-e5]. Our sources do not cover each institution's procedures.

**What the two computer science publishers require.**

- **ACM (Association for Computing Machinery)**: its authorship policy (version updated September 16, 2025) applies to all ACM journals, conferences, magazines and books[^acm2025authorship-e1]. Every author must meet all of these: be an identifiable human being; have made a substantial intellectual contribution to the work (such as conception, design or analysis) and taken part in drafting or revising the manuscript; and take responsibility for the full published content[^acm2025authorship-e2]. Everyone who qualifies should be listed as an author; gift authorship, guest authorship, ghost authorship and purchased authorship are all clear violations[^acm2025authorship-e3]. People whose contributions don't qualify them for authorship go in the acknowledgments, with what each did, ideally using CRediT role names (a standard taxonomy of contributor roles)[^acm2025authorship-e4]; generative artificial intelligence cannot be an author, and any content generated with it must be fully disclosed in the paper[^acm2025authorship-e5].
- **IEEE (Institute of Electrical and Electronics Engineers)**: its publications operations manual (revision of June 2026) requires authors to meet all three of: an important intellectual contribution to at least one of theoretical development, system or experimental design, prototype development, or the analysis and interpretation of data[^ieee2026pspb-e6]; taking part in drafting the paper or revising its content; and approving the final accepted version, including the references[^ieee2026pspb-e7].

**Author order differs between fields.** For example, economics conventionally orders authors alphabetically by surname[^einav2006surname-e1], while psychology orders them by contribution[^einav2006surname-e3]. For each field's conventions, see the field overviews, for example [Economics](../07_fields/economics/README.md#alphabetical-authorship), [Mathematics](../07_fields/mathematics/README.md#one-person-or-a-few-listed-alphabetically), [Sociology](../07_fields/sociology/README.md#authorship), [Education](../07_fields/education/README.md), [History and archaeology](../07_fields/history-archaeology/README.md) and [Physical sciences](../07_fields/physical-sciences/README.md#authorship). In computer science, IEEE does not prescribe author order; the authors decide it themselves[^ieee2026pspb-e8]. We found only one set of statistics: Waltman (2012) analyzed multi-author papers indexed in Web of Science[^waltman2012empirical-e2], comparing journal subject categories over 2007–2011[^waltman2012empirical-e3]. In the "Computer science, theory & methods" journal category, 48.6% of papers list authors in alphabetical order of surname; after using a model to subtract cases that are alphabetical by chance, about 32.6% are estimated to be intentionally alphabetical[^waltman2012empirical-e5][^waltman2012empirical-e4]. The paper lists all 25 categories with at least 15% intentional alphabetical ordering[^waltman2012empirical-e9], and this is the only computer science category among them, so all other computer science categories are below 15%. For details, see [Theory](../07_fields/computer-science/subfields/theory.md#conventions-specific-to-this-area). Our sources do not cover how other areas of computer science order authors by contribution, or where the advisor is usually placed; ask your advisor when you join the group `[Our analysis]`. For integrity requirements on authorship and citation, see [Research integrity and ethics](integrity_and_ethics.md).

**Why:** The longer you wait, the further apart people's memories of who contributed what, and their expectations, drift, and the harder it is to agree `[Our analysis]`.

**Where people go wrong:** Assuming "we'll follow the usual convention" without saying it out loud; or handing out authorship as a favor `[Our analysis]`.

**Write it down:** Keep a "who did what" column in your project log and add a line after each milestone. When authorship comes up, use it as your record `[Our analysis]`.

## 7. Ask for feedback

**How:**

- **Ask for feedback regularly.** There is no harm in asking your advisor for feedback often, say once a semester[^dredze2012successful-e10].
- **Finish drafts early.** Finish a paper at least a week before the deadline, so your advisor can give useful comments; they often have several other papers to read before the same deadline[^dredze2012successful-e21]. For journal submissions with no fixed deadline, give your advisor the same amount of time `[Our analysis]`. Proofread carefully yourself before sending[^herremans2020successful-e3], so readers can spend their time on the research `[Our analysis]`.
- **After every talk, including practice talks in your group, ask the audience**: was it clear, and how could the content, style and delivery be improved[^dredze2012successful-e22].
- **When in doubt, talk to someone.** Talking to other researchers, especially your advisor, is a good way to get a fresh perspective[^nanda2025mindsets-e16]. When you are unsure what to work on, ask experienced people for suggestions; there is no shame in working on someone else's idea[^schulman2020opinionated-e4]. To develop your sense of which problems are good, ask your advisor to score your list of ideas one by one, then discuss the ones where you disagree most[^olah2021taste-e4]; see [Judging and screening ideas](../01_find-a-problem/04_judge-and-screen.md#3-if-you-arent-sure-ask-your-advisor-to-score-them) for how.

**Where people go wrong:** Only going to people when something has gone wrong; or sending a draft the night before the deadline, which amounts to not asking for feedback at all `[Our analysis]`.

**Write it down:** Mark the next point where you will get feedback in your calendar (your next group meeting talk, the internal deadline for your next draft), and note whom you will ask and what.

---

## Common mistakes

| Mistake | Why it's a problem | What to do instead |
|---|---|---|
| Saving a week's results to show your advisor for the first time in the meeting | Your advisor has no time to understand and think about them[^huang2023advisor-e1] | Send results as you get them (Section 2) |
| Showing only a table in the meeting, or just saying "it doesn't work" | Others can hardly tell what you did[^huang2023unstuck-e8] | Put the results in context (Sections 2 and 3) |
| Asking "what should I do next?" after the meeting | Waiting to be told what to do means something is wrong[^dredze2012successful-e16] | Come with prioritized next steps and reasons (Section 4) |
| Avoiding your advisor when things aren't going well | Your advisor would rather know early[^dredze2012successful-e20] | Report early and specifically (Section 3) |
| Judging whether you are behind by comparing yourself with others | You can't guess accurately; ask your advisor[^dredze2012successful-e23] | Ask for feedback regularly (Sections 1 and 7) |
| Not discussing division of work and authorship at the start of a collaboration | The medical journals' authorship recommendations suggest deciding at the planning stage[^icmje2026recommendations-e4] | Write a division-of-work table when you start (Sections 5 and 6) |
| Adding people who didn't contribute as authors, or submitting without every author reading the final draft | Every author should have made a significant contribution and read the final draft[^herremans2020successful-e4] | Decide by the criteria; those who don't qualify go in the acknowledgments (Section 6) |
| Sending the draft to co-authors the day before the deadline | Co-authors can't make time and can't give useful comments[^herremans2020successful-e1][^dredze2012successful-e21] | For conference papers, at least two weeks ahead (Sections 6 and 7) |

## Further reading

- **Dredze & Wallach, "How to Be a Successful PhD Student"**: the most comprehensive checklist; the items in the "You and Your Advisor" section can be followed as they are.
- **Jia-Bin Huang, "How to meet with your advisors/mentors?"** (Twitter thread): read it before a meeting and compare against its good and bad examples.
- **Karpathy, "A Survival Guide to a PhD"**: the "Adviser" section covers differences in advising styles; "Resistance" in the "Research topics" section discusses when you can go against your advisor.
- **Vinitsky, "Expectation Setting"**: an advisor's statement of expectations for his students, useful as a basis for discussion with your own advisor.
- **Herremans, "How to be a successful PhD student?"**: etiquette between co-authors and basic principles of authorship.
- **The authorship recommendations of the International Committee of Medical Journal Editors (ICMJE)**: written for medical journals, but very concrete on who should be an author, when to decide, and whom to turn to if you can't agree; other fields can use them as a reference `[Our analysis]`.

[^dredze2012successful-e6]: Dredze & Wallach 2012 (v1.2), You and Your Advisor, p. 2. [Evidence](../../sources/notes/dredze2012successful.md#e6)
[^dredze2012successful-e7]: Dredze & Wallach 2012 (v1.2), You and Your Advisor, p. 2. [Evidence](../../sources/notes/dredze2012successful.md#e7)
[^dredze2012successful-e8]: Dredze & Wallach 2012 (v1.2), #5, p. 2. [Evidence](../../sources/notes/dredze2012successful.md#e8)
[^dredze2012successful-e9]: Dredze & Wallach 2012 (v1.2), #6, p. 2. [Evidence](../../sources/notes/dredze2012successful.md#e9)
[^dredze2012successful-e10]: Dredze & Wallach 2012 (v1.2), #7, p. 3. [Evidence](../../sources/notes/dredze2012successful.md#e10)
[^dredze2012successful-e11]: Dredze & Wallach 2012 (v1.2), #8, p. 3. [Evidence](../../sources/notes/dredze2012successful.md#e11)
[^dredze2012successful-e12]: Dredze & Wallach 2012 (v1.2), #9, p. 3. [Evidence](../../sources/notes/dredze2012successful.md#e12)
[^dredze2012successful-e13]: Dredze & Wallach 2012 (v1.2), #10, p. 3. [Evidence](../../sources/notes/dredze2012successful.md#e13)
[^dredze2012successful-e14]: Dredze & Wallach 2012 (v1.2), #11, p. 3. [Evidence](../../sources/notes/dredze2012successful.md#e14)
[^dredze2012successful-e15]: Dredze & Wallach 2012 (v1.2), #14, p. 4. [Evidence](../../sources/notes/dredze2012successful.md#e15)
[^dredze2012successful-e16]: Dredze & Wallach 2012 (v1.2), #17, p. 4. [Evidence](../../sources/notes/dredze2012successful.md#e16)
[^dredze2012successful-e17]: Dredze & Wallach 2012 (v1.2), #13, p. 4. [Evidence](../../sources/notes/dredze2012successful.md#e17)
[^dredze2012successful-e18]: Dredze & Wallach 2012 (v1.2), #32, p. 6. [Evidence](../../sources/notes/dredze2012successful.md#e18)
[^dredze2012successful-e19]: Dredze & Wallach 2012 (v1.2), #37, p. 7. [Evidence](../../sources/notes/dredze2012successful.md#e19)
[^dredze2012successful-e20]: Dredze & Wallach 2012 (v1.2), #45, p. 8. [Evidence](../../sources/notes/dredze2012successful.md#e20)
[^dredze2012successful-e21]: Dredze & Wallach 2012 (v1.2), #46, p. 8. [Evidence](../../sources/notes/dredze2012successful.md#e21)
[^dredze2012successful-e22]: Dredze & Wallach 2012 (v1.2), #54, p. 9. [Evidence](../../sources/notes/dredze2012successful.md#e22)
[^dredze2012successful-e23]: Dredze & Wallach 2012 (v1.2), Progressing Through Graduate School, p. 10. [Evidence](../../sources/notes/dredze2012successful.md#e23)
[^huang2023advisor-e1]: Jia-Bin Huang 2023, tweet thread, [How to meet with your advisors/mentors?](https://twitter.com/jbhuang0604/status/1653614931202195458), Present results. [Evidence](../../sources/notes/huang2023advisor.md#e1)
[^huang2023advisor-e2]: Jia-Bin Huang 2023, tweet thread, Present results. [Evidence](../../sources/notes/huang2023advisor.md#e2)
[^huang2023advisor-e3]: Jia-Bin Huang 2023, tweet thread, Make an agenda. [Evidence](../../sources/notes/huang2023advisor.md#e3)
[^huang2023advisor-e4]: Jia-Bin Huang 2023, tweet thread, Start with a summary. [Evidence](../../sources/notes/huang2023advisor.md#e4)
[^huang2023advisor-e5]: Jia-Bin Huang 2023, tweet thread, Interpret your results. [Evidence](../../sources/notes/huang2023advisor.md#e5)
[^huang2023advisor-e6]: Jia-Bin Huang 2023, tweet thread, Propose next steps. [Evidence](../../sources/notes/huang2023advisor.md#e6)
[^huang2023advisor-e7]: Jia-Bin Huang 2023, tweet thread, Summarize your meeting. [Evidence](../../sources/notes/huang2023advisor.md#e7)
[^huang2023unstuck-e7]: Jia-Bin Huang 2023, tweet thread, [How to get unstuck?](https://twitter.com/jbhuang0604/status/1717381151508054029), Help your mentors help you. [Evidence](../../sources/notes/huang2023unstuck.md#e7)
[^huang2023unstuck-e8]: Jia-Bin Huang 2023, tweet thread, Make your experiments easy to understand. [Evidence](../../sources/notes/huang2023unstuck.md#e8)
[^karpathy2016survival-e1]: Karpathy 2016, Adviser / Student adviser relationship. [Evidence](../../sources/notes/karpathy2016survival.md#e1)
[^karpathy2016survival-e2]: Karpathy 2016, Adviser / Student adviser relationship. [Evidence](../../sources/notes/karpathy2016survival.md#e2)
[^karpathy2016survival-e3]: Karpathy 2016, Adviser / Axes of variation. [Evidence](../../sources/notes/karpathy2016survival.md#e3)
[^karpathy2016survival-e4]: Karpathy 2016, Adviser / Impressing an adviser. [Evidence](../../sources/notes/karpathy2016survival.md#e4)
[^karpathy2016survival-e5]: Karpathy 2016, Adviser / Consider the entire lab. [Evidence](../../sources/notes/karpathy2016survival.md#e5)
[^karpathy2016survival-e6]: Karpathy 2016, Research topics / Resistance. [Evidence](../../sources/notes/karpathy2016survival.md#e6)
[^karpathy2016survival-e7]: Karpathy 2016, Research topics / Resistance. [Evidence](../../sources/notes/karpathy2016survival.md#e7)
[^vinitskyexpectation-e1]: Vinitsky, Expectation Setting, opening (year to be confirmed). [Evidence](../../sources/notes/vinitskyexpectation.md#e1)
[^vinitskyexpectation-e2]: Vinitsky, Expectation Setting, opening. [Evidence](../../sources/notes/vinitskyexpectation.md#e2)
[^vinitskyexpectation-e3]: Vinitsky, Expectation Setting, Year one / Meetings. [Evidence](../../sources/notes/vinitskyexpectation.md#e3)
[^vinitskyexpectation-e4]: Vinitsky, Expectation Setting, Year Three. [Evidence](../../sources/notes/vinitskyexpectation.md#e4)
[^freeman2013research-e8]: Freeman 2013, p. 2. [Evidence](../../sources/notes/freeman2013research.md#e8)
[^freeman2013research-e9]: Freeman 2013, p. 3. [Evidence](../../sources/notes/freeman2013research.md#e9)
[^freeman2013research-e10]: Freeman 2013, p. 3. [Evidence](../../sources/notes/freeman2013research.md#e10)
[^herremans2020successful-e1]: Herremans 2020, co-authors key point. [Evidence](../../sources/notes/herremans2020successful.md#e1)
[^herremans2020successful-e2]: Herremans 2020, pair up key point. [Evidence](../../sources/notes/herremans2020successful.md#e2)
[^herremans2020successful-e3]: Herremans 2020, proofread key point. [Evidence](../../sources/notes/herremans2020successful.md#e3)
[^herremans2020successful-e4]: Herremans 2020, authors key point. [Evidence](../../sources/notes/herremans2020successful.md#e4)
[^herremans2020successful-e5]: Herremans 2020, software code key point. [Evidence](../../sources/notes/herremans2020successful.md#e5)
[^herremans2020successful-e6]: Herremans 2020, Own your project key point. [Evidence](../../sources/notes/herremans2020successful.md#e6)
[^halimtips-e1]: Halim, PhD Tips, The Advantages of Taking Graduate Studies. [Evidence](../../sources/notes/halimtips.md#e1)
[^halimtips-e2]: Halim, PhD Tips, The Advantages of Taking Graduate Studies. [Evidence](../../sources/notes/halimtips.md#e2)
[^halimtips-e4]: Halim, PhD Tips, Miscellaneous Things. [Evidence](../../sources/notes/halimtips.md#e4)
[^kuroseadvice-e1]: Kurose, slide #7, p. 16. [Evidence](../../sources/notes/kuroseadvice.md#e1)
[^kuroseadvice-e2]: Kurose, slide #9, p. 18. [Evidence](../../sources/notes/kuroseadvice.md#e2)
[^ruder2020tips-e3]: Ruder 2020, 4) Collaborate. [Evidence](../../sources/notes/ruder2020tips.md#e3)
[^ruder2020tips-e4]: Ruder 2020, 4) Collaborate. [Evidence](../../sources/notes/ruder2020tips.md#e4)
[^ruder2020tips-e5]: Ruder 2020, 4) Collaborate. [Evidence](../../sources/notes/ruder2020tips.md#e5)
[^ruder2020tips-e6]: Ruder 2020, 10) Play the long game. [Evidence](../../sources/notes/ruder2020tips.md#e6)
[^nanda2025mindsets-e15]: Nanda 2025b, Prioritisation. [Evidence](../../sources/notes/nanda2025mindsets.md#e15)
[^nanda2025mindsets-e16]: Nanda 2025b, Truth Seeking. [Evidence](../../sources/notes/nanda2025mindsets.md#e16)
[^nanda2025taste-e9]: Nanda 2025, Conclusion. [Evidence](../../sources/notes/nanda2025taste.md#e9)
[^perez2024tips-e6]: Perez 2024, Tactical Research Tips & Approach. [Evidence](../../sources/notes/perez2024tips.md#e6)
[^perez2024tips-e7]: Perez 2024, What success generally looks like. [Evidence](../../sources/notes/perez2024tips.md#e7)
[^perez2024tips-e8]: Perez 2024, What success generally looks like. [Evidence](../../sources/notes/perez2024tips.md#e8)
[^schulman2020opinionated-e4]: Schulman 2020, Honing Your Taste. [Evidence](../../sources/notes/schulman2020opinionated.md#e4)
[^nielsen2004principles-e5]: Nielsen 2004, Self-discipline. [Evidence](../../sources/notes/nielsen2004principles.md#e5)
[^olah2021taste-e4]: Olah 2021, Exercise 1. [Evidence](../../sources/notes/olah2021taste.md#e4)
[^allea2023european-e7]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e7)
[^allea2023european-e8]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e8)
[^icmje2026recommendations-e4]: ICMJE 2026, §II.A.2 Who Is an Author? [Evidence](../../sources/notes/icmje2026recommendations.md#e4)
[^icmje2026recommendations-e5]: ICMJE 2026, §II.A.2. [Evidence](../../sources/notes/icmje2026recommendations.md#e5)
[^icmje2026recommendations-e7]: ICMJE 2026, §II.A.3. [Evidence](../../sources/notes/icmje2026recommendations.md#e7)
[^einav2006surname-e1]: Einav & Yariv 2006, p. 175. [Evidence](../../sources/notes/einav2006surname.md#e1)
[^einav2006surname-e3]: Einav & Yariv 2006, p. 182, footnote 8. [Evidence](../../sources/notes/einav2006surname.md#e3)
[^acm2025authorship-e1]: ACM Policy on Authorship 2025, Scope of Policy. [Evidence](../../sources/notes/acm2025authorship.md#e1)
[^acm2025authorship-e2]: ACM Policy on Authorship 2025, Criteria for Authorship. [Evidence](../../sources/notes/acm2025authorship.md#e2)
[^acm2025authorship-e3]: ACM Policy on Authorship 2025, Criteria for Authorship, Note. [Evidence](../../sources/notes/acm2025authorship.md#e3)
[^acm2025authorship-e4]: ACM Policy on Authorship 2025, Criteria for Authorship. [Evidence](../../sources/notes/acm2025authorship.md#e4)
[^acm2025authorship-e5]: ACM Policy on Authorship 2025, Criteria for Authorship. [Evidence](../../sources/notes/acm2025authorship.md#e5)
[^ieee2026pspb-e6]: IEEE PSPB Operations Manual 2026, §8.2.1.A.1. [Evidence](../../sources/notes/ieee2026pspb.md#e6)
[^ieee2026pspb-e7]: IEEE PSPB Operations Manual 2026, §8.2.1.A.1. [Evidence](../../sources/notes/ieee2026pspb.md#e7)
[^ieee2026pspb-e8]: IEEE PSPB Operations Manual 2026, §8.2.1.A.2. [Evidence](../../sources/notes/ieee2026pspb.md#e8)
[^waltman2012empirical-e2]: Waltman 2012, §3. [Evidence](../../sources/notes/waltman2012empirical.md#e2)
[^waltman2012empirical-e3]: Waltman 2012, §3.2. [Evidence](../../sources/notes/waltman2012empirical.md#e3)
[^waltman2012empirical-e4]: Waltman 2012, §2. [Evidence](../../sources/notes/waltman2012empirical.md#e4)
[^waltman2012empirical-e5]: Waltman 2012, §3.2 Table 1. [Evidence](../../sources/notes/waltman2012empirical.md#e5)
[^waltman2012empirical-e9]: Waltman 2012, §3.2. [Evidence](../../sources/notes/waltman2012empirical.md#e9)
