#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

R=Path(__file__).resolve().parents[1]
d=pd.read_csv(R/'data/credit_s03c.csv')

# Recalculate every derived loan growth from balance and increment.
mask=d.growth_status.eq('derived') & d.loan_increment_100m_cny.notna()
d.loc[mask,'loan_growth_recalc_pct']=(
    d.loc[mask,'loan_increment_100m_cny'] /
    (d.loc[mask,'loan_balance_100m_cny']-d.loc[mask,'loan_increment_100m_cny']) * 100
)
d.loc[~mask,'loan_growth_recalc_pct']=d.loc[~mask,'loan_growth_pct']
d.to_csv(R/'outputs/credit_growth_reproduced.csv',index=False)

w=d.pivot(index='year',columns='region',values='loan_growth_recalc_pct')
rows=[]
for y in [2010,2011,2012,2013,2014,2015,2016]:
    if y in w.index and '大连' in w.columns and '辽宁' in w.columns:
        rows.append([y,w.loc[y,'大连'],w.loc[y,'辽宁'],w.loc[y,'大连']-w.loc[y,'辽宁']])
pd.DataFrame(rows,columns=['year','dalian_growth','liaoning_growth','gap_pp']).to_csv(
    R/'outputs/dalian_liaoning_credit_gap.csv',index=False)

# Dalian share of Liaoning new credit, only years with comparable increments.
shares=[]
for y in [2013,2014,2015,2016]:
    dl=d[(d.region=='大连')&(d.year==y)].iloc[0]
    ln=d[(d.region=='辽宁')&(d.year==y)].iloc[0]
    shares.append([y,dl.loan_increment_100m_cny/ln.loan_increment_100m_cny*100])
pd.DataFrame(shares,columns=['year','dalian_share_of_liaoning_loan_increment_pct']).to_csv(
    R/'outputs/dalian_credit_increment_share.csv',index=False)
