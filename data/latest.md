# Market data snapshot

**Generated:** 2026-11-14T02:15:09+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 24 / 24

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 356.27 | 339.04 | 326.65 | 301.25 | +18.26% | 0.80x | falling | rising | +0.0120 |
| **AMD** | 534.06 | 554.55 | 527.46 | 423.12 | +26.22% | 1.88x 🔺 | rising | falling | -0.0551 |
| **AMZN** | 266.66 | 254.81 | 254.07 | 244.60 | +9.02% | 0.70x | rising | falling | -0.0985 |
| **BLK** | 1,222.91 | 1,113.34 | 1,101.20 | 1,067.15 | +14.60% | 0.62x | rising | falling | -0.0177 |
| **BRK.B** | 592.94 | 529.66 | 516.22 | 500.43 | +18.49% | 1.04x | rising | rising | +0.0444 |
| **CAT** | 600.20 | 740.77 | 809.16 | 807.43 | -25.67% | 0.74x | falling | falling | -0.0922 |
| **GOOGL** | 295.77 | 328.19 | 338.43 | 338.48 | -12.62% | 1.00x | falling | falling | -0.2668 |
| **INTC** | 59.66 | 94.97 | 98.16 | 87.40 | -31.74% | 0.88x | falling | falling | -0.1277 |
| **META** | 641.69 | 679.81 | 636.91 | 630.77 | +1.73% | 0.75x | falling | falling | -0.3000 |
| **MSFT** | 523.88 | 519.00 | 480.12 | 441.42 | +18.68% | 0.85x | falling | rising | +0.0370 |
| **MU** | 778.31 | 943.78 | 943.00 | 765.61 | +1.66% | 0.81x | falling | falling | -0.1449 |
| **NVDA** | 162.85 | 214.65 | 212.26 | 204.19 | -20.25% | 2.59x 🔺 | falling | falling | -0.0066 |
| **O** | 58.82 | 56.88 | 60.07 | 61.53 | -4.41% | 0.87x | falling | rising | +0.0370 |
| **PLTR** | 167.99 | 184.79 | 166.67 | 153.72 | +9.28% | 0.46x | falling | rising | +0.0803 |
| **QQQ** | 679.89 | 717.87 | 714.45 | 682.24 | -0.34% | 1.06x | falling | falling | -0.2020 |
| **ROKU** | 160.52 | 155.39 | 150.86 | 129.38 | +24.07% | 0.00x | rising | rising | +0.0356 |
| **SCHD** | 36.10 | 34.29 | 33.93 | 32.68 | +10.46% | 1.61x 🔺 | rising | rising | +0.2922 |
| **SMH** | 486.75 | 559.80 | 567.58 | 523.89 | -7.09% | 1.26x | falling | falling | -0.1274 |
| **SPY** | 754.25 | 764.43 | 760.28 | 731.92 | +3.05% | 2.31x 🔺 | falling | falling | -0.1539 |
| **TSLA** | 390.22 | 374.74 | 366.55 | 382.73 | +1.96% | 0.83x | rising | rising | +0.0915 |
| **UNH** | 407.46 | 391.43 | 401.77 | 366.44 | +11.20% | 0.63x | rising | rising | +0.1357 |
| **VNQ** | 96.47 | 92.96 | 95.62 | 94.89 | +1.67% | 0.63x | rising | rising | +0.1264 |
| **XLK** | 170.25 | 187.10 | 184.83 | 170.82 | -0.33% | 1.03x | falling | falling | -0.1504 |
| **XLU** | 44.04 | 41.89 | 43.19 | 44.33 | -0.65% | 0.59x | rising | rising | +0.0735 |

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
