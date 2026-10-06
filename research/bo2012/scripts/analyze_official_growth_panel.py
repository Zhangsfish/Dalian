#!/usr/bin/env python3
"""S02D official-growth multi-control diagnostics.

No p-values or causal labels: one treated city and a tiny control set.
2012 is transition and Qingdao only has an excluded forecast, so main
pre/post arithmetic omits 2012.
"""
from pathlib import Path
import numpy as np
import pandas as pd

R=Path(__file__).resolve().parents[1]
P=R/"data/official_growth_panel_s02d.csv"

def gap_stats(wide, controls, pre, post):
    cm=wide[controls].mean(axis=1)
    gap=wide["大连"]-cm
    return gap.loc[pre].mean(), gap.loc[post].mean()

def main():
    p=pd.read_csv(P)
    w=p.pivot(index="year",columns="region",values="gdp_real_growth_pct")
    pre=[2008,2009,2010,2011]
    post_main=[2013,2014,2015]
    post_ext=[2013,2014,2015,2016]

    cm=w[["武汉","青岛"]].mean(axis=1)
    gap=w["大连"]-cm
    event=(gap-gap.loc[2011])

    rows=[]
    for y in pre+post_ext:
        rows.append({
            "year":y,"dalian_growth":w.loc[y,"大连"],
            "wuhan_growth":w.loc[y,"武汉"],"qingdao_growth":w.loc[y,"青岛"],
            "outside_control_mean":cm.loc[y],"dalian_minus_outside":gap.loc[y],
            "event_gap_vs_2011":event.loc[y],
            "period":"pre" if y<=2011 else ("post_extension" if y==2016 else "post")
        })
    pd.DataFrame(rows).to_csv(R/"outputs/official_growth_event_gaps_reproduced.csv",index=False)

    summaries=[]
    for label,controls in [
        ("Dalian_minus_equal_Wuhan_Qingdao",["武汉","青岛"]),
        ("Dalian_minus_Wuhan",["武汉"]),
        ("Dalian_minus_Qingdao",["青岛"]),
    ]:
        for pname,post in [("2013-2015",post_main),("2013-2016",post_ext)]:
            a,b=gap_stats(w,controls,pre,post)
            summaries.append([label,"2008-2011",pname,a,b,b-a])

    # Trend sensitivity for equal outside control.
    x=np.array(pre,dtype=float); y=gap.loc[pre].to_numpy()
    slope,intercept=np.polyfit(x,y,1)
    for pname,post in [("2013-2015",post_main),("2013-2016",post_ext)]:
        pred=slope*np.array(post)+intercept
        residual=gap.loc[post].to_numpy()-pred
        summaries.append(["outside_gap_linear_pretrend_adjusted","2008-2011",pname,np.nan,np.nan,residual.mean()])

    out=pd.DataFrame(summaries,columns=[
        "comparison","pre_window","post_window","pre_mean_gap_pp",
        "post_mean_gap_pp","post_minus_pre_pp"])
    out["interpretation"]="descriptive_not_causal"
    out.to_csv(R/"outputs/official_growth_summary_reproduced.csv",index=False)

if __name__=="__main__":
    main()
