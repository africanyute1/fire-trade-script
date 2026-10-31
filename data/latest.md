# Market data snapshot

**Generated:** 2026-10-31T01:32:49+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 24 / 24

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 344.63 | 333.04 | 321.45 | 296.56 | +16.21% | 1.39x | rising | falling | -0.0602 |
| **AMD** | 504.80 | 548.29 | 529.05 | 410.49 | +22.98% | 1.63x 🔺 | falling | rising | +0.0637 |
| **AMZN** | 240.35 | 254.28 | 251.80 | 243.40 | -1.25% | 2.36x 🔺 | falling | rising | +0.0959 |
| **BLK** | 1,147.54 | 1,103.80 | 1,084.27 | 1,063.65 | +7.89% | 0.94x | rising | rising | +0.0478 |
| **BRK.B** | 542.49 | 515.11 | 507.63 | 495.74 | +9.43% | 0.99x | rising | rising | +0.0363 |
| **CAT** | 622.75 | 783.30 | 844.71 | 809.91 | -23.11% | 1.70x 🔺 | falling | falling | -0.0878 |
| **GOOGL** | 279.84 | 339.07 | 345.54 | 340.66 | -17.85% | 2.16x 🔺 | falling | falling | -0.1433 |
| **INTC** | 65.76 | 101.11 | 104.81 | 86.86 | -24.30% | 3.97x 🔺 | falling | falling | -0.1234 |
| **META** | 614.99 | 669.98 | 631.70 | 632.10 | -2.71% | 1.25x | falling | falling | -0.2496 |
| **MSFT** | 521.91 | 512.91 | 465.52 | 437.93 | +19.18% | 1.15x | falling | rising | +0.0058 |
| **MU** | 884.74 | 978.71 | 970.90 | 746.83 | +18.47% | 0.85x | falling | falling | -0.0613 |
| **NVDA** | 204.64 | 221.75 | 214.52 | 204.38 | +0.12% | 1.35x | falling | falling | -0.1424 |
| **O** | 56.93 | 57.50 | 60.34 | 61.63 | -7.63% | 1.49x | rising | rising | +0.0684 |
| **PLTR** | 184.11 | 186.90 | 162.42 | 153.57 | +19.89% | 0.79x | falling | rising | +0.0610 |
| **QQQ** | 690.49 | 725.00 | 719.02 | 679.52 | +1.61% | 2.20x 🔺 | falling | falling | -0.0207 |
| **ROKU** | 155.12 | 155.15 | 149.22 | 127.73 | +21.45% | 1.13x | rising | rising | +0.1644 |
| **SCHD** | 35.78 | 34.13 | 33.57 | 32.35 | +10.60% | 1.23x | rising | rising | +0.2747 |
| **SMH** | 522.49 | 572.62 | 581.06 | 519.50 | +0.58% | 1.84x 🔺 | falling | falling | -0.0764 |
| **SPY** | 755.72 | 767.49 | 759.22 | 728.85 | +3.69% | 1.67x 🔺 | falling | rising | +0.0460 |
| **TSLA** | 399.81 | 369.60 | 367.92 | 385.30 | +3.77% | 1.05x | falling | rising | +0.1316 |
| **UNH** | 406.97 | 390.20 | 402.17 | 362.76 | +12.19% | 0.80x | falling | falling | -0.0583 |
| **VNQ** | 93.94 | 93.18 | 95.70 | 94.61 | -0.70% | 1.36x | rising | rising | +0.0340 |
| **XLK** | 179.51 | 189.69 | 186.30 | 169.54 | +5.88% | 2.15x 🔺 | falling | rising | +0.0336 |
| **XLU** | 43.43 | 41.75 | 43.30 | 44.30 | -1.97% | 1.28x | rising | rising | +0.2592 |

## Validation vs Twelve Data's own OBV / AD endpoints

Absolute levels are expected to differ (both are cumulative from an arbitrary
start). Only DIRECTION must agree. A mismatch means something is wrong.

- **AAPL** — ✅ pass
  - `obv`: ours **rising** vs theirs **rising**
  - `ad`: ours **falling** vs theirs **falling**
- **QQQ** — ✅ pass
  - `obv`: ours **falling** vs theirs **falling**
  - `ad`: ours **falling** vs theirs **falling**

---

_Automated market-data snapshot. Public market data only —
this repository contains no holdings, positions or personal information._
