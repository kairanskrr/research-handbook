# Focus groups: bringing a small group together to discuss a topic, and learning from how they interact

This page covers **focus groups**: you bring together a small group of people and, with a moderator guiding them, have them discuss a topic you have set; the record of the discussion is your qualitative data. What makes the method distinctive is that participants talk to each other. You listen not only to what each person says but also to how views form, clash, and shift as they talk.

Focus groups share many steps with [Interview studies](interview_study.md): purposive sampling, judging saturation, designing and piloting a guide, transcription, thematic analysis, and making your analysis trustworthy. This page doesn't repeat those; it links to them where they come up and concentrates on **what changes when you work with a group**. For the general ethics requirements when research involves people, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md#4-when-research-involves-people-or-could-harm-others-protect-people-first).

**Scope**: The methods sources behind this page come from health research (Kitzinger's 1995 introductory article in the *BMJ*, Carlsen and Glenton's survey of focus group studies in health journals, and Hennink et al.'s empirical study of saturation in focus groups), research ethics in social research (Sim and Waterfield), program evaluation (Krueger's freely available handout), and conservation biology (O.Nyumba et al.'s review of 170 conservation studies). Human–computer interaction and software engineering also use focus groups, for example to understand user needs or to get practitioners' feedback on a new tool or concept, but we found no openly available full-text methods guide for focus groups in those areas, so this page does not cite their norms. Fields differ in their habits about group size, number of groups, and reporting; check your own field's conventions first.

**Strategies it usually serves**: [Description](../05_research-strategies/observe_describe.md). Focus groups are also often one component of a [Mixed methods](mixed_methods.md) study, for example to help you draft items before a questionnaire, or to help you explain results after a questionnaire or experiment.

**After reading this page, you should be able to:**

- decide whether your question calls for focus groups, individual interviews, or a questionnaire;
- decide how to compose the groups, how many people to put in each, and how many groups to run;
- write a moderator's guide, run a discussion, and handle one person dominating and everyone else going along;
- tell individual opinion from group consensus during analysis, and treat the interaction itself as data;
- tell participants plainly how far you can keep what they say in the group confidential.

---

## 1. What this kind of study is, and when to use it

A focus group is usually defined as collecting participants' views and experiences through a moderated group discussion on a topic set by the researcher[^carlsen2011what-e1]. A broad definition cited by Sim and Waterfield is a group discussion on a topic, guided by a trained moderator[^sim2019focus-e1].

**It is not the same as interviewing several people at once.** Group interviews are often just a way to save time by collecting data from several people at the same time; focus groups explicitly use the interaction within the group as part of the method[^kitzinger1995qualitative-e1]. The emphasis is on interaction among participants, not on question and answer between moderator and participants[^carlsen2011what-e1]. The researcher acts as a moderator, steering a discussion among the participants[^nyumba2018use-e2]. Some authors treat focus groups and interviews as the same thing[^nyumba2018use-e3]; avoid doing that when you write your methods section.

**Questions it is good at:**

- **What people think, and why they think it.** Focus groups are particularly suited to exploring people's knowledge and experiences, looking not only at what people think but at how and why they think that way[^kitzinger1995qualitative-e2].
- **How views take shape within a group.** Kitzinger's comparison: individual experiences are better explored with interviews; how knowledge and ideas develop and operate within a given cultural context is better explored with focus groups; questionnaires suit the question "how many people hold this view?", while focus groups suit exploring how those views came about[^kitzinger1995qualitative-e19].
- **People who are hard to reach with questionnaires or formal interviews.** Focus groups don't exclude people who cannot read or write, and they can bring in people who would be reluctant to be interviewed on their own[^kitzinger1995qualitative-e3]. Health research often uses them to reach marginalized groups who don't return postal questionnaires or who are wary of formal interviews[^carlsen2011what-e2].
- **Working alongside a questionnaire or experiment.** Having a focus group discuss a questionnaire is a good way to test item wording, and focus groups can also help explain or dig into questionnaire results[^kitzinger1995qualitative-e7]; health research often places them before or after a questionnaire or trial[^carlsen2011what-e2].

**When it does not fit:**

- **When you need numbers.** Focus groups give depth and insight but cannot produce useful numerical results; don't use them when you need statistics[^nyumba2018use-e12].
- **When participants are not at ease with one another, or speaking up could expose them to discrimination**, focus groups should not be used[^nyumba2018use-e12].
- **When you worry that minority views will be drowned out.** Group norms can silence individual dissent[^kitzinger1995qualitative-e4].

> **Where sources disagree: can you use focus groups for sensitive topics?**
>
> - **The cautious view**: compared with individual interviews or questionnaires, participants are sometimes unwilling to discuss sensitive topics in a group, so take this into account when designing your questions[^nyumba2018use-e13].
> - **The less pessimistic view**: Kitzinger argues you should not assume a group is always more inhibiting than an interview; the more outgoing members speaking first can break the ice for shyer ones, which can actually help a group discuss taboo topics[^kitzinger1995qualitative-e5].
>
> In practice, look at where the sensitivity lies. If the worry is "saying this in front of people I know will have consequences," use individual interviews. If the worry is "this is hard to say on my own," a group of people with similar experiences may make it easier. If you're unsure, try one or two groups first.

**How it differs from related methods**:

| | Focus group | [Interview studies](interview_study.md) | [Questionnaire surveys](questionnaire_survey.md) |
|---|---|---|---|
| How many people at a time | A group of several | One | Many, each answering separately |
| Researcher's role | Moderator who gets participants talking to each other | Interviewer who probes one person in depth | Designs the items, usually not present |
| Data | Discussion record, including the interaction | One person's account | Standardized answers |
| Main output | Views within a group, disagreements, and how they took shape | Individual experiences, themes | Proportions, correlations |
| Unit of analysis | Usually the group | The individual | The individual |

For the basis of the "Unit of analysis" row, see [Step 6](#step-6-analysis-treat-the-interaction-as-data).

**An example**: The running example, "LLM vulnerability-detection results are inflated by data leakage," is a measurement project: the claim has to be tested by re-running the evaluation, and focus groups cannot prove it. But they can play a supporting role. Before you design a "clean" test set, you want to know how smart contract auditors view and use the vulnerability reports that large language models produce, and which public vulnerabilities they feel "everyone has already seen." You could group people by role: one group of auditors from audit firms, one of developers who write contracts, about two groups for each role. As people add to and push back on each other, a discussion often surfaces agreements and disagreements, such as "which vulnerability samples nearly everyone knows," faster than one-on-one interviews would. What you get are views and leads that help you pick test samples and write the motivation section of your paper, not evidence for the claim itself.

---

## 2. How to do it

### Step 1: Decide how to compose the groups

**How:**

- **First decide whether groups should be homogeneous or mixed.** Most researchers recommend homogeneous groups, to draw on shared experience; you can also deliberately mix people from different backgrounds to widen the range of perspectives in a group[^kitzinger1995qualitative-e8]. Krueger's handout also says a group is made up of similar people[^krueger2002designing-e1].
- **Then decide whether to use existing groups or recruit groups specially.** A group can be one that already exists, such as colleagues, or one convened for the study. With existing groups you can observe fragments of interaction close to how these people normally talk[^kitzinger1995qualitative-e9]. But when participants know each other, anonymity is harder to maintain[^sim2019focus-e8].
- **Segment by the characteristics you want to compare.** For example, sort people into categories by role or age and give each category its own groups, so you can later compare categories. Segmentation directly determines how many groups you need; see Step 2.
- **Recruit purposively, and over-recruit.** Identifying participants may be the most critical step, because the method relies mainly on participants stimulating one another to generate data[^nyumba2018use-e4]. Not everyone you recruit will show up, so recruit 10% to 25% more than you need[^nyumba2018use-e5]. For purposive sampling in general, see [Step 1 of Interview studies](interview_study.md#step-1-choose-interviewees).

**Why:** Who sits with whom decides what people dare to say. Hierarchy within a group affects the data: a nursing assistant placed in a group with a senior doctor from the same hospital, for instance, is unlikely to speak freely[^kitzinger1995qualitative-e8].

**Where people go wrong:** Putting managers with their staff, or advisors with their students, in the same group. The same goes for computer science: don't put a company's head of security and the engineers who report to them in one group to discuss "how our team handles vulnerabilities."

### Step 2: Set group size and the number of groups

**How:**

- **Group size**: sources give slightly different numbers. Kitzinger considers 4 to 8 people ideal[^kitzinger1995qualitative-e10]; Krueger says 5 to 10, preferably 6 to 8[^krueger2002designing-e1]; Carlsen and Glenton conclude that recommendations rarely fall outside 4 to 12[^carlsen2011what-e4]. Above 12, a group becomes hard to manage and may split into two or three side conversations[^nyumba2018use-e6].
- **Count your sample in groups, not people.** Most guidelines recommend the group as the unit of analysis, so sample size means the number of groups, not the total number of participants[^carlsen2011what-e3].
- **Start from a rule of thumb, finish with saturation.** Textbooks generally recommend 2 to 5 groups per category of participant, while stressing that this is only a rule of thumb and that the number depends on how complex the question is and how the groups are composed[^carlsen2011what-e6]. Krueger also lists running several groups as a basic feature of focus groups[^krueger2002designing-e1].
- **When you segment, run at least one group per segment, preferably two.** In Hennink et al.'s study, one group per segment was enough to find the issues, two groups per segment gave a fuller understanding, and more added little[^hennink2019what-e2]. Their example: segmenting by gender, you need at least two groups to cover both segments, and ideally two per segment, four in total[^hennink2019what-e6].
- **Plan a range in advance, not a fixed number.** A universal number of groups for focus group research is not useful; when you propose a sample size in advance, it is common to give a range (such as 4 to 6 groups) so you can adjust during data collection[^hennink2019what-e8].

**Two kinds of saturation.** Saturation means collecting more data yields nothing new; for how to judge it, see [Step 1 of Interview studies](interview_study.md#step-1-choose-interviewees). Hennink et al. distinguish two kinds: code saturation, when no new issues appear and the codebook stabilizes; and meaning saturation, when you fully understand those issues and no new insights or nuances emerge[^hennink2019what-e3]. In their study, four groups were enough to find most of the new issues, but more groups were needed to understand them fully[^hennink2019what-e1]; the first group alone produced 60% of the new codes[^hennink2019what-e4]. As they report, Guest et al. found that with a homogeneous, unsegmented population, saturation could be reached in three to six groups[^hennink2019what-e7].

**Why:** Too few groups and too many groups both lower the quality of a study[^carlsen2011what-e5]. Running too many places a burden on participants without adding scientific value, and can even be seen as unethical[^carlsen2011what-e9].

**Where people go wrong:** Fixing the number of groups, running them all, then analyzing and declaring "saturation was reached." Carlsen and Glenton found that several studies claiming saturation apparently had not analyzed data while collecting it[^carlsen2011what-e8]. If you use saturation to decide the number of groups, analyze after every group and record which new codes it added.

### Step 3: Write the moderator's guide

**How:**

- **Order the questions in five types**: opening (everyone answers in turn), introductory, transition, key, and ending, moving from general to specific[^krueger2002designing-e9]. Have only a few key questions, put them in the middle, and leave plenty of time for them.
- **Ask open questions about experience.** Avoid questions that can only be answered yes or no; use "think back" questions that take people back to an experience, rather than asking them to imagine the future[^krueger2002designing-e8]. For example, ask "Think back to the last time you used a large language model to check a contract. How did it go?" rather than "Do you think large language models will replace manual audits?"
- **Prepare your opening remarks and ground rules**: there are no right or wrong answers, only different points of view; you don't have to agree with others, but please listen respectfully; please talk to one another[^krueger2002designing-e6].
- **Plan the ending**: the moderator gives a brief oral summary and asks "Is this an accurate summary?"; then restates the purpose of the study and asks "Have we missed anything?"[^krueger2002designing-e10]
- **You can prepare a group exercise**, such as having the group sort and rank statements written on cards. What matters is the discussion the ranking provokes, not the final order[^kitzinger1995qualitative-e13].
- **Pilot the guide**: the same way as an interview guide; see [Step 2 of Interview studies](interview_study.md#step-2-design-the-interview-guide).

**Why:** In a focus group the time is shared among several people, so each question gets far less discussion than it would in an individual interview; keep the questions few and well chosen. Sessions that run too long tire participants[^nyumba2018use-e8]; Kitzinger suggests one to two hours per session[^kitzinger1995qualitative-e10].

**Where people go wrong:** Reusing an individual interview guide as is. An interview guide is built for one-to-one question and answer; in a group it turns into the moderator asking each person in turn, and the interaction disappears.

### Step 4: Moderate the discussion

**How:**

- **Work in pairs.** A focus group needs a skilled moderator plus an assistant; the assistant watches nonverbal interaction and the effects of group dynamics, and notes the general content of the discussion[^nyumba2018use-e7].
- **Get people talking to each other.** The moderator should explain that the point is for participants to talk to one another, not to the researcher; in the later part of a session the moderator can be more active, keeping debates going and asking people to discuss inconsistencies between participants and within their own thinking[^kitzinger1995qualitative-e11]. One advantage of focus groups is that disagreements between members can be explored with the participants on the spot[^kitzinger1995qualitative-e12].
- **Use pauses and probes.** Pause for five seconds; probe with "Would you explain further?" or "Would you give an example?"[^krueger2002designing-e4]
- **Control your own reactions.** Avoid saying "good," "excellent," and the like[^krueger2002designing-e5]. The moderator should stay engaged while remaining verbally and physically neutral[^nyumba2018use-e14].
- **Rein in dominant talkers and draw in quiet ones.** Group discussions carry group biases: dominance (one forceful person steers the discussion), the halo effect (someone's status sways the discussion), groupthink (people converge to keep the peace), and others; the moderator and assistant need to notice and handle them during data collection[^nyumba2018use-e15]. Krueger advises controlling "experts" and dominant talkers tactfully and drawing in shy participants[^krueger2002designing-e5]. The moderator should give everyone a chance to speak without pressuring anyone who doesn't want to, and should not let one or two people dominate[^sim2019focus-e13]. In practice: say to a heavy talker, "Thanks, let's hear from some others too," then look toward someone who hasn't spoken yet; and open with a question everyone answers in turn, so that each person has spoken once.
- **Give private views a way out.** After the discussion, you can hand out a short questionnaire or arrange a private conversation so each person has a chance to record views they didn't feel able to voice in the group[^kitzinger1995qualitative-e14].
- **Online focus groups need extra thought**: they reach only people with internet access, connections drop, and nonverbal cues are hard to capture[^nyumba2018use-e9].

**Why:** In a focus group, the interaction is the data. If the moderator keeps asking and evaluating, the session becomes question and answer; if the moderator lets go entirely, one or two people take over the discussion.

**Where people go wrong:** Taking surface agreement in the group for real consensus. Group norms can silence individual dissent[^kitzinger1995qualitative-e4].

### Step 5: Record and transcribe

**How:**

- **Record and transcribe.** Group discussions are best audio-recorded and transcribed; if that isn't possible, take careful notes[^kitzinger1995qualitative-e15].
- **The assistant takes the notes.** Note-taking is mainly the assistant moderator's job; don't expect the moderator to take notes while running the discussion[^krueger2002designing-e11]. The assistant also looks after the recording equipment[^krueger2002designing-e3].
- **Mark who is speaking in the transcript.** Identify the moderator's comments, and identify the speaker of each comment as far as you can[^krueger2002designing-e16]. Use brackets to note sounds such as laughter or raised voices, and note who was interrupted[^krueger2002designing-e17].
- **Debrief the same day.** Right after each group, the moderator and assistant debrief together, noting themes, hunches, and ideas, and comparing with other groups[^krueger2002designing-e12].
- **Allow enough time.** Krueger estimates that one hour of recording takes about eight hours to transcribe[^krueger2002designing-e16]. For other points on transcription, see [Step 4 of Interview studies](interview_study.md#step-4-transcribe).

**Why:** People talking at once and interrupting each other is what makes group recordings hardest to transcribe. If you can't tell who said what, you can't later analyze who changed their mind or who shut whom down.

**Where people go wrong:** Using automatic transcription as is, without marking speakers. Automatic transcription tools often can't tell speakers apart in a multi-person conversation; correct the transcript against the recording and the assistant's seating chart and notes.

### Step 6: Analysis: treat the interaction as data

**How:**

- **The basics are the same as in other qualitative analysis**: coding, developing themes, looking for counterexamples; see [Step 5 of Interview studies](interview_study.md#step-5-coding-and-thematic-analysis). Both data collection and analysis should attend to the content of the conversation and to the interaction within the group[^sim2019focus-e2].
- **The group or the individual as the unit?** Most guidelines recommend the group as the unit of analysis[^carlsen2011what-e3]. Kitzinger cautions that reports generally should not give percentages, that you should distinguish individual opinions voiced against group pressure from genuine group consensus, and that you should analyze cases that go against the mainstream[^kitzinger1995qualitative-e16]. In practice you can work at both levels: first summarize, group by group, how each question was discussed, then compare across groups and segments; when you quote an individual, say what discussion the remark came up in and how others in the group responded. Krueger likewise recommends debriefing right after each group and comparing it with other groups[^krueger2002designing-e12].
- **Code the interaction.** Kitzinger argues that the only distinctive feature of analyzing focus group data is accounting for the influence of group dynamics and making use of the interaction among participants; you can create codes for types of narrative, such as jokes and anecdotes, and for types of interaction, such as questions, agreeing with others, censorship, and changes of mind[^kitzinger1995qualitative-e17].
- **Look at context.** Every comment was triggered by some stimulus, either the moderator's question or someone else's remark; find that stimulus when you analyze[^krueger2002designing-e13]. Participants may change or even reverse their positions after interacting with others; when that happens, follow the conversation for clues that might explain the change[^krueger2002designing-e14].
- **Specific experiences carry more weight than vague generalities**[^krueger2002designing-e15].
- **Frequent does not mean important**: how often an issue comes up in the data says nothing about how important it is for understanding the phenomenon you study[^hennink2019what-e5].

**Why:** The same sentence carries different weight when someone says it first and when someone says it to go along with others. If you chop the group record into single sentences and code each in isolation, you lose the most valuable part of a focus group.

**Where people go wrong:** Reporting "6 out of 8 people agreed" as a proportion. In a group, the later "agreements" may just be people going along[^kitzinger1995qualitative-e16].

### Step 7: Ethics: confidentiality doesn't depend on you alone

Focus groups raise ethical issues that are not quite the same as those of one-on-one interviews[^sim2019focus-e3]. Here are the ones specific to groups.

**How:**

- **Be clear about what you can and can't guarantee.** Sim and Waterfield distinguish two kinds of confidentiality: the researcher can guarantee "external confidentiality," because they control what goes into reports; "internal confidentiality" (whether group members repeat what others said) depends on members keeping to the ground rules, and the researcher has little control over it[^sim2019focus-e7]. The researcher can give some assurances, but strictly speaking only about the part they can influence[^sim2019focus-e11]. So in your consent form and opening remarks, don't say "everything you say here will be kept completely confidential." Say instead: "The research team will keep what you say confidential. We also ask everyone not to repeat what others say outside this room, but we can't guarantee that on other people's behalf." Note that the sample opening in Krueger's 2002 handout says complete confidentiality can be assured[^krueger2002designing-e7]; by Sim and Waterfield's analysis, that promise goes beyond what a researcher can control.
- **Stress at the start that this is a public setting.** In the briefing before the discussion, you can stress that a focus group is a public setting, that everyone needs to respect each other's confidentiality and anonymity, and which topics are not suitable to raise in the group[^sim2019focus-e12].
- **Explain the withdrawal rules up front.** Leaving a group discussion partway through is a public act that can disrupt the discussion, and individuals may find it hard to do[^sim2019focus-e5]. Sim and Waterfield recommend making clear during informed consent that people can leave the group and can ask not to be quoted in reports, but that withdrawing their data before analysis is not possible[^sim2019focus-e6]. Each person must consent individually; the group's agreement cannot stand in for each person's consent[^nyumba2018use-e11].
- **Guard against people disclosing too much.** In the public setting of a group, things said are harder to "take back" than in a one-on-one interview[^sim2019focus-e9]. The moderator should watch for distress, disclosure of other people's private information, or someone saying too much, and steer the conversation away when needed[^sim2019focus-e13]. After discussing a distressing topic, it is best to close on a neutral or positive one[^sim2019focus-e14]; afterward, the moderator can stay a little longer so individual participants have a chance to raise concerns privately[^sim2019focus-e15].
- **Prevent identification in reports.** You can omit some details, attribute quotes to a category of participant rather than to a pseudonymous individual, or alter other details that could reveal identity[^sim2019focus-e10].

**Why:** What happens in a focus group depends partly on the other participants, who may bring up topics the moderator neither planned nor anticipated[^sim2019focus-e4]. The presence of other participants in itself compromises confidentiality[^kitzinger1995qualitative-e4].

**Where people go wrong:** Convening a group within one company or one open-source community to discuss "whose code on the team is most likely to contain vulnerabilities." The participants will keep working together afterward, and what they said can't be taken back.

### Step 8: Write the report

**How:**

- **Report what you did**: how many people per group, how many groups, how you recruited, how long each session lasted, how you segmented, and who moderated. In O.Nyumba et al.'s review of 170 conservation studies, more than half did not report sample size, 55% did not report group size, and 32% did not say how many sessions were held[^nyumba2018use-e10]; in the health studies surveyed by Carlsen and Glenton, only 17% tried to justify the number of groups[^carlsen2011what-e7].
- **Show conversations, not just single sentences.** A focus group report that is faithful to the data should present at least some exchanges between participants, not only isolated quotes stripped of context[^kitzinger1995qualitative-e18].
- **When you combine methods, make clear which conclusions come from the focus groups.** Of the 170 studies reviewed by O.Nyumba et al., 144 used focus groups together with other methods, and in most of them it was hard to tell which results came from the focus groups[^nyumba2018use-e16].
- **Check yourself against a reporting guideline.** Health research commonly uses COREQ (Consolidated Criteria for Reporting Qualitative Research), a 32-item checklist for interviews and focus groups[^equatorcoreq-e1].

**Why:** Readers rely on this information to judge how far your conclusions reach. If you don't say how many people were in each group and who they were, readers can't tell whether a "consensus" was real or driven by one person.

**Where people go wrong:** Writing only "we conducted focus groups," without saying how many people per group, how you recruited, or how the sessions were moderated. For general criteria of trustworthiness, see [Step 6 of Interview studies](interview_study.md#step-6-make-your-analysis-trustworthy).

---

## 3. Checklist

This checklist is this handbook's own summary of the sources above, not an official standard; when you submit in health research, follow COREQ and your field's other norms.

**Must do**

- [ ] Explain why you used focus groups rather than individual interviews or a questionnaire: you need the interaction and the views within a group[^kitzinger1995qualitative-e19]
- [ ] Describe how the groups were composed (homogeneous or mixed, whether members knew each other, whether there were hierarchical relationships)[^kitzinger1995qualitative-e8]
- [ ] Report group size, number of groups, how you recruited, and session length[^nyumba2018use-e10]
- [ ] Justify the number of groups; if you used saturation, show that you analyzed while collecting[^carlsen2011what-e8]
- [ ] Record and transcribe, or keep detailed notes[^kitzinger1995qualitative-e15]
- [ ] In analysis, distinguish individual opinion from group consensus, and don't give percentages[^kitzinger1995qualitative-e16]
- [ ] In informed consent, explain what the researcher can guarantee and that confidentiality within the group depends on everyone[^sim2019focus-e7][^sim2019focus-e11]

**Better practice**

- [ ] Have two people, a moderator and an assistant[^nyumba2018use-e7]
- [ ] Segment by the characteristics you want to compare, with about two groups per segment[^hennink2019what-e2]
- [ ] Plan a range for the number of groups in advance, and use saturation during collection to decide where to stop[^hennink2019what-e8]
- [ ] Code the interaction (agreeing, contradicting, changing one's mind, and so on)[^kitzinger1995qualitative-e17]
- [ ] Present stretches of conversation in the report, not just single sentences[^kitzinger1995qualitative-e18]
- [ ] Offer a chance to express views privately after the discussion[^kitzinger1995qualitative-e14]

**Outstanding**

- [ ] Publish the moderator's guide, the codebook, and coding examples
- [ ] Combine focus groups with individual interviews or a questionnaire, and say clearly which conclusions each one supports[^nyumba2018use-e16]
- [ ] Report the moderator's background and relationship to the participants, and reflect on how these shaped the discussion (reflexivity; see [Step 6 of Interview studies](interview_study.md#step-6-make-your-analysis-trustworthy))

**Fine to skip; not a flaw**

- Statistical representativeness, when the aim is to understand the views of a particular group (for quality criteria in qualitative research, see [Interview studies](interview_study.md#first-remember-qualitative-research-has-different-quality-criteria-from-quantitative-research))
- Hitting exactly the number a particular book recommends, as long as groups have 4 to 12 people[^carlsen2011what-e4]
- Running only one or two groups, when you use focus groups only to draft questionnaire items and test their wording (this use is described in Section 1)

---

## 4. Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Treating a focus group as "interviewing several people at once" and asking each person in turn | What defines a focus group is that it uses the interaction within the group[^kitzinger1995qualitative-e1] |
| Putting managers and their staff in the same group | Hierarchy affects who dares to speak[^kitzinger1995qualitative-e8] |
| Groups of a dozen or more | Hard to manage, and may split into side conversations[^nyumba2018use-e6] |
| Drawing conclusions from a single group | The rule of thumb is 2 to 5 groups per category of participant[^carlsen2011what-e6] |
| Running every group before analyzing, then claiming saturation | Saturation requires analyzing while you collect[^carlsen2011what-e8] |
| Letting one or two people dominate | Dominance and groupthink distort the data[^nyumba2018use-e15] |
| The moderator taking notes while moderating | The assistant should take notes[^krueger2002designing-e11] |
| Reporting "75% of participants felt that..." | Focus group data generally should not be reported as percentages[^kitzinger1995qualitative-e16] |
| Promising participants "complete confidentiality" | The researcher can't control whether group members repeat what was said[^sim2019focus-e7] |
| Presenting only isolated single-sentence quotes | You should show exchanges between participants[^kitzinger1995qualitative-e18] |

---

## 5. Further reading

- **Introduction**: Kitzinger 1995, part of the *BMJ*'s "Qualitative Research" series. In four pages it covers what focus groups are for, group composition, moderation, and analysis, with particular emphasis on how to use interaction. From health research.
- **Practical checklists for moderating and questioning**: Krueger's 2002 handout, with a sample opening, the five question types, the assistant's duties, and key points on transcription and analysis. *Focus Groups: A Practical Guide for Applied Research* by Krueger and Casey is the fuller version, but it is not freely available.
- **Ethics**: Sim & Waterfield 2019, a systematic discussion of informed consent, confidentiality, and risk of harm in focus groups, with measures for four stages: informed consent, the opening briefing, moderation, and the debrief afterward.
- **How many groups**: Hennink, Kaiser & Weber 2019 used data from 10 focus groups to test how many groups code saturation and meaning saturation require; Carlsen & Glenton 2011 surveyed how health research reports the number of groups.
- **How another field uses them**: O.Nyumba et al. 2018 reviewed twenty years of focus group research in conservation biology and end with five recommendations, including on moderator skills and group biases.

For links to all sources, see the [source list](../../sources/README.md).

[^carlsen2011what-e1]: Carlsen & Glenton 2011, Background. [Evidence](../../sources/notes/carlsen2011what.md#e1)
[^carlsen2011what-e2]: Carlsen & Glenton 2011, Background. [Evidence](../../sources/notes/carlsen2011what.md#e2)
[^carlsen2011what-e3]: Carlsen & Glenton 2011, Background. [Evidence](../../sources/notes/carlsen2011what.md#e3)
[^carlsen2011what-e4]: Carlsen & Glenton 2011, Background. [Evidence](../../sources/notes/carlsen2011what.md#e4)
[^carlsen2011what-e5]: Carlsen & Glenton 2011, Background. [Evidence](../../sources/notes/carlsen2011what.md#e5)
[^carlsen2011what-e6]: Carlsen & Glenton 2011, Background. [Evidence](../../sources/notes/carlsen2011what.md#e6)
[^carlsen2011what-e7]: Carlsen & Glenton 2011, Abstract. [Evidence](../../sources/notes/carlsen2011what.md#e7)
[^carlsen2011what-e8]: Carlsen & Glenton 2011, Abstract. [Evidence](../../sources/notes/carlsen2011what.md#e8)
[^carlsen2011what-e9]: Carlsen & Glenton 2011, Discussion. [Evidence](../../sources/notes/carlsen2011what.md#e9)
[^equatorcoreq-e1]: EQUATOR Network, COREQ item headings. [Evidence](../../sources/notes/equatorcoreq.md#e1)
[^hennink2019what-e1]: Hennink et al. 2019, Abstract. [Evidence](../../sources/notes/hennink2019what.md#e1)
[^hennink2019what-e2]: Hennink et al. 2019, Abstract. [Evidence](../../sources/notes/hennink2019what.md#e2)
[^hennink2019what-e3]: Hennink et al. 2019, Introduction. [Evidence](../../sources/notes/hennink2019what.md#e3)
[^hennink2019what-e4]: Hennink et al. 2019, Discussion. [Evidence](../../sources/notes/hennink2019what.md#e4)
[^hennink2019what-e5]: Hennink et al. 2019, Discussion. [Evidence](../../sources/notes/hennink2019what.md#e5)
[^hennink2019what-e6]: Hennink et al. 2019, Discussion. [Evidence](../../sources/notes/hennink2019what.md#e6)
[^hennink2019what-e7]: Hennink et al. 2019, Discussion. [Evidence](../../sources/notes/hennink2019what.md#e7)
[^hennink2019what-e8]: Hennink et al. 2019, Discussion. [Evidence](../../sources/notes/hennink2019what.md#e8)
[^kitzinger1995qualitative-e1]: Kitzinger 1995, p. 299. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e1)
[^kitzinger1995qualitative-e2]: Kitzinger 1995, p. 299. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e2)
[^kitzinger1995qualitative-e3]: Kitzinger 1995, box on p. 299. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e3)
[^kitzinger1995qualitative-e4]: Kitzinger 1995, p. 300. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e4)
[^kitzinger1995qualitative-e5]: Kitzinger 1995, p. 300. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e5)
[^kitzinger1995qualitative-e7]: Kitzinger 1995, p. 300. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e7)
[^kitzinger1995qualitative-e8]: Kitzinger 1995, p. 300. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e8)
[^kitzinger1995qualitative-e9]: Kitzinger 1995, p. 300. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e9)
[^kitzinger1995qualitative-e10]: Kitzinger 1995, p. 301. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e10)
[^kitzinger1995qualitative-e11]: Kitzinger 1995, p. 301. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e11)
[^kitzinger1995qualitative-e12]: Kitzinger 1995, p. 301. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e12)
[^kitzinger1995qualitative-e13]: Kitzinger 1995, p. 301. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e13)
[^kitzinger1995qualitative-e14]: Kitzinger 1995, p. 301. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e14)
[^kitzinger1995qualitative-e15]: Kitzinger 1995, p. 301. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e15)
[^kitzinger1995qualitative-e16]: Kitzinger 1995, p. 301. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e16)
[^kitzinger1995qualitative-e17]: Kitzinger 1995, pp. 301–302. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e17)
[^kitzinger1995qualitative-e18]: Kitzinger 1995, p. 302. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e18)
[^kitzinger1995qualitative-e19]: Kitzinger 1995, p. 302. [Evidence](../../sources/notes/kitzinger1995qualitative.md#e19)
[^krueger2002designing-e1]: Krueger 2002, p. 1. [Evidence](../../sources/notes/krueger2002designing.md#e1)
[^krueger2002designing-e3]: Krueger 2002, p. 2. [Evidence](../../sources/notes/krueger2002designing.md#e3)
[^krueger2002designing-e4]: Krueger 2002, p. 2. [Evidence](../../sources/notes/krueger2002designing.md#e4)
[^krueger2002designing-e5]: Krueger 2002, p. 2. [Evidence](../../sources/notes/krueger2002designing.md#e5)
[^krueger2002designing-e6]: Krueger 2002, p. 3. [Evidence](../../sources/notes/krueger2002designing.md#e6)
[^krueger2002designing-e7]: Krueger 2002, p. 4. [Evidence](../../sources/notes/krueger2002designing.md#e7)
[^krueger2002designing-e8]: Krueger 2002, p. 6. [Evidence](../../sources/notes/krueger2002designing.md#e8)
[^krueger2002designing-e9]: Krueger 2002, p. 6. [Evidence](../../sources/notes/krueger2002designing.md#e9)
[^krueger2002designing-e10]: Krueger 2002, p. 7. [Evidence](../../sources/notes/krueger2002designing.md#e10)
[^krueger2002designing-e11]: Krueger 2002, p. 9. [Evidence](../../sources/notes/krueger2002designing.md#e11)
[^krueger2002designing-e12]: Krueger 2002, p. 10. [Evidence](../../sources/notes/krueger2002designing.md#e12)
[^krueger2002designing-e13]: Krueger 2002, p. 11. [Evidence](../../sources/notes/krueger2002designing.md#e13)
[^krueger2002designing-e14]: Krueger 2002, p. 11. [Evidence](../../sources/notes/krueger2002designing.md#e14)
[^krueger2002designing-e15]: Krueger 2002, p. 11. [Evidence](../../sources/notes/krueger2002designing.md#e15)
[^krueger2002designing-e16]: Krueger 2002, p. 15. [Evidence](../../sources/notes/krueger2002designing.md#e16)
[^krueger2002designing-e17]: Krueger 2002, p. 15. [Evidence](../../sources/notes/krueger2002designing.md#e17)
[^nyumba2018use-e2]: O.Nyumba et al. 2018, §1, p. 21. [Evidence](../../sources/notes/nyumba2018use.md#e2)
[^nyumba2018use-e3]: O.Nyumba et al. 2018, §1, p. 21. [Evidence](../../sources/notes/nyumba2018use.md#e3)
[^nyumba2018use-e4]: O.Nyumba et al. 2018, §2.1, p. 22. [Evidence](../../sources/notes/nyumba2018use.md#e4)
[^nyumba2018use-e5]: O.Nyumba et al. 2018, §2.1, p. 23. [Evidence](../../sources/notes/nyumba2018use.md#e5)
[^nyumba2018use-e6]: O.Nyumba et al. 2018, §2.1, p. 23. [Evidence](../../sources/notes/nyumba2018use.md#e6)
[^nyumba2018use-e7]: O.Nyumba et al. 2018, §2.2, p. 23. [Evidence](../../sources/notes/nyumba2018use.md#e7)
[^nyumba2018use-e8]: O.Nyumba et al. 2018, §2.2, p. 23. [Evidence](../../sources/notes/nyumba2018use.md#e8)
[^nyumba2018use-e9]: O.Nyumba et al. 2018, §3.7, p. 24. [Evidence](../../sources/notes/nyumba2018use.md#e9)
[^nyumba2018use-e10]: O.Nyumba et al. 2018, §5, p. 25. [Evidence](../../sources/notes/nyumba2018use.md#e10)
[^nyumba2018use-e11]: O.Nyumba et al. 2018, §7, p. 27. [Evidence](../../sources/notes/nyumba2018use.md#e11)
[^nyumba2018use-e12]: O.Nyumba et al. 2018, §10, p. 28. [Evidence](../../sources/notes/nyumba2018use.md#e12)
[^nyumba2018use-e13]: O.Nyumba et al. 2018, §10, p. 29. [Evidence](../../sources/notes/nyumba2018use.md#e13)
[^nyumba2018use-e14]: O.Nyumba et al. 2018, §11, p. 29. [Evidence](../../sources/notes/nyumba2018use.md#e14)
[^nyumba2018use-e15]: O.Nyumba et al. 2018, §11, p. 30. [Evidence](../../sources/notes/nyumba2018use.md#e15)
[^nyumba2018use-e16]: O.Nyumba et al. 2018, §11, p. 30. [Evidence](../../sources/notes/nyumba2018use.md#e16)
[^sim2019focus-e1]: Sim & Waterfield 2019, §1.1. [Evidence](../../sources/notes/sim2019focus.md#e1)
[^sim2019focus-e2]: Sim & Waterfield 2019, §1.1. [Evidence](../../sources/notes/sim2019focus.md#e2)
[^sim2019focus-e3]: Sim & Waterfield 2019, Abstract. [Evidence](../../sources/notes/sim2019focus.md#e3)
[^sim2019focus-e4]: Sim & Waterfield 2019, §2.1. [Evidence](../../sources/notes/sim2019focus.md#e4)
[^sim2019focus-e5]: Sim & Waterfield 2019, §2.2. [Evidence](../../sources/notes/sim2019focus.md#e5)
[^sim2019focus-e6]: Sim & Waterfield 2019, §2.2. [Evidence](../../sources/notes/sim2019focus.md#e6)
[^sim2019focus-e7]: Sim & Waterfield 2019, §3.1. [Evidence](../../sources/notes/sim2019focus.md#e7)
[^sim2019focus-e8]: Sim & Waterfield 2019, §3.1. [Evidence](../../sources/notes/sim2019focus.md#e8)
[^sim2019focus-e9]: Sim & Waterfield 2019, §3.1. [Evidence](../../sources/notes/sim2019focus.md#e9)
[^sim2019focus-e10]: Sim & Waterfield 2019, §3.1. [Evidence](../../sources/notes/sim2019focus.md#e10)
[^sim2019focus-e11]: Sim & Waterfield 2019, §5, informed consent. [Evidence](../../sources/notes/sim2019focus.md#e11)
[^sim2019focus-e12]: Sim & Waterfield 2019, §5, opening briefing. [Evidence](../../sources/notes/sim2019focus.md#e12)
[^sim2019focus-e13]: Sim & Waterfield 2019, §5, moderating the discussion. [Evidence](../../sources/notes/sim2019focus.md#e13)
[^sim2019focus-e14]: Sim & Waterfield 2019, §5, moderating the discussion. [Evidence](../../sources/notes/sim2019focus.md#e14)
[^sim2019focus-e15]: Sim & Waterfield 2019, §5, debriefing afterward. [Evidence](../../sources/notes/sim2019focus.md#e15)
