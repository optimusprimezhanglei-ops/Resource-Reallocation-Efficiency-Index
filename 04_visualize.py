"""
04_visualize.py — Generate publication-quality figures (PNG)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np, pandas as pd
from pathlib import Path

# High-quality style
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 120,
    'savefig.dpi': 150,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

DATA = Path('/home/user/re_v2/data')
FIG  = Path('/home/user/re_v2/docs/figures')
FIG.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA/'RE_v2_index_full.csv')
df23 = df[df['year']==2023].sort_values('RE_geom', ascending=False).reset_index(drop=True)

country_order_2023 = df23['code'].tolist()  # for heatmap consistency

# ================== FIG 1: 2023 Ranking Bar (with MC CI) ==================
fig, ax = plt.subplots(figsize=(10, 8))
y_pos = np.arange(len(df23))
colors = plt.cm.RdYlGn(df23['RE_geom'].values / df23['RE_geom'].max())
bars = ax.barh(y_pos, df23['RE_geom'], color=colors, edgecolor='#333', linewidth=0.6)
# Add MC 90% CI whiskers
for i, (lo, hi) in enumerate(zip(df23['RE_MC_p05'], df23['RE_MC_p95'])):
    ax.plot([lo, hi], [i, i], color='#333', linewidth=1.5, alpha=0.7)
    ax.plot([lo, lo], [i-0.15, i+0.15], color='#333', linewidth=1.5, alpha=0.7)
    ax.plot([hi, hi], [i-0.15, i+0.15], color='#333', linewidth=1.5, alpha=0.7)
ax.set_yticks(y_pos)
ax.set_yticklabels([f"{c} — {df23.iloc[i]['country_en']}" for i, c in enumerate(df23['code'])])
ax.invert_yaxis()
ax.set_xlabel('RE Index (Geometric aggregation, 0-1)')
ax.set_title('G20 Resource Reallocation Efficiency Index — 2023\nBaseline + Monte-Carlo 90% CI', fontweight='bold', pad=15)
ax.grid(axis='x', alpha=0.3)
ax.set_xlim(0, 0.95)
# add value labels
for i, v in enumerate(df23['RE_geom']):
    ax.text(v + 0.02, i, f'{v:.3f}', va='center', fontsize=8, color='#333')
plt.tight_layout()
plt.savefig(FIG/'fig1_ranking_2023.png', bbox_inches='tight')
plt.close()
print(f"✓ Saved {FIG/'fig1_ranking_2023.png'}")

# ================== FIG 2: Heatmap 24 years × 20 countries ==================
pivot = df.pivot(index='code', columns='year', values='RE_geom')
pivot = pivot.loc[country_order_2023]

fig, ax = plt.subplots(figsize=(14, 7))
im = ax.imshow(pivot.values, aspect='auto', cmap='RdYlGn', vmin=0.1, vmax=0.8)
ax.set_xticks(range(len(pivot.columns)))
ax.set_xticklabels(pivot.columns, rotation=45)
ax.set_yticks(range(len(pivot.index)))
ax.set_yticklabels(pivot.index)
ax.set_title('G20 RE Index Evolution 2000-2023 — Heatmap\n(Countries sorted by 2023 rank)', fontweight='bold', pad=15)
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('RE Index (Geometric)')
# Mark COVID year
covid_x = list(pivot.columns).index(2020)
ax.axvline(covid_x, color='red', linewidth=1.5, alpha=0.5, linestyle='--')
ax.text(covid_x + 0.3, -1.2, 'COVID-19', color='red', fontsize=9, fontweight='bold')
plt.tight_layout()
plt.savefig(FIG/'fig2_heatmap_evolution.png', bbox_inches='tight')
plt.close()
print(f"✓ Saved {FIG/'fig2_heatmap_evolution.png'}")

# ================== FIG 3: Time-series for 8 key countries ==================
key_countries = ['USA','GBR','DEU','KOR','JPN','CHN','IND','BRA']
country_colors = {'USA':'#1f77b4','GBR':'#ff7f0e','DEU':'#2ca02c','KOR':'#d62728',
                  'JPN':'#9467bd','CHN':'#e377c2','IND':'#8c564b','BRA':'#7f7f7f'}
fig, ax = plt.subplots(figsize=(12, 6))
for c in key_countries:
    sub = df[df['code']==c].sort_values('year')
    ax.plot(sub['year'], sub['RE_geom'], marker='o', linewidth=1.8, markersize=4,
            color=country_colors[c], label=f"{c} ({sub['country_en'].iloc[0]})")
ax.axvline(2008, color='gray', linewidth=1, alpha=0.4, linestyle=':')
ax.axvline(2020, color='red', linewidth=1, alpha=0.4, linestyle=':')
ax.text(2008.2, 0.15, 'GFC', color='gray', fontsize=8)
ax.text(2020.2, 0.15, 'COVID', color='red', fontsize=8)
ax.set_xlabel('Year')
ax.set_ylabel('RE Index (Geometric)')
ax.set_title('RE Index Evolution 2000-2023 — Selected G20 Economies', fontweight='bold', pad=15)
ax.grid(True, alpha=0.3)
ax.legend(loc='upper left', framealpha=0.95, ncol=2)
ax.set_xlim(2000, 2023.5)
ax.set_ylim(0.1, 0.85)
plt.tight_layout()
plt.savefig(FIG/'fig3_timeseries.png', bbox_inches='tight')
plt.close()
print(f"✓ Saved {FIG/'fig3_timeseries.png'}")

# ================== FIG 4: D1-D2-D3 Radar for 6 archetypes ==================
archetypes = ['USA','KOR','JPN','CHN','DEU','ITA']
labels = ['D1 Process\n过程', 'D2 Outcome\n结果', 'D3 Institution\n制度']
N = len(labels)
angles = [n / N * 2 * np.pi for n in range(N)]
angles += angles[:1]

fig, axes = plt.subplots(2, 3, figsize=(14, 9), subplot_kw={'projection':'polar'})
axes = axes.flatten()
for i, c in enumerate(archetypes):
    row = df[(df['code']==c)&(df['year']==2023)].iloc[0]
    values = [row['D1_process'], row['D2_outcome'], row['D3_institution']]
    values += values[:1]
    ax = axes[i]
    ax.plot(angles, values, linewidth=2.5, color='#2c5aa0', marker='o')
    ax.fill(angles, values, alpha=0.25, color='#2c5aa0')
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75])
    ax.set_yticklabels(['0.25','0.50','0.75'], fontsize=7)
    ax.set_title(f"{c} — {row['country_en']}\nRE = {row['RE_geom']:.3f}",
                 pad=15, fontweight='bold', fontsize=11)
    ax.grid(True, alpha=0.4)
plt.suptitle('Three-Dimensional Profile of Six G20 Economies (2023)', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(FIG/'fig4_radar_6countries.png', bbox_inches='tight')
plt.close()
print(f"✓ Saved {FIG/'fig4_radar_6countries.png'}")

# ================== FIG 5: D1 vs D3 scatter with quadrant labels ==================
fig, ax = plt.subplots(figsize=(10, 8))
d1_mean = df23['D1_process'].mean(); d3_mean = df23['D3_institution'].mean()
ax.axhline(d3_mean, color='#999', linewidth=1, linestyle='--', alpha=0.6)
ax.axvline(d1_mean, color='#999', linewidth=1, linestyle='--', alpha=0.6)

# Quadrant background
ax.fill_between([d1_mean, 1], d3_mean, 1, color='#c8e6c9', alpha=0.35, label='Robust Leaders 稳健领军')
ax.fill_between([0, d1_mean], d3_mean, 1, color='#fff9c4', alpha=0.35, label='Strong-Inst / Rigid-Process 制度好过程僵')
ax.fill_between([d1_mean, 1], 0, d3_mean, color='#ffe0b2', alpha=0.35, label='Vigorous-Process / Weak-Inst 过程活制度弱')
ax.fill_between([0, d1_mean], 0, d3_mean, color='#ffcdd2', alpha=0.35, label='Double-Weak 双短板')

for _, row in df23.iterrows():
    ax.scatter(row['D1_process'], row['D3_institution'], s=100, 
               c='#2c5aa0', edgecolor='white', linewidth=1.5, zorder=5)
    dx, dy = 0.015, 0.005
    if row['code'] in ['USA','GBR']: dx = -0.045; dy = 0.02
    if row['code'] == 'JPN': dy = 0.02
    ax.annotate(row['code'], (row['D1_process']+dx, row['D3_institution']+dy), fontsize=10, fontweight='bold', color='#333')

ax.set_xlabel('D1 Process (Reallocation Intensity)  ·  过程维度（再配置强度）', fontsize=11)
ax.set_ylabel('D3 Institution (Enabling Environment)  ·  制度维度（赋能环境）', fontsize=11)
ax.set_title('G20 Countries in Process × Institution Space — 2023\nDiagnostic quadrant classification', fontweight='bold', pad=15)
ax.set_xlim(0.1, 1.0); ax.set_ylim(0.0, 1.05)
ax.grid(True, alpha=0.2)
ax.legend(loc='upper left', framealpha=0.95, fontsize=9)
plt.tight_layout()
plt.savefig(FIG/'fig5_scatter_D1_D3.png', bbox_inches='tight')
plt.close()
print(f"✓ Saved {FIG/'fig5_scatter_D1_D3.png'}")

# ================== FIG 6: Method comparison — RE_geom vs DEA-BoD 2023 ==================
fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(df23['RE_geom'], df23['RE_BoD_2023'], s=120, c='#2c5aa0', 
           edgecolor='white', linewidth=1.5, zorder=5)
# 45-degree reference
lim = [0, 1.05]
ax.plot(lim, lim, 'k--', alpha=0.4, linewidth=1)
for _, row in df23.iterrows():
    ax.annotate(row['code'], (row['RE_geom']+0.008, row['RE_BoD_2023']+0.006),
                fontsize=9, color='#333')
from scipy.stats import spearmanr
rho, _ = spearmanr(df23['RE_geom'], df23['RE_BoD_2023'])
ax.set_xlabel('RE Geometric aggregation  ·  几何加权聚合', fontsize=11)
ax.set_ylabel('RE DEA-BoD (share-bounded)  ·  DEA-BoD 稳健聚合', fontsize=11)
ax.set_title(f'Dual-track Aggregation Robustness — 2023\nSpearman ρ = {rho:.3f}', fontweight='bold', pad=15)
ax.text(0.05, 0.95, 'Highly consistent\nagreement', color='#666', fontsize=10,
        transform=ax.transAxes, va='top',
        bbox=dict(boxstyle='round,pad=0.5', fc='#f0f0f0', ec='#999'))
ax.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig(FIG/'fig6_method_comparison.png', bbox_inches='tight')
plt.close()
print(f"✓ Saved {FIG/'fig6_method_comparison.png'}")

# ================== FIG 7: Cronbach α per dimension ==================
fig, ax = plt.subplots(figsize=(10, 5))
data = pd.DataFrame({
    'Dimension': ['All 15 items', 'D1 Process', 'D2 Outcome', 'D3 Institution'],
    'Cronbach α':  [0.903, 0.818, 0.402, 0.931],
})
colors2 = ['#2c5aa0','#5486c9','#e0a842','#3e9b52']
bars = ax.bar(data['Dimension'], data['Cronbach α'], color=colors2, edgecolor='#333', linewidth=0.6)
ax.axhline(0.70, color='#333', linewidth=1, linestyle='--')
ax.axhline(0.80, color='#333', linewidth=1, linestyle=':')
ax.text(3.4, 0.71, 'α = 0.70 (good)', fontsize=8, ha='right', color='#333')
ax.text(3.4, 0.81, 'α = 0.80 (excellent)', fontsize=8, ha='right', color='#333')
for i, v in enumerate(data['Cronbach α']):
    ax.text(i, v + 0.02, f'{v:.3f}', ha='center', fontsize=10, fontweight='bold')
ax.set_ylim(0, 1.05)
ax.set_ylabel("Cronbach's α")
ax.set_title('Internal Consistency Reliability — Full RE Index and Three Dimensions',
             fontweight='bold', pad=15)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig(FIG/'fig7_cronbach.png', bbox_inches='tight')
plt.close()
print(f"✓ Saved {FIG/'fig7_cronbach.png'}")

# ================== FIG 8: KOR / CHN / USA trajectory decomposition ==================
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
for i, code in enumerate(['USA','KOR','CHN']):
    ax = axes[i]
    sub = df[df['code']==code].sort_values('year')
    ax.plot(sub['year'], sub['RE_geom'], marker='o', linewidth=2.5, color='#2c5aa0',
            markersize=5, label='RE (composite)', zorder=5)
    ax.plot(sub['year'], sub['D1_process'], marker='^', linewidth=1.2, color='#e74c3c', alpha=0.7, label='D1 Process')
    ax.plot(sub['year'], sub['D2_outcome'], marker='s', linewidth=1.2, color='#f39c12', alpha=0.7, label='D2 Outcome')
    ax.plot(sub['year'], sub['D3_institution'], marker='D', linewidth=1.2, color='#27ae60', alpha=0.7, label='D3 Institution')
    ax.axvline(2020, color='red', linewidth=1, alpha=0.4, linestyle=':')
    ax.set_title(f"{code} — {sub['country_en'].iloc[0]}", fontweight='bold')
    ax.set_xlabel('Year')
    if i == 0: ax.set_ylabel('Score (0–1)')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower right', framealpha=0.9, fontsize=8)
    ax.set_ylim(0, 1.05)
plt.suptitle('Three-Dimensional Trajectory Decomposition — USA, KOR, CHN (2000-2023)',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(FIG/'fig8_trajectories.png', bbox_inches='tight')
plt.close()
print(f"✓ Saved {FIG/'fig8_trajectories.png'}")

print(f"\nAll {len(list(FIG.glob('*.png')))} figures saved to {FIG}")
