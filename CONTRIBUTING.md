# 贡献规则

## 仓库的两部分

- **原始资料**：`sources/`（资料列表和证据摘录）、`papers/`、`repos/`。只登记和摘录，不加工。
- **整理内容**：`guide/`，我们写给科研新手的手册正文。每条事实都要能在原始资料中找到证据。

## 基本原则

1. **每条内容都要注明出处**。没有出处的事实不要写。本项目自己的分析和建议不挂脚注，也不另加标记（写法见下文"怎么写"）。
2. **不复制受版权保护的全文或 PDF**。用自己的话概括，必要时可以简短引用并注明出处。PDF 只保存在本地的 `papers/pdf/`（已加入 `.gitignore`），只有开放许可的论文才可以提交。
3. **不确定就标"待确认"**，不要猜测。
4. 用中文撰写；资料标题、术语和文件名保留英文。

## 添加一篇论文

1. 核实标题、作者、出处和 DOI（打开原始页面确认）。
2. 在 `papers/references.bib` 中添加条目。无法核实的 DOI 不要写，在 `note` 中说明。
3. 在 `papers/README.md` 的表格中添加一行，注明免费全文的来源；付费的放进"待获取"。
4. 如果有合法的免费全文，在 `scripts/fetch_papers.sh` 中添加下载地址。
5. 在 `sources/README.md` 的对应分类下添加条目，格式为：

   ```
   - [标题](https://原文地址) - 作者，出处 年份。一句话说明用途。🆓 `bibtex-key`
   ```

## 添加一个 GitHub 仓库

1. 确认仓库确实存在、有实际内容，并记下许可证。
2. 在 `repos/README.md` 中记录上游地址、固定版本（当前默认分支的完整 commit hash）、提交日期和许可。
3. 在 `sources/README.md` 的对应分类下添加条目，注明许可和更新情况（例如长期未更新）。

## 写整理内容

### 新内容放在哪里

读法见 [`guide/00_start-here/how-to-use.md`](guide/00_start-here/how-to-use.md)。简单说：

| 内容 | 放在哪里 |
|---|---|
| 找题目阶段要想清楚什么、做出什么（进入领域、找问题、探索、筛选、收敛） | 第一部分 · 想到一个好题目：`guide/01_find-a-problem/`，按章节模板写（计划 §6） |
| 把题目做出来要想清楚什么、做出什么（证据、方法、计划、效度、试验、执行、分析、决策点） | 第二部分 · 把它做出来：`guide/02_do-the-project/`，按章节模板写 |
| 一类研究产生什么知识、需要什么证据、常用哪些方法、哪些学科常用 | 为什么（研究套路）：`guide/05_research-strategies/` |
| 一种具体做法怎么做好，而且两个及以上学科在用 | 研究类型里的通用方法：`guide/06_methods/`，并在 `guide/06_methods/README.md` 的对照表里加一行 |
| 只有一个学科使用的研究实践 | 该学科的 `practices/`（如 `guide/07_fields/computer-science/practices/`）；它在导航里和通用方法一起归入研究类型，也要在 `guide/06_methods/README.md` 的对照表里加一行 |
| 某个学科、某个社区特有的规矩 | 学科篇：`guide/07_fields/<学科>/README.md`。只写学科特有的内容，通用方法链接到 `guide/06_methods/` |
| 不属于某个阶段、一直要面对的事（计划、材料、合作、诚信、心态） | 贯穿全程：`guide/08_throughout/` |

研究方法和学科实践的文档可以用 [`templates/research-type.md`](templates/research-type.md) 模板。

### 怎么写

1. **说人话。** 用中文、短句、第二人称，从读者此刻的困惑开始；先给做法，再说为什么。术语和 [`guide/00_start-here/key-concepts.md`](guide/00_start-here/key-concepts.md) 一致，缩写第一次出现时写出全称。
2. **事实逐句挂脚注。** 某位作者的建议、某项研究的发现、某个规范的要求、数字，每句都挂脚注，指向 `sources/notes/<key>.md` 中的一条证据，而且那条证据的原文要真的支持这句话。还没有摘录的资料，先按 [`sources/notes/README.md`](sources/notes/README.md) 的格式补上。
3. **我们综合的建议直接写，不挂脚注，也不加标记。** 做法表格、判断规则、例子这类没有哪份资料逐字这样说的内容，读者靠"没有脚注"认出它们是本手册的话；同一段里夹着的事实仍然单独挂脚注。有两种情况要用文字写明：我们的推论紧跟在引文后面、读者可能以为是资料的意思时，写"由此看""本手册的建议是"之类；对某份资料本身下判断时（例如"该文没有讨论效度威胁"），写明这是本手册通读全文后的判断。
4. **不确定的标 `[待确认]`**；找不到可靠依据的，直接写"本文资料未涉及"，不要凭印象写。
5. **"不同的看法"只在分歧影响操作时写**：并列写出各自的做法和理由，再给一段本手册的实际操作建议，不要强行合成一个结论。
6. **写明出处来自哪个领域。** 不要把计算机、软件工程或机器学习的做法写成所有学科的规律。

### 写完后更新目录页

新增或改动了章节、方法、学科篇，同时更新所在的目录页：两部分的章节见仓库首页 [`README.zh.md`](README.zh.md) 的目录，研究套路见 [`guide/05_research-strategies/README.md`](guide/05_research-strategies/README.md)，研究类型（通用方法和各学科独有的实践）见 [`guide/06_methods/README.md`](guide/06_methods/README.md)，学科篇和各学科独有的实践，还要更新 [`guide/07_fields/README.md`](guide/07_fields/README.md)，贯穿全程见 [`guide/08_throughout/README.md`](guide/08_throughout/README.md)。

## 许可说明

- ACM SIGSOFT Empirical Standards 采用 CC0 1.0，可以自由引用和改编，但仍需注明出处。
- 其他资料各有版权或许可，见 `repos/README.md` 和 `papers/README.md`。
