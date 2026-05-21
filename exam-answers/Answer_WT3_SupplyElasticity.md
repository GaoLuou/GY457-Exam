# WT Part 2: Housing Supply Elasticity — Identification & Evidence
> 考题类型：Partitioned | 出现：Mock 2025/26 Q4、2013/14考试 Q6

---

## Past Exam Questions

**2013/14 Exam — Partitioned (WT):**
> Estimating housing supply and demand curves is an empirical challenge due to the 'identification problem'.
> (a) What exactly is the 'identification problem' in estimating housing supply and demand curves? Explain. (30 marks)
> (b) How have empirical researchers estimated the housing supply price elasticity? Discuss methodology and main insights. (40 marks)
> (c) To what extent can it be helpful for investors and/or policymakers to know the housing supply price elasticity? Discuss. (30 marks)

**Mock Exam 2025/26 — Partitioned:**
> (a) What empirical difficulties would you need to overcome to estimate supply price elasticity for your home region? (30 marks)
> (b) What empirical approach/methodology would you choose and why? (20 marks)
> (c) What would your estimating equation look like? (20 marks)
> (d) What locational factors determine supply price elasticity? Discuss with reference to the literature. (30 marks)

---

## Part (a): The Identification Problem (30 marks)

**The core problem:**
We observe equilibrium price-quantity pairs (P*, Q*) which lie simultaneously on both the supply curve and the demand curve. A simple OLS regression of Q on P estimates neither the supply nor the demand curve — it estimates a weighted average of both (simultaneity bias / simultaneous equations bias).

**Intuition:** If we see prices and quantities move together over time, we cannot tell whether:
- Demand shifted right (movement along supply curve → identifies supply) — or
- Supply shifted right (movement along demand curve → identifies demand) — or
- Both shifted simultaneously

**Why standard regression fails:** OLS assumes the right-hand side variable (P) is exogenous. But P is jointly determined with Q in equilibrium. Cov(P, ε) ≠ 0 → OLS coefficient on P is biased.

**Additional difficulties (mock exam):**
- Lack of transaction-level data (UK historically poor data environment)
- Defining the housing "market" boundary (what counts as a unit of quantity?)
- Functional form: levels vs log-log vs changes specification
- Housing stock vs new construction: distinct elasticities (Mayer & Somerville 2000 find stock elasticity = 0.08, new starts elasticity = 6.3)

---

## Part (b): Methodology — IV / 2SLS Approach (40 marks)

**Solution: Instrumental Variables (IV) / Two-Stage Least Squares (2SLS)**

**Principle:** To estimate the *supply* curve, we need a variable (instrument Z) that:
1. **Shifts demand** (relevant: correlated with P) — keeping supply fixed, so movement traces out the supply curve
2. **Only affects supply through price** (exclusion restriction: Z ⊥ ε_supply)

**The Bartik shift-share instrument (Bartik 1991):**
- Construct a predicted local demand shock: Z_jt = Σ_k (share of industry k in region j in base year) × (national employment growth in industry k)
- This captures exogenous local demand variation from national industry trends
- Exclusion restriction: national industry trends affect local housing demand through income, but do not directly affect local construction costs or planning constraints

**Saiz (2010) — Supply-side instrument for demand:**
To estimate *demand* elasticity: use supply-side instruments (topographic constraints — % undevelopable land, water bodies, steep slopes). These shift supply without directly affecting demand.

**Two-stage procedure:**
1. First stage: Regress ΔP_t on ΔZ_t (and controls) → get fitted Δ P̂_t
2. Second stage: Regress ΔQ_t on Δ P̂_t → coefficient = (1/supply elasticity) in inverse form, or supply elasticity if equation specified correctly

**Why changes (ΔP, ΔQ) not levels?**
Housing prices and stock are non-stationary (trending upward). Regressing levels on levels produces spurious correlation. First-differencing removes unit roots (Mayer & Somerville 2000). Use ∂lnP ≈ ΔP/P and ∂lnH ≈ ΔQ/Q.

**Key estimates from literature:**
| Study | Elasticity | Notes |
|-------|-----------|-------|
| Mayer & Somerville (2000) | Stock: 0.08; New starts: 6.3 | US; stock inelastic because housing durable |
| Saiz (2010) | Average: 1.7 (range 0.6–5.5) | US MSAs; topographic IV |
| Hilber & Mense (2025) | Average: 1.16 (range 0.15–3.6) | UK; regulatory + topographic constraints |
| Hilber & Mayer (2009) | Urban: 0.014; Rural: 0.16 | Land constraint heterogeneity |

---

## Part (c): Estimating Equation (20 marks — mock) / Policy Value (30 marks — 2013/14)

**Estimating equation (mock Q4c):**

Supply equation (second stage):
> ΔQ^S_t = α_0 + α_1·Δ P̂_t + α_2·(ΔSupply Shifters_t) + ε_t

Where:
- ΔQ^S_t = change in housing stock (or new starts) at time t
- Δ P̂_t = predicted price change from first stage (instrumented by Bartik Z)
- Supply Shifters: construction cost index, planning constraint measure, topographic index
- α_1 = supply price elasticity

First stage:
> ΔP_t = β_0 + β_1·ΔZ_t + β_2·(Supply Shifters_t) + μ_t

Where Z_t is the Bartik instrument.

**For the 2013/14 Q6c — Policy value of knowing elasticity:**

**For investors:**
- Elastic market (Houston): demand shock → quantity ↑, price stable → lower capital gain risk; predictable rental yields
- Inelastic market (London): demand shock → price ↑↑ → higher capital gain potential but downside risk
- Investor can position portfolio: long inelastic markets for appreciation; short/hedge elastic markets

**For policymakers:**
- Hilber & Turner (2014): housing subsidies (e.g., UK Help-to-Buy, US MID) have **zero average effect** on homeownership nationally; **negative effect** in inelastic markets (subsidies → demand↑ → price↑↑ → deposit requirements↑ → ownership falls)
- "Help people, not places" (Hilber et al.): in inelastic markets, place-based subsidies capitalise into land values → benefit existing owners, not target households
- Knowing elasticity allows calibrating policy: subsidies effective only where supply can respond

---

## Part (d): Locational Determinants of Supply Elasticity (30 marks)

**Two categories of supply constraint (H&V 2016):**

**1. Physical / topographic constraints:**
- Water bodies (coastline, lakes, rivers) — limit developable land
- Steep slopes (>15% gradient) — costly construction
- Saiz (2010) constructs "Residential Land Available" (RLA) index from GIS data
- More undevelopable land → less competition for buildable land → higher land prices per unit → lower elasticity

**2. Regulatory constraints:**
- Zoning (density limits, land use controls), height limits, conservation areas, green belts
- H&V (2016) measure using vote shares in favour of development in 1947–79 planning committee records
- Endogeneity concern: areas with high demand may attract more restrictive regulation. H&V instrument for regulatory constraints using long-lagged regulatory strictness (pre-determined)

**H&V (2016) key findings:**
- Regulatory constraints dominate physical constraints in explaining English house price cyclicality
- South-east England most supply-constrained → largest cycles
- Regulatory elasticity: −0.13 (regulatory constraints); physical: −0.09

**Hilber & Mayer (2009) — Land availability within cities:**
- Urban areas (low % undeveloped land): supply elasticity = **0.014** — virtually zero
- Rural areas (high % undeveloped land): supply elasticity = **0.16**
- Higher elasticity in rural areas → fiscal improvements (e.g., better schools) capitalise less (10%) than in urban areas (33%)

**Why does less developable land reduce elasticity?**
Three channels:
1. *Cost channel:* Building on difficult terrain is more expensive → high construction costs → less new supply
2. *Political economy:* Dense, developed areas have more homeowners with NIMBY incentives → more restrictive planning
3. *Real options:* Scarce developable land has higher option value (Grenadier 1995) → developers wait → reduced supply response

---

## Key Terms

| English | Chinese |
|---------|---------|
| Identification problem | 识别问题 |
| Simultaneous equations bias | 联立方程偏差 |
| Instrumental variable (IV) / 2SLS | 工具变量 / 两阶段最小二乘 |
| Exclusion restriction | 排他性限制 |
| Bartik shift-share instrument | Bartik工具变量 |
| First stage / second stage | 第一阶段/第二阶段 |
| Supply price elasticity | 供给价格弹性 |
| Physical constraint | 物理约束 |
| Regulatory constraint | 法规约束 |
| Topographic index | 地形指数 |
| Non-stationarity | 非平稳性 |
| Stock elasticity vs flow elasticity | 存量弹性 vs 流量弹性 |

## 中文答题思路

**识别问题（a）**：核心——我们观察到的是均衡点（P*,Q*），它同时在供给曲线和需求曲线上。OLS无法区分是S还是D移动导致的价格变化。不能用OLS直接回归P和Q。

**IV方法（b）**：想估计供给曲线？需要移动需求（保持供给不变）的工具变量。Bartik工具：用国家行业增长×地方行业构成预测外生需求冲击。关键是两个条件：相关性（Z影响P）+ 排他性限制（Z只通过需求影响Q，不直接影响供给）。

**供给弹性决定因素（d）**：两类约束：物理（地形/水体）vs 法规（规划限制）。H&V找到法规约束更重要。Hilber & Mayer：城市弹性0.014 vs 农村0.16——为什么差距这么大？房主投票+土地稀缺+建设成本。

**Mock考试主要错误**：
- 很多人提议用DiD而不是IV/2SLS（错误！DiD估计的是处理效应，不是弹性）
- 第一阶段第二阶段搞混
- 回归levels而不是changes（非平稳性问题）
