# GY457 Theory & Model Guide — Exam Ready
> Organized by model. For each: mechanism → key papers & numbers → how to write it.
> Exam: 3 hours, answer 2 questions (1 AT + 1 WT).

---

# AT MODELS (Bagagli)

---

## MODEL 1 — AMM Monocentric City Model
*Alonso (1964), Mills (1967), Muth (1969)*

### What it is
The baseline model of urban spatial structure. Land goes to the highest bidder; firms cluster at the centre (CBD); residents sort by their trade-off between rent and commuting.

### Core mechanism

**Bid-rent:** The maximum rent a household/firm is willing to pay at each distance x from CBD while maintaining constant utility/profit.

**The key gradient formula:**
> ∂p_q / ∂x = −t / q

- t = commuting cost per unit distance
- q = housing consumed
- The gradient is negative: rent falls as you move away from CBD

**Suburbanisation — two triggers:**

| Trigger | Mechanism | Evidence |
|---------|-----------|---------|
| Income ↑ (y↑) | y↑ → q↑ (housing is normal good) → gradient −t/q flattens → city boundary expands | Baum-Snow (2007): each US urban highway → **−18%** central population |
| Commuting cost ↓ (t↓) | Directly flattens gradient → suburbs cheaper → households move out | Heblich et al. (2020): London steam railways triggered mass suburbanisation |

**Who lives where (income segregation):**
- Rich: higher q → flatter bid-rent → live in suburbs (monetary commuting cost model)
- Poor: steeper bid-rent → live centrally

### How to write it in exam

> "In the AMM framework, a household's bid-rent gradient is given by ∂p_q/∂x = −t/q. Rising income increases housing demand q, which flattens the gradient, rotating the bid-rent curve outward and expanding the urban boundary. Baum-Snow (2007) finds that each additional highway through a US city centre reduces central city population by 18%, consistent with this mechanism."

### When this appears
- AT Essay Q: "Critically assess the monocentric city model" → use as Part 1 foundation
- AT Partitioned Q(a): "Two explanations for suburbanisation under AMM" → this is the direct answer

### 📌 中文备考注释

**60分重点在哪：**
不能只说"收入高了就搬郊区"，必须走完逻辑链：**y↑ → q↑（normal good）→ 梯度 −t/q 变平 → 城市边界 x̄ 外扩**。这个链条要说全，少一步都显得很superficial。

**表述关键：**
- 先用一句话定义bid-rent是什么（"the maximum rent a household is willing to pay at distance x while maintaining constant utility"）
- 再写公式 ∂p_q/∂x = −t/q，解释变量含义
- 然后说机制（income → q → gradient flattens）
- 最后接Baum-Snow (-18%) 作为实证支撑

**两个机制怎么衔接：**
> "A second driver of suburbanisation is falling commuting costs. A reduction in t directly flattens the bid-rent gradient by the same mechanism, making suburban locations more attractive. Heblich et al. (2020) show that London's steam railways triggered the first mass suburbanisation, consistent with this prediction."

**常见失分点：** 把Rich/Poor的住址搞反（货币通勤成本下，Rich住郊区；但如果是时间成本，Rich住市中心 → 这是LeRoy-Sonstiele的逻辑）。两者不要混。

---

## MODEL 2 — Agglomeration & CBD Concentration
*Rosenthal & Strange (2020), Liotta et al. (2022), Heblich et al. (2020)*

### What it is
Why firms cluster near the CBD: not just transport access, but **productivity spillovers** that decay with distance.

### Core mechanism

**Productivity function:**
> A_i = a · e^(−θ · D_i)

- θ = spatial decay parameter
- D_i = distance from other firms / CBD
- Higher θ → faster decay → stronger pull toward CBD

**Three types of agglomeration economies (Marshall):**
1. **Knowledge spillovers** — operate at street/building level (most localised)
2. **Labour market pooling** — effective at commuting-zone level
3. **Input sharing** — regional level

**Spatial scale evidence (Rosenthal & Strange 2020):**
- Knowledge spillovers: decay within a few city blocks
- Labour pooling: effective across the whole metro area

**Empirical rent gradient:**
- Liotta et al. (2022): global average rent declines **−1.4%/km** from CBD
- Heblich et al. (2020): removing London's historical rail network → land values **−50%**

### How to write it in exam

> "Firms concentrate near the CBD not merely for transport access but because productivity spillovers — especially knowledge spillovers — decay sharply with distance (Rosenthal & Strange 2020). The productivity function A_i = a·e^(−θD_i) implies that firms with high spatial decay parameter θ (finance, law, tech) have steep bid-rent curves and strong CBD incentives. Liotta et al. (2022) document a global rent gradient of −1.4% per km, consistent with this mechanism."

### 📌 中文备考注释

**60分重点在哪：**
这个model的关键不是说"企业喜欢在CBD因为方便"，而是要讲**为什么具体是CBD**：因为knowledge spillovers极度局部（街区/楼层级别），高θ行业（金融、法律、科技）bid-rent曲线最陡 → CBD集聚最强。这个"why specifically CBD"是Mock考试反馈里点名缺失的内容。

**三种集聚经济的空间尺度（这个很考）：**
- Knowledge spillovers → 街区/建筑内（most localised）
- Labour market pooling → 通勤区（metro-wide）
- Input sharing → 区域（regional）

答题时可以用一句话带过三种，然后重点讲knowledge spillovers最局部这一点，因为它最能解释CBD的存在。

**表述衔接：**
> "This explains why knowledge-intensive sectors such as finance and professional services cluster most tightly in the CBD, while manufacturing — with low θ — disperses to suburban or peri-urban locations."

---

## MODEL 3 — Bilateral Spillovers & Endogenous Agglomeration
*Ahlfeldt & Wendland (2013), Ahlfeldt et al. (2020), Krugman (1991)*

### What it is
The monocentric model treats CBD agglomeration as *given*. In reality, firms generate spillovers **with each other** — agglomeration is self-reinforcing and can arise anywhere.

### Core mechanism

**Extended productivity function:**
> A_i = a_i · e^(−θD_i) · e^(βZ_i)

- Z_i = proximity-weighted output of *all other firms* (not just CBD)
- β = strength of bilateral spillovers
- Firms benefit from *other firms nearby*, not just from being near the historical centre

**Implications:**
- Clusters can be self-sustaining **anywhere**, not just at a historical CBD
- Creates **multiple equilibria**: different stable city structures can emerge
- Outcome depends on **initial conditions** (path dependence)

**Path dependence evidence (Ahlfeldt et al. 2020):**
- NYC: 3.4 million people in 1900, early subway → dense monocentric CBD today
- LA: only 100k in 1900, car-based → dispersed polycentric structure today
- Same technology, different history → different city structure

**Krugman (1991) core-periphery:** analogous idea — agglomeration can lock in to any location; history determines which one.

### How to write it in exam

> "A fundamental limitation of the monocentric model is its assumption that CBD agglomeration is exogenous. Ahlfeldt & Wendland (2013) show that firms generate bilateral spillovers with each other, captured by A_i = a_i·e^(−θD_i)·e^(βZ_i). This creates self-reinforcing clusters that can be stable at any location, generating multiple equilibria. The observed CBD structure is therefore historically contingent: Ahlfeldt et al. (2020) show that NYC's dense monocentric structure reflects its 1900 population of 3.4 million and early subway investment, while LA's dispersed structure reflects late urbanisation."

### 📌 中文备考注释

**60分重点在哪：**
这是AT Essay里"批判性评估"部分的核心武器。用Model 1（AMM）做基础，然后用Model 3来说AMM的局限性：AMM假设CBD是外生给定的，但Ahlfeldt & Wendland证明集聚是**内生的、双向的**。

**逻辑链（必须说全）：**
1. AMM treats CBD as exogenous → 这是局限
2. In reality: bilateral spillovers → e^(βZ_i) 项 → firms benefit from *other firms*
3. → Self-reinforcing → can be stable anywhere → **multiple equilibria**
4. → Which equilibrium we're in depends on **history** (path dependence)
5. → NYC vs LA = same technology, different 1900 starting point → different outcomes

**衔接到"will cities become more polycentric"：**
> "If bilateral spillovers are strong (high β), existing clusters are hard to dislodge — the CBD advantage is self-perpetuating. However, if transport costs fall or congestion rises sufficiently, the balance can tip toward new stable clusters, generating polycentricity."

**最容易丢的点：** 很多人知道"NYC有路径依赖"但不解释为什么。要说：bilateral spillovers → self-reinforcing → once established, cluster is stable → history determines which cluster.

---

## MODEL 4 — Sub-centres & Edge Cities
*McMillen & Smith (2003), Henderson & Mitra (1996), Fujita & Ogawa (1982)*

### What it is
Two routes to polycentric cities: sub-centres that emerge **organically** from many decentralised decisions, and **edge cities** built by a single developer.

### Sub-centres (organic) — McMillen & Smith (2003)

**Definition:** Employment density peaks *above* what distance from CBD would predict.

**Why they form (Fujita & Ogawa 1982):**
- Population ↑ → CBD congestion ↑ → firms decentralise
- When decentralised agglomeration forces > CBD access advantage → new stable cluster forms
- Older, larger, more congested cities → more sub-centres

**Evidence:** McMillen & Smith (2003) document sub-centres across US metros; more common in older cities with congested CBDs.

### Edge cities (developer-built) — Henderson & Mitra (1996)

**Definition:** A single developer builds an employment centre — internalises agglomeration gains.

**Developer's trade-off:** closer to CBD = more spillovers but higher wages/land; farther = lower costs but fewer spillovers. Chooses optimal distance K.

**Key example:** Tyson's Corner, VA — **28 million sq ft** Class A office space (vs DC CBD's 17m sq ft). More jobs than bedrooms → net commuting destination.

**Empirical decentralisation:**
- Glaeser & Kahn (2001): fewer than **29%** of US jobs within 3 miles of CBD
- Baum-Snow et al. (2017) China: ring roads displaced **50%** of industrial employment

### How to write it in exam

> "Sub-centres emerge organically when CBD congestion costs exceed the benefits of central access (Fujita & Ogawa 1982). McMillen & Smith (2003) identify sub-centres empirically as density peaks above the distance-predicted level. In contrast, edge cities are strategically built by a single developer who internalises agglomeration gains — Tyson's Corner exemplifies this, with 28 million sq ft of Class A office space exceeding DC's CBD (Henderson & Mitra 1996). Glaeser & Kahn (2001) find fewer than 29% of US jobs remain within 3 miles of the CBD, confirming the extent of decentralisation."

### 📌 中文备考注释

**60分重点在哪：**
这个model主要服务于AT Essay的"Should cities become more polycentric?"部分，以及任何问到sub-centres/edge cities的题。关键是**区分两种类型**：有机形成（organic）和开发商建造（developer-built），两者机制完全不同。

**Sub-centres重点说：**
- 为什么形成：CBD congestion ↑ → decentralisation pressure → firms cluster elsewhere → new stable cluster
- 实证识别方法说一句：density peak above distance-predicted level（这是McMillen & Smith的贡献）

**Edge cities重点说：**
- 单一开发商内化集聚收益（internalise agglomeration gains）— 这是关键词
- 选址trade-off：靠近CBD获得spillovers vs 远离CBD节约土地/工资成本
- Tyson's Corner数字：28m sq ft（比DC CBD的17m还大）

**衔接到"会更多元中心吗"：**
> "Whether polycentricity deepens depends on θ — the spatial decay of spillovers. In knowledge-intensive cities with high θ, CBD advantage remains strong, limiting sub-centre formation. In lower-θ cities or where congestion is severe, polycentric structures are more likely to emerge."

---

## MODEL 5 — LeRoy & Sonstiele (1983): 4-Stage Transport Cycle
*LeRoy & Sonstiele (1983), Couture & Handbury (2020)*

### What it is
A single theory that explains BOTH suburbanisation (rich move out) AND gentrification (rich return to city) through successive transport technology cycles.

### Core mechanism

**Key assumption:** Income elasticity of marginal commuting cost > income elasticity of housing demand
→ Rich value *time saved* more than *bigger houses*

| Stage | Transport | Rich live | Poor live |
|-------|-----------|-----------|-----------|
| 1. Paradise | Slow + cheap only | **Centre** | Periphery |
| 2. Paradise Lost | Fast mode appears (expensive — rich only) | **Suburbs** | Centre |
| 3. Re-gentrification | Fast mode becomes affordable (everyone uses it) | **Centre** (return) | Suburbs |
| 4. Paradise Regained | All have fast transport | Centre | Suburbs |

**US application:**
- 1900s: cars expensive → only rich can drive → Stage 2 (white flight / suburbanisation)
- Late 20th century: cars near-universal (92% of US households own one by 2017) → Stage 3
- Rich return to city: high time value → prefer short commute + urban amenities
- Couture & Handbury (2020): young high-income professionals value **non-tradeable urban goods** (restaurants, culture, nightlife) that only exist in city centres

### How to write it in exam

> "LeRoy & Sonstiele (1983) explain both suburbanisation and its reversal through a 4-stage transport cost cycle. New transport technologies are initially fast but expensive, adopted first by the rich. In Stage 2, wealthy households suburbanise to access cheap land via the new mode. Once the technology becomes affordable for all (Stage 3), the rich lose their differential commuting advantage and return to cities — driven by their higher time value and demand for non-tradeable urban amenities (Couture & Handbury 2020). By 2017, 92% of US households owned a car, consistent with this transition."

> "The model's key assumption is that income elasticity of marginal commuting cost exceeds income elasticity of housing demand — the rich value time savings more than they value additional housing space, making central locations increasingly attractive once commuting costs equalise."

### 📌 中文备考注释

**60分重点在哪：**
Mock Q2(b)直接考这个，40分。必须做到：
1. **说清楚assumption**（时间价值弹性 > 住房需求弹性）— 这是模型成立的前提，很多人漏掉
2. **4个阶段都能说出来**（不需要详细，但要有阶段名称和对应住所）
3. **解释Stage 2→3的转变机制**（快速交通普及后富人失去差异化优势 → 回城）

**这道题的特殊价值：** 它是"唯一一个能同时解释郊区化和绅士化"的理论。答题时要明确说：
> "Unlike the AMM model which only explains suburbanisation, LeRoy & Sonstiele's framework explains both suburbanisation (Stage 2) and its reversal (Stage 3) within a single theoretical framework."

**衔接到Couture & Handbury：**
写完4阶段后加一句：
> "Couture & Handbury (2020) provide complementary evidence: young, high-income professionals increasingly value non-tradeable urban amenities — restaurants, culture, nightlife — that are concentrated in city centres and unavailable in suburbs, reinforcing the Stage 3 return."

**常见错误：** 把4个阶段全写成描述，但没有说assumption和机制。考官要看的是你理解**为什么**富人在每个阶段住在那里，不是单纯列出阶段。

---

## MODEL 6 — Gentrification: Welfare Analysis
*Guerrieri et al. (2013), Ellen & O'Regan (2011), Waights (2018), Ahlfeldt & Maennig (2015)*

### What it is
Who wins and who loses when a neighbourhood gentrifies? The outcome depends critically on tenure (owner vs renter) and mobility costs.

### Core framework

Households consume neighbourhood quality N and non-housing goods G: Y = n·N + G

Gentrification → N↑ → forced to consume more N than preferred → welfare effect depends on whether you can/do move

**Homeowners:**
- N↑ → property value ↑ → capital gain
- Can stay (enjoy) or sell (realise gain)
- Only cost: loss of established social network
- **Unambiguously better off**
- Evidence: Guerrieri et al. (2013) — Harlem prices +**130%** in 2000–06 vs Midtown +**45%**

**Renters — depends on mobility costs:**

| Scenario | Welfare effect |
|----------|--------------|
| No mobility costs | Relocate to preferred neighbourhood → neutral |
| Has mobility costs, moves | Budget shrinks by moving cost → welfare ↓ |
| Has mobility costs, stays | Forced overconsumption of N → welfare ↓ unless... |
| Stays + values amenities | Positive externality offsets forced overconsumption → could be neutral or ↑ |

**Empirical split:**
- **US** (Ellen & O'Regan 2011): modest displacement; stayers often see income gains, lower crime, better schools
- **UK** (Waights 2018): significant displacement of original residents
- Context (tenure laws, mobility costs) determines outcome

**Political economy:**
- Homeowners = "homevoters" → support neighbourhood improvements (Ahlfeldt & Maennig 2015)
- Renters = "leasevoters" → oppose policies that trigger gentrification

### How to write it in exam

> "Gentrification creates clear winners and potential losers depending on housing tenure and mobility costs. Homeowners unambiguously gain: rising neighbourhood quality N capitalises directly into property values, as evidenced by Harlem's 130% price appreciation in 2000–2006 compared to 45% in Midtown Manhattan (Guerrieri et al. 2013). For renters, the welfare effect is ambiguous and depends on mobility costs. With costless mobility, renters can relocate to their preferred neighbourhood and are approximately welfare-neutral. When mobility is costly and renters stay, they face forced overconsumption of N — a welfare loss unless they genuinely value the neighbourhood improvements. Empirically, US evidence suggests modest displacement (Ellen & O'Regan 2011), while UK evidence shows more significant displacement (Waights 2018), reflecting differences in rental tenure security."

### 📌 中文备考注释

**60分重点在哪：**
Mock Q2(c) 30分，Mock反馈明确说：弱答案在"房主赢、租户输"就停了，这只有Pass水平。60分要求：

**必须说到的四层：**
1. **房主：unambiguously better off**（property value capitalises N↑，+Harlem 130% vs 45%）
2. **租户：取决于mobility costs**（这是核心分析）
3. **租户留下 vs 搬走**的分情况讨论（表格里4个场景至少说2个）
4. **实证对比**：US（modest displacement）vs UK（significant displacement）

**这道题的福利框架怎么写：**
先说framework：households consume N and G, budget constraint Y = n·N + G。Gentrification → N↑ → forced overconsumption if preferences haven't changed → welfare loss。然后branching：mobility costs low → can move → welfare neutral；costs high → stuck → welfare loss unless amenities valued。

**US vs UK的差异怎么衔接：**
> "This contrast between US and UK evidence (Ellen & O'Regan 2011 vs Waights 2018) suggests that the welfare outcome for renters is highly context-dependent, reflecting differences in rental tenure security, housing benefit systems, and the strength of displacement pressures."

**政治经济学（加分点）：**
> "This distributional split has political economy implications: homeowners act as 'homevoters' supporting neighbourhood improvement, while renters act as 'leasevoters' opposing gentrification-inducing policies (Ahlfeldt & Maennig 2015)."

---

---

# WT MODELS (Hilber)

---

## MODEL 7 — Tiebout (1956): Vote with Your Feet
*Tiebout (1956), Oates (1969), Black (1999), Gibbons et al. (2013)*

### What it is
Efficient provision of local public goods through residential sorting and inter-jurisdictional competition. Households "vote with their feet" — relocating to the jurisdiction that best matches their tax-service preferences.

### Core mechanism

**Three forces:**
1. **Variety** — multiple jurisdictions offer different tax-service bundles
2. **Sorting** — households reveal preferences through location choices
3. **Competition** — jurisdictions compete for residents → disciplined provision

**5 key assumptions (memorise these):**

| Assumption | Real-world violation |
|-----------|---------------------|
| Perfect information | Information is costly to acquire |
| Costless mobility | Moving costs are high, especially for low-income |
| Many jurisdictions | Limited number of realistic alternatives |
| No spillovers | Education has positive cross-boundary externalities |
| No scale economies | Hospitals, transit require large catchment areas |

### Fiscal capitalisation (the empirical test)

**Prediction:** fiscal variables (taxes, school quality) should be capitalised into house prices.

**Oates (1969) — New Jersey municipalities:**
- Property tax ↑ £1,000 → house price **−£664** (≈67% capitalisation)
- Higher school spending → significantly higher house prices

**School quality capitalisation (subsequent literature):**
- 1 SD improvement in school test scores → house price premium **1.3%–10%**
- Black (1999): sharp price discontinuities at school district boundaries → confirms sorting

### Where it breaks down

1. **Mobility costs** → low-income cannot sort freely → efficiency breaks down for them
2. **Spillovers** → education benefits neighbouring jurisdictions → Tiebout under-provides
3. **Scale economies** → small jurisdictions cannot provide specialised services efficiently
4. **Race to the bottom (Wilson 1986)** → business tax competition depletes public finances
5. **Supply elasticity mediates who benefits (Hilber & Mayer 2009):**
   - Urban areas (inelastic supply): fiscal improvement → **price ↑↑** → homeowners capture all gains; renters pay more
   - Rural areas (elastic supply): fiscal improvement → **quantity ↑** → benefits spread to new residents
   - Urban capitalisation: **33%** vs rural: **10%**

**Policy implication — "Help people, not places" (Hilber et al.):**
Place-based subsidies in supply-constrained areas → capitalised into land values → benefit existing owners, not target households. Direct transfers to people are more effective.

### How to write it in exam

> "Tiebout (1956) argued that residential mobility and inter-jurisdictional competition generate efficient local public good provision: households sort into jurisdictions matching their preferred tax-service bundles, and competition disciplines inefficient provision. The primary empirical test is fiscal capitalisation — Oates (1969) found that a £1,000 increase in property taxes reduces house prices by £664 (67% capitalisation), broadly consistent with the model."

> "However, the efficiency result depends on assumptions routinely violated in practice. High mobility costs prevent low-income households from sorting freely. Education generates positive cross-boundary spillovers that Tiebout ignores, leading to under-provision. Furthermore, Hilber & Mayer (2009) show that supply elasticity fundamentally determines *who* benefits from fiscal improvements: in supply-constrained urban areas, improved school quality capitalises into prices (33% rate), benefiting homeowners rather than renters. In elastic rural areas, the capitalisation rate is only 10% as supply expands."

### 📌 中文备考注释

**60分重点在哪：**
这道题的结构是：先说模型成立（mechanism + 实证支撑）→ 再系统批判（4个假设失效）→ 最重要的是加入supply elasticity这个维度（很多人漏掉这个）。

**答题黄金结构：**
1. 机制：variety + sorting + competition → efficiency（2句话）
2. 实证支撑：Oates (1969) — £664/£1000；学校质量 1SD → 1.3%-10% 房价（2句话）
3. 批判1：假设失效 — 重点讲mobility costs（最现实）和spillovers（教育外部性）
4. 批判2（核心，高分）：**Supply elasticity mediates who benefits** — Hilber & Mayer 33% vs 10%
5. Policy implication："help people not places"

**供给弹性这个点怎么衔接：**
> "A further limitation, not anticipated by Tiebout, is that the degree of fiscal capitalisation — and therefore who captures the fiscal surplus — depends critically on housing supply elasticity. Hilber & Mayer (2009) find that in supply-constrained urban areas, improved school quality raises prices by 33 cents per pound of expenditure, concentrating gains with homeowners. In elastic rural areas, the capitalisation rate falls to 10% as supply expands to accommodate new demand."

**"Race to the bottom"要不要说：** 可以加一句，但不要展开，它属于加分点不是核心。

---

## MODEL 8 — Land Use Regulation: Market Failure vs Policy Failure
*Fischel (2000), Hilber & Robert-Nicoud (2013), H&V (2016), Hsieh & Moretti (2019)*

### What it is
Two competing frameworks for why planning regulation exists and whether it is welfare-improving. Cheshire (2013): in Britain, **policy failure > market failure**.

### Market failure — 4 justifications for LUR

1. **Negative externalities** — development causes congestion, pollution, visual intrusion → private over-development
2. **Positive externalities / public goods** — historic buildings, parks: non-excludable, non-rival → market under-provides
3. **Coordination failure (hold-out problem)** — land assembly for large developments requires all owners to agree; one strategic hold-out blocks socially beneficial redevelopment
4. **Information asymmetry** — planners may know more about infrastructure capacity than developers

### Policy failure — 2 mechanisms

**1. Homevoter hypothesis (Fischel 2000):**
- Housing = middle-class households' primary (undiversifiable) asset
- Homeowners systematically vote/lobby *against* new development → protects their property value
- Democratic planning process → captures homeowner interests, not aggregate welfare
- Produces *excessive* restriction beyond social optimum

**2. Influential landowner hypothesis (Hilber & Robert-Nicoud 2013):**
- Already-developed landowners lobby for restrictions → constrained supply → their land rents rise
- Prediction: areas that are already developed → more restrictive planning → higher prices → larger cycles
- Endogenous regulation: areas with high demand attract stricter controls (confirmed by H&V 2016)

### Empirical evidence

**Costs of LUR (policy failure side):**
- H&V (2016): counterfactual — if England had US planning flexibility → house prices **35% lower**
- Cheshire & Hilber (2008): London West End office — regulatory tax = **809%** of construction cost (i.e., regulation makes building 9× more expensive)
- Hsieh & Moretti (2019): removing US housing constraints post-1964 → aggregate GDP **+2% per year**
- Cheshire et al. (2018): planning refusal rate +1SD → vacancies +**23%**, commuting distances +**6.1%**

**Benefits of LUR (market failure side):**
- Some evidence of positive capitalisation near protected buildings (Been et al. 2016; Koster et al. 2016)
- But: capitalisation ≠ welfare maximisation (only captures benefit to marginal buyer; ignores aggregate supply effects)

**Net effect:**
- Turner et al. (2014): net welfare of UK LUR is **negative** — DWL of excessive regulation > DWL of market solution

### How to write it in exam

> "Land use regulation is justified by genuine market failures: negative development externalities, under-provision of public goods (parks, historic buildings), coordination failures in land assembly, and information asymmetries. These failures justify some planning intervention — as Cheshire (2013) acknowledges."

> "However, policy failure arises because planning is not determined by a benevolent planner but by a political process. Fischel's (2000) homevoter hypothesis argues that homeowners — for whom housing is their primary undiversifiable asset — systematically lobby against new development to protect property values. Hilber & Robert-Nicoud (2013) show that already-developed landowners lobby for restrictions that raise rents on their existing assets. The result is excessive restriction beyond the social optimum."

> "Empirically, the costs appear to dominate. Hilber & Vermeulen (2016) estimate that US-style planning flexibility would reduce English house prices by 35%. Hsieh & Moretti (2019) find that removing US housing constraints would raise aggregate GDP by 2% annually. Cheshire's claim that policy failure exceeds market failure in Britain is well-supported."

### 📌 中文备考注释

**60分重点在哪：**
Mock反馈明确：这道题"一阶概念缺口"是没有讲政治经济学理论（homevoter + influential landowner）。只讲市场失灵不够，必须讲为什么**政策**会失灵。

**答题层次：**
- 第一层（Pass）：市场失灵4个来源 + 简单提一下LUR可能过度
- 第二层（Merit/60+）：讲清楚homevoter和influential landowner两个mechanism + 用H&V (35%) 和Hsieh & Moretti (2% GDP) 支撑成本远大于收益
- 第三层（Distinction）：批判证据的局限性（capitalisation ≠ welfare maximisation）+ 综合结论

**两个政治经济学理论的区别：**
- Homevoter (Fischel)：**民主选举机制**被现有房主捕获 → 投票反对新建
- Influential landowner (H&RN)：**游说机制**被大地主捕获 → 限制竞争、保护地租

写答案时先写Fischel（更intuitive），再写H&RN（更sophisticated），最后说两者共同预测：开发程度越高的地区 → 限制越严格 → H&V实证证实。

**实证证据怎么呈现：**
不要只列数字，要说为什么这个数字说明policy failure > market failure：
> "Hilber & Vermeulen (2016) estimate that if England had adopted US-level planning flexibility, house prices would be 35% lower. This scale of distortion — driven primarily by regulatory rather than physical constraints — is difficult to justify on market failure grounds alone, suggesting that policy failure is the dominant force."

**一个好的conclusion句：**
> "The implication is not to abolish planning — genuine externalities justify some regulation — but to redesign it to be less captured by existing property interests, working with markets rather than against them."

---

## MODEL 9 — Identification Problem & IV/2SLS
*Bartik (1991), Saiz (2010), Mayer & Somerville (2000)*

### What it is
Why we cannot simply regress house prices on quantity to estimate supply or demand curves — and how instrumental variables solve this.

### The identification problem

**We observe:** equilibrium (P*, Q*) — lies simultaneously on *both* supply and demand curves.

**The problem:** When P and Q move together, we cannot tell if:
- Demand shifted right → movement along supply curve (would identify supply slope)
- Supply shifted right → movement along demand curve (would identify demand slope)
- Both shifted simultaneously

**OLS failure:** P is jointly determined with Q → Cov(P, ε) ≠ 0 → OLS coefficient is biased. It estimates neither supply nor demand — a weighted average of both.

### Solution: IV / 2SLS

**Principle:** To estimate the *supply* curve, we need an instrument Z that:
1. **Shifts demand** (relevant: Z correlated with P) — keeps supply fixed, so movement traces out supply slope
2. **Does NOT directly affect supply** (exclusion restriction: Z ⊥ ε_supply)

**The Bartik shift-share instrument (Bartik 1991):**
> Z_jt = Σ_k (share of industry k in region j at base year) × (national employment growth in industry k at time t)

- Captures exogenous local demand variation from *national* industry trends
- Exclusion restriction: national trends affect local housing demand through income, but do NOT directly affect local construction costs or planning constraints

**Two-stage procedure:**
- **First stage:** ΔP_t = β₀ + β₁·ΔZ_t + supply shifters + μ_t → get predicted Δ P̂_t
- **Second stage:** ΔQ_t = α₀ + α₁·Δ P̂_t + supply shifters + ε_t → **α₁ = supply elasticity**

**Why use changes (ΔP, ΔQ) not levels?**
House prices and stock are non-stationary (trending). Regressing levels on levels → spurious regression. First-differencing removes the trend (Mayer & Somerville 2000).

### How to write it in exam

> "The identification problem arises because observed equilibrium (P*, Q*) lies simultaneously on both the supply and demand curves. OLS regression of Q on P is biased because price is jointly determined with quantity — we cannot distinguish supply from demand shifts."

> "The solution is IV/2SLS with a demand-shifting instrument to identify the supply curve. The Bartik (1991) shift-share instrument exploits the interaction between local industry composition (fixed at a base year) and national industry employment trends. This generates exogenous variation in local demand, holding supply conditions fixed. The exclusion restriction — that national industry trends affect local housing only through income, not through construction costs — is plausible but not guaranteed."

### 📌 中文备考注释

**60分重点在哪：**
这道题WT部分会直接考（Mock Q4 + 2013/14 Q6都考过）。识别问题（a）是基础，IV方法（b）是核心，方程（c）是加分，locational determinants（d）是深度。

**识别问题（a）的表述套路：**
三步走：
1. 我们观察到的是均衡点(P*, Q*)，它同时在供给曲线和需求曲线上
2. OLS回归 Q on P → biased，因为P和Q jointly determined（Cov(P,ε) ≠ 0）
3. 所以估计的结果既不是供给曲线也不是需求曲线

> "A simple OLS regression of quantity on price estimates neither the supply nor the demand curve — it estimates a weighted average of both, since price is jointly determined with quantity in equilibrium."

**Bartik工具的排他性限制怎么解释：**
> "The exclusion restriction requires that national industry employment trends affect local housing markets *only* through the income channel — not through direct effects on local construction costs or planning decisions. This is plausible since national trends are driven by aggregate factors outside any single region's control."

**Mock考试最大错误（必须避免）：**
- 有人建议用DiD（差分法）来估计弹性 — 这是错误的！DiD估计的是treatment effect，不是弹性的slope
- 第一阶段第二阶段搞混（第一阶段回归的是价格，不是数量）
- 用levels不用changes（non-stationarity问题 — Mayer & Somerville 2000就是因为这个才用changes）

---

## MODEL 10 — Housing Supply Elasticity
*H&V (2016), Saiz (2010), Mayer & Somerville (2000), Hilber & Mayer (2009), Hilber & Mense (2025)*

### What it is
How much does housing quantity respond to a price increase? Determined by physical geography and planning regulation.

### Key estimates (memorise these)

| Study | Elasticity | What it covers |
|-------|-----------|---------------|
| Mayer & Somerville (2000) | Stock: **0.08**; Starts: **6.3** | US; stock nearly inelastic (housing durable) |
| Saiz (2010) | Average: **1.7** (range 0.6–5.5) | US metro areas; topographic IV |
| Hilber & Mense (2025) | Average: **1.16** (range 0.15–3.6) | UK; much lower than US |
| Hilber & Mayer (2009) | Urban: **0.014**; Rural: **0.16** | Within-city land availability |

**Why stock elasticity (0.08) << starts elasticity (6.3):**
Housing is highly durable — new construction is only 1–2% of total stock per year. Even a large starts response barely moves the stock.

### Two types of constraint (H&V 2016)

**1. Physical/topographic constraints:**
- Water bodies, steep slopes (>15%) → limit buildable land
- Saiz (2010): constructs Residential Land Available (RLA) index from satellite GIS data
- More undevelopable land → less buildable land → higher land prices → lower elasticity

**2. Regulatory constraints:**
- Zoning, height limits, conservation areas, green belts
- H&V (2016): measured using 1947–79 local planning committee vote data
- **Key finding: regulatory constraints > physical constraints** in explaining English house price cycles
- Regulatory elasticity: **−0.13**; physical: **−0.09**

**Why less developable land → lower elasticity (3 channels):**
1. *Cost channel:* Building on constrained land is more expensive
2. *Political economy:* Dense areas have more homeowners with NIMBY incentives → stricter planning
3. *Real options (Grenadier 1995):* Scarce land has high option value → developers delay → supply lags

### How to write it in exam

> "Housing supply elasticity measures the percentage increase in housing quantity for a 1% price increase. Estimates vary substantially: Saiz (2010) finds an average of 1.7 for US metros (range 0.6–5.5), while Hilber & Mense (2025) find a lower average of 1.16 for the UK, reflecting stricter planning. Mayer & Somerville (2000) distinguish stock elasticity (0.08) from new starts elasticity (6.3) — the former is near-zero because new construction is only 1–2% of total stock annually."

> "Hilber & Vermeulen (2016) decompose supply constraints into physical (topographic) and regulatory components, finding that regulatory constraints (elasticity −0.13) dominate physical constraints (−0.09) in explaining English house price variation. Their counterfactual: US-like planning flexibility would reduce English house prices by 35%."

**Policy implications (2013/14 Q6c — "why does it matter for investors and policymakers?"):**

*For investors:*
- Elastic market (e.g., Houston): demand shock → quantity ↑, price stable → predictable rental yields, lower capital gain risk
- Inelastic market (e.g., London): demand shock → price ↑↑ → higher appreciation potential but larger downside risk
- Knowing elasticity allows portfolio positioning: overweight inelastic markets for price appreciation; expect stable income returns in elastic markets

*For policymakers — the counter-intuitive result:*
> "Hilber & Turner (2014) find that housing subsidies — such as the UK's Help-to-Buy or the US mortgage interest deduction — have zero average effect on homeownership rates nationally, and a **negative effect** in supply-inelastic markets. The mechanism: subsidy → demand ↑ → in inelastic markets, price ↑↑ rather than quantity ↑ → deposit requirements rise → first-time buyers are priced out further. The subsidy is captured by existing owners, not the intended beneficiaries."

> "This implies that the policy value of knowing supply elasticity is substantial: interventions designed to expand homeownership are only effective where supply can actually respond. In constrained markets, 'help people not places' — direct transfers to households outperform place-based subsidies that capitalise into land values."

### 📌 中文备考注释

**60分重点在哪：**
数字是这道题的命根。把4个关键弹性估计记住（0.08/6.3/1.7/1.16/0.014/0.16），然后能解释为什么这些数字有意义。

**0.08 vs 6.3的解释（必考）：**
不能只报数字，要说为什么差这么大：
> "Mayer & Somerville (2000) distinguish stock elasticity (0.08) from new starts elasticity (6.3). The near-zero stock elasticity reflects housing durability — new construction accounts for only 1–2% of total stock annually, so even a large starts response barely moves the overall supply."

**UK vs US弹性差异（必考）：**
> "The UK average supply elasticity of 1.16 (Hilber & Mense 2025) is substantially lower than the US average of 1.7 (Saiz 2010), reflecting stricter planning regulation in the UK rather than differences in physical geography alone."

**三个渠道（为什么developable land少 → 弹性低）：**
很多人只说"土地少所以建不了" — 这太简单。60分要说三个渠道：cost channel + political economy（NIMBY/homevoter） + real options（option value → 开发商等待）。

**政策含义这一段（Mock Q4c / 2013/14 Q6c）：**
记住Hilber & Turner的结论：在非弹性市场，补贴完全无效甚至有害（subsidies → demand↑ → price↑↑ → 首付要求↑ → 反而减少homeownership）。这个反直觉结论是高分点。

---

## MODEL 11 — Real Estate Cycles: Supply Constraints Theory
*Hilber & Vermeulen (2016), Saiz (2010)*

### What it is
Real estate price cycles as a **fundamental** phenomenon: demand shocks amplified by inelastic supply. Not a bubble — a structural outcome.

### Core mechanism

> Supply-inelastic markets: demand shock → price ↑↑ (little quantity response) → serial correlation + mean reversion

> Supply-elastic markets: demand shock → quantity ↑, price ≈ stable → no persistent cycle

**Two types of supply constraint (H&V 2016):**
- **Physical:** undevelopable land — Saiz (2010) topographic index
- **Regulatory:** planning restrictions — H&V use 1947–79 planning vote data

**H&V (2016) key findings:**
- Regulatory constraint elasticity: **−0.13**
- Physical constraint elasticity: **−0.09**
- Regulatory > physical in explaining English house price cyclicality
- Counterfactual: US-like flexibility → prices **35% lower**

**City comparison:**
- San Francisco (inelastic — topography + strict regulation) → extreme boom-bust
- Columbus, OH (elastic — flat terrain, permissive) → near-zero price volatility

**Predictions of this theory:**
1. Price cycles larger in constrained (inelastic) markets
2. Demand fundamentals (income, employment) drive cycles in constrained markets
3. Unconstrained markets adjust via quantity, not price

### How to write it in exam

> "One fundamental explanation for real estate cycles is the interaction of demand shocks with inelastic housing supply. In supply-constrained markets, positive demand shocks (income growth, population influx) cannot be absorbed by new construction, generating large price increases. These prices are serially correlated as expectations adjust and mean-reverting as supply eventually responds. Hilber & Vermeulen (2016) decompose supply constraints into physical (topographic, elasticity −0.09) and regulatory (planning, −0.13) components, finding regulatory constraints dominate in England. Their counterfactual implies that US-level planning flexibility would reduce English house prices by 35%."

### 📌 中文备考注释

**60分重点在哪：**
这是WT Cycles Part(a)的Theory 1（fundamental explanation）。关键是要说清楚**为什么非弹性供给会产生周期**，而不只是说"供给弹性低所以价格高"。

**核心逻辑链（必须走完）：**
需求冲击（income↑ / population↑）→ 在非弹性供给市场 → 无法通过新建吸收 → 价格↑↑ → 序列相关（serial correlation）→ 最终均值回归（mean reversion）→ 这就是"周期"

**Serial correlation + mean reversion这两个概念怎么解释：**
> "This interaction generates the two defining features of real estate cycles: serial correlation — prices above trend tend to remain above trend as expectations adjust — and eventual mean reversion, as supply slowly responds or demand moderates."

**SF vs Columbus的对比（必须举）：**
San Francisco（非弹性）→ 极端繁荣-萧条；Columbus OH（弹性）→ 价格几乎没有波动。这是最直观的evidence，答题中一句话带过。

**和Theory 2（loss aversion）怎么衔接：**
> "While H&V (2016) offer a fundamentals-based explanation for cycles, a complementary behavioural account focuses on why prices fall more slowly than they rise — specifically, loss aversion (Genesove & Mayer 2001)."

---

## MODEL 12 — Real Estate Cycles: Loss Aversion
*Genesove & Mayer (2001, QJE), Kahneman & Tversky (prospect theory)*

### What it is
A **behavioural** explanation for why house prices fall slowly in downturns: sellers resist realising nominal losses.

### Core mechanism

**Prospect theory (Kahneman & Tversky):** losses feel twice as painful as equivalent gains. Applied to housing: sellers compare current market value to their *purchase price* (the reference point).

**When current price < purchase price (nominal loss territory):**
- Seller refuses to accept the loss → sets higher asking price
- Stays on market longer
- Price stickiness → market doesn't clear quickly → volume collapses
- Creates asymmetric price dynamics: prices fall slowly in downturns, rise more quickly in booms

### Key findings — Genesove & Mayer (2001)

**Setting:** Boston condo market, early 1990s downturn. Compare sellers in nominal loss vs sellers not in loss.

| Metric | Finding |
|--------|---------|
| Asking price | **3–18% higher** than comparable sellers without losses |
| Transaction price | **3–7% higher** (partial, not full, exploitation) |
| Time on market | Significantly longer |
| Effect stronger for... | Higher LTV (deeper paper loss) |

**Predictions:**
1. Downturns: price stickiness → slow decline → prolonged adjustment
2. Transaction volume collapses before prices fall (prices are last to move)
3. Markets with more leveraged buyers → stronger loss aversion effects

### How to write it in exam

> "Genesove & Mayer (2001) apply prospect theory to explain downward price rigidity in housing markets. Sellers facing nominal losses — where purchase price exceeds current market value — resist accepting those losses, posting asking prices 3–18% above comparable non-loss sellers and achieving transaction prices 3–7% higher, though at the cost of significantly longer time on market. This loss aversion generates price stickiness in downturns: rather than prices falling quickly to clear the market, transaction volumes collapse while prices decline slowly. The mechanism explains why housing market recessions are characterised by quantity collapse before price adjustment."

### 📌 中文备考注释

**60分重点在哪：**
这是WT Cycles Part(a)的Theory 2（behavioural explanation）。必须给三件事：mechanism + predictions + evidence。缺任何一个都是弱答案。

**Mechanism的表述顺序：**
1. 从prospect theory出发（losses feel more painful than equivalent gains）
2. 应用到住房：reference point = 买入价格
3. 当当前价格 < 买入价格 → nominal loss → 卖家拒绝接受损失
4. → 挂牌价更高 → 在市场上停留更长 → 价格下行粘性

**数字怎么用（必须精确）：**
- Asking price高 **3–18%**（这是范围，反映LTV程度）
- Transaction price高 **3–7%**（比挂牌价低 — 说明卖家部分妥协了，但仍显著高于无损失卖家）
- LTV越高 → 账面损失越深 → 效应越强

**Predictions怎么写（高分）：**
> "Loss aversion generates three predictions: first, prices in downturns decline more slowly than fundamentals would predict; second, transaction volumes collapse before prices fall — sellers exit the market rather than accept losses; third, markets with higher leverage (more sellers in nominal loss territory) experience more prolonged price stickiness."

**这个theory和H&V互补关系：**
H&V解释为什么**upswing**那么大（非弹性供给放大需求冲击）；Loss aversion解释为什么**downswing**那么慢（价格向下粘性）。两者放在一起是完整的cycles解释。

---

## MODEL 13 — Cobweb Model & Construction Lag
*Wheaton (1999)*

### What it is
Cyclical overshooting in construction due to the **time lag** between price signal and supply delivery.

### Core mechanism

**The lag problem:**
- Today's price ↑ → developers decide to build → construction takes 2–4 years
- Supply arrives years after the signal → if demand has reversed by then → oversupply → price crash

**Cobweb cycle:**
1. Demand ↑ → prices ↑
2. Developers respond to today's high prices → start construction
3. 2–4 years pass
4. New supply hits market → demand may have already fallen
5. Oversupply → prices ↓
6. Developers stop building → supply shortage builds again → cycle repeats

**Why commercial > residential cycles:**
- Office/retail: planning + construction takes longer (3–7 years) → bigger lag → more overshooting
- Leases: 5–25 year commercial leases → slower demand adjustment

**Application to Las Vegas & Phoenix (2000–2009):**
- Low interest rates → massive speculative demand → prices ↑ → developers build at scale
- Credit dries up 2006 → speculative demand collapses → supply arrives into empty market
- Elastic supply amplified the *quantity* boom-bust (not just price)

### How to write it in exam

> "The Cobweb model (Wheaton 1999) explains real estate cycles through construction lags. Developers respond to current prices, but supply only arrives 2–4 years later. If demand reverses before supply is delivered, the market is flooded with excess inventory, triggering a price crash. This creates self-sustaining cycles: oversupply → low prices → under-building → shortage → high prices → over-building. The mechanism is especially powerful in commercial real estate, where planning and construction timelines extend to 3–7 years."

### 📌 中文备考注释

**60分重点在哪：**
Cobweb主要用在两个地方：① Part(a)选它作Theory之一（但不如H&V和Genesove & Mayer强）；② **LV/PHX Part(c)的核心解释**（20分）。

**LV/PHX的解释套路（20分题别超过10分钟）：**
三步：
1. 说明paradox（弹性供给 → 按AMM理论不该有大价格周期）
2. 解释：speculative demand（非基本面需求，由低利率/次贷驱动）+ Cobweb（建设时滞）
3. 说弹性供给的paradox：弹性供给只能稳定**fundamental demand驱动**的价格，无法防止**speculative demand**驱动的周期

> "The elastic supply paradox: unlike San Francisco where supply inelasticity amplified fundamental demand shocks, Las Vegas and Phoenix experienced both price *and* quantity booms driven by non-fundamental speculative demand. When speculative demand collapsed post-2006, elastic construction had generated massive excess inventory, amplifying rather than dampening the price crash."

**商业地产 > 住宅地产的原因（可能单独考）：**
两个渠道：更长的建设时滞（3-7年 vs 1-2年）+ 更长的租约（5-25年 → 需求调整更慢）。两者叠加 → 商业地产cobweb效应更强。

---

## MODEL 14 — Irrational Exuberance / Extrapolative Expectations
*Case & Shiller (1988, 1989, 2003, 2012)*

### What it is
House prices deviate from fundamentals because buyers form **extrapolative expectations** — expecting past price growth to continue, even when fundamentals don't justify it.

### Core mechanism

**Rational expectations:** buyers use all available information to forecast future prices.

**Extrapolative expectations (what actually happens):** buyers look at recent price trends and assume they will continue. If prices rose 10% last year → expect 10% again → buy at any current price → demand further pushes prices up → self-fulfilling momentum.

**Case & Shiller methodology:**
- Survey homebuyers in boom markets: "What do you expect house prices to do?"
- Finding: in boom markets, buyers expect continued price rises at rates inconsistent with long-run fundamentals → evidence of irrational exuberance

**Predictions:**
1. Boom: prices overshoot fundamentals (momentum > fundamentals)
2. Eventually: expectations correct → demand collapses → prices revert to fundamental value
3. The correction can be sharp (crash) because it involves unwinding leveraged positions

**Difficulty distinguishing from rational expectations:**
- A rational buyer *should* expect prices to rise if they believe demand will continue to grow
- Cannot directly observe whether expectations are rational or extrapolative from prices alone
- Survey evidence is the primary tool

### How to write it in exam

> "Case & Shiller (1988, 1989, 2003) document extrapolative expectations in housing markets: survey evidence shows that buyers in boom markets expect continued price appreciation at rates inconsistent with long-run fundamentals. This 'irrational exuberance' generates momentum beyond what supply-demand fundamentals can explain — rising prices fuel further buying, pushing prices further above equilibrium. The main empirical difficulty is distinguishing rational forward-looking expectations (which could also justify price rises if fundamentals are expected to improve) from truly irrational extrapolation. Survey data provides the most direct evidence but may not reflect actual trading behaviour."

### 📌 中文备考注释

**60分重点在哪：**
Case & Shiller主要用于Part(b)（fundamentals vs deviation from equilibrium），而不是Part(a)（两个theories）。作为Part(b)的第三个实证方法（survey approach）来用。

**Part(b)三种方法的分工：**
1. **Capozza et al. (2004)** — 回归方法：看fundamentals解释不了的serial correlation还有多少
2. **H&V (2016)** — 结构性IV：isolate residual beyond fundamentals
3. **Case & Shiller surveys** — 直接问买家预期：发现boom市场的预期超出fundamentals → extrapolative

**这个方法的核心困难（必须说）：**
> "The central empirical challenge is that rational expectations and extrapolative expectations can generate observationally similar price paths. Survey data provides the most direct evidence but is subject to stated-preference bias — respondents may not act on their stated beliefs."

**总结Part(b)的conclusion怎么写：**
> "The empirical literature suggests that both fundamentals and non-fundamental deviations contribute to real estate cycles. In supply-constrained markets, fundamental demand shocks generate large price movements; behavioural factors — loss aversion (Genesove & Mayer) and extrapolative expectations (Case & Shiller) — amplify and prolong these movements beyond what fundamentals alone predict."

---

---

# MASTER KEY NUMBERS (memorise all of these)

| Number | Paper | What it means |
|--------|-------|--------------|
| **−1.4%/km** | Liotta et al. (2022) | Global rent gradient from CBD |
| **−50%** | Heblich et al. (2020) | Land values if London rail network removed |
| **−18%** | Baum-Snow (2007) | Central city population per urban highway |
| **<29%** | Glaeser & Kahn (2001) | US jobs within 3 miles of CBD |
| **3.4m vs 100k** | Ahlfeldt et al. (2020) | NYC vs LA population in 1900 → path dependence |
| **28m vs 17m sq ft** | Henderson & Mitra (1996) | Tyson's Corner vs DC Class A office |
| **130% vs 45%** | Guerrieri et al. (2013) | Harlem vs Midtown price rise 2000–06 |
| **92%** | LeRoy-Sonstiele | US households with a car (2017) |
| **−0.13 / −0.09** | H&V (2016) | Regulatory / physical constraint price elasticity |
| **35%** | H&V (2016) | House price reduction if England = US planning |
| **809%** | Cheshire & Hilber (2008) | London West End regulatory tax as % of construction cost |
| **+2% GDP** | Hsieh & Moretti (2019) | Annual US GDP gain if housing constraints removed |
| **+23% / +6.1%** | Cheshire et al. (2018) | Vacancy / commuting increase per 1SD refusal rate ↑ |
| **0.08 / 6.3** | Mayer & Somerville (2000) | US stock / new starts supply elasticity |
| **1.7** | Saiz (2010) | US average supply elasticity (range 0.6–5.5) |
| **1.16** | Hilber & Mense (2025) | UK average supply elasticity (range 0.15–3.6) |
| **0.014 / 0.16** | Hilber & Mayer (2009) | Urban / rural supply elasticity |
| **33% / 10%** | Hilber & Mayer (2009) | Urban / rural fiscal capitalisation rate |
| **3–18% / 3–7%** | Genesove & Mayer (2001) | Loss aversion: asking / transaction price premium |
| **£664 / £1,000** | Oates (1969) | Tax capitalisation into house prices (67%) |
| **1.3%–10%** | Gibbons et al. etc. | School quality 1SD → house price premium |
