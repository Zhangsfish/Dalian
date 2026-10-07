#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
R=Path(__file__).resolve().parents[1]
def main():
    d=pd.read_csv(R/'data/chongqing_parallel_s05a.csv')
    post=d[d.period=='post']
    assert post.gdp_real_growth_pct.min()>=10.7
    assert post.fai_growth_pct.dropna().min()>=12.1
    assert d.loc[d.year==2012,'loan_growth_pct'].iloc[0]>=18.0
    assert d.loc[d.year==2014,'loan_growth_pct'].iloc[0]>=14.0
    assert d.loc[d.year==2015,'loan_growth_pct'].iloc[0]>=11.0
    # Smooth deceleration is not proof of zero treatment effect.
    out=pd.DataFrame({
      'year':d.year,
      'gdp_growth_pct':d.gdp_real_growth_pct,
      'loan_growth_pct':d.loan_growth_pct,
      'fai_growth_pct':d.fai_growth_pct
    })
    out.to_csv(R/'outputs/chongqing_parallel_path_s05a.csv',index=False)
if __name__=='__main__':
    main()
