#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

R=Path(__file__).resolve().parents[1]

def main():
    d=pd.read_csv(R/'data/real_estate_investment_panel_s03a.csv')
    rows=[]
    for region in ['大连','辽宁','武汉']:
        x=d[d.region==region].set_index('year')
        if 2013 in x.index and 2015 in x.index:
            rows.append({
                'region':region,
                'real_estate_investment_change_2013_2015_pct':
                    (x.loc[2015,'real_estate_investment_100m_cny']/x.loc[2013,'real_estate_investment_100m_cny']-1)*100
            })
    out=pd.DataFrame(rows)
    out.to_csv(R/'outputs/real_estate_cumulative_change_s03a.csv',index=False)

    p=d.pivot(index='year',columns='region',values='real_estate_growth_pct')
    g=(p['大连']-p['辽宁']).dropna()
    assert abs(g.mean()-0.4570608467)<1e-6

    x=d[d.region.isin(['大连','辽宁'])].pivot(index='year',columns='region',values='real_estate_share_of_fai_pct')
    assert abs((x['大连']-x['辽宁']).abs().max())<0.7

    f=d[d.region.isin(['大连','辽宁'])].pivot(index='year',columns='region',values='total_fai_100m_cny')
    dl=(f.loc[2015,'大连']/f.loc[2013,'大连']-1)*100
    ln=(f.loc[2015,'辽宁']/f.loc[2013,'辽宁']-1)*100
    assert abs(dl-ln)<1.0

if __name__=='__main__':
    main()
