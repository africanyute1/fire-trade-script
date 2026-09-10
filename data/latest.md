# Market data snapshot

**Generated:** 2026-09-10T01:23:46+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 18 / 18

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 315.34 | 316.47 | 304.17 | 284.35 | +10.90% | 1.25x | falling | rising | +0.0378 |
| **AMD** | 521.10 | 498.59 | 471.47 | 343.86 | +51.54% | 0.71x | rising | rising | +0.0918 |
| **AMZN** | 252.40 | 254.68 | 255.31 | 239.44 | +5.41% | 0.69x | falling | falling | -0.0502 |
| **AVGO** | 364.38 | 383.57 | 397.51 | 370.02 | -1.53% | 1.00x | falling | falling | -0.0340 |
| **BLK** | 1,072.03 | 1,097.12 | 1,070.20 | 1,059.93 | +1.14% | 0.67x | falling | falling | -0.2108 |
| **BRK.B** | 506.72 | 503.50 | 492.19 | 492.45 | +2.90% | 0.70x | falling | falling | -0.1233 |
| **CAT** | 815.56 | 864.84 | 882.71 | 775.91 | +5.11% | 0.59x | falling | falling | -0.0907 |
| **DAL** | 78.75 | 86.01 | 81.36 | 74.41 | +5.83% | 0.66x | falling | falling | -0.3722 |
| **GOOGL** | 330.65 | 348.13 | 358.88 | 336.40 | -1.71% | 1.09x | falling | rising | +0.0612 |
| **META** | 653.69 | 598.58 | 604.60 | 622.69 | +4.98% | 2.00x 🔺 | rising | falling | -0.0322 |
| **MSFT** | 491.65 | 449.05 | 429.50 | 431.07 | +14.05% | 0.35x | rising | falling | -0.0117 |
| **MU** | 1,027.77 | 933.29 | 874.59 | 614.35 | +67.29% | 0.52x | rising | rising | +0.1137 |
| **NVDA** | 223.67 | 211.80 | 210.91 | 197.09 | +13.49% | 0.54x | falling | falling | -0.2465 |
| **PLTR** | 169.53 | 152.11 | 144.01 | 151.41 | +11.97% | 0.49x | falling | falling | -0.0470 |
| **QQQ** | 716.31 | 711.17 | 707.82 | 658.90 | +8.71% | 0.65x | falling | falling | -0.0011 |
| **SPY** | 762.40 | 758.02 | 746.58 | 713.18 | +6.90% | 0.66x | falling | falling | -0.1556 |
| **TSLA** | 367.81 | 356.84 | 381.03 | 399.21 | -7.87% | 0.70x | rising | rising | +0.0861 |
| **XLP** | 83.05 | 84.99 | 84.43 | 83.39 | -0.41% | 1.09x | falling | falling | -0.1570 |

## Validation vs Twelve Data's own OBV / AD endpoints

Absolute levels are expected to differ (both are cumulative from an arbitrary
start). Only DIRECTION must agree. A mismatch means something is wrong.

- **AAPL** — ✅ pass
  - `obv`: ours **falling** vs theirs **falling**
  - `ad`: ours **rising** vs theirs **rising**
- **QQQ** — ✅ pass
  - `obv`: ours **falling** vs theirs **falling**
  - `ad`: ours **falling** vs theirs **falling**

---

_Automated market-data snapshot. Public market data only —
this repository contains no holdings, positions or personal information._
