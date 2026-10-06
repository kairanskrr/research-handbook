# Fox 等 2021：Data and Software Sharing Guidance for Authors Submitting to AGU Journals

- 资料：`fox2021agudata`，[原文](https://data.agu.org/resources/agu-data-software-sharing-guidance)
- 版本：AGU 开放科学网站上的指南网页（CC BY 4.0），对应 Zenodo 记录 https://doi.org/10.5281/zenodo.5124741 。AGU 主站的"Data and Software for Authors"页面对脚本访问返回 403，Internet Archive 快照的正文由脚本加载、无法读出，所以本摘录只用这份指南。位置写小标题。

### E1

- 位置：引言
- 原文："These digital objects need to be accessible, understandable, and open as possible for reuse to support transparency and replicability."
- 要点：AGU 期刊要求数据和软件尽可能开放、可理解、可重用，以支持透明和可重复。所列对象包括野外观测数据、卫星数据、实验室数据、分析和建模用的软件、论文图中的全部数据。

### E2

- 位置：引言
- 原文："Data or software should be as open as possible, as closed as necessary. For data concerning Indigenous Peoples, authors should consult the CARE Principles for Indigenous Data Governance."
- 要点：数据和软件"尽可能开放，必要时才封闭"；涉及原住民的数据，要参考 CARE 原则。

### E3

- 位置：1. When to Make Your Data and Software Available
- 原文："At the time your paper is submitted, your data and software must be available to the editors and reviewers."
- 要点：投稿时，数据和软件就必须能让编辑和审稿人拿到。

### E4

- 位置：1. When to Make Your Data and Software Available
- 原文："Data or software that are sensitive and require restrictions on access (e.g., personal data, medical information, fossil locations, strategic models) must be preserved in a repository with appropriate access controls."
- 要点：敏感数据（例如个人数据、化石产地位置）也要存进有访问控制的数据库，而不是不存。

### E5

- 位置：Software Availability Statement (required)
- 原文："Note that “git/GitHub/GitLab” are not acceptable software preservation repositories because they are not archival."
- 要点：GitHub、GitLab 不算合格的软件保存库，因为它们不是存档服务。

### E6

- 位置：6. Availability Statements and Template Examples
- 原文："Statements to the effect of “data available from authors” are not acceptable. Also, statements to the effect of “data available from http://nasa.gov” are not acceptable since high-level website references do not meet the AGU’s Data and Software for Authors requirements."
- 要点："数据可向作者索取"和只给一个大网站首页的写法，都不符合 AGU 期刊的要求。

### E7

- 位置：2. Guidelines for Research Primarily Based on Numerical Models or Theory
- 原文："The goal is to provide sufficient information and resources so that an interested user, with sufficient computer resources, can replicate your simulation."
- 要点：模型配置、参数和运行脚本要提供到这样的程度：有足够算力的读者能重复你的模拟。

### E8

- 位置：2. Guidelines for Research Primarily Based on Numerical Models or Theory
- 原文："There are currently limited resources for preserving files of very large size. However, selecting adequate output to produce manuscript figures and tables is generally much more manageable and is sufficient to meet the needs of replicability."
- 要点：海量模型输出难以全部保存，但保存足以画出论文图表的那部分输出，一般可行，也够用。

### E9

- 位置：3. Selecting a repository
- 原文："Selecting a repository and determining data and software management best practices begins when you propose and fund your research project, through your Data (and Software) Management Plan."
- 要点：选数据库、定数据管理做法，从写项目申请和数据管理计划时就开始。

### E10

- 位置：1. Considerations for publication，Large Data
- 原文："Large Data (>1TB): Preservation of large data may be possible in some repositories for a fee. Authors should account for this in their research budget and Data Management Plan."
- 要点：超过 1 TB 的大数据保存可能要收费，要写进预算和数据管理计划。

### E11

- 位置：3. Selecting a repository，Institutional Repository
- 原文："Librarians can be an excellent source of research data management support, including repository selection"
- 要点：图书馆员可以帮忙选数据库、管理科研数据。

### E12

- 位置：1. Considerations for publication，Data Citation
- 原文："Include data citations for the primary and processed research data in the References section of your paper. Doing so ensures proper credit is given for the data."
- 要点：原始数据和处理后的数据都要写进参考文献，这样数据的贡献者才能得到应有的认可。

### E13

- 位置：2. Guidelines for Research Primarily Based on Numerical Models or Theory
- 原文："In the Ocean modeling community it is common to use numerical models that are open access and well documented"
- 要点：海洋建模界常用开放获取、文档完善的数值模型（这是指南对海洋建模这一个方向的描述）。

### E14

- 位置：Software Availability Statement (required)
- 原文："A Software Availability Statement is required in the Open Research section of your paper for software that is central to your research such as for model simulations, data analysis, data visualization, and model output analysis."
- 要点：AGU 期刊要求在"开放研究"（Open Research）一节写软件可获取性声明，覆盖模拟、数据分析、可视化和模型输出分析用的软件。

### E15

- 位置：2. Guidelines for Research Primarily Based on Numerical Models or Theory
- 原文："the software code (e.g. Python, Jupyter Notebooks, R, MATLAB) used to perform any data analysis and to produce the manuscript’s figures should be made available in a free and open platform (e.g., Github) and preserved in a repository (e.g., Zenodo)."
- 要点：做分析和画图的代码，要放在开放平台上，并存档到 Zenodo 这类保存库。
