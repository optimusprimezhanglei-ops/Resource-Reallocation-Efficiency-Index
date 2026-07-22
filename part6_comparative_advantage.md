# 第六部分 · 与现有指数的对比优势 / Part 6 · Comparative Advantages over Existing Indices

## 6.1 现有指数景观 / Landscape of Existing Indices

**中文：** 在评估 RE v2.0 的相对贡献之前，有必要梳理与其邻近的**九大既有指数家族**，这九个家族在概念覆盖、数据源、方法论上与本项目形成对话或竞争关系：

| 指数 / Index | 发布机构 | 概念焦点 | 主要方法 | 与 RE 的关系 |
|:---|:---|:---|:---|:---|
| Fraser EFW 2025 | Fraser Institute | 经济自由度（制度约束）| 5 领域算术平均 | D3 制度补集 |
| Heritage IEF | Heritage Foundation | 经济自由度 | 12 分项算术平均 | D3 制度补集 |
| WEF GCI 4.0 | World Economic Forum | 综合竞争力 | 12 支柱、103 指标 | 竞争替代 |
| IMD WCY | IMD 洛桑 | 国家竞争力 | 4 因素、300+ 指标 | 竞争替代 |
| OECD PMR | OECD | 产品市场监管严厉度 | 6 层级、~1450 问题 | RE 内嵌 D3 变量 |
| World Bank Doing Business / B-READY | 世界银行 | 营商便利度 | 10-12 主题、原子分数 | D3 制度补集 |
| PWT TFP | Groningen 大学 | 全要素生产率 | 双重变形约束+成本函数 | RE 内嵌 D2 变量 |
| Hsieh-Klenow TFPQ Gap | Hsieh-Klenow 2009 | 企业级配置扭曲 | ln(TFPR) 方差 | 概念先驱 |
| OECD 生产率仪表板 | OECD | 多层次生产率 | MultiProd + DynEmp | 数据源之一 |

**English:** Nine adjacent index families define the intellectual neighborhood of RE v2.0: (1) Fraser EFW; (2) Heritage IEF; (3) WEF GCI; (4) IMD WCY; (5) OECD PMR; (6) World Bank Doing Business / B-READY; (7) Penn World Table TFP; (8) Hsieh-Klenow TFPQ Gap; (9) OECD Productivity Dashboard. Each occupies a partly overlapping but distinct conceptual niche relative to RE.

---

## 6.2 六维度对比矩阵 / Six-Dimensional Comparison Matrix

**中文：** 我们在六个方法论维度上系统对比 RE v2.0 与主要竞品：

| 方法维度 | RE v2.0 | Fraser EFW | Heritage IEF | WEF GCI | OECD PMR | PWT TFP | HK-TFPQ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **概念焦点** | 动态再配置 | 制度自由 | 制度自由 | 竞争力综合 | 监管严厉度 | 要素生产率 | 配置扭曲 |
| **过程 D1** | ✓✓✓ | ✗ | ✗ | 部分 | ✗ | ✗ | ✓✓✓ |
| **结果 D2** | ✓✓✓ | ✗ | 部分 | ✓✓ | ✗ | ✓✓✓ | ✓ |
| **制度 D3** | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓ | ✓✓ | ✗ | ✗ |
| **国家覆盖** | 20 (可扩) | 165 | 178 | 141 | 50 | 185 | ~20 |
| **时间覆盖** | 2000-23 | 1970-23 | 1995-23 | 2007-19 | 1998-23 | 1950-23 | 静态 |
| **数据源公开** | ✓✓✓ | ✓✓ | ✓✓ | 部分 | ✓✓ | ✓✓✓ | 私有 |
| **方法透明度** | ✓✓✓ | ✓✓ | ✓ | ✓ | ✓✓✓ | ✓✓✓ | ✓✓ |
| **信度检验** | Cronbach α, ω | 报告部分 | 部分 | 部分 | 强 | 无 | 无 |
| **效度检验** | 六层完整 | 部分 | 部分 | 部分 | 强 | 无 | 无 |
| **UA/SA** | Monte Carlo + Sobol | 无 | 无 | 无 | 无 | 无 | 无 |
| **可复现性** | ✓✓✓ (GitHub+Docker) | 部分 | ✗ | ✗ | 部分 | ✓✓ | ✗ |
| **形成性/反映性** | 混合建模 | 反映性 | 反映性 | 反映性 | 混合 | 形成性 | 形成性 |

RE v2.0 的核心相对优势体现在：**（i）过程+结果+制度三维完整覆盖**、**（ii）方法论透明度与可复现性居首**、**（iii）唯一系统实施 UA/SA 稳健性检验**。

**English:** RE v2.0 dominates on three fronts: **(i) triple-dimensional coverage** (Process + Outcome + Institution) — no other index covers all three; **(ii) methodological transparency and reproducibility** — the only fully open-source stack (Python/R/Docker/Snakemake) with public replication data; **(iii) systematic UA/SA robustness** — the only index that applies Monte Carlo (N=10,000) and Sobol global sensitivity analysis.

---

## 6.3 与 Fraser EFW 的深入对比 / Deep Comparison with Fraser EFW

**中文：** Fraser EFW 是最广泛使用的制度维度指数（1970–2023，165 国），也是 RE v2.0 D3 的重要数据源之一。二者的分野与互补关系至关重要：

**（1）概念定位**：EFW 测量"经济自由度"——即政府对个人经济决策的约束程度（政府规模、法治、货币、贸易、监管）。它是**静态存量**指标——描述某时点上的制度状态。RE 则测量**再配置效率**——即资源从低效用向高效用重新配置的能力，是**动态流量**概念，包含制度约束（EFW 覆盖部分）、过程强度（EFW 完全不覆盖）与结果质量（EFW 完全不覆盖）。

**（2）方法差异**：EFW 使用五大领域等权算术平均，各领域内部使用非线性 0–10 映射（多数为端点归一化）；RE 采用几何聚合，惩罚极端不均衡。EFW 未实施 CFA/EFA、Monte Carlo UA、Sobol SA；RE 全部实施。

**（3）经验分歧的信息价值**：如第 5.7 节所示，RE 与 EFW 的国家排名 Spearman ρ = 0.859，收敛良好，但 Japan (RE #11 vs. EFW #5)、Saudi Arabia (RE #18 vs. EFW #16)、Turkey (RE #12 vs. EFW #20) 的差异揭示了 EFW **无法捕捉**的信息：过程强度停滞、结构单一化、近期改革动能。RE 与 EFW **应视为互补而非替代**——EFW 提供制度快照，RE 提供再配置动力学诊断。

**English:** Fraser EFW is the most-used *static institutional stock* index; RE is a *dynamic reallocation flow* index. The two are correlated (ρ = 0.859) but capture different information — Japan (RE #11 vs. EFW #5), Saudi Arabia, and Türkiye reveal what EFW misses: process stagnation, sectoral monoculture, and recent-reform dynamics. RE and EFW are **complementary**, not substitutes.

---

## 6.4 与 WEF Global Competitiveness Index 的对比 / Comparison with WEF GCI

**中文：** WEF GCI 4.0（2017 版本后）覆盖 141 国 × 12 支柱 × 103 指标，是综合竞争力测量的行业金标准。然而，GCI 因方法学争议与数据缺失于 2020 年停止发布年度报告（转为"竞争力主题重启"报告）。

RE 相对 GCI 的方法学优势：

1. **概念聚焦**：GCI 目标是"综合竞争力"，导致指标构成庞杂（涵盖健康、教育、宏观稳定、创新、基础设施等），实际是"发展综合指数"。RE 严格聚焦"资源再配置效率"这一单一构念，边界清晰。
2. **数据源公开**：GCI 依赖大量私有执行调查（Executive Opinion Survey，~13,000 CEO 主观打分），主观性强、样本非随机。RE 全部使用公开的宏观/微观定量数据。
3. **方法透明度**：GCI 权重使用"专家判断+简单加权"，非完全透明。RE 使用等权基线 + 多种敏感性替代（专家/熵/BoD）。
4. **可复现性**：GCI 无公开可运行代码。RE 提供完整 Python/R 管道 + Docker + Snakemake。

**English:** WEF GCI 4.0's compound "development composite" nature (12 pillars, 103 indicators) contrasts with RE's tightly scoped "reallocation efficiency" construct. GCI relies heavily on subjective CEO surveys (~13,000 responses); RE uses exclusively public quantitative data. GCI code and pipeline are proprietary; RE is fully open-source. Since 2020, WEF has suspended annual GCI publication — providing an opportunity for RE to fill the "system-level dynamic-comparison" gap.

---

## 6.5 与 OECD PMR / EPL 的对比 / Comparison with OECD PMR / EPL

**中文：** OECD PMR（Product Market Regulation）与 EPL（Employment Protection Legislation）是本领域最严格的制度测量工具，也是 RE v2.0 D3 的关键数据源。RE 与之的关系是**上游数据整合，而非替代**：

- **PMR/EPL 优势**：极高的深度（PMR 涵盖 ~1,450 个 yes/no 或多档问题）；严格的方法学（专家编码、外部校验）；OECD 官方权威。
- **PMR/EPL 局限**：只覆盖制度维度，不含过程与结果；只覆盖 OECD + 6 partner 国家（50 国左右）；每 5 年更新一次，缺乏年度分辨率。

RE 将 PMR 与 EPL 作为 D3 的两个次级指标（各占 D3 权重 20%），并**扩展**至 G20 完整样本（含非 OECD 的 CHN, IND, IDN, BRA, ZAF, RUS, SAU, ARG），并对缺失年份使用线性插值。这样 RE 既保留了 PMR/EPL 的深度，又实现了**更广的国别覆盖**与**更细的时间分辨率**。

**English:** OECD PMR and EPL are the gold-standard institutional depth measures but are limited to institution dimension only and to ~50 countries updated every 5 years. RE v2.0 embeds PMR and EPL as D3 sub-indicators (20% weight each) and *extends* coverage to the full G20 (including non-OECD BRICS + AR/SA) with annual linear interpolation — trading marginal depth for **breadth and temporal granularity**.

---

## 6.6 与 Hsieh–Klenow (2009) 及其后续文献的对比 / Comparison with the Hsieh–Klenow Programme

**中文：** [Hsieh & Klenow (2009, QJE)](https://web.stanford.edu/~klenow/HK.pdf) 是资源再配置研究的经典基础文献，通过测量企业级 TFPR（收入 TFP）方差量化"配置扭曲"，指出印度、中国若消除配置扭曲，TFP 可提升 30–60%。HK 框架的贡献是**理论基础**与**微观量化**，但 HK 本身**并非合成指数**——它是一个理论测量框架，需要企业级数据（如 ASI、中国工业企业数据库），不产出可比的国家排名。

RE v2.0 与 HK 的关系：**RE 是 HK 的"国家—年份合成指数化"实现**。RE 在概念上继承 HK 的核心洞见（配置扭曲 → TFP 差距），但在操作上做出三大突破：

1. **国家—年份分辨率**：HK 需要企业微数据（受限于数据可得性 + 保密要求），只能对少数国家某几个年份进行测量。RE 使用可公开获取的宏观/中观数据实现所有国家的年度测量。
2. **多维度整合**：HK 只测量结果扭曲（TFPR 方差），不测量过程强度（JR 等）与制度约束（PMR 等）。RE 融合三维。
3. **政策解释性**：HK 的 TFPR 方差本身难以解释（是税收、金融摩擦、地方保护等多种扭曲的混合）。RE 的三维分解允许对具体政策工具（改革劳动法、开放市场、破产制度改革）的针对性建议。

**English:** [Hsieh & Klenow (2009)](https://web.stanford.edu/~klenow/HK.pdf) established the theoretical foundation via firm-level TFPR variance but is not itself a composite index — it requires confidential firm microdata and cannot produce comparable country-year rankings. RE v2.0 is the **country-year compositization of the HK programme**: it inherits the theoretical insight (misallocation → TFP gap) but delivers annual, cross-country, policy-decomposable rankings using public data. Beyond that, RE extends HK by integrating process (D1) and institutional (D3) dimensions that HK's outcome-only approach omits.

---

## 6.7 与 OECD MultiProd / DynEmp 的对比 / Comparison with OECD MultiProd / DynEmp

**中文：** OECD MultiProd 与 DynEmp 是当前最先进的微观生产率与企业动态测量系统（各国统计办公室按标准化脚本处理保密企业数据，产出可公开的聚合指标）。二者是 RE 的重要数据基础，也是概念上的近邻。

RE 相对 MultiProd/DynEmp 的定位：

- **MultiProd/DynEmp 是"生产率/企业动态诊断工具集"**——分维度公布 TFP 离散度、生产率增长、进入退出率、生存函数等，但**不聚合**为单一指数。
- **RE 是"聚合指数"**——将 MultiProd/DynEmp 的多个维度整合为可用于跨国排名与政策沟通的 0-1 分数。
- **互补关系**：政策分析师使用 MultiProd/DynEmp 进行**深度诊断**，使用 RE 进行**跨国基准与沟通**。RE v2.0 的 D1 与 D2 大量利用 MultiProd/DynEmp 中的公开变量（bp_disp, tfp_gr, entry_exit）。

**English:** OECD MultiProd and DynEmp deliver rich dimensional diagnostic panels but do not aggregate to a single index. RE v2.0 aggregates their public variables (bp_disp, tfp_gr, entry_exit, etc.) into a policy-communicable 0–1 composite. The two tool-sets are complementary: MultiProd/DynEmp for depth diagnostics, RE for cross-country benchmarking.

---

## 6.8 RE v2.0 的五大原创贡献 / Five Original Contributions of RE v2.0

**中文：** 综合上述对比，RE v2.0 在既有指数景观中的独特贡献可总结为五点：

**贡献一：概念创新——从"静态存量"到"动态流量"的范式跃迁**

现有指数（EFW/IEF/GCI/PMR）主要测量制度状态或综合竞争力，均为静态存量概念。RE 首次将"再配置效率"作为**独立的构念**——不测量制度存量本身，而测量制度、过程与结果如何**协同产生资源流动**。这一"动态流量"视角源自 [Restuccia & Rogerson (2008)](https://www.nber.org/system/files/working_papers/w13018/w13018.pdf) 与 [Hsieh & Klenow (2009)](https://web.stanford.edu/~klenow/HK.pdf) 的理论突破，但**首次在合成指数层面完整实现**。

**贡献二：数据整合——首个融合宏观/中观/微观三层次的公开可复现数据集**

现有指数使用单一层级数据：EFW 主要宏观，MultiProd 主要微观。RE 将三层级整合：（i）宏观 TFP（PWT 11.0）作为国家总生产率锚；（ii）行业级劳动生产率（World Bank GPD、GGDC ETD）作为结构再配置代理；（iii）企业动态（OECD DynEmp）作为微观流动信号。这一"三层数据金字塔"是首次在开源合成指数中实现。

**贡献三：方法学突破——五项技术创新**

- **形成性—反映性混合建模**：D1/D3 反映性（Cronbach α + CFA + AVE），D2 形成性（MIMIC + VIF），首次在合成指数中系统区分。
- **DEA-BoD 稳健对照**：使用 Cherchye et al. 的份额上下界 BoD 版本，产生方法学替代排名（ρ = 0.934 vs 几何主排名）。
- **Sobol 全局敏感性**：使用 Saltelli-Jansen pick-freeze，识别权重为主导不确定性源（S_T = 0.58 for w_D3），指导后续应用。
- **马尔科夫分位数持续性**：将时间稳定性从"平均秩相关"升级为"分位数转移矩阵"，捕捉收敛俱乐部结构。
- **危机预测效度**：首次系统验证 RE → COVID-19 恢复的领先预测力（β = 1.24, p = 0.014）。

**贡献四：透明度与可复现性——完全开源工具链**

现有指数中，Fraser EFW 与 Heritage IEF 部分公开数据，但未公开完整代码；WEF/IMD 更为封闭。RE v2.0 提供：（i）GitHub 公开源代码仓库（Python + R + Snakemake + Dockerfile）；（ii）Zenodo 存档的数据集（DOI）；（iii）一键复现的 `snakemake --use-conda all` 命令；（iv）13 单元测试。任何研究者可在 30 分钟内在自己机器上复制全部结果。

**贡献五：政策解释性——三维分解允许工具靶向的改革建议**

现有指数（EFW/GCI）的单一综合分数难以直接指向政策改革工具。RE 的三维（D1/D2/D3）与十二次级（JR/entry-exit/mafdi/cwtfp/tfp_gr/lp_gr/scc/hitech/PMR/EPL/INSOLV/FDI/EFW）分解允许识别**具体改革抓手**——例如，日本改进方向是 D1（劳动力市场 + 企业动态），中国改进方向是 D3（产权 + 破产 + 金融），法国改进方向是 D3（PMR/EPL 简化）。

**English:** RE v2.0's five original contributions: (1) **paradigm shift** from static-stock to dynamic-flow measurement of institutional effectiveness; (2) **first open, replicable macro-meso-micro integration** across PWT, World Bank, GGDC, OECD, IMF, and Fraser sources; (3) **five methodological innovations** — formative/reflective mixed modeling, DEA-BoD robust checks, Sobol global sensitivity, Markov-quantile persistence, and crisis-prediction criterion validity; (4) **fully open-source toolchain** with GitHub + Zenodo + Snakemake + Docker + unit tests; (5) **policy decomposability** — the three-dimensional structure identifies country-specific reform levers (Japan: D1 process; China: D3 institution; France: D3 regulation).

---

## 6.9 局限性与谦卑声明 / Limitations and Humility

**中文：** RE v2.0 也存在若干应当明确承认的局限：

1. **G20 样本仅 20 国**：虽然占全球 85% GDP，但对小型开放经济体（新加坡、爱尔兰、瑞士、以色列）与最不发达国家的适用性尚待检验。v3.0 计划扩至 OECD 38 与 65 个新兴市场。
2. **D1 部分数据依赖代理**：JR（岗位重新配置率）在部分新兴市场（阿根廷、沙特）的官方数据不齐全，本项目使用行业级劳动就业变动近似，可能引入测量误差。
3. **年度数据分辨率**：PMR 每 5 年一次，EPL 不规则更新，需要线性插值。对于变化剧烈的国家（如土耳其近年制度变动），插值可能低估实际波动。
4. **权重的价值判断**：等权基线是"最小假设"选择，但仍是一种选择。用户可能有理由使用不同权重（例如更强调制度）。UA 显示权重是最大不确定性源，因此我们**建议使用者始终报告 90% CI**。
5. **无法完全消除生产率测量误差**：TFP 本身是残差概念，含有测量误差。这是所有 TFP-based 指数的共性局限。

**English:** RE v2.0 acknowledges five limitations: (1) G20-only sample requires extension to OECD-38 and 65 emerging markets; (2) JR proxies introduce measurement error for some non-OECD countries; (3) 5-year PMR/annual interpolation may smooth genuine institutional volatility; (4) equal-weight baseline is a value choice — users should report 90% MC-CI bounds; (5) TFP residual measurement error is a shared limitation of all TFP-based indices. These limitations motivate the transparent open-source design: users can adjust and re-run.
