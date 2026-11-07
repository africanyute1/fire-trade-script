# Market data snapshot

**Generated:** 2026-11-07T15:35:14+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 24 / 24

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 342.37 | 336.01 | 323.77 | 298.81 | +14.58% | 0.89x | falling | falling | -0.0767 |
| **AMD** | 449.04 | 546.81 | 526.91 | 415.98 | +7.95% | 1.82x 🔺 | falling | falling | -0.1690 |
| **AMZN** | 259.30 | 253.95 | 252.52 | 243.94 | +6.30% | 0.93x | falling | falling | -0.0624 |
| **BLK** | 1,178.87 | 1,104.92 | 1,091.75 | 1,064.68 | +10.73% | 0.75x | rising | falling | -0.0481 |
| **BRK.B** | 570.89 | 521.56 | 511.49 | 497.72 | +14.70% | 1.18x | rising | rising | +0.0186 |
| **CAT** | 558.63 | 760.34 | 828.68 | 808.53 | -30.91% | 1.53x 🔺 | falling | falling | -0.2109 |
| **GOOGL** | 284.78 | 332.93 | 341.52 | 339.51 | -16.12% | 1.17x | falling | falling | -0.2688 |
| **INTC** | 56.28 | 97.95 | 101.75 | 87.04 | -35.34% | 1.49x | falling | falling | -0.1753 |
| **META** | 610.15 | 674.92 | 633.43 | 631.94 | -3.45% | 0.77x | falling | falling | -0.2845 |
| **MSFT** | 530.61 | 516.65 | 472.30 | 439.85 | +20.64% | 0.87x | falling | rising | +0.0024 |
| **MU** | 690.00 | 961.64 | 959.42 | 756.73 | -8.82% | 1.25x | falling | falling | -0.2404 |
| **NVDA** | 186.64 | 219.81 | 213.99 | 204.67 | -8.81% | 1.44x | falling | falling | -0.3345 |
| **O** | 59.04 | 57.10 | 60.15 | 61.56 | -4.10% | 0.88x | rising | rising | +0.1128 |
| **PLTR** | 160.38 | 185.88 | 164.26 | 153.53 | +4.46% | 0.71x | falling | falling | -0.0212 |
| **QQQ** | 656.10 | 720.97 | 716.58 | 680.89 | -3.64% | 1.79x 🔺 | falling | falling | -0.2865 |
| **ROKU** | 160.52 | 155.33 | 150.62 | 129.11 | +24.33% | 3.64x 🔺 | rising | rising | +0.0308 |
| **SCHD** | 35.17 | 34.19 | 33.73 | 32.52 | +8.16% | 1.24x | rising | rising | +0.1715 |
| **SMH** | 463.96 | 565.64 | 574.86 | 521.76 | -11.08% | 1.75x 🔺 | falling | falling | -0.2452 |
| **SPY** | 735.29 | 765.68 | 759.53 | 730.38 | +0.67% | 1.27x | falling | falling | -0.2589 |
| **TSLA** | 358.22 | 372.14 | 366.78 | 383.87 | -6.68% | 0.93x | falling | rising | +0.0033 |
| **UNH** | 394.15 | 390.65 | 401.81 | 364.23 | +8.21% | 1.09x | falling | falling | -0.0236 |
| **VNQ** | 95.73 | 92.92 | 95.60 | 94.72 | +1.06% | 0.98x | rising | rising | +0.0792 |
| **XLK** | 164.74 | 188.45 | 185.61 | 170.20 | -3.21% | 2.22x 🔺 | falling | falling | -0.2339 |
| **XLU** | 43.13 | 41.77 | 43.25 | 44.31 | -2.67% | 1.11x | rising | rising | +0.1338 |

## Validation vs Twelve Data's own OBV / AD endpoints

Absolute levels are expected to differ (both are cumulative from an arbitrary
start). Only DIRECTION must agree. A mismatch means something is wrong.

- **AAPL** — ✅ pass
  - `obv`: ours **falling** vs theirs **falling**
  - `ad`: ours **falling** vs theirs **falling**
- **QQQ** — ✅ pass
  - `obv`: ours **falling** vs theirs **falling**
  - `ad`: ours **falling** vs theirs **falling**

---

_Automated market-data snapshot. Public market data only —
this repository contains no holdings, positions or personal information._
