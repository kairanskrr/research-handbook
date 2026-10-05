# Sandve 等人 2013：Ten Simple Rules for Reproducible Computational Research

- 资料：`sandve2013ten`，本地 PDF `papers/pdf/sandve2013ten.pdf`
- 版本：PLoS Computational Biology 9(10): e1003285, 2013，开放获取

### E1

- 位置：引言
- 原文："We want to emphasize that reproducibility is not only a moral responsibility with respect to the scientific field, but that a lack of reproducibility can also be a burden for you as an individual researcher."
- 要点：可复现不只是对学术界的道德责任；做不到可复现，也会给研究者自己带来负担。

### E2

- 位置：Rule 1
- 原文："For Every Result, Keep Track of How It Was Produced" / "As a minimum, you should at least record sufficient details on programs, parameters, and manual procedures to allow yourself, in a year or so, to approximately reproduce the results."
- 要点：每个结果都要记录它是怎么得到的；最低要求是：一年后你自己还能大致重现。

### E3

- 位置：Rule 2、Rule 7、Rule 9（规则标题）
- 原文："Avoid Manual Data Manipulation Steps" / "Always Store Raw Data behind Plots" / "Connect Textual Statements to Underlying Results"
- 要点：避免手工改数据；保存每张图背后的原始数据；论文里的每个陈述都要能对应到具体结果。

### E4

- 位置：Rule 4
- 原文："Version Control All Custom Scripts" / "This can cast doubt on previous results, as it may be impossible to know if they were partly the result of a bug or otherwise unfortunate behavior."
- 要点：所有自写脚本都要做版本控制；否则回不到产生某个结果的代码状态，就无法判断结果是否来自程序错误。

### E5

- 位置：Rule 6（规则标题）
- 原文："For Analyses That Include Randomness, Note Underlying Random Seeds"
- 要点：分析中有随机性时，记录随机种子。

### E6

- 位置：Rule 10
- 原文："Provide Public Access to Scripts, Runs, and Results" / "Making reproducibility of your work by peers a realistic possibility sends a strong signal of quality, trustworthiness, and transparency."
- 要点：公开脚本、运行记录和结果；让同行真的能复现，是质量、可信和透明的有力信号。

### E7

- 位置：Rule 1: For Every Result, Keep Track of How It Was Produced
- 原文："Whenever a result may be of potential interest, keep track of how it was produced."
- 要点：只要一个结果可能有用，就记下它是怎么得到的。

### E8

- 位置：Rule 1
- 原文："For every involved step, you should ensure that every detail that may influence the execution of the step is recorded. If the step is performed by a computer program, the critical details include the name and version of the program, as well as the exact parameters and inputs that were used."
- 要点：每一步中可能影响结果的细节都要记录；如果由程序执行，关键是程序名和版本，以及确切的参数和输入。

### E9

- 位置：Rule 1
- 原文："As a minimum, you should at least record sufficient details on programs, parameters, and manual procedures to allow yourself, in a year or so, to approximately reproduce the results."
- 要点：最低要求：记录足够的细节，让一年后的你自己能大致重现结果。

### E10

- 位置：Rule 2: Avoid Manual Data Manipulation Steps
- 原文："If manual operations cannot be avoided, you should as a minimum note down which data files were modified or moved, and for what purpose."
- 要点：避免不了手工操作时，至少记下改动或移动了哪些数据文件、为什么。

### E11

- 位置：Rule 4 与 Rule 6（规则标题）
- 原文："Version Control All Custom Scripts [...] For Analyses That Include Randomness, Note Underlying Random Seeds"
- 要点：自写脚本都要做版本控制；分析中有随机性时，记录随机种子。

### E12

- 位置：Rule 9: Connect Textual Statements to Underlying Results
- 原文："As a minimum, you should provide enough details along with your textual interpretations so as to allow the exact underlying results, or at least some related results, to be tracked down in the future."
- 要点：写下的每条结论，都要附上足够信息，让将来能找回它所依据的确切结果。
