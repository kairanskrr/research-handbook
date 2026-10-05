# Noble 2009：A Quick Guide to Organizing Computational Biology Projects

- 资料：`noble2009quick`，[原文](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)
- 版本：PLoS Computational Biology 5(7): e1000424, 2009，开放获取，2026-10-05 读取。位置写小标题。

### E1

- 位置：Principles
- 原文："The core guiding principle is simple: Someone unfamiliar with your project should be able to look at your computer files and understand in detail what you did and why. [...] Most commonly, however, that “someone” is you."
- 要点：核心原则：不熟悉项目的人看你的文件，就能详细了解你做了什么、为什么做；这个人最常见的就是几个月后的你自己。

### E2

- 位置：Principles
- 原文："Everything you do, you will probably have to do over again."
- 要点：你做的每件事，大概都得重做一遍；组织清楚，重做就容易得多。

### E3

- 位置：File and Directory Organization
- 原文："It is generally a good idea to store all of the files relevant to one project under a common root directory. The exception to this rule is source code or scripts that are used in multiple projects."
- 要点：一个项目的所有文件放在同一个根目录下；多个项目共用的代码例外，可以单独成项目。

### E4

- 位置：File and Directory Organization
- 原文："If you try to give your directories logical names, you may end up with a very long list of directories with names that, six months from now, you no longer know how to interpret."
- 要点：给结果目录起"逻辑"名字，半年后可能连自己都看不懂。

### E5

- 位置：File and Directory Organization
- 原文："Instead, I have found that organizing my data and results directories chronologically makes the most sense."
- 要点：作者的做法是数据和结果目录按时间组织（如 2008-12-19 这样的日期目录）。

### E6

- 位置：The Lab Notebook
- 原文："Entries in the notebook should be dated, and they should be relatively verbose, with links or embedded images or tables displaying the results of the experiments that you performed. In addition to describing precisely what you did, the notebook should record your observations, conclusions, and ideas for future work."
- 要点：实验记录本按日期记，写得详细些，附上结果图表；除了做了什么，还要记观察、结论和后续想法。

### E7

- 位置：The Lab Notebook
- 原文："Before doing that, it is important to document how you know the experiment failed, since the interpretation of your results may not be obvious to someone else reading your lab notebook."
- 要点：实验失败时，开始下一个实验之前，先写下你凭什么判断它失败了。

### E8

- 位置：Carrying Out a Single Experiment
- 原文："The general principle is that you should record every operation that you perform, and make those operations as transparent and reproducible as possible."
- 要点：记录你做的每一步操作，并让它尽可能透明、可重复。

### E9

- 位置：Carrying Out a Single Experiment
- 原文："The lab notebook contains a prose description of the experiment, whereas the driver script contains all the gory details."
- 要点：记录本用文字描述实验，驱动脚本保存全部细节，两者并行。

### E10

- 位置：Figure 1 说明
- 原文："The README files in the data directories specify who downloaded the data files from what URL on what date."
- 要点：数据目录里的 README 写明谁在哪天从哪里下载了数据。
