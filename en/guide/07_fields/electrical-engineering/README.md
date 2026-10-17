# Electrical, electronic, and information engineering: field overview

This page explains how research actually runs in electrical engineering, electronic engineering, and information engineering (together called "EE" below): you often have to build physical hardware, you have to measure it, and you often have to plan around publications, patents, and standards. The field overlaps heavily with computing; for practices the two share, see the [Computer science page](../computer-science/README.md). For what applies in every field (choosing a topic, planning, writing, peer review, research ethics), see the chapters of each Part listed in [The research journey at a glance](../../00_start-here/research-journey.md) and [Throughout the project](../../08_throughout/README.md). For the research strategies the field commonly uses and the evidence each one relies on, see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence). This page covers only what is specific to this field.

**After reading this page, you should be able to:**

- explain how this field relates to computer science, and know which pages to consult for the overlapping areas;
- understand where tape-outs, testbeds, simulation, and measurement fit into the pace of research;
- using IEEE as the example, know what a publisher's rules say about authorship, multiple submission, turning conference papers into journal papers, and preprints;
- plan publication and patent filing so that neither costs you the other.

---

## How research works in this field

### How this field relates to computer science

The two fields have always been close. According to the overview report of Computing Curricula 2005, before the 1990s students who wanted to work on software and the theory of computing chose computer science, and those who wanted to work on hardware chose electrical engineering[^shackelford2005computing-e1]. Both sides were developing new technology, were often housed in the same college of a university, and sometimes needed each other's help[^shackelford2005computing-e2]. After the microprocessor appeared in the mid-1970s, computer engineering split off from electrical engineering as a discipline of its own[^shackelford2005computing-e3]. Computer engineering studies hardware, software, communications, and the interactions among them[^shackelford2005computing-e4]. The same report puts the difference in emphasis this way: in computer engineering the focus is software for hardware devices; in computer science, software is the medium for expressing ideas[^shackelford2005computing-e5].

The overlapping areas include hardware (chips, computer architecture), signal processing, communications and networking, and control `[Our analysis]`. If you work in these areas, much of the Computer science page applies to you too `[Our analysis]`.

### Working with physical hardware: tape-outs and testbeds

In some areas, a conclusion can only be backed up by building the real thing and measuring it `[Our analysis]`. Two examples follow.
**Chips have to be "taped out."** A tape-out means handing a finished chip design to a foundry for fabrication `[Our analysis]`. Going straight to a commercial foundry to make an application-specific integrated circuit (ASIC) for a small, specialized market can be very expensive; a **multi-project wafer** (MPW) run is one way to cut prototyping costs[^europracticempw-e1]: several designs are placed on the same wafer and fabricated together `[Our analysis]`. The process below uses Europractice, a European chip prototyping service, as the example. It is one organization's practice; service providers in other regions, foundries, and your own institution's channels may have different processes and terms, so follow the channel you actually use `[Our analysis]`. At Europractice, the process is[^europracticempw-e3]:

1. Submit the finished design.
2. It goes through electrical rule checks and design rule checks.
3. It is sent to the foundry and fabricated on a particular MPW run.
4. The prototype chips are shipped back, and the designer tests and validates them.

The prototypes Europractice ships back are generally unpackaged and untested[^europracticempw-e4], so once you have the chips, a good deal of testing is still up to you `[Our analysis]`. Also, once you choose a process technology, you need the foundry's **design kit** (design rules, electrical parameters, standard cell libraries) before you can design; at Europractice, getting it requires signing a non-disclosure agreement or a design kit license agreement first[^europracticempw-e2]. This means you may not be able to publish your complete design the way you would publish code `[Our analysis]`.

**Communications and networking experiments run on "testbeds."** A testbed is a system built from real equipment specifically for running experiments `[Our analysis]`. Writing about wireless networking research, Lamela and colleagues point out that testbeds are increasingly expensive to maintain and often underused, but their results are realistic, and they are an essential step in validating and tuning protocols[^lamela2019repeatable-e2].

The pace of this kind of work is often set by outside schedules: MPW runs start on fixed dates, and testbeds have to be booked; one failed tape-out can mean waiting for the next run to try again `[Our analysis]`. So check thoroughly before you commit, and plan backward from those dates. For general scheduling methods, see [Planning and daily routines](../../08_throughout/planning_and_routines.md) in Throughout the project.

### Simulation and measurement: you need both, and each has limits

The three points below come from the literature on wireless networking and signal processing. Other areas can learn from them, but things may not work exactly the same way there `[Our analysis]`

- **Simulation tends to be optimistic.** In wireless networking research, simulation is flexible, but modeling forces many simplifications, and the results are often optimistic[^lamela2019repeatable-e1].
- **Measurements are hard to repeat.** Real wireless experiments are affected by random factors such as noise, interference, and multipath (the signal arriving by several reflected paths that add together), so the same inputs can give very different results[^lamela2019repeatable-e3]. Vandewalle and colleagues consider physical experiments probably the hardest kind of work to reproduce; often the best you can get is statistically equivalent results[^vandewalle2009reproducible-e6].
- **What to do.** Make your measurement data reusable by others, and describe your setup (see [Common strategies and standards of evidence](#common-strategies-and-standards-of-evidence) below). Lamela and colleagues' approach is to record the experimental conditions in a real experiment and then replay them in a simulator, so the conditions can be repeated[^lamela2019repeatable-e4]. For how to verify and validate a simulation study, see [Quantitative simulation](../../06_methods/simulation_study.md).

### Publishing: with IEEE as the example, a conference paper can grow into a journal paper

IEEE (the Institute of Electrical and Electronics Engineers) describes itself as the world's largest technical professional organization[^ieeeauthorreproducibility-e5], and the rules on this page use its policies as the example. All the rules below are IEEE's own; when you submit to other publishers such as the Institution of Engineering and Technology (IET) or Elsevier, or to Chinese journals, follow their rules `[Our analysis]`. IEEE's publication policies state that "progressive publication" is common in technical publishing: early ideas appear at workshops or as preprints, more mature work at conferences, and fully mature results in journals or **Transactions** (the name of many IEEE journals)[^ieee2026pspb-e4]. IEEE supports this path, on two conditions[^ieee2026pspb-e5]:

- The journal version must fully cite the earlier conference version.
- The journal version must contain **substantial** technical content beyond the conference version.

When you submit to an IEEE journal, you must disclose your own similar papers that are published or under review elsewhere (a conference paper, for example) and explain how the new manuscript differs from them[^ieeeauthorsubmission-e1]. This is not quite the same as in most areas of computing, where a paper at a top conference counts as a finished publication (see the [Computer science page](../computer-science/README.md#conferences-are-the-main-publication-venue)), so check what your target journal requires before you submit `[Our analysis]`. A few more IEEE rules that are easy to trip over:

- **Multiple submission** means the same paper is under review at two or more publications at once; each IEEE organizational unit decides for itself whether to allow it[^ieeeauthorsubmission-e2], so check the rules of the specific journal or conference.
- **Someone has to present a conference paper.** IEEE may exclude a paper that was not presented from IEEE Xplore (IEEE's digital library)[^ieee2026pspb-e13].
- **Preprints are allowed.** IEEE does not treat a preprint on arXiv, TechRxiv (an engineering and technology preprint server run by IEEE)[^ieee2026pspb-e15], or another nonprofit preprint server IEEE approves as "published"[^ieeeauthorposting-e1]. After acceptance, you must replace the public version with a full citation including the DOI (Digital Object Identifier, a permanent link), or with the accepted manuscript including the DOI[^ieeeauthorposting-e2]; for papers that are not open access, you may not post IEEE's typeset final version yourself[^ieeeauthorposting-e3]. Note: the moment you upload a preprint, it counts as a public disclosure for patent purposes; see "Publish or patent" below.

### Authorship: building the prototype counts

IEEE's authorship criteria have three parts, and all three must be met[^ieee2026pspb-e6][^ieee2026pspb-e7]:

1. A significant intellectual contribution to at least one of theoretical development, system or experimental design, **prototype development**, or data analysis.
2. Drafting the paper or revising it for content.
3. Approving the final accepted version.

Prototype development is written explicitly into the first criterion[^ieee2026pspb-e6]. In other words, the person who built the hardware and ran the tests should be an author, as long as the other two criteria are also met `[Our analysis]`. IEEE does not set author order; the authors decide it among themselves[^ieee2026pspb-e8]. For general principles of authorship and how to agree on order early, see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md#5-authorship-citation-and-conflicts-of-interest-give-every-contributor-due-credit) in Throughout the project.

---

## How this field differs from computer science

The table below is our own summary, meant to help you spot the differences quickly; it is not a strict division between fields `[Our analysis]`.

| | EE | Computing |
|---|---|---|
| Where results come from | Theoretical derivation and simulation, plus measurements on physical hardware (chips, circuits, testbeds) | Mainly experiments on code, systems, and data |
| What sets the schedule | Also outside schedules such as tape-out runs and testbed bookings | Mainly conference deadlines |
| Publication path | IEEE explicitly supports "conference version → journal version," with substantial new content in the journal version[^ieee2026pspb-e5] | Top conferences dominate in most areas (see the [Computer science page](../computer-science/README.md#conferences-are-the-main-publication-venue)) |
| How much you can make public | Chip design kits usually require a confidentiality or license agreement (the Europractice example[^europracticempw-e2]); industry-funded projects may not allow code to be released[^vandewalle2009reproducible-e9] | Experimental areas have a tradition of releasing artifacts (code, data) (see the [Computer science page](../computer-science/README.md#artifact-evaluation-and-badges)) |
| Patents | You may need to consider a patent before publishing (see below) | Not covered on the Computer science page |
| Standards | Some research in areas such as communications relates to the work of standards bodies such as IEEE and 3GPP (see below) | Not covered on the Computer science page |

---

## Norms and reporting standards in this field

### The IEEE Code of Ethics and publication policies

IEEE's publications operations manual includes the full text of the IEEE Code of Ethics. Two of its points matter most for research in this field `[Our analysis]`:

- **Public safety comes first.** Promptly disclose factors that could endanger the public or the environment[^ieee2026pspb-e1]. Keep this in mind especially if you work on power systems, medical electronics, or automotive electronics `[Our analysis]`.
- **Disclose conflicts of interest**[^ieee2026pspb-e2]; papers must state funding sources and potential conflicts of interest[^ieee2026pspb-e10].

A few IEEE publication rules worth remembering on their own:

- If a new manuscript builds on your own earlier work (including conference papers), cite the earlier work and briefly explain what the new contribution is[^ieee2026pspb-e12].
- IEEE cannot publish sensitive information subject to export controls, such as military or defense information; general scientific, mathematical, and engineering principles commonly taught in universities, and information already in the public domain, are exempt[^ieeeauthorsubmission-e3].

The rest are integrity requirements common to all fields. For example, IEEE counts using someone else's words, ideas, processes, results, or algorithms without credit as plagiarism[^ieee2026pspb-e11]; see [Research integrity and ethics](../../08_throughout/integrity_and_ethics.md).

### Reproducibility: the debate in signal processing

In a 2009 article in *IEEE Signal Processing Magazine*, Vandewalle and colleagues defined "reproducible" this way: all information relevant to the work (text, data, code, and so on) is made available, so that an independent researcher can reproduce the results[^vandewalle2009reproducible-e2]. They examined all 134 papers published in *IEEE Transactions on Image Processing* in 2004: only 9% made their code available, and 33% their data[^vandewalle2009reproducible-e3]. They identified several problems:

- Algorithm papers often omit the exact dataset, the initialization and stopping criteria, and the precise parameter values[^vandewalle2009reproducible-e1].
- Common test images exist online in several versions, and readers cannot tell which one a paper used[^vandewalle2009reproducible-e4].
- Even the authors themselves could not reproduce their work: there were several versions of the code on the hard drive, and nobody knew which one produced the final figures[^vandewalle2009reproducible-e5].

Their own practice is worth copying: write one script for each figure and each table that regenerates it when run[^vandewalle2009reproducible-e13]; and state the platform you tested on, even if the code is in principle platform-independent[^vandewalle2009reproducible-e8]. The first time, cleaning up after the fact took about a week; later, when they planned for reproducibility from the start, the same work took about a day[^vandewalle2009reproducible-e11].

What IEEE does now:

- It encourages (but does not require) all authors to share data and code[^ieeeauthorreproducibility-e1]; data can go in public repositories such as figshare, Zenodo, or Dryad[^ieeeauthorreproducibility-e2].
- It recommends Code Ocean (a platform for storing and running code in the cloud)[^ieeeauthorreproducibility-e3]; authors who have published with IEEE in the past five years can link their code to their paper's page on IEEE Xplore[^ieeeauthorreproducibility-e4].
- The *IEEE Open Journal of Signal Processing* (OJSP) is piloting a **reproducibility review**[^ojspreproducibility-e2]: after a paper is conditionally accepted[^ojspreproducibility-e3], a reviewer actually runs the authors' code on Code Ocean and checks the computational results[^ojspreproducibility-e1]. The review is a good-faith check, not a hunt for edge cases that break the code[^ojspreproducibility-e4]. OJSP explains why it does not rely on GitHub alone: with only the source code, other people often spend a lot of time setting up the environment before they can run it[^ojspreproducibility-e5]. This is one journal's pilot, not an IEEE-wide requirement `[Our analysis]`.

**Watch the terminology.** In discussions of reproducibility, different communities use "reproduce" and "replicate" in exactly opposite ways[^barba2018terminologies-e2]. The signal processing literature mostly follows the usage of Vandewalle and colleagues above: "reproduce" means getting the results again using the authors' published data and code[^vandewalle2009reproducible-e2]; Barba's classification table also puts signal processing in the camp of Claerbout, Donoho, and Peng[^barba2018terminologies-e3]. For the usage in computing (the Association for Computing Machinery, ACM) and how it changed, see [Replication studies: first, get the terms straight](../../06_methods/replication.md#first-get-the-terms-straight). When you read the literature, first check how the authors define these two words.

### Publish or patent (the US as the example)

If your results have practical value, think about patents before you publish `[Our analysis]`. All the rules below come from guidance published by the technology transfer offices (the units that handle a university's patents and commercialization) of several US universities (Rutgers, Berkeley, and Utah), and reflect US law and those universities' policies. **Patent law in China and other countries, and the policies of your own institution, may differ; follow your institution's guidance.**

**What counts as "public disclosure" (as US universities describe it).** Describing the invention to the public, without confidentiality and in enough detail that a person of ordinary skill in the field could make it without undue experimentation, counts as public disclosure[^rutgersinventionfaq-e4]. Some cases that are easy to overlook:

- A conference talk itself and a published abstract both count[^utahprotecting-e3]; even with no handouts, it counts if someone in the audience takes notes[^rutgersinventionfaq-e5].
- A preprint counts the moment it is uploaded[^utahprotecting-e2].
- A journal article counts only from formal publication; submission and confidential peer review do not count[^utahprotecting-e1].
- In the US, a thesis or dissertation defense legally counts as public disclosure, even if only people from the university attend[^utahprotecting-e4].

**What happens after disclosure.** According to Berkeley, once you disclose, you have only one year left to file in the US, and in most countries outside the US you lose the right to file altogether[^berkeleydisclose-e4]. Rutgers says the same: if you disclose before reporting the invention to the university, you cannot get patent rights outside the US, and if no application is filed within a year, you may lose US patent rights as well[^rutgersinventionfaq-e1][^rutgersinventionfaq-e2]. The US "one-year grace period" you often read about online does not take international patent law and other factors into account, so you cannot rely on it[^berkeleydisclose-e3].

**How to do both.** Berkeley recommends submitting an invention disclosure to the university at least 1 to 2 months before any public disclosure, if possible[^berkeleydisclose-e2]. A US provisional application can be filed within days, even using the manuscript or slides as they are, to secure a priority date[^utahprotecting-e5]. Rutgers explicitly promises that, given advance notice, it will work on a patent application without delaying publication, and it will never stop researchers from publishing[^rutgersinventionfaq-e3].

**Working with industry.** Berkeley requires an invention disclosure to the university before the collaboration starts[^berkeleydisclose-e1]. Vandewalle and colleagues also note that companies often file patents before publishing, and companies funding research may not want code released[^vandewalle2009reproducible-e9]. In that case, at least make your work reproducible internally, so that your colleagues can reproduce your results[^vandewalle2009reproducible-e10].

### Standards bodies

Some research in areas such as communications involves standards, for example comparing against a standardized scheme or submitting proposals to a standard `[Our analysis]`. The IEEE Standards Association holds that standards support interoperability, that is, they let different devices work together[^ieeesadevelop-e1]. Two examples:

- **IEEE Standards Association (IEEE SA)**: standards are developed through a fixed six-stage process[^ieeesadevelop-e2] that relies on voluntary collaboration among the parties involved[^ieeesadevelop-e3]. It has a dedicated patent committee responsible for patent policy related to standards[^ieeesadevelop-e4].
- **3GPP (3rd Generation Partnership Project)**: founded in 1998, originally to develop 3G mobile standards[^3gpp2026about-e2]; its specifications now cover cellular radio access, the core network, and service capabilities[^3gpp2026about-e1].

If your research relates to a standard, first read and understand the relevant parts of the standard, and ask your advisor and collaborators what arrangements apply on patents and confidentiality `[Our analysis]`.

---

## Common strategies and standards of evidence

A **research strategy** is the main logic by which a project produces new knowledge; see [Key concepts](../../00_start-here/key-concepts.md#research-strategy) and [Research strategies](../../05_research-strategies/README.md). The table below lists the four strategies this page's sources support; our sources do not cover the other strategies. The grouping and the second column are our own summary, and each standard represents only the areas in its footnotes (mostly wireless networking and signal processing) `[Our analysis]`.

| Strategy | What it looks like in this field | Common evidence and standards | How to do it |
|---|---|---|---|
| [Building and improving](../../05_research-strategies/build_improve.md) | Propose and evaluate a new circuit, chip, algorithm, or communication system | In wireless networking research, simulation makes many simplifications for modeling, so results are often optimistic[^lamela2019repeatable-e1]; testbed results are realistic and an essential step in validating and tuning protocols[^lamela2019repeatable-e2]; prototype chips are tested and validated by the designer after they are shipped back[^europracticempw-e3] | [Engineering research](../computer-science/practices/engineering_research.md) (Computer science page), [Quantitative simulation](../../06_methods/simulation_study.md) |
| [Comparative evaluation](../../05_research-strategies/compare_evaluate.md) | Compare several algorithms or schemes under the same conditions | State the exact dataset, initialization and stopping criteria, and parameter values[^vandewalle2009reproducible-e1]; common test images exist online in several versions, so say which one you used[^vandewalle2009reproducible-e4]; state the platform you tested on[^vandewalle2009reproducible-e8] | [Benchmarking](../computer-science/practices/benchmarking.md) (Computer science page) |
| [Description](../../05_research-strategies/observe_describe.md) | Measure the characteristics of a channel, device, or system in a real environment | Wireless experiments are affected by noise, interference, and multipath, so the same inputs can give very different results[^lamela2019repeatable-e3]; physical experiments are hard to reproduce fully, so make the measurement data reusable by others[^vandewalle2009reproducible-e6] and describe the setup and measurement equipment in detail[^vandewalle2009reproducible-e7] | [Experimental measurement](../../06_methods/experimental_measurement.md) |
| [Proof](../../05_research-strategies/prove.md) | Derive performance bounds, prove properties of algorithms | Signal processing sits between theory and experiment; theorems are often accompanied by numerical simulations that help with understanding[^vandewalle2009reproducible-e12] | [Theoretical research](../computer-science/practices/theoretical_research.md) (Computer science page) |

How to use this table `[Our analysis]`: first choose the main strategy based on your central claim. For example, if you propose a new circuit and also derive its performance bounds, the derivation is held to the standards for proof. For areas that overlap with computing, also see [the section of the same name on the Computer science page](../computer-science/README.md#common-strategies-and-standards-of-evidence).

## Research methods common in this field

This field has no method pages of its own; it uses the cross-field methods in [Research types](../../06_methods/README.md) and the practices on the Computer science page:

- [Experimental measurement](../../06_methods/experimental_measurement.md) and [Quantitative simulation](../../06_methods/simulation_study.md): you need both; see [Simulation and measurement](#simulation-and-measurement-you-need-both-and-each-has-limits) above.
- [Engineering research](../computer-science/practices/engineering_research.md), [Benchmarking](../computer-science/practices/benchmarking.md), [Theoretical research](../computer-science/practices/theoretical_research.md), and [Optimization studies](../computer-science/practices/optimization_study.md) (Computer science page): evaluating a new circuit or system may require measurements on a prototype, not just simulation; problems such as resource allocation and choosing circuit parameters can be modeled as optimization problems `[Our analysis]`.
- [Replication studies](../../06_methods/replication.md): watch how "reproduce" and "replicate" are used; see [Reproducibility](#reproducibility-the-debate-in-signal-processing) above.

---

## Advice for newcomers

1. **From day one, write a script that generates each figure.** Once Vandewalle and colleagues planned for reproducibility from the start, the cleanup work shrank from about a week to about a day[^vandewalle2009reproducible-e11]. For general practice, see [Organizing your research materials](../../08_throughout/organizing_materials.md).
2. **Do both simulation and measurement, and explain the gap between them** (for why, see [Simulation and measurement](#simulation-and-measurement-you-need-both-and-each-has-limits) above).
3. **For tape-outs and testbed experiments, plan backward from the outside schedule.** Check thoroughly before you submit; if something goes wrong, you may have to wait for the next run `[Our analysis]`.
4. **Think about patents before you write the paper.** Before you submit, present, or post a preprint, ask your advisor whether the results should be patented; if so, contact your institution's patent office as early as possible (Berkeley recommends at least 1 to 2 months before public disclosure[^berkeleydisclose-e2]).
5. **When turning a conference paper into a journal paper, genuinely extend it.** When you submit to an IEEE journal, cite the conference version and say clearly what is new[^ieee2026pspb-e5][^ieeeauthorsubmission-e1].
6. **Before signing a non-disclosure agreement, find out what you will be allowed to publish.** Design kits, company data, and code from collaborations may all be restricted[^europracticempw-e2][^vandewalle2009reproducible-e9]; publish whatever you can (measurement data, simulation code) `[Our analysis]`.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Claiming a scheme works in real systems on the strength of simulation results alone | In wireless networking research, simulation tends to be optimistic because of its simplifications[^lamela2019repeatable-e1] |
| Reporting a single measurement run without describing the setup and conditions | Wireless experiments are affected by random factors, so the same inputs can give very different results[^lamela2019repeatable-e3] |
| Leaving exact parameters, data versions, and the test platform out of the paper | Others cannot reproduce the work, and after a while neither can you[^vandewalle2009reproducible-e1][^vandewalle2009reproducible-e5] |
| Lightly revising a conference paper and submitting it to an IEEE journal without citing the conference version | IEEE requires the journal version to add substantial new content and cite the earlier work[^ieee2026pspb-e5] |
| Assuming multiple submission is always allowed, or always forbidden | At IEEE, each organizational unit decides for itself; check the specific journal's rules[^ieeeauthorsubmission-e2] |
| Nobody goes to present an accepted IEEE conference paper | IEEE may leave it out of IEEE Xplore[^ieee2026pspb-e13] |
| Presenting at a conference or posting a preprint first, and only then thinking about a patent | According to US university guidance, you have already lost the right to file in most countries outside the US[^berkeleydisclose-e4] |
| Listing only the people who did the theory and wrote the paper as authors, and leaving out those who built and tested the prototype | IEEE lists prototype development as a contribution that can qualify someone for authorship[^ieee2026pspb-e6] |

---

## Further reading

- **IEEE Publication Services and Products Board (PSPB) Operations Manual**: the source document for IEEE's publication rules, including the full IEEE Code of Ethics. Focus on §8.1.7.F (conference papers into journal papers) and §8.2.1 (authorship and author responsibilities). Read it before you submit to IEEE.
- **The publication ethics pages of the IEEE Author Center**: practical guidance on multiple submission, preprints, copyright, and reproducibility.
- **Vandewalle, Kovačević, and Vetterli 2009, Reproducible Research in Signal Processing**: why and how to do reproducible research, including the authors' own failures. Good for anyone just starting on simulations and algorithms.
- **Barba 2018, Terminologies for Reproducible Research**: sorts out how different fields use "reproduce" and "replicate." Read it before you read the literature on replication.
- **Guidance from your own institution's technology transfer or patent office**: this page cites pages from several US universities; laws differ by country and policies differ by institution, so follow your institution's guidance.

[^shackelford2005computing-e1]: Shackelford et al. 2005 (Computing Curricula 2005 overview report), §2.2.1, p. 9. [Evidence](../../../sources/notes/shackelford2005computing.md#e1)
[^shackelford2005computing-e2]: Shackelford et al. 2005, §2.2.1, p. 10. [Evidence](../../../sources/notes/shackelford2005computing.md#e2)
[^shackelford2005computing-e3]: Shackelford et al. 2005, §2.2.1, p. 10. [Evidence](../../../sources/notes/shackelford2005computing.md#e3)
[^shackelford2005computing-e4]: Shackelford et al. 2005, §2.3.1, p. 13. [Evidence](../../../sources/notes/shackelford2005computing.md#e4)
[^shackelford2005computing-e5]: Shackelford et al. 2005, §2.2.3, p. 12. [Evidence](../../../sources/notes/shackelford2005computing.md#e5)
[^europracticempw-e1]: Europractice, MPW Prototyping, top of page. [Evidence](../../../sources/notes/europracticempw.md#e1)
[^europracticempw-e2]: Europractice, MPW Prototyping, Selecting and Accessing Technology. [Evidence](../../../sources/notes/europracticempw.md#e2)
[^europracticempw-e3]: Europractice, MPW Prototyping, Fabricating and Packaging Prototypes. [Evidence](../../../sources/notes/europracticempw.md#e3)
[^europracticempw-e4]: Europractice, MPW Prototyping, Fabricating and Packaging Prototypes. [Evidence](../../../sources/notes/europracticempw.md#e4)
[^lamela2019repeatable-e1]: Lamela et al. 2019, I. Introduction. [Evidence](../../../sources/notes/lamela2019repeatable.md#e1)
[^lamela2019repeatable-e2]: Lamela et al. 2019, I. Introduction. [Evidence](../../../sources/notes/lamela2019repeatable.md#e2)
[^lamela2019repeatable-e3]: Lamela et al. 2019, I. Introduction. [Evidence](../../../sources/notes/lamela2019repeatable.md#e3)
[^lamela2019repeatable-e4]: Lamela et al. 2019, III. Trace-based Simulation Approach. [Evidence](../../../sources/notes/lamela2019repeatable.md#e4)
[^vandewalle2009reproducible-e1]: Vandewalle et al. 2009, opening, p. 37. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e1)
[^vandewalle2009reproducible-e2]: Vandewalle et al. 2009, When is research reproducible, p. 39. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e2)
[^vandewalle2009reproducible-e3]: Vandewalle et al. 2009, Reproducible research study, p. 40. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e3)
[^vandewalle2009reproducible-e4]: Vandewalle et al. 2009, Failures of reproducibility, p. 41. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e4)
[^vandewalle2009reproducible-e5]: Vandewalle et al. 2009, Failures of reproducibility, p. 41. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e5)
[^vandewalle2009reproducible-e6]: Vandewalle et al. 2009, Experiments, pp. 41–42. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e6)
[^vandewalle2009reproducible-e7]: Vandewalle et al. 2009, Experiments, p. 42. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e7)
[^vandewalle2009reproducible-e8]: Vandewalle et al. 2009, Algorithms, p. 41. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e8)
[^vandewalle2009reproducible-e9]: Vandewalle et al. 2009, Implementation and issues, p. 43. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e9)
[^vandewalle2009reproducible-e10]: Vandewalle et al. 2009, Implementation and issues, p. 43. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e10)
[^vandewalle2009reproducible-e11]: Vandewalle et al. 2009, Case study: super-resolution, p. 42. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e11)
[^vandewalle2009reproducible-e12]: Vandewalle et al. 2009, Components and Theory, p. 41. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e12)
[^vandewalle2009reproducible-e13]: Vandewalle et al. 2009, Case study: super-resolution, p. 42. [Evidence](../../../sources/notes/vandewalle2009reproducible.md#e13)
[^ieee2026pspb-e1]: IEEE PSPB Operations Manual 2026, §2.7 (IEEE Code of Ethics, item 1). [Evidence](../../../sources/notes/ieee2026pspb.md#e1)
[^ieee2026pspb-e2]: IEEE PSPB Operations Manual 2026, §2.7 (IEEE Code of Ethics, item 3). [Evidence](../../../sources/notes/ieee2026pspb.md#e2)
[^ieee2026pspb-e4]: IEEE PSPB Operations Manual 2026, §8.1.7.F. [Evidence](../../../sources/notes/ieee2026pspb.md#e4)
[^ieee2026pspb-e5]: IEEE PSPB Operations Manual 2026, §8.1.7.F. [Evidence](../../../sources/notes/ieee2026pspb.md#e5)
[^ieee2026pspb-e6]: IEEE PSPB Operations Manual 2026, §8.2.1.A.1. [Evidence](../../../sources/notes/ieee2026pspb.md#e6)
[^ieee2026pspb-e7]: IEEE PSPB Operations Manual 2026, §8.2.1.A.1. [Evidence](../../../sources/notes/ieee2026pspb.md#e7)
[^ieee2026pspb-e8]: IEEE PSPB Operations Manual 2026, §8.2.1.A.2. [Evidence](../../../sources/notes/ieee2026pspb.md#e8)
[^ieee2026pspb-e10]: IEEE PSPB Operations Manual 2026, §8.2.1.B.2. [Evidence](../../../sources/notes/ieee2026pspb.md#e10)
[^ieee2026pspb-e11]: IEEE PSPB Operations Manual 2026, §8.2.1.B.9. [Evidence](../../../sources/notes/ieee2026pspb.md#e11)
[^ieee2026pspb-e12]: IEEE PSPB Operations Manual 2026, §8.2.1.B.12. [Evidence](../../../sources/notes/ieee2026pspb.md#e12)
[^ieee2026pspb-e13]: IEEE PSPB Operations Manual 2026, §8.2.1.B.16. [Evidence](../../../sources/notes/ieee2026pspb.md#e13)
[^ieee2026pspb-e15]: IEEE PSPB Operations Manual 2026, §4.3.7. [Evidence](../../../sources/notes/ieee2026pspb.md#e15)
[^ieeeauthorsubmission-e1]: IEEE Author Center, Submission and Peer Review Policies, Multiple Submission and Prior Publication. [Evidence](../../../sources/notes/ieeeauthorsubmission.md#e1)
[^ieeeauthorsubmission-e2]: IEEE Author Center, Submission and Peer Review Policies, Multiple Submission and Prior Publication. [Evidence](../../../sources/notes/ieeeauthorsubmission.md#e2)
[^ieeeauthorsubmission-e3]: IEEE Author Center, Submission and Peer Review Policies, export control section. [Evidence](../../../sources/notes/ieeeauthorsubmission.md#e3)
[^ieeeauthorposting-e1]: IEEE Author Center, Post-Publication Policies, Preprint. [Evidence](../../../sources/notes/ieeeauthorposting.md#e1)
[^ieeeauthorposting-e2]: IEEE Author Center, Post-Publication Policies, Author-submitted article. [Evidence](../../../sources/notes/ieeeauthorposting.md#e2)
[^ieeeauthorposting-e3]: IEEE Author Center, Post-Publication Policies, Published article. [Evidence](../../../sources/notes/ieeeauthorposting.md#e3)
[^ieeeauthorreproducibility-e1]: IEEE Author Center, Research Reproducibility, IEEE Open Research Statement. [Evidence](../../../sources/notes/ieeeauthorreproducibility.md#e1)
[^ieeeauthorreproducibility-e2]: IEEE Author Center, Research Reproducibility, Sharing Data. [Evidence](../../../sources/notes/ieeeauthorreproducibility.md#e2)
[^ieeeauthorreproducibility-e3]: IEEE Author Center, Research Reproducibility, Uploading Code. [Evidence](../../../sources/notes/ieeeauthorreproducibility.md#e3)
[^ieeeauthorreproducibility-e4]: IEEE Author Center, Research Reproducibility, Uploading Code. [Evidence](../../../sources/notes/ieeeauthorreproducibility.md#e4)
[^ieeeauthorreproducibility-e5]: IEEE Author Center, footer. [Evidence](../../../sources/notes/ieeeauthorreproducibility.md#e5)
[^ojspreproducibility-e1]: IEEE Signal Processing Society, OJSP (Open Journal of Signal Processing) reproducibility review: instructions for authors, main text, para. 1. [Evidence](../../../sources/notes/ojspreproducibility.md#e1)
[^ojspreproducibility-e2]: IEEE Signal Processing Society, OJSP (Open Journal of Signal Processing) reproducibility review: instructions for authors, main text, para. 1. [Evidence](../../../sources/notes/ojspreproducibility.md#e2)
[^ojspreproducibility-e3]: IEEE Signal Processing Society, OJSP (Open Journal of Signal Processing) reproducibility review: instructions for authors, note on submission timing. [Evidence](../../../sources/notes/ojspreproducibility.md#e3)
[^ojspreproducibility-e4]: IEEE Signal Processing Society, OJSP (Open Journal of Signal Processing) reproducibility review: instructions for authors, FAQ. [Evidence](../../../sources/notes/ojspreproducibility.md#e4)
[^ojspreproducibility-e5]: IEEE Signal Processing Society, OJSP (Open Journal of Signal Processing) reproducibility review: instructions for authors, FAQ. [Evidence](../../../sources/notes/ojspreproducibility.md#e5)
[^barba2018terminologies-e2]: Barba 2018, Introduction. [Evidence](../../../sources/notes/barba2018terminologies.md#e2)
[^barba2018terminologies-e3]: Barba 2018, explanation of the decision tree; Conclusions, Table 2. [Evidence](../../../sources/notes/barba2018terminologies.md#e3)
[^rutgersinventionfaq-e1]: Rutgers technology transfer FAQ, When should I submit an invention disclosure? [Evidence](../../../sources/notes/rutgersinventionfaq.md#e1)
[^rutgersinventionfaq-e2]: Rutgers technology transfer FAQ, When should I submit an invention disclosure? [Evidence](../../../sources/notes/rutgersinventionfaq.md#e2)
[^rutgersinventionfaq-e3]: Rutgers technology transfer FAQ, What if I want to publish my results? [Evidence](../../../sources/notes/rutgersinventionfaq.md#e3)
[^rutgersinventionfaq-e4]: Rutgers technology transfer FAQ, What constitutes a public disclosure? [Evidence](../../../sources/notes/rutgersinventionfaq.md#e4)
[^rutgersinventionfaq-e5]: Rutgers technology transfer FAQ, Oral disclosures. [Evidence](../../../sources/notes/rutgersinventionfaq.md#e5)
[^berkeleydisclose-e1]: UC Berkeley IPIRA, When to Disclose an Invention to OTL. [Evidence](../../../sources/notes/berkeleydisclose.md#e1)
[^berkeleydisclose-e2]: UC Berkeley IPIRA, When to Disclose an Invention to OTL. [Evidence](../../../sources/notes/berkeleydisclose.md#e2)
[^berkeleydisclose-e3]: UC Berkeley IPIRA, FAQ (grace period). [Evidence](../../../sources/notes/berkeleydisclose.md#e3)
[^berkeleydisclose-e4]: UC Berkeley IPIRA, FAQ (consequences of early disclosure). [Evidence](../../../sources/notes/berkeleydisclose.md#e4)
[^utahprotecting-e1]: University of Utah TLO, Protecting Your Research, Journal publications. [Evidence](../../../sources/notes/utahprotecting.md#e1)
[^utahprotecting-e2]: University of Utah TLO, Protecting Your Research, Online preprint servers. [Evidence](../../../sources/notes/utahprotecting.md#e2)
[^utahprotecting-e3]: University of Utah TLO, Protecting Your Research, Conference presentations. [Evidence](../../../sources/notes/utahprotecting.md#e3)
[^utahprotecting-e4]: University of Utah TLO, Protecting Your Research, Thesis and dissertation defenses. [Evidence](../../../sources/notes/utahprotecting.md#e4)
[^utahprotecting-e5]: University of Utah TLO, Protecting Your Research, Provisional applications. [Evidence](../../../sources/notes/utahprotecting.md#e5)
[^ieeesadevelop-e1]: IEEE SA, Develop Standards, top of page. [Evidence](../../../sources/notes/ieeesadevelop.md#e1)
[^ieeesadevelop-e2]: IEEE SA, Develop Standards, top of page. [Evidence](../../../sources/notes/ieeesadevelop.md#e2)
[^ieeesadevelop-e3]: IEEE SA, Develop Standards, Our Principles. [Evidence](../../../sources/notes/ieeesadevelop.md#e3)
[^ieeesadevelop-e4]: IEEE SA, Develop Standards, Standards Board Committees. [Evidence](../../../sources/notes/ieeesadevelop.md#e4)
[^3gpp2026about-e1]: 3GPP, About 3GPP, top of the page. [Evidence](../../../sources/notes/3gpp2026about.md#e1)
[^3gpp2026about-e2]: 3GPP, About 3GPP, History section. [Evidence](../../../sources/notes/3gpp2026about.md#e2)
