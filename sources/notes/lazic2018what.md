# Lazic、Clarke-Williams 和 Munafò 2018：What exactly is 'N' in cell culture and animal experiments?

- 资料：`lazic2018what`，[原文](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.2005282)
- 版本：PLOS Biology 16(4):e2005282，2018 年，开放获取。原文文本读取自 PLOS 网站提供的文章 XML，2026-10-06。位置写小标题。

### E1

- 位置：Introduction
- 原文："The wrong choice of replicate cannot be fixed by a clever statistical analysis after the experiment is completed (e.g., using multilevel or hierarchical models); it needs to be planned at the design stage."
- 要点：重复做在了错误的层次上，实验做完后再巧妙的统计分析也补救不了，必须在设计阶段就规划好。

### E2

- 位置：Introduction
- 原文："we argue that the frequent and common distinction made between ‘biological’ and ‘technical’ replication is unhelpful because they are inconsistently defined, do not capture the important characteristics of an experiment, and do not clarify what to replicate."
- 要点：作者认为常用的"生物学重复 / 技术重复"二分法没有帮助：定义不一致，抓不住实验的要害，也说不清该重复什么。他们改用生物单位、实验单位、观察单位三个概念。

### E3

- 位置：Box 2. Types of units
- 原文："Experimental unit (EU): the entity that is randomly and independently assigned to experimental conditions. The sample size (N) is equal to the number of EUs." / "Observational unit (OU): the entity on which measurements are taken, which may be different from the EUs and BUs of interest. Increasing the number of OUs does not increase the sample size."
- 要点：实验单位是被随机、独立地分配到不同实验条件的对象，样本量 N 等于实验单位的个数；观察单位是被测量的对象，增加观察单位不会增加样本量。

### E4

- 位置：Requirements for genuine replication
- 原文："First, EUs must be independently allocated to experimental conditions or interventions." / "The second requirement is that the experimental intervention must be applied independently to each EU." / "The third requirement is that EUs must not influence each other, especially on the measured outcome variables."
- 要点：真正的重复要满足三条：实验单位被独立分组；处理被独立地施加到每个实验单位；实验单位之间互不影响，尤其在测量的结局上。

### E5

- 位置：Cell culture experiments
- 原文："Hence, the third criterion is not met for using cells as the EU. Thus, a well, culture dish, or another plastic container is the appropriate EU for cell culture experiments."
- 要点：同一孔里的细胞同时接受处理、彼此影响，不能当实验单位；细胞培养实验的实验单位是孔、培养皿或其他容器。

### E6

- 位置：Cell culture experiments
- 原文："For this reason, in vitro experiments are usually repeated on multiple days, and the number of wells, aliquots, or culture dishes within a day are treated as subsamples." / "This is a scientific judgement about the relevant unit that we would like to make inferences about, and although opinions may differ, using more stringent criteria makes the results more believable."
- 要点：体外实验对条件很敏感，所以通常在不同的日子重复整个实验，同一天内的孔、分装、培养皿只算子样本。这是一个科学判断，看法可能不同，但标准越严，结果越可信。

### E7

- 位置：Requirements for genuine replication
- 原文："If we hypothesise that breast cancer cell lines proliferate at a faster rate than lung cancer cell lines, we need multiple breast and lung cell lines, as the hypothesis is about differences between the tissue of origin."
- 要点：假设关于哪一层，就要在哪一层重复。比如假设是"乳腺癌细胞系比肺癌细胞系增殖快"，就要用多株乳腺癌和多株肺癌细胞系。

### E8

- 位置：Analysis of hierarchical data
- 原文："a simple solution to the problem of pseudoreplication is to reduce the data to a single value for each EU."
- 要点：避免伪重复的简单办法：把每个实验单位的多次测量汇总成一个值（如平均值）再做统计。

### E9

- 位置：What is the extent of the problem?；Box 1
- 原文："We found that only 22% of studies (95% CI = 17%–29%) had genuine replication and thus made valid statistical inferences. Nearly half of the studies (46%, 95% CI = 38%–53%) had pseudoreplication" / "restricting the search to non-review articles between January 2011 and September 2016"
- 要点：作者从 PubMed 抽取 2011 年 1 月到 2016 年 9 月发表的 200 篇动物研究（处理施加在亲代、在子代测量结果）：只有 22% 做了真正的重复，46% 有伪重复，其余信息不足无法判断。

### E10

- 位置：Requirements for genuine replication
- 原文："to increase the sample size we need to increase the number of EUs (a useful phrase to remember is ‘sample size is where you randomise’)"
- 要点：要增加样本量，就要增加实验单位；一句好记的话："在哪一层随机分组，样本量就按哪一层算"。
