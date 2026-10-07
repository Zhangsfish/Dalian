#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

R=Path(__file__).resolve().parents[1]

def main():
    d=pd.read_csv(R/'data/credit_panel_s03b.csv')
    p=d.pivot(index='year',columns='region',values='loan_growth_pct')
    rows=[]
    for y in [2013,2014,2015]:
        ext=(p.loc[y,'武汉']+p.loc[y,'青岛'])/2
        rows.append({
            'year':y,
            'dalian_growth_pct':p.loc[y,'大连'],
            'liaoning_growth_pct':p.loc[y,'辽宁'],
            'external_mean_wuhan_qingdao_pct':ext,
            'dalian_minus_liaoning_pp':p.loc[y,'大连']-p.loc[y,'辽宁'],
            'dalian_minus_external_pp':p.loc[y,'大连']-ext,
        })
    out=pd.DataFrame(rows)
    out.to_csv(R/'outputs/credit_relative_gaps_s03b.csv',index=False)

    bal=d.pivot(index='year',columns='region',values='loan_balance_100m_cny')
    dl=(bal.loc[2015,'大连']/bal.loc[2012,'大连']-1)*100
    ln=(bal.loc[2015,'辽宁']/bal.loc[2012,'辽宁']-1)*100
    assert abs(dl-28.1904)<0.01
    assert abs(ln-37.9203)<0.01
    assert abs(out.loc[out.year==2013,'dalian_minus_external_pp'].iloc[0])<0.05
    assert out.loc[out.year==2014,'dalian_minus_liaoning_pp'].iloc[0] < -3
    assert out.loc[out.year==2015,'dalian_minus_liaoning_pp'].iloc[0] < -3

if __name__=='__main__':
    main()
