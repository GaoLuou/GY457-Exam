# WT Part 2: Real Estate Cycles
> 考题类型：Essay + Partitioned | 出现：2012/13考试、2018/19考试、Seminar 5核心题

---

## Past Exam Questions

**2012/13 Exam — Partitioned (WT):**
> Various key measures of residential and commercial property markets behave cyclically.
> (a) Discuss two theories explaining real estate cycles. Discuss mechanism, predictions and supporting evidence for each. (40 marks)
> (b) How have empirical researchers tried to identify whether real estate booms are the result of (i) fundamentals or (ii) deviation from equilibrium? What are the main empirical difficulties? (40 marks)
> (c) Las Vegas and Phoenix face few long-term supply constraints, yet observed steep price rises 2000–2005 followed by steeper decline. Explain. (20 marks)

**2018/19 Exam — Essay (WT):**
> "To what extent can fundamental factors on the demand and supply side explain local real estate price cycles, and why and when do real estate prices deviate from such fundamental factors? Discuss with reference to the theoretical and empirical literature." (100 marks)

---

## Part (a): Two Theories of Real Estate Cycles (40 marks)

*(Choose any two — loss aversion and Hilber & Vermeulen recommended as strongest)*

### Theory 1: Exogenous Demand Shocks + Supply Constraints — Hilber & Vermeulen (2016)

**Mechanism:** Real estate cycles can be driven by fundamentals when demand shocks (income, employment, population) interact with **inelastic housing supply**. In markets with elastic supply (Houston), demand shocks → quantity adjustment → stable prices. In markets with inelastic supply (San Francisco, London), demand shocks → large price swings. The interaction creates serial correlation (prices above trend continue upward) and mean reversion (prices eventually correct).

**Two types of supply constraint (H&V 2016):**
- *Physical constraints:* Undevelopable land (water bodies, steep slopes) — measured by Saiz (2010) topographic index.
- *Regulatory constraints:* Planning restrictions — measured by H&V using historical planning vote data (1947–79 development plan vote shares).

**Key findings (H&V 2016, England):**
- Regulatory constraints: price elasticity = **−0.13** (1% stricter regulation → 0.13% higher prices)
- Physical constraints: **−0.09**
- Counterfactual: If England had US-like planning flexibility → house prices **35% lower**
- Regulatory constraints dominate in the south-east of England

**Predictions:** Price cycles larger in supply-constrained markets; mean-reverting in unconstrained markets.

**Evidence:** San Francisco (inelastic, topography + regulations) shows extreme boom-bust; Columbus OH (elastic) shows near-zero price volatility (Hilber & Mayer, course slides).

### Theory 2: Loss Aversion — Genesove & Mayer (2001, QJE)

**Mechanism:** Drawing on Kahneman-Tversky prospect theory, sellers facing **nominal losses** (purchase price > current market value) experience asymmetric disutility. They resist accepting a loss by posting higher asking prices, leading to price stickiness and market freeze in downturns.

**Research design:** Boston condo market, early 1990s downturn. Compare sellers facing nominal losses (LTV high, in negative equity) vs sellers not facing losses.

**Key findings:**
- Sellers facing losses ask **3–18% more** than comparable sellers without losses
- They actually achieve **3–7% higher** transaction prices (not fully exploited)
- They remain on market **longer** (time-on-market ↑)
- Effect is stronger for higher LTV (deeper paper loss)

**Predictions:** Downturns marked by (i) price stickiness (not clearing quickly), (ii) transaction volume collapse, (iii) prolonged adjustment. Explains why prices fall slowly and volumes crash in recessions.

**Evidence:** Consistent with general evidence of trading volume collapsing in housing downturns (Stein 1995; Lamont & Stein 1999 on liquidity constraints amplifying this).

---

## Part (b): Fundamentals vs Deviations from Equilibrium (40 marks)

**The empirical challenge:** Observed prices may reflect either (i) rational response to fundamentals (income, employment, demography) or (ii) irrational deviation (bubbles, extrapolative expectations). Distinguishing them is hard because:
1. We do not observe the unobservable "fundamental value"
2. Rational expectation models and behavioural models can generate similar price paths
3. Endogeneity: prices affect fundamentals (e.g., housing wealth affects consumption)

**Approach 1 — Capozza et al. (2004) reduced-form model:**
Regress local price growth on fundamentals (income, population, construction cost) and lagged prices. Test whether serial correlation (momentum) and mean reversion are present *above and beyond* what fundamentals predict. Finding: prices above trend → tend to continue upward (irrational exuberance?); eventually mean-revert (fundamentals anchor). Markets with larger population and income shocks show stronger persistence.

**Difficulty:** Cannot identify whether momentum reflects rational forward-looking expectations or irrational extrapolation. Cannot distinguish bubble from slow supply response.

**Approach 2 — H&V (2016) structural IV approach:**
Regress real house prices on demand fundamentals (instrumented using Bartik shift-share for income shocks) and supply constraints. Isolate the portion of price variance explained by fundamentals vs unexplained residual (potential deviations).

**Difficulty:** Requires valid instruments; Bartik assumption (exclusion restriction: national industry growth only affects local housing through income channel) may be violated if demand shocks affect supply-side decisions.

**Approach 3 — Case & Shiller (1988, 1989, 2003) surveys:**
Ask homebuyers directly about their price expectations. Find: in boom markets, buyers expect further price rises (extrapolative expectations inconsistent with rationality). Evidence for irrational exuberance. Difficulty: survey expectations may not reflect actual trading decisions.

**Conclusion:** Empirical literature suggests both fundamentals AND deviations matter. In supply-constrained markets, demand shocks create large price movements; behavioural factors (extrapolation, loss aversion) amplify and prolong these movements.

---

## Part (c): Las Vegas and Phoenix — Elastic Supply but Boom-Bust (20 marks)

**The puzzle:** Both cities have elastic supply (flat terrain, minimal regulation), yet experienced extreme booms (2000–2005) and crashes (2005–2009).

**Explanation — Cobweb + speculative demand (non-fundamental):**

1. **Speculative demand (Wheaton 1999; Nathan & Zwick 2013):** In the 2000s, low interest rates and loose credit (subprime) attracted investor/speculative demand. Buyers purchased homes expecting capital gains, not for housing services. This demand is not anchored to fundamentals (income, employment). When credit dried up post-2006, speculative demand collapsed.

2. **Cobweb dynamics (Wheaton 1999):** Developers — even with elastic supply — respond to current prices with a lag. The price signal in 2004–05 triggered massive supply response. When demand collapsed before supply hit the market, prices fell steeply. The elastic supply amplified the quantity overshooting (excess inventory), preventing price recovery.

3. **Elastic supply paradox:** Unlike SF (price-volatile, quantity-stable), LV/PHX experienced both price volatility AND massive quantity swings. The boom-bust was driven by non-fundamental speculative demand interacting with elastic construction response — producing extreme inventory gluts by 2009.

**Conclusion:** Supply elasticity prevents demand-driven price cycles from fundamentals, but cannot prevent cycles driven by speculative, non-fundamental demand. Credit conditions and investor speculation can generate boom-bust even in unconstrained markets.

---

## Essay Version: "To What Extent Can Fundamentals Explain Cycles?"

**Structure (intro → body → conclusion):**

**Introduction:** Real estate prices are serially correlated and mean-reverting — a stylised fact consistent with both fundamental and non-fundamental explanations. This essay assesses the relative contribution of supply-demand fundamentals versus behavioural and financial factors.

**Fundamentals side (H&V 2016, Capozza et al.):** Supply-demand interactions can generate persistent cycles. Demand shocks (income, employment) in supply-constrained markets → large price swings. Empirical evidence: H&V find inelastic supply drives cyclicality in England; 35% counterfactual gap suggests fundamentals matter enormously.

**Non-fundamental side:** (i) Loss aversion (Genesove & Mayer 2001) creates downward price stickiness and volume collapse. (ii) Irrational exuberance (Case & Shiller): extrapolative expectations create momentum beyond fundamentals. (iii) Liquidity constraints (Ortalo-Magne & Rady 2006): credit shocks amplify cycles by affecting first-time buyer entry. (iv) Option theory (Grenadier 1995): high uncertainty → delayed construction → amplified supply shortfalls.

**Conclusion:** Fundamentals (supply constraints + demand shocks) are necessary but not sufficient. Behavioural factors amplify and prolong deviations from fundamentals. The relative importance varies: in supply-elastic markets, fundamental shocks dissipate quickly; in constrained markets, they interact with behavioural amplifiers to create severe cycles.

---

## Key Terms

| English | Chinese |
|---------|---------|
| Real estate cycle | 房地产周期 |
| Serial correlation / momentum | 序列相关性 / 动量 |
| Mean reversion | 均值回归 |
| Supply constraint (physical / regulatory) | 供给约束（物理/法规）|
| Housing supply price elasticity | 住房供给价格弹性 |
| Loss aversion | 损失厌恶 |
| Nominal loss | 账面损失 |
| Price stickiness | 价格粘性 |
| Irrational exuberance | 非理性繁荣 |
| Extrapolative expectations | 向后看预期 |
| Cobweb model | Cobweb模型（蛛网）|
| Speculative demand | 投机性需求 |
| Liquidity constraint | 流动性约束 |
| Option value (investment timing) | 期权价值（投资时机）|
| Fundamentals | 基本面 |

## 中文答题思路

**Part (a) 最佳组合**：选H&V供给约束（fundamental theory）+ 损失厌恶（behavioral theory），形成对比。必须给：mechanism + predictions + evidence，三样缺一不可。

**Part (b) 核心**：为什么难以区分fundamentals vs bubble？→ (1) 无法观察"真实价值"；(2) 理性预期和非理性预期可产生相似价格路径；(3) 内生性。Capozza et al. 方法：残差序列相关超过fundamentals能解释的部分 = 可能的deviation。

**Part (c) 陷阱**：Las Vegas/Phoenix供给弹性，所以不应该出现价格周期……but they did! 原因：投机性需求（非fundamental）+ Cobweb（时滞）。弹性供给只能稳定由fundamental需求驱动的价格，无法防止由credit/speculation驱动的周期。
