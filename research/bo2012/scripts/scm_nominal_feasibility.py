#!/usr/bin/env python3
"""S02B donor-feasibility screening.

This is NOT a causal estimator. It asks only whether candidate donors can reproduce
Dalian's pre-2012 nominal-GDP trajectory after normalizing 2005=100.

Input values are secondary historical GDP-level aggregates documented in sources.csv.
Post-2011 gaps are deliberately not interpreted as effects because city historical
levels contain asynchronous statistical revisions/rebasings.
"""
from __future__ import annotations
import math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize

R = Path(__file__).resolve().parents[1]
YEARS = list(range(2005, 2020))

DATA = {
"Dalian":[2152.23,2569.67,3130.68,3858.25,4349.51,5158.16,6150.63,7002.83,7650.79,7655.58,7731.64,6810.2,6989.82,7668.48,7002],
"Qingdao":[2695.82,3206.58,3786.52,4436.18,4853.87,5666.19,6615.6,7302.11,8006.6,8692.1,9300.07,10011.29,11024.11,12001.52,11741],
"Ningbo":[2449.3099,2874.4435,3435.0042,3964.0472,4329.3025,5163,6059.24,6582.21,7128.87,7610.28,8003.61,8686.49,9842.06,10745.46,11985],
"Xiamen":[1006.58,1168.02,1387.85,1560.02,1737.23,2060.07,2539.31,2817.07,3018.16,3273.58,3466.03,3784.27,4351.72,4791.41,5995],
"Yantai":[2012.46,2405.7504,2879.9509,3434.19,3701.79,4358.46,4906.83,5281.38,5613.87,6002.08,6446.08,6925.66,7343.53,7832.58,7653],
"Guangzhou":[5154.2283,6073.8277,7109.1814,8215.8151,9138.2135,10748.28,12423.44,13551.21,15420.14,16706.87,18100.41,19547.44,21503.15,22859.35,23629],
"Shenzhen":[4950.9078,5813.5624,6801.5706,7806.5387,8201.3176,9581.51,11505.53,12950.06,14500.23,16001.82,17502.86,19492.6,22490.06,24221.98,26927],
"Tangshan":[2027.6374,2362.141,2779.419,3561.19,3812.7192,4469.16,5442.45,5861.64,6121.21,6225.3,6103.06,6354.87,6530.1,6954.97,6890],
"Suzhou":[4026.52,4820.26,5700.85,6701.29,7740.2,9228.91,10716.99,12011.65,13015.7,13760.89,14504.07,15475.09,17319.51,18597.47,19236],
"Wuxi":[2804.68,3300.59,3858.54,4419.5,4991.72,5793.3,6880.15,7568.15,8070.18,8205.31,8518.26,9210.02,10511.8,11438.62,11852],
"Fuzhou":[1476.31,1664.05,1974.58,2284.16,2604.04,3123.41,3736.38,4218.29,4678.5,5169.16,5618.08,6197.64,7085.52,7856.81,9392],
"Tianjin":[3697.62,4359.15,5050.4,6354.38,7521.85,9224.46,11307.28,12893.88,14370.16,15726.93,16538.19,17885.39,18549.19,18809.64,14104],
"Nantong":[1472.08,1758.34,2111.88,2510.13,2872.8038,3465.67,4080.22,4558.67,5038.89,5652.69,6148.4,6768.2,7734.64,8427,9383],
"Wuhan":[2238,2590.7569,3141.9048,3960.0819,4620.86,5565.93,6762.2,8003.82,9051.27,10069.48,10905.6,11912.61,13410.34,14847.29,16223],
"Zhuhai":[634.9521,747.7029,895.901,992.0616,1038.6627,1208.6,1404.93,1503.76,1662.38,1867.21,2025.41,2226.37,2675.18,2914.74,3436],
}

STRICT = ["Qingdao","Ningbo","Xiamen","Yantai"]
EXPANDED = [k for k in DATA if k != "Dalian"]
PRE = list(range(2005, 2012))

def fit(idx: pd.DataFrame, donors: list[str]):
    X = idx.loc[PRE, donors].to_numpy()
    y = idx.loc[PRE, "Dalian"].to_numpy()
    def loss(w):
        return np.mean((X @ w - y) ** 2)
    res = minimize(
        loss, np.ones(len(donors))/len(donors),
        bounds=[(0,1)]*len(donors),
        constraints=[{"type":"eq","fun":lambda w:w.sum()-1}],
        method="SLSQP", options={"maxiter":5000,"ftol":1e-12}
    )
    if not res.success:
        raise RuntimeError(res.message)
    rmspe = math.sqrt(loss(res.x))
    weights = {d: float(w) for d,w in zip(donors,res.x) if w > 1e-6}
    return rmspe, weights

def main():
    df = pd.DataFrame(DATA, index=YEARS)
    idx = df.div(df.loc[2005]).mul(100)

    rows=[]
    for pool_name, donors in [("strict_original4", STRICT), ("expanded_nonliaoning", EXPANDED)]:
        rmspe, w = fit(idx, donors)
        for region, weight in w.items():
            rows.append({"pool":pool_name,"pre_rmspe_index_points":rmspe,
                         "region":region,"weight":weight})
    out = pd.DataFrame(rows)
    out.to_csv(R/"outputs/scm_nominal_prefit_weights_reproduced.csv", index=False)

    loo=[]
    for label, drops in [
        ("expanded_full", []),
        ("drop_Wuhan", ["Wuhan"]),
        ("drop_Yantai", ["Yantai"]),
        ("drop_Wuhan_and_Yantai", ["Wuhan","Yantai"]),
    ]:
        donors=[d for d in EXPANDED if d not in drops]
        rmspe,w=fit(idx,donors)
        loo.append({"scenario":label,"pre_rmspe_index_points":rmspe,
                    "weights":";".join(f"{k}:{v:.6f}" for k,v in w.items())})
    pd.DataFrame(loo).to_csv(R/"outputs/scm_nominal_leaveout_reproduced.csv", index=False)

    # Warning: post-period index gaps are not causal outputs.
    _, w = fit(idx, EXPANDED)
    syn = sum(idx[d]*weight for d,weight in w.items())
    pd.DataFrame({
        "year":YEARS,
        "dalian_index_2005_100":idx["Dalian"].values,
        "synthetic_index_2005_100":syn.values,
        "gap_index_points":idx["Dalian"].values-syn.values,
        "admissible_use":"diagnostic_only_post_gap_not_causal"
    }).to_csv(R/"outputs/scm_nominal_diagnostic_path.csv", index=False)

if __name__ == "__main__":
    main()
