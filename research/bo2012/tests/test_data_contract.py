from pathlib import Path
import unittest
import numpy as np
import pandas as pd
R=Path(__file__).resolve().parents[1]
class DataContract(unittest.TestCase):
    def setUp(self):
        self.p=pd.read_csv(R/'data/panel_as_reported.csv')
        self.s=pd.read_csv(R/'data/sources.csv')
    def test_unique_keys(self):
        self.assertFalse(self.p.duplicated(['region','year','vintage']).any())
        self.assertFalse(self.s.source_id.duplicated().any())
    def test_source_coverage(self):
        self.assertTrue(set(self.p.gdp_source_id)<=set(self.s.source_id))
        self.assertTrue(set(self.p.fai_source_id.dropna())<=set(self.s.source_id))
    def test_no_forecast_inserted(self):
        self.assertTrue(self.p[(self.p.region=='大连')&self.p.year.isin([2011,2012])].empty)
    def test_pre_post_gap_arithmetic(self):
        w=self.p.pivot(index='year',columns='region',values='gdp_real_growth_pct')
        g=w['大连']-w['辽宁'];b=g.loc[2007:2010].mean()
        self.assertAlmostEqual(b,2.35)
        self.assertAlmostEqual(g.loc[2013:2015].mean()-b,-1.85)
        self.assertAlmostEqual(g.loc[2013:2016].mean()-b,.275)
    def test_scope_break_retained(self):
        d=self.p[self.p.region=='大连'].set_index('year')
        self.assertIn('全社会',d.loc[2010,'fai_scope'])
        self.assertIn('不含农户',d.loc[2013,'fai_scope'])
    def test_actual_2015_investment(self):
        v=self.p[(self.p.region=='大连')&(self.p.year==2015)].iloc[0]
        self.assertEqual(v.fai_growth_pct,-32.7)
    def test_fdi_not_trend_ready(self):
        a=pd.read_csv(R/'data/auxiliary_audit.csv')
        d=a[a.variable.str.contains('fdi|foreign_capital')]
        self.assertTrue(d.admissible_use.eq('scope_audit_only').all())
    def test_no_causal_claim(self):
        self.assertFalse(self.p.causal_ready.any())
    def test_dalian_wuhan_gap_screen(self):
        d=pd.read_csv(R/'data/dalian_wuhan_official_growth.csv')
        pre=d[d.period=='pre'].gap_pp.mean()
        post=d[d.period=='post'].gap_pp.mean()
        self.assertAlmostEqual(pre,1.05)
        self.assertAlmostEqual(post,-3.1666666667)
        self.assertAlmostEqual(post-pre,-4.2166666667)
    def test_scm_prefit_is_diagnostic_only(self):
        w=pd.read_csv(R/'outputs/scm_nominal_prefit_weights.csv')
        strict=w[w.pool=='strict_original4'].pre_rmspe_index_points.iloc[0]
        expanded=w[w.pool=='expanded_nonliaoning'].pre_rmspe_index_points.iloc[0]
        self.assertGreater(strict,expanded)
        self.assertAlmostEqual(strict,19.6502807943,places=6)
        self.assertAlmostEqual(expanded,2.5423726537,places=6)
if __name__=='__main__':unittest.main()
