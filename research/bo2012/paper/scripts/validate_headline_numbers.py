#!/usr/bin/env python3
"""Recompute and validate headline numbers used in the paper."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

def mean(x):
    return float(np.mean(list(x)))

def main():
    g = pd.read_csv(DATA / "official_growth_panel_s02d.csv")
    w = g.pivot(index="year", columns="region", values="gdp_real_growth_pct")
    pre = [2008, 2009, 2010, 2011]
    post = [2013, 2014, 2015]
    out_gap = w["大连"] - w[["武汉", "青岛"]].mean(axis=1)
    main_gap = out_gap.loc[post].mean() - out_gap.loc[pre].mean()
    assert abs(main_gap - (-4.5666666667)) < 1e-8
    assert abs((w["大连"]-w["武汉"]).loc[post].mean() - (w["大连"]-w["武汉"]).loc[pre].mean() - (-4.2166666667)) < 1e-8
    assert abs((w["大连"]-w["青岛"]).loc[post].mean() - (w["大连"]-w["青岛"]).loc[pre].mean() - (-4.9166666667)) < 1e-8

    x = np.array(pre, dtype=float)
    y = out_gap.loc[pre].to_numpy()
    slope, intercept = np.polyfit(x, y, 1)
    residual = out_gap.loc[post].to_numpy() - (slope*np.array(post)+intercept)
    assert abs(residual.mean() - (-2.9916666667)) < 1e-8

    p = pd.read_csv(DATA / "panel_as_reported.csv")
    ln = p[p.region=="辽宁"].set_index("year")["gdp_real_growth_pct"]
    dl_pre = pd.Series({2008:16.5, 2009:15.0, 2010:15.2, 2011:13.5})
    dl_post = pd.Series({2013:9.0, 2014:5.8, 2015:4.2})
    within_pre = mean(dl_pre[y]-ln.loc[y] for y in pre)
    within_post = mean(dl_post[y]-ln.loc[y] for y in post)
    within = within_post - within_pre
    assert abs(within - (-1.45)) < 1e-8
    regional = main_gap - within
    assert abs(regional - (-3.1166666667)) < 1e-8

    re = pd.read_csv(DATA / "real_estate_investment_panel_s03a.csv")
    def row(region, year):
        return re[(re.region==region)&(re.year==year)].iloc[0]
    d13,d14,d15 = row("大连",2013),row("大连",2014),row("大连",2015)
    l13,l14,l15 = row("辽宁",2013),row("辽宁",2014),row("辽宁",2015)
    assert abs((d15.real_estate_investment_100m_cny/d13.real_estate_investment_100m_cny-1)*100 - (-47.5268943)) < 1e-6
    assert abs((l15.real_estate_investment_100m_cny/l13.real_estate_investment_100m_cny-1)*100 - (-44.8331990)) < 1e-6
    assert abs((d15.total_fai_100m_cny/d13.total_fai_100m_cny-1)*100 - (-29.6197959)) < 1e-6
    assert abs((l15.total_fai_100m_cny/l13.total_fai_100m_cny-1)*100 - (-28.8446800)) < 1e-6
    assert abs((d15.real_estate_investment_100m_cny-d13.real_estate_investment_100m_cny)/(d15.total_fai_100m_cny-d13.total_fai_100m_cny)*100 - 42.3650198) < 1e-6
    assert abs((l15.real_estate_investment_100m_cny-l13.real_estate_investment_100m_cny)/(l15.total_fai_100m_cny-l13.total_fai_100m_cny)*100 - 40.4432946) < 1e-6

    cr = pd.read_csv(DATA / "credit_s03c.csv")
    cw = cr.pivot(index="year", columns="region", values="loan_growth_pct")
    assert abs((cw.loc[2014,"大连"]-cw.loc[2014,"辽宁"]) - (-3.441)) < 1e-6
    assert abs((cw.loc[2015,"大连"]-cw.loc[2015,"辽宁"]) - (-3.348)) < 1e-6
    assert abs((cw.loc[2016,"大连"]-cw.loc[2016,"辽宁"]) - (-4.304)) < 1e-6

    fi = pd.read_csv(DATA / "fiscal_resource_audit.csv")
    f14=float(fi[(fi.region=="大连")&(fi.year==2014)].reported_upper_resource_total_100m_cny.iloc[0])
    f15=float(fi[(fi.region=="大连")&(fi.year==2015)].reported_upper_resource_total_100m_cny.iloc[0])
    assert abs((f15/f14-1)*100 - 4.8314547) < 1e-6

    cq = pd.read_csv(DATA / "chongqing_parallel_s03c.csv")
    cq["control"] = cq[["chengdu_gdp_growth_pct","wuhan_gdp_growth_pct"]].mean(axis=1, skipna=True)
    cq["gap"] = cq.cq_gdp_growth_pct-cq.control
    assert abs(cq.loc[cq.period=="pre","gap"].mean()-1.55) < 1e-8
    assert abs(cq.loc[cq.period=="post","gap"].mean()-2.35) < 1e-8

    out = pd.DataFrame([
        ["outside_gap_change_pp", main_gap],
        ["pretrend_residual_pp", residual.mean()],
        ["within_liaoning_change_pp", within],
        ["regional_algebraic_change_pp", regional],
        ["dalian_real_estate_2013_2015_pct", (d15.real_estate_investment_100m_cny/d13.real_estate_investment_100m_cny-1)*100],
        ["liaoning_real_estate_2013_2015_pct", (l15.real_estate_investment_100m_cny/l13.real_estate_investment_100m_cny-1)*100],
        ["credit_gap_2014_pp", cw.loc[2014,"大连"]-cw.loc[2014,"辽宁"]],
        ["credit_gap_2015_pp", cw.loc[2015,"大连"]-cw.loc[2015,"辽宁"]],
        ["upper_fiscal_growth_2014_2015_pct", (f15/f14-1)*100],
        ["chongqing_pre_gap_pp", cq.loc[cq.period=="pre","gap"].mean()],
        ["chongqing_post_gap_pp", cq.loc[cq.period=="post","gap"].mean()],
    ], columns=["metric","value"])
    dest = ROOT / "paper" / "validation"
    dest.mkdir(parents=True, exist_ok=True)
    out.to_csv(dest/"headline_numbers.csv", index=False)
    print(out.to_string(index=False))

if __name__ == "__main__":
    main()
