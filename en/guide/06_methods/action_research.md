# Action research: improving a real organization while you study it

This page covers **action research**: you partner with a real organization, take part yourself in a change (for example, introducing a code review process together with a development team), and while you push the improvement forward, you systematically study what the change does.

If you only observe and don't intervene, that is a [case study](case_study.md); if your contribution is a new tool or technique in itself, see [Engineering research](../07_fields/computer-science/practices/engineering_research.md).

**Scope** `[Our analysis]`: the sources for this page come from software engineering and information systems. They are the action research standard in the ACM SIGSOFT Empirical Standards (the empirical research standards of the Association for Computing Machinery's Special Interest Group on Software Engineering; "the SIGSOFT standards" below), Staron's guidelines for action research in software engineering (which restate the principles of Davison et al.), and dos Santos and Travassos's report on action research in software engineering. Other areas of computer science can use this page directly, as long as the study is about rolling out a change in a team or organization (for example, introducing a new incident postmortem process in an operations team, or new data management rules in a lab). If you do action research in another field, read that field's norms first, because the same name can mean different things. In education, for example, the educator in action research is both researcher and teacher[^anderson2012design-e4], and the work is usually done by teachers themselves[^anderson2012design-e5] (see the [education field overview](../07_fields/education/README.md#research-methods-common-in-this-field)). The approach on this page, where researchers and practitioners team up to bring about change in a real setting, is closer to what education calls [Design-based research](../07_fields/education/practices/design_based_research.md).

**Strategies it usually serves**: [Building and improving](../05_research-strategies/build_improve.md) (introducing an improvement in a real organization) and [Description](../05_research-strategies/observe_describe.md) (seeing how people in a real setting respond).

**After reading this page, you should be able to:**

- tell whether your project is action research, a case study, or an "experience report";
- agree on terms with your partner organization and work through the cycle of diagnosing, planning, acting, evaluating, and reflecting;
- design data collection that can show what the intervention did, and handle your dual role as researcher;
- check your study against the checklist at the end of the page.

---

## 1. What this kind of research is and when to use it

Action research studies **how an intervention (such as introducing a method or tool) affects a real setting**[^ralph2020empirical-e330]. Researchers and participants work together to solve problems[^santos2011action-e1]. The difficulty it addresses is **how to introduce a new practice and study it at the same time**[^staron2025guidelines-e1].

**How it differs from related methods**:

| | Action research | Case study | Experiment | Engineering research |
|---|---|---|---|---|
| Does the researcher intervene? | Yes; changing things and observing the results are at the core of the research[^ralph2020empirical-e331] | No; the researcher is an observer or participant[^staron2025guidelines-e2] | Yes, but under control, which favors small, isolated problems[^staron2025guidelines-e2] | Proposes and evaluates a technical artifact |
| Suited to | Interventions with a social dimension, such as changing ways of working, processes or culture[^ralph2020empirical-e332] | Understanding a phenomenon in its real setting | Testing hypotheses | A new tool or technique in itself, especially one without a social dimension[^ralph2020empirical-e332] |

If your study both builds a new tool and drives a change with a social dimension in an organization, refer to both standards[^ralph2020empirical-e332]. Action research and case studies are sometimes hard to tell apart, especially when some phases involve more observation than action[^santos2011action-e8]. A simple test: **did the researcher help decide on and drive the change?** `[Our analysis]`

**Action research is not consulting, and it is not an experience report.** What sets it apart from everyday improvement work is that it is actively driven by theory and research methods[^santos2011action-e7]. You have to write down your criteria before the study starts; otherwise what you describe at the end may be "action rather than research"[^santos2011action-e5]. Conversely, systematic observation and reflection should not be dismissed as consulting, and consulting or experience should not pass itself off as action research[^ralph2020empirical-e342].

**When not to do it**[^staron2025guidelines-e9]:

- you can't get into the organization, and there is no one from the organization on your team;
- you can't commit for the long term;
- you only want a paper and can't contribute to the organization's practice.

If the conditions aren't there, be ready to switch methods; in most cases, a case study to get to know the organization is a better starting point[^staron2025guidelines-e10].

---

## 2. How to do it

One example runs through this section: **you partner with a company's development team to introduce a code review process and evaluate its effect.** `[Our analysis]`

### Step 0: Agree on terms and build the team

Action research needs an agreement that sets out what each side will do and what each side gets out of it[^santos2011action-e3]. Following the principles proposed by Davison et al. (as restated by Staron), confirm these points[^staron2025guidelines-e3]:

- both sides agree that action research suits the situation, and the organization explicitly commits to taking part;
- the roles and responsibilities of each side;
- the project's goals and **evaluation measures**;
- the data collection and analysis methods.

Both sides also need to lay their expectations on the table: what results the researcher wants, what they plan to publish and how much time they will put in; how many resources the organization can provide, and whether it can actually carry out the intervention[^staron2025guidelines-e10]. Also agree on any review before publication and on confidentiality requirements `[Our analysis]`.

**Who to approach**: in a hierarchical organization, go to management first; in an autonomous one, go to the team first[^staron2025guidelines-e11]. **Your team needs two kinds of people**: at least a few people with research degrees, and at least a few practitioners from the organization[^staron2025guidelines-e8].

**Why:** the agreement also decides when the study ends: when both sides are satisfied with the results[^santos2011action-e3]. In the paper, describe the relationship between the researchers and the organization, such as project funding, potential conflicts of interest, and which relationships gave you access[^ralph2020empirical-e333].

### The cycle: diagnose, plan, act, evaluate, reflect

Action research proceeds in cycles. A common description is a five-phase cycle[^santos2011action-e2][^staron2025guidelines-e6], though the number of phases can vary[^staron2025guidelines-e6]; each cycle builds on the one before[^ralph2020empirical-e335]. You can also go back between phases; for example, if the problem is unclear or the plan can't be carried out, return to diagnosis[^santos2011action-e4].

**1. Diagnose**: get a full picture of the situation, the stakeholders and their expectations[^santos2011action-e2], and identify the problem and its likely causes. The researcher must **diagnose** the organization's situation **independently**[^staron2025guidelines-e4].

> Example: you interview team members and look at the defect records, and find that many defects are discovered only after merging, partly because nobody looks at anyone else's code. `[Our analysis]`

**2. Plan**: design an intervention aimed at the causes you diagnosed[^staron2025guidelines-e17], and write down in advance the theory it is based on, which you will later use to explain the results[^staron2025guidelines-e22]. Decide these things in advance:

- **what counts as success, what counts as failure, and when to stop**[^staron2025guidelines-e14];
- **the baseline**: every intervention must be compared against a baseline[^staron2025guidelines-e14]. To check the effect of introducing code review, you have to measure review speed, duration and frequency **before** you introduce it[^staron2025guidelines-e15];
- **what data to collect**. Deciding this in advance means that when something unexpected happens, you can concentrate on monitoring the action[^santos2011action-e10];
- keep the intervention in each cycle **small and atomic** (one change at a time). Other changes happening at the same time become confounders (factors that also affect the outcome and lead you to misjudge the cause), and you won't be able to tell whether the effect came from your intervention or from something else[^staron2025guidelines-e13];
- the organization must approve the plan before it is carried out[^staron2025guidelines-e4].

**3. Act**: carry out the intervention. The people implementing it should be team members who are able to make the change within the scope of their own work; building a demonstration prototype on the side of the existing work is not action research[^staron2025guidelines-e13].

- Unplanned things will happen. Record them so you can explain your reasoning later[^santos2011action-e10];
- watch for events such as reorganizations, new members joining or product changes that might affect the results[^staron2025guidelines-e16];
- collect data automatically where you can, for example by recording audio, to free up your time to take part in the intervention[^santos2011action-e11].

**4. Evaluate**: look at both quantitative and qualitative effects[^staron2025guidelines-e12][^ralph2020empirical-e334]:

- Quantitative: compare against the baseline, for example time spent on review, or the number of defects found after merging[^staron2025guidelines-e12]; `[Our analysis, for the specific metrics]`
- Qualitative: interviews, workshops, retrospectives[^staron2025guidelines-e12];
- report how participants and stakeholders reacted to the intervention[^ralph2020empirical-e336], but **don't report only what participants think**: you need a systematic evaluation that doesn't avoid the problems[^ralph2020empirical-e341];
- when you collect data before the intervention, be prepared for the Hawthorne effect: people change their behavior when they know they are being observed[^staron2025guidelines-e15].

**5. Reflect**: sum up with the participants what you have learned, and spread it within the organization[^santos2011action-e2]. Then **make an explicit decision** about whether to run another cycle[^staron2025guidelines-e4], adjusting the theory, scope, team or the intervention itself if needed[^staron2025guidelines-e17]. A whole study may end after two or three cycles, or run to ten or more[^staron2025guidelines-e19].

**A failed intervention still has value.** Reporting negative results of an intervention and analyzing why a method didn't fit is acceptable[^ralph2020empirical-e340]; negative or inconclusive results are also valuable to the research community[^staron2025guidelines-e18].

---

## 3. The researcher's dual role

In action research you are often both the researcher and the person driving the change, sometimes even a member of the team[^santos2011action-e9]. This brings two risks: losing distance and seeing only what you want to see, and promoting the method you brought in. The SIGSOFT standards list "losing professional distance and impartiality" and "over-selling a tool or method without regard for participants' problems, practices or values" as antipatterns[^ralph2020empirical-e341].

> **Where sources disagree: how deeply should the researcher be embedded in the organization?**
> - Staron argues that in software engineering, the research must be embedded in the organization, or the change will often be abandoned[^staron2025guidelines-e5]. Embedded means the researcher is either employed by the organization or has the same access as its employees[^staron2025guidelines-e7].
> - The SIGSOFT standards warn that getting too involved with the community you study, and losing distance and impartiality, is an antipattern[^ralph2020empirical-e341].
>
> The two don't contradict each other: being embedded makes the change actually stick, and keeping your distance makes the evaluation credible. In practice, you can take part deeply in the intervention and still keep the evaluation fair with the measures below `[Our analysis]`.

**How to reduce bias**:

- **Write down the theory, evaluation measures and success criteria in advance**, then use them to interpret the results, which limits over-interpretation[^staron2025guidelines-e22][^staron2025guidelines-e14]. Rigorous action research needs some control to reduce the influence of researcher bias and other factors, and it also needs the underlying theory to stay explicit throughout[^santos2011action-e15];
- **Reflect on your own biases**; this is required[^ralph2020empirical-e336], including reflecting on any negative effect you may have on some participants[^ralph2020empirical-e344];
- **Get other people to look**: member checking (asking participants to confirm your understanding of what they said and experienced), feedback from practitioners who weren't involved, and having your advisor or peers review your coding[^ralph2020empirical-e337]; ideally, several researchers corroborate one another's findings[^ralph2020empirical-e338];
- **Triangulate quantitative and qualitative data**[^ralph2020empirical-e337].

---

## 4. How far your conclusions reach

The SIGSOFT standards treat "it only studied one organization, so the conclusions can't be generalized" as an **invalid** criticism of action research[^ralph2020empirical-e343]. Action research is judged by criteria such as reflexivity, credibility, resonance, usefulness and transferability; positivist criteria such as internal validity, construct validity, generalizability and reliability usually don't apply[^ralph2020empirical-e339]. Transferability is the extent to which the results are likely to apply to other places, people or contexts[^ralph2020empirical-e344].

On the other hand, **don't generalize too quickly yourself**: what worked in one organization won't necessarily work in another[^staron2025guidelines-e22]. The theories action research produces are often concrete relationships taken directly from observation, or somewhat more abstract "middle-range theories" that still stay close to what was observed[^santos2011action-e14]. So:

- **Describe the context in detail**, including which interventions were made[^staron2025guidelines-e20], for example the type of organization, team size and project background `[Our analysis]`. If you must choose between disclosing the organization's name and disclosing its characteristics, the characteristics are more useful to readers[^staron2025guidelines-e20];
- **Explain your process**: action research can't reach the repeatability of the natural sciences, but you need to make clear the process by which you reached your conclusions[^santos2011action-e6].

For a general discussion of validity, see [Validity and limitations](../02_from-project-to-study/03_validity-and-limits.md).

---

## 5. Ethics

Action research is collaborative research in a real setting, so ethical issues matter even more[^santos2011action-e13]:

- **Genuinely voluntary participation is hard**: research activities overlap with people's jobs, and participants may feel they have no choice. You can promise not to publish individual data[^santos2011action-e13].
- **Sensitive information**: you will see private conversations, emails and commits containing sensitive information. Consult the organization's management and legal team before sharing anything; when presenting more widely, remove anything that identifies individuals or teams[^staron2025guidelines-e21].
- **Do no harm to the organization**: be ready to stop at any time if the intervention causes harm[^staron2025guidelines-e18]; follow the organization's rules just as an employee would[^staron2025guidelines-e11].
- **Don't sacrifice the problem for the paper**: the goal of the agreement is always to solve a real problem[^santos2011action-e12].
- Don't force an intervention the participants or the organization can't accept[^ralph2020empirical-e341].

For the general principles of research ethics, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md). Every study must acknowledge and mitigate the risks and harms it may cause[^ralph2020empirical-e65].

---

## 6. Checklist

This checklist follows the SIGSOFT action research standard, which is a review standard for software engineering; in other fields, your own field's norms take precedence `[Our analysis]`.

**Essential**

- [ ] Explain why you chose this organization, and describe it in detail[^ralph2020empirical-e333]
- [ ] Describe the relationship between the researchers and the organization (funding, conflicts of interest, how you got access)[^ralph2020empirical-e333]
- [ ] Describe the intervention in detail, and explain who decided on it and how it was evaluated[^ralph2020empirical-e334]
- [ ] State how long the study lasted, who carried out the intervention, and which part of the organization you worked with[^ralph2020empirical-e335]
- [ ] Describe the cycles or phases of the study and how they relate to the intervention[^ralph2020empirical-e335]
- [ ] Give a clear chain of evidence from observations to conclusions[^ralph2020empirical-e336]
- [ ] Report how participants and stakeholders reacted to the intervention, and what the organization learned[^ralph2020empirical-e336]
- [ ] Reflect on your own possible biases as a researcher[^ralph2020empirical-e336]

**Desirable**

- [ ] Use plenty of direct quotations, and provide supplementary materials such as interview guides and coding schemes[^ralph2020empirical-e337]
- [ ] Check your results with member checking, peer review of coding and similar methods[^ralph2020empirical-e337]
- [ ] Your conclusions are potentially transferable to other contexts[^ralph2020empirical-e337]
- [ ] Triangulate quantitative and qualitative data[^ralph2020empirical-e337]

**Extraordinary**

- [ ] Work as a team of several researchers who corroborate one another, to reduce researcher bias[^ralph2020empirical-e338]

**Acceptable deviations (not flaws)**[^ralph2020empirical-e340]

- Leaving out details and direct quotations to protect participants
- The intervention failed: you report the negative results and analyze why

**Common reviewer criticisms that are not valid** (as listed in the SIGSOFT standards, for software engineering submissions)[^ralph2020empirical-e342][^ralph2020empirical-e343]: you don't need to worry about these

- "The researchers intervened in the setting, so the conclusions are invalid": introducing a change and observing the response is the whole point of action research
- "This is just consulting or an experience report" (provided you did systematic observation and reflection)
- "Only one organization was studied", "the sample is not representative", "the results can't be generalized"
- "There is no control group": action research is not an experiment

---

## 7. Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Writing up a consulting or improvement project as action research after the fact | Without criteria written down in advance, it is just "action rather than research"[^santos2011action-e5][^ralph2020empirical-e342] |
| Starting the intervention without a baseline | You can't tell whether anything improved[^staron2025guidelines-e14] |
| Reporting only whether participants liked the new process | There is no systematic evaluation, and the problems are avoided[^ralph2020empirical-e341] |
| Promoting the tool or method you brought in | It ignores the participants' problems and values[^ralph2020empirical-e341] |
| Forcing an intervention the organization doesn't accept | It goes against the principle of collaboration[^ralph2020empirical-e341] |
| A large, long intervention | It is easily interrupted, and you can't tell where the effect came from[^staron2025guidelines-e13] |
| Not recording unexpected events such as reorganizations or staff changes | Those events may be the real cause of the results[^staron2025guidelines-e16][^santos2011action-e10] |
| Claiming something "works in general" because it worked in one organization | Overgeneralization[^staron2025guidelines-e22] |
| Giving the organization's name instead of describing the context | Readers can't judge whether the results apply to their own situation[^staron2025guidelines-e20] |

---

## 8. Further reading

- **Review standard**: the action research standard in the SIGSOFT Empirical Standards, with suggested readings and exemplar papers.
- **Practical guidelines**: Staron 2025 gives 20 guidelines covering project setup, the organizational setting, intervention design, reporting and ethics, and restates the principles and checklist for canonical action research from Davison et al. 2004. The author acknowledges that these guidelines have not yet been validated in industrial action research[^staron2025guidelines-e23].
- **A complete worked study**: dos Santos & Travassos 2011 report a refactoring study in full across the five phases, and give a template for reporting action research (§5.2.3). Their survey of the existing literature found that the rigor of action research in software engineering still needs to improve[^santos2011action-e16].
- **Book**: Staron 2020, *Action Research in Software Engineering: Theory and Applications* (Springer). The book is not open access, and we have not read the full text.

Links to all of these are in the [source list](../../sources/README.md).

[^ralph2020empirical-e330]: SIGSOFT Action Research standard, Definition. [Evidence](../../sources/notes/ralph2020empirical.md#e330)
[^ralph2020empirical-e331]: SIGSOFT Action Research standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e331)
[^ralph2020empirical-e332]: SIGSOFT Action Research standard, Application. [Evidence](../../sources/notes/ralph2020empirical.md#e332)
[^ralph2020empirical-e333]: SIGSOFT Action Research standard, Essential Attributes and footnote 1. [Evidence](../../sources/notes/ralph2020empirical.md#e333)
[^ralph2020empirical-e334]: SIGSOFT Action Research standard, Essential Attributes and footnote 2. [Evidence](../../sources/notes/ralph2020empirical.md#e334)
[^ralph2020empirical-e335]: SIGSOFT Action Research standard, Essential Attributes and footnotes 3 and 4. [Evidence](../../sources/notes/ralph2020empirical.md#e335)
[^ralph2020empirical-e336]: SIGSOFT Action Research standard, Essential Attributes (results and discussion). [Evidence](../../sources/notes/ralph2020empirical.md#e336)
[^ralph2020empirical-e337]: SIGSOFT Action Research standard, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e337)
[^ralph2020empirical-e338]: SIGSOFT Action Research standard, Extraordinary Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e338)
[^ralph2020empirical-e339]: SIGSOFT Action Research standard, Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e339)
[^ralph2020empirical-e340]: SIGSOFT Action Research standard, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e340)
[^ralph2020empirical-e341]: SIGSOFT Action Research standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e341)
[^ralph2020empirical-e342]: SIGSOFT Action Research standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e342)
[^ralph2020empirical-e343]: SIGSOFT Action Research standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e343)
[^ralph2020empirical-e344]: SIGSOFT Glossary, Reflexivity, Transferability. [Evidence](../../sources/notes/ralph2020empirical.md#e344)
[^ralph2020empirical-e65]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e65)
[^staron2025guidelines-e1]: Staron 2025, §1. [Evidence](../../sources/notes/staron2025guidelines.md#e1)
[^staron2025guidelines-e2]: Staron 2025, §1. [Evidence](../../sources/notes/staron2025guidelines.md#e2)
[^staron2025guidelines-e3]: Staron 2025, §2.2, paraphrasing Davison et al. 2004. [Evidence](../../sources/notes/staron2025guidelines.md#e3)
[^staron2025guidelines-e4]: Staron 2025, §2.2, paraphrasing Davison et al. 2004. [Evidence](../../sources/notes/staron2025guidelines.md#e4)
[^staron2025guidelines-e5]: Staron 2025, §2.2. [Evidence](../../sources/notes/staron2025guidelines.md#e5)
[^staron2025guidelines-e6]: Staron 2025, §2.1 and Fig. 2. [Evidence](../../sources/notes/staron2025guidelines.md#e6)
[^staron2025guidelines-e7]: Staron 2025, §3. [Evidence](../../sources/notes/staron2025guidelines.md#e7)
[^staron2025guidelines-e8]: Staron 2025, §3.1. [Evidence](../../sources/notes/staron2025guidelines.md#e8)
[^staron2025guidelines-e9]: Staron 2025, §3.2. [Evidence](../../sources/notes/staron2025guidelines.md#e9)
[^staron2025guidelines-e10]: Staron 2025, §4.1, Guidelines 2 and 3. [Evidence](../../sources/notes/staron2025guidelines.md#e10)
[^staron2025guidelines-e11]: Staron 2025, §4.2, Guidelines 5 and 6. [Evidence](../../sources/notes/staron2025guidelines.md#e11)
[^staron2025guidelines-e12]: Staron 2025, §4.3, Guideline 7. [Evidence](../../sources/notes/staron2025guidelines.md#e12)
[^staron2025guidelines-e13]: Staron 2025, §4.3, Guidelines 8 and 9. [Evidence](../../sources/notes/staron2025guidelines.md#e13)
[^staron2025guidelines-e14]: Staron 2025, §4.4, Guidelines 10 and 11. [Evidence](../../sources/notes/staron2025guidelines.md#e14)
[^staron2025guidelines-e15]: Staron 2025, §4.4. [Evidence](../../sources/notes/staron2025guidelines.md#e15)
[^staron2025guidelines-e16]: Staron 2025, §4.4, Guideline 12. [Evidence](../../sources/notes/staron2025guidelines.md#e16)
[^staron2025guidelines-e17]: Staron 2025, §4.4, Guideline 13. [Evidence](../../sources/notes/staron2025guidelines.md#e17)
[^staron2025guidelines-e18]: Staron 2025, §4.4, Guideline 14. [Evidence](../../sources/notes/staron2025guidelines.md#e18)
[^staron2025guidelines-e19]: Staron 2025, §4.4, Guideline 15. [Evidence](../../sources/notes/staron2025guidelines.md#e19)
[^staron2025guidelines-e20]: Staron 2025, §4.5, Guideline 18. [Evidence](../../sources/notes/staron2025guidelines.md#e20)
[^staron2025guidelines-e21]: Staron 2025, §4.6. [Evidence](../../sources/notes/staron2025guidelines.md#e21)
[^staron2025guidelines-e22]: Staron 2025, §4.6, Guidelines 19 and 20. [Evidence](../../sources/notes/staron2025guidelines.md#e22)
[^staron2025guidelines-e23]: Staron 2025, §5. [Evidence](../../sources/notes/staron2025guidelines.md#e23)
[^santos2011action-e1]: dos Santos & Travassos 2011, §2.2. [Evidence](../../sources/notes/santos2011action.md#e1)
[^santos2011action-e2]: dos Santos & Travassos 2011, §2.2. [Evidence](../../sources/notes/santos2011action.md#e2)
[^santos2011action-e3]: dos Santos & Travassos 2011, §2.2. [Evidence](../../sources/notes/santos2011action.md#e3)
[^santos2011action-e4]: dos Santos & Travassos 2011, §2.2. [Evidence](../../sources/notes/santos2011action.md#e4)
[^santos2011action-e5]: dos Santos & Travassos 2011, §2.2. [Evidence](../../sources/notes/santos2011action.md#e5)
[^santos2011action-e6]: dos Santos & Travassos 2011, §2.2. [Evidence](../../sources/notes/santos2011action.md#e6)
[^santos2011action-e7]: dos Santos & Travassos 2011, §2.2.1. [Evidence](../../sources/notes/santos2011action.md#e7)
[^santos2011action-e8]: dos Santos & Travassos 2011, §5.1.1. [Evidence](../../sources/notes/santos2011action.md#e8)
[^santos2011action-e9]: dos Santos & Travassos 2011, §5.1.1. [Evidence](../../sources/notes/santos2011action.md#e9)
[^santos2011action-e10]: dos Santos & Travassos 2011, §5.1.1. [Evidence](../../sources/notes/santos2011action.md#e10)
[^santos2011action-e11]: dos Santos & Travassos 2011, §5.1.1. [Evidence](../../sources/notes/santos2011action.md#e11)
[^santos2011action-e12]: dos Santos & Travassos 2011, §5.1.3. [Evidence](../../sources/notes/santos2011action.md#e12)
[^santos2011action-e13]: dos Santos & Travassos 2011, §5.1.3. [Evidence](../../sources/notes/santos2011action.md#e13)
[^santos2011action-e14]: dos Santos & Travassos 2011, §5.2.1. [Evidence](../../sources/notes/santos2011action.md#e14)
[^santos2011action-e15]: dos Santos & Travassos 2011, §5.2.2. [Evidence](../../sources/notes/santos2011action.md#e15)
[^santos2011action-e16]: dos Santos & Travassos 2011, Abstract. [Evidence](../../sources/notes/santos2011action.md#e16)
[^anderson2012design-e4]: Anderson & Shattuck 2012, collaborative partnership. [Evidence](../../sources/notes/anderson2012design.md#e4)
[^anderson2012design-e5]: Anderson & Shattuck 2012, Comparison to Action Research. [Evidence](../../sources/notes/anderson2012design.md#e5)
