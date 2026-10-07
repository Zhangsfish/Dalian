#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

R=Path(__file__).resolve().parents[1]
d=pd.read_csv(R/'data/real_estate_land_s03a.csv')

def val(region,year,indicator):
    x=d[(d.region==region)&(d.year==year)&(d.indicator==indicator)]
    return float(x.value.iloc[0])

rows=[]
for region in ['大连','辽宁']:
    fai13=val(region,2013,'fixed_asset_investment')
    fai14=val(region,2014,'fixed_asset_investment')
    fai15=val(region,2015,'fixed_asset_investment')
    re13=val(region,2013,'real_estate_investment')
    re14=val(region,2014,'real_estate_investment')
    re15=val(region,2015,'real_estate_investment')
    rows += [
      [region,'real_estate_share_of_fai_2013',re13/fai13],
      [region,'real_estate_share_of_fai_2014',re14/fai14],
      [region,'real_estate_share_of_fai_2015',re15/fai15],
      [region,'fai_decline_2013_to_2015_100m_cny',fai15-fai13],
      [region,'real_estate_decline_2013_to_2015_100m_cny',re15-re13],
      [region,'real_estate_share_of_fai_decline_2013_to_2015',(re15-re13)/(fai15-fai13)],
      [region,'fai_decline_2014_to_2015_100m_cny',fai15-fai14],
      [region,'real_estate_decline_2014_to_2015_100m_cny',re15-re14],
      [region,'real_estate_share_of_fai_decline_2014_to_2015',(re15-re14)/(fai15-fai14)],
    ]

out=pd.DataFrame(rows,columns=['region','metric','value'])
out.to_csv(R/'outputs/real_estate_accounting_reproduced.csv',index=False)

# Growth comparison panel for display
growth=d[d.indicator=='real_estate_investment_growth'][['region','year','value']].pivot(index='year',columns='region',values='value')
growth.to_csv(R/'outputs/real_estate_growth_comparison.csv')
print(out)
