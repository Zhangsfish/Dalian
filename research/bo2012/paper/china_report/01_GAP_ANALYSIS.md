# China Report 适配 Gap Analysis

基准稿：`../MANUSCRIPT.md`  
审计日期：2026-10-08

## 总判断

**FIT：中高。当前稿不能直接翻译投稿，但不需要重做核心研究。**

最需要改的是“文章身份”，不是核心数字：
- 当前稿：偏经济学工作论文 / identification audit。
- China Report 目标稿：China political economy research article。
- 主贡献应从“政治效应有没有被识别”转成：
  **为什么同一类政治网络冲击在不同地方经济结构中产生不同结果。**

## 1. 逐项差距

| 项目 | 当前状态 | China Report 目标 | 差距 |
|---|---|---|---|
| Article type | 工作论文 | Research Article | 小 |
| Title | 含“薄熙来政治失势” | 更概念化、可检索 | 中 |
| Abstract | 中文、非150–200词 structured abstract | 150–200 words structured | 大 |
| Keywords | 7个中文关键词 | 5–6英文具体关键词 | 小 |
| 主叙事 | identification-first | China political economy / mechanism-first | 大 |
| Literature | 偏计量、干部网络 | 需补 China local state / regional political economy | 中 |
| Methods | 技术细节较多 | 主文保留透明方法，细节进补充材料 | 中 |
| Results | 数据丰富 | 基本可保留 | 小 |
| Chongqing | 作为平行案例 | 应升级为“state-dependence”核心证据 | 中 |
| Figures/tables | 主文约13图 + 多表 | 主文压缩到6–8个核心图表 | 大 |
| References | 混合格式 | Chicago | 大 |
| Data appendix | 很完整 | 适合做 supplement | 小 |
| Anonymization | GitHub与文件结构可识别作者 | 完全双盲 | 大 |
| Data availability | 当前公开GitHub | 匿名审稿期不能暴露作者 | 大 |
| Title page | 未制作 | 单独完整Title Page | 大 |
| Declarations | 未制作 | 必须齐全 | 大 |
| AI disclosure | 尚无 | 按SAGE policy披露 | 中 |
| English | 尚未制作正式英文稿 | 学术英语且非逐字翻译 | 大 |
| Preprint risk | GitHub有中文过程稿 | 英文投稿稿不得做preprint | 中 |

## 2. 最重要的内容改造

### 2.1 Introduction
当前 Introduction 已经较干净，但对 China Report 仍偏“经济学论文”。

需要改成：
1. 从一个 China political economy puzzle 开场；
2. Bo Xilai/Dalian 作为具体 case，而不是标题中心；
3. 先提出“political network shock × local vulnerability”；
4. 再介绍多层证据；
5. 不把文章卖点写成“我们不能识别精确ATT”。

### 2.2 Theory / literature
保留：
- Jiang & Zhang
- Li & Zhou
- Jia et al.
- Persson & Zhuravskaya

新增一层：
- 中国地方政府 / local state
- regional restructuring / Northeast decline
- political connections under stress
- local development coalitions / investment-led growth

目标是让编辑一眼看出：
> 这不是一篇“薄熙来八卦 + 数据”，而是在讨论一个更一般的地方政治经济机制。

### 2.3 Methods
主文保留：
- Wuhan/Qingdao outside benchmark
- Liaoning nested comparison
- mechanism comparison
- Chongqing parallel case
- robustness summary

移至 supplement：
- 完整 window sensitivity
- SCM donor diagnostics
- data vintage audit
- 逐条 source ledger
- replication details

### 2.4 Results
核心结果不需要重算。

主文应该压成三段：
1. **Regional shock:** Dalian and Liaoning co-move in real estate, FAI, secondary-sector collapse.
2. **Local amplification:** credit, NPL, private investment weaken more in Dalian.
3. **Visible-resource continuity:** transfers, national platforms, large projects continue.

### 2.5 Chongqing
当前稿里重庆是后置 robustness / mechanism case。

China Report 版建议升级为主论证：
> 同一政治人物网络冲击，在重庆没有复制大连路径。

作用：
- 不是证明 zero effect；
- 是把文章贡献抬到 **conditional / state-dependent political effects**。

### 2.6 Conclusion
不要用“中国经济学论文式”结论：
> political effect is not identified precisely.

要用 China Report 式结论：
> political connections matter conditionally; their macroeconomic consequence depends on the health of local investment regimes, corporate cash flow and credit systems.

## 3. 图表精简建议

### 主文建议保留
1. 大连 vs 武汉/青岛 GDP path
2. 大连 outside gap vs Liaoning nested gap（合并现图2/4）
3. 大连/辽宁房地产与投资路径（合并现图5/6）
4. GDP产业拆分 + 工业收入利润（现图6A）
5. 大连 vs 辽宁 credit / NPL（合并现图7/8）
6. visible resources timeline（财政 + 国家平台，可做一张综合图）
7. 重庆 vs 大连 path（GDP/credit/investment整合）

### Supplement
- pretrend extrapolation
- window sensitivity
- SCM feasibility
- detailed fiscal bars
- all raw mechanism tables
- source ledger

## 4. 现在稿件的优势

1. 数据比 China Report 很多纯定性 political economy 文章更扎实；
2. 有明确 China-specific institutional story；
3. 有 Dalian + Liaoning + external controls + Chongqing 的多层比较；
4. 不是把政治事件硬解释为因果，而是提出条件性机制；
5. 已有完整 reproducibility / source audit，可以直接变成 Supplement。

## 5. 最大的 desk-reject 风险

1. 标题与开头太像“薄熙来个案政治评论”；
2. 方法部分太像弱识别 econometrics paper，编辑会追问“既然不能识别，为什么要看这个”；
3. China studies 文献不足；
4. 图表太多、技术细节太重；
5. 双盲匿名处理不彻底；
6. 英文稿如果只是逐字翻译，会显得生硬。

## 6. 当前判断

**不需要新增大计量才能投 China Report。**

先完成 journal adaptation，再决定是否补新数据。

只有在英文适配后出现以下问题才考虑新增计量：
- 主结论仍然过度依赖 −4.57pp；
- 重庆案例不能支持 conditionality；
- reviewer-style internal audit 认为“political network”证据太间接。

否则不要主动把项目拖回数据无限搜集。
