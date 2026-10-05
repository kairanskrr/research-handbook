# Karpathy 2019：A Recipe for Training Neural Networks

- 资料：`karpathy2019recipe`，[原文](https://karpathy.github.io/2019/04/25/recipe/)
- 版本：作者博客，2019-04-25。
- 说明：内容针对训练神经网络（机器学习）。这里只摘录可推广的经验：从简单开始、每步验证、一次只加一样东西、用"不该有效"的基线做检查。

### E1

- 位置：The recipe（总述）
- 原文："it builds from simple to complex and at every step of the way we make concrete hypotheses about what will happen and then either validate them with an experiment or investigate until we find some issue."
- 要点：从简单到复杂，每一步都先对结果做具体预测，再用实验验证，不符合就查到找出问题为止。

### E2

- 位置：The recipe（总述）
- 原文："What we try to prevent very hard is the introduction of a lot of “unverified” complexity at once"
- 要点：要尽力避免一次引入大量未经验证的复杂度。

### E3

- 位置：2) Neural net training fails silently
- 原文："Everything could be correct syntactically, but the whole thing isn’t arranged properly, and it’s really hard to tell."
- 要点：程序不报错，不代表做对了；很多错误是静默的，结果看上去照样"能用"。

### E4

- 位置：2. Set up the end-to-end training/evaluation skeleton + get dumb baselines › fix random seed
- 原文："Always use a fixed random seed to guarantee that when you run the code twice you will get the same outcome."
- 要点：搭建和排错阶段固定随机种子，保证两次运行结果相同，去掉一个变动来源。

### E5

- 位置：同上 › input-indepent baseline
- 原文："Train an input-independent baseline, (e.g. easiest is to just set all your inputs to zero). This should perform worse than when you actually plug in your data without zeroing it out."
- 要点：做一个"不看输入"的基线：如果它和真实模型差不多好，说明模型并没有从数据里学到东西。

### E6

- 位置：3. Overfit › complexify only one at a time
- 原文："If you have multiple signals to plug into your classifier I would advise that you plug them in one by one and every time ensure that you get a performance boost you’d expect."
- 要点：要加入多个新东西时，一个一个加，每次确认得到了预期的提升。

### E7

- 位置：1. Become one with the data
- 原文："The outliers especially almost always uncover some bugs in data quality or preprocessing."
- 要点：先亲自看数据，尤其是离群值，它们几乎总能暴露数据质量或预处理的问题。
