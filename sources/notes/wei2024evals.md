# Jason Wei 2024：Successful language model evals

- 资料：`wei2024evals`，[原文](https://www.jasonwei.net/blog/evals)
- 版本：博客文章，2024 年 5 月 24 日；2026-10-05 读取。
- 说明：作者是大语言模型研究者，从使用者和构建者角度总结什么样的评测基准（eval）会成功。内容针对大语言模型评测。

### E1

- 位置：第 1 段
- 原文："Evals are incentives for the research community, and breakthroughs are often closely linked to a huge performance jump on some eval."
- 要点：评测基准是研究社区的激励，突破往往和某个基准上的大幅提升联系在一起。

### E2

- 位置：评测常见错误
- 原文："If an eval doesn’t have enough examples, it will be noisy and a bad UI for researchers." / "It’s good to have at least 1,000 examples for your eval; perhaps more if it’s a multiple choice eval."
- 要点：样本太少，评测结果噪声大；最好至少 1000 个样本，选择题形式的更多。

### E3

- 位置：评测常见错误
- 原文："Evals should be high quality. If there are a lot of mistakes in your eval, people won’t trust it."
- 要点：评测集要高质量，错误多了没人信。作者举例：模型强到一定程度后，它答错的题更可能是标准答案错了。

### E4

- 位置：评测常见错误
- 原文："It’s critical to have a single-number metric—I can’t think of any great evals that don’t have a single-number metric."
- 要点：要有一个单一数字的指标；指标和子集太多，评测难以理解，用的人就少。

### E5

- 位置：评测常见错误
- 原文："If your eval takes too much work to run, it won’t gain traction even if everything else is good."
- 要点：运行起来太费事的评测，其他方面再好也难以推广。

### E6

- 位置：评测常见错误
- 原文："If an eval is not on a meaningful task, AI researchers won’t deeply care about it."
- 要点：任务本身没有意义，在上面做得好也得不出有实质意义的结论。

### E7

- 位置：评测常见错误
- 原文："The grading in your eval should be extremely correct."
- 要点：评分必须极其准确，要尽量减少答案解析等环节的错误。

### E8

- 位置：评测常见错误
- 原文："For the eval to stand the test of time, performance must not become saturated too quickly."
- 要点：评测不能太快被"做满"（饱和），否则很难再显示进步，大家就不用了。

### E9

- 位置：测试集污染
- 原文："After the creation of a good eval, examples of the eval tend to get propagated into various places in the internet, like arxiv papers, ChatGPT examples, or reddit." / "Chris Manning had a good suggestion of an eval having both a public test set and a private test set, and monitoring whether any models deviate substantially on those two test sets."
- 要点：好的评测发布后，题目会扩散到互联网各处，造成测试集污染；一种办法是同时设公开和私有测试集，监测模型在两者上的表现是否明显不同。

### E10

- 位置：人工两两评比
- 原文："The dangerous side of pairwise evals is that you aren’t exactly sure what you’re measuring"
- 要点：让人两两比较模型输出的评测，危险在于不确定到底测的是什么，例如感觉和风格占了多大比重。

### E11

- 位置：大语言模型让评测更难
- 原文："And even those have problems, like deciding on the prompt or parsing the answer."
- 要点：即使是评分简单的评测，也有提示词怎么定、答案怎么解析的问题。

### E12

- 位置：评测常见错误（开头）
- 原文："It’s easier to mess up an eval than to make a good one."
- 要点：做坏一个评测比做好一个容易。
