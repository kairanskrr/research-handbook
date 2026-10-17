# Being a reviewer

> Most of the sources on this page come from computer science (programming languages, systems, software engineering, machine learning), plus guidelines from the American Philosophical Association and the American Mathematical Society; the examples are from computer science. Reviewing rules differ a lot between journals and conferences, so before you start, read the reviewer instructions of the venue that invited you.

## When you need this page

- You have received your first review invitation and don't know whether to accept it, or what to do if you do;
- Your advisor has asked you to look at a paper they are reviewing and write a first draft of the review;
- You have written a few reviews, but they feel thin or harsh, or you are never sure whether to recommend acceptance or rejection.

Peer review does two jobs: it judges whether the research is good, and it gives the authors feedback that helps them improve it[^hicks2014reviewing-e1]. The second job holds whether or not the paper is accepted in the end[^roscoe2007reviews-e1]. So your role is to help the authors, even when your verdict is rejection[^bourne2006reviewers-e4].

Reviewing is also practice. Reviewing other people's papers helps you write your own. A good way to start is with your advisor: ask them to pass you a paper they are reviewing and write the first draft yourself[^bourne2005published-e4]. But manuscripts are confidential: if the journal uses anonymous review, you may not show a manuscript to colleagues without the editor's permission[^bourne2006reviewers-e11]. So before your advisor hands you a paper, they should make sure the journal or conference allows it, or that the editor has agreed. If you are not sure, just ask your advisor `[Our analysis]`.

---

## 1. Should you accept the invitation?

**How:** When an invitation arrives, answer these three questions quickly, then accept or decline.

1. **Can I finish on time?** If not, decline. Learn to say no[^bourne2006reviewers-e1].
2. **Do I have a conflict of interest?** If there is any chance of one, don't accept[^bourne2006reviewers-e2]. If you are unsure, tell the editor or the program committee chair and let them decide[^mightreview-e2] (the next section lists typical conflicts).
3. **Do I know this area?** If not at all, decline or tell the editor honestly. If you can't follow parts of the paper, you can still accept, but say in your review which parts you cannot judge `[Our analysis]` (Section 5 shows how).

**Reply quickly.** Whether you accept or not, answer early. The American Philosophical Association's guidelines for journal refereeing ask referees to respond within a week of the invitation at most[^apaphil2022journal-e11]. That is a rule for philosophy journals; in other fields, go by the invitation email. The reason for replying early is the same everywhere `[Our analysis]`.

**Why:** The American Philosophical Association's guidelines describe refereeing as a professional duty of every member of the field: unpaid service from which everyone benefits[^apaphil2022journal-e10]. If you sit on an invitation, or accept and then fail to deliver, you waste the authors' and the editor's time `[Our analysis]`.

**Where people go wrong:** Newcomers often accept papers they have no time for, or can't follow, because "it's my first invitation and it would be awkward to say no". Declining is not rude. Accepting and then handing in a careless review is what actually hurts the authors `[Our analysis]`.

**Write it down:** Open the invitation email and write down the deadline, how long you expect the review to take, and any relationship you might have with the authors. Click "accept" only if all three are fine.

## 2. Keep it confidential and declare conflicts of interest

**How:**

- **Keep it confidential.** The submission was given to you in confidence: don't reveal where a paper has been submitted, and don't pass it on to anyone[^hicks2014reviewing-e7].
- **Don't give the manuscript to a large language model.** Pasting a manuscript into a large language model also hands it to a third party `[Our analysis]`. One conference as an example: the machine learning conference NeurIPS 2025 (Conference on Neural Information Processing Systems) requires everything in the review process to stay confidential; reviewers may not discuss or share submissions with anyone, including any large language model[^neurips2025llm-e1]. Without sharing the manuscript, reviewers may use a large language model or other resources to understand a concept, or to check the grammar and wording of their review[^neurips2025llm-e3]. Whatever tools they use, reviewers are responsible for the quality and accuracy of their review[^neurips2025llm-e4]. This is one conference's rule for one year; rules differ between venues and keep changing, so follow the inviting venue's instructions for that year `[Our analysis]`.
- **Declare conflicts of interest.** The American Philosophical Association's guidelines for journal refereeing say: if there is a potential conflict of interest, tell the editor, especially if you know who the author is[^apaphil2022journal-e9]. The American Mathematical Society's ethical guidelines likewise require you to step out of the decision when there is a conflict of interest[^ams2022ethical-e7].
- **Don't try to find out who the authors are.** The American Philosophical Association's guidelines note that many philosophy papers are online before submission, so a quick search would reveal the author; the guidelines ask referees not to go looking[^apaphil2022journal-e8]. Preprints are common in other fields too; under anonymous review, do the same `[Our analysis]`.

**Common conflicts of interest** (computer science examples `[Our analysis]`): the author is your advisor, your student, someone in your group, or a recent collaborator; you have a personal grudge with the author; the paper works on exactly the problem you are working on.

The last one is the easiest to miss. One professor's reviewing guide for graduate students calls it a "scholarly conflict" and advises telling the chair or editor about such a paper and staying out of the discussion of it[^mightreview-e10]. Say you are working on "detecting reentrancy vulnerabilities in smart contracts with large language models" and the paper you receive does exactly that. You will find it hard to judge it without self-interest, so declare it `[Our analysis]`.

**Why:** Review is usually anonymous, and reviewers hold a lot of power with little accountability[^roscoe2007reviews-e8]. Confidentiality and recusal are there so that this power is not used to harm authors `[Our analysis]`.

**Where people go wrong:** Thinking "I'm just asking a senior student to take a quick look" or "I'm just pasting the abstract into a large language model for a summary" is harmless. Both hand a confidential manuscript to a third party `[Our analysis]`.

**Write it down:** In your reply accepting the invitation, or in the review system, list every relationship you might have with the authors. Include the ones you are unsure about and let the editor or chair decide.

## 3. Read the paper like a reviewer

**How:** Read with four questions in mind[^hicks2014reviewing-e2]:

1. Is the idea or the study interesting or useful?
2. Is it new, or does it overlap heavily with existing work?
3. Are the paper's conclusions correct?
4. Is it written clearly enough for others to understand?

The ACM SIGSOFT Empirical Standards (standards for reviewing empirical research, from the Association for Computing Machinery's Special Interest Group on Software Engineering; "the software engineering review standards" below) put **trustworthiness before importance**: a trustworthy paper can be accepted even if it is not important; a paper that is not trustworthy cannot be accepted, however important it seems[^ralph2020empirical-e53].

As you read, first note your gut reaction and the reasons for it. Acknowledging your gut reaction helps you avoid looking only for evidence that confirms it[^mightreview-e4]. Then go through the paper section by section and check whether that first impression holds up `[Our analysis]`.

**When judging novelty, watch for these mistakes:**

- **Mistaking complexity for novelty.** A guide to novelty for reviewers points out that reviewers often take complex, difficult or highly technical work to be novel[^black2022novelty-e1]. A single change that nobody thought of before is novel in itself[^black2022novelty-e2].
- **Hindsight.** Judge novelty from where things stood before the idea appeared[^black2022novelty-e3]. Thinking "isn't this obvious?" after reading the paper is no reason to call it not novel.
- **Looking only at technical novelty.** A new dataset can be novel even if every method it uses is known, as long as it does something other datasets don't; the same goes for a new use of an old method[^black2022novelty-e4].
- **Overlap with existing work.** Overlap does not mean nothing is new: if a paper offers new ideas and useful data, it still has some novelty[^hicks2014reviewing-e8].

> **Where sources disagree: should you read every word from start to finish?**
> - **You can skim the middle.** One programming languages researcher's advice on reviewing: read the introduction, conclusion and related work carefully, and skim the middle[^hicks2014reviewing-e11].
> - **You must read every word.** The software engineering review standards list "skimming a manuscript instead of carefully reading each word and inspecting each figure and table" as a reviewing antipattern[^ralph2020empirical-e58].
>
> **Our suggestion** `[Our analysis]`: start with the introduction and conclusion to see what the paper is trying to show; but whenever you are going to judge whether a conclusion is right, read the part that supports it carefully. If you only read part of the paper, treat that as one of your limitations and say so in your review (the software engineering review standards ask reviewers to state their own limitations and biases[^ralph2020empirical-e55]).

**Write it down:** After reading, without looking at the paper, write three to five sentences: what it is trying to show, what evidence it uses, and what your first impression is. If you can't, you haven't understood it yet; read it again.

## 4. Judge it by its own research strategy

**How:** First work out which [Research strategies](../05_research-strategies/README.md) the paper's central claim belongs to, then judge it by that strategy's standards.

The software engineering review standards say there are no universal quality criteria: each study should be evaluated against the standards for the method that fits it. Don't apply criteria that don't fit, such as demanding internal validity (whether a causal conclusion really holds) from a study that makes no causal claim[^ralph2020empirical-e24]. Some examples from "large language models and smart contract security" `[Our analysis]`:

| The paper's claim | Strategy | Ask | Don't ask |
|---|---|---|---|
| "40% of contracts generated by large language models have reentrancy vulnerabilities" | Description | Is the sample representative? How was "has a vulnerability" decided? | "Why does this happen?" (that's a different paper) |
| "Existing benchmarks suffer from data leakage" | Measurement | Is the method for detecting leakage accurate? How do conclusions change once leaked samples are removed? | "Where is your new detection method?" |
| "On real contracts, tool A's detection rate is higher than B's" | Comparative evaluation | Is the comparison fair? Does the benchmark favor one tool? | "Why didn't you propose a new tool?" |
| "The new method finds 30% more vulnerabilities" | Building and improving | Are the baselines strong enough? Is the benchmark leaked? | "You should have done a large observational study first" |

For what evidence each strategy needs, see the strategy pages, for example [Building and improving](../05_research-strategies/build_improve.md) and [Comparative evaluation](../05_research-strategies/compare_evaluate.md).

**Don't raise criticisms that don't hold up.** Examples: rejecting a paper because its results are negative, or dismissing it only because you would have used a different method. The software engineering review standards include a list of "invalid criticisms" that authors can push back on with good reasons; see [Reviews, revision, and what to do after rejection](../03_write-and-publish/03_review-and-revision.md#3-decide-what-to-change-and-what-to-argue). When you are the reviewer, check yourself against that list first `[Our analysis]`.

**Why:** Each strategy has its own idea of "enough". Holding an observational study to the standards of building and improving and asking it to "propose a new method" is asking the authors to write a different paper `[Our analysis]`.

**Where people go wrong:** Criticizing the choice of participants in general terms, for example "using students as participants is not acceptable". A group of experts on software engineering experiments advises reviewers not to treat this as a general rule that holds for every experiment, but to explain specifically why it is inappropriate in the particular circumstances of this experiment[^falessi2018empirical-e6].

**Write it down:** Write one sentence: "This paper's central claim is …, which is a … strategy." Then list the two or three questions that matter most for that strategy. Your main comments should be about those questions.

## 5. Write a useful review

**How:** Use this structure.

1. **Summary.** In your own words, neutrally describe what the paper is about, where the authors are coming from, why they think the problem matters, and what they did[^roscoe2007reviews-e3], without judging it[^hicks2014reviewing-e3]. This shows the authors and the other reviewers whether you understood the paper `[Our analysis]`.
2. **Contribution.** State what you think the paper's contribution is[^roscoe2007reviews-e4].
3. **Main comments.** Put the most important points first and details later[^hicks2014reviewing-e5]. Number them so they are easy to read and respond to, and say how critical each one is to acceptance[^bourne2006reviewers-e5]. The software engineering review standards also recommend distinguishing required changes from suggestions, ideally in separate lists[^ralph2020empirical-e54].
4. **Strengths.** Write down what impressed you in the paper too[^roscoe2007reviews-e6].
5. **Minor issues.** Typos, unclear wording and the like go last `[Our analysis]`. The American Philosophical Association's guidelines warn against giving too much weight to small writing problems; they may just mean the author is not a native English speaker[^apaphil2022journal-e15].
6. **Recommendation and reasons** (see Section 6).

**How to write each criticism:**

- **Be specific.** Give specific, well-organized reasons for both criticism and praise[^bourne2006reviewers-e3]. The software engineering review standards list vague criticisms that the authors cannot act on as an antipattern[^ralph2020empirical-e56]: if you say "details are missing", say which ones[^ralph2020empirical-e61]; if you say "not novel", cite published work with nearly the same contribution[^ralph2020empirical-e60].
- **Suggest a fix.** When you criticize something, also suggest how to improve it[^mightreview-e5]. With a little thought, every negative comment can be rewritten as a constructive suggestion[^roscoe2007reviews-e9]. For example, instead of "this has all been done before", write "the paper would be more convincing if it explained what it adds beyond such-and-such work"[^roscoe2007reviews-e15].
- **When you suspect an error, ask instead of asserting**[^roscoe2007reviews-e5]. You may always have misunderstood the paper[^roscoe2007reviews-e10]. For example, instead of "the experiment suffers from data leakage", write "Could the contracts in the benchmark appear in the models' training data? How did the authors rule this out?" `[Our analysis]`
- **Be restrained when adding references.** Pointing out references the authors missed (not your own) is a brief and effective way to help[^bourne2006reviewers-e10].

**State your own limitations.** The software engineering review standards ask reviewers to reflect on and state their own limitations and biases[^ralph2020empirical-e55], such as which parts of the paper you cannot judge `[Our analysis]`. Most review forms have a "reviewer confidence" field; if you are unsure, it is fine to give yourself an honest low score[^roscoe2007reviews-e13].

**Why:** Having already spent hours reading the paper, it is well worth another half hour to an hour to help the authors improve it[^hicks2014reviewing-e12]. And writing the review tests your judgment: someone who has written a review is usually better placed to assess a paper than someone who has only read it[^roscoe2007reviews-e2].

**Write it down:** Once you have a draft, check each criticism in turn: could the authors act on it? If not, rewrite it or delete it.

## 6. Make a recommendation

**How:**

- **Give a clear recommendation with reasons**[^roscoe2007reviews-e7]. Don't sit on the fence; fence-sitting only drags out the process for nothing[^bourne2006reviewers-e6].
- **Make the text and the score agree.** The text is the substance; the score just summarizes it[^hicks2014reviewing-e4]. After reading your text, the authors should be able to guess your score `[Our analysis]`.
- **When recommending rejection, say what would change your mind**[^mightreview-e6]. That tells the authors what to work on next `[Our analysis]`.
- **Judge against the venue's standards.** To decide whether a paper is good enough, you need to know what this journal or conference, and this community, values[^hicks2014reviewing-e9]. In computer science, at least in theory, conference papers report complete, mature work, while workshop papers can be early work or position papers[^roscoe2007reviews-e12].
- **Comments for the editor only must also be backed by the review.** Many review forms have a field for confidential comments to the editor; anything you say there must be supported by the main review[^bourne2006reviewers-e9]. You can't write a mild review and then privately say "this should never be published" `[Our analysis]`. That field is also a good place to mention your own gaps and biases regarding the paper's content[^bourne2006reviewers-e12].

**Why:** Your recommendation is not the final decision. At computer science conferences, the program committee's aim is to select the best set of papers, not to pass judgment on each paper[^roscoe2007reviews-e14]; the outcome is the collective judgment of all the reviewers, "more art than science"[^hicks2014reviewing-e10]. Your job is to give the decision-makers a clear, reasoned judgment `[Our analysis]`.

**Where people go wrong:** The reviewing guide for graduate students mentioned earlier warns that reviews written by graduate students are among the most negative[^mightreview-e3]. Newcomers easily mistake "I can find lots of problems" for "this paper is bad". Before you start finding faults, list the paper's strengths `[Our analysis]`.

**Write it down:** Under your recommendation, write one sentence: "If the authors did …, I would change my recommendation to accept" (or "…, I would change it to reject"). Then check that your score matches your text `[Our analysis]`.

## 7. Keep to reviewing ethics

**How:**

- **Don't take ideas from the manuscript.** The American Mathematical Society's ethical guidelines require editors and referees to keep submissions confidential and, in particular, not to appropriate ideas from them[^ams2022ethical-e10]. NeurIPS 2025's rules are more specific: until a submission is public, don't use its ideas, code or results in your own work[^neurips2025llm-e1]; once it is public, you may use them only if the license the authors granted covers your use[^neurips2025llm-e2].
- **Don't use the review to promote yourself.** The software engineering review standards list using a review to promote your own views, theories, methods or papers as an antipattern[^ralph2020empirical-e57].
- **Don't judge by who the authors are.** Don't let the authors' past record sway you, positively or negatively[^mightreview-e8]; the software engineering review standards likewise say not to let the authors' identity or affiliation affect the review[^ralph2020empirical-e59].
- **Criticize the paper, not the people.** Even if the paper is weak throughout, respect the authors, and don't exaggerate[^hicks2014reviewing-e6]. Humor is fine, but don't mock the paper[^roscoe2007reviews-e11]; a review is not the place to show off your wit[^mightreview-e7]. Anonymity is a shield, not a sword[^mightreview-e9].
- **Don't reject something because it isn't what you expected.** The questionnaire survey part of the software engineering review standards lists these as invalid criticisms: the results are controversial or unsurprising; the results disagree with the reviewer's personal experience or with earlier studies[^ralph2020empirical-e249]. The same reasoning applies to other kinds of research `[Our analysis]`.

**Why:** A simple test: review others the way you would want to be reviewed[^mightreview-e1].

**Write it down:** Before you submit, reread your review as if someone had written it about your paper. Any sentence that would make you feel humiliated without giving you any idea how to improve: change it `[Our analysis]`.

---

## Common mistakes

| Mistake | Why it's wrong | What to do instead |
|---|---|---|
| Accepting a review you have no time for, then rushing it at the deadline | If you can't finish on time, you shouldn't accept[^bourne2006reviewers-e1] | Estimate the time before accepting; decline if you can't do it |
| Passing the manuscript to a labmate or pasting it into a large language model "to take a look" | Manuscripts are confidential and may not be passed on[^hicks2014reviewing-e7], and some conferences explicitly forbid giving them to large language models[^neurips2025llm-e1] | Use only resources that don't involve the manuscript's content to understand concepts |
| Reviewing a paper on the same problem you are working on, as if nothing were wrong | You should tell the editor or chair and recuse yourself[^mightreview-e10] | Declare it as soon as the invitation arrives |
| Demanding that an observational study "propose a new method", by the standards of building and improving | Quality criteria that don't fit should not be applied[^ralph2020empirical-e24] | Identify the strategy first and review by that strategy's standards |
| Writing "lacks novelty" or "incomplete related work" without citing specific work | The software engineering review standards list these as invalid criticisms[^ralph2020empirical-e60][^ralph2020empirical-e61] | Cite the closest published work and ask the authors to explain the difference |
| Listing only weaknesses, with no fixes | Vague criticism that the authors can't act on is an antipattern[^ralph2020empirical-e56] | Attach a suggested fix to each criticism |
| Mild text but a very low score | The score should summarize the text[^hicks2014reviewing-e4] | Compare text and score before submitting |
| Recommending "could go either way" | Fence-sitting drags out the process[^bourne2006reviewers-e6] | Give a clear recommendation with reasons; if unsure, lower your confidence score |
| Asking the authors to cite your own papers | Don't use a review to promote your own papers[^ralph2020empirical-e57] | Only add references the authors genuinely missed and that have nothing to do with you |

## Further reading

- How to identify a paper's central claim and which strategy it belongs to: [Research strategies](../05_research-strategies/README.md)
- The author's side, responding to reviews and revising: [Reviews, revision, and what to do after rejection](../03_write-and-publish/03_review-and-revision.md)
- Research integrity beyond reviewing: [Research integrity and ethics](integrity_and_ethics.md)
- External sources: Bourne & Korngreen, "Ten Simple Rules for Reviewers" (PLoS Computational Biology, 2006); Roscoe, "Writing reviews for systems conferences" (2007); the reviewing sections of the ACM SIGSOFT Empirical Standards.

[^hicks2014reviewing-e1]: Hicks 2014, opening. [Evidence](../../sources/notes/hicks2014reviewing.md#e1)
[^hicks2014reviewing-e2]: Hicks 2014, Judging the work. [Evidence](../../sources/notes/hicks2014reviewing.md#e2)
[^hicks2014reviewing-e3]: Hicks 2014, Start with a summary. [Evidence](../../sources/notes/hicks2014reviewing.md#e3)
[^hicks2014reviewing-e4]: Hicks 2014, Scores abstract text. [Evidence](../../sources/notes/hicks2014reviewing.md#e4)
[^hicks2014reviewing-e5]: Hicks 2014, Put the most important parts first. [Evidence](../../sources/notes/hicks2014reviewing.md#e5)
[^hicks2014reviewing-e6]: Hicks 2014, Be respectful. [Evidence](../../sources/notes/hicks2014reviewing.md#e6)
[^hicks2014reviewing-e7]: Hicks 2014, Confidentiality. [Evidence](../../sources/notes/hicks2014reviewing.md#e7)
[^hicks2014reviewing-e8]: Hicks 2014, Judging the work. [Evidence](../../sources/notes/hicks2014reviewing.md#e8)
[^hicks2014reviewing-e9]: Hicks 2014, Interesting or useful? [Evidence](../../sources/notes/hicks2014reviewing.md#e9)
[^hicks2014reviewing-e10]: Hicks 2014, Interesting or useful? [Evidence](../../sources/notes/hicks2014reviewing.md#e10)
[^hicks2014reviewing-e11]: Hicks 2014, Reading the paper. [Evidence](../../sources/notes/hicks2014reviewing.md#e11)
[^hicks2014reviewing-e12]: Hicks 2014, Suggestions for improvement. [Evidence](../../sources/notes/hicks2014reviewing.md#e12)
[^roscoe2007reviews-e1]: Roscoe 2007, §2, p. 1. [Evidence](../../sources/notes/roscoe2007reviews.md#e1)
[^roscoe2007reviews-e2]: Roscoe 2007, §2, p. 2. [Evidence](../../sources/notes/roscoe2007reviews.md#e2)
[^roscoe2007reviews-e3]: Roscoe 2007, §4, p. 3. [Evidence](../../sources/notes/roscoe2007reviews.md#e3)
[^roscoe2007reviews-e4]: Roscoe 2007, §4, p. 3. [Evidence](../../sources/notes/roscoe2007reviews.md#e4)
[^roscoe2007reviews-e5]: Roscoe 2007, §4, p. 4. [Evidence](../../sources/notes/roscoe2007reviews.md#e5)
[^roscoe2007reviews-e6]: Roscoe 2007, §4, p. 4. [Evidence](../../sources/notes/roscoe2007reviews.md#e6)
[^roscoe2007reviews-e7]: Roscoe 2007, §4, p. 4. [Evidence](../../sources/notes/roscoe2007reviews.md#e7)
[^roscoe2007reviews-e8]: Roscoe 2007, §5, p. 4. [Evidence](../../sources/notes/roscoe2007reviews.md#e8)
[^roscoe2007reviews-e9]: Roscoe 2007, §5, p. 5. [Evidence](../../sources/notes/roscoe2007reviews.md#e9)
[^roscoe2007reviews-e10]: Roscoe 2007, §5, p. 5. [Evidence](../../sources/notes/roscoe2007reviews.md#e10)
[^roscoe2007reviews-e11]: Roscoe 2007, §5, p. 5. [Evidence](../../sources/notes/roscoe2007reviews.md#e11)
[^roscoe2007reviews-e12]: Roscoe 2007, §4, p. 4. [Evidence](../../sources/notes/roscoe2007reviews.md#e12)
[^roscoe2007reviews-e13]: Roscoe 2007, §5, p. 4. [Evidence](../../sources/notes/roscoe2007reviews.md#e13)
[^roscoe2007reviews-e14]: Roscoe 2007, §6, p. 5. [Evidence](../../sources/notes/roscoe2007reviews.md#e14)
[^roscoe2007reviews-e15]: Roscoe 2007, §5, p. 5. [Evidence](../../sources/notes/roscoe2007reviews.md#e15)
[^bourne2005published-e4]: Bourne 2005, Rule 8. [Evidence](../../sources/notes/bourne2005published.md#e4)
[^bourne2006reviewers-e1]: Bourne & Korngreen 2006, Rule 1. [Evidence](../../sources/notes/bourne2006reviewers.md#e1)
[^bourne2006reviewers-e2]: Bourne & Korngreen 2006, Rule 2. [Evidence](../../sources/notes/bourne2006reviewers.md#e2)
[^bourne2006reviewers-e3]: Bourne & Korngreen 2006, Rule 3. [Evidence](../../sources/notes/bourne2006reviewers.md#e3)
[^bourne2006reviewers-e4]: Bourne & Korngreen 2006, Rule 4. [Evidence](../../sources/notes/bourne2006reviewers.md#e4)
[^bourne2006reviewers-e5]: Bourne & Korngreen 2006, Rule 9. [Evidence](../../sources/notes/bourne2006reviewers.md#e5)
[^bourne2006reviewers-e6]: Bourne & Korngreen 2006, Rule 9. [Evidence](../../sources/notes/bourne2006reviewers.md#e6)
[^bourne2006reviewers-e9]: Bourne & Korngreen 2006, Rule 10. [Evidence](../../sources/notes/bourne2006reviewers.md#e9)
[^bourne2006reviewers-e10]: Bourne & Korngreen 2006, Rule 6. [Evidence](../../sources/notes/bourne2006reviewers.md#e10)
[^bourne2006reviewers-e11]: Bourne & Korngreen 2006, Rule 8. [Evidence](../../sources/notes/bourne2006reviewers.md#e11)
[^bourne2006reviewers-e12]: Bourne & Korngreen 2006, Rule 10. [Evidence](../../sources/notes/bourne2006reviewers.md#e12)
[^mightreview-e1]: Might, opening. [Evidence](../../sources/notes/mightreview.md#e1)
[^mightreview-e2]: Might, Recognize conflicts. [Evidence](../../sources/notes/mightreview.md#e2)
[^mightreview-e3]: Might, Don't review like a grad student. [Evidence](../../sources/notes/mightreview.md#e3)
[^mightreview-e4]: Might, Acknowledge visceral reactions. [Evidence](../../sources/notes/mightreview.md#e4)
[^mightreview-e5]: Might, Offer constructive criticism. [Evidence](../../sources/notes/mightreview.md#e5)
[^mightreview-e6]: Might, Offer constructive criticism. [Evidence](../../sources/notes/mightreview.md#e6)
[^mightreview-e7]: Might, Hold the snark. [Evidence](../../sources/notes/mightreview.md#e7)
[^mightreview-e8]: Might, Keep it impersonal. [Evidence](../../sources/notes/mightreview.md#e8)
[^mightreview-e9]: Might, Anonymize but don't hide. [Evidence](../../sources/notes/mightreview.md#e9)
[^mightreview-e10]: Might, Scholarly conflict. [Evidence](../../sources/notes/mightreview.md#e10)
[^black2022novelty-e1]: Black 2022, opening. [Evidence](../../sources/notes/black2022novelty.md#e1)
[^black2022novelty-e2]: Black 2022, Novelty as complexity. [Evidence](../../sources/notes/black2022novelty.md#e2)
[^black2022novelty-e3]: Black 2022, Novelty as surprise. [Evidence](../../sources/notes/black2022novelty.md#e3)
[^black2022novelty-e4]: Black 2022, Novelty as technical novelty. [Evidence](../../sources/notes/black2022novelty.md#e4)
[^ralph2020empirical-e24]: ACM SIGSOFT Empirical Standards, General Standard, General Quality Criteria. [Evidence](../../sources/notes/ralph2020empirical.md#e24)
[^ralph2020empirical-e53]: ACM SIGSOFT Empirical Standards, Good Review Practices. [Evidence](../../sources/notes/ralph2020empirical.md#e53)
[^ralph2020empirical-e54]: ACM SIGSOFT Empirical Standards, Good Review Practices. [Evidence](../../sources/notes/ralph2020empirical.md#e54)
[^ralph2020empirical-e55]: ACM SIGSOFT Empirical Standards, Good Review Practices. [Evidence](../../sources/notes/ralph2020empirical.md#e55)
[^ralph2020empirical-e56]: ACM SIGSOFT Empirical Standards, Reviewing Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e56)
[^ralph2020empirical-e57]: ACM SIGSOFT Empirical Standards, Reviewing Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e57)
[^ralph2020empirical-e58]: ACM SIGSOFT Empirical Standards, Reviewing Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e58)
[^ralph2020empirical-e59]: ACM SIGSOFT Empirical Standards, Reviewing Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e59)
[^ralph2020empirical-e60]: ACM SIGSOFT Empirical Standards, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e60)
[^ralph2020empirical-e61]: ACM SIGSOFT Empirical Standards, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e61)
[^ralph2020empirical-e249]: ACM SIGSOFT Empirical Standards, Questionnaire Surveys standard, Invalid Criticism. [Evidence](../../sources/notes/ralph2020empirical.md#e249)
[^falessi2018empirical-e6]: Falessi et al. 2018, §6.2. [Evidence](../../sources/notes/falessi2018empirical.md#e6)
[^apaphil2022journal-e8]: American Philosophical Association 2022, Statement on Best Practices in Journal Publishing. [Evidence](../../sources/notes/apaphil2022journal.md#e8)
[^apaphil2022journal-e9]: American Philosophical Association 2022, Statement on Best Practices in Journal Publishing. [Evidence](../../sources/notes/apaphil2022journal.md#e9)
[^apaphil2022journal-e10]: American Philosophical Association 2022, Statement on Best Practices in Journal Publishing. [Evidence](../../sources/notes/apaphil2022journal.md#e10)
[^apaphil2022journal-e11]: American Philosophical Association 2022, Statement on Best Practices in Journal Publishing. [Evidence](../../sources/notes/apaphil2022journal.md#e11)
[^apaphil2022journal-e15]: American Philosophical Association 2022, Statement on Best Practices in Journal Publishing. [Evidence](../../sources/notes/apaphil2022journal.md#e15)
[^ams2022ethical-e7]: American Mathematical Society Ethical Guidelines. [Evidence](../../sources/notes/ams2022ethical.md#e7)
[^ams2022ethical-e10]: American Mathematical Society Ethical Guidelines. [Evidence](../../sources/notes/ams2022ethical.md#e10)
[^neurips2025llm-e1]: NeurIPS 2025 Policy on the Use of Large Language Models, LLM Policy for Reviewers. [Evidence](../../sources/notes/neurips2025llm.md#e1)
[^neurips2025llm-e2]: NeurIPS 2025 Policy on the Use of Large Language Models, Reviewers FAQ 2. [Evidence](../../sources/notes/neurips2025llm.md#e2)
[^neurips2025llm-e3]: NeurIPS 2025 Policy on the Use of Large Language Models, Reviewers FAQ 4. [Evidence](../../sources/notes/neurips2025llm.md#e3)
[^neurips2025llm-e4]: NeurIPS 2025 Policy on the Use of Large Language Models, Reviewers FAQ 4. [Evidence](../../sources/notes/neurips2025llm.md#e4)
