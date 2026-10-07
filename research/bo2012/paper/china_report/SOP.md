# SOP｜China Report 投稿适配

项目：Dalian / Bo2012  
目标：把当前中文工作论文改成可提交 China Report 的英文 Research Article。  
原则：**一次只推进一个 Gate；每个 Gate 都留下可审计产物；不在适配阶段无边界新增计量。**

---

## CR-S00｜冻结期刊要求与目标定位

### 输入
- China Report 官方 Submission Guidelines
- SAGE AI policy
- 当前 MANUSCRIPT.md

### 产物
- `00_REQUIREMENTS.md`
- `01_GAP_ANALYSIS.md`
- 本 SOP

### Gate
- [x] Article type = Research Article
- [x] 普通发表费用 = 0
- [x] Double-anonymized
- [x] Abstract = structured 150–200 words
- [x] Keywords = 5–6
- [x] Chicago style
- [x] Figures separate, 300 dpi
- [x] No preprints
- [x] Title page / declarations / data availability required
- [x] AI-use disclosure纳入提交包
- [x] 论文定位改为 political network shocks × local vulnerability

**状态：COMPLETE**

---

## CR-S01｜重定论文问题与叙事

### 目标
把“薄熙来是否导致大连失速”改成更适配 China Report 的一般性问题：

> Why do political network shocks produce different economic outcomes across localities?

Dalian = 主案例  
Liaoning = regional exposure  
Chongqing = parallel treated case

### 需要完成
1. 锁定英文标题；
2. 写 150–200 words structured abstract v1；
3. 锁定 5–6 keywords；
4. 写一页 positioning memo：
   - puzzle
   - argument
   - contribution
   - evidence
   - why China Report
5. 明确 Bo Xilai 在题目中的位置：正文核心背景，不放主标题。

### Gate
编辑只看 title + abstract + introduction 第一页时，能读出：
- 一般性研究问题；
- China-specific relevance；
- 条件性政治经济机制；
- 大连不是纯人物案例。

**未开始**

---

## CR-S02｜重构主文架构

### 建议 China Report 主文结构

1. Introduction
2. Political Networks and Local Vulnerability in China
3. Dalian, the 2012 Shock and Research Design
4. Regional Slowdown and Dalian’s Relative Decline
5. From Industrial Cash Flow to Credit Contraction
6. What Did Not Collapse: Fiscal and Project Resources
7. Chongqing and the Conditional Effect of Political Shocks
8. Discussion
9. Conclusion

### 核心动作
- 把纯 econometric diagnostics 从主文移到 Supplement；
- 把重庆前移并提高理论地位；
- 将“地产→二产利润→NPL→credit”做成主机制链；
- 对日结构保留为 alternative / slow-moving mechanism；
- 删除重复的 identification disclaimers。

### Gate
- 主文每一节都有一个明确的 substantive question；
- 无一节只是为了展示一个方法；
- 主文不需要读 Supplement 才能理解主要结论。

**未开始**

---

## CR-S03｜图表瘦身与 Supplement 拆分

### 主文目标
控制在约 6–8 个核心图表组合。

### Main text
- GDP / outside-vs-regional comparison
- Real-estate / FAI path
- Sector + industrial cash flow
- Credit + NPL
- Visible-resource continuity
- Chongqing comparison

### Supplement
- pretrend extrapolation
- all window sensitivity
- SCM feasibility
- detailed Japan table
- detailed fiscal definitions
- source audit
- replication tables

### 技术要求
- 图连续编号；
- 300 dpi 或合格矢量转换；
- 独立文件上传；
- 英文图题、轴、注释；
- 黑白打印仍可区分；
- 主文图注自足。

### Gate
- 任意一张主图都有明确论文任务；
- 没有“为了证明我们做了很多分析”的图。

**未开始**

---

## CR-S04｜英文适配稿 v1

### 原则
**不是逐句翻译。**

要做：
- academic English rewrite；
- China Report 读者默认懂中国，但不默认懂大连；
- 第一次出现的本土制度概念要解释；
- econometric jargon 降低；
- 保留数字和识别诚实性。

### 工作目标
- 主文约 7,000–8,500 words（内部目标，不是期刊硬限）；
- abstract 150–200 words；
- 5–6 keywords；
- title < 50 words（SAGE general checklist）。

### Gate
- 英文读起来像一篇原生英文 China studies 论文；
- 不出现中式直译句法；
- 不用 defensive prose 推进逻辑。

**未开始**

---

## CR-S05｜文献与 Chicago style

### 任务
1. 补 China Report / China studies 文献；
2. 所有正文 citation 与 reference 一一核对；
3. 全部改 Chicago；
4. 政府网页、统计公报、JETRO、新闻材料统一格式；
5. 添加 access date 规则；
6. 移除无法核验或不必要的二手网页。

### Gate
- citation-reference 双向检查 100%；
- 没有混合 APA / Harvard / Chicago。

**未开始**

---

## CR-S06｜匿名化与 Supplement package

### 主稿
- 删除作者名、单位、邮箱；
- 删除可识别 GitHub username；
- 删除自我指称；
- 文件名不含作者姓名。

### Supplement
制作匿名目录：
- data/
- code/
- figures/
- source_notes/
- README_ANON.md

避免：
- git metadata
- GitHub username
- 本地用户名路径
- commit hash 中的身份线索
- acknowledgements/funding等识别信息

### Gate
一个陌生审稿人从所有上传文件中无法反推出作者身份。

**未开始**

---

## CR-S07｜Title Page / Declarations / Cover Letter

### Title Page
- title
- authors
- affiliations
- corresponding author
- acknowledgements
- Statements and Declarations
- funding
- conflict
- ethics
- consent
- data availability
- AI-use disclosure

### Cover Letter
只回答三件事：
1. 这篇文章研究什么；
2. 为什么适合 China Report；
3. 核心新发现是什么。

不要：
- 夸大因果；
- 说“这是第一篇”除非能证实；
- 解释过多技术细节。

### Gate
投稿系统所需信息全部可以复制粘贴。

**未开始**

---

## CR-S08｜模拟 desk review + reviewer audit

### Editor check
- scope
- title
- abstract
- contribution
- readability
- excessive technicality
- sensitivity / political framing

### Reviewer check
重点模拟三类 reviewer：
1. China political economy
2. regional/urban economics
3. quantitative methods

### 必须回答
- Why Dalian?
- Why 2012?
- Why Wuhan/Qingdao?
- Why is Liaoning informative?
- What does Chongqing add?
- What exactly is the political-network mechanism?
- What would falsify the argument?
- Which claim is causal and which is descriptive?

### Gate
没有 P0/P1 逻辑问题；剩余问题只是可讨论的研究限制。

**未开始**

---

## CR-S09｜Submission package final preflight

### 上传文件
- anonymized manuscript .docx
- title page .docx
- figures separate
- supplement
- cover letter
- required declaration data

### 最终检查
- structured abstract 150–200 words
- 5–6 keywords
- Chicago references
- figures numbered / 300 dpi
- double anonymized
- no preprint conflict
- no fees / no OA selected
- ORCID prepared
- AI disclosure consistent with SAGE policy

### Gate
**READY_TO_SUBMIT**

---

# 当前执行顺序

只做下一项：

> **CR-S01：重定题目、Abstract、Keywords、Positioning Memo。**

CR-S01 完成并审计后，才进入结构重写。