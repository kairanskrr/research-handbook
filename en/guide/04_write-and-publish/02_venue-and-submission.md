# Choosing a venue and submitting

> The reasoning in this chapter applies to every field; the examples and concrete steps come from computer science.

## Where you are

You have a first draft: the claim, the evidence, and the related work are on paper, and your advisor has read it once or twice. For how to write the paper well, see [Telling the story and writing the paper](01_story-and-paper.md).

Now a string of very practical questions comes up. Where should you send it? A conference or a journal? Should you post it on a preprint server first? How do you fill in all the forms and declarations in the submission system? And what happens after you click "Submit"?

## What this stage is for

Get a finished paper **to the right place, and submitted by the rules**. Concretely, answer these five questions:

1. Which journal or conference has the readers and the standards that best fit this paper?
2. In your field, should you aim for a conference or a journal?
3. Should you post a preprint first? Would that break any submission rules?
4. What does your target venue require: formatting, anonymization, code and data, an ethics statement, authorship and contribution statements?
5. What happens after you submit, and what should you do while you wait?

While planning, you may already have picked a rough target venue and deadline; see [Writing a research plan](../01_from-interest-to-project/04_research-plan.md#1-fix-the-finish-line-where-to-submit-and-when). This chapter turns that decision into action now that the paper exists, and revises it if needed.

Below we cite many rules from conferences, journals, and societies as examples. Each rule is that one venue's version for that one year, not a general law. When you submit, go by your target venue's current pages.

---

## 1. Choosing a venue: start with readers and standards

**Ask "who should read this paper?" before "which venue is most famous?"** Choosing a venue is really choosing your target readers (for why readers come first, see [Writing a research plan](../01_from-interest-to-project/04_research-plan.md#1-fix-the-finish-line-where-to-submit-and-when)). The venue also determines the paper's format, the level of detail, and how novel the work has to be[^bourne2005published-e5]. When reviewers judge whether a paper is good enough, they measure it against what that journal or conference, and that community, values[^hicks2014reviewing-e9].

**The easiest starting point: see where the closest related work was published.** When you converged on your project you drew a comparison table (see [Converging on a project](../01_from-interest-to-project/03_converge.md#3-has-someone-already-done-it)). Your paper most likely belongs in front of the same readers as the papers in that table, at the same conferences and journals `[Our analysis]`.

**Then read the rules on the venue's website.** The American Philosophical Association's 2022 advice to authors is to look at the journal's website before submitting[^apaphil2022journal-e3]. There you can find the acceptance rate, the average review time, the average time from acceptance to publication, and similar information[^apaphil2022journal-e4]; use it to judge whether the journal is the right choice, and prepare the manuscript as it asks[^apaphil2022journal-e5]. If you are unsure, many journals offer pre-submission inquiries; use them[^bourne2005published-e10].

**Pay attention to the journal's stated scope and standards.** Take the 2026 author guidelines of *Environmental Science & Technology* (ES&T below), the American Chemical Society's environmental science journal. They say lack of novelty is a common reason for rejection[^estauthorguidelines-e1], and that manuscripts reporting only routine data, or addressing problems that are already well understood, will not be considered[^estauthorguidelines-e2]. Manuscripts that fall short of these standards may not even be sent out for review (see the cover letter in Section 5).

Use these questions to compare your candidate venues one by one `[Our analysis]`:

| Question | How to find out | Example: "large language models and smart contract security" |
|---|---|---|
| Who reads it? | Look at the papers it published in the last two or three years | Security conference readers care about attacks and defenses; software engineering conference readers care about development tools and processes |
| Has it published work close to yours? | Search its paper list for your keywords | Has it published papers on vulnerability detection or benchmark quality? |
| What kind of evidence does it value? | Read a few papers it accepted and see how they evaluate | Does it expect evaluation on real-world contracts and comparison with existing tools? |
| Length and format? | Call for papers or author guidelines | Does the page limit leave room for all your results? |
| Does the timing work? | Deadline, review cycle | Is there enough time before the deadline for the final checks? |
| Any unusual rules? | The anonymization, ethics, and artifact sections of the call for papers | A security conference may require a discussion of research ethics (see Section 4) |

**If a journal you have never heard of invites you to submit, ask your advisor first.** Watch out for "predatory journals" (also called "fake journals"). The 2026 recommendations of the International Committee of Medical Journal Editors (ICMJE) are written for medical journals, and describe such outlets like this: they accept almost anything, charge publication fees, and often tell you about the fee only after acceptance[^icmje2026recommendations-e34]; they claim to do peer review but don't, and may take a name close to that of a well-known journal[^icmje2026recommendations-e35]. ICMJE also reminds authors that assessing the integrity, history, practices, and reputation of the journals they submit to is the authors' own responsibility[^icmje2026recommendations-e36].

You can go through the journal checklist (2023 version) of Think. Check. Submit., an initiative launched jointly by several publishing-industry organizations[^thinkchecksubmit2023checklist-e1]. For example: do you or your colleagues know the journal[^thinkchecksubmit2023checklist-e2]? Can you identify and contact the publisher[^thinkchecksubmit2023checklist-e3]? Does it say clearly what type of peer review it uses, and does it promise guaranteed acceptance or very fast review[^thinkchecksubmit2023checklist-e4]? Are all its fees stated clearly[^thinkchecksubmit2023checklist-e5]? The checklist's advice: submit only if you can answer "yes" to most or all of the questions[^thinkchecksubmit2023checklist-e6].

These questions only help you rule out suspicious outlets. The safest approach is still to submit only to venues your advisor and peers recognize `[Our analysis]`.

**Write it down:** List two or three candidate venues. For each, fill in the six rows of the table above, and write down "which paper it published is most like mine".

## 2. Conference or journal: follow your field's norms

What counts as a "real publication" differs between fields. First find out which one your field mainly relies on, then choose within that type.

**Computer science: conferences carry great weight.** According to a 1999 memo from the Computing Research Association, experimental areas prefer conferences, and the top conferences are usually harder to get into than the top journals[^cra1999evaluating-e3]. Theory also values conferences, but has a long tradition of completing and extending conference papers and then submitting them to journals[^cra1999evaluating-e4]. For the pros, cons, and debate, see the [Computer science field overview](../07_fields/computer-science/README.md#conferences-or-journals-a-long-running-debate).

**Other fields differ a lot.** The field overviews below cover each field's norms; read the one for your field before you submit:

- Economics: circulate a working paper first, then submit to a journal; journal review is very slow. See the [Economics field overview](../07_fields/economics/README.md#working-papers-first-journal-publication-is-slow);
- Mathematics: mainly journals; publishing is slow. See the [Mathematics field overview](../07_fields/mathematics/README.md#mostly-journals-slow-and-not-many-papers);
- Physics: preprints plus journals. See the [Physical sciences field overview](../07_fields/physical-sciences/README.md#publishing-arxiv-preprints-plus-journals);
- Clinical medicine: mainly journals, many of which share one set of rules. See the [Clinical medicine field overview](../07_fields/clinical-medicine/README.md#publishing-is-mostly-in-journals-and-the-rules-are-fairly-uniform).

**You can publish the same work in stages, but say so.** In computer science, at least in principle, conference papers report complete, mature work, while workshop papers can report early work or put forward a position[^roscoe2007reviews-e12]. The 2026 Operations Manual of the Publication Services and Products Board of the Institute of Electrical and Electronics Engineers (IEEE) explicitly endorses this "progressive publication": early ideas at a workshop or as a preprint, more mature work at a conference, fully mature results in a journal[^ieee2026pspb-e4]. But it requires you to cite the earlier versions in full, and the journal version must add substantial technical content beyond the conference paper[^ieee2026pspb-e5].

Which earlier publications affect a later submission varies from venue to venue. For example:

- The 2025 call for papers of NeurIPS (the Conference on Neural Information Processing Systems, a top machine learning conference) allows submissions that were presented at a workshop, as long as they did not appear in archival proceedings[^neurips2025cfp-e7];
- The American Physical Society's 2024 ethics guidelines say that publishing an abstract or short report at a conference generally does not prevent you from later submitting a longer, more complete version, but you must disclose it fully when you submit[^aps2024ethics-e15];
- The American Chemical Society's 2026 ethical guidelines for publication say that expanding a published short communication into a full paper is generally acceptable, but you must cite the communication and inform the editor when you submit[^acs2026ethical-e6].

**Write it down:** In one or two sentences, state whether your field (or subfield) mainly relies on conferences or journals. If you plan to go to a workshop first and extend the work later, write down what the extended version will add.

## 3. Should you post a preprint first?

A **preprint** is a version of a paper made public online before formal publication. The best-known preprint server is arXiv, founded in 1991[^arxivabout-e1]. According to its 2026 "About" page, arXiv moderates submissions for relevance to the subject area and for scholarly value, but **does not do peer review**[^arxivabout-e2], and the content is entirely the submitter's responsibility[^arxivabout-e3].

**Check your target venue's policy before posting.** The ICMJE 2026 recommendations say that before posting a preprint, you should find out the policy of the journal you plan to submit to[^icmje2026recommendations-e13]. The American Physical Society's 2024 ethics guidelines say the same: many journals do not treat posting a preprint as duplicate publication, but finding and following the journal's policy is the author's responsibility[^aps2024ethics-e8]. Some examples (rules get updated; go by the page at the time you submit):

| Venue (version of the rule) | Preprint policy |
|---|---|
| NeurIPS (2025 call for papers) | A non-anonymous preprint will not get your paper rejected, and reviewers are asked not to actively search for it[^neurips2025cfp-e5]; but the public version should not say anything like "under review at NeurIPS"[^neurips2025cfp-e6] |
| USENIX Security, a top security conference (2026 call for papers) | Submissions must be anonymous, but during review authors may still post preprints, give talks, and disclose vulnerabilities[^usenixsec2026cfp-e3] |
| IEEE journals (Author Center pages, accessed 2026) | Preprints on approved nonprofit preprint servers such as arXiv and TechRxiv do not count as prior publication[^ieeeauthorposting-e1] |
| ES&T, environmental science (author guidelines, accessed 2026) | Before acceptance you may post to a preprint server that assigns the manuscript a DOI (Digital Object Identifier, a permanent ID), but you must cite the preprint[^estauthorguidelines-e16] |
| Medical journals following the ICMJE recommendations (2026 version) | When you submit, tell the journal the work has been posted as a preprint and give the link[^icmje2026recommendations-e14] |
| Philosophy journals (American Philosophical Association 2022 advice, not a binding rule) | Editors should generally be willing to consider papers already posted in a preprint archive[^apaphil2022journal-e13] |

One more thing that is easy to miss: if the submitted work is part of your thesis or dissertation, ES&T requires you either to put the thesis in a public repository with a DOI, or to delay or remove the online version of the thesis until the paper is formally published[^estauthorguidelines-e17]. Check before submitting whether other venues have similar rules `[Our analysis]`.

**Your first arXiv submission needs an "endorsement".** According to arXiv's 2026 help pages, before your first submission to arXiv, or to a new category, you need an endorsement[^arxivendorsement-e1]. For a graduate student, good choices are your advisor or a faculty member at your institution in the same area who posts on arXiv actively[^arxivendorsement-e2].

**How do you decide whether to post?** `[Our analysis]`

| Leans toward posting | Leans toward holding off |
|---|---|
| Your area routinely posts preprints first, and your peers all do | The target journal restricts preprints, or you haven't checked yet |
| Your area moves fast, and you want the work seen early | The paper still has errors or obvious gaps you know about |
| Your advisor and group have already checked the paper | Your coauthors haven't agreed to make it public |

**Write it down:** Write down your target venue's preprint policy (copy one sentence verbatim), and your reason for posting or not.

## 4. Read the submission requirements and prepare item by item

**Read the call for papers or author guidelines from start to finish.** Editors and reviewers will look at your manuscript against it[^bourne2005published-e8]. Below we go through the common requirements one at a time; your target venue's specifics take precedence.

### Format and length

Respect page limits and formatting requirements[^allman2001plea-e4]. Limits vary widely: NeurIPS 2025 allows 9 pages of main text, including figures and tables[^neurips2025cfp-e2]; ES&T (2026 author guidelines) caps research articles at 7000 words[^estauthorguidelines-e10]. Some conferences also require a checklist; for example, NeurIPS 2025 requires every submission to include the paper checklist[^neurips2025cfp-e3]. Write in the venue's template from the start; don't leave the formatting until the end `[Our analysis]`.

### Anonymization

Some conferences use **double-blind review**: reviewers don't know who the authors are, and authors don't know who the reviewers are. For example, NeurIPS 2025 requires submissions to be anonymized, with no identifying information that could violate the double-blind policy[^neurips2025cfp-e4]. The American Philosophical Association's 2022 advice goes further: it strongly recommends that philosophy journals keep authors' identities from the editors as well[^apaphil2022journal-e1].

When you cite your own earlier work, USENIX Security 2026 requires you to do it in the third person, as if citing someone else[^usenixsec2026cfp-e4]. Other common slips to check for one by one `[Our analysis]`:

- Author names, affiliations, acknowledgments, and grant numbers removed;
- Code and data links that point to a repository or personal homepage with your name on it (use an anonymized repository instead);
- Author names left in the PDF's file properties;
- Screenshots, file paths, or server names in figures that reveal your institution.

### Code, data, and other research artifacts

An **artifact**, as defined by the Association for Computing Machinery (ACM) in 2020, is a digital object created by the authors for their research or produced by their experiments, such as software, scripts that run the experiments, input data, raw data, and analysis scripts[^acm2020artifact-e1]. Venue requirements range from "voluntary" to "mandatory". For example:

- USENIX Security 2026 requires artifacts to be available during review; if you can't provide them, you must explain why in an "Open Science" appendix[^usenixsec2026cfp-e12];
- The systems conference OSDI 2024 (the USENIX Symposium on Operating Systems Design and Implementation) evaluates artifacts only after a paper is accepted, and participation is voluntary[^sysartifactsguide-e1]; but it warns that the time between acceptance and artifact submission is short, so you should start preparing while the paper is still under review[^sysartifactsguide-e2];
- The PLOS journals (data policy accessed 2026) require that all data needed to replicate the results be publicly available at publication[^plosdatapolicy-e1], that the data availability statement give the repository name and a persistent identifier[^plosdatapolicy-e3], and they do not allow "data not shown"[^plosdatapolicy-e4];
- Under the ICMJE 2026 recommendations, clinical trial papers submitted since July 2018 to journals that follow ICMJE must include a data sharing statement[^icmje2026recommendations-e22].

To earn ACM's 2020 "Artifacts Available" badge, the artifact must be in a publicly accessible archival repository, with a DOI or a link with a unique identifier; a personal homepage does not qualify[^acm2020artifact-e4]. If the artifact depends on proprietary components that can't be made public, you may leave them out, but you must state that they are needed and explain how to obtain them[^acm2020artifact-e6]. Even if your target venue doesn't award badges, this is a standard you can follow `[Our analysis]`. For how to organize code and data, see [Organizing your research materials](../08_throughout/organizing_materials.md); for artifact evaluation and badges in computer science, see the [Computer science field overview](../07_fields/computer-science/README.md#artifact-evaluation-and-badges).

### Ethics statement

Some venues require a dedicated ethics section in the paper. Take USENIX Security 2026: every submission must discuss research ethics[^usenixsec2026cfp-e2]; if you found vulnerabilities, the paper must say whom you disclosed them to and what happened[^usenixsec2026cfp-e6]; and it states specifically that approval from an institutional review board (IRB) does not relieve researchers of their own responsibility to consider the ethics[^usenixsec2026cfp-e7].

For research involving humans or animals, some journals require you to name the ethics committee that approved it and give the approval number, and, for human samples or data, to state that informed consent was obtained; ES&T's 2026 author guidelines are one example[^estauthorguidelines-e18].

Ethics is not something you start thinking about at submission time; here you are only writing down what you already did. For how to handle ethics during the research, see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md).

### Authorship and contributions

**Who should be an author?** The 2023 revised edition of *The European Code of Conduct for Research Integrity* applies to all fields[^allea2023european-e18]. It lists four conditions: a significant contribution to the research design, data collection, analysis, or interpretation; drafting or critically reviewing the paper; approving the final version; and agreeing to be responsible for the content[^allea2023european-e7]. The ICMJE 2026 recommendations also use four criteria, require every author to meet all four, and say everyone who meets all four should be an author[^icmje2026recommendations-e3]. The IEEE 2026 Operations Manual explicitly lists prototype development as one of the contributions that can qualify someone for authorship[^ieee2026pspb-e6]; for computer science research that builds systems and tools, this is worth noting `[Our analysis]`.

**Who doesn't qualify?** Under the ICMJE 2026 recommendations, acquiring funding, general supervision or administrative support, or writing assistance and language editing are not, on their own, enough for authorship[^icmje2026recommendations-e7]; these people go in the acknowledgments, with a note on what each of them did[^icmje2026recommendations-e8].

**How do you settle it?** The American Physical Society's 2024 ethics guidelines require every author to be able to identify and confirm their specific contribution[^aps2024ethics-e4], and recommend deciding, when you start writing, who will be an author, in what order, and who goes in the acknowledgments, and confirming this with everyone on the team to avoid disputes[^aps2024ethics-e5]. Author order is agreed jointly by the authors[^allea2023european-e8], not decided by the editor[^icmje2026recommendations-e27]. The American Chemical Society's 2026 guidelines also require the submitting author to send the manuscript to every coauthor and obtain their consent to be listed[^acs2026ethical-e8]. Whatever venue you submit to, do this before you submit `[Our analysis]`.

Ordering conventions vary by field: coauthored papers in economics are mostly in alphabetical order by surname; see the [Economics field overview](../07_fields/economics/README.md#alphabetical-authorship). For how to discuss authorship with your advisor, see [Collaboration and advisors](../08_throughout/collaboration_and_advisors.md).

### Conflicts of interest, funding, and prior publications

- **Funding and conflicts of interest**: The IEEE 2026 Operations Manual requires that funding sources and any potential conflicts of interest be stated in the paper[^ieee2026pspb-e10]; the 2023 edition of *The European Code of Conduct for Research Integrity* requires disclosure of both financial and non-financial conflicts of interest[^allea2023european-e10].
- **Your own similar papers**: IEEE journals (Author Center pages, accessed 2026) require you to disclose, at submission, your similar papers that have been published or submitted elsewhere, and to explain clearly how the new manuscript differs[^ieeeauthorsubmission-e1].
- **No simultaneous submission**: USENIX Security 2026 considers submitting the same work to several venues at once dishonest or fraudulent[^usenixsec2026cfp-e11]; the American Physical Society's 2024 guidelines also forbid submitting to several journals at once[^aps2024ethics-e13]; and according to the American Philosophical Association's 2022 guidance, the act of submitting itself signals that the manuscript is not under review elsewhere[^apaphil2022journal-e6].
- **Writing tools (such as large language models)**: Rules differ; here are two examples. The ICMJE 2026 recommendations, followed by medical journals, say chatbots cannot be listed as authors, because they cannot be responsible for the accuracy, integrity, and originality of the work[^icmje2026recommendations-e29]; if you used artificial intelligence (AI) to help with writing, say so in the acknowledgments; if you used it for data collection, analysis, or figures, say so in the methods[^icmje2026recommendations-e30]. IEEE journals (Author Center pages, accessed 2026) require you to disclose AI-generated content (text, figures, code, and so on) in the acknowledgments, naming the system and the sections where it was used[^ieeeauthorsubmission-e4]; using it only to edit wording and grammar does not have to be disclosed, though disclosure is recommended[^ieeeauthorsubmission-e5]. Follow whatever your target venue says.

**Write it down:** Turn your target venue's call for papers or author guidelines into a to-do table, one requirement per row: "requirement / what I do / done?". Cover at least these seven: format, anonymization, artifacts and data, ethics, authorship, conflicts of interest, and prior publications.

## 5. One last check before you submit

**A sloppy paper makes people think the research is sloppy**[^allman2001plea-e1]. Reviewers' attention is limited, and the effort you put in before submitting pays off most: spend your energy on improving the manuscript before it goes out[^bourne2005published-e6].

1. **Proofread the whole paper**[^allman2001plea-e2].
2. **Answer in advance the easy questions a reviewer will ask at first glance**, such as "why is this parameter set to 17?"[^allman2001plea-e3].
3. **Ask someone with no stake in the work to read it**, ideally including someone outside your area[^bourne2005published-e7].
4. **Check the paper against the reporting guidelines for this kind of study.** Starting without reading the existing guidelines for this kind of research is listed as an antipattern in the empirical standards of ACM SIGSOFT (the ACM Special Interest Group on Software Engineering)[^ralph2020empirical-e26]. Medicine has established reporting guidelines; one example the ICMJE 2026 recommendations give is CONSORT for randomized trials[^icmje2026recommendations-e25].
5. **Go through the to-do table from Section 4** and tick off every item.
6. **For a journal, write a good cover letter.** According to ES&T's 2026 author guidelines, a substantial share of its submissions are not sent out for review, because the editors judge them insufficient in novelty, scientific merit, or environmental importance; the cover letter is your chance to persuade the editor[^estauthorguidelines-e12]. In two or three sentences, say what problem the paper solves, what the main findings are, and why it fits this journal `[Our analysis]`.

**Leave yourself time for these checks.** If you do them on deadline day, things get missed `[Our analysis]`. Set an internal deadline before the official one; see [Writing a research plan](../01_from-interest-to-project/04_research-plan.md#5-estimate-time-and-build-in-slack).

**Write it down:** Set an "internal final-draft date" at least one week before the deadline, and write down who will read the whole paper before that date.

## 6. What happens after you submit

Once you click "Submit", you are waiting. If you know the process, you know what to do while you wait.

**Conferences (computer science as the example)** `[Our analysis, based on the sources below]`:

| Stage | What happens |
|---|---|
| Review | Members of the program committee (the group of researchers who review papers and decide acceptance) review the paper; some conferences send early reject notifications, for example USENIX Security 2026[^usenixsec2026cfp-e1] |
| Author response | Some conferences let you respond in writing, within a short window, after seeing the initial reviews; NeurIPS 2025, for example, allows one week[^neurips2025cfp-e8] |
| Discussion and decision | The committee discusses and decides. When writing your response, it is best to assume the area chair (the senior member who consolidates the reviews and makes a recommendation) reads only the reviews and your response[^parikh2020rebuttals-e2]; if no reviewer is willing to champion your paper in the discussion, its chance of acceptance is small[^zeller2012rebuttals-e1] |
| After acceptance | Revise according to the reviews and submit the camera-ready version; some conferences also have artifact evaluation, for example OSDI 2024[^sysartifactsguide-e1] |

For the details of one conference's process, see the [Computer science field overview](../07_fields/computer-science/README.md#the-life-of-a-conference-paper).

**Journals**: The editor looks at the manuscript first and may reject it without sending it out for review (a desk reject); the American Philosophical Association's 2022 advice is that editors should also have read the manuscript anonymously before making that decision[^apaphil2022journal-e2]. After review, the editor decides, based on the reviews, to accept, ask for a revision and re-review, or reject `[Our analysis]`. If you get a major revision, revise seriously, and address every comment both in the response letter and in the revised text[^bourne2005published-e2]. Journal review can take months; for the figures by field, see [Writing a research plan](../01_from-interest-to-project/04_research-plan.md#1-fix-the-finish-line-where-to-submit-and-when). The American Philosophical Association's 2022 advice is that four months after submission you may ask about the status of the review, unless the journal has said it takes longer[^apaphil2022journal-e7]; journals in other fields may differ, so check the average review time on the journal's website first `[Our analysis]`.

**Things to do while you wait** `[Our analysis]`:

- Prepare your artifact: OSDI 2024, for example, warns that the time between acceptance and artifact submission is short[^sysartifactsguide-e2];
- Think about which points reviewers are most likely to challenge, and prepare supporting data in advance, so you aren't scrambling during the response period;
- Start your next project rather than refreshing the submission system all day.

**Things not to do while you wait**: Don't submit the same paper anywhere else (USENIX Security 2026 considers it dishonest or fraudulent[^usenixsec2026cfp-e11]); and when you update your preprint, don't write "under review at such-and-such conference" (NeurIPS 2025 explicitly forbids it[^neurips2025cfp-e6]).

**When the decision comes.** The final decision is the collective judgment of all the reviewers, "more art than science"[^hicks2014reviewing-e10]; the purpose of a conference's discussion is to select a set of the best papers, not to pass a verdict on each paper[^roscoe2007reviews-e14]. So one decision doesn't capture the full value of your work `[Our analysis]`.

- **If you have to revise, respond, or were rejected**: see [Reviews, revision, and what to do after rejection](03_review-and-revision.md).
- **If you were accepted**: submit the final version as required, and check the venue's rules for after acceptance. For example, the IEEE 2026 Operations Manual expects authors of conference papers to present them at the conference, and IEEE may leave papers that weren't presented out of its post-conference database[^ieee2026pspb-e13]; IEEE journals (Author Center pages, accessed 2026) require that after acceptance you replace any previously posted version with a citation that includes the DOI, or with the accepted version carrying the DOI and a copyright notice[^ieeeauthorposting-e2]; the American Physical Society's 2024 guidelines require that after formal publication you add a link to the published version on your preprint[^aps2024ethics-e8].
- **If you find an error after publication**: correct it promptly; the IEEE 2026 Operations Manual makes this an obligation of authors[^ieee2026pspb-e14].

**Write it down:** Write down the key dates for your target venue from submission to decision (response period, notification date, camera-ready deadline), and two things you plan to do while you wait.

---

## Judgment calls

**Which tier to aim for?** `[Our analysis]`

| Situation | Usual approach |
|---|---|
| The evidence is solid and on par with work the top venues publish | Submit to a top venue; if rejected, revise according to the reviews and resubmit |
| The claim is good, but the evidence supports only part of it | Narrow the claim and submit; or go to a workshop first to get feedback |
| An early idea, still missing key experiments | A workshop or a preprint; submit the full paper once the evidence is in |
| You don't know whether it's good enough | Put three papers the venue accepted next to yours and compare, then ask your advisor |

Better to publish one paper in a high-quality journal than several in weaker ones[^bourne2005published-e9].

**Make this deadline, or wait for the next?** Some criticize computer science for being deadline-driven: papers get submitted when a suitable deadline comes along, not when the research is truly ready[^fortnow2009time-e2]. If the evidence still isn't enough by the deadline, better to aim for the next venue, or narrow your claim to what the evidence can support `[Our analysis]`.

## Common mistakes

| Mistake | Why it's a problem |
|---|---|
| Choosing a venue by prestige alone, ignoring its readers and scope | If the paper falls short of the journal's bar for novelty and significance, it may be returned without review (ES&T 2026 author guidelines)[^estauthorguidelines-e12] |
| Writing in another venue's format without reading the call for papers | Editors and reviewers read the manuscript against the submission guidelines[^bourne2005published-e8] |
| Writing "our previous work [5]" in a double-blind submission | It reveals who you are; USENIX Security 2026 requires citing your own work in the third person[^usenixsec2026cfp-e4] |
| Writing "under review at such-and-such conference" on the preprint | NeurIPS 2025 explicitly forbids it[^neurips2025cfp-e6] |
| Extending a conference version into a journal version without citing it or explaining the differences | IEEE requires citing the earlier version and explaining what the new manuscript adds[^ieee2026pspb-e5][^ieeeauthorsubmission-e1] |
| Submitting the same paper to two places at once | USENIX Security 2026 considers it dishonest or fraudulent[^usenixsec2026cfp-e11] |
| Not confirming authorship with coauthors before submitting | The American Chemical Society's 2026 guidelines require the submitting author to obtain every coauthor's consent[^acs2026ethical-e8] |
| Treating code on your personal homepage as "publicly available" | ACM's "Artifacts Available" badge doesn't accept personal homepages; the artifact must be in a public archival repository[^acm2020artifact-e4] |
| Starting to organize the artifact only after acceptance | At OSDI 2024, for example, the time between acceptance and artifact submission is short[^sysartifactsguide-e2] |
| Proofreading on deadline day | A sloppy paper makes people think the research is sloppy[^allman2001plea-e1] |

## What you should have at the end

- A comparison table of candidate venues, plus the venue you chose and why (Section 1)
- Your decision on the preprint and its basis (Section 3)
- A to-do table of submission requirements, with every item done (Section 4)
- A cover letter (for a journal, Section 5)
- Artifacts and data prepared as required (if the target venue requires them)
- A table of key dates after submission (Section 6)

## Checklist before moving on

You are ready to click "Submit" when:

- [ ] You can say who reads your target venue, and which paper it published is most like yours
- [ ] You know whether your field mainly uses conferences or journals, and chose a venue accordingly
- [ ] You have checked the target venue's preprint policy, and what you did complies with it
- [ ] Format, length, and anonymization have all been checked against the requirements
- [ ] Statements on artifacts, data, ethics, and conflicts of interest are written as required
- [ ] Every author has seen the final version and agrees to the author list and order
- [ ] At least one person not involved in the work has read it from start to finish

## When to go back

| If this happens | Go back to |
|---|---|
| You can't find a single venue with the right readers | Your claim may still be unclear; go back to [Converging on a project](../01_from-interest-to-project/03_converge.md) |
| The paper won't fit, and cutting any part seems to break the argument | The paper's storyline isn't clear yet; go back to [Telling the story and writing the paper](01_story-and-paper.md) |
| After reading the target venue's papers, you see your evidence is clearly not enough | Go back to [Running and iterating](../03_conduct-and-analyze/01_run-and-iterate.md) for more experiments, or narrow the claim |
| While writing the ethics statement, you find an issue you never dealt with | Stop and talk to your advisor; see [Research integrity and ethics](../08_throughout/integrity_and_ethics.md) |
| Coauthors disagree about authorship | Resolve it before submitting; see [Collaboration and advisors](../08_throughout/collaboration_and_advisors.md) |

## Next

Once the paper is out, sooner or later the reviews will come back: you will need to respond, revise, or deal with a rejection. For how to read reviews, write a response, revise, and what to do after a rejection, see [Reviews, revision, and what to do after rejection](03_review-and-revision.md). For how to approach your first time as a reviewer, see [Being a reviewer](../08_throughout/being_a_reviewer.md).

[^bourne2005published-e2]: Bourne 2005, Rule 5. [Evidence](../../sources/notes/bourne2005published.md#e2)
[^bourne2005published-e5]: Bourne 2005, Rule 9. [Evidence](../../sources/notes/bourne2005published.md#e5)
[^bourne2005published-e6]: Bourne 2005, Rule 3. [Evidence](../../sources/notes/bourne2005published.md#e6)
[^bourne2005published-e7]: Bourne 2005, Rule 6. [Evidence](../../sources/notes/bourne2005published.md#e7)
[^bourne2005published-e8]: Bourne 2005, Rule 7. [Evidence](../../sources/notes/bourne2005published.md#e8)
[^bourne2005published-e9]: Bourne 2005, Rule 10. [Evidence](../../sources/notes/bourne2005published.md#e9)
[^bourne2005published-e10]: Bourne 2005, Rule 9. [Evidence](../../sources/notes/bourne2005published.md#e10)
[^hicks2014reviewing-e9]: Hicks 2014 (reviewing), Interesting or useful? [Evidence](../../sources/notes/hicks2014reviewing.md#e9)
[^hicks2014reviewing-e10]: Hicks 2014 (reviewing), Interesting or useful? [Evidence](../../sources/notes/hicks2014reviewing.md#e10)
[^apaphil2022journal-e1]: American Philosophical Association 2022, Guidelines for Journals / Communicating with Authors. [Evidence](../../sources/notes/apaphil2022journal.md#e1)
[^apaphil2022journal-e2]: American Philosophical Association 2022, Guidelines for Journals / Communicating with Authors. [Evidence](../../sources/notes/apaphil2022journal.md#e2)
[^apaphil2022journal-e3]: American Philosophical Association 2022, Guidelines for Authors / Manuscript Preparation. [Evidence](../../sources/notes/apaphil2022journal.md#e3)
[^apaphil2022journal-e4]: American Philosophical Association 2022, Guidelines for Authors / Manuscript Preparation. [Evidence](../../sources/notes/apaphil2022journal.md#e4)
[^apaphil2022journal-e5]: American Philosophical Association 2022, Guidelines for Authors / Manuscript Preparation. [Evidence](../../sources/notes/apaphil2022journal.md#e5)
[^apaphil2022journal-e6]: American Philosophical Association 2022, Guidelines for Authors / Manuscript Submission/Resubmission. [Evidence](../../sources/notes/apaphil2022journal.md#e6)
[^apaphil2022journal-e7]: American Philosophical Association 2022, Guidelines for Authors / Requests for Information. [Evidence](../../sources/notes/apaphil2022journal.md#e7)
[^apaphil2022journal-e13]: American Philosophical Association 2022, Copyright and Open Access / Consideration of Previously Posted Papers. [Evidence](../../sources/notes/apaphil2022journal.md#e13)
[^estauthorguidelines-e1]: ES&T Author Guidelines (accessed 2026-10-06), Journal Scope. [Evidence](../../sources/notes/estauthorguidelines.md#e1)
[^estauthorguidelines-e2]: ES&T Author Guidelines (accessed 2026-10-06), Journal Scope. [Evidence](../../sources/notes/estauthorguidelines.md#e2)
[^estauthorguidelines-e10]: ES&T Author Guidelines (accessed 2026-10-06), Article Types. [Evidence](../../sources/notes/estauthorguidelines.md#e10)
[^estauthorguidelines-e12]: ES&T Author Guidelines (accessed 2026-10-06), Cover Letter. [Evidence](../../sources/notes/estauthorguidelines.md#e12)
[^estauthorguidelines-e16]: ES&T Author Guidelines (accessed 2026-10-06), Prior Publication Policy. [Evidence](../../sources/notes/estauthorguidelines.md#e16)
[^estauthorguidelines-e17]: ES&T Author Guidelines (accessed 2026-10-06), Theses/Dissertations. [Evidence](../../sources/notes/estauthorguidelines.md#e17)
[^estauthorguidelines-e18]: ES&T Author Guidelines (accessed 2026-10-06), Ethical Use of Animals or Human Participants in Research. [Evidence](../../sources/notes/estauthorguidelines.md#e18)
[^cra1999evaluating-e3]: Patterson, Snyder & Ullman 1999, Structure of The Field. [Evidence](../../sources/notes/cra1999evaluating.md#e3)
[^cra1999evaluating-e4]: Patterson, Snyder & Ullman 1999, Structure of The Field. [Evidence](../../sources/notes/cra1999evaluating.md#e4)
[^roscoe2007reviews-e12]: Roscoe 2007, §4, p. 4. [Evidence](../../sources/notes/roscoe2007reviews.md#e12)
[^roscoe2007reviews-e14]: Roscoe 2007, §6, p. 5. [Evidence](../../sources/notes/roscoe2007reviews.md#e14)
[^ieee2026pspb-e4]: IEEE PSPB Operations Manual 2026, §8.1.7.F, p. 91. [Evidence](../../sources/notes/ieee2026pspb.md#e4)
[^ieee2026pspb-e5]: IEEE PSPB Operations Manual 2026, §8.1.7.F, pp. 91–92. [Evidence](../../sources/notes/ieee2026pspb.md#e5)
[^ieee2026pspb-e6]: IEEE PSPB Operations Manual 2026, §8.2.1.A.1, p. 104. [Evidence](../../sources/notes/ieee2026pspb.md#e6)
[^ieee2026pspb-e10]: IEEE PSPB Operations Manual 2026, §8.2.1.B.2, p. 106. [Evidence](../../sources/notes/ieee2026pspb.md#e10)
[^ieee2026pspb-e13]: IEEE PSPB Operations Manual 2026, §8.2.1.B.16, p. 107. [Evidence](../../sources/notes/ieee2026pspb.md#e13)
[^ieee2026pspb-e14]: IEEE PSPB Operations Manual 2026, §8.2.1.B.8, p. 106. [Evidence](../../sources/notes/ieee2026pspb.md#e14)
[^ieeeauthorsubmission-e1]: IEEE Author Center (accessed 2026-10-06), Submission Policies — Multiple Submission and Prior Publication. [Evidence](../../sources/notes/ieeeauthorsubmission.md#e1)
[^ieeeauthorsubmission-e4]: IEEE Author Center (accessed 2026-10-10), Guidelines for Artificial Intelligence (AI)-Generated Content. [Evidence](../../sources/notes/ieeeauthorsubmission.md#e4)
[^ieeeauthorsubmission-e5]: IEEE Author Center (accessed 2026-10-10), Guidelines for Artificial Intelligence (AI)-Generated Content. [Evidence](../../sources/notes/ieeeauthorsubmission.md#e5)
[^ieeeauthorposting-e1]: IEEE Author Center (accessed 2026-10-06), Article Sharing and Posting Policies — Preprint. [Evidence](../../sources/notes/ieeeauthorposting.md#e1)
[^ieeeauthorposting-e2]: IEEE Author Center (accessed 2026-10-06), Article Sharing and Posting Policies — Author-submitted article. [Evidence](../../sources/notes/ieeeauthorposting.md#e2)
[^neurips2025cfp-e2]: NeurIPS 2025 Call for Papers, Paper Formatting Instructions. [Evidence](../../sources/notes/neurips2025cfp.md#e2)
[^neurips2025cfp-e3]: NeurIPS 2025 Call for Papers, Paper Checklist. [Evidence](../../sources/notes/neurips2025cfp.md#e3)
[^neurips2025cfp-e4]: NeurIPS 2025 Call for Papers, Double-blind Reviewing. [Evidence](../../sources/notes/neurips2025cfp.md#e4)
[^neurips2025cfp-e5]: NeurIPS 2025 Call for Papers, Preprints. [Evidence](../../sources/notes/neurips2025cfp.md#e5)
[^neurips2025cfp-e6]: NeurIPS 2025 Call for Papers, Preprints. [Evidence](../../sources/notes/neurips2025cfp.md#e6)
[^neurips2025cfp-e7]: NeurIPS 2025 Call for Papers, Dual Submissions. [Evidence](../../sources/notes/neurips2025cfp.md#e7)
[^neurips2025cfp-e8]: NeurIPS 2025 Call for Papers, Author Responses. [Evidence](../../sources/notes/neurips2025cfp.md#e8)
[^usenixsec2026cfp-e1]: USENIX Security '26 call for papers, Important Dates. [Evidence](../../sources/notes/usenixsec2026cfp.md#e1)
[^usenixsec2026cfp-e2]: USENIX Security '26 call for papers, Executive Summary. [Evidence](../../sources/notes/usenixsec2026cfp.md#e2)
[^usenixsec2026cfp-e3]: USENIX Security '26 call for papers, Anonymous Submission. [Evidence](../../sources/notes/usenixsec2026cfp.md#e3)
[^usenixsec2026cfp-e4]: USENIX Security '26 call for papers, Anonymous Submission. [Evidence](../../sources/notes/usenixsec2026cfp.md#e4)
[^usenixsec2026cfp-e6]: USENIX Security '26 call for papers, Ethics Guidelines, Disclosures. [Evidence](../../sources/notes/usenixsec2026cfp.md#e6)
[^usenixsec2026cfp-e7]: USENIX Security '26 call for papers, Ethics Guidelines, Is IRB approval a sufficient alternative? [Evidence](../../sources/notes/usenixsec2026cfp.md#e7)
[^usenixsec2026cfp-e11]: USENIX Security '26 call for papers, Simultaneous Submission and Plagiarism. [Evidence](../../sources/notes/usenixsec2026cfp.md#e11)
[^usenixsec2026cfp-e12]: USENIX Security '26 call for papers, Executive Summary. [Evidence](../../sources/notes/usenixsec2026cfp.md#e12)
[^aps2024ethics-e4]: American Physical Society Ethics Standards 2024, II. Authorship. [Evidence](../../sources/notes/aps2024ethics.md#e4)
[^aps2024ethics-e5]: American Physical Society Ethics Standards 2024, II. Authorship. [Evidence](../../sources/notes/aps2024ethics.md#e5)
[^aps2024ethics-e8]: American Physical Society Ethics Standards 2024, III. Redundant Publication. [Evidence](../../sources/notes/aps2024ethics.md#e8)
[^aps2024ethics-e13]: American Physical Society Ethics Standards 2024, III. Redundant Publication. [Evidence](../../sources/notes/aps2024ethics.md#e13)
[^aps2024ethics-e15]: American Physical Society Ethics Standards 2024, III. Redundant Publication. [Evidence](../../sources/notes/aps2024ethics.md#e15)
[^acs2026ethical-e6]: American Chemical Society Ethical Guidelines to Publication of Chemical Research 2026, B, item 9. [Evidence](../../sources/notes/acs2026ethical.md#e6)
[^acs2026ethical-e8]: American Chemical Society Ethical Guidelines to Publication of Chemical Research 2026, B, item 13. [Evidence](../../sources/notes/acs2026ethical.md#e8)
[^arxivabout-e1]: arXiv (accessed 2026-10-06), About arXiv, para. 4. [Evidence](../../sources/notes/arxivabout.md#e1)
[^arxivabout-e2]: arXiv (accessed 2026-10-06), About arXiv. [Evidence](../../sources/notes/arxivabout.md#e2)
[^arxivabout-e3]: arXiv (accessed 2026-10-06), About arXiv. [Evidence](../../sources/notes/arxivabout.md#e3)
[^arxivendorsement-e1]: arXiv (accessed 2026-10-06), The arXiv endorsement system. [Evidence](../../sources/notes/arxivendorsement.md#e1)
[^arxivendorsement-e2]: arXiv (accessed 2026-10-06), The arXiv endorsement system. [Evidence](../../sources/notes/arxivendorsement.md#e2)
[^icmje2026recommendations-e3]: ICMJE 2026, §II.A.2. [Evidence](../../sources/notes/icmje2026recommendations.md#e3)
[^icmje2026recommendations-e7]: ICMJE 2026, §II.A.3. [Evidence](../../sources/notes/icmje2026recommendations.md#e7)
[^icmje2026recommendations-e8]: ICMJE 2026, §II.A.3. [Evidence](../../sources/notes/icmje2026recommendations.md#e8)
[^icmje2026recommendations-e13]: ICMJE 2026, §III.D.3. [Evidence](../../sources/notes/icmje2026recommendations.md#e13)
[^icmje2026recommendations-e14]: ICMJE 2026, §III.D.3.b. [Evidence](../../sources/notes/icmje2026recommendations.md#e14)
[^icmje2026recommendations-e22]: ICMJE 2026, §III.L.3. [Evidence](../../sources/notes/icmje2026recommendations.md#e22)
[^icmje2026recommendations-e25]: ICMJE 2026, §IV.A.2. [Evidence](../../sources/notes/icmje2026recommendations.md#e25)
[^icmje2026recommendations-e27]: ICMJE 2026, §II.A.2. [Evidence](../../sources/notes/icmje2026recommendations.md#e27)
[^icmje2026recommendations-e29]: ICMJE 2026, §II.A.4. [Evidence](../../sources/notes/icmje2026recommendations.md#e29)
[^icmje2026recommendations-e30]: ICMJE 2026, §II.A.4. [Evidence](../../sources/notes/icmje2026recommendations.md#e30)
[^icmje2026recommendations-e34]: ICMJE 2026, §II.C.1.a. [Evidence](../../sources/notes/icmje2026recommendations.md#e34)
[^icmje2026recommendations-e35]: ICMJE 2026, §II.C.1.a. [Evidence](../../sources/notes/icmje2026recommendations.md#e35)
[^icmje2026recommendations-e36]: ICMJE 2026, §II.C.1.a. [Evidence](../../sources/notes/icmje2026recommendations.md#e36)
[^thinkchecksubmit2023checklist-e1]: Think. Check. Submit. journal checklist (2023 version, accessed 2026-10-10), footer description of the initiative. [Evidence](../../sources/notes/thinkchecksubmit2023checklist.md#e1)
[^thinkchecksubmit2023checklist-e2]: Think. Check. Submit. journal checklist (2023 version, accessed 2026-10-10), checklist items. [Evidence](../../sources/notes/thinkchecksubmit2023checklist.md#e2)
[^thinkchecksubmit2023checklist-e3]: Think. Check. Submit. journal checklist (2023 version, accessed 2026-10-10), checklist items. [Evidence](../../sources/notes/thinkchecksubmit2023checklist.md#e3)
[^thinkchecksubmit2023checklist-e4]: Think. Check. Submit. journal checklist (2023 version, accessed 2026-10-10), checklist items. [Evidence](../../sources/notes/thinkchecksubmit2023checklist.md#e4)
[^thinkchecksubmit2023checklist-e5]: Think. Check. Submit. journal checklist (2023 version, accessed 2026-10-10), checklist items. [Evidence](../../sources/notes/thinkchecksubmit2023checklist.md#e5)
[^thinkchecksubmit2023checklist-e6]: Think. Check. Submit. journal checklist (2023 version, accessed 2026-10-10), end of the checklist. [Evidence](../../sources/notes/thinkchecksubmit2023checklist.md#e6)
[^allea2023european-e18]: ALLEA 2023, Preamble. [Evidence](../../sources/notes/allea2023european.md#e18)
[^allea2023european-e7]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e7)
[^allea2023european-e8]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e8)
[^allea2023european-e10]: ALLEA 2023, §2.7. [Evidence](../../sources/notes/allea2023european.md#e10)
[^acm2020artifact-e1]: ACM 2020, opening. [Evidence](../../sources/notes/acm2020artifact.md#e1)
[^acm2020artifact-e4]: ACM 2020, Artifacts Available v1.1. [Evidence](../../sources/notes/acm2020artifact.md#e4)
[^acm2020artifact-e6]: ACM 2020, Artifacts Evaluated – Functional, Notes. [Evidence](../../sources/notes/acm2020artifact.md#e6)
[^sysartifactsguide-e1]: sysartifacts, OSDI '24 Call for Artifacts. [Evidence](../../sources/notes/sysartifactsguide.md#e1)
[^sysartifactsguide-e2]: sysartifacts, OSDI '24 Call for Artifacts. [Evidence](../../sources/notes/sysartifactsguide.md#e2)
[^plosdatapolicy-e1]: PLOS Data Availability (accessed 2026-10-06), Introduction. [Evidence](../../sources/notes/plosdatapolicy.md#e1)
[^plosdatapolicy-e3]: PLOS Data Availability (accessed 2026-10-06), Acceptable data sharing methods. [Evidence](../../sources/notes/plosdatapolicy.md#e3)
[^plosdatapolicy-e4]: PLOS Data Availability (accessed 2026-10-06), Minimal data set. [Evidence](../../sources/notes/plosdatapolicy.md#e4)
[^allman2001plea-e1]: Allman 2001, 2. Sloppy Papers Are Long Shots. [Evidence](../../sources/notes/allman2001plea.md#e1)
[^allman2001plea-e2]: Allman 2001, 2. Sloppy Papers Are Long Shots. [Evidence](../../sources/notes/allman2001plea.md#e2)
[^allman2001plea-e3]: Allman 2001, 7. Answer All The Easy Questions. [Evidence](../../sources/notes/allman2001plea.md#e3)
[^allman2001plea-e4]: Allman 2001, 6. Don't Waste My Time III. [Evidence](../../sources/notes/allman2001plea.md#e4)
[^ralph2020empirical-e26]: SIGSOFT General Standard, Research and Reporting Antipatterns. [Evidence](../../sources/notes/ralph2020empirical.md#e26)
[^parikh2020rebuttals-e2]: Parikh, Batra & Lee 2020, who reads the rebuttal. [Evidence](../../sources/notes/parikh2020rebuttals.md#e2)
[^zeller2012rebuttals-e1]: Zeller 2012, Identify the champion. [Evidence](../../sources/notes/zeller2012rebuttals.md#e1)
[^fortnow2009time-e2]: Fortnow 2009, main text. [Evidence](../../sources/notes/fortnow2009time.md#e2)
