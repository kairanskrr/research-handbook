# Steinhardt 2018: Research as a Stochastic Decision Process

- Source: `steinhardt2018stochastic`, [original](https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html)
- Version: Personal web page, 2018

### E1

- Location: Opening
- Quote: "Throughout, I draw my examples primarily from problems in machine learning and mathematics, but I believe that the principles generalize to other situations as well."
- Key point: The examples come mainly from machine learning and mathematics, but the author believes the principles apply in other settings.

### E2

- Location: Warm-Up
- Quote: "I would do all the easy parts, then get to the hard part and encounter a fundamental obstacle that required scrapping the entire plan and coming up with a new one."
- Key point: Working from easy to hard often means finishing all the easy parts only to hit a fundamental obstacle in the hard part, so the whole plan has to be scrapped.

### E3

- Location: Warm-Up
- Quote: "Rather, we should prioritize tasks that are more likely to fail (so that we remove the risk of them failing) but also tasks that take less time (so that we've wasted less time if one of the tasks does fail, and also so that we get information about tasks more quickly)."
- Key point: Prioritize tasks that are more likely to fail, and also tasks that take less time; that way less is wasted when something fails, and you get information sooner.

### E4

- Location: A Better Strategy: Sorting by Information Rate
- Quote: "Do the components in order from most informative per unit time to least informative per unit time."
- Key point: Rank the parts of the work by "information gained per unit of time," from highest to lowest.

### E5

- Location: A further improvement: opening up the "task" black box
- Quote: "Specifically, for each task we want a cheap way to obtain high confidence about whether that task will be feasible. This is called "de-risking". The following pattern is indispensable: (Basic Pattern) De-risk all components (to the extent feasible), then execute."
- Key point: For each task, first find a cheap way to tell whether it is feasible; this is called "de-risking." The basic pattern is to de-risk all the parts first, then execute.

### E6

- Location: A further improvement
- Quote: "To avoid this issue, we could first download a few thousand examples. We can then examine several examples by hand, as well as compute some aggregate statistics, to assess whether the dataset has the properties we want."
- Key point: Example: before investing heavily in preparing the whole dataset, take a few thousand examples, inspect some by hand, and compute some statistics to judge whether the data fits your needs.

### E7

- Location: Some further practical ideas
- Quote: "The counterpart to ceilings are baselines--simple or off-the-shelf methods that give a quick lower bound on achievable accuracy. Baselines provide an important sanity check, as complicated methods often underperform simple baselines."
- Key point: A baseline (a simple or off-the-shelf method) gives a lower bound on achievable performance and is an important sanity check; complex methods often do worse than simple baselines.

### E8

- Location: Some further practical ideas
- Quote: "More generally, thinking about simplified instances of a problem is often useful. This is because it provides intuition that often suggests/rules out approaches for the original problem."
- Key point: Thinking about simplified versions of the problem first often suggests or rules out approaches to the original problem.

### E9

- Location: Exponentially branching search trees
- Quote: "Whenever something doesn't work, I ask why it didn't work. My goal is to avoid trying similar things that will fail for the same reason"
- Key point: Ask why each failure happened, so you do not keep trying approaches that will fail for the same reason.

### E10

- Location: Exponentially branching search trees
- Quote: "When an experiment fails, it is tempting to conclude "I tried X and it didn't work". However, if X is a high-level conceptual approach, then a more correct conclusion is "I tried an implementation comprising 0.1% of the possible implementations of X, and observed that that particular implementation did not work"."
- Key point: A failed experiment only shows that one particular implementation of X does not work, not that the idea X does not work.

### E11

- Location: Exponentially branching search trees
- Quote: "For this reason, I am far less in favor than most people of publishing negative results, unless the negative result comes with insight into what caused the failure."
- Key point: For this reason the author is more opposed than most people to publishing negative results, unless they come with insight into why the failure happened.

### E12

- Location: Summary
- Quote: "We often try easier tasks first, when instead we should try the most informative tasks first. [...] We are often too slow to try to disprove our own ideas."
- Key point: Common wrong intuitions: doing the easy tasks first instead of the most informative ones, and trying to falsify your own ideas too late.

### E13

- Location: Additional Discussion
- Quote: "I am also not advocating for the failure mode of only trying low-variance ideas, or of avoiding projects that lack an obviously promising approach."
- Key point: De-risking does not mean only pursuing safe ideas; being able to rule out ideas systematically is exactly what lets you try ideas with a low chance of success.

### E14

> Withdrawn: duplicates [E5](#e5) (the quote is fully contained in E5).

- Location: A further improvement: opening up the "task" black box
- Quote: "Specifically, for each task we want a cheap way to obtain high confidence about whether that task will be feasible. This is called "de-risking"."
- Key point: Definition of de-risking: for each task, find a cheap way to determine, quickly and with high confidence, whether it is feasible.

### E15

> Withdrawn: duplicates [E5](#e5) (the quote is fully contained in E5).

- Location: A further improvement: opening up the "task" black box
- Quote: "De-risk all components (to the extent feasible), then execute."
- Key point: The basic pattern: de-risk all the parts first, then execute for real.

### E16

- Location: Caveats
- Quote: "You can get better at this within a few weeks by estimating completion times for each task and then recording the actual completion times in a daily log. You should also practice decomposing tasks into small actionable chunks, each taking roughly 20 minutes to 2 hours."
- Key point: Estimating time can be practiced: estimate each task's time beforehand, then record the actual time in a daily log; also practice breaking tasks into chunks of 20 minutes to 2 hours.

### E17

> Withdrawn: duplicates [E8](#e8) (the quote is fully contained in E8).

- Location: Some further practical ideas
- Quote: "More generally, thinking about simplified instances of a problem is often useful."
- Key point: Thinking about simplified versions of the problem is usually very useful and helps suggest or rule out approaches.

### E18

- Location: Some further practical ideas
- Quote: "Running simulations. If we wish to prove X, first run simulations to check if X is actually true."
- Key point: Theoretical work can also be de-risked: before trying to prove X, run simulations to check whether X actually holds.

### E19

> Withdrawn: duplicates [E9](#e9) (the quote is fully contained in E9).

- Location: Exponentially branching search trees
- Quote: "Whenever something doesn't work, I ask why it didn't work."
- Key point: Ask why each failure happened, so you do not keep trying approaches that fail for the same reason.

### E20

> Withdrawn: duplicates [E10](#e10) (the quote is fully contained in E10).

- Location: Exponentially branching search trees
- Quote: "However, if X is a high-level conceptual approach, then a more correct conclusion is "I tried an implementation comprising 0.1% of the possible implementations of X, and observed that that particular implementation did not work"."
- Key point: A failed experiment only shows that "this one implementation" does not work; it cannot be equated with "this idea" not working.

### E21

- Location: Exponentially branching search trees
- Quote: "In the past, I have spent months trying different approaches to a problem before finally stepping back and realizing that they were all failing for the same reason."
- Key point: The author once spent months trying different approaches before stepping back and realizing they all failed for the same reason.

### E22

- Location: Additional Discussion
- Quote: "When ruling out ideas, it is important to hold oneself to a high standard. "This doesn't seem like it will work" or "I feel less motivated after trying a few things along this line that didn't work" are not ruling out an idea."
- Key point: Hold a high bar for ruling out an idea; "it doesn't seem to work" or "I tried a few times and lost steam" does not count as truly eliminating it.

### E23

> Withdrawn: duplicates [E12](#e12) (the quote is fully contained in E12).

- Location: Summary
- Quote: "We often try easier tasks first, when instead we should try the most informative tasks first."
- Key point: People often do the easy tasks first, when they should do the most informative tasks first.

### E24

- Location: Some further practical ideas
- Quote: "For empirical work, measuring "ceilings" (an upper bound of how high performance could possibly be) is often useful." / "we can easily substitute a "cheating" version of that component (e.g. by looking at the test set or by using information that won't be available at deployment time)" / "Together with ceilings, they delineate a range of possible performance, which helps us interpret our core results."
- Key point: In empirical work it is often useful to measure an "upper bound" (how good performance could possibly be), for example by first replacing the hard-to-implement part with a "cheating" version (peeking at the test set, or using information unavailable at deployment); together with the baseline, the upper bound marks the range where performance could fall and helps interpret the core results.
