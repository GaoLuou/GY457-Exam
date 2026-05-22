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
