# Carlini 等人 2019：On Evaluating Adversarial Robustness

- 资料：`carlini2019evaluating`，[原文](https://arxiv.org/abs/1902.06705)
- 版本：arXiv:1902.06705，本地 PDF `papers/pdf/carlini2019evaluating.pdf`。
- 说明：面向机器学习安全方向（对抗样本防御）的评估指南。

### E1

- 位置：§2.5 Adaptive Adversaries
- 原文："After the defense has been defined, ask: what attack could possibly defeat this defense? All attacks that might work must be shown to be ineffective." / "Just applying existing adversarial attacks with default hyperparameters is not sufficient, even if these attacks are state-of-the-art"
- 要点：评估一个防御时，要问"什么攻击可能攻破它"，并证明这些攻击都无效；只用默认参数跑现成的攻击，即使是最先进的攻击，也不够。
