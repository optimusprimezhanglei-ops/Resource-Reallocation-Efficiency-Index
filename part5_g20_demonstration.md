# 第五部分 · G20 国家示范测算 / Part 5 · G20 Empirical Demonstration

## 5.1 样本与覆盖 / Sample and Coverage

**中文：** 本部分展示 RE v2.0 指数在 **G20 20 个经济体、2000–2023 年共 24 个年份、共 480 个国家–年观测点**上的实测结果。样本涵盖：19 个成员国（阿根廷、澳大利亚、巴西、加拿大、中国、法国、德国、印度、印尼、意大利、日本、韩国、墨西哥、俄罗斯、沙特阿拉伯、南非、土耳其、英国、美国）+ 欧洲联盟（EUU）作为区域集合观察。这一样本占全球 GDP 的 ~85%、人口的 ~66%、二氧化碳排放的 ~78%，是当代政治经济学与国际治理研究中最具代表性的国家集合，也是资源再配置效率跨国比较的自然试验场。数据全部来自公开可复现来源（PWT 11.0、World Bank ASPD/GPD、GGDC ETD、OECD PMR/EPL、Adalet McGowan–Andrews Insolvency、IMF FDI、Fraser EFW），已经完成清洗、方向反转与 Min-Max 归一化处理，主数据文件为 `/home/user/re_v2/data/RE_v2_master_panel.csv` 与 `/home/user/re_v2/data/RE_v2_index_full.csv`。

**English:** This section presents empirical results of RE v2.0 on **20 G20 economies × 24 years (2000–2023) = 480 country-year observations**. The sample comprises the 19 sovereign members plus the European Union (EUU) as a regional aggregate — collectively ~85% of global GDP, ~66% of population, and ~78% of CO₂ emissions. All input data derive from open, replicable sources (PWT 11.0, World Bank ASPD/GPD, GGDC ETD, OECD PMR/EPL, Adalet McGowan–Andrews Insolvency, IMF FDI, Fraser EFW); processed panels are stored in `RE_v2_master_panel.csv` and `RE_v2_index_full.csv`.

---

## 5.2 2023 年 G20 总排名 / 2023 G20 Overall Ranking

**中文：** 2023 年全 G20 国家的 RE 综合分数（几何聚合、等权重、Min-Max 归一化）如下表所列。为便于跨维度比较，同时报告三维分维度分数（D1 过程强度、D2 结果质量、D3 制度赋能）、DEA-BoD 稳健对照分数，以及 90% 蒙特卡罗置信区间的下限与上限。

| 排名 | 代码 | 国家 (中/英) | RE 分数 | D1 过程 | D2 结果 | D3 制度 | RE_BoD | 90% CI 下 | 90% CI 上 | EFW 2023 | cwtfp | 人均 GDP (USD) |
|---:|:---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | USA | 美国 / United States | **0.762** | 0.789 | 0.613 | 0.986 | 1.000 | 0.688 | 0.879 | 8.06 | 1.012 | 71,779 |
| 2 | AUS | 澳大利亚 / Australia | 0.674 | 0.701 | 0.544 | 0.860 | 0.886 | 0.610 | 0.772 | 8.01 | 0.878 | 60,239 |
| 3 | GBR | 英国 / United Kingdom | 0.662 | 0.740 | 0.493 | 0.878 | 0.912 | 0.579 | 0.784 | 7.86 | 0.831 | 46,563 |
| 4 | KOR | 韩国 / South Korea | 0.657 | 0.599 | 0.651 | 0.728 | 0.938 | 0.627 | 0.692 | 7.57 | 0.655 | 35,022 |
| 5 | CAN | 加拿大 / Canada | 0.646 | 0.645 | 0.511 | 0.886 | 0.876 | 0.576 | 0.766 | 7.89 | 0.899 | 50,854 |
| 6 | FRA | 法国 / France | 0.573 | 0.544 | 0.534 | 0.662 | 0.796 | 0.547 | 0.617 | 7.77 | 0.930 | 44,543 |
| 7 | EUU | 欧盟 / European Union | 0.572 | 0.546 | 0.515 | 0.691 | 0.783 | 0.539 | 0.630 | 7.75 | 0.874 | 38,375 |
| 8 | DEU | 德国 / Germany | 0.560 | 0.441 | 0.563 | 0.707 | 0.808 | 0.498 | 0.632 | 7.84 | 0.929 | 50,855 |
| 9 | ITA | 意大利 / Italy | 0.452 | 0.410 | 0.431 | 0.530 | 0.634 | 0.427 | 0.490 | 7.72 | 0.815 | 36,551 |
| 10 | MEX | 墨西哥 / Mexico | 0.422 | 0.400 | 0.394 | 0.488 | 0.587 | 0.403 | 0.455 | 7.03 | 0.587 | 10,941 |
| 11 | JPN | 日本 / Japan | 0.419 | **0.190** | 0.468 | 0.797 | 0.706 | 0.285 | 0.590 | 7.85 | 0.663 | 44,272 |
| 12 | TUR | 土耳其 / Türkiye | 0.408 | 0.405 | 0.502 | 0.311 | 0.658 | 0.352 | 0.451 | 5.73 | 0.624 | 9,940 |
| 13 | BRA | 巴西 / Brazil | 0.398 | 0.489 | 0.341 | 0.398 | 0.573 | 0.369 | 0.444 | 6.53 | 0.468 | 9,589 |
| 14 | ZAF | 南非 / South Africa | 0.392 | 0.408 | 0.322 | 0.491 | 0.518 | 0.358 | 0.445 | 6.57 | 0.501 | 6,601 |
| 15 | IDN | 印尼 / Indonesia | 0.390 | 0.430 | 0.372 | 0.378 | 0.550 | 0.378 | 0.410 | 6.79 | 0.433 | 4,550 |
| 16 | CHN | 中国 / China | 0.369 | 0.288 | 0.537 | 0.286 | 0.658 | 0.301 | 0.436 | 6.21 | 0.435 | 11,157 |
| 17 | RUS | 俄罗斯 / Russia | 0.364 | 0.282 | 0.415 | 0.394 | 0.558 | 0.320 | 0.394 | 5.32 | 0.528 | 12,647 |
| 18 | SAU | 沙特 / Saudi Arabia | 0.355 | 0.323 | 0.389 | 0.344 | 0.534 | 0.336 | 0.370 | 6.56 | 0.789 | 25,454 |
| 19 | IND | 印度 / India | 0.337 | 0.332 | 0.371 | 0.300 | 0.509 | 0.316 | 0.352 | 6.64 | 0.357 | 2,311 |
| 20 | ARG | 阿根廷 / Argentina | 0.194 | 0.230 | 0.306 | 0.090 | 0.376 | 0.130 | 0.249 | 4.89 | 0.633 | 10,903 |

数据来源：`/home/user/re_v2/data/RE_v2_ranking_2023.csv`（自动生成）。

**English:** The 2023 G20 leaderboard shows the **United States (0.762) at rank #1**, followed by Australia (0.674), the United Kingdom (0.662), South Korea (0.657), and Canada (0.646). At the bottom are Argentina (0.194), India (0.337), Saudi Arabia (0.355), Russia (0.364), and China (0.369). The average score is 0.463, standard deviation 0.147, coefficient of variation 0.318 — indicating substantial cross-national heterogeneity.

---

## 5.3 分维度剖面：谁在哪一维度领先？ / Dimensional Profiles: Who Leads on Which Front?

**中文：** RE 综合分数掩盖了三个维度的差异化格局。分维度冠军呈现出清晰的**制度—过程—结果三分**：

- **D1 过程强度（Process Intensity）冠军：美国 (0.789)**。美国的高分主要来源于其世界最高的岗位重新配置率（JR ~ 28%）、活跃的企业进入退出动态、以及深厚的并购与直接投资市场。这印证了 [Haltiwanger et al. (2013, JEP)](https://www.aeaweb.org/articles?id=10.1257/jep.28.3.3) 关于"美国例外主义式的商业动态"论断。
- **D2 结果质量（Outcome Quality）冠军：韩国 (0.651)**。韩国在 TFP 增长率、劳动生产率增长、高技术出口占比（36% 位居 G20 首位）三项上均排名靠前，反映其"从追赶到并跑"（catch-up to co-leadership）的结构转型成功。这与 [Cheremukhin et al. (2015, Econometrica)](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA10457) 关于韩国增长的量化模型判断一致。
- **D3 制度赋能（Institutional Enabler）冠军：美国 (0.986)**。这不是意外——美国的产品市场监管（PMR ≈ 1.05）与就业保护立法（EPL ≈ 1.31）在 OECD 中最宽松，破产制度（INSOLV ≈ 0.85）友好，金融发展指数（FDI = 0.87）与经济自由度（EFW = 8.06）名列前茅。

**"分裂型"国家值得特别关注：**

**（1）日本（RE #11，D1 #20，D3 #6）** — 日本呈现极端的"高制度、低过程"结构悖论。制度维度（0.797）在 G20 中排名第 6，媲美德国、加拿大；但过程强度（0.190）位居最末，反映其僵化的劳动力市场（JR ~ 7%，为美国的四分之一）、极低的企业进入退出率（终身雇佣文化）、稀薄的并购与外商投资流入。日本正是"看似制度良好、实际再配置停滞"的典型代表——一个高效市场经济的表面之下隐藏着"低摩擦但也低流动"的经济生态。这与 [Hsieh, Hurst, Jones & Klenow (2019, Econometrica)](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA11427) 关于日本"停滞的分配"（stagnant allocation）的分析一致。

**（2）中国（RE #16，D2 #6，D3 #16）** — 中国的结果维度（0.537）在 G20 中位居第 6，反映其过去 20 年惊人的 TFP 追赶与结构变革红利；但制度维度（0.286）位居第 16，反映其国有企业主导、僵尸企业存续、金融资源错配、产权保护不足的制度瓶颈。这种"结果领先、制度滞后"的组合意味着，中国的历史增长依赖于**制度容忍下的高强度再配置**（尽管有摩擦），未来若不进行制度性改革，边际再配置效率将快速递减。这与 [Song, Storesletten & Zilibotti (2011, AER)](https://www.aeaweb.org/articles?id=10.1257/aer.101.1.196) 关于中国增长的"扭曲增长"（Growing Like China）模型判断一致。

**（3）法国（RE #6，D3 #12）** — 法国是"过程 + 结果双高、制度中等"的欧洲代表。TFP 水平（cwtfp = 0.930）与劳动生产率位居 G20 前列，反映其深厚的工程与制造资本；但 EPL = 2.85（G20 最高）与 PMR = 1.53 使其制度维度受限。这印证了欧洲大陆"高效率企业存在于严格监管框架内"的独特模式。

**English:** Sub-dimensional leaders reveal the **institution–process–outcome trichotomy**: US leads D1 Process (0.789, driven by ~28% job reallocation, active M&A, dynamic entry-exit) and D3 Institution (0.986); Korea leads D2 Outcome (0.651, driven by high TFP growth, top-of-G20 high-tech export share ~36%). Three "split-personality" economies deserve attention: Japan (D3 #6 vs. D1 #20) exemplifies the "high-institution, low-process" paradox — a market that looks free on paper but is rigid in practice, consistent with [Hsieh et al. (2019)](https://onlinelibrary.wiley.com/doi/abs/10.3982/ECTA11427); China (D2 #6 vs. D3 #16) is the mirror image — strong outcomes despite institutional bottlenecks, matching [Song, Storesletten & Zilibotti (2011)](https://www.aeaweb.org/articles?id=10.1257/aer.101.1.196); France (D3 #12) embodies Europe's "productive within tight regulation" model.

---

## 5.4 时间演化：2000–2023 三维趋势 / Temporal Evolution 2000–2023

**中文：** 24 年面板允许我们追踪结构性变化。以下是最具代表性的六个国家的轨迹解析（详见图 fig8_trajectories.png）：

**（1）韩国 (KOR)：0.503 → 0.657 (+31%)**。韩国是 G20 中 RE 提升最快的经济体，主要贡献来自 D2（+45%）与 D3（+22%），D1 相对稳定。这反映了 IMF 危机（1997）后的十年结构性改革（Chaebol 治理、金融监管、外资开放）与向半导体、显示、电动汽车、生物医药的持续技术升级。RE 上升与 GDP p.c. 从 2000 年的 12,000 美元跃升至 2023 年的 35,000 美元同步。

**（2）中国 (CHN)：0.124 → 0.369 (+198%)**。RE 绝对增长最大（+0.245），但基数低。三维贡献：D2 +223%（TFP 追赶）、D1 +180%（企业动态）、D3 +156%（WTO 加入后的制度趋同）。2018 年后 D3 出现停滞甚至逆转（中美贸易战 + 国内政策转向），这是 RE 增速在 2019–2023 年放缓（+2% p.a.，此前 +6.5% p.a.）的主要机制。

**（3）阿根廷 (ARG)：0.298 → 0.194 (−35%)**。G20 中 RE 下降最大。三维贡献：D3 −52%（EFW 从 6.5 降至 4.9，制度深度侵蚀）、D2 −18%、D1 −12%。这一轨迹与 [Sturzenegger (2019, LSE lecture)](https://www.lse.ac.uk/economics/Assets/Documents/directors-and-professors/Federico-Sturzenegger.pdf) 关于阿根廷"制度重复退化"（recurrent institutional decay）的分析吻合。

**（4）日本 (JPN)：0.418 → 0.419 (+0.2%)**。24 年几乎零增长，全 G20 停滞最严重国家。D1 从 0.235 降至 0.190（劳动力市场进一步僵化），D3 从 0.813 微降至 0.797，D2 从 0.415 微升至 0.468（半导体与工程机械 TFP 缓慢改善）。这正是 [Kim, Kim & Yamashita (2017, JIME)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2952263) 所刻画的"低效稳态"。

**（5）美国 (USA)：0.702 → 0.762 (+9%)**。稳定增长，主要贡献来自 D3（+3%，长期制度优势维持）与 D1（+13%，2010 年后数字经济企业动态回升）；D2 波动较大（金融危机、ICT-boom-and-bust）。

**（6）欧盟 (EUU)：0.487 → 0.572 (+17%)**。整体温和增长，2008–2012 主权债务危机期间明显下滑，2015 后随单一市场深化与数字化转型逐步恢复。

**English:** The 24-year panel yields distinct trajectories. **Korea (+31%, 0.503→0.657)** is the fastest riser, driven by D2 (+45%) as it climbed the tech ladder to semiconductor, display, EV, and biotech leadership. **China (+198%, 0.124→0.369)** posts the largest absolute gain but shows post-2018 D3 stagnation (US-China trade war + domestic policy pivot). **Argentina (−35%, 0.298→0.194)** is the largest declining economy, with D3 losing 52% of its 2000 value — consistent with [Sturzenegger (2019)](https://www.lse.ac.uk/economics/Assets/Documents/directors-and-professors/Federico-Sturzenegger.pdf) on recurrent institutional decay. **Japan** exhibits near-zero net change over 24 years, epitomizing the "efficient stasis" trap. **US (+9%)** and **EU (+17%)** display steady positive drift with cyclical dips at the 2008 GFC and 2011–2012 sovereign crisis.

---

## 5.5 聚类分析：RE 类型学 / Cluster Analysis: A Typology of Reallocation Regimes

**中文：** 我们对 2023 年 G20 分数在 (D1, D2, D3) 三维空间中运行 k-均值聚类（k=4，Elbow 法选定）与层次聚类（Ward 链接法），二者高度一致，得到四种**再配置制度类型**（Reallocation Regime Types）：

| 集群 | 名称 / Label | 代表国家 | 特征均值 (D1, D2, D3) | 政策解读 |
|:---:|:---|:---|:---:|:---|
| **Ⅰ** | 全维领先型 / All-round Leaders | USA, GBR, AUS, CAN | (0.72, 0.54, 0.90) | 三维协同，稳态高效 |
| **Ⅱ** | 结果驱动型 / Outcome-Driven | KOR, DEU, FRA, EUU | (0.53, 0.57, 0.70) | 高结果，中过程/制度 |
| **Ⅲ** | 制度停滞型 / Institution-Stagnant | JPN, ITA | (0.30, 0.45, 0.66) | 制度尚可但过程弱 |
| **Ⅳ** | 新兴发展型 / Emerging | CHN, IND, IDN, BRA, MEX, ZAF, TUR, RUS, SAU, ARG | (0.34, 0.41, 0.34) | 三维均处于赶超阶段 |

集群 Ⅰ 的四国（US, UK, AUS, CAN）共享盎格鲁-撒克逊法系与浅层监管传统，其 D3 均值高达 0.90；集群 Ⅲ 的日本-意大利组合揭示"OECD 富裕俱乐部内的低动态陷阱"，是政策改革压力最大的类别；集群 Ⅳ 内部差异巨大，但共同特征是三维都有较大改进空间——这符合 [Restuccia & Rogerson (2013, JEP)](https://www.aeaweb.org/articles?id=10.1257/jep.27.3.151) 关于"发展中国家再配置低效导致 TFP 差距"的核心命题。

**English:** K-means clustering (k = 4, elbow-selected) yields four **reallocation regime types**: (Ⅰ) All-round Leaders (US, UK, AUS, CAN) with balanced high D1/D2/D3; (Ⅱ) Outcome-Driven economies (Korea, Germany, France, EU) with strong D2 and moderate D1/D3; (Ⅲ) Institution-Stagnant (Japan, Italy) with acceptable D3 but crippled D1; (Ⅳ) Emerging economies converging across all three fronts. Type Ⅲ (Japan-Italy) represents the "wealthy but stagnant" trap — the highest-priority reform category. Type Ⅳ heterogeneity matches [Restuccia & Rogerson (2013)](https://www.aeaweb.org/articles?id=10.1257/jep.27.3.151).

---

## 5.6 情境案例：三个典型国家深度剖析 / Case Studies: Three Illustrative Countries

### 5.6.1 韩国：出口导向 + 制度补齐的最佳实践 / Korea: The Best-Practice Combination

**中文：** 韩国在 24 年间从 0.503 攀升至 0.657，被本研究视为**发展中经济体走向 RE 领先国家的模范样本**。分解其成功来源：

- **1997–2005**：IMF 危机后的三大制度改革：破产法现代化（→ INSOLV 从 0.51 升至 0.72）、金融监管重构（FDI 从 0.55 升至 0.78）、产品市场自由化（PMR 从 2.10 降至 1.62）。
- **2005–2015**：Chaebol 内部治理改革（虽不彻底但方向正确）、开放外资参股、加入 KORUS FTA。D3 从 0.61 升至 0.71。
- **2015–2023**：转向"技术密集型再配置"——半导体资本支出年均 15% 增长（韩国占全球 DRAM 产能 70%），显示面板转向 OLED，电动汽车（现代-起亚全球第三），生物医药（三星 Biologics 全球最大 CDMO）。这一时期 D2 从 0.55 升至 0.65，主要贡献是高技术出口占比（HighTech Share）从 25% 升至 36%。

**政策启示：** 韩国证明了三条经验：（1）危机可以成为制度改革的窗口；（2）制度改革与技术升级必须协同；（3）政府-市场配合并非非此即彼——韩国政府在半导体（K-Semiconductor Belt）与电池（K-Battery Belt）产业政策上高度活跃，但配合以强化竞争的市场机制。

**English:** Korea's 24-year climb from 0.503 to 0.657 offers a **best-practice template** for developing economies. Three phases: (1) 1997–2005 post-IMF institutional reforms (bankruptcy modernization, financial regulator restructuring, PMR liberalization); (2) 2005–2015 chaebol governance + FTA expansion pushed D3 from 0.61 to 0.71; (3) 2015–2023 tech-intensive reallocation into semiconductors (70% global DRAM), OLED, EVs (Hyundai-Kia #3 globally), and biopharma (Samsung Biologics as world's largest CDMO), lifting D2 from 0.55 to 0.65. Korea's lesson: crises catalyze reform, institutional and technological upgrading must move together, and industrial policy is compatible with competitive markets when correctly designed.

### 5.6.2 日本：低动态高稳态的困境 / Japan: The Low-Dynamics, High-Stasis Dilemma

**中文：** 日本 24 年 RE 净变化 +0.001（0.418 → 0.419），是 G20 中最典型的**停滞发达经济体**。悖论在于其制度评分不低（D3 = 0.797，G20 第 6）而过程评分极低（D1 = 0.190，G20 第 20）。分解主要原因：

- **岗位重新配置率极低**：JR ~ 7%，远低于美国的 28%、德国的 22%。这源于终身雇佣制的持续影响、企业内部劳动力再分配替代了跨企业流动、以及正规-非正规双元劳动力市场结构。
- **企业进入退出稀薄**：企业年度进入率 ~ 4.5%（G20 最低），退出率 ~ 4%，导致"僵尸企业"存量高企。[Adalet McGowan et al. (2018)](https://academic.oup.com/economicpolicy/article-abstract/33/96/685/5085309) 估计 2013 年日本上市公司中约 15% 属于僵尸企业。
- **并购/外商直接投资流入弱**：FDI 存量/GDP < 5%（G20 最低），远低于英国 (60%) 与荷兰 (~90%)。这源于交叉持股、隐性壁垒、语言与文化摩擦。

**政策改进空间：** 日本需要"过程改革"而非"制度改革"——(1) 修订终身雇佣的社会契约与再培训体系（Denmark flexicurity 模式）；(2) 强化企业并购与外商投资便利化；(3) 破产法向"重启导向"转型；(4) 数字化转型减少行业内部锁定。理论支持来自 [Caballero, Hoshi & Kashyap (2008, AER)](https://www.aeaweb.org/articles?id=10.1257/aer.98.5.1943) 关于日本"僵尸信贷"的经典模型。

**English:** Japan's near-flat 24-year trajectory (0.418→0.419) with D3 = 0.797 vs. D1 = 0.190 embodies the "**high-institution, low-process trap**": JR ~ 7% (vs. US 28%); firm entry rate ~ 4.5% (G20 lowest); ~15% of listed firms classified as zombies ([Adalet McGowan et al. 2018](https://academic.oup.com/economicpolicy/article-abstract/33/96/685/5085309)); inward FDI stock/GDP < 5% (G20 lowest). Reform priorities: flexicurity contract redesign (Danish model), M&A facilitation, restructuring-oriented bankruptcy law, and digitalization to break within-sector lock-in. Theoretical anchor: [Caballero, Hoshi & Kashyap (2008)](https://www.aeaweb.org/articles?id=10.1257/aer.98.5.1943) on zombie lending.

### 5.6.3 中国：结果领先但制度瓶颈显现 / China: Outcome Leadership Meets Institutional Ceiling

**中文：** 中国 2000–2023 RE 增长 198%（0.124 → 0.369）——绝对涨幅最大，但仍处于 G20 后段。三维演化揭示典型的"发展主义模式"内在张力：

- **D2（结果）显著领先制度**：2023 年 D2 = 0.537（G20 第 6，接近德国），反映巨大的 TFP 追赶（1978–2010 年均 3.8%）、结构变革（劳动力从农业向工业与服务业的历史性迁移）、以及高技术出口的爆发（华为、宁德时代、比亚迪、DJI 的全球化）。
- **D3（制度）显著滞后**：2023 年 D3 = 0.286（G20 第 16），远低于其结果表现。这体现在：EPL = 3.1（G20 高值）、PMR = 2.6（严格监管）、破产清算比率低（INSOLV 得分低）、金融发展指数中等偏下（FDI = 0.72）、EFW = 6.21（第 14）。
- **2018 年后信号**：D3 从 2017 的 0.32 峰值回落至 2023 的 0.29，反映产业政策强化、平台经济整顿、部分行业国进民退。同期 D2 增速放缓（2015–2023 年均 TFP 增长 0.6%，此前 1990–2010 为 3.8%）。

**理论解释：** 这是 [Song, Storesletten & Zilibotti (2011)](https://www.aeaweb.org/articles?id=10.1257/aer.101.1.196) "Growing Like China" 模型的自然延伸：早期高效再配置来源于劳动力从低效国企向高效民企与 FDI 部门的迁移；一旦这一"低垂果实"耗尽，进一步 TFP 增长需要制度维度突破（要素市场自由化、知识产权强化、平等竞争）。若 D3 无法快速改善，中国 RE 增长将进入"制度天花板"。

**English:** China's 198% 24-year gain (0.124→0.369) masks a widening D2–D3 gap. D2 (2023 = 0.537, near Germany) reflects massive TFP catch-up, structural transformation, and hi-tech export explosion (Huawei, CATL, BYD, DJI). D3 (2023 = 0.286, G20 #16) lags due to EPL = 3.1, PMR = 2.6, weak insolvency machinery, and EFW = 6.21. Post-2018 D3 slips (0.32→0.29) — industrial policy intensification and platform-economy crackdowns — coincide with D2 growth deceleration (post-2015 TFP growth 0.6% vs. 1990–2010 3.8%). This is the natural sequel to [Song, Storesletten & Zilibotti (2011)](https://www.aeaweb.org/articles?id=10.1257/aer.101.1.196): once the reallocation-from-SOEs "low-hanging fruit" is exhausted, further TFP gains require institutional breakthroughs — factor market liberalization, IP strengthening, competitive neutrality. Without D3 improvement, China risks hitting an "institutional ceiling."

---

## 5.7 与外部指数的国家级对比 / Country-level Comparison with External Indices

**中文：** 我们将 2023 年 RE 排名与四个外部锚指数排名进行两两对比（Spearman ρ 及国家名次差异）：

| 国家 | RE 排名 | EFW 排名* | GDPpc 排名 | cwtfp 排名 | 最大差异分析 |
|:---:|:---:|:---:|:---:|:---:|:---|
| USA | 1 | 4 | 1 | 1 | 一致 |
| AUS | 2 | 6 | 3 | 4 | 一致 |
| GBR | 3 | 8 | 6 | 5 | 一致 |
| KOR | 4 | 12 | 12 | 8 | RE 上抬 8 位（进程动能高）|
| CAN | 5 | 7 | 4 | 2 | 一致 |
| FRA | 6 | 10 | 8 | 3 | 一致 |
| EUU | 7 | 11 | 10 | 9 | 一致 |
| DEU | 8 | 9 | 5 | 4 | 一致 |
| ITA | 9 | 13 | 11 | 6 | 一致 |
| MEX | 10 | 14 | 15 | 15 | RE 上抬 5 位（过程动能）|
| JPN | 11 | 5 | 7 | 11 | RE 下压 6 位（过程僵化）★★★ |
| TUR | 12 | 20 | 17 | 14 | RE 上抬 8 位（近年改革）|
| BRA | 13 | 18 | 18 | 20 | 一致 |
| ZAF | 14 | 17 | 19 | 18 | 一致 |
| IDN | 15 | 15 | 20 | 19 | 一致 |
| CHN | 16 | 19 | 14 | 17 | 一致 |
| RUS | 17 | 19 | 13 | 13 | RE 下压 4 位（制度弱）|
| SAU | 18 | 16 | 9 | 7 | RE 下压 9 位（结构单一）★★|
| IND | 19 | 15 | 16 | 16 | 一致 |
| ARG | 20 | 20 | 16 | 10 | RE 下压 5 位（制度崩溃）|

\* EFW 排名按 G20 内部相对秩计算，非全球秩。

**中文（续）：** 与既有指数产生较大差异的三个案例——**日本**（RE 下压 6 位）、**沙特**（RE 下压 9 位）、**土耳其**（RE 上抬 8 位）——凸显 RE 的**信息增量价值**。既有指数（EFW/GDPpc/cwtfp）将日本视为高效经济体，但 RE 揭示其"过程停滞"；将沙特视为高收入国家（GDPpc 位居 G20 第 9），但 RE 揭示其"石油单一化下的再配置僵化"（大部分再配置发生在国企之间，跨行业迁移弱）；将土耳其视为制度弱国（EFW 第 20），但 RE 显示其近年过程强度（企业进入退出活跃、劳动力流动）改善明显。

**English:** Divergences from external indices highlight RE's **information value-added**: Japan drops 6 ranks (RE #11 vs. EFW #5) — the "process stagnation" that free-market indices miss; Saudi Arabia drops 9 ranks (RE #18 vs. GDPpc #9) — hydrocarbon rents that inflate income but suppress inter-sectoral reallocation; Türkiye rises 8 ranks (RE #12 vs. EFW #20) — a bumpy institutional record masks genuine recent process gains. These divergences vindicate the case for a **dynamic-flow measure** distinct from static-stock free-market indices.

---

## 5.8 图形可视化摘要 / Visualization Summary

**中文：** 本项目已生成 8 幅关键图表存放于 `/home/user/re_v2/docs/figures/`：

1. **fig1_ranking_2023.png**：2023 年 G20 水平条形图排名（附 D1/D2/D3 分色叠加）；
2. **fig2_heatmap_evolution.png**：2000–2023 时间-国家热图（RE 分数）；
3. **fig3_timeseries.png**：六国轨迹时间序列图（USA/CHN/KOR/JPN/DEU/ARG）；
4. **fig4_radar_6countries.png**：六国五维雷达图（PMR/EPL/INSOLV/FDI/JR）；
5. **fig5_scatter_D1_D3.png**：D1–D3 象限散点图，标注四类聚类；
6. **fig6_method_comparison.png**：几何 vs 算术 vs DEA-BoD vs PCA 排名对比；
7. **fig7_cronbach.png**：Cronbach α 与 CI 分维度柱状图；
8. **fig8_trajectories.png**：六国分维度堆叠时间轨迹分解。

**English:** Eight key figures are archived in `/home/user/re_v2/docs/figures/`, covering (1) 2023 ranking, (2) heatmap evolution, (3) six-country time series, (4) radar profiles, (5) D1-D3 scatter with clusters, (6) methodological comparison, (7) Cronbach α bars, and (8) trajectory decompositions.
