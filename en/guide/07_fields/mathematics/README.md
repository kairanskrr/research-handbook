# Mathematics: field overview

This page explains how research actually runs in mathematics: the output is proofs; collaborations are small and authors are listed alphabetically; publishing is mainly in journals and is slow; arXiv preprints matter; and advisors, problem choice, and seminars all play a role. For what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md); we do not repeat it here. **How to write a proof and how to check your own proof** is already covered in [Theoretical research](../computer-science/practices/theoretical_research.md) on the Computer science page (the parts marked as applying to all proof-based work apply to mathematics), so this page does not repeat that either. For the research strategies mathematics commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence).

**After reading this page, you should be able to:**

- describe the stages a math paper goes through from idea to publication, and why it is slow;
- understand what alphabetical authorship, arXiv preprints, and anonymous refereeing mean in mathematics;
- name the research strategies mathematics commonly uses and the evidence each relies on, and know how to learn through seminars and the literature;
- avoid the mistakes newcomers most often make with authorship, announcing results, and submitting papers.

---

## How research works in this field

### The output is a proof; the goal is understanding

The core of a math paper is its theorems and proofs. But for William Thurston, the mathematician, proof is not the whole point. He argues that what mathematicians are fundamentally doing is finding ways for people to understand and think about mathematics[^thurston1994proof-e1]. The controversy over the computer proof of the four-color theorem shows exactly this: people want not only to know that a theorem is true but also to understand its proof[^thurston1994proof-e2].

What makes a proof reliable? Thurston's view: people are not very good at checking formal correctness line by line, but they are quite good at spotting where a proof is weak[^thurston1994proof-e9]; the reliability of mathematical results comes mainly from mathematicians thinking carefully and critically about the ideas involved[^thurston1994proof-e11]. So he argues for writing proofs clearly and as simply as possible, so that weak spots are easy to find[^thurston1994proof-e10]. For how to write them, see [Theoretical research](../computer-science/practices/theoretical_research.md#step-3-write-the-proof-so-it-can-be-checked-all-proof-based-work).

### One person or a few, listed alphabetically

In 2004 the American Mathematical Society (AMS) issued a statement specifically to explain the culture of collaboration in mathematics:

- In most areas of mathematics, collaboration means sharing ideas and skills that cannot be separated out and credited to individuals; roles are rarely divided as they are in the experimental sciences[^amsculture2004joint-e1]. Ideas grow out of discussion among all the collaborators, and asking "who contributed which idea" is often meaningless[^amsculture2004joint-e7].
- Collaborations almost always involve a small number of people contributing equally[^amsculture2004joint-e2].
- So mathematicians have traditionally listed authors **alphabetically by surname**[^amsculture2004joint-e3]. The statistics the statement cites: of journal papers with at least one US author, nearly half are coauthored, and more than 75% of those list authors alphabetically; for coauthored papers in pure mathematics, the figure is more than 90%[^amsculture2004joint-e4].
- People in other fields often misunderstand this, which can sometimes hurt young mathematicians, especially those whose surnames come late in the alphabet[^amsculture2004joint-e6].

Alphabetical order does not mean "it doesn't matter who is on the paper". The AMS Ethical Guidelines require that every listed author have made a significant contribution to the content, and that everyone who made a significant contribution be offered the opportunity to be an author[^ams2022ethical-e5].

"One person" does not mean working in isolation either. Thurston stresses that the social setting of mathematical research is extremely important[^thurston1994proof-e12]; people who prove theorems do so within a mathematical community, not on their own[^thurston1994proof-e14].

### Mostly journals, slow, and not many papers

A second AMS statement, from 2006, explains mathematicians' publishing habits:

- Compared with some other sciences, mathematicians publish relatively little, and most research appears in refereed journals rather than conference proceedings or books[^amsculture2006rates-e1]. Of the items indexed in *Mathematical Reviews* (an index of the mathematical literature) from 2001 to 2005, 80% came from refereed journals[^amsculture2006rates-e5].
- A paper is usually a mature treatment of a problem, and mathematical research is not considered time-sensitive, so **publication delays are common**[^amsculture2006rates-e2]. Terence Tao, the mathematician, says the gap between posting a preprint and formal publication is measured in years[^taocareer-e28].
- Publishing little does not mean doing poorly. Of the 40 mathematicians who received Sloan Research Fellowships in 2005–2006, 70% had published on average no more than two papers a year in the five years before the award[^amsculture2006rates-e3]. Most mathematicians' work is judged mainly on the quality of their papers, not the speed[^amsculture2006rates-e4].

We have no reliable general figure for how long a journal takes from submission to acceptance. Before submitting, check the figures your target journal publishes, or ask your advisor. The AMS Ethical Guidelines say published articles should show the date of original submission and of any revisions[^ams2022ethical-e11]; leaf through recent articles in your target journal and you can get a rough idea of how long it takes from submission to acceptance.

### The life of a paper

The table below shows the usual process; the basis for each stage is in the right-hand column:

| Stage | What happens | Note |
|---|---|---|
| Ideas and partial results | A problem often takes months before real progress[^taocareer-e34] | Partial progress is valuable in itself[^taocareer-e6] |
| Discussion and talks | Present in seminars and discuss face to face with colleagues | Face-to-face conversation conveys far more than formal mathematical language[^thurston1994proof-e5] |
| Writing the full paper | Write out every detail | For how, see [Theoretical research](../computer-science/practices/theoretical_research.md) |
| Posting a preprint | Make it public on arXiv | Do not announce a result before it is of publishable quality[^taocareer-e30] |
| Submitting to a journal | Choose a suitable journal | Sending a borderline paper to a top journal can mean a long process that ends in rejection[^taowriting-e17] |
| Refereeing and revision | Anonymous referees read it and the editor decides | Editors accept only when reasonably confident the paper is correct[^ams2022ethical-e9] |
| Formal publication | Often long after the preprint went public | The gap is measured in years[^taocareer-e28] |

### arXiv preprints

A **preprint** is a version of a paper made public before formal publication. arXiv is a preprint server where submissions are classified by research area[^arxivmoderation-e2].

- **Why post one**: formal publication takes years, and a preprint lets others read your work now[^taocareer-e28]; arXiv has a reliable timestamp, which establishes priority, that is, proof that you got the result first[^taocareer-e29].
- **When to go public**: if all you have is a draft that is not of publishable quality, it is best not to announce the result yet[^taocareer-e30].
- **Your first submission needs an "endorsement"** (someone vouching for you)[^arxivendorsement-e1]. For a graduate student, the best person to ask is your advisor, or a faculty member at your institution in the same area who is active on arXiv[^arxivendorsement-e2]. Do not send mass emails looking for an endorser, and do not keep chasing people[^arxivendorsement-e3].
- **arXiv moderation is not peer review**: moderators do not give you feedback on your paper[^arxivmoderation-e1], but they may move it to the most relevant category[^arxivmoderation-e2]. Submissions with no original research, such as course assignments or research proposals, may be rejected[^arxivmoderation-e3]. So "it's on arXiv" does not mean "it has been accepted by the community".
- **Should you send your preprint to experts?** Tao does so only when the preprint is directly relevant to them, for example when it solves a conjecture they posed[^taocareer-e31].

### Refereeing: anonymous, confidential, focused on correctness

The AMS Ethical Guidelines set out clearly what referees for math journals must do:

- Referees are anonymous unless otherwise stated in advance[^ams2022ethical-e8].
- Editors and referees keep manuscripts confidential and **must not appropriate ideas from the manuscript**[^ams2022ethical-e10].
- If there is a conflict of interest (for example, the manuscript concerns your own research or that of a colleague or student), you should withdraw[^ams2022ethical-e7].
- Editors judge a paper against the state of knowledge at the time of submission, and accept it only when reasonably confident that it is correct[^ams2022ethical-e9].

As an author, make the referee's job easy. When deciding what level of journal to aim for, Tao suggests first asking yourself whether the paper is written so that the correctness of the argument is easy to check[^taowriting-e19]. Before submitting, also check whether the journal's editorial board includes someone who knows your area[^taowriting-e18]. For the general review process and how to be a referee, see the Writing and publishing chapter [Choosing a venue and submitting](../../03_write-and-publish/02_venue-and-submission.md).

### Advisors and choosing problems

For how to work with your advisor and how to choose your first problem, see [Collaboration and advisors](../../08_throughout/collaboration_and_advisors.md) and [Generating candidate problems](../../01_find-a-problem/02_generate-problems.md). Two points are worth special attention in mathematics:

- **The degree has to show that you can do mathematics independently.** The AMS Ethical Guidelines state that a doctorate in mathematics certifies both mathematical knowledge and independent mathematical achievement[^ams2022ethical-e12]. If your advisor has little time, talk regularly with at least one other mathematician[^taocareer-e25].
- **Choose a feasible first problem.** Famous problems are almost never solved out of nowhere[^taocareer-e13]; spend most of your time on more tractable problems, building experience, skill, and reputation, and take on bigger projects when you are ready[^taocareer-e14]. The AMS Ethical Guidelines also say that those who supervise doctoral students should tell them about employment opportunities inside and outside academia[^ams2022ethical-e13]; you can ask about this yourself.

### Reading the literature and seminars

In mathematics, a lot is learned by listening, not just by reading. For general ways to read the literature, see [Entering a field and exploring the literature](../../01_find-a-problem/01_enter-a-field.md); here we cover only how mathematicians do it:

- As a graduate student, Thurston did not understand what a "proof" was; he came to understand it gradually by going to **seminars** (small, regular research talks and discussions), reading papers, and talking with other graduate students[^thurston1994proof-e6].
- Within a subfield, the idea of an important proof can often be explained face to face in a few minutes[^thurston1994proof-e4]. Face-to-face conversation can use far more ways of communicating than formal mathematical language[^thurston1994proof-e5].
- To find out which facts a field takes for granted, Thurston's method was to look at which facts other papers in the field cite without proof, and what their reference lists contain[^thurston1994proof-e7].
- Also go to talks that are not directly related to your area: knowing what others are working on and what they find interesting often gives you a new perspective on your own work[^taocareer-e32]. It is normal not to understand all of it; if you learn something, the talk was worth it[^taocareer-e33]. Thurston also admits that at a typical colloquium (a talk aimed at a broader audience), most of the audience gets little out of it[^thurston1994proof-e3].
- Keeping up with new work: subscribe to arXiv alerts for new papers in your area[^taocareer-e27]; starting from one relevant paper, go backward through its references, and go forward with MathSciNet (a database of the mathematical literature) to see who cited it[^taocareer-e36].

---

## How this field differs from others

### Compared with computer science

The computer science column draws on the [Computer science page](../computer-science/README.md).

| | Mathematics | Computer science (most areas) |
|---|---|---|
| Main publication venue | Refereed journals[^amsculture2006rates-e1] | Conferences |
| Pace | Not considered time-sensitive; publication delays are common[^amsculture2006rates-e2] | Driven by conference deadlines |
| Size of collaborations | Almost always a few people[^amsculture2004joint-e2] | Anything from one person to large teams |
| Authorship | Traditionally alphabetical[^amsculture2004joint-e3] | Figures exist only for theory: of multi-author papers in the Web of Science category "Computer Science, Theory & Methods" from 2007 to 2011, an estimated 32.6% or so used intentional alphabetical ordering[^waltman2012empirical-e2][^waltman2012empirical-e3][^waltman2012empirical-e5]; we found no sources for other areas, so do not assume alphabetical order, and ask when you join a group |
| Main evidence | Proof | Experiments and measurement (except in theory) |
| Preprints | Formal publication takes years, so you should put your preprints online[^taocareer-e28] | arXiv posting is widespread, but you must follow the conference's anonymity rules |

### Pure and applied mathematics

The difference is one of degree, with no sharp boundary. What our sources support:

- **Authorship**: more than 90% of coauthored papers in pure mathematics list authors alphabetically[^amsculture2004joint-e4]; areas of mathematics more closely tied to other disciplines may have authorship cultures mixed with those disciplines'[^amsculture2004joint-e5]. Ask about your group's authorship practice when you join.
- **Computation**: mathematics that uses computation (numerical computing, experimental mathematics, computer-assisted proofs) also has to consider whether others can reproduce the computations. The report from a 2012 workshop at ICERM (the Institute for Computational and Experimental Research in Mathematics) recommends making public all the details others need to reproduce a computation, namely the data and the code[^stodden2013setting-e1]. The report notes that computational work often does not record the code and workflow actually used[^stodden2013setting-e2]; the participants included computational scientists and mathematicians, among them pure mathematicians working in experimental mathematics and computer-assisted proof[^stodden2013setting-e3].
- **Applied mathematics often involves other disciplines**: the paper's readers, journals, and standards of evaluation may be closer to those of the partner discipline.

---

## Norms in this field

Among the sources we collected, we found no reporting standard general to mathematics (a checklist of what a paper must state) and no preregistration requirement. This section relies mainly on the **AMS Ethical Guidelines**, published by the American Mathematical Society. The guidelines describe themselves as guiding principles, not rigid rules[^ams2022ethical-e14]. The points most directly related to research:

- **Plagiarism includes the spoken word**: knowingly presenting another person's discovery as your own is plagiarism, whether written or oral, published or unpublished[^ams2022ethical-e1].
- **Cite unpublished work too**: other people's unpublished material, material on websites, and results that have only been announced must all be properly cited[^ams2022ethical-e2].
- **"I didn't know" is not grounds for claiming independent discovery**: you cannot claim to have independently discovered a widely circulated result just because you had not read it[^ams2022ethical-e6].
- **If you announce a result, publish the details promptly**: announcing before you are reasonably sure gets in the way of others working on the same problem[^ams2022ethical-e3].
- **If you find an error, correct or retract**[^ams2022ethical-e4].
- **Authorship and refereeing**: see the sections on alphabetical authorship and refereeing above.

For research that uses computation, see the recommendations of the ICERM report: important claims (for example, a computer-assisted proof of a long-standing open result) should be rigorously verified, with full computational details made public[^stodden2013setting-e4]; results of symbolic computation should ideally be cross-checked with two different software packages, because even the best software has bugs[^stodden2013setting-e5].

For general research integrity requirements, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md) in Throughout the project.

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge, chosen according to your central claim; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists the strategies in mathematics that this page's sources support. The grouping and the "What it looks like in mathematics" column are our own summary.

| Strategy | What it looks like in mathematics | Common evidence and standards | How to do it |
|---|---|---|---|
| [Proof](../../05_research-strategies/prove.md) | Proving new theorems, constructing counterexamples, improving known results. Mathematicians want not only to know that a theorem is true but also to understand its proof[^thurston1994proof-e2] | The reliability of results comes mainly from mathematicians thinking carefully and critically about the ideas[^thurston1994proof-e11]; editors accept only when reasonably confident the paper is correct[^ams2022ethical-e9]; the paper should be written so the argument is easy to check[^taowriting-e19] | [Theoretical research](../computer-science/practices/theoretical_research.md) (the parts marked as applying to all proof-based work) |
| [Proof](../../05_research-strategies/prove.md) (with computation) | Computer-assisted proofs, experimental mathematics | Important claims are rigorously verified, with full computational details made public[^stodden2013setting-e4]; symbolic computations are ideally cross-checked with two different software packages[^stodden2013setting-e5] | [Theoretical research: machine checking](../computer-science/practices/theoretical_research.md#step-4-check-your-own-proof-all-proof-based-work-the-machine-checking-part-is-computer-science) |
| [Building and improving](../../05_research-strategies/build_improve.md) | Numerical methods and models in applied mathematics | Two common kinds of evidence: analysis of an algorithm's convergence, accuracy, and stability, plus computational results showing that the method actually works (what two journals say is given after the table); the ICERM report recommends making public the data and code others need to reproduce the computations[^stodden2013setting-e1] | [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Synthesis](../../05_research-strategies/synthesize.md) | Surveys and expository writing that make the ideas of an area clear | Thurston argues that mathematicians communicate not only definitions, theorems, and proofs but also ways of thinking[^thurston1994proof-e15]; write so that mathematicians outside the topic can follow (see the AMS examples after the table); our sources do not cover more detailed standards | [Review studies](../../06_methods/review_study.md) |

How to use this table:

- **Math papers are mainly about proof.** The other rows are more common in applied and computational areas; when a paper has both theorems and numerical experiments, pick the main strategy from the central claim.
- **Whether it is "enough" depends on the target journal and your peers.** Mathematics has no common reporting checklist (see [Norms in this field](#norms-in-this-field) above); referees mainly check whether the argument is correct.
- **The building-and-improving and synthesis rows draw on the description pages of particular journals and societies** (cited from 2024 archived copies). They say only what these journals publish; they are not refereeing standards, let alone rules across mathematics. Before submitting, read your target journal's own description.

What those pages say:

- **Numerical methods.** The *SIAM Journal on Numerical Analysis* (SINUM), from the Society for Industrial and Applied Mathematics (SIAM), publishes papers that develop and analyze numerical methods, including rigorous studies of the convergence, accuracy, stability, and computational complexity of algorithms[^siamsinumabout-e1], as well as computational results that show how an algorithm performs and where it applies[^siamsinumabout-e2]. The same society's *SIAM Journal on Scientific Computing* (SISC) says in its description that its papers include computational results demonstrating the effectiveness of the proposed techniques[^siamsiscabout-e1].
- **Surveys and exposition.** The AMS *Bulletin* publishes expository articles on contemporary research, written so that mathematicians who are not experts in the topic can gain insight[^amsbullabout-e1]. The AMS also awards the Steele Prize for Mathematical Exposition for a book or a substantial survey or expository research paper[^amssteeleexposition-e1]; this shows that the society treats making an area clear as an achievement worth honoring.

---

## Research methods common in this field

Mathematics has no method pages of its own. For proving theorems and computer-assisted proofs, see [Theoretical research](../computer-science/practices/theoretical_research.md): all the parts marked as applying to all proof-based work apply, while the step on submitting to conferences and journals describes computer science practice; mathematics publishes mainly in journals[^amsculture2006rates-e1]. For numerical computing and modeling, see [Quantitative simulation](../../06_methods/simulation_study.md); a math paper may also need to prove properties of the method itself, such as convergence (whether the result gets closer to the true solution as the mesh or step size gets finer). For surveys and expository writing, see [Review studies](../../06_methods/review_study.md), though a math survey is usually the author's own account of an area and does not necessarily involve a systematic search. These two judgments are our own.

---

## Advice for newcomers

1. **Count partial results as results.** Partial progress is a key stepping stone toward solving a problem completely[^taocareer-e6]; going months without visible progress is not unusual[^taocareer-e35].
2. **Go to seminars often, including in other areas.** Thurston came to understand what a "proof" is through seminars, reading papers, and talking with fellow students[^thurston1994proof-e6]; it is worth going even if you do not understand everything[^taocareer-e33].
3. **Announce a result only when it is mature, and once you announce it, post the full paper soon.** Do not announce a result that is still only a draft[^taocareer-e30]; after announcing, publish the full details promptly[^ams2022ethical-e3].
4. **Line up an arXiv endorser before you submit.** Your first submission needs an endorsement[^arxivendorsement-e1], and your advisor is a suitable person to ask[^arxivendorsement-e2].
5. **Choose the journal to match the paper's actual level.** Sending a borderline paper to a top journal can take a long time and end in rejection[^taowriting-e17]; submit a final draft, not a first draft, or things will actually go slower[^taowriting-e21].
6. **Do not compare your publication count with other fields.** Mathematics judges quality, not speed[^amsculture2006rates-e4]. When you apply for interdisciplinary jobs or grants, you can attach the AMS statement on alphabetical authorship to explain it to reviewers.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Assuming alphabetical authorship when collaborating with people from other fields, without discussing it first | Alphabetical authorship is a mathematical tradition that people in other fields often misunderstand[^amsculture2004joint-e6]; conventions differ between fields, so agree on it in advance |
| Listing someone who only took part in discussions without a significant contribution, or leaving out someone who did contribute significantly | Every author must have made a significant contribution, and everyone who made one should be offered authorship[^ams2022ethical-e5] |
| Presenting someone else's unpublished idea in a talk without saying where it came from | Oral and unpublished material counts as plagiarism too[^ams2022ethical-e1][^ams2022ethical-e2] |
| Announcing "I proved it" in a talk or online before the proof is written up | Announcing before you are reasonably sure gets in the way of your peers[^ams2022ethical-e3] |
| Finding an error in your own published paper and saying nothing | You should correct or retract it promptly[^ams2022ethical-e4] |
| Assuming that anything published or on arXiv must be correct | arXiv moderation is not peer review[^arxivmoderation-e1]; Thurston also mentions published theorems that insiders know are false or whose proofs are incomplete[^thurston1994proof-e8] |
| Going straight for a famous hard problem | Hard problems are almost never solved out of nowhere[^taocareer-e13]; work on feasible problems first[^taocareer-e14] |
| Giving only the conclusion of a computer-assisted result, without the code and computational details | Important claims need full computational details made public[^stodden2013setting-e4] |

---

## Further reading

- **AMS 2004, Joint Research and Its Publication**: one page explaining why mathematicians list authors alphabetically. Use it when you collaborate with other fields or explain authorship to reviewers from outside mathematics.
- **AMS 2006, Rates of Publication**: one page explaining why mathematicians publish little and slowly.
- **AMS Ethical Guidelines**: the American Mathematical Society's professional guidelines; focus on sections I (research and its presentation) and IV (publications).
- **Thurston 1994, On proof and progress in mathematics**: how mathematicians actually understand, communicate, and check proofs. Good for new graduate students who want to know what mathematical research really is.
- **Terence Tao's Career advice series**: one piece of advice per page. Newcomers should start with "Talk to your advisor", "Take the initiative", "Attend talks and conferences", "Make your work available", and "Be patient".
- **ICERM 2013 report, Setting the Default to Reproducible**: for anyone doing numerical computing, experimental mathematics, or computer-assisted proofs.

[^thurston1994proof-e1]: Thurston 1994, §1. [Evidence](../../../sources/notes/thurston1994proof.md#e1)
[^thurston1994proof-e2]: Thurston 1994, §1. [Evidence](../../../sources/notes/thurston1994proof.md#e2)
[^thurston1994proof-e3]: Thurston 1994, §3. [Evidence](../../../sources/notes/thurston1994proof.md#e3)
[^thurston1994proof-e4]: Thurston 1994, §3. [Evidence](../../../sources/notes/thurston1994proof.md#e4)
[^thurston1994proof-e5]: Thurston 1994, §3. [Evidence](../../../sources/notes/thurston1994proof.md#e5)
[^thurston1994proof-e6]: Thurston 1994, §4. [Evidence](../../../sources/notes/thurston1994proof.md#e6)
[^thurston1994proof-e7]: Thurston 1994, §4. [Evidence](../../../sources/notes/thurston1994proof.md#e7)
[^thurston1994proof-e8]: Thurston 1994, §4. [Evidence](../../../sources/notes/thurston1994proof.md#e8)
[^thurston1994proof-e9]: Thurston 1994, §4. [Evidence](../../../sources/notes/thurston1994proof.md#e9)
[^thurston1994proof-e10]: Thurston 1994, §4. [Evidence](../../../sources/notes/thurston1994proof.md#e10)
[^thurston1994proof-e11]: Thurston 1994, §4. [Evidence](../../../sources/notes/thurston1994proof.md#e11)
[^thurston1994proof-e12]: Thurston 1994, §5. [Evidence](../../../sources/notes/thurston1994proof.md#e12)
[^thurston1994proof-e14]: Thurston 1994, §5. [Evidence](../../../sources/notes/thurston1994proof.md#e14)
[^thurston1994proof-e15]: Thurston 1994, §3. [Evidence](../../../sources/notes/thurston1994proof.md#e15)
[^amsculture2004joint-e1]: AMS 2004, para. 2. [Evidence](../../../sources/notes/amsculture2004joint.md#e1)
[^amsculture2004joint-e2]: AMS 2004, para. 2. [Evidence](../../../sources/notes/amsculture2004joint.md#e2)
[^amsculture2004joint-e3]: AMS 2004, para. 3. [Evidence](../../../sources/notes/amsculture2004joint.md#e3)
[^amsculture2004joint-e4]: AMS 2004, para. 3. [Evidence](../../../sources/notes/amsculture2004joint.md#e4)
[^amsculture2004joint-e5]: AMS 2004, para. 4. [Evidence](../../../sources/notes/amsculture2004joint.md#e5)
[^amsculture2004joint-e6]: AMS 2004, para. 5. [Evidence](../../../sources/notes/amsculture2004joint.md#e6)
[^amsculture2004joint-e7]: AMS 2004, para. 2. [Evidence](../../../sources/notes/amsculture2004joint.md#e7)
[^amsculture2006rates-e1]: AMS 2006, para. 2. [Evidence](../../../sources/notes/amsculture2006rates.md#e1)
[^amsculture2006rates-e2]: AMS 2006, para. 2. [Evidence](../../../sources/notes/amsculture2006rates.md#e2)
[^amsculture2006rates-e3]: AMS 2006, para. 3. [Evidence](../../../sources/notes/amsculture2006rates.md#e3)
[^amsculture2006rates-e4]: AMS 2006, para. 5. [Evidence](../../../sources/notes/amsculture2006rates.md#e4)
[^amsculture2006rates-e5]: AMS 2006, para. 4. [Evidence](../../../sources/notes/amsculture2006rates.md#e5)
[^ams2022ethical-e1]: AMS Ethical Guidelines, I. Mathematical Research and its Presentation. [Evidence](../../../sources/notes/ams2022ethical.md#e1)
[^ams2022ethical-e2]: AMS Ethical Guidelines, I. [Evidence](../../../sources/notes/ams2022ethical.md#e2)
[^ams2022ethical-e3]: AMS Ethical Guidelines, I. [Evidence](../../../sources/notes/ams2022ethical.md#e3)
[^ams2022ethical-e4]: AMS Ethical Guidelines, I. [Evidence](../../../sources/notes/ams2022ethical.md#e4)
[^ams2022ethical-e5]: AMS Ethical Guidelines, I. [Evidence](../../../sources/notes/ams2022ethical.md#e5)
[^ams2022ethical-e6]: AMS Ethical Guidelines, I. [Evidence](../../../sources/notes/ams2022ethical.md#e6)
[^ams2022ethical-e7]: AMS Ethical Guidelines, II. Social Responsibility of Mathematicians. [Evidence](../../../sources/notes/ams2022ethical.md#e7)
[^ams2022ethical-e8]: AMS Ethical Guidelines, II. [Evidence](../../../sources/notes/ams2022ethical.md#e8)
[^ams2022ethical-e9]: AMS Ethical Guidelines, IV. Publications. [Evidence](../../../sources/notes/ams2022ethical.md#e9)
[^ams2022ethical-e10]: AMS Ethical Guidelines, IV. [Evidence](../../../sources/notes/ams2022ethical.md#e10)
[^ams2022ethical-e11]: AMS Ethical Guidelines, IV. [Evidence](../../../sources/notes/ams2022ethical.md#e11)
[^ams2022ethical-e12]: AMS Ethical Guidelines, III. Education and Granting of Degrees. [Evidence](../../../sources/notes/ams2022ethical.md#e12)
[^ams2022ethical-e13]: AMS Ethical Guidelines, III. [Evidence](../../../sources/notes/ams2022ethical.md#e13)
[^ams2022ethical-e14]: AMS Ethical Guidelines, opening. [Evidence](../../../sources/notes/ams2022ethical.md#e14)
[^taocareer-e13]: Tao, Don't base career decisions on glamour or fame. [Evidence](../../../sources/notes/taocareer.md#e13)
[^taocareer-e14]: Tao, Don't prematurely obsess on a single "big problem" or "big theory". [Evidence](../../../sources/notes/taocareer.md#e14)
[^taocareer-e6]: Tao, On the importance of partial progress. [Evidence](../../../sources/notes/taocareer.md#e6)
[^taocareer-e25]: Tao, Talk to your advisor. [Evidence](../../../sources/notes/taocareer.md#e25)
[^taocareer-e27]: Tao, Take the initiative. [Evidence](../../../sources/notes/taocareer.md#e27)
[^taocareer-e28]: Tao, Make your work available. [Evidence](../../../sources/notes/taocareer.md#e28)
[^taocareer-e29]: Tao, Make your work available. [Evidence](../../../sources/notes/taocareer.md#e29)
[^taocareer-e30]: Tao, Make your work available. [Evidence](../../../sources/notes/taocareer.md#e30)
[^taocareer-e31]: Tao, Make your work available. [Evidence](../../../sources/notes/taocareer.md#e31)
[^taocareer-e32]: Tao, Attend talks and conferences, even those not directly related to your work. [Evidence](../../../sources/notes/taocareer.md#e32)
[^taocareer-e33]: Tao, Attend talks and conferences, even those not directly related to your work. [Evidence](../../../sources/notes/taocareer.md#e33)
[^taocareer-e34]: Tao, Be patient. [Evidence](../../../sources/notes/taocareer.md#e34)
[^taocareer-e35]: Tao, Be patient. [Evidence](../../../sources/notes/taocareer.md#e35)
[^taocareer-e36]: Tao, Don't be afraid to learn things outside your field. [Evidence](../../../sources/notes/taocareer.md#e36)
[^taowriting-e17]: Tao, Submit to an appropriate journal. [Evidence](../../../sources/notes/taowriting.md#e17)
[^taowriting-e18]: Tao, Submit to an appropriate journal. [Evidence](../../../sources/notes/taowriting.md#e18)
[^taowriting-e19]: Tao, Submit to an appropriate journal. [Evidence](../../../sources/notes/taowriting.md#e19)
[^taowriting-e21]: Tao, Submit a final draft, not a first draft. [Evidence](../../../sources/notes/taowriting.md#e21)
[^arxivendorsement-e1]: arXiv, The arXiv endorsement system, opening. [Evidence](../../../sources/notes/arxivendorsement.md#e1)
[^arxivendorsement-e2]: arXiv, The arXiv endorsement system. [Evidence](../../../sources/notes/arxivendorsement.md#e2)
[^arxivendorsement-e3]: arXiv, The arXiv endorsement system. [Evidence](../../../sources/notes/arxivendorsement.md#e3)
[^arxivmoderation-e1]: arXiv, Content Moderation, opening. [Evidence](../../../sources/notes/arxivmoderation.md#e1)
[^arxivmoderation-e2]: arXiv, Content Moderation, opening. [Evidence](../../../sources/notes/arxivmoderation.md#e2)
[^arxivmoderation-e3]: arXiv, Content Moderation. [Evidence](../../../sources/notes/arxivmoderation.md#e3)
[^stodden2013setting-e1]: Stodden et al. 2013 (ICERM report), Abstract. [Evidence](../../../sources/notes/stodden2013setting.md#e1)
[^siamsinumabout-e1]: SIAM, SINUM journal page (2024 snapshot). [Evidence](../../../sources/notes/siamsinumabout.md#e1)
[^siamsinumabout-e2]: SIAM, SINUM journal page (2024 snapshot). [Evidence](../../../sources/notes/siamsinumabout.md#e2)
[^siamsiscabout-e1]: SIAM, SISC journal page (2024 snapshot). [Evidence](../../../sources/notes/siamsiscabout.md#e1)
[^amsbullabout-e1]: AMS, Bulletin journal "About" page (2024 snapshot). [Evidence](../../../sources/notes/amsbullabout.md#e1)
[^amssteeleexposition-e1]: AMS, Steele Prize for Mathematical Exposition page (2024 snapshot). [Evidence](../../../sources/notes/amssteeleexposition.md#e1)
[^stodden2013setting-e2]: Stodden et al. 2013, Introduction. [Evidence](../../../sources/notes/stodden2013setting.md#e2)
[^stodden2013setting-e3]: Stodden et al. 2013, Introduction. [Evidence](../../../sources/notes/stodden2013setting.md#e3)
[^stodden2013setting-e4]: Stodden et al. 2013, Journals section. [Evidence](../../../sources/notes/stodden2013setting.md#e4)
[^stodden2013setting-e5]: Stodden et al. 2013, Appendix C. [Evidence](../../../sources/notes/stodden2013setting.md#e5)
[^waltman2012empirical-e2]: Waltman 2012, §3. [Evidence](../../../sources/notes/waltman2012empirical.md#e2)
[^waltman2012empirical-e3]: Waltman 2012, §3.2. [Evidence](../../../sources/notes/waltman2012empirical.md#e3)
[^waltman2012empirical-e5]: Waltman 2012, §3.2 Table 1. [Evidence](../../../sources/notes/waltman2012empirical.md#e5)
