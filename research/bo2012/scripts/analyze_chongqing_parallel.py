#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

R=Path(__file__).resolve().parents[1]
d=pd.read_csv(R/'data/chongqing_parallel_s03c.csv')
d['control_mean']=d[['chengdu_gdp_growth_pct','wuhan_gdp_growth_pct']].mean(axis=1,skipna=True)
d['gap_pp']=d['cq_gdp_growth_pct']-d['control_mean']
d[['year','cq_gdp_growth_pct','control_mean','gap_pp','period']].to_csv(
    R/'outputs/chongqing_relative_gap.csv',index=False
)
pre=d.loc[d.period=='pre','gap_pp'].mean()
post=d.loc[d.period=='post','gap_pp'].mean()
print({'pre_gap':pre,'post_gap':post,'change':post-pre})
