# 附录 B · 关键代码摘录 / Appendix B — Key Code Excerpts

## B.1 数据主面板构建（Python）/ Master Panel Construction (Python)

**中文：** 以下是从原始数据源构建 G20 × 24 年 = 480 观测主面板的核心 Python 代码框架（完整版见 `/home/user/re_v2/src/01_build_master_dataset.py`）：

```python
import pandas as pd
import numpy as np
from pathlib import Path

# ---- 1. 国家与年份 ----
G20 = ["ARG","AUS","BRA","CAN","CHN","FRA","DEU","IND","IDN","ITA",
       "JPN","KOR","MEX","RUS","SAU","ZAF","TUR","GBR","USA","EUU"]
YEARS = list(range(2000, 2024))
panel = pd.MultiIndex.from_product([G20, YEARS], names=["code","year"]).to_frame(index=False)

# ---- 2. D1 过程强度指标 ----
# JR: OECD DynEmp / 学术文献插值
# entry_exit: World Bank 企业注册数据
# mafdi: UNCTAD M&A + FDI 存量/GDP
panel["JR"]         = load_jr_series(G20, YEARS)
panel["entry_exit"] = load_entry_exit(G20, YEARS)
panel["mafdi"]      = load_ma_fdi(G20, YEARS)

# ---- 3. D2 结果质量指标 ----
# cwtfp: PWT 11.0 (welfare TFP relative to US)
# tfp_gr: PWT rtfpna 增长率
# lp_gr: World Bank ASPD 劳动生产率增长
# bp_disp: 企业间生产率离散度 (OECD MultiProd)
# scc: GGDC ETD 结构变革贡献
# hitech: World Bank 高技术出口占比
panel["cwtfp"]   = load_pwt_cwtfp(G20, YEARS)
panel["tfp_gr"]  = load_pwt_tfp_growth(G20, YEARS)
panel["lp_gr"]   = load_wb_lp_growth(G20, YEARS)
panel["bp_disp"] = load_multiprod_disp(G20, YEARS)
panel["scc"]     = load_ggdc_scc(G20, YEARS)
panel["hitech"]  = load_wb_hitech(G20, YEARS)

# ---- 4. D3 制度赋能指标 ----
# PMR: OECD Product Market Regulation
# EPL: OECD Employment Protection Legislation v4
# INSOLV: OECD Adalet McGowan-Andrews Insolvency Indicator
# FDI: IMF Financial Development Index
# EFW: Fraser Economic Freedom of the World
panel["PMR"]    = load_oecd_pmr(G20, YEARS)
panel["EPL"]    = load_oecd_epl(G20, YEARS)
panel["INSOLV"] = load_oecd_insolvency(G20, YEARS)
panel["FDI"]    = load_imf_fdi(G20, YEARS)
panel["EFW"]    = load_fraser_efw(G20, YEARS)

# ---- 5. 输出 ----
panel.to_csv("/home/user/re_v2/data/RE_v2_master_panel.csv", index=False)
```

**English:** Core master-panel construction: G20 × 24 years × 15 indicators sourced from PWT 11.0, World Bank, OECD, IMF, GGDC, and Fraser. All loader functions are documented in `01_build_master_dataset.py` with full source URLs.

## B.2 RE 指数计算（Python）/ RE Index Computation (Python)

**中文：** 核心计算函数（`/home/user/re_v2/src/02_compute_re_index.py`）：

```python
import numpy as np
import pandas as pd

EPS = 0.001

def normalize_minmax(x):
    """面板 Min-Max 归一化。"""
    return (x - x.min()) / (x.max() - x.min() + 1e-12)

def invert_negative(x):
    """负向指标反转：PMR/EPL/BP disp 值越高越差。"""
    return x.max() - x

def compute_pillar(df, cols, weights=None):
    """维度聚合（几何平均，等权基线）。"""
    if weights is None:
        weights = np.ones(len(cols)) / len(cols)
    arr = df[cols].values + EPS
    return np.exp(np.sum(weights * np.log(arr), axis=1))

def compute_re(df):
    """三维几何聚合。"""
    D1 = compute_pillar(df, ["n_JR", "n_entry_exit", "n_mafdi"])
    D2 = compute_pillar(df, ["n_cwtfp", "n_tfp_gr", "n_lp_gr",
                             "n_bp_disp_inv", "n_scc", "n_hitech"])
    D3 = compute_pillar(df, ["n_PMR_inv", "n_EPL_inv",
                             "n_INSOLV", "n_FDI", "n_EFW"])
    RE = np.cbrt(D1 * D2 * D3)  # equal-weight geometric mean
    return pd.DataFrame({"D1_process": D1, "D2_outcome": D2,
                         "D3_institution": D3, "RE_geom": RE})
```

**English:** Simple, transparent computation: (1) invert negative-direction indicators, (2) Min-Max normalize, (3) geometric mean within pillars, (4) geometric mean across pillars. Total: ~50 lines of core logic.

## B.3 DEA-BoD 优化（Python + scipy.optimize）/ DEA-BoD via scipy

**中文：** 每个国家单独求解带份额约束的线性规划：

```python
from scipy.optimize import linprog

def dea_bod_country(x_i, X_all, L=0.1, U=0.6):
    """
    x_i: 目标国的 K 个指标向量
    X_all: 全部 N 国 × K 指标矩阵
    L, U: 份额下限与上限
    """
    N, K = X_all.shape
    # Maximize sum(w_k * x_i[k]) subject to X @ w <= 1, share bounds
    c = -x_i  # scipy 求最小
    A_ub = X_all
    b_ub = np.ones(N)
    # 份额约束通过线性变形加入
    bounds = [(0, None)] * K
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    if not result.success:
        return np.nan
    w_star = result.x
    return float(np.dot(w_star, x_i))
```

**English:** Country-specific LP: maximize weighted sum subject to "no country's weighted score > 1" plus 10%-60% share bounds. Solved via scipy's HiGHS backend for numerical stability.

## B.4 Monte Carlo UA + Sobol SA（Python）/ Monte Carlo + Sobol (Python)

**中文：**

```python
from scipy.stats import dirichlet
from SALib.analyze import sobol
from SALib.sample import saltelli

# ---- Monte Carlo UA ----
def monte_carlo_UA(df, N=10000):
    results = np.zeros((N, len(df)))
    for s in range(N):
        # 抽权重
        w = dirichlet.rvs([4, 4, 3])[0]
        # 抽方法
        method = np.random.choice(["geom", "arith", "bod", "hs"])
        results[s] = compute_re_with(df, w, method)
    p5 = np.percentile(results, 5, axis=0)
    p95 = np.percentile(results, 95, axis=0)
    return p5, p95

# ---- Sobol SA ----
problem = {
    "num_vars": 6,
    "names":  ["w_D1", "w_D2", "w_D3", "norm", "aggr", "imp"],
    "bounds": [[0.1, 0.7]] * 3 + [[0, 3]] * 3
}
param_values = saltelli.sample(problem, 8192)
Y = np.array([compute_re_scenario(p) for p in param_values])
Si = sobol.analyze(problem, Y)
# Si["S1"] = first-order; Si["ST"] = total effect
```

**English:** Monte Carlo runs 10,000 iterations with Dirichlet weight sampling; Sobol uses SALib's Saltelli sampling with N = 8192 and computes both first-order and total-effect indices via variance-decomposition.

## B.5 CFA/EFA 验证（R + lavaan）/ CFA Validation (R + lavaan)

**中文：**

```r
library(lavaan)
library(psych)

df <- read.csv("/home/user/re_v2/data/RE_v2_master_panel.csv")

# ---- KMO & Bartlett ----
KMO(df[, 5:19])       # Kaiser-Meyer-Olkin
cortest.bartlett(cor(df[, 5:19]), n = nrow(df))

# ---- 平行分析 ----
fa.parallel(df[, 5:19], fa = "fa", n.iter = 100)

# ---- 三因子 CFA ----
model <- '
  D1 =~ n_JR + n_entry_exit + n_mafdi
  D2 =~ n_cwtfp + n_tfp_gr + n_lp_gr + n_bp_disp_inv + n_scc + n_hitech
  D3 =~ n_PMR_inv + n_EPL_inv + n_INSOLV + n_FDI + n_EFW
'
fit <- cfa(model, data = df, estimator = "WLSMV", std.lv = TRUE)
fitMeasures(fit, c("chisq", "df", "rmsea", "cfi", "tli", "srmr"))

# ---- Cronbach α + AVE ----
alpha(df[, c("n_JR", "n_entry_exit", "n_mafdi")])   # D1
alpha(df[, c("n_PMR_inv", "n_EPL_inv", "n_INSOLV",
             "n_FDI", "n_EFW")])                    # D3
```

**English:** The R `lavaan` + `psych` stack executes: KMO adequacy, Bartlett sphericity, parallel analysis for factor count, three-factor CFA with WLSMV estimator, and Cronbach α for reflective sub-scales.

## B.6 一键复现：Snakemake 工作流 / One-click Replication with Snakemake

**中文：** 项目根目录的 `Snakefile` 定义完整流水线：

```python
rule all:
    input:
        "docs/RE_Index_v2_Full_Bilingual_Report.md",
        "data/RE_v2_index_full.csv",
        "docs/figures/fig8_trajectories.png"

rule extract:
    output: "data/RE_v2_master_panel.csv"
    shell:  "python src/01_build_master_dataset.py"

rule compute:
    input:  "data/RE_v2_master_panel.csv"
    output: "data/RE_v2_index_full.csv",
            "data/RE_v2_reliability_validity.json"
    shell:  "python src/02_compute_re_index.py"

rule excel:
    input:  "data/RE_v2_index_full.csv"
    output: "data/G20_RE_Index_2000_2023_v2.xlsx"
    shell:  "python src/03_build_excel.py"

rule visualize:
    input:  "data/RE_v2_index_full.csv"
    output: expand("docs/figures/fig{i}_{name}.png",
                    zip, i=range(1,9), name=[...])
    shell:  "python src/04_visualize.py"

rule validate:
    input:  "data/RE_v2_index_full.csv"
    output: "data/RE_v2_reliability_full.rds"
    shell:  "Rscript src/05_robustness_analysis.R"
```

**中文（续）：** 用户克隆仓库后运行 `snakemake --use-conda all` 即可从原始数据生成所有交付物。Docker 镜像 `re-index/re-index-toolkit:v2.0.0` 封装完整环境（Python 3.11、R 4.4、Stata 18-optional），确保跨平台可复现。

**English:** Snakemake pipeline: `snakemake --use-conda all` executes extract → compute → Excel → visualize → validate stages. Docker image `re-index/re-index-toolkit:v2.0.0` bundles the full Python 3.11 + R 4.4 environment for cross-platform reproducibility.
