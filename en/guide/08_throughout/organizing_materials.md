# Organizing your research materials: data, code, results, and notes

> The reasoning on this page applies to every field; the examples and concrete steps come from computer science.

## When you need this page

- **On the first day of a project:** setting up the folders and the rules now is far less work than fixing things later.
- **When results start piling up:** you can no longer say which experiment produced `result_v3_new.csv`.
- **When you come back to a project after a few weeks, need to find a number for the paper, or your advisor asks "where did this result come from?":** if you can't answer, use this page to catch up.

Organizing has one goal: **someone unfamiliar with the project can look at your files and understand in detail what you did and why.** Most often, that someone is you[^noble2009quick-e1]. As the joke goes, "yourself from 3 months ago doesn't answer email"[^wilson2017good-e5].

Why it is worth the effort: everything you do, you will probably have to do over again[^noble2009quick-e2]. Finding a problem in the data, getting new data, or a reviewer asking for another experiment all mean rerunning things. If your materials are well organized, redoing the work is a few commands; if they are a mess, it is archaeology. `[Our analysis]`

A note on scope first: most of the sources cited here are written for researchers who do computational work. Wilson and colleagues describe "good enough" practices for scientific computing[^wilson2017good-e1], Schnell's notebook rules are for biologists who do purely computational work[^schnell2015ten-e8], and Noble's examples come from computational biology. The principles (raw data stays read-only, every result can be traced, the log is kept by date) carry over to questionnaires, interviews, and lab work; adapt the specifics, such as folder names and git, to your field. `[Our analysis]`

This page covers only the practical how-to. For why you should record, keep, and share materials (the integrity angle), see [Research integrity and ethics](integrity_and_ethics.md); for what makes a conclusion credible, see [Validity and limitations](../02_do-the-project/04_validity-and-limits.md).

---

## 1. One project, one folder, set up on day one

**How:**

- Put all of a project's files under a single root folder named after the project[^wilson2017good-e6][^noble2009quick-e3].
- How to divide work into projects: by how much the data and code overlap[^wilson2017good-e6]. In academia a project tends to map naturally onto a paper, so "one project = one paper = one folder = one git repository" is a good default[^mineault2021good-e1] (a version control system records every change to your files; git is one such tool; see Section 4).
- Code or tools shared by several papers get their own project[^noble2009quick-e3][^mineault2021good-e2].
- Text documents (paper drafts, code documentation, an electronic lab notebook) go in `doc/`, raw data in `data/`, and files generated during cleaning and analysis in `results/`[^wilson2017good-e7][^wilson2017good-e8]. Keep data, methods, and outputs clearly separated[^turingwaycompendia-e3].

Here is a starting point you can copy `[Our analysis, combining the sources in this section and Sections 2, 5, and 6]`. It is not a standard; cut and change it to fit your project. A project with no code can skip `src/`.

```
llm-contract-vuln/
├── README.md          what the project is, where it stands, how to reproduce it, what each folder holds
├── data/
│   ├── raw/           raw data, read-only; with a README giving source and date obtained
│   └── processed/     generated from raw by scripts; can be deleted and rebuilt
├── src/               your own code and analysis scripts
├── results/
│   ├── 2026-10-05_reentrancy-prompt-comparison/   experiment output from the exploratory phase, stored by date
│   └── paper/         figures and tables going into the paper, plus the scripts that make them
├── notes/
│   ├── status.md      current status: always up to date
│   ├── log.md         research log: appended by date
│   └── findings.md    settled conclusions: findings, decisions, limitations
├── doc/               paper drafts, one-page project summary, reports
└── requirements.txt   computing environment: software used and versions
```

A collection of all the digital parts of a project (data, code, texts) kept together is called a research compendium[^turingwaycompendia-e1]. Its main purpose is to let all parts of the project be published together, so a basic folder structure that keeps them together can be enough[^turingwaycompendia-e2].

**Where people go wrong:** Waiting until "the project settles down" to organize. Projects never settle down, and the longer you wait, the more you have to fix. `[Our analysis]`

**Write it down:** Set up this folder structure for your current project, and move in the materials scattered across your downloads folder, your desktop, and your chat history.

## 2. Raw data is read-only; everything else can be regenerated

**How:**

- **Keep raw data separate and never modify it.** Inside the data folder, make separate subfolders for raw data, derived data, and data summaries[^osforganizing-e2].
- **Make it read-only.** That makes it hard to damage by accident, or to hand-edit in a moment of weakness[^wilson2017good-e9][^osforganizing-e3]. Don't do calculations, sums, or charts inside the raw data file[^osforganizing-e3].
- **Back it up in at least two places**[^wilson2017good-e10].
- **Derived data must be regenerable from the raw data and code.** If it is, intermediate files don't need to go under version control[^wilson2017good-e17].
- **Record where the data came from.** In the data folder's README, write who obtained the data, from where, and on what date[^noble2009quick-e10]. If the data comes from a public database too large to keep a local copy, record the exact steps used to get it, plus the official version number or the download date[^wilson2017good-e21].
- **If manual processing truly can't be avoided**, at least record which files you changed or moved, and why[^sandve2013ten-e10].

**Why:** It is tempting to overwrite raw data with a cleaned-up version, but only by keeping the raw data exactly as it was can you rerun the analysis from start to finish, recover from mistakes, and experiment without fear[^wilson2017good-e20].

**In the smart-contract example** `[Our analysis]`: contract source code scraped from a blockchain explorer and a downloaded public vulnerability dataset are raw data and go in `data/raw/`. The version after removing duplicates and filtering out contracts that don't compile is derived data, generated by a script in `src/`. Your own manual labels ("does this contract have a reentrancy vulnerability?") are raw data you produced yourself; after each labeling round, save a read-only copy as well.

The same holds in other fields: original questionnaires, interview recordings, files exported from instruments, and scans of field notes are all raw data. `[Our analysis]`

**Where people go wrong:** "Just quickly" deleting a few obviously bad rows in the raw file. A few months later you can't say which rows you deleted or why, and you can't rerun from the start. `[Our analysis]`

**Write it down:** In `data/raw/README.md`, write one line for each raw dataset: what it is, where it came from, when it was obtained, and by whom.

## 3. Every result must be traceable to how it was produced

**How:** For any result that might turn out to be useful, record how it was produced[^sandve2013ten-e7]. The minimum bar: you yourself, a year from now, can roughly reproduce it[^sandve2013ten-e2].

Record every detail of every step that might affect the result. For steps done by a program, the key items are the program's name and version and the exact parameters and inputs[^sandve2013ten-e8]. For analyses involving randomness, record the random seed[^sandve2013ten-e11].

**For every run, record at least these** `[Our analysis]`:

| What to record | Smart-contract example |
|---|---|
| What you wanted to test | "Does adding vulnerability patterns to the prompt raise the detection rate for reentrancy vulnerabilities?" |
| Which version of the code and data | The commit ID in version control; whether the benchmark is before or after removing leaked samples |
| Parameters and program versions | Large language model name and version, temperature, full prompt text |
| Random seed | The random seeds used for sampling and model calls |
| Where the output is | `results/2026-10-07_prompt-comparison/` |
| What you saw and what you make of it | For example, "detection rate went up, but so did false positives; need to check which kinds of contracts" |

**Keep two records side by side.** The principle is to record every operation you perform and make it as transparent and repeatable as possible[^noble2009quick-e8]. One practical approach: describe the experiment in prose in your notebook, and keep every detail in the script that runs it[^noble2009quick-e9]. The script makes sure you can rerun it; the notebook makes sure you can understand why you ran it.

**Every conclusion in the paper must lead back to the exact result it rests on**[^sandve2013ten-e12]. If the paper says "the prompt raised the detection rate by 12 percentage points", you should be able to trace that number all the way back to a particular results folder, commit, and data version.

**What tools to use** `[Our analysis]`: when you have only a few experiments, a spreadsheet or a text file is enough, one row per experiment. When there are too many for a spreadsheet, consider a dedicated experiment-tracking tool; these are common in machine learning. For example, MLflow provides an API and a user interface for logging parameters, code versions, metrics, and output files[^mlflowtracking-e1]. A tool only automates the record-keeping; the principles of what to record stay the same. Research that doesn't run large numbers of computational experiments doesn't need one.

**Where people go wrong:** Recording only the runs that "worked". Failed and inconclusive results are often what you later rely on to explain why you designed things the way you did. `[Our analysis]`

**Write it down:** Turn the table above into a run-log template (one row per run) and fill in your most recent experiment. Any column you can't fill in is something missing from your records.

## 4. Use version control, not file names, to manage versions

**How:**

- **Don't manage versions with `final`, `final2`, `final_really_final`** `[Our analysis]`. File names should reflect content or purpose. Also avoid sequential numbers (`result1.csv`) or a position in the manuscript (`fig_3_a.png`); those numbers will almost certainly change[^wilson2017good-e13].
- **Use version control from the start of the project.** Don't wait a few weeks only to find there is no record of your first versions of the code[^noble2023ten-e12]. Put every script you write under version control[^sandve2013ten-e11].
- **Commit small and often.** One commit covers one group of related work, at a pace of roughly a few times a day to a few times a week[^mineault2021good-e3]. How big should a change be? A group of edits you can imagine wanting to undo in one step someday[^wilson2017good-e14].

**Why:** Version control timestamps every saved change automatically, so you no longer depend on people giving backup copies sensible names[^wilson2017good-e16]. `final2` can't tell you how it differs from `final`; the commit history can. More importantly, if you can't get back to the code that produced a result, you can't tell whether that result was caused by a bug[^sandve2013ten-e4].

**Materials that aren't code** `[Our analysis]`: if questionnaires, interview guides, or paper drafts aren't under version control, name the copies by "date + content" (e.g. `2026-10-05_annotation-guide_round2.docx`) and note what changed in a change log (see Section 5).

**Write it down:** Initialize a git repository in the project's root folder and commit your existing scripts. Rename every file called `final`, `new`, or `v2` to something that says what it contains.

## 5. Keep three kinds of notes apart

Every project should keep at least three kinds of written record, each with its own job `[Our analysis, based on the sources below]`:

| Note | What it answers | How to keep it |
|---|---|---|
| **Status** | Where does the project stand now? What's next? | Only one copy, always current; overwrite old content. It can be a section of the README plus a to-do list[^wilson2017good-e12] |
| **Research log** | What did I do on which day, what did I see, what did I make of it, what did I decide? | Append by date, in some detail[^noble2009quick-e6]; never delete old entries |
| **Settled conclusions** | What do we know for sure? What important decisions did we make, and why? What limitations do we know about? | Only findings and decisions that have been checked, updated as the project goes; this is the raw material for the paper |

**The research log is the core.** For how to log each day and review every week or two while running the study, see [Running and iterating](../02_do-the-project/06_run-and-iterate.md). Here we cover only how to keep it so it holds up when you look things up later. Most of the points below come from notebook rules written for computational biologists[^schnell2015ten-e8], and they apply equally to other research `[Our analysis]`:

- **Write it chronologically, one entry after another**, each with its date and subject[^schnell2015ten-e10].
- **Write each entry right after the work is done**[^schnell2015ten-e3]. If you rely on memory, a suggestion from a meeting or a key step in your analysis may well be gone by the time you need it[^schnell2015ten-e9].
- **Record more than what you did:** also your observations, conclusions, and ideas for what to do next, with the result figures attached[^noble2009quick-e6].
- **Don't erase mistakes.** Put a thin line through them and write the correction next to them. Mistakes are an important part of the research process[^schnell2015ten-e4].

A **change log** is a stripped-down research log that records only what changed in the project's files: put a `CHANGELOG.txt` in the documentation folder and write dated notes of changes in reverse chronological order (most recent first). It serves as the equivalent of a lab notebook[^wilson2017good-e15]. Materials that aren't under version control need one most `[Our analysis]`.

**Reading notes** are kept separately, one file per paper; see [Entering a field and exploring the literature](../01_find-a-problem/01_enter-a-field.md#6-take-notes-one-per-paper-plus-a-problem-log). You can put them under `notes/papers/`, alongside the project. `[Our analysis]`

**Why three kinds:** The log is ordered by time and answers "what happened that day". When you want to know "where do things stand" or "what do we know for sure", paging through hundreds of log entries is too slow. On the other hand, with only a status document, a few months later you can't say how a decision came about. The three complement each other; you don't pick one. In each weekly review, condense that week's log into the status and settled-conclusions files; see [Planning and daily routines](planning_and_routines.md). `[Our analysis]`

**Write it down:** Create the three files `status.md`, `log.md`, and `findings.md`. Write the first log entry today: date, what you did, what you saw, next step.

> **Where sources disagree: organize the results folder by date or by content?**
>
> - **By date:** Noble organizes data and results folders by date, because "logical" folder names may be meaningless even to you six months later[^noble2009quick-e4][^noble2009quick-e5].
> - **By content:** Wilson and colleagues recommend using naming conventions or subfolders to clearly separate intermediate files such as cleaned data, statistical tables, and publication-ready figures, grouping together those that belong to the same paper[^wilson2017good-e19].
>
> The two can be combined `[Our analysis]`: during exploration, store by date (`results/2026-10-05_topic/`), which lines up neatly with a research log kept by date; when you start writing the paper, move the figures and tables that go into it, plus the scripts that make them, to a place named by content (e.g. `results/paper/`).

## 6. Write a README for your future self

**How:**

- **Put a README in the project's root folder** that explains the purpose of the project[^wilson2017good-e11]. It is the landing page for the whole project[^turingwaycompendia-e4]. Say clearly what the project is, where it stands, how to run or reproduce it, and what each folder holds `[Our analysis]`.
- **Put a README in each major folder too**, explaining what the files are and what they are for; update it whenever files are added or removed[^osforganizing-e4].
- **Specify the computing environment**[^turingwaycompendia-e3], such as the software and versions used.

**Why:** A few months from now you will certainly come back to your own code, for example to run a few extra experiments for the final version of the paper, and find you have no idea what is going on. One remedy is to write a detailed README in every repository, as a note to your future self on how the code works and how to run it[^karpathy2016survival-e10]. As one saying puts it, documentation is a love letter you write to your future self[^mineault2021good-e4]. File names and locations are also documentation in their own right: the more clearly they are organized, the more reproducible your research[^osforganizing-e1].

**Where people go wrong:** Writing the README once and never updating it, so it no longer matches the folders. An outdated README is more misleading than none. `[Our analysis]`

**Write it down:** Spend ten minutes writing the root README. Then ask a classmate to read only the README and tell you how to produce your main result; wherever they get stuck is what you need to add.

---

## Common mistakes

| Mistake | Why it is a problem |
|---|---|
| Cleaning and editing the raw data directly | If something goes wrong you can't go back, and you can't rerun the analysis from scratch[^wilson2017good-e20] |
| Naming files `final`, `final2`, `result1` | You can't tell how versions differ, and the numbers change[^wilson2017good-e13][^wilson2017good-e16] |
| Starting version control only after a few weeks | The first versions have no record[^noble2023ten-e12] |
| Committing a pile of unrelated changes at once | Later you can't undo just one of them[^wilson2017good-e14] |
| Not recording how a result file was produced | A year later even you can't reproduce it[^sandve2013ten-e2] |
| Keeping only one figure from a failed experiment and moving on | Others, and future you, can't see why it counted as a failure[^noble2009quick-e7] |
| Filling in the log a few days later | The key ideas and steps are already forgotten[^schnell2015ten-e9] |
| Keeping only a log, with no status or conclusions | To find out "where things stand" you have to page through hundreds of entries `[Our analysis]` |
| No README, or a README never updated | A few months later even you can't make sense of it[^karpathy2016survival-e10] |

## Further reading

- **Noble, "A Quick Guide to Organizing Computational Biology Projects"** (2009): read it when setting up folders and starting a notebook. Short and written for computational biologists, but the principles carry over to other research.
- **Wilson et al., "Good enough practices in scientific computing"** (2017): for scientific computing; the minimum set of practices the authors believe every researcher can and should consider adopting[^wilson2017good-e1], covering data, code, collaboration, project organization, and version control.
- **Sandve et al., "Ten Simple Rules for Reproducible Computational Research"** (2013): for computational research; read it when you want every result to be traceable and reproducible.
- **Schnell, "Ten Simple Rules for a Computational Biologist's Laboratory Notebook"** (2015): read it when you want to keep a better research log. Written for biologists who do purely computational work.
- **The Turing Way, Research Compendia:** read it when you want to package a whole project so it can be shared and reproduced.
- **Mineault, The Good Research Code Handbook:** for people who write research code; covers project structure, git, and documentation.
- **OSF (Open Science Framework), "Organizing files":** a help page from this open-science platform; a short checklist on separating raw and derived data, making raw data read-only, and writing READMEs.

[^wilson2017good-e1]: Wilson et al. 2017, Introduction. [Evidence](../../sources/notes/wilson2017good.md#e1)
[^wilson2017good-e5]: Wilson et al. 2017, Introduction. [Evidence](../../sources/notes/wilson2017good.md#e5)
[^wilson2017good-e6]: Wilson et al. 2017, Project organization, 4a. [Evidence](../../sources/notes/wilson2017good.md#e6)
[^wilson2017good-e7]: Wilson et al. 2017, Project organization, 4b. [Evidence](../../sources/notes/wilson2017good.md#e7)
[^wilson2017good-e8]: Wilson et al. 2017, Project organization, 4c. [Evidence](../../sources/notes/wilson2017good.md#e8)
[^wilson2017good-e9]: Wilson et al. 2017, Data management, 1a. [Evidence](../../sources/notes/wilson2017good.md#e9)
[^wilson2017good-e10]: Wilson et al. 2017, Data management, 1b. [Evidence](../../sources/notes/wilson2017good.md#e10)
[^wilson2017good-e11]: Wilson et al. 2017, Collaboration, 3a. [Evidence](../../sources/notes/wilson2017good.md#e11)
[^wilson2017good-e12]: Wilson et al. 2017, Collaboration, 3b. [Evidence](../../sources/notes/wilson2017good.md#e12)
[^wilson2017good-e13]: Wilson et al. 2017, Project organization, 4f. [Evidence](../../sources/notes/wilson2017good.md#e13)
[^wilson2017good-e14]: Wilson et al. 2017, Keeping track of changes, 5b. [Evidence](../../sources/notes/wilson2017good.md#e14)
[^wilson2017good-e15]: Wilson et al. 2017, Keeping track of changes, 5f. [Evidence](../../sources/notes/wilson2017good.md#e15)
[^wilson2017good-e16]: Wilson et al. 2017, Keeping track of changes. [Evidence](../../sources/notes/wilson2017good.md#e16)
[^wilson2017good-e17]: Wilson et al. 2017, Keeping track of changes. [Evidence](../../sources/notes/wilson2017good.md#e17)
[^wilson2017good-e19]: Wilson et al. 2017, Project organization, 4c. [Evidence](../../sources/notes/wilson2017good.md#e19)
[^wilson2017good-e20]: Wilson et al. 2017, Data management, 1a. [Evidence](../../sources/notes/wilson2017good.md#e20)
[^wilson2017good-e21]: Wilson et al. 2017, Data management, 1a. [Evidence](../../sources/notes/wilson2017good.md#e21)
[^noble2009quick-e1]: Noble 2009, Principles. [Evidence](../../sources/notes/noble2009quick.md#e1)
[^noble2009quick-e2]: Noble 2009, Principles. [Evidence](../../sources/notes/noble2009quick.md#e2)
[^noble2009quick-e3]: Noble 2009, File and Directory Organization. [Evidence](../../sources/notes/noble2009quick.md#e3)
[^noble2009quick-e4]: Noble 2009, File and Directory Organization. [Evidence](../../sources/notes/noble2009quick.md#e4)
[^noble2009quick-e5]: Noble 2009, File and Directory Organization. [Evidence](../../sources/notes/noble2009quick.md#e5)
[^noble2009quick-e6]: Noble 2009, The Lab Notebook. [Evidence](../../sources/notes/noble2009quick.md#e6)
[^noble2009quick-e7]: Noble 2009, The Lab Notebook. [Evidence](../../sources/notes/noble2009quick.md#e7)
[^noble2009quick-e8]: Noble 2009, Carrying Out a Single Experiment. [Evidence](../../sources/notes/noble2009quick.md#e8)
[^noble2009quick-e9]: Noble 2009, Carrying Out a Single Experiment. [Evidence](../../sources/notes/noble2009quick.md#e9)
[^noble2009quick-e10]: Noble 2009, Figure 1 caption. [Evidence](../../sources/notes/noble2009quick.md#e10)
[^sandve2013ten-e2]: Sandve et al. 2013, Rule 1. [Evidence](../../sources/notes/sandve2013ten.md#e2)
[^sandve2013ten-e4]: Sandve et al. 2013, Rule 4. [Evidence](../../sources/notes/sandve2013ten.md#e4)
[^sandve2013ten-e7]: Sandve et al. 2013, Rule 1. [Evidence](../../sources/notes/sandve2013ten.md#e7)
[^sandve2013ten-e8]: Sandve et al. 2013, Rule 1. [Evidence](../../sources/notes/sandve2013ten.md#e8)
[^sandve2013ten-e10]: Sandve et al. 2013, Rule 2. [Evidence](../../sources/notes/sandve2013ten.md#e10)
[^sandve2013ten-e11]: Sandve et al. 2013, Rule 4, Rule 6. [Evidence](../../sources/notes/sandve2013ten.md#e11)
[^sandve2013ten-e12]: Sandve et al. 2013, Rule 9. [Evidence](../../sources/notes/sandve2013ten.md#e12)
[^schnell2015ten-e3]: Schnell 2015, Rule 4. [Evidence](../../sources/notes/schnell2015ten.md#e3)
[^schnell2015ten-e9]: Schnell 2015, Rule 3. [Evidence](../../sources/notes/schnell2015ten.md#e9)
[^schnell2015ten-e10]: Schnell 2015, Rule 5. [Evidence](../../sources/notes/schnell2015ten.md#e10)
[^schnell2015ten-e4]: Schnell 2015, Rule 5. [Evidence](../../sources/notes/schnell2015ten.md#e4)
[^schnell2015ten-e8]: Schnell 2015, Introduction. [Evidence](../../sources/notes/schnell2015ten.md#e8)
[^turingwaycompendia-e1]: The Turing Way, Research Compendia, Summary. [Evidence](../../sources/notes/turingwaycompendia.md#e1)
[^turingwaycompendia-e2]: The Turing Way, Research Compendia, Summary. [Evidence](../../sources/notes/turingwaycompendia.md#e2)
[^turingwaycompendia-e3]: The Turing Way, Research Compendia, Structure of a Research Compendium. [Evidence](../../sources/notes/turingwaycompendia.md#e3)
[^turingwaycompendia-e4]: The Turing Way, Research Compendia, Basic Compendium. [Evidence](../../sources/notes/turingwaycompendia.md#e4)
[^mineault2021good-e1]: Mineault 2021, Setting up your project. [Evidence](../../sources/notes/mineault2021good.md#e1)
[^mineault2021good-e2]: Mineault 2021, Setting up your project. [Evidence](../../sources/notes/mineault2021good.md#e2)
[^mineault2021good-e3]: Mineault 2021, Setting up your project, git section. [Evidence](../../sources/notes/mineault2021good.md#e3)
[^mineault2021good-e4]: Mineault 2021, Document your code (citing Damian Conway). [Evidence](../../sources/notes/mineault2021good.md#e4)
[^osforganizing-e1]: OSF Support, Organizing files. [Evidence](../../sources/notes/osforganizing.md#e1)
[^osforganizing-e2]: OSF Support, Separate raw data from derived data. [Evidence](../../sources/notes/osforganizing.md#e2)
[^osforganizing-e3]: OSF Support, Make raw data read-only. [Evidence](../../sources/notes/osforganizing.md#e3)
[^osforganizing-e4]: OSF Support, Make README files. [Evidence](../../sources/notes/osforganizing.md#e4)
[^mlflowtracking-e1]: MLflow documentation, MLflow Tracking (official tool documentation). [Evidence](../../sources/notes/mlflowtracking.md#e1)
[^karpathy2016survival-e10]: Karpathy 2016, Writing code, "Think of the future you". [Evidence](../../sources/notes/karpathy2016survival.md#e10)
[^noble2023ten-e12]: Noble 2023, Rule 9. [Evidence](../../sources/notes/noble2023ten.md#e12)
