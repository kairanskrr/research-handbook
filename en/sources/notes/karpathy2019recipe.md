# Karpathy 2019: A Recipe for Training Neural Networks

- Source: `karpathy2019recipe`, [original](https://karpathy.github.io/2019/04/25/recipe/)
- Version: Author's blog, 2019-04-25.
- Note: Written about training neural networks (machine learning). We excerpt only the lessons that generalize: start simple, verify every step, add one thing at a time, and check against baselines that "should not work."

### E1

- Location: The recipe (overview)
- Quote: "it builds from simple to complex and at every step of the way we make concrete hypotheses about what will happen and then either validate them with an experiment or investigate until we find some issue."
- Key point: Build from simple to complex; at each step, make a concrete prediction of what will happen, then verify it with an experiment or investigate until you find the problem.

### E2

- Location: The recipe (overview)
- Quote: "What we try to prevent very hard is the introduction of a lot of “unverified” complexity at once"
- Key point: Try hard to avoid introducing a lot of unverified complexity at once.

### E3

- Location: 2) Neural net training fails silently
- Quote: "Everything could be correct syntactically, but the whole thing isn’t arranged properly, and it’s really hard to tell."
- Key point: Code that runs without errors is not necessarily correct; many mistakes are silent, and the results still look like they "work."

### E4

- Location: 2. Set up the end-to-end training/evaluation skeleton + get dumb baselines › fix random seed
- Quote: "Always use a fixed random seed to guarantee that when you run the code twice you will get the same outcome."
- Key point: While building and debugging, fix the random seed so two runs give the same outcome, removing one source of variation.

### E5

- Location: Same as above › input-indepent baseline
- Quote: "Train an input-independent baseline, (e.g. easiest is to just set all your inputs to zero). This should perform worse than when you actually plug in your data without zeroing it out."
- Key point: Train an input-independent baseline: if it does about as well as the real model, the model is not learning anything from the data.

### E6

- Location: 3. Overfit › complexify only one at a time
- Quote: "If you have multiple signals to plug into your classifier I would advise that you plug them in one by one and every time ensure that you get a performance boost you’d expect."
- Key point: When adding several new signals, add them one at a time and check each time that you get the improvement you expect.

### E7

- Location: 1. Become one with the data
- Quote: "The outliers especially almost always uncover some bugs in data quality or preprocessing."
- Key point: Look at the data yourself first, especially the outliers, which almost always uncover problems in data quality or preprocessing.

### E8

- Location: 2. Set up the end-to-end training/evaluation skeleton + get dumb baselines (opening paragraph)
- Quote: "Our next step is to set up a full training + evaluation skeleton and gain trust in its correctness via a series of experiments. At this stage it is best to pick some simple model that you couldn’t possibly have screwed up somehow"
- Key point: Before trying complex models, set up a full training and evaluation skeleton and gain trust in it through a series of experiments; at this stage, pick a model so simple you could not have gotten it wrong.

### E9

- Location: 2. Set up the end-to-end training/evaluation skeleton + get dumb baselines (closing paragraph)
- Quote: "we have the full training + evaluation pipeline working. For any given model we can (reproducibly) compute a metric that we trust." / "the performance of a few dumb baselines (we better beat these)"
- Key point: This step is done when the full training and evaluation pipeline works, you can reproducibly compute a trusted metric for any model, and you have the scores of a few dumb baselines that you must beat.
