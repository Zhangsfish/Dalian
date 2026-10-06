#!/usr/bin/env python3
"""S01 reproducible audit and descriptive sensitivity. NOT a political-effect estimator.
Run: python research/bo2012/scripts/analyze.py
Dependencies: pandas,numpy,matplotlib. Missing years remain missing. No imputation.
"""
from pathlib import Path
import json, hashlib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'outputs'; OUT.mkdir(exist_ok=True)
P=pd.read_csv(ROOT/'data/panel_as_reported.csv')
S=pd.read_csv(ROOT/'data/sources.csv')
A=pd.read_csv(ROOT/'data/auxiliary_audit.csv')
assert not P.duplicated(['region','year','vintage']).any(), 'Duplicate panel observations'
assert set(P.gdp_source_id)<=set(S.source_id), 'Missing source metadata'
assert set(P.fai_source_id.dropna())<=set(S.source_id), 'Missing investment source'
assert set(A.source_id)<=set(S.source_id), 'Missing auxiliary source'
assert P.vintage.eq('as_reported').all()
assert not P.causal_ready.any(), 'S01 must not mark unvalidated series causal-ready'
# Reindex the full year grid so plots DO NOT bridge missing 2011/2012/2017.
years=list(range(2005,2020))
g=P.pivot(index='year',columns='region',values='gdp_real_growth_pct').reindex(years)
f=P.pivot(index='year',columns='region',values='fai_growth_pct').reindex(years)
gaps=pd.DataFrame({'year':years,'gdp_gap_DL_minus_LN_pp':g['大连']-g['辽宁'],
                   'fai_gap_DL_minus_LN_pp':f['大连']-f['辽宁']}).reset_index(drop=True)
gaps['interpretation']='descriptive_not_causal;province_contains_city;as_reported_vintages'
gaps.to_csv(OUT/'annual_gaps.csv',index=False,float_format='%.6f')

# Common pre window is only 2007-2010. 2011 actual Dalian observation NOT recovered.
matched=(g['大连']-g['辽宁']).dropna()
pre=matched.loc[2007:2010]
assert pre.index.tolist()==[2007,2008,2009,2010]
x=pre.index.to_numpy(dtype=float); y=pre.to_numpy()
slope, intercept=np.polyfit(x-2007,y,1)
rows=[]
for baseline in [(2007,2010),(2008,2010),(2009,2010)]:
    b=matched.loc[baseline[0]:baseline[1]]
    for window in [(2013,2015),(2013,2016)]:
        z=matched.loc[window[0]:window[1]]
        assert len(z)==window[1]-window[0]+1
        rows.append(dict(pre_years=';'.join(map(str,b.index)),post_years=';'.join(map(str,z.index)),
             n_pre=len(b),n_post=len(z),pre_mean_gap_pp=b.mean(),post_mean_gap_pp=z.mean(),
             change_in_mean_gap_pp=z.mean()-b.mean(),method='arithmetic_gap_change_NOT_identified_DiD'))
sens=pd.DataFrame(rows); sens.to_csv(OUT/'window_sensitivity.csv',index=False,float_format='%.6f')
trend_rows=[]
for window in [(2013,2015),(2013,2016)]:
    z=matched.loc[window[0]:window[1]]
    extrap=intercept+slope*(z.index.to_numpy()-2007)
    trend_rows.append(dict(pre_years='2007;2008;2009;2010',post_years=';'.join(map(str,z.index)),
         gap_slope_pp_per_year=slope,pre_mean_gap_pp=pre.mean(),post_observed_gap_pp=z.mean(),
         post_extrapolated_gap_pp=float(extrap.mean()),observed_minus_extrapolation_pp=float(z.mean()-extrap.mean()),
         interpretation='sensitivity_only;4_pre_points;not_credible_counterfactual;no_p_value'))
pd.DataFrame(trend_rows).to_csv(OUT/'pretrend_sensitivity.csv',index=False,float_format='%.6f')
loo=[]
for omitted in pre.index:
    base=pre.drop(omitted).mean()
    for end in [2015,2016]:
        post=matched.loc[2013:end].mean()
        loo.append(dict(omitted_pre_year=int(omitted),post_end=end,pre_gap_pp=base,post_gap_pp=post,change_pp=post-base))
pd.DataFrame(loo).to_csv(OUT/'leave_one_pre_year_out.csv',index=False,float_format='%.6f')
coverage=[]
for region in ['大连','辽宁','青岛','宁波','厦门','烟台','重庆']:
    q=P.loc[P.region.eq(region)]
    for col in ['gdp_real_growth_pct','fai_growth_pct']:
        present=q.loc[q[col].notna(),'year'].tolist()
        coverage.append(dict(region=region,variable=col,n_observed=len(present),observed_years=';'.join(map(str,present)),
          missing_pre_2005_2011=';'.join(str(y) for y in range(2005,2012) if y not in present),
          missing_post_2013_2016=';'.join(str(y) for y in range(2013,2017) if y not in present)))
pd.DataFrame(coverage).to_csv(OUT/'coverage.csv',index=False)
# FDI is a data audit only, not a seamless comparable series.
checks=[dict(check='mixed_140_to_27.03',value=(27.03/140-1)*100,unit='percent',admissible=False,
             interpretation='INVALID decline: broad foreign capital versus differently labelled later series'),
        dict(check='25_to_27.03_arithmetic',value=(27.03/25-1)*100,unit='percent',admissible=False,
             interpretation='matches rounded 8.1% but arithmetic alone does not establish comparable scope'),
        dict(check='Dalian2016_over_Liaoning2016_FDI',value=30/29.99,unit='ratio',admissible=False,
             interpretation='city nearly equals entire province: check Dalian separate reporting and scope/vintage')]
pd.DataFrame(checks).to_csv(OUT/'scope_checks.csv',index=False,float_format='%.6f')

# Matplotlib defaults; each chart independent, no subplots.
for pivot,col,filename,title,ylabel in [
(g,'gdp','gdp_growth','Reported real GDP growth (missing years left blank)','Percent, as reported'),
(f,'fai','investment_growth','Reported fixed-asset investment growth: scope breaks present','Percent, not constant-price growth')]:
    fig,ax=plt.subplots(figsize=(9.6,5.6),dpi=160)
    for region,label in [('大连','Dalian'),('辽宁','Liaoning (includes Dalian)'),('青岛','Qingdao: sparse pilot only')]:
        ax.plot(pivot.index,pivot[region],marker='o',markersize=4,label=label)
    ax.axvline(2012,linestyle='--',linewidth=1,label='2012 transition')
    ax.set(xlabel='Year',ylabel=ylabel,title=title,xticks=list(range(2005,2020,2)))
    ax.legend(fontsize=8);ax.grid(axis='y',alpha=.2)
    fig.text(.01,.01,'Official annual bulletins; no political causal effect is estimated. See data/sources.csv.',fontsize=8)
    fig.tight_layout(rect=(0,.025,1,1)); fig.savefig(OUT/f'{filename}.png');plt.close(fig)
fig,ax=plt.subplots(figsize=(9.6,5.6),dpi=160)
ax.plot(years,(g['大连']-g['辽宁']),marker='o',label='Dalian minus Liaoning')
ax.axvline(2012,linestyle='--',linewidth=1);ax.axhline(0,linestyle=':',linewidth=1)
ax.set(title='GDP growth gap: baseline and endpoint matter',ylabel='Percentage points',xlabel='Year',xticks=list(range(2005,2020,2)))
ax.grid(axis='y',alpha=.2);ax.legend()
fig.text(.01,.01,'Provincial benchmark is not an untreated control. Missing 2011/2012 left blank; no interpolation.',fontsize=8)
fig.tight_layout(rect=(0,.025,1,1));fig.savefig(OUT/'gdp_gap.png');plt.close(fig)

# Compact monochrome SVG for repository view.
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 420" width="920" height="420">',
 '<rect width="920" height="420" fill="white"/>',
 '<g font-family="sans-serif" fill="black">',
 '<text x="35" y="38" font-size="23">Dalian relative to Liaoning: the endpoint changes the sign</text>',
 '<text x="35" y="66" font-size="14">Mean real-GDP-growth gap; arithmetic only, not a political-effect estimate</text>']
entries=[('2007-2010 pre (4 observed years)',pre.mean()),('2013-2015 post (3 years)',matched.loc[2013:2015].mean()),('2013-2016 post (4 years)',matched.loc[2013:2016].mean())]
for i,(label,value) in enumerate(entries):
    yy=125+i*70
    svg += [f'<text x="35" y="{yy}" font-size="16">{label}</text>',f'<rect x="370" y="{yy-19}" width="{value*130:.3f}" height="28" fill="none" stroke="black"/>',f'<text x="{385+value*130:.3f}" y="{yy+1}" font-size="18">+{value:.3f} pp</text>']
svg += ['<text x="35" y="340" font-size="16">Change versus pre: -1.850 pp (to 2015), +0.275 pp (to 2016)</text>',
 '<text x="35" y="370" font-size="13">Liaoning includes Dalian. Annual vintages are not harmonized; 2011 actual data still missing.</text>',
 '<text x="35" y="393" font-size="13">Including or excluding 2016 is a reported sensitivity, not a license to choose a preferred result.</text>', '</g></svg>']
(OUT/'window_sensitivity.svg').write_text('\n'.join(svg),encoding='utf-8')

summary=dict(panel_rows=len(P),unique_sources=len(S),auxiliary_rows=len(A),
 main_pre_years=list(map(int,pre.index)),pre_mean_gap_pp=float(pre.mean()),pre_gap_slope_pp_per_year=float(slope),
 post_2013_2015_gap_pp=float(matched.loc[2013:2015].mean()),post_2013_2016_gap_pp=float(matched.loc[2013:2016].mean()),
 causal_identification='NOT_ATTEMPTED: incomplete pre data and donors; vintages not harmonized',
 validation=dict(unique_rows=True,source_keys_valid=True,missing_years_not_imputed=True))
(OUT/'run_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'data').glob('*.csv'))}
(OUT/'input_sha256.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert np.isclose(pre.mean(),2.35)
assert np.isclose(sens.iloc[0].change_in_mean_gap_pp,-1.85)
assert np.isclose(sens.iloc[1].change_in_mean_gap_pp,.275)
assert np.isnan(g.loc[2011,'大连']) and np.isnan(g.loc[2012,'大连'])
print(json.dumps(summary,ensure_ascii=False,indent=2))
print(sens.to_string(index=False))
print(pd.DataFrame(trend_rows).to_string(index=False))
