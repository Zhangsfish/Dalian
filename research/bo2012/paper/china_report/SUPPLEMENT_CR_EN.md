# Supplementary Material

## Political Network Shocks and Local Economic Vulnerability: Evidence from Dalian after 2012

This supplement documents data construction, robustness checks, detailed mechanism series and reproducibility information that are intentionally kept out of the main article. It should be read as supporting material for a structured observational case study, not as a separate causal-identification exercise.

---

# Appendix A. Data Sources, Definitions and Statistical Vintages

## A1. Core source types

The analysis combines:

- annual statistical bulletins for Dalian, Liaoning, Wuhan, Qingdao, Chongqing and Chengdu;
- local budget-execution reports and Ministry of Finance materials;
- People's Bank of China local financial materials;
- State Council and National Development and Reform Commission policy approvals;
- JETRO reports on Japanese investment in Dalian and China;
- official leadership biographies and project announcements.

Each extracted observation is linked to a source ID in the project source ledger. The anonymized peer-review package contains the source title, issuing institution, publication date, stable public URL, variable extracted and any comparability note.

## A2. Contemporaneous versus revised data

The main analysis uses annual **real-GDP growth rates as reported contemporaneously** in each year's official bulletin. Historical nominal GDP levels are more vulnerable to non-synchronous revisions associated with economic censuses and later unified-accounting changes. For that reason, historical level data are not used to construct the main post-2012 counterfactual.

The year **2012** is treated as a transition year because the political event occurred in March and annual data cannot separate pre- and post-event months. It is shown in annual trajectories but excluded from the main pre/post means.

The year **2016** is retained as a sensitivity year rather than part of the principal regional window. Dalian and Liaoning reported unusually large discontinuities in fixed-asset investment and historical GDP records around this period. Liaoning also publicly acknowledged that some cities and counties had fabricated fiscal-revenue data during 2011-2014. This episode concerned fiscal data and is not proof that the real-GDP growth rates used in the article were fabricated; it nevertheless motivates conservative interpretation of provincial aggregates.

## A3. Variable definitions

- **Real-GDP growth:** official annual comparable-price growth rate.
- **Fixed-asset investment (FAI):** contemporaneous official measure; scope changes are preserved in source notes.
- **Real-estate development investment:** official annual development-investment measure.
- **Bank-loan growth:** reported rate where available; otherwise derived from year-end balance and comparable annual increment.
- **NPL ratio:** reported non-performing-loan ratio.
- **Industrial revenue/profit:** above-scale industrial main-business revenue and total profit. These are operating-performance indicators, not direct cash-flow measures.
- **Formal upper-level fiscal resources:** only tax rebates, general transfers, special transfers or upper-level appropriations explicitly reported in budget documents.
- **Japanese exposure:** JETRO-reported new-project counts and actual investment; 2015 carries a methodology-break warning.

---

# Appendix B. External-Benchmark Robustness

## B1. Baseline and single-benchmark comparisons

**Supplementary Table S1. Relative real-GDP growth-gap results**

| Comparison | Pre mean gap, 2008-2011 (pp) | Post mean gap, 2013-2015 (pp) | Change (pp) |
|---|---:|---:|---:|
| Dalian vs Wuhan-Qingdao equal mean | +1.8000 | -2.7667 | **-4.5667** |
| Dalian vs Wuhan | +1.0500 | -3.1667 | **-4.2167** |
| Dalian vs Qingdao | +2.5500 | -2.3667 | **-4.9167** |
| Dalian vs Liaoning | +1.9500 | +0.5000 | **-1.4500** |

The external reversal is therefore not driven by either Wuhan or Qingdao alone. The Dalian-Liaoning comparison has a different role: it is a nested regional benchmark and is not treated as an independent untreated control.

## B2. Pre-event relative trend

The Dalian-minus-Wuhan-Qingdao gap was +2.35 pp in 2008, +2.05 in 2009, +1.40 in 2010 and +1.40 in 2011. A linear fit over these four pre-event observations implies expected gaps of approximately +0.58 pp in 2013, +0.23 in 2014 and -0.13 in 2015.

Observed gaps were -1.00, -3.05 and -4.25 pp. The average observed-minus-extrapolated residual for 2013-2015 is approximately **-2.99 pp**.

This is a sensitivity exercise, not a credible standalone counterfactual: four pre-event observations are insufficient to establish a structural trend.

## B3. Extended post window

Including 2016 in the external comparison leaves the main direction unchanged:

- post 2013-2016 mean external gap: approximately -2.41 pp;
- pre/post change: approximately **-4.21 pp**.

The principal article nevertheless stops the regional accounting at 2015 because 2016 is unusually discontinuous in Liaoning and Dalian investment/statistical records.

## B4. Pseudo-event check

Using 2010 as a pseudo break:

- 2008-2009 mean external gap: approximately +2.20 pp;
- 2010-2011 mean external gap: approximately +1.40 pp;
- change: approximately -0.80 pp.

The gradual pre-event narrowing is materially smaller than the 2013-2015 reversal.

---

# Appendix C. Regional Investment Accounting

## C1. Real-estate share of fixed investment

**Supplementary Table S2. Dalian and Liaoning investment structure**

| Metric | Dalian | Liaoning |
|---|---:|---:|
| Real-estate share of FAI, 2013 | 26.40% | 26.02% |
| Real-estate share of FAI, 2014 | 21.10% | 21.70% |
| Real-estate share of FAI, 2015 | 19.69% | 20.17% |
| FAI decline, 2013-2015 | RMB 191.88bn | RMB 715.10bn |
| Real-estate investment decline, 2013-2015 | RMB 81.29bn | RMB 289.21bn |
| RE decline / FAI decline, 2013-2015 | 42.37% | 40.44% |
| RE decline / FAI decline, 2014-2015 | 24.02% | 25.68% |

The accounting ratios are descriptive. They are not causal contribution shares.

The 2014-2015 values are particularly useful: only about one quarter of the nominal fall in total FAI is mechanically accounted for by the decline in real-estate development investment, showing that the contraction had broadened beyond property.

## C2. Transition-year land and fiscal stress

In 2012:

- Dalian government-fund revenue fell **56.3%**;
- Dalian municipal land-sale revenue fell **45.4%**;
- Liaoning government-fund revenue fell **28.7%**.

These values indicate that land- and property-related fiscal stress was already visible in the event year. They do not establish whether the weakness began before or after March 2012.

---

# Appendix D. Credit, Asset Quality and Financing Structure

## D1. Loan-growth series

**Supplementary Table S3. Bank-loan growth (%)**

| Year | Dalian | Liaoning | Dalian minus Liaoning (pp) |
|---|---:|---:|---:|
| 2011 | 16.318 | 17.248 | -0.930 |
| 2012 | 15.071 | 15.173 | -0.102 |
| 2013 | 11.558 | 12.764 | -1.206 |
| 2014 | 7.404 | 10.845 | -3.441 |
| 2015 | 6.471 | 9.819 | -3.348 |
| 2016 | 2.319 | 6.623 | -4.304 |

Dalian's relative credit weakness therefore becomes more pronounced after 2013.

## D2. Asset quality

Dalian NPL ratios:

- 2013: **1.07%**
- 2014: **1.86%**
- 2015: **2.16%**
- 2016: **3.22%**

The NPL path is consistent with deteriorating borrower/project quality, but aggregate annual data cannot establish the direction of causality between lending and real activity.

## D3. New-loan share

Dalian's share of the Liaoning-wide annual bank-loan increment fell from approximately:

- **31.4%** in 2013
- **23.4%** in 2014
- **21.9%** in 2015
- **11.1%** in 2016.

## D4. Private investment

In 2014 private investment grew:

- Dalian: **2.4%**
- Wuhan: **16.1%**
- Qingdao: **24.0%**

This provides a non-bank indicator of weakening local investment appetite.

## D5. Financing segmentation

**Supplementary Table S4. Selected financing measures**

| Year | Bank-loan increment (RMB bn) | Capital-market financing (RMB bn) | Interpretation |
|---|---:|---:|---|
| 2014 | 75.55 | 103.08 | Direct-financing scale remained substantial |
| 2015 | 70.99 | 117.20 | Bank increment weakened while direct finance increased |
| 2016 | 26.75 | 141.68 | Large divergence between bank increment and reported market financing |

The bank-loan increment and capital-market financing variables have different definitions and cannot be added, divided into causal substitution shares or interpreted as directly interchangeable flows.

## D6. Identification boundary: credit supply versus demand

The available city-level aggregate data do not separate:

1. banks becoming less willing to lend, from
2. firms becoming less willing or able to borrow as investment returns deteriorate.

No consistent city-level panel of application rates, rejection rates, borrower categories or loan prices was recovered. The article therefore refers to **weaker bank-credit growth/conditions**, not an identified pure credit-supply contraction.

---

# Appendix E. Japanese Exposure

**Supplementary Table S5. Japanese investment and project entry**

| Indicator | 2012 | 2013 | 2014 | 2015 |
|---|---:|---:|---:|---:|
| Japanese new projects in Dalian | 136 | 75 | 61 | 47 |
| Actual Japanese FDI in Dalian (US$ mn) | — | 2,627.46 | 2,535 | 147* |
| Japanese FDI share of Dalian FDI | — | 19.3% | 18.1% | 5.4%* |

* JETRO reports a methodology change in 2015; absolute amounts should not be chained mechanically to earlier years.

From 2012 to 2015, new Japanese project entry fell about **65.4%**. However, actual Japanese investment fell only **3.5%** in 2014, compared with a **38.8%** decline in Japanese FDI into China nationally under Chinese statistics.

Interpretation: Dalian's Japanese growth engine was maturing, but the timing is more consistent with a slow-moving structural headwind than a discrete 2014 withdrawal shock.

---

# Appendix F. Formal Public Resources, Leadership and Major Projects

## F1. Comparable fiscal transfers

The clean comparable fiscal series begins in 2014.

- 2014 central/provincial tax rebates and transfers: **RMB 18.897bn**
- 2015: **RMB 19.810bn**
- nominal change: approximately **+4.83%**

Earlier reports use different fiscal classifications. These figures therefore do **not** establish that Dalian received the same level of fiscal support before and after 2012. They establish only that the observable comparable budgetary channel did not collapse during the key 2014-2015 slowdown.

## F2. Leadership continuity

- Municipal party secretary Tang Jun: June 2011-February 2017
- Mayor Li Wancai: May 2009-December 2014

The 2012 political event was not accompanied by an immediate replacement of Dalian's top municipal leadership.

## F3. Selected post-2012 platforms and projects

- **2014:** State Council approval of Jinpu New Area
- **2015:** Intel announced up to US$5.5bn of further investment in the Dalian facility over subsequent years
- **2016:** Dalian included in the national cross-border e-commerce comprehensive pilot programme
- **2017:** Dalian area established within the Liaoning Free Trade Zone

These are evidence of continuity in visible formal platforms and large-project access. They are not measures of the total economic value of political connections.

---

# Appendix G. Synthetic-Control Feasibility Diagnostics

Synthetic control was explored as a pre-fit diagnostic but is not used for the article's main causal inference.

## G1. Pre-treatment fit

Using a strict initial donor set, the best nominal-GDP index fit placed all weight on Yantai and produced a pre-treatment RMSPE of **19.65 index points**.

With an expanded non-Liaoning donor pool:

- Yantai weight: **0.2712**
- Wuhan weight: **0.7288**
- pre-treatment RMSPE: **2.5424**

## G2. Donor sensitivity

**Supplementary Table S6. Expanded-donor leave-out diagnostics**

| Scenario | Pre RMSPE | Main weights |
|---|---:|---|
| Full expanded pool | 2.542 | Yantai 0.271; Wuhan 0.729 |
| Drop Wuhan | 3.873 | Tianjin 0.318; Nantong 0.682 |
| Drop Yantai | 2.878 | Tangshan 0.081; Nantong 0.481; Wuhan 0.438 |
| Drop Wuhan and Yantai | 3.890 | Tianjin 0.318; Nantong 0.682 |

The diagnostics show that a plausible donor space exists. The reason the post-treatment synthetic gap is excluded from the main paper is not a complete absence of donor fit, but the use of historical nominal-GDP series drawn from non-synchronous statistical vintages. A formal synthetic-control estimate would require rebuilding a common-vintage real-output panel.

---

# Appendix H. Replication and Headline-Number Validation

## H1. Headline checks

The replication code recalculates the principal quantities from bottom-level CSV files:

- external relative decline: **-4.5667 pp**
- Wuhan-only: **-4.2167 pp**
- Qingdao-only: **-4.9167 pp**
- Dalian-vs-Liaoning: **-1.4500 pp**
- external linear-pretrend residual, 2013-2015 mean: **-2.9917 pp**
- Dalian 2013-2015 industrial revenue: **+9.7% to -27.4%**
- industrial profit: **+26.1% to -30.7%**
- Dalian NPL: **1.07% to 2.16%**
- comparable fiscal transfers, 2014-2015: **+4.83% nominal**
- Chongqing relative growth advantage: **+1.55 pp pre to +2.35 pp post**

## H2. Files included in anonymized replication package

The reviewer package should contain, without repository metadata or author identifiers:

- core growth data;
- investment and real-estate data;
- sector/industrial operating data;
- bank-credit and NPL data;
- fiscal-resource and project ledgers;
- Japanese-exposure data;
- Chongqing comparison data;
- source ledger;
- headline-number validation script;
- raw data for each submitted figure.

## H3. Reproducibility scope

The package reproduces all headline arithmetic and submitted figures from derived public-source data. It does not redistribute copyrighted source reports in full; instead it provides stable source links and extraction notes.

---

# Supplementary Data-Quality Summary

| Issue | Treatment in paper |
|---|---|
| 2012 event occurs within year | Excluded from main pre/post means |
| Liaoning contains Dalian | Used only as nested regional context |
| Liaoning fiscal-data irregularities | Disclosed; not generalized into an unsupported GDP-fabrication claim |
| 2015 JETRO methodology change | Absolute 2015 FDI not chained to prior years |
| Bank supply vs loan demand | Not separately identified |
| Different direct-finance definitions | Used as scale evidence only, not substitution ratios |
| 2016 Dalian/Liaoning discontinuity | Sensitivity year, not principal regional window |
| SCM historical vintage mismatch | Pre-fit diagnostic only |

