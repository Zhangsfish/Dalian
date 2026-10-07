# 附录A｜数据、变量与图表来源

## A1. 主要数据文件与原始来源

| 主题 | 论文用途 | 数据文件 | 原始来源 |
|---|---|---|---|
| 实际GDP增速 | 省外基准、趋势、供体剔除 | ../data/official_growth_panel_s02d.csv | 大连、武汉、青岛历年统计公报；2011大连为统计公报镜像并经独立材料交叉核验 |
| 辽宁区域参照 | 区域嵌套分解、窗口敏感性 | ../data/panel_as_reported.csv | 大连与辽宁历年统计公报 |
| 房地产与投资 | 区域投资机制 | ../data/real_estate_land_s03a.csv；../data/real_estate_investment_panel_s03a.csv | 各地统计公报、政府工作报告、辽宁财政资料 |
| GDP产业构成与工业现金流 | 实体利润→信用机制 | ../data/sector_cashflow_supplement.csv | 大连、辽宁2013—2015统计公报；同期金融统计 |
| 银行信贷与不良率 | 信用机制 | ../data/credit_s03c.csv；../data/credit_panel_s03b.csv | 各地统计公报、中国人民银行地方金融资料 |
| 民间投资 | 私人投资机制 | ../data/private_investment_s03c.csv | 大连、武汉、青岛政府/统计资料 |
| 融资结构 | 银行与直接融资分层 | ../data/financing_structure_s03d.csv；../data/financing_substitution_s03c.csv | 大连统计公报、人民银行大连中心支行报告、政府工作报告 |
| 上级财政资源 | 显性公共资源 | ../data/fiscal_resource_audit.csv | 财政部转载的大连预算执行报告 |
| 领导时间线 | 治理连续性 | ../data/leadership_timeline.csv | 人民网干部简历与官方转载 |
| 国家平台/重大项目 | 项目与政策资源 | ../data/major_project_policy_ledger.csv | 国务院、国家发改委、辽宁省政府、企业项目公告 |
| 日本暴露 | 长期结构机制 | ../data/japan_exposure_s03b.csv | JETRO 2013—2015年度对华直接投资报告 |
| 重庆平行案例 | 机制外部比较 | ../data/chongqing_parallel_s03c.csv；../data/chongqing_parallel_s05a.csv | 重庆、成都、武汉统计公报及金融资料 |
| 合成控制可行性 | 事前供体拟合 | ../scripts/scm_nominal_feasibility.py | 二手历史名义GDP聚合序列，仅用于事前供体诊断 |

每条原始观测的完整URL、发布机构、发布日期、原文定位和提取日期见 ../data/sources.csv。

## A2. 主要图表对应关系

| 正文编号 | 文件 | 底层数据 |
|---|---|---|
| 图1 | figures/fig01_growth_paths.svg | official_growth_panel_s02d.csv |
| 图2 | figures/fig02_relative_gap.svg | official_growth_panel_s02d.csv |
| 图3 | figures/fig05_gap_pretrend.svg | official_growth_panel_s02d.csv |
| 图4 | figures/fig06_outside_vs_liaoning_gap.svg | official_growth_panel_s02d.csv + panel_as_reported.csv |
| 图5 | figures/fig07_real_estate_growth.svg | real_estate_investment_panel_s03a.csv |
| 图6 | figures/fig08_investment_index.svg | real_estate_investment_panel_s03a.csv |
| 图6A | figures/fig06A_sector_cashflow.svg | sector_cashflow_supplement.csv |
| 图7 | figures/fig09_credit_growth_gap.svg | credit_s03c.csv |
| 图8 | figures/fig10_npl_ratio.svg | credit_s03c.csv |
| 图9 | figures/fig11_upper_fiscal_resources.svg | fiscal_resource_audit.csv |
| 图10 | figures/fig12_governance_project_timeline.svg | leadership_timeline.csv + major_project_policy_ledger.csv |
| 图11 | figures/fig13_chongqing_relative_gap.svg | chongqing_parallel_s03c.csv |
| 图12 | figures/fig14_chongqing_dalian_paths.svg | chongqing_parallel_s03c.csv + credit_s03c.csv |
| 图13 | figures/fig15_window_sensitivity.svg | panel_as_reported.csv / window_sensitivity.csv |

## A3. 变量与口径

实际GDP增速采用年度统计公报直接报告的可比价格增速。固定资产投资和房地产开发投资保留各年官方统计范围；2011前后固定资产投资统计范围变化在原始字段中单独记录。银行贷款增速优先使用报告值，缺失时由可比年初余额和当年新增额计算，并保留计算口径。财政资源仅使用预算执行报告明确披露的税收返还、一般性转移支付、专项转移支付或上级专项拨款，不以财政支出减本级收入推算。

2012年作为事件过渡年，不进入主前后均值；2016年进入扩展敏感性。对日投资2015年存在JETRO报告注明的统计方法变化，因此正文使用报告同比方向和项目数，并避免把2014与2015绝对金额直接拼接。
