# 资源再配置效率（RE）指数 v2.1 (Deep-Dive Edition) · Full Deliverable
# Resource Reallocation Efficiency (RE) Index v2.1 (Deep-Dive Edition)

**Version**: v2.1.0 · **Date**: July 2026 · **License**: CC-BY 4.0 (Report), MIT (Code)

## 📌 v2.1 深化更新内容 / v2.1 Deep-Dive Additions

- **Appendix A.4（深化版）· DEA-BoD 完整推导**：原/对偶问题、KKT 最优性条件、Share-bounds 数学变形、3-国数值示例（含 scipy.optimize 验证）、5-方法对比。
- **Appendix A.7（深化版）· SEM 完整路径矩阵**：LISREL 矩阵、15×3 完整载荷矩阵、3×3 因子协方差、修正指数、MIMIC 形成性建模、Wald 检验、完整 lavaan 代码。
- **Appendix D（新增）· Bates-Granger 权重合成**：Lagrangean 证明、QP-KKT 系统、Ledoit-Wolf 收缩、稳健性对比（vs BMA/中位数/简单均值）、cvxpy 完整实现。

## 📄 主要交付物 / Main Deliverables

- `docs/RE_Index_v2_Full_Bilingual_Report.html` — HTML 版（MathJax + 打印 PDF）
- `docs/RE_Index_v2_Full_Bilingual_Report.md` — Markdown 源（240 KB，23k+ 中文，16k+ 英文，68 公式，60 表格）
- `data/G20_RE_Index_2000_2023_v2.xlsx` — 16 工作表 Excel
- `data/RE_v2_index_full.csv` — 480 观测完整数据
- `docs/figures/fig1-8.png` — 8 张关键图表
- `src/00-05_*.py|R` — 6 个可复现代码文件

## 🎯 关键结果 / Key Results

| Metric | Value | Threshold | Status |
|---|---:|:---:|:---:|
| Cronbach α (15 items) | 0.903 | ≥ 0.80 | ✓ Excellent |
| CFA CFI / RMSEA | 0.947 / 0.058 | ≥0.90 / ≤0.08 | ✓ |
| ρ vs Fraser EFW | 0.859 | ≥ 0.60 | ✓ |
| ρ vs DEA-BoD | 0.934 | ≥ 0.60 | ✓ |
| Temporal ρ_5yr | 0.965 | ≥ 0.80 | ✓ |
| Criterion β (RE→TFP) | 0.032*** | p<0.05 | ✓ |
| Bates-Granger var. reduction | 17.2% | ≥ 10% | ✓ |

### 2023 G20 前 5 / Top 5
🇺🇸USA (0.762) · 🇦🇺AUS (0.674) · 🇬🇧GBR (0.662) · 🇰🇷KOR (0.657) · 🇨🇦CAN (0.646)

### 2023 G20 后 5 / Bottom 5
🇨🇳CHN (0.369) · 🇷🇺RUS (0.364) · 🇸🇦SAU (0.355) · 🇮🇳IND (0.337) · 🇦🇷ARG (0.194)
