# Market data snapshot

**Generated:** 2026-09-26T00:32:46+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 20 / 20

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 341.07 | 321.83 | 311.74 | 287.77 | +18.52% | 0.58x | rising | rising | +0.1543 |
| **AMD** | 630.63 | 504.71 | 500.49 | 364.75 | +72.89% | 0.61x | rising | rising | +0.3901 |
| **AMZN** | 249.67 | 256.18 | 254.42 | 240.85 | +3.66% | 0.74x | falling | rising | +0.1199 |
| **AVGO** | 352.81 | 376.63 | 390.35 | 368.35 | -4.22% | 0.62x | falling | rising | +0.0420 |
| **BLK** | 1,086.31 | 1,108.38 | 1,071.95 | 1,061.39 | +2.35% | 0.74x | falling | falling | -0.0330 |
| **BRK.B** | 505.48 | 506.29 | 496.68 | 492.65 | +2.60% | 0.62x | rising | rising | +0.0513 |
| **CAT** | 821.58 | 829.23 | 879.36 | 789.56 | +4.05% | 0.65x | rising | rising | +0.1264 |
| **GOOGL** | 343.92 | 344.29 | 357.86 | 338.21 | +1.69% | 0.71x | rising | falling | -0.0268 |
| **INTC** | 123.00 | 99.05 | 108.29 | 79.20 | +55.30% | 0.81x | rising | rising | +0.2009 |
| **META** | 751.66 | 615.75 | 609.73 | 626.47 | +19.98% | 1.37x | rising | rising | +0.0304 |
| **MSFT** | 516.17 | 475.81 | 438.84 | 432.06 | +19.47% | 1.10x | falling | rising | +0.0575 |
| **MU** | 1,082.28 | 941.62 | 935.56 | 661.10 | +63.71% | 0.47x | rising | rising | +0.2207 |
| **NVDA** | 225.07 | 215.98 | 212.88 | 199.47 | +12.83% | 0.63x | rising | falling | -0.0416 |
| **PLTR** | 189.67 | 163.93 | 148.24 | 152.02 | +24.76% | 0.45x | rising | rising | +0.1107 |
| **QQQ** | 744.50 | 712.65 | 715.69 | 665.59 | +11.86% | 0.75x | rising | rising | +0.2028 |
| **SCHD** | 33.21 | 34.06 | 33.13 | 31.59 | +5.13% | 1.09x | falling | falling | -0.2816 |
| **SMH** | 606.56 | 565.89 | 581.27 | 493.28 | +22.96% | 0.46x | rising | rising | +0.1545 |
| **SPY** | 771.35 | 761.57 | 752.78 | 718.45 | +7.36% | 0.72x | falling | rising | +0.0273 |
| **TSLA** | 372.11 | 348.25 | 379.11 | 395.62 | -5.94% | 1.04x | rising | falling | -0.0931 |
| **UNH** | 376.59 | 399.38 | 400.51 | 355.43 | +5.95% | 0.71x | falling | falling | -0.0663 |

## Validation vs Twelve Data's own OBV / AD endpoints

Absolute levels are expected to differ (both are cumulative from an arbitrary
start). Only DIRECTION must agree. A mismatch means something is wrong.

- **AAPL** — ✅ pass
  - `obv`: ours **rising** vs theirs **rising**
  - `ad`: ours **rising** vs theirs **rising**
- **QQQ** — ✅ pass
  - `obv`: ours **rising** vs theirs **rising**
  - `ad`: ours **rising** vs theirs **rising**

---

_Automated market-data snapshot. Public market data only —
this repository contains no holdings, positions or personal information._
