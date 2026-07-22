# 附录 A · 完整数学公式与推导 / Appendix A — Complete Mathematical Formulation

## A.1 归一化 / Normalization

**中文：** 为了将不同度量单位的指标统一到 [0, 1] 区间，我们对每个原始变量 $x_{it,k}$（国家 $i$、年份 $t$、指标 $k$）采用**面板 Min-Max 归一化**（全样本 480 观测的极值）：

$$
\tilde{x}_{it,k} = \frac{x_{it,k} - \min_{i,t}(x_{i,t,k})}{\max_{i,t}(x_{i,t,k}) - \min_{i,t}(x_{i,t,k})}
$$

对负向指标（如 PMR、EPL、BP dispersion——数值越大表示越差），先取相反数或倒数后再归一化。这一处理方式的核心优势是：（i）保留跨国、跨年可比性；（ii）0 与 1 分别对应全样本最差与最佳；（iii）计算简单、易于解释。当某国某年份出现完全缺失时，我们采用**KNN(k=5)插补**——利用邻近 5 个国家（Mahalanobis 距离最近）的同年份数据加权平均填补。

**English:** All raw indicators are rescaled to [0, 1] via panel-wide Min-Max normalization over the 480 country-year sample. Negative-direction indicators (PMR, EPL, BP dispersion) are inverted before normalization. Missing values are imputed via k-nearest-neighbor (k=5, Mahalanobis metric).

## A.2 权重体系的完整表达 / Full Weight System

**中文：** RE v2.0 采用**分层等权 + 稳健替代**的权重架构：

- **主排名：等权基线**——D1, D2, D3 三维使用等权重 $(w_1, w_2, w_3) = (1/3, 1/3, 1/3)$；每个维度内部次级指标等权。
- **敏感性替代 A：主观 AHP**——通过 [Saaty (1980)](https://www.rwspublications.com/books/analytic-hierarchy-process/) 层次分析法，构造成对比较矩阵，特征向量法解出权重。经三位领域专家平均：$w = (0.30, 0.40, 0.30)$，D2 权重略高（因结果最直接反映再配置效率）。
- **敏感性替代 B：客观熵权法**——Shannon 熵表示每个指标的"信息含量"，熵越低（分布越分散）权重越高：

$$
w_k^{\text{entropy}} = \frac{1 - H_k}{\sum_{k'}(1 - H_{k'})}, \quad H_k = -\frac{1}{\ln N}\sum_{it}\tilde{x}_{it,k}\ln\tilde{x}_{it,k}
$$

- **敏感性替代 C：CRITIC 权重**——考虑指标间对比强度（标准差）与冲突性（相关矩阵）的复合权重（[Diakoulaki et al. 1995](https://www.sciencedirect.com/science/article/abs/pii/030505489400059H)）：

$$
w_k^{\text{CRITIC}} = \frac{\sigma_k \sum_{k'}(1 - r_{k,k'})}{\sum_{k}\sigma_k \sum_{k'}(1 - r_{k,k'})}
$$

- **敏感性替代 D：PCA 权重**——首主成分方差贡献占比：$w_k^{\text{PCA}} = \sqrt{\lambda_1}\ell_{1,k}$。
- **敏感性替代 E：BWM 权重**——Best-Worst 方法（[Rezaei 2015](https://www.sciencedirect.com/science/article/abs/pii/S0305048314001480)）通过最佳与最差指标的成对比较求解优化问题。
- **合成权重（Bates-Granger 最小化）**：将上述五种权重通过 Bates-Granger 组合最小化预测误差方差：

$$
w^{\text{final}} = \arg\min_{\alpha \in \Delta^5} \text{Var}\left(\sum_j \alpha_j RE^{(j)}\right)
$$

**English:** The weight system layers an equal-weight baseline with five alternative schemes (AHP, Shannon entropy, CRITIC, PCA, BWM) combined via Bates-Granger variance-minimizing convex combination. This produces a "consensus" weight vector while allowing all five to be reported for transparency.

## A.3 几何聚合 / Geometric Aggregation

**中文：** 三维分数按几何平均聚合：

$$
RE_{it} = \left(\prod_{d=1}^{3} P_{d,it}^{w_d}\right) = \left(P_{1,it}^{1/3} \cdot P_{2,it}^{1/3} \cdot P_{3,it}^{1/3}\right)
$$

其中 $P_{d,it}$ 为国家 $i$ 年份 $t$ 在维度 $d$ 的分数。几何平均相较算术平均的核心优势是**惩罚极端不均衡**：假如国家 A 在三维分数为 (0.9, 0.9, 0.1)，B 为 (0.6, 0.6, 0.7)：

- 算术平均：$A = 0.63, B = 0.63$（并列）
- 几何平均：$A = 0.43, B = 0.63$（B 领先）

这一性质对 RE 概念至关重要——**再配置效率需要三维协同**，任何单一维度的严重短板都不应被其他维度掩盖。这与 UNDP HDI 2010 版从算术均值切换到几何均值的方法论理由完全一致（[Klugman, Rodriguez & Choi 2011, HDR Research Paper](https://hdr.undp.org/system/files/documents/hdrp201101.pdf)）。为处理零值，我们对每个归一化分数施加 Laplace 平滑 ε = 0.001：$P^{\ast} = P + \varepsilon$。

**English:** Geometric aggregation ($RE = \prod_d P_d^{w_d}$) is preferred over arithmetic averaging because it penalizes extreme imbalance among dimensions — a critical property for RE, where all three fronts must move together. A Laplace ε = 0.001 smoothing handles zero-boundary edge cases. This mirrors UNDP HDI's 2010 methodological shift documented in [Klugman et al. (2011)](https://hdr.undp.org/system/files/documents/hdrp201101.pdf).

## A.4 DEA-BoD 稳健对照 / DEA-BoD Robustness Check

**中文：** 数据包络分析的"疑罪从无"聚合器（Benefit of the Doubt）由 [Cherchye, Moesen & Van Puyenbroeck (2004)](https://www.napawatersheds.org/img/managed/Document/3424/Cherchye2006%20AnIntroduction2BenefitOfTheDoubtCompositeIndicators.pdf) 提出。对每个国家 $i$，求解线性规划：

$$
\max_{w \geq 0} \quad RE_i^{BoD} = \sum_k w_{i,k} \tilde{x}_{i,k}
$$

$$
\text{s.t.} \quad \sum_k w_{i,k} \tilde{x}_{j,k} \leq 1 \quad \forall j \in \text{sample}
$$

即"允许每个国家选择对自己最有利的权重，但需要在此权重下所有其他国家分数 ≤ 1"。为避免极端权重（某国将所有权重赋予单一指标），我们添加**份额约束（share bounds）**：

$$
L_k \leq \frac{w_{i,k} \tilde{x}_{i,k}}{\sum_{k'} w_{i,k'} \tilde{x}_{i,k'}} \leq U_k
$$

设 $(L_k, U_k) = (0.1, 0.6)$（[Cherchye et al. 2007](https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=1462660)）。这样每个指标的贡献占比被限制在 10%–60%，避免退化到"单指标独裁"。

**RE_BoD 与主排名 RE_geom 的 Spearman ρ = 0.934**——这一高度一致性是最强的方法学稳健性证据。

**English:** DEA Benefit-of-the-Doubt allows each country data-endogenous weights subject to a "no country >1" constraint. Share bounds (L_k = 0.1, U_k = 0.6) prevent single-indicator dictatorship. The 0.934 Spearman correlation between RE_BoD and equal-weight RE_geom is the strongest methodological robustness evidence.

## A.5 Monte Carlo 不确定性分析 / Monte Carlo UA

**中文：** N = 10,000 次抽样中，对每次抽样 $s$：

1. **权重扰动**：$(w_1, w_2, w_3)^{(s)} \sim \text{Dirichlet}(4, 4, 3)$，即以 (1/3, 1/3, 1/3) 为中心的宽先验。
2. **归一化方法**：$M^{(s)} \sim \text{Uniform}\{Min\text{-}Max, z\text{-}score, rank\}$。
3. **聚合方法**：$A^{(s)} \sim \text{Uniform}\{geometric, arithmetic, BoD, HS\text{-}ratio\}$。
4. **插补方法**：$I^{(s)} \sim \text{Uniform}\{mean, KNN, MICE\}$。
5. **计算** $RE_{i,t}^{(s)}$ 并存储 10,000 次结果。
6. **统计**：中位数 $RE_{i,t}^{med}$、90% CI 上下界 $[p_5, p_{95}]$、CI 宽度 $\Delta_{i,t} = p_{95} - p_5$。

稳健性等级判定：Grade A 若 $\Delta \leq 0.10$，Grade B 若 $0.10 < \Delta \leq 0.20$，Grade C 若 $\Delta > 0.20$。59.8% 的国家-年份达到 Grade A。

**English:** 10,000 Monte Carlo iterations jointly perturb weights (Dirichlet(4,4,3)), normalization method, aggregation rule, and imputation strategy. Grade A (CI ≤ 0.10) is achieved by 59.8% of country-years.

## A.6 Sobol 全局敏感性分析 / Sobol Global SA

**中文：** 使用 Saltelli-Jansen pick-freeze 估计器（[Saltelli et al. 2010, Computer Physics Communications](https://www.sciencedirect.com/science/article/abs/pii/S0010465509003087)）：

- **一阶指数** $S_i$：单变量 $X_i$ 对输出方差的独立贡献
- **总效应指数** $S_{Ti}$：$X_i$ 及其所有交互对输出方差的总贡献

$$
S_i = \frac{\text{Var}_{X_i}[\mathbb{E}_{X_{-i}}(Y | X_i)]}{\text{Var}(Y)}, \quad S_{Ti} = \frac{\mathbb{E}_{X_{-i}}[\text{Var}_{X_i}(Y | X_{-i})]}{\text{Var}(Y)}
$$

估计器：

$$
\hat{S}_i = \frac{1}{N}\sum_{j=1}^{N} B_j (A_j^{(i)} - A_j), \quad \hat{S}_{Ti} = \frac{1}{2N}\sum_{j=1}^{N} (A_j - A_j^{(i)})^2
$$

其中 $A, B$ 为两个独立随机样本矩阵，$A^{(i)}$ 是 $A$ 中第 $i$ 列被 $B$ 中同列替换后的矩阵。样本 $N = 8192$（$2^{13}$，充分保证收敛）。结果：$S_T(w_{D3}) = 0.58$、$S_T(w_{D1}) = 0.47$，权重支配总方差的 73%。

**English:** Saltelli-Jansen pick-freeze estimator (N = 8192) computes first-order S_i and total-effect S_Ti indices. Weights dominate: S_T(w_D3) = 0.58, S_T(w_D1) = 0.47, accounting for 73% of total variance.

## A.7 SEM 结构方程模型 / SEM Structural Equation Model

**中文：** 在 R `lavaan` 中拟合三因子 CFA 模型的完整语法：

```r
library(lavaan)

model_re <- '
  # Measurement model
  D1_process   =~ n_JR + n_entry_exit + n_mafdi
  D2_outcome   =~ n_cwtfp + n_tfp_gr + n_lp_gr + n_bp_disp_inv + n_scc + n_hitech
  D3_institution =~ n_PMR_inv + n_EPL_inv + n_INSOLV + n_FDI + n_EFW

  # Factor correlations
  D1_process ~~ D2_outcome
  D1_process ~~ D3_institution
  D2_outcome ~~ D3_institution
'

fit <- cfa(model_re, data = df_norm,
           estimator = "WLSMV",
           std.lv = TRUE)

summary(fit, fit.measures = TRUE, standardized = TRUE)
```

WLSMV 估计器适用于**部分观测变量偏态严重**的情形（如 JR、hitech 在部分国家呈偏斜分布），比 ML 更稳健。拟合优度：$\chi^2/df = 2.71$（阈值 <3）、RMSEA = 0.058（阈值 ≤0.08）、CFI = 0.947、TLI = 0.932、SRMR = 0.049，全部通过。

**English:** CFA fitted with lavaan's WLSMV estimator (robust to skewed indicators): χ²/df = 2.71, RMSEA = 0.058, CFI = 0.947, TLI = 0.932, SRMR = 0.049 — all within thresholds.
