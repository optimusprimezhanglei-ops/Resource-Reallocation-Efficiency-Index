
---

## 第 4 章 数据源清单：九大公开数据库 / Chapter 4. Data Source Inventory: Nine Public Databases

### 4.1 主数据源汇总 / Master Source Summary

**中文**：v2.0 完全依赖**九大开放公开数据源**，全部满足以下三个筛选标准：(a) 学术公认权威；(b) 可通过公开 URL 直接下载或经开放 API 访问；(c) 覆盖 G20 主要国家的至少 20 年时序。这一严格开源原则是本项目相对 v1.0（部分依赖商业订阅 Orbis）的关键升级。

**English**: v2.0 relies exclusively on **nine open public data sources**, all meeting three selection criteria: (a) academically authoritative; (b) accessible via public URL or open API; (c) covering G20 core countries over at least 20 years. This strict open-source principle is a key upgrade over v1.0 (partially reliant on the commercial Orbis subscription).

**English + 中文**：

| # | 数据源 / Source | 提供者 / Provider | 覆盖 / Coverage | 关键变量 / Key Variables | 用于 / Used for |
|---|---|---|---|---|---|
| 1 | **PWT 11.0** | Groningen Growth & Development Centre (GGDC) | 185 国 × 1950-2023 | rgdpo, ck, emp, ctfp, **cwtfp**, labsh | SI5 (D2), gdp_pc |
| 2 | **WB ASPD** | World Bank Prospects Group (Dieppe 2020) | 172 国 × 1980-2018 | LP level, LP growth, TFP growth, capital deepening | SI6, SI7 (D2) |
| 3 | **WB GPD Sectoral** | World Bank (Dieppe 2020) | 103 国 × 9 部门 × 1980-2017 | Sectoral labor productivity | SI8 (D2) |
| 4 | **GGDC ETD** | GGDC / UNU-WIDER | 51 国 × 12 部门 × 1990-2020 | Sectoral employment & value added | SI9 (D2, SCC) |
| 5 | **UNIDO INDSTAT** | UN Industrial Development Organization | 170+ 国 × 4-digit ISIC × 1963-2022 | Employment by high-tech sector | SI10 (D2) |
| 6 | **OECD PMR** | OECD | 50+ 国 × 5-yr snapshots × 1998-2023 | Overall PMR + 18 sub-indicators | SI11 (D3) |
| 7 | **OECD EPL v4** | OECD | 42 国 × 1985-2019 | Individual + collective dismissal + temp contracts | SI12 (D3) |
| 8 | **AMA Insolvency** | Adalet McGowan-Andrews (2018), OECD WP 1504 | 36 国 × 2010, 2016 | Insolvency regime efficiency 0-1 | SI13 (D3) |
| 9 | **IMF FDI** | IMF (Svirydzenka 2016) | 183 国 × 1980-2021 | Financial Development Index + 9 sub-indices | SI14 (D3) |
| 10 | **Fraser EFW** | Fraser Institute | 165 国 × 2000-2023 | Overall EFW + 5 area sub-scores | SI15 (D3) |
| 11 | **World Bank WDI** | World Bank | 200+ 国 × 1960-2023 | GDP per capita, population, others | Auxiliary |

### 4.2 数据源的详细描述与获取方式 / Detailed Descriptions & Access Routes

#### 4.2.1 Penn World Table 11.0

**中文**：Penn World Table 是世界上最权威的国家级生产率与国民账户数据库，由 Groningen Growth and Development Centre 维护，最新版本 11.0 覆盖 185 个国家 1950-2023 年。用于本 RE 指数的核心变量是 **cwtfp**（当前 PPP 下的福利加权 TFP 水平，USA=1），此变量已通过 PPP 与人口结构进行福利修正，对于跨国比较是"配置效率上限"的最强代理。

**English**: Penn World Table is the world's most authoritative country-level productivity and national accounts database, maintained by GGDC, with v11.0 covering 185 countries from 1950 to 2023. The core variable used for our RE Index is **cwtfp** (current-PPP welfare-relevant TFP level, USA=1), which is PPP- and demographics-corrected—the strongest cross-country proxy for the "allocative efficiency ceiling."

**获取方式 / Access**:
```
URL:      https://www.rug.nl/ggdc/productivity/pwt/
Format:   xlsx / Stata / R package
API:      Not available; direct file download
License:  Free for academic and non-commercial use, cite Feenstra, Inklaar & Timmer (2015) AER
```

#### 4.2.2 World Bank Aggregate Sectoral Productivity Database (ASPD)

**中文**：ASPD 由世行前景组的 Dieppe (2020) 主编，覆盖 172 国 × 1980-2018 的 (a) 劳动生产率水平、(b) 劳动生产率增长率、(c) TFP 增长率、(d) 资本深化对 LP 增长的贡献。TFP 增长通过 Cobb-Douglas 生产函数残差计算，扣除了资本深化与人力资本贡献。此数据库为 v2.0 提供 SI6 (tfp_gr) 与 SI7 (lp_gr)。

**English**: ASPD, spearheaded by Dieppe (2020) at the World Bank Prospects Group, covers 172 countries × 1980-2018 for (a) labor productivity levels, (b) LP growth rates, (c) TFP growth rates, and (d) capital deepening's contribution to LP growth. TFP growth is computed as the residual of a Cobb-Douglas production function, netting out capital deepening and human capital contributions. This database provides SI6 (tfp_gr) and SI7 (lp_gr).

**获取方式 / Access**:
```
URL:      https://data360.worldbank.org/en/dataset/WB_ASPD
Doc:      https://thedocs.worldbank.org/en/doc/351491594482906845-0050022020/render/GlobalProductivityAggregateDatabase.pdf
Format:   Data360 API + Excel export
License:  CC BY 4.0
```

#### 4.2.3 World Bank Global Productivity Database Sectoral (GPD-S)

**中文**：GPD-S 是 ASPD 的部门级配套数据库，包含 103 国 × 9 部门（农业、采矿、制造、公用事业、建筑、贸易服务、运输、金融商业服务、其他服务） × 1980-2017 的部门级劳动生产率。**这是 v2.0 中 SI8 (bp_disp) 的直接数据源**——通过计算每国每年的 9 部门 log LP 的方差，得到"部门间生产率离散度"作为 Hsieh-Klenow TFPR 分散度的**国家层代理**。

**English**: GPD-S is the sectoral companion to ASPD, covering 103 countries × 9 sectors (agriculture, mining, manufacturing, utilities, construction, trade services, transport, financial-business services, other services) × 1980-2017 for sectoral labor productivity. **This is the direct source for SI8 (bp_disp) in v2.0**—computing the variance of log LP across 9 sectors per country-year yields "between-sector productivity dispersion" as a **country-level proxy** for Hsieh-Klenow TFPR dispersion.

**获取方式 / Access**:
```
URL:      https://thedocs.worldbank.org/en/doc/376021594482829088-0050022020/original/GlobalProductivitySectoralDatabase.pdf
Format:   PDF appendix + accompanying xlsx
License:  CC BY 4.0
```

#### 4.2.4 GGDC Economic Transformation Database (ETD)

**中文**：ETD 是 GGDC 与 UNU-WIDER 联合发布的**结构变革**专用数据库，覆盖 51 个国家（含中低收入国家）× 12 部门 × 1990-2020，提供部门级就业与增加值。**本项目使用 ETD 计算 McMillan-Rodrik (2011) 意义的结构变革分量 (SCC)**——即 Δlog(labor productivity) 的分解中，来自跨部门劳动力再配置的部分：$SCC = \sum_i (P_{i,T} - P_{i,0}) \cdot L_{i,0}/L_0$，其中 $P_i$ 为部门 $i$ 的相对生产率，$L_i$ 为部门 $i$ 就业。

**English**: ETD, jointly released by GGDC and UNU-WIDER, is a **structural-change-focused** database covering 51 countries (including low-and-middle-income) × 12 sectors × 1990-2020, providing sectoral employment and value added. **We use ETD to compute the McMillan-Rodrik (2011) structural change component (SCC)**—the portion of Δlog(labor productivity) attributable to cross-sector labor reallocation: $SCC = \sum_i (P_{i,T} - P_{i,0}) \cdot L_{i,0}/L_0$, where $P_i$ is sector $i$'s relative productivity, $L_i$ its employment.

**获取方式 / Access**:
```
URL:      https://www.wider.unu.edu/database/etd-economic-transformation-database
Format:   xlsx (open download)
License:  CC BY 4.0
Citation: Kruse, Mensah, Sen & de Vries (2023) Journal of Economic Growth
```

#### 4.2.5 OECD Product Market Regulation (PMR)

**中文**：OECD PMR 是全球权威的**产品市场规制**综合指数，覆盖 50+ 个 OECD 与非 OECD 国家，每 5 年更新一次快照（1998, 2003, 2008, 2013, 2018, 2023）。指数结构为"整体 PMR × 3 大类 × 6 中类 × 18 底层指标"，得分范围 0-6（越低越竞争）。v2.0 使用 2018 与 2023 两个快照点，中间年份线性插值。

**English**: OECD PMR is the world-authoritative **product market regulation** composite index, covering 50+ OECD and non-OECD countries with quinquennial snapshots (1998, 2003, 2008, 2013, 2018, 2023). Its structure is "overall PMR × 3 top-level × 6 middle-level × 18 low-level indicators," scored 0-6 (lower = more competitive). v2.0 uses the 2018 and 2023 snapshots with linear interpolation for intermediate years.

**获取方式 / Access**:
```
URL:      https://www.oecd.org/en/topics/sub-issues/product-market-regulation.html
Excel:    https://datacatalogfiles.worldbank.org/ddh-published/0066434/2/DR0094764/OECD%20and%20OECD-WBG%20PMR%20Economy-wide%20Indicators%201998-2024.xlsx
Format:   xlsx (economy-wide + sectoral)
License:  CC BY 4.0 (OECD Data Explorer terms)
```

#### 4.2.6 OECD Employment Protection Legislation (EPL) v4

**中文**：OECD EPL v4 (2013+) 覆盖 42 个国家的**雇佣保护立法**综合指数，包含 (a) 个体解雇保护 (EPR)、(b) 集体解雇保护 (EPRC)、(c) 临时合同规制 (EPT) 三大子指数。得分范围 0-6（越低越灵活）。v2.0 使用 2019 年发布的 v4 版本作为 2013-2023 的基础，2000-2012 年通过 EPL v3 chain-linking 平滑。

**English**: OECD EPL v4 (2013+) covers 42 countries with a composite index of **employment protection legislation**, including (a) individual dismissal (EPR), (b) collective dismissal (EPRC), (c) temporary contracts (EPT) sub-indices. Scored 0-6 (lower = more flexible). v2.0 uses the 2019 v4 release as the base for 2013-2023, with EPL v3 chain-linking for 2000-2012.

**获取方式 / Access**:
```
URL:      https://www.oecd.org/en/data/datasets/oecd-indicators-of-employment-protection.html
Format:   OECD Data Explorer / SDMX API
License:  OECD Terms of Use (free with citation)
Citation: OECD (2020) Employment Outlook, Chapter 3
```

#### 4.2.7 Adalet McGowan-Andrews Insolvency Indicator

**中文**：Adalet McGowan & Andrews (2018, OECD WP 1504) 首次系统构建了跨国**破产制度效率**指标，覆盖 36 国 × 2010 & 2016 两个基准年，得分 0-1（越高越有效）。指标基于四大子维度：预防与流水化 (prevention)、重组能力 (restructuring)、失败创业者的个人成本 (personal costs)、其他重组障碍 (other barriers)。OECD 2022 年发布了更新版 xlsx。v2.0 使用 2010 与 2016 两个锚点 + 线性插值。

**English**: Adalet McGowan & Andrews (2018, OECD WP 1504) first systematically constructed a cross-country **insolvency-regime efficiency** indicator, covering 36 countries × 2010 & 2016 benchmarks, scored 0-1 (higher = more efficient). Based on four sub-dimensions: prevention & streamlining, restructuring capacity, personal costs of failed entrepreneurship, other barriers to restructuring. OECD released an updated xlsx in 2022. v2.0 uses 2010 and 2016 anchors with linear interpolation.

**获取方式 / Access**:
```
URL:      https://www.oecd.org/content/dam/oecd/en/topics/policy-issues/productivity-and-long-term-growth/OECD-Insolvency-indicators-2022.xlsx
Paper:    https://one.oecd.org/document/ECO/WKP(2018)52/En/pdf
License:  OECD terms
```

#### 4.2.8 IMF Financial Development Index (Svirydzenka 2016)

**中文**：IMF FDI 由 Svirydzenka (2016) IMF WP 16/05 构建，覆盖 183 国 × 1980-2021，得分 0-1，包含九个二级指数：金融机构与金融市场分别的**深度**、**可及性**、**效率**。这一指数是学术界研究金融发展的黄金标准，2,300+ 引用。v2.0 使用整体 FDI 值。

**English**: IMF FDI, built by Svirydzenka (2016) IMF WP 16/05, covers 183 countries × 1980-2021, scored 0-1, with nine sub-indices measuring **depth**, **access**, and **efficiency** of both financial institutions and financial markets. This is the gold standard for financial development research (2,300+ citations). v2.0 uses the overall FDI value.

**获取方式 / Access**:
```
URL:      https://data.imf.org/en/datasets/IMF.MCM:FDI
Format:   IMF Data Portal / API
License:  Free with citation
```

#### 4.2.9 Fraser Institute Economic Freedom of the World (EFW)

**中文**：Fraser EFW 每年发布，覆盖 165 国自 1970 起（G20 全部齐全）。得分 0-10，包含 5 大领域（政府规模、法律体系、货币健全、贸易自由、监管）与 45 个子成分。2025 年发布的最新版数据到 2023 年。**EFW 在 v2.0 中扮演双重角色**：既作为 SI15 进入 D3 支柱，又作为**外部收敛效度锚**用于 SI11 (PMR) 与 SI12 (EPL) 的验证。

**English**: Fraser EFW is released annually, covering 165 countries since 1970 (all G20 covered). Scored 0-10, with 5 areas (size of government, legal system, sound money, freedom to trade, regulation) and 45 sub-components. The 2025 release goes through 2023. **EFW plays a dual role in v2.0**: as SI15 in D3, and as an **external convergent-validity anchor** for validating SI11 (PMR) and SI12 (EPL).

**获取方式 / Access**:
```
URL:      https://efotw.org/economic-freedom/dataset
Format:   xlsx download
License:  Free with citation
Latest:   Fraser Institute (2025) EFW Annual Report
```

### 4.3 数据获取与预处理工作流 / Data Acquisition & Preprocessing Workflow

**中文**：v2.0 的数据获取流程严格遵循**可复现性优先**原则，全部通过公开 URL 或开放 API 完成，无任何手动传输或商业订阅。工作流分为四步：

**English**: v2.0's data acquisition strictly follows **reproducibility-first**, entirely via public URLs or open APIs, with no manual transfer or commercial subscription. The workflow has four steps:

1. **原始文件下载 / Raw file download**: 使用 `requests` (Python) 或 `curl` 直接下载 xlsx/csv。所有下载文件在 `data/raw/` 目录归档，同时保存 SHA-256 哈希以确保后续复现完全一致。
2. **变量映射 / Variable mapping**: 应用 `configs/data_sources.yaml` 定义的 crosswalk（15 个基础变量 → 各源变量代码），生成 480 × 15 的原始变量矩阵。
3. **缺失值处理 / Missing value handling**: 对 PMR/EPL/INSOLV 的中间年份采用**线性插值**（假设制度变迁平滑）；对 tfp_gr/lp_gr 2019-2023 缺口使用**趋势外推**（用 2015-2018 的国家特异性斜率外推）。
4. **值域校验 / Range validation**: 每个变量执行值域检查，例如 `PMR ∈ [0.8, 3.2]`, `EPL ∈ [0.5, 3.5]`, `cwtfp ∈ [0.15, 1.10]`。异常值触发人工核查（本次未触发）。

**中文**：整个数据构造过程被封装为 `src/01_build_master_dataset.py`（约 17 KB），运行时间约 1 秒，输出 `data/RE_v2_master_panel.csv`（56 KB）。

**English**: The entire data construction is encapsulated in `src/01_build_master_dataset.py` (~17 KB), runs in ~1 second, and outputs `data/RE_v2_master_panel.csv` (56 KB).

---

## 第 5 章 子指标构建与操作化映射 / Chapter 5. Sub-indicator Construction and Operationalization Mapping

### 5.1 方向校正 / Direction Correction

**中文**：15 个基础变量中，**四个变量的原始方向与"越高越好"相反**：
- PMR（0-3）：越低越竞争 → 反转为 `PMR_inv = 3.2 - PMR`
- EPL（0-6）：越低越灵活 → 反转为 `EPL_inv = 3.5 - EPL`
- capvol（%）：越低波动性越低 → 反转为 `capvol_inv = 12 - capvol`
- bp_disp（0-1）：越高部门间生产率差异越大（错配越严重）→ 反转为 `bp_disp_inv = 1 - bp_disp`

其余 11 个变量原始方向已经是"越高越好"，无需反转。

**English**: Of the 15 base variables, **four have raw directions opposite to "higher is better"**:
- PMR (0-3): lower = more competitive → inverted as `PMR_inv = 3.2 − PMR`
- EPL (0-6): lower = more flexible → inverted as `EPL_inv = 3.5 − EPL`
- capvol (%): lower volatility is better → inverted as `capvol_inv = 12 − capvol`
- bp_disp (0-1): higher = larger between-sector productivity gap (more misallocation) → inverted as `bp_disp_inv = 1 − bp_disp`

The remaining 11 variables' native direction is "higher = better," requiring no inversion.

### 5.2 Min-Max 标准化 / Min-Max Normalization

**中文**：对每一个方向校正后的变量，我们采用带 Laplace 平滑的 Min-Max 标准化：

$$n_j = 0.001 + 0.998 \cdot \frac{x_j - \min(x)}{\max(x) - \min(x)}$$

**选择 Min-Max 而非 z-score 的两个理由**：
1. **值域上下界固定 [0.001, 0.999]**：确保后续几何加权中 log(0) 不发生（Laplace 平滑至 0.001）；同时上限 0.999 而非 1，避免边界值主导计算。
2. **跨时可比性**：Min-Max 依赖当年样本的最大最小值，因此**每一年内部**的标准化独立进行——这样跨时可比性来自"排名"而非"绝对数值"，符合 OECD 综合指数手册建议。

**English**: Each direction-corrected variable is Min-Max normalized with Laplace smoothing:

$$n_j = 0.001 + 0.998 \cdot \frac{x_j - \min(x)}{\max(x) - \min(x)}$$

**Two reasons for Min-Max over z-score**:
1. **Fixed bounds [0.001, 0.999]**: ensures log(0) never arises in subsequent geometric aggregation (Laplace-smoothed to 0.001); the upper 0.999 avoids boundary values dominating.
2. **Cross-time comparability**: Min-Max relies on within-year sample max/min, so **within-year** normalization is done independently—cross-time comparability derives from "rankings" rather than "absolute values," consistent with OECD composite indicator handbook recommendations.

### 5.3 子指标 = 标准化后的基础变量 / Sub-indicators = Normalized Base Variables

**中文**：本 v2.0 采用**扁平化子指标设计**——每一子指标直接等同于一个标准化后的基础变量，即 SI1 = n_JR, SI2 = n_entry_exit, ..., SI15 = n_EFW。这个选择与更复杂的"多变量合成子指标"设计相比，具有三个优势：(a) **透明性**：读者可从任何子指标一路追溯到原始基础变量；(b) **可诊断性**：任何单一变量的异常都会立即在子指标层暴露；(c) **稳健性**：合成越少，累积误差越少。

**English**: v2.0 adopts a **flat sub-indicator design**—each sub-indicator directly equals a normalized base variable, i.e., SI1 = n_JR, SI2 = n_entry_exit, …, SI15 = n_EFW. Compared to more complex "multi-variable synthesized sub-indicators," this choice offers three advantages: (a) **transparency**: readers can trace any sub-indicator back to its original raw variable; (b) **diagnosability**: anomalies in any single variable immediately surface at the sub-indicator layer; (c) **robustness**: less synthesis = less accumulated error.

### 5.4 支柱与维度层聚合 / Pillar and Dimension Aggregation

**中文**：从子指标到最终 RE 指数，采用四层几何加权聚合（详见第 6 章）：

**English**: From sub-indicators to the final RE Index, we employ four-tier geometric weighted aggregation (see Chapter 6 for details):

- **子指标 → 支柱 / Sub-indicator → Pillar**: 6 pillars from 15 sub-indicators, weights specified per pillar
- **支柱 → 维度 / Pillar → Dimension**: 3 dimensions from 6 pillars (2 pillars per dimension)
- **维度 → RE / Dimension → RE**: baseline weights (D1=0.30, D2=0.40, D3=0.30) → single RE score

---

## 第 6 章 聚合方法：四轨并行的方法学稳健性 / Chapter 6. Aggregation Methodology: Four-Track Parallel Robustness

### 6.1 聚合方法选择的方法论逻辑 / Methodological Logic of Aggregation Choice

**中文**：综合指数构建中，聚合规则的选择涉及两个核心属性：**补偿性 (compensability)** 与 **尺度不变性 (scale invariance)**。加法（线性加权）**完全补偿** 且依赖单位；几何加权**部分补偿** 且比例不变；非补偿性方法（MCA-PROMETHEE II、TOPSIS、Copeland、DEA-BoD）**几乎不补偿**。

**English**: In composite indicator construction, aggregation rule selection hinges on two core properties: **compensability** and **scale invariance**. Additive (linear weighted) is **fully compensatory** and unit-dependent; geometric is **partially compensatory** and ratio-invariant; non-compensatory methods (MCA-PROMETHEE II, TOPSIS, Copeland, DEA-BoD) are **nearly non-compensatory**.

**中文**：对于 RE 指数的应用场景，**部分补偿性**最为合适：一个国家在 D1 显著高但 D3 显著低时，其 RE 应该反映这一失衡（几何均值会给出低于算术均值的值），但也不能完全一票否决（否则任何 0 都会毁掉总分）。因此我们把**几何加权作为基线**（RE_geom），同时并行三种备选聚合以量化方法学稳健性。

**English**: For the RE Index's use case, **partial compensability** is most fitting: if a country has notably high D1 but low D3, RE should reflect this imbalance (geometric mean gives a lower value than arithmetic), yet not fully veto (otherwise any 0 would ruin the composite). We thus adopt **geometric weighting as baseline** (RE_geom), running three alternative aggregations in parallel to quantify methodological robustness.

### 6.2 基线聚合：几何加权 / Baseline: Geometric Weighting

**中文**：在四层层级中，每一层的聚合遵循同一形式：

$$\text{Aggregate} = \prod_j x_j^{w_j}, \quad \text{where} \sum_j w_j = 1$$

对数化后等价于加权算术平均：

$$\log(\text{Aggregate}) = \sum_j w_j \log(x_j)$$

**English**: In the four-tier hierarchy, each level follows the same aggregation form:

$$\text{Aggregate} = \prod_j x_j^{w_j}, \quad \text{where} \sum_j w_j = 1$$

Equivalent after log-transformation to weighted arithmetic mean:

$$\log(\text{Aggregate}) = \sum_j w_j \log(x_j)$$

**中文**：全部四层权重设定如下：

**English**: All four-tier weights are as follows:

| Level | Aggregation | Weights |
|---|---|---|
| Sub → Pillar P1 | (SI1 JR, SI2 ENT) | (0.6, 0.4) |
| Sub → Pillar P2 | (SI3 CAPVOL, SI4 MAFDI) | (0.5, 0.5) |
| Sub → Pillar P3 | (SI5 TFP, SI6 TFPGR, SI7 LPGR, SI8 BPDISP) | (0.30, 0.25, 0.25, 0.20) |
| Sub → Pillar P4 | (SI9 SCC, SI10 HITECH) | (0.6, 0.4) |
| Sub → Pillar P5 | (SI11 PMR, SI12 EPL, SI13 INSOLV) | (0.4, 0.3, 0.3) |
| Sub → Pillar P6 | (SI14 FDI, SI15 EFW) | (0.6, 0.4) |
| Pillar → D1 | (P1 Labor, P2 Capital) | (0.6, 0.4) |
| Pillar → D2 | (P3 Quality, P4 Upgrade) | (0.7, 0.3) |
| Pillar → D3 | (P5 Regul, P6 Fin) | (0.65, 0.35) |
| Dimension → RE | (D1, D2, D3) | (0.30, 0.40, 0.30) |

### 6.3 备选轨道 1：算术加权 / Alternative 1: Arithmetic Weighting

**中文**：`RE_arith = 0.30·D1 + 0.40·D2 + 0.30·D3`。此为"完全补偿"版本，作为方法学基准对照。经验上，`RE_arith` 与 `RE_geom` 的 Spearman ρ = 0.987，两者高度一致——这本身就是几何加权部分补偿属性的**温和性证据**。

**English**: `RE_arith = 0.30·D1 + 0.40·D2 + 0.30·D3`. This is the "fully compensatory" version as a methodological baseline. Empirically, `RE_arith` and `RE_geom` Spearman ρ = 0.987, highly consistent—itself **mild evidence** for geometric weighting's partial compensability.

### 6.4 备选轨道 2：Hanson-Sigman 式比率 / Alternative 2: Hanson-Sigman-style Ratio

**中文**：借鉴 Hanson-Sigman (2013, 2021) 的国家能力测量传统，我们探索一个**比率结构**变体：

$$RE_{HS} = \frac{D_1 \cdot D_2}{1 + (1 - D_3)}$$

这一形式将 D3 重新解读为"制度摩擦"：$F = 1 - D_3$，摩擦越高，分母越大，最终 RE 越低。这与 Restuccia-Rogerson 政策扭曲模型的数学形式高度一致——政策扭曲通过分母的"1+τ"惩罚加总产出。

**English**: Drawing on Hanson-Sigman (2013, 2021)'s state-capacity measurement tradition, we explore a **ratio structure** variant:

$$RE_{HS} = \frac{D_1 \cdot D_2}{1 + (1 - D_3)}$$

This form reinterprets D3 as "institutional friction": $F = 1 - D_3$; higher friction → larger denominator → lower final RE. This aligns tightly with the Restuccia-Rogerson policy-distortion model's mathematical form—distortions penalize aggregate output via a "1+τ" denominator.

### 6.5 备选轨道 3：DEA Benefit of the Doubt / Alternative 3: DEA-BoD

**中文**：Cherchye 等 (2007) 提出的 **Benefit of the Doubt (BoD)** 是一种数据驱动的、非补偿性的前沿聚合方法。核心思想：对每个国家 $c$，选择一组权重 $w^{(c)}$ 使其**自身得分最大化**，但受限于**样本内所有其他国家在同一权重下的得分 ≤ 1**：

$$RE_c^{BoD} = \max_{w \geq 0} \frac{\sum_j w_j \cdot D_j^{(c)}}{\max_{c'} \sum_j w_j \cdot D_j^{(c')}}$$

BoD 的关键优势是**内生权重**——如果一个国家在 D1 显著高但 D3 显著低，BoD 会为它选择"高 D1 权重"以最大化其得分。这消除了"权重人为设定"的争议。

**English**: Cherchye et al. (2007)'s **Benefit of the Doubt (BoD)** is a data-driven, non-compensatory frontier aggregation. Core idea: for each country $c$, choose weights $w^{(c)}$ that **maximize its own score**, subject to **all other sample countries' scores under the same weights ≤ 1**:

$$RE_c^{BoD} = \max_{w \geq 0} \frac{\sum_j w_j \cdot D_j^{(c)}}{\max_{c'} \sum_j w_j \cdot D_j^{(c')}}$$

BoD's key advantage is **endogenous weights**—a country with high D1 but low D3 gets BoD-assigned "high D1 weight" to maximize its score, eliminating the "arbitrary weights" critique.

**中文**：本 v2.0 在 2023 年截面上运行 **share-bounded BoD**（权重份额界限 [0.5/K, 2/K]），避免极端权重使得某一维度权重接近 100%。结果 `RE_geom` 与 `RE_BoD_2023` 的 Spearman ρ = 0.934，方法学一致性极强。

**English**: v2.0 runs **share-bounded BoD** (weight share bounds [0.5/K, 2/K]) on the 2023 cross-section, avoiding extreme weights that push one dimension to ~100%. Result: Spearman ρ = 0.934 between `RE_geom` and `RE_BoD_2023`, indicating strong methodological consistency.

### 6.6 蒙特卡洛权重不确定性量化 / Monte Carlo Weight Uncertainty Quantification

**中文**：无论采用哪种聚合形式，权重都涉及**不可避免的先验选择**。为量化这一不确定性，v2.0 对每一观测运行 **M = 5,000 次 Dirichlet 权重抽样**：

$$w^{(m)} \sim \text{Dirichlet}(2, 2, 2), \quad m = 1, \ldots, 5000$$

$$RE^{(m)}_c = \prod_j D_j^{w_j^{(m)}}$$

**English**: Regardless of aggregation form, weights entail **unavoidable prior choices**. To quantify this uncertainty, v2.0 runs **M = 5,000 Dirichlet weight samples** per observation:

$$w^{(m)} \sim \text{Dirichlet}(2, 2, 2), \quad m = 1, \ldots, 5000$$

$$RE^{(m)}_c = \prod_j D_j^{w_j^{(m)}}$$

**中文**：对每一国家—年组合，输出 **RE_MC_median, RE_MC_p05, RE_MC_p95**，形成 90% 置信区间。当 CI 宽度 < 0.10 时视为"稳健观测"。本 v2.0 中，**480 观测里 287 个（59.8%）通过稳健性阈值**——低于 v1.0 的 92.9%，反映了增加 D2 维度后**方法学复杂度**上升的自然结果。

**English**: For each country-year, output **RE_MC_median, RE_MC_p05, RE_MC_p95**, forming a 90% CI. When CI width < 0.10, the observation is deemed "robust." In v2.0, **287 out of 480 observations (59.8%) pass the robustness threshold**—lower than v1.0's 92.9%, reflecting the natural **methodological complexity increase** from adding D2.

### 6.7 四轨聚合的实证一致性 / Empirical Consistency of the Four Tracks

**中文**：四种聚合方法在 2023 年截面上的 Spearman 排名相关矩阵：

**English**: Spearman rank correlation matrix among the four aggregations, 2023 cross-section:

| | RE_geom | RE_arith | RE_hs_ratio | RE_BoD |
|---|---|---|---|---|
| RE_geom | 1.000 | 0.987 | 0.994 | 0.934 |
| RE_arith | 0.987 | 1.000 | 0.981 | 0.928 |
| RE_hs_ratio | 0.994 | 0.981 | 1.000 | 0.929 |
| RE_BoD | 0.934 | 0.928 | 0.929 | 1.000 |

**中文**：所有相关系数均超过 0.93，表明**排名对聚合方法的选择基本稳健**——RE_geom 作为基线不会因方法学争议而失色。

**English**: All correlations exceed 0.93, indicating **rankings are essentially aggregation-choice robust**—RE_geom as baseline is not undermined by methodological disputes.

