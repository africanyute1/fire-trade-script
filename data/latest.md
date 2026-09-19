# Market data snapshot

**Generated:** 2026-09-19T00:10:14+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 20 / 20

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 336.13 | 320.14 | 308.51 | 286.34 | +17.39% | 1.64x 🔺 | rising | rising | +0.1451 |
| **AMD** | 559.82 | 495.85 | 486.52 | 354.62 | +57.86% | 1.07x | rising | rising | +0.2527 |
| **AMZN** | 253.71 | 255.84 | 255.08 | 240.30 | +5.58% | 1.14x | falling | rising | +0.0774 |
| **AVGO** | 357.61 | 379.76 | 393.10 | 369.10 | -3.11% | 1.75x 🔺 | falling | falling | -0.0306 |
| **BLK** | 1,069.78 | 1,106.30 | 1,070.86 | 1,061.15 | +0.81% | 1.56x 🔺 | falling | falling | -0.0878 |
| **BRK.B** | 509.77 | 505.09 | 495.14 | 492.61 | +3.48% | 2.61x 🔺 | rising | rising | +0.1389 |
| **CAT** | 808.99 | 840.14 | 881.55 | 784.11 | +3.17% | 1.56x 🔺 | rising | rising | +0.0413 |
| **DAL** | 79.62 | 84.37 | 82.04 | 75.03 | +6.11% | 3.64x 🔺 | rising | falling | -0.1181 |
| **GOOGL** | 349.54 | 345.58 | 359.09 | 337.50 | +3.57% | 1.56x 🔺 | rising | rising | +0.0448 |
| **META** | 665.75 | 607.38 | 603.93 | 624.16 | +6.66% | 1.50x 🔺 | rising | rising | +0.0157 |
| **MSFT** | 493.78 | 464.68 | 434.59 | 431.60 | +14.41% | 1.12x | rising | rising | +0.0932 |
| **MU** | 1,015.80 | 927.26 | 908.40 | 640.15 | +58.68% | 0.79x | falling | rising | +0.1669 |
| **NVDA** | 222.27 | 214.27 | 211.76 | 198.38 | +12.04% | 1.32x | rising | falling | -0.1440 |
| **PLTR** | 177.64 | 158.26 | 145.90 | 151.75 | +17.06% | 0.98x | rising | rising | +0.1211 |
| **QQQ** | 721.45 | 709.95 | 711.87 | 662.60 | +8.88% | 1.20x | rising | rising | +0.1413 |
| **SCHD** | 33.68 | 33.97 | 33.04 | 31.45 | +7.11% | 1.03x | falling | falling | -0.1938 |
| **SMH** | 573.00 | 564.78 | 576.30 | 487.31 | +17.58% | 0.61x | rising | rising | +0.0767 |
| **SPY** | 761.69 | 759.73 | 750.05 | 716.28 | +6.34% | 1.33x | falling | rising | +0.0291 |
| **TSLA** | 364.27 | 350.25 | 379.40 | 397.33 | -8.32% | 1.18x | rising | falling | -0.0627 |
| **XLP** | 82.80 | 84.92 | 84.50 | 83.58 | -0.93% | 0.95x | falling | falling | -0.3284 |

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
