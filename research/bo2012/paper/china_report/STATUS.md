# China Report Adaptation｜STATUS

更新时间：2026-10-08

## 当前状态
**CR-S09 PACKAGE BUILT / AWAITING AUTHOR METADATA & EDITOR POLICY DECISION**

## 已完成

- CR-S00：官方要求、Gap Analysis、SOP
- CR-S01：英文标题、150–200词 structured abstract、6 keywords、positioning memo
- CR-S02：China Report 主文架构与旧稿映射
- CR-S03：主文图表/Supplement 拆分
- CR-S04：英文 Research Article 全文适配
- CR-S05：China political economy 文献、Chicago 引用、引用双向审计
- CR-S06：双盲匿名化审计与匿名数据包设计
- CR-S07：Title Page / declarations / AI disclosure / Cover Letter 模板
- CR-S08：desk review + China political economy / quantitative / regional reviewer 模拟审稿
- CR-S09：投稿文件制作、Word 渲染 QA、匿名 metadata 检查、复现包构建

## 当前文章

**Title**  
Political Network Shocks and Local Economic Vulnerability: Evidence from Dalian after 2012

**Article type**  
Research Article

**Core argument**  
The macroeconomic consequences of political-network shocks are conditional on local structural vulnerability.

## 最终主文结构

1. Introduction
2. Political Networks and Local Economic Vulnerability in China
3. Dalian, the 2012 Shock, and Research Design
4. Regional Slowdown and Dalian's Relative Decline
5. From Industrial Earnings Deterioration to Credit Weakening
6. What Did Not Collapse: Public Resources and External Capital
7. Chongqing and the Conditional Effect of Political Shocks
8. Discussion and Limitations
9. Conclusion

主文：约 8,000 words（含表格与 captions）  
Abstract：150–200 words 内  
Keywords：6  
Figures：5 个独立 EPS  
Tables：3 个正文 Word 真表格

## CR-S08 审稿结论

**Analytical core: READY WITHIN REVIEWED SCOPE**

不需要为了 China Report 再新增一轮大计量。

已锁定的边界：
- 不把 −4.57pp 叫薄熙来因果效应；
- 辽宁只作 nested regional context；
- 武汉/青岛是透明外部 benchmarks，不是 matched controls；
- Chongqing 是 parallel exposed case，不是 same-treatment control；
- 工业收入/利润不是直接 cash flow；
- 贷款是 growth slowdown，不是 stock contraction；
- aggregate credit 无法拆 supply/demand；
- 2014–2015 fiscal evidence 只支持“观察到的正式渠道未断崖”，不支持“和2012前完全一样”。

## CR-S09 已完成的本地投稿文件

- Manuscript_ChinaReport_Anon.docx
- Supplementary_Material.docx
- Figure1.eps … Figure5.eps
- Anonymous_Replication_Package.zip
- Title_Page_TEMPLATE.docx
- Cover_Letter_TEMPLATE.docx

### QA
- 主稿 32 页：逐页渲染检查完成
- Supplement 12 页：逐页渲染检查完成
- Title Page / Cover Letter 模板：逐页检查完成
- DOCX creator / lastModifiedBy：已清空
- reviewer-facing DOCX：无 GitHub username / email / affiliation 残留
- 复现脚本：headline-number validation PASS
- Figures：EPS 结构检查 + raster preview 检查完成

## 尚未完成 / 需要作者确认

### 1. Title Page 实名信息
仍需填写：
- author full name
- affiliation
- city/country
- corresponding-author address
- email
- phone
- ORCID（如有）
- funding
- acknowledgements

这些信息不能推断，必须由作者确认。

### 2. Public GitHub / no-preprint policy
Dalian repo 当前是 public，且此前已有 working manuscript / research materials 可见。

处理原则：
- reviewer-facing manuscript 不链接 GitHub；
- Cover Letter 主动披露既有 public working repository；
- 明确未投 designated preprint server、未正式发表；
- 最终是否接受这类 prior public availability 由编辑判断，不隐瞒。

## Gate

当前不是“无条件 READY_TO_SUBMIT”，而是：

**PACKAGE READY — WAITING FOR AUTHOR METADATA + EDITOR ACCEPTANCE OF PRIOR PUBLIC AVAILABILITY**
