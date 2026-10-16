# Carlini et al. 2019: On Evaluating Adversarial Robustness

- Source: `carlini2019evaluating`, [Original](https://arxiv.org/abs/1902.06705)
- Version: arXiv:1902.06705, local PDF `papers/pdf/carlini2019evaluating.pdf`.
- Note: An evaluation guide for machine learning security (defenses against adversarial examples).

### E1

- Location: §2.5 Adaptive Adversaries
- Quote: "After the defense has been defined, ask: what attack could possibly defeat this defense? All attacks that might work must be shown to be ineffective." / "Just applying existing adversarial attacks with default hyperparameters is not sufficient, even if these attacks are state-of-the-art"
- Key point: When evaluating a defense, ask what attack could possibly defeat it, and show that every such attack is ineffective; running existing attacks with default hyperparameters is not enough, even state-of-the-art ones.
