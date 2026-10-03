# Market data snapshot

**Generated:** 2026-10-03T01:05:29+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 20 / 20

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 333.69 | 322.42 | 313.94 | 289.16 | +15.40% | 0.63x | falling | rising | +0.0566 |
| **AMD** | 633.91 | 513.53 | 510.27 | 374.72 | +69.17% | 0.73x | rising | rising | +0.3447 |
| **AMZN** | 251.52 | 256.54 | 253.22 | 241.36 | +4.21% | 0.75x | falling | falling | -0.0018 |
| **AVGO** | 355.14 | 373.22 | 386.66 | 367.50 | -3.36% | 0.97x | rising | falling | -0.1507 |
| **BLK** | 1,059.63 | 1,109.65 | 1,071.60 | 1,060.86 | -0.12% | 0.78x | falling | falling | -0.0586 |
| **BRK.B** | 502.65 | 507.38 | 498.09 | 492.77 | +2.01% | 0.88x | rising | rising | +0.0035 |
| **CAT** | 845.42 | 823.45 | 875.14 | 795.10 | +6.33% | 0.81x | rising | rising | +0.1118 |
| **GOOGL** | 343.50 | 344.37 | 355.21 | 338.92 | +1.35% | 0.76x | rising | falling | -0.0738 |
| **INTC** | 119.33 | 100.87 | 108.35 | 81.18 | +47.00% | 0.82x | rising | rising | +0.1333 |
| **META** | 728.08 | 625.04 | 615.63 | 628.38 | +15.87% | 0.68x | rising | falling | -0.0388 |
| **MSFT** | 517.53 | 487.72 | 443.71 | 432.83 | +19.57% | 0.51x | falling | rising | +0.0171 |
| **MU** | 1,074.89 | 956.05 | 954.17 | 681.61 | +57.70% | 0.63x | rising | rising | +0.0834 |
| **NVDA** | 233.95 | 218.28 | 213.87 | 200.71 | +16.56% | 0.97x | rising | falling | -0.2166 |
| **PLTR** | 188.75 | 169.78 | 150.83 | 152.10 | +24.09% | 0.47x | rising | rising | +0.0921 |
| **QQQ** | 749.53 | 716.82 | 717.78 | 668.60 | +12.10% | 1.56x 🔺 | rising | rising | +0.0940 |
| **SCHD** | 32.72 | 34.05 | 33.18 | 31.72 | +3.16% | 0.94x | falling | falling | -0.4006 |
| **SMH** | 630.75 | 569.85 | 584.36 | 499.50 | +26.28% | 1.41x | rising | rising | +0.0799 |
| **SPY** | 769.64 | 763.70 | 754.38 | 720.47 | +6.82% | 0.94x | falling | falling | -0.0686 |
| **TSLA** | 370.59 | 347.58 | 376.28 | 393.18 | -5.75% | 1.29x | falling | falling | -0.1927 |
| **UNH** | 371.90 | 393.74 | 400.42 | 356.35 | +4.36% | 0.58x | falling | falling | -0.0536 |

## Validation vs Twelve Data's own OBV / AD endpoints

Absolute levels are expected to differ (both are cumulative from an arbitrary
start). Only DIRECTION must agree. A mismatch means something is wrong.

- **AAPL** — ✅ pass
  - `obv`: ours **falling** vs theirs **falling**
  - `ad`: ours **rising** vs theirs **rising**
- **QQQ** — ✅ pass
  - `obv`: ours **rising** vs theirs **rising**
  - `ad`: ours **rising** vs theirs **rising**

---

_Automated market-data snapshot. Public market data only —
this repository contains no holdings, positions or personal information._
