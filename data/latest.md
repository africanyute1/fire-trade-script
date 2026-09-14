# Market data snapshot

**Generated:** 2026-09-14T20:58:29+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 20 / 20

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 333.00 | 318.46 | 305.99 | 285.24 | +16.74% | 0.03x | rising | rising | +0.1175 |
| **AMD** | 493.26 | 496.06 | 478.22 | 348.30 | +41.62% | 0.70x | falling | rising | +0.1089 |
| **AMZN** | 253.57 | 255.47 | 255.44 | 239.93 | +5.68% | 0.03x | falling | rising | +0.1140 |
| **AVGO** | 344.82 | 382.77 | 396.10 | 370.04 | -6.81% | 0.84x | falling | falling | -0.0452 |
| **BLK** | 1,065.85 | 1,102.53 | 1,070.85 | 1,060.84 | +0.47% | 0.34x | falling | falling | -0.3085 |
| **BRK.B** | 514.91 | 503.99 | 493.36 | 492.54 | +4.54% | 0.68x | falling | rising | +0.0227 |
| **CAT** | 783.74 | 852.59 | 882.85 | 779.66 | +0.52% | 0.64x | falling | falling | -0.0126 |
| **DAL** | 79.79 | 85.18 | 81.61 | 74.73 | +6.78% | 0.64x | falling | falling | -0.2688 |
| **GOOGL** | 349.49 | 346.97 | 358.97 | 336.97 | +3.72% | 0.96x | falling | rising | +0.1595 |
| **META** | 665.71 | 602.56 | 603.89 | 623.49 | +6.77% | 0.91x | rising | falling | -0.0452 |
| **MSFT** | 505.72 | 455.97 | 431.78 | 431.42 | +17.22% | 0.02x | rising | rising | +0.0910 |
| **MU** | 924.29 | 927.58 | 889.84 | 625.57 | +47.75% | 0.61x | falling | rising | +0.0961 |
| **NVDA** | 210.88 | 212.91 | 211.35 | 197.61 | +6.71% | 0.02x | falling | falling | -0.3106 |
| **PLTR** | 173.31 | 154.81 | 144.70 | 151.58 | +14.34% | 0.64x | falling | falling | -0.0257 |
| **QQQ** | 709.24 | 710.34 | 709.74 | 660.66 | +7.35% | 0.02x | falling | falling | -0.0315 |
| **SCHD** | 34.34 | 33.84 | 32.93 | 31.32 | +9.66% | 1.04x | falling | falling | -0.1956 |
| **SMH** | 540.85 | 568.08 | 573.79 | 483.17 | +11.94% | 0.06x | rising | falling | -0.0030 |
| **SPY** | 760.75 | 758.94 | 748.18 | 714.69 | +6.44% | 0.03x | falling | falling | -0.1946 |
| **TSLA** | 358.97 | 353.81 | 380.11 | 398.63 | -9.95% | 0.64x | rising | rising | +0.0634 |
| **XLP** | 84.42 | 84.98 | 84.47 | 83.49 | +1.12% | 0.09x | falling | falling | -0.2685 |

## Validation vs Twelve Data's own OBV / AD endpoints

Absolute levels are expected to differ (both are cumulative from an arbitrary
start). Only DIRECTION must agree. A mismatch means something is wrong.

- **AAPL** — ✅ pass
  - `obv`: ours **rising** vs theirs **rising**
  - `ad`: ours **rising** vs theirs **rising**
- **QQQ** — ✅ pass
  - `obv`: ours **falling** vs theirs **falling**
  - `ad`: ours **falling** vs theirs **falling**

---

_Automated market-data snapshot. Public market data only —
this repository contains no holdings, positions or personal information._
