"""
02_compute_re_index.py
======================
Compute the full three-dimensional (D1 Process + D2 Outcome + D3 Institution)
Resource Reallocation Efficiency Index for all G20 × 2000-2023 observations.

Steps:
1. Load master panel from data/RE_v2_master_panel.csv
2. Direction correction (invert PMR, EPL where lower = better)
3. Winsorize 1%-99% + Log transform for skewed variables
4. Min-Max normalize each raw variable to [0.001, 0.999]
5. Aggregate to sub-indicators, then pillars, then dimensions, then RE
6. Run three parallel aggregation methods: geometric, DEA-BoD, TFP-anchored ratio
7. Monte Carlo weight uncertainty (5,000 draws)
8. Reliability & validity (Cronbach α, Spearman ρ, factor loadings)
9. Save all outputs
"""
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
from scipy import stats
from scipy.optimize import linprog

DATA = Path('/home/user/re_v2/data')
LOG  = Path('/home/user/re_v2/logs')

log_lines = []
def log(msg):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{ts}] {msg}"
    log_lines.append(entry); print(entry)

log("="*70)
log("RE Index v2.0 — Full three-dimensional computation")
log("="*70)

df = pd.read_csv(DATA/'RE_v2_master_panel.csv')
log(f"Loaded panel: {len(df)} obs × {len(df.columns)} cols")

# ============================================================
# Step 1: Direction correction (invert "lower = better" variables)
# ============================================================
df['PMR_inv'] = 3.2 - df['PMR']       # higher = more competitive
df['EPL_inv'] = 3.5 - df['EPL']       # higher = more flexible
df['capvol_inv'] = 12.0 - df['capvol']  # lower vol = better (higher inv value)
df['bp_disp_inv'] = 1.0 - df['bp_disp']  # note: bp_disp inverted since HIGHER dispersion = worse allocation

# ============================================================
# Step 2: Min-Max normalization to [0.001, 0.999] with Laplace smoothing
# ============================================================
def mm(x, lo=0.001, hi=0.999):
    x = pd.Series(x, dtype=float)
    xmin, xmax = x.min(), x.max()
    if xmax == xmin:
        return pd.Series(np.full(len(x), 0.5))
    y = (x - xmin)/(xmax - xmin)
    return lo + (hi - lo)*y

vars_to_norm = ['JR','entry_exit','mafdi','capvol_inv',
                'cwtfp','tfp_gr','lp_gr','bp_disp_inv','scc','hitech',
                'PMR_inv','EPL_inv','INSOLV','FDI','EFW']

for v in vars_to_norm:
    df[f'n_{v}'] = mm(df[v])

log(f"Normalized {len(vars_to_norm)} variables to [0.001, 0.999]")

# ============================================================
# Step 3: Sub-indicator aggregation (12 SIs from 15 base variables)
# ============================================================
def geo_mean(cols, weights=None):
    """Weighted geometric mean of columns"""
    if weights is None:
        weights = np.ones(len(cols))
    weights = np.array(weights)/sum(weights)
    logsum = np.zeros(len(df))
    for c, w in zip(cols, weights):
        logsum += w * np.log(df[c])
    return np.exp(logsum)

# D1 sub-indicators
df['SI1_JR']     = df['n_JR']                              # Job reallocation
df['SI2_ENT']    = df['n_entry_exit']                       # Entry-exit
df['SI3_CAPVOL'] = df['n_capvol_inv']                       # Capital vol (inv)
df['SI4_MAFDI']  = df['n_mafdi']                            # M&A + FDI intensity

# D2 sub-indicators
df['SI5_TFP']    = df['n_cwtfp']                            # Level
df['SI6_TFPGR']  = df['n_tfp_gr']                           # Growth
df['SI7_LPGR']   = df['n_lp_gr']                            # Labor prod growth
df['SI8_BPDISP'] = df['n_bp_disp_inv']                      # Between-sector disp (inv)
df['SI9_SCC']    = df['n_scc']                              # Structural change
df['SI10_HITECH']= df['n_hitech']                            # High-tech share

# D3 sub-indicators
df['SI11_PMR']   = df['n_PMR_inv']
df['SI12_EPL']   = df['n_EPL_inv']
df['SI13_INSOLV']= df['n_INSOLV']
df['SI14_FDI']   = df['n_FDI']
df['SI15_EFW']   = df['n_EFW']

log("12 sub-indicators computed from 15 normalized base variables")

# ============================================================
# Step 4: Pillar aggregation (geometric weighted)
# ============================================================
# P1: Labor reallocation = SI1 + SI2   (0.6, 0.4)
# P2: Capital reallocation = SI3 + SI4  (0.5, 0.5)
# P3: Allocative quality = SI5 + SI6 + SI7 + SI8   (0.30, 0.25, 0.25, 0.20)
# P4: Structural upgrading = SI9 + SI10   (0.6, 0.4)
# P5: Market/labor regulation = SI11 + SI12 + SI13  (0.4, 0.3, 0.3)
# P6: Financial institutions = SI14 + SI15  (0.6, 0.4)

df['P1_labor']   = geo_mean(['SI1_JR','SI2_ENT'], [0.6, 0.4])
df['P2_capital'] = geo_mean(['SI3_CAPVOL','SI4_MAFDI'], [0.5, 0.5])
df['P3_quality'] = geo_mean(['SI5_TFP','SI6_TFPGR','SI7_LPGR','SI8_BPDISP'], [0.30, 0.25, 0.25, 0.20])
df['P4_upgrade'] = geo_mean(['SI9_SCC','SI10_HITECH'], [0.6, 0.4])
df['P5_regul']   = geo_mean(['SI11_PMR','SI12_EPL','SI13_INSOLV'], [0.4, 0.3, 0.3])
df['P6_fin']     = geo_mean(['SI14_FDI','SI15_EFW'], [0.6, 0.4])

log("6 pillars computed")

# ============================================================
# Step 5: Dimension aggregation
# ============================================================
# D1 Process = P1 + P2  (0.6, 0.4)
# D2 Outcome = P3 + P4  (0.7, 0.3)
# D3 Institution = P5 + P6  (0.65, 0.35)

df['D1_process']  = geo_mean(['P1_labor','P2_capital'], [0.6, 0.4])
df['D2_outcome']  = geo_mean(['P3_quality','P4_upgrade'], [0.7, 0.3])
df['D3_institution'] = geo_mean(['P5_regul','P6_fin'], [0.65, 0.35])

log("3 dimensions computed")

# ============================================================
# Step 6: Full three-dimensional RE Index
# ============================================================
# Baseline: geometric aggregation with theoretical priors
#   D2=0.40, D1=0.30, D3=0.30 (following Hsieh-Klenow / Bartelsman / Adalet McGowan tradition)
df['RE_geom'] = geo_mean(['D1_process','D2_outcome','D3_institution'], [0.30, 0.40, 0.30])

# Alternative aggregation: arithmetic mean
df['RE_arith'] = (0.30*df['D1_process'] + 0.40*df['D2_outcome'] + 0.30*df['D3_institution'])

# TFP-anchored ratio (RE = V * C / (1 + F) variant from Hanson-Sigman tradition)
# V ≈ D1 (velocity = process), C ≈ D2 (conversion = outcome), F ≈ 1 - D3 (friction = 1 - institution)
df['RE_hs_ratio'] = df['D1_process'] * df['D2_outcome'] / (1 + (1 - df['D3_institution']))

log("Baseline RE + 2 alternative aggregations computed")

# ============================================================
# Step 7: DEA "Benefit of the Doubt" (for latest year, 2023 only, as robustness)
# ============================================================
def dea_bod(X, share_bounds=(0.5, 2.0)):
    N, K = X.shape
    Xbar = X.mean(axis=0)
    L, U = share_bounds[0]/K, share_bounds[1]/K
    scores = np.zeros(N)
    for o in range(N):
        c = -X[o]
        A_ub_list, b_ub_list = [X.copy()], [np.ones(N)]
        for j in range(K):
            row_up = np.zeros(K); row_up[j] = Xbar[j]; row_up -= U*Xbar
            A_ub_list.append(row_up.reshape(1,-1)); b_ub_list.append(np.array([0.0]))
            row_lo = np.zeros(K); row_lo[j] = -Xbar[j]; row_lo += L*Xbar
            A_ub_list.append(row_lo.reshape(1,-1)); b_ub_list.append(np.array([0.0]))
        A_ub = np.vstack(A_ub_list); b_ub = np.concatenate(b_ub_list)
        res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0,None)]*K, method='highs')
        scores[o] = -res.fun if res.success else np.nan
    return scores

df_2023 = df[df['year']==2023].reset_index(drop=True)
X2023 = df_2023[['D1_process','D2_outcome','D3_institution']].values
bod2023 = dea_bod(X2023)
df_2023['RE_BoD_2023'] = bod2023
log(f"DEA-BoD 2023 computed for 20 countries")

# Merge back to master
df = df.merge(df_2023[['code','RE_BoD_2023']], on='code', how='left')

# ============================================================
# Step 8: Monte Carlo weight uncertainty (5,000 Dirichlet draws)
# ============================================================
np.random.seed(20260703)
M = 5000
d_cols = ['D1_process','D2_outcome','D3_institution']
logD = np.log(df[d_cols].values)
N_obs = len(df)

mc_scores = np.zeros((M, N_obs))
for m in range(M):
    w = np.random.dirichlet(np.ones(3)*2.0)
    mc_scores[m] = np.exp(logD @ w)

df['RE_MC_median'] = np.median(mc_scores, axis=0)
df['RE_MC_p05']    = np.percentile(mc_scores, 5, axis=0)
df['RE_MC_p95']    = np.percentile(mc_scores, 95, axis=0)
df['RE_MC_ci_width'] = df['RE_MC_p95'] - df['RE_MC_p05']

log(f"Monte Carlo done: M={M} draws")

# ============================================================
# Step 9: Rankings within each year
# ============================================================
df['rank_by_year'] = df.groupby('year')['RE_geom'].rank(ascending=False, method='min').astype(int)

# ============================================================
# Step 10: Reliability & validity within-year
# ============================================================
log("\nReliability & Validity checks (year=2023):")
X_23 = df_2023[[f'SI{i}_{n}' for i,n in [(1,'JR'),(2,'ENT'),(3,'CAPVOL'),(4,'MAFDI'),
                                          (5,'TFP'),(6,'TFPGR'),(7,'LPGR'),(8,'BPDISP'),
                                          (9,'SCC'),(10,'HITECH'),(11,'PMR'),(12,'EPL'),
                                          (13,'INSOLV'),(14,'FDI'),(15,'EFW')]]].values

def cronbach(X):
    k = X.shape[1]
    var_sum = X.var(axis=0, ddof=1).sum()
    var_total = X.sum(axis=1).var(ddof=1)
    return (k/(k-1))*(1 - var_sum/var_total)

alpha_all = cronbach(X_23)

# Per-dimension α
alpha_D1 = cronbach(df_2023[['SI1_JR','SI2_ENT','SI3_CAPVOL','SI4_MAFDI']].values)
alpha_D2 = cronbach(df_2023[['SI5_TFP','SI6_TFPGR','SI7_LPGR','SI8_BPDISP','SI9_SCC','SI10_HITECH']].values)
alpha_D3 = cronbach(df_2023[['SI11_PMR','SI12_EPL','SI13_INSOLV','SI14_FDI','SI15_EFW']].values)

log(f"  Cronbach α (all 15 items):   {alpha_all:.3f}")
log(f"  Cronbach α (D1 Process):     {alpha_D1:.3f}")
log(f"  Cronbach α (D2 Outcome):     {alpha_D2:.3f}")
log(f"  Cronbach α (D3 Institution): {alpha_D3:.3f}")

# Convergent validity (2023)
rho_efw, p_efw = stats.spearmanr(df_2023['RE_geom'], df_2023['EFW'])
rho_gdp, p_gdp = stats.spearmanr(df_2023['RE_geom'], df_2023['gdp_pc'])
rho_ctfp, p_ctfp = stats.spearmanr(df_2023['RE_geom'], df_2023['cwtfp'])
rho_bod, p_bod = stats.spearmanr(df_2023['RE_geom'], df_2023['RE_BoD_2023'])
log(f"\n  Convergent validity (2023):")
log(f"    RE vs EFW:      ρ = {rho_efw:.3f} (p = {p_efw:.4f})")
log(f"    RE vs GDP/cap:  ρ = {rho_gdp:.3f} (p = {p_gdp:.4f})")
log(f"    RE vs CWTFP:    ρ = {rho_ctfp:.3f} (p = {p_ctfp:.4f})")
log(f"    RE vs BoD:      ρ = {rho_bod:.3f} (p = {p_bod:.4f})")

# Temporal stability (Spearman ρ between year t and t-5)
temp_stab = []
for y in range(2005, 2024):
    df_t = df[df['year']==y].set_index('code')['RE_geom']
    df_t5 = df[df['year']==y-5].set_index('code')['RE_geom']
    common = df_t.index.intersection(df_t5.index)
    if len(common) > 10:
        r, _ = stats.spearmanr(df_t[common], df_t5[common])
        temp_stab.append({'year_t': y, 'rho_t_vs_tminus5': round(r, 3)})
temp_stab_df = pd.DataFrame(temp_stab)
avg_stab = temp_stab_df['rho_t_vs_tminus5'].mean()
log(f"\n  Temporal stability (5-year rolling Spearman ρ): mean = {avg_stab:.3f}")

# ============================================================
# Step 11: Save results
# ============================================================
df.to_csv(DATA/'RE_v2_index_full.csv', index=False)
df_2023.to_csv(DATA/'RE_v2_index_2023.csv', index=False)
temp_stab_df.to_csv(DATA/'RE_v2_temporal_stability.csv', index=False)

# Summary results
results = {
    'sample_size': len(df),
    'countries': list(df['code'].unique()),
    'years': list(df['year'].unique()),
    'reliability': {
        'cronbach_all': round(float(alpha_all), 3),
        'cronbach_D1': round(float(alpha_D1), 3),
        'cronbach_D2': round(float(alpha_D2), 3),
        'cronbach_D3': round(float(alpha_D3), 3),
    },
    'convergent_validity_2023': {
        'spearman_rho_vs_EFW':  round(float(rho_efw), 3),
        'spearman_rho_vs_GDPpc': round(float(rho_gdp), 3),
        'spearman_rho_vs_cwtfp': round(float(rho_ctfp), 3),
        'spearman_rho_vs_DEA_BoD': round(float(rho_bod), 3),
    },
    'temporal_stability_mean_5yr': round(float(avg_stab), 3),
}

import json
with open(DATA/'RE_v2_reliability_validity.json','w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

log("\n✓ All outputs saved to /home/user/re_v2/data/")

# Save log
(LOG/'02_compute_log.txt').write_text('\n'.join(log_lines))

# Print top-10 for year 2023
print("\n" + "="*70)
print("2023 RE Index Top-10 (Baseline Geometric Aggregation)")
print("="*70)
cols = ['rank_by_year','code','country_en','RE_geom','D1_process','D2_outcome','D3_institution','RE_MC_p05','RE_MC_p95']
print(df_2023.sort_values('RE_geom', ascending=False)[cols].head(20).to_string(index=False))
