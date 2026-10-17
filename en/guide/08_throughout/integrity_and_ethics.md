# Research integrity and ethics

> The ideas on this page apply to every field; the examples and concrete practices come from computer science. Each set of rules cited below has its own origin and scope (a European code, one field's standard, one conference's rules for one year), and we say which each time. For your own research, the rules of your institution, your field and the venue you submit to take precedence.

## When you need this page

- You want to know what you must never do, and what is "not against the rules" yet makes your results untrustworthy;
- Your research involves people, collects data about people, or could harm others, for example finding vulnerabilities in smart contracts that are actually deployed;
- You want to use a large language model to help write a paper or run experiments, or you have found an error in a paper you already published.

---

## 1. Know the red lines: fabrication, falsification, plagiarism

**How:** The European Code of Conduct for Research Integrity (written by ALLEA, All European Academies; "the European code" below) keeps the three traditional categories of research misconduct[^allea2023european-e3]. Treat them as lines you never cross, under any circumstances:

| Type | What it means | What it looks like in computer science |
|---|---|---|
| Fabrication | Making up data or results and recording them as if real | Filling in numbers for experiments you never ran |
| Falsification | Manipulating materials, equipment, images or procedures; or changing, omitting or suppressing data or results without justification | Dropping the runs that make your method look bad |
| Plagiarism | Using other people's work or ideas without proper credit | Putting someone else's code or paragraphs straight into your paper |

The "What it looks like in computer science" column gives our own examples.

The European code also lists other practices that are just as unacceptable, for example: misusing statistics to make results look "significant"; withholding data or results without justification; citing selectively or inaccurately[^allea2023european-e4]; splitting one study into several papers to publish more ("salami slicing"); republishing substantial parts of your own earlier papers (including in translation) without acknowledging it[^allea2023european-e5]; manipulating authorship or belittling other people's contributions[^allea2023european-e9]; and hiding the use of artificial intelligence or automated tools when drafting a paper[^allea2023european-e19]. The software engineering empirical standards also list salami slicing as an antipattern[^ralph2020empirical-e67].

**Why:** In the European code's words, these practices damage the research process and relationships between researchers, undermine trust in research, waste resources, and can cause unnecessary harm to participants, society or the environment[^allea2023european-e6]. Although the code is European, it states that it applies to all fields of research[^allea2023european-e18], which is why we use it as the reference for the red lines.

**Where people go wrong:** Thinking only "making up data" counts as misconduct. "Quietly dropping unfavorable results" sounds like data cleaning, but it may already be falsification[^allea2023european-e3].

**Write it down:** Using the table above, think about which step in your current project is most tempting to "tidy up a little" (picking runs, deleting outlier samples). Write down how you will record that step so that others can see what you did.

## 2. Be honest with the evidence: don't fool yourself, report all results

**How:**

- Report the facts that disagree with your conclusion along with the ones that agree[^feynman1974cargo-e4].
- When you decide to test an idea, decide to report the result whichever way it comes out. If you only publish one kind of result, your argument looks better than it is[^feynman1974cargo-e9].
- Check symmetrically: if you hunt for bugs when results look "bad", hunt just as hard when they look "good". The history of physics has a lesson here: when later researchers got values that differed from an authoritative result, they searched hard for what was wrong; when they got values close to it, they didn't look so hard[^feynman1974cargo-e14].
- If your method involves randomness, report the results of all runs; don't rerun again and again and report only the best one[^zeller2021devil-e1]. When comparing with other people's methods, give them the same chance to tune parameters[^zeller2021devil-e2]. (These two are examples from computer science experiments.)
- Speculation is fine, but keep it separate from conclusions backed by evidence, and label it as such[^lipton2019troubling-e1][^lipton2019troubling-e3].

**Why:** The first principle of scientific integrity is that you must not fool yourself, and you are the easiest person to fool[^feynman1974cargo-e7]. The European code also says negative results may be just as worth publishing and sharing as positive ones[^allea2023european-e12]; the software engineering empirical standards list "rejecting a paper because its results are negative" as an invalid criticism[^ralph2020empirical-e41].

**Where people go wrong:**

- Reporting only the statistical tests that came out "significant" (p-hacking); or, in a study presented as testing hypotheses stated before data collection, writing hypotheses after seeing the results as if they had been there all along (HARKing, hypothesizing after the results are known). The software engineering empirical standards list both as antipatterns[^ralph2020empirical-e27].
- Writing a limitations section and then drawing conclusions as if the limitations didn't exist[^ralph2020empirical-e66].
- Treating "not against the rules" as "fine". Not preregistering (publicly registering your study plan in advance), not keeping an experiment log, not keeping version history, not testing your code, not validating results, and not sharing anything: none of these is research misconduct[^zeller2021devil-e8]. In our view, though, they leave no way for anyone to trust your results.

Anyone can make these mistakes; the authors who criticize this practice admit that they have themselves written "speculation disguised as explanation"[^lipton2019troubling-e12].

For how to do the analysis, separate exploratory from confirmatory conclusions, and write limitations, see [Analysis and interpretation](../02_do-the-project/07_analyze-and-interpret.md).

**Write it down:** List every experiment run you have so far, including failed and unflattering ones. Next to the list, write one sentence: if a reviewer saw this complete list, would your conclusion still hold?

## 3. Make your work checkable by others

**How:**

- Where applicable, describe your methods in enough detail for others to check or repeat them[^allea2023european-e14].
- Keep research materials such as data, code and protocols safely for a reasonable, stated period[^allea2023european-e15].
- When you publish, release your data and code: deposit them in a trusted repository that assigns a DOI (digital object identifier, a permanent ID that keeps working even if web addresses change), and state the license[^wilson2017good-e4][^sandve2013ten-e6].
- If something can't be released, explain why. The European code's principle is "as open as possible, as closed as necessary"[^allea2023european-e15]; the software engineering open science standard says that ethical, legal and similar obstacles can justify not releasing materials[^ralph2020empirical-e76], as long as you explain why[^ralph2020empirical-e77].

**Why:** Reproducibility is not just a duty to the research community; failing at it also hurts you[^sandve2013ten-e1]: if you can't get back to the version of the code that produced a result, you can't tell whether that result came from a bug[^sandve2013ten-e4]. Making your work genuinely reproducible by peers is itself a strong signal of quality and trustworthiness[^sandve2013ten-e6].

**Where people go wrong:** Thinking that putting things on GitHub or a cloud drive counts as releasing them. The software engineering open science standard points out that personal websites, GitHub and cloud drives are not adequate long-term archives[^ralph2020empirical-e78]. Consider Zenodo (a free archive for research outputs), OSF (the Open Science Framework) or your institution's repository.

For how to record where each result came from day to day, and how to store and back up raw data (including non-computational materials such as lab notebooks, questionnaires and interview recordings), see [Organizing your research materials](organizing_materials.md).

**Write it down:** List the data, code and other materials your paper will use. For each, write where you plan to release it and under which license; for anything that can't be released, write one sentence on why.

## 4. When research involves people or could harm others, protect people first

The Menlo Report points out that advances in information and communication technology have widened the gap between what researchers can do and what they should do[^bailey2012menlo-e1]. So it is not only medicine and psychology: any research that involves people, collects data about people, or could affect others needs to think about ethics first.

**How:**

1. **Start thinking early**, at the design stage; don't wait until the paper is written and then tack on an ethics paragraph. The ethics guidelines of the security conference USENIX Security '26 recommend considering ethics "early in the research process"[^usenixsec2026cfp-e9].
2. **Check your field's and institution's rules on whether you need ethics review.** Taking psychology as an example, the American Psychological Association's ethics code requires that when institutional approval is needed, you submit an accurate protocol and obtain approval before starting, and then conduct the research as approved[^apa2017ethical-e2]. The software engineering ethics supplement lists "the paper names the ethics review board that approved the study and gives the approval number" as a desirable attribute[^ralph2020empirical-e73]. Rules differ widely between countries, fields and institutions; for specific requirements see the field overviews, for example [Computer science](../07_fields/computer-science/README.md#ethics-issues-specific-to-this-field), [Psychology](../07_fields/psychology/README.md#ethics-the-apa-ethics-code-and-institutional-approval), [Clinical medicine](../07_fields/clinical-medicine/README.md#your-subjects-are-people-so-ethics-comes-first), [Education](../07_fields/education/README.md#ethics-minors-gatekeepers-and-studying-your-own-students), [Sociology](../07_fields/sociology/README.md#ethics-the-asa-code-and-the-bsa-statement) and [Media and communication](../07_fields/media-communication/README.md#ethics-of-online-and-social-media-research).
3. **Go through a framework item by item.** In computer security you can use the Menlo Report, a US report on ethical principles for information and communication technology research; USENIX Security '26 strongly encourages authors to be familiar with it[^usenixsec2026cfp-e10]. It keeps the three principles of the Belmont Report (ethical principles and guidelines for the protection of human research subjects[^bailey2012menlo-e7]) and adds a fourth[^bailey2012menlo-e2]:

| Principle | What it requires |
|---|---|
| Respect for persons | Participation is voluntary and based on informed consent; people who are not research subjects but are affected by the research must be protected too[^bailey2012menlo-e3] |
| Beneficence | Avoid harm; maximize benefits and minimize harms; assess risks and benefits systematically[^bailey2012menlo-e4] |
| Justice | Select research subjects fairly and distribute burdens fairly among those affected[^bailey2012menlo-e5] |
| Respect for law and public interest | Do legal due diligence; be transparent about methods and results; be accountable for your actions[^bailey2012menlo-e6] |

4. **Say it clearly in the paper.** The software engineering ethics supplement requires studies with human participants to state: what risks participants may face, what was done to mitigate them, and why the study's benefits justify those risks[^ralph2020empirical-e68]; how participants were recruited, what compensation they received, how coercion was avoided, and how free informed consent was obtained[^ralph2020empirical-e69]; and how privacy was protected, including the possibility that someone could combine several data sources to re-identify participants[^ralph2020empirical-e70]. The European code also requires telling participants in advance how their data will be used, stored and deleted[^allea2023european-e17].

Examples from "large language models and smart contract security":

- You ask developers to try your tool, or you interview them: this is research with human participants. Find out first whether you need ethics review, and obtain informed consent.
- You find a vulnerability in a deployed contract: notify the responsible party privately first, then go public. The USENIX Security '26 ethics guidelines point out that publishing before private disclosure and mitigation can cause harm[^usenixsec2026cfp-e5]; they require the paper to say to whom the vulnerability was disclosed and what came of it[^usenixsec2026cfp-e6].

**Why:** Risks fall not only on participants but also on the applications of the research, on society and on the environment, and they too must be identified, weighed and mitigated[^allea2023european-e16][^ralph2020empirical-e65]. The USENIX Security '26 ethics guidelines go as far as saying that sometimes the most ethical choice is not to do the research, or not to publish it once done[^usenixsec2026cfp-e8].

**Where people go wrong:**

- Justifying risks by saying "research in general is beneficial", rather than arguing for the specific benefits of this study; downplaying risks when recruiting. The software engineering ethics supplement lists these as antipatterns[^ralph2020empirical-e71].
- Thinking that once the ethics review has approved the study, you are done. The USENIX Security '26 ethics guidelines warn that review boards may not know the norms of computer security research, so even with approval you still need to do your own ethical analysis[^usenixsec2026cfp-e7].
- Skipping informed consent when the study requires deception (such as not telling participants the real purpose). The software engineering ethics supplement allows informed consent to be adapted in that case, but the deception itself must be fully described in the paper[^ralph2020empirical-e72].

> **Where sources disagree: what if the law and ethics conflict?**
>
> - **Obey the law as a principle**: the US Menlo Report asks researchers to do legal due diligence[^bailey2012menlo-e6]; the European code requires compliance with relevant codes, guidelines and regulations[^allea2023european-e16].
> - **Weigh ethics and legality together**: the software engineering ethics supplement holds that in rare cases, ethical research may require illegal actions; frameworks like Menlo include respect for law precisely so that ethics and legality are weighed together[^ralph2020empirical-e75].
>
> In practice: as a newcomer, default to obeying the law and complete your institution's ethics review. In gray areas, talk to your advisor and the ethics committee first; don't decide on your own.

**Write it down:** List everyone your research will touch, including people who are not research subjects but may be affected (such as the people who deployed the contracts and their users). For each group, write one sentence: what harm they might suffer, and how you plan to reduce it.

## 5. Authorship, citation and conflicts of interest: give every contributor due credit

**How:**

- **Authorship**: for who should be an author, who goes in the acknowledgments, how to order authors and when to discuss it, see [Collaboration and advisors](collaboration_and_advisors.md#6-authorship-discuss-it-at-the-start-and-adjust-as-you-go). Here, remember just one red line: the European code lists manipulating authorship and belittling other people's contributions as unacceptable[^allea2023european-e9].
- **Credit every idea, dataset, piece of code or text you take from others**; otherwise it is plagiarism[^allea2023european-e3]. Cite accurately, and don't cite only the work that supports you[^allea2023european-e4].
- **Disclose conflicts of interest and funding sources**, financial and non-financial[^allea2023european-e10].

**Where people go wrong:** Commenting out the acknowledgments and author information for anonymous submission, then forgetting to restore them for the public version. Before release, check that all authors are listed, names and affiliations are correct, and the acknowledgments are back[^carlini2022checklist-e2]. Every time you make a mistake like this, add it to your own release checklist[^carlini2022checklist-e1].

**Write it down:** List the code, data, ideas and figures from others that your paper uses, and check each one is credited. Then list the project's funding sources and any conflicts of interest you might have.

## 6. When you use large language models and other tools, you are still responsible

Rules on large language models differ between venues and keep changing. Two sets of rules serve as examples below: the large language model policy of NeurIPS 2025 (the Conference on Neural Information Processing Systems, a top machine learning conference), and the recommendations of the International Committee of Medical Journal Editors (ICMJE) for medical journals.

**How:**

- **A large language model cannot be an author.** NeurIPS 2025 says only humans can be authors, and whatever tools they use, authors are responsible for the entire content of the paper, including text, figures and methods[^neurips2025llm-e6]. The medical journal recommendations give the reason: tools cannot take responsibility for the accuracy, integrity and originality of the work, which authorship requires[^icmje2026recommendations-e29].
- **Check everything it generates, item by item.** Output from large language models sounds authoritative but can be wrong, incomplete or biased[^icmje2026recommendations-e31]. References in particular: using references generated by a large language model without checking that they exist, are correct and are relevant is given by NeurIPS 2025 as an example of a violation, and for a violation NeurIPS reserves the right to revoke the paper's publication status[^neurips2025llm-e7].
- **When a large language model is part of your method, describe it in the method.** NeurIPS 2025 requires that when a large language model is an important, original or non-standard part of the method, it be described in the experimental setup[^neurips2025llm-e5]; the medical journal recommendations require enough detail for others to repeat it, including the tool, the version and, where applicable, the prompts[^icmje2026recommendations-e32]. In research like "large language models and smart contract security", where the large language model is itself the object of study, this matters all the more.
- **Don't feed other people's data to tools.** Some tools keep input data for training; NeurIPS 2025 reminds authors to mind personal privacy[^neurips2025llm-e9]. When you review papers later, manuscripts must not be given to large language models either; see [Being a reviewer](being_a_reviewer.md).

> **Where sources disagree: if you only use a large language model to polish your writing, do you need to declare it?**
>
> - **No need**: NeurIPS 2025's policy is that use only for writing, editing or formatting, which does not affect the methods, rigor or originality, need not be declared in the paper[^neurips2025llm-e8].
> - **Declare it**: the medical journal recommendations require that use of artificial intelligence for writing assistance be described in the acknowledgments[^icmje2026recommendations-e30]; failure to disclose may require a correction and in some cases may be judged misconduct[^icmje2026recommendations-e33]. The European code lists hiding the use of artificial intelligence when drafting a paper as unacceptable[^allea2023european-e19].
>
> In practice: before submitting, read the target conference's or journal's own policy and follow it; if unsure, state what you used and what for.

**Write it down:** List every stage of this project where you use a large language model (finding literature, writing code, running experiments, editing text). For each, write down how you checked its output, and whether the target conference or journal requires you to declare it.

## 7. When you find an error, correct it yourself

**How:** If you find an error in a paper you have published, issue a correction promptly, and retract the paper if necessary[^allea2023european-e11]. When presenting your research to others, be clear about how reliable the evidence is and what remains uncertain[^allea2023european-e13].

**Why:** The European code defines misconduct as fabrication, falsification and plagiarism[^allea2023european-e3]; under that definition, an honest error is not misconduct in itself, and correcting it yourself is nothing to be ashamed of. The code also says authors who proactively publish corrections after publication should be given credit for it[^allea2023european-e20].

**Where people go wrong:** Not wanting to lose face and planning to "fix it in passing in the next paper". In the meantime, others may already be building on your wrong result.

**Write it down:** Suppose you discover tomorrow that a key number in your paper was miscalculated. Write down whom you would tell first (advisor, co-authors, editor or conference chair), and how you would decide between a correction and a retraction.

---

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Thinking only making up data counts as misconduct | Deleting or hiding results without justification is falsification[^allea2023european-e3] |
| Running many times and reporting only the best run | A cherry-picked result doesn't represent how the method really performs[^zeller2021devil-e1] |
| Hunting for errors when results are bad, not checking when they are good | Asymmetric checking lets wrong conclusions survive[^feynman1974cargo-e14] |
| Writing limitations but still overstating the conclusion | The limitations become empty words[^ralph2020empirical-e66] |
| Keeping data and code only on GitHub or a cloud drive | Not an adequate long-term archive[^ralph2020empirical-e78] |
| Justifying risks to participants with "research is beneficial overall" | You need to argue for the specific benefits of this study[^ralph2020empirical-e71] |
| Not thinking about ethics anymore once the ethics review has approved the study | Approval doesn't mean there are no ethical issues[^usenixsec2026cfp-e7] |
| Putting a newly found vulnerability straight into a public paper | Disclosure before a fix can cause harm[^usenixsec2026cfp-e5] |
| Listing people with no significant contribution as authors, or leaving out people who contributed | Manipulating authorship is unacceptable[^allea2023european-e9] |
| Splitting one study into several papers | Salami slicing, which is unacceptable[^allea2023european-e5] |
| Using references from a large language model as they are | They may not even exist; at NeurIPS 2025 this is a violation[^neurips2025llm-e7] |
| Listing a large language model as an author | A tool can't take responsibility for the work and can't be an author[^icmje2026recommendations-e29] |

The "Why it's a problem" column is our own summary; the footnotes point to the relevant rules or examples, whose origin and scope are given in the main text.

## Further reading

- **Feynman, "Cargo Cult Science"**: a short talk that makes "don't fool yourself" and "publish whatever the result" clear; a good first read.
- **ALLEA (All European Academies), The European Code of Conduct for Research Integrity, 2023 revised edition**: states that it applies to all fields; the place to look when you need to know what counts as misconduct.
- **Sandve et al. 2013; Wilson et al. 2017**: concrete practices for reproducibility and data management; both short enough to follow directly.
- **Bailey et al. 2012 (an introduction to the Menlo Report) and the ethics supplement of the software engineering empirical standards**: for designing research with human participants and writing the ethics section.
- **Zeller, "The Devil's Guide to Incremental Research"**: a satirical list of common questionable practices, useful for checking yourself against.
- **The large language model policy of your target conference or journal**, for example the NeurIPS 2025 policy: read it before submitting, as every venue's requirements differ.

[^allea2023european-e3]: ALLEA 2023, §3.1. [Evidence](../../sources/notes/allea2023european.md#e3)
[^allea2023european-e4]: ALLEA 2023, §3.1. [Evidence](../../sources/notes/allea2023european.md#e4)
[^allea2023european-e5]: ALLEA 2023, §3.1. [Evidence](../../sources/notes/allea2023european.md#e5)
[^allea2023european-e6]: ALLEA 2023, §3. [Evidence](../../sources/notes/allea2023european.md#e6)
[^allea2023european-e9]: ALLEA 2023, §3.1. [Evidence](../../sources/notes/allea2023european.md#e9)
[^allea2023european-e10]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e10)
[^allea2023european-e11]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e11)
[^allea2023european-e12]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e12)
[^allea2023european-e13]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e13)
[^allea2023european-e14]: ALLEA 2023, §2.3. [Evidence](../../sources/notes/allea2023european.md#e14)
[^allea2023european-e15]: ALLEA 2023, §2.5. [Evidence](../../sources/notes/allea2023european.md#e15)
[^allea2023european-e16]: ALLEA 2023, §2.4. [Evidence](../../sources/notes/allea2023european.md#e16)
[^allea2023european-e17]: ALLEA 2023, §2.5. [Evidence](../../sources/notes/allea2023european.md#e17)
[^allea2023european-e18]: ALLEA 2023, Preamble. [Evidence](../../sources/notes/allea2023european.md#e18)
[^allea2023european-e19]: ALLEA 2023, §3.1. [Evidence](../../sources/notes/allea2023european.md#e19)
[^allea2023european-e20]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e20)
[^feynman1974cargo-e4]: Feynman 1974, "Details that could throw doubt" paragraph. [Evidence](../../sources/notes/feynman1974cargo.md#e4)
[^feynman1974cargo-e7]: Feynman 1974, "The first principle" paragraph. [Evidence](../../sources/notes/feynman1974cargo.md#e7)
[^feynman1974cargo-e9]: Feynman 1974, "One example of the principle" paragraph. [Evidence](../../sources/notes/feynman1974cargo.md#e9)
[^feynman1974cargo-e14]: Feynman 1974, Millikan oil-drop example. [Evidence](../../sources/notes/feynman1974cargo.md#e14)
[^lipton2019troubling-e1]: Lipton & Steinhardt 2019, §1. [Evidence](../../sources/notes/lipton2019troubling.md#e1)
[^lipton2019troubling-e3]: Lipton & Steinhardt 2019, §3.1. [Evidence](../../sources/notes/lipton2019troubling.md#e3)
[^lipton2019troubling-e12]: Lipton & Steinhardt 2019, §3.1. [Evidence](../../sources/notes/lipton2019troubling.md#e12)
[^zeller2021devil-e1]: Zeller 2021, THE CHERRY SHUFFLE. [Evidence](../../sources/notes/zeller2021devil.md#e1)
[^zeller2021devil-e2]: Zeller 2021, THE AUTOTUNE. [Evidence](../../sources/notes/zeller2021devil.md#e2)
[^zeller2021devil-e8]: Zeller 2021, third-to-last paragraph. [Evidence](../../sources/notes/zeller2021devil.md#e8)
[^ralph2020empirical-e27]: SIGSOFT General Standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e27)
[^ralph2020empirical-e41]: SIGSOFT General Standard, Invalid Criticisms. [Evidence](../../sources/notes/ralph2020empirical.md#e41)
[^ralph2020empirical-e65]: SIGSOFT General Standard, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e65)
[^ralph2020empirical-e66]: SIGSOFT General Standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e66)
[^ralph2020empirical-e67]: SIGSOFT General Standard, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e67)
[^ralph2020empirical-e68]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e68)
[^ralph2020empirical-e69]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Essential Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e69)
[^ralph2020empirical-e70]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Essential Attributes, footnote 2. [Evidence](../../sources/notes/ralph2020empirical.md#e70)
[^ralph2020empirical-e71]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e71)
[^ralph2020empirical-e72]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Acceptable Deviations. [Evidence](../../sources/notes/ralph2020empirical.md#e72)
[^ralph2020empirical-e73]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e73)
[^ralph2020empirical-e75]: SIGSOFT Ethics (Studies with Human Participants) Supplement, Note. [Evidence](../../sources/notes/ralph2020empirical.md#e75)
[^ralph2020empirical-e76]: SIGSOFT Open Science Supplement, Principle. [Evidence](../../sources/notes/ralph2020empirical.md#e76)
[^ralph2020empirical-e77]: SIGSOFT Open Science Supplement, Desirable Attributes. [Evidence](../../sources/notes/ralph2020empirical.md#e77)
[^ralph2020empirical-e78]: SIGSOFT Open Science Supplement, Notes. [Evidence](../../sources/notes/ralph2020empirical.md#e78)
[^sandve2013ten-e1]: Sandve et al. 2013, Introduction. [Evidence](../../sources/notes/sandve2013ten.md#e1)
[^sandve2013ten-e4]: Sandve et al. 2013, Rule 4. [Evidence](../../sources/notes/sandve2013ten.md#e4)
[^sandve2013ten-e6]: Sandve et al. 2013, Rule 10. [Evidence](../../sources/notes/sandve2013ten.md#e6)
[^wilson2017good-e4]: Wilson et al. 2017, Box 1. [Evidence](../../sources/notes/wilson2017good.md#e4)
[^bailey2012menlo-e1]: Bailey et al. 2012, p. 71. [Evidence](../../sources/notes/bailey2012menlo.md#e1)
[^bailey2012menlo-e2]: Bailey et al. 2012, p. 72. [Evidence](../../sources/notes/bailey2012menlo.md#e2)
[^bailey2012menlo-e3]: Bailey et al. 2012, pp. 72–73. [Evidence](../../sources/notes/bailey2012menlo.md#e3)
[^bailey2012menlo-e4]: Bailey et al. 2012, p. 72. [Evidence](../../sources/notes/bailey2012menlo.md#e4)
[^bailey2012menlo-e5]: Bailey et al. 2012, p. 73. [Evidence](../../sources/notes/bailey2012menlo.md#e5)
[^bailey2012menlo-e6]: Bailey et al. 2012, p. 73. [Evidence](../../sources/notes/bailey2012menlo.md#e6)
[^bailey2012menlo-e7]: Bailey et al. 2012, p. 74, reference 3. [Evidence](../../sources/notes/bailey2012menlo.md#e7)
[^apa2017ethical-e2]: American Psychological Association Ethics Code, 8.01. [Evidence](../../sources/notes/apa2017ethical.md#e2)
[^usenixsec2026cfp-e5]: USENIX Security '26 ethics guidelines, Disclosures. [Evidence](../../sources/notes/usenixsec2026cfp.md#e5)
[^usenixsec2026cfp-e6]: USENIX Security '26 ethics guidelines, Disclosures. [Evidence](../../sources/notes/usenixsec2026cfp.md#e6)
[^usenixsec2026cfp-e7]: USENIX Security '26 ethics guidelines, the IRB question. [Evidence](../../sources/notes/usenixsec2026cfp.md#e7)
[^usenixsec2026cfp-e8]: USENIX Security '26 ethics guidelines. [Evidence](../../sources/notes/usenixsec2026cfp.md#e8)
[^usenixsec2026cfp-e9]: USENIX Security '26 ethics guidelines, when to start thinking about ethics. [Evidence](../../sources/notes/usenixsec2026cfp.md#e9)
[^usenixsec2026cfp-e10]: USENIX Security '26 ethics guidelines. [Evidence](../../sources/notes/usenixsec2026cfp.md#e10)
[^carlini2022checklist-e1]: Carlini 2022, opening. [Evidence](../../sources/notes/carlini2022checklist.md#e1)
[^carlini2022checklist-e2]: Carlini 2022, Secondary checklist for public releases. [Evidence](../../sources/notes/carlini2022checklist.md#e2)
[^neurips2025llm-e5]: NeurIPS 2025 Policy on the Use of Large Language Models, section for authors. [Evidence](../../sources/notes/neurips2025llm.md#e5)
[^neurips2025llm-e6]: NeurIPS 2025 Policy on the Use of Large Language Models, section for authors, FAQ 2. [Evidence](../../sources/notes/neurips2025llm.md#e6)
[^neurips2025llm-e7]: NeurIPS 2025 Policy on the Use of Large Language Models, section for authors. [Evidence](../../sources/notes/neurips2025llm.md#e7)
[^neurips2025llm-e8]: NeurIPS 2025 Policy on the Use of Large Language Models, section for authors, FAQ 3. [Evidence](../../sources/notes/neurips2025llm.md#e8)
[^neurips2025llm-e9]: NeurIPS 2025 Policy on the Use of Large Language Models, section for authors. [Evidence](../../sources/notes/neurips2025llm.md#e9)
[^icmje2026recommendations-e29]: ICMJE 2026, II.A.4. [Evidence](../../sources/notes/icmje2026recommendations.md#e29)
[^icmje2026recommendations-e30]: ICMJE 2026, II.A.4. [Evidence](../../sources/notes/icmje2026recommendations.md#e30)
[^icmje2026recommendations-e31]: ICMJE 2026, II.A.4. [Evidence](../../sources/notes/icmje2026recommendations.md#e31)
[^icmje2026recommendations-e32]: ICMJE 2026, IV.A.3.d. [Evidence](../../sources/notes/icmje2026recommendations.md#e32)
[^icmje2026recommendations-e33]: ICMJE 2026, V.A. [Evidence](../../sources/notes/icmje2026recommendations.md#e33)
