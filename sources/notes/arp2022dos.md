# Arp 等人 2022：Dos and Don'ts of Machine Learning in Computer Security

- 资料：`arp2022dos`，[原文](https://arxiv.org/abs/2010.09470)
- 版本：USENIX Security 2022，本地 PDF `papers/pdf/arp2022dos.pdf`。
- 说明：总结机器学习用于计算机安全时的十种常见陷阱（P1–P10）。

### E1

- 位置：§2，P6 Inappropriate Baseline
- 原文："To show to what extent a novel method improves the state of the art, it is vital to compare it with previously proposed methods." / "Instead of focusing solely on complex models for comparison, simple models should also be considered throughout the evaluation."
- 要点：要说明新方法比现有方法好多少，就必须和已有方法比较；除了复杂模型，也要和简单模型比。

### E2

- 位置：§2，P9 Lab-Only Evaluation
- 原文："A learning-based system is solely evaluated in a laboratory setting, without discussing its practical limitations." / "it should be evaluated in a realistic setting whenever possible to transparently assess its capabilities"
- 要点：只在实验室环境中评估、不讨论实际局限，是常见陷阱；只要可能，就应在真实环境中评估。
