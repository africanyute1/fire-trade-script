# Market data snapshot

**Generated:** 2026-10-17T12:51:41+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 24 / 24

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 343.46 | 325.70 | 317.72 | 292.46 | +17.44% | 1.19x | rising | falling | -0.1223 |
| **AMD** | 528.75 | 537.14 | 525.73 | 394.25 | +34.12% | 0.89x | falling | rising | +0.2043 |
| **AMZN** | 250.00 | 257.08 | 252.27 | 242.73 | +3.00% | 0.92x | rising | falling | -0.0472 |
| **BLK** | 1,134.38 | 1,106.41 | 1,072.42 | 1,061.17 | +6.90% | 1.68x 🔺 | rising | rising | +0.0483 |
| **BRK.B** | 532.02 | 508.51 | 501.37 | 493.56 | +7.79% | 0.88x | rising | rising | +0.0423 |
| **CAT** | 730.76 | 812.76 | 865.50 | 805.74 | -9.31% | 0.97x | falling | rising | +0.0315 |
| **GOOGL** | 340.59 | 344.58 | 350.89 | 340.90 | -0.09% | 0.96x | rising | falling | -0.1715 |
| **INTC** | 89.85 | 103.17 | 107.11 | 84.56 | +6.26% | 1.08x | falling | falling | -0.0522 |
| **META** | 709.33 | 655.24 | 627.93 | 631.98 | +12.24% | 1.06x | rising | falling | -0.0570 |
| **MSFT** | 529.05 | 505.53 | 455.40 | 435.25 | +21.55% | 0.76x | rising | falling | -0.0374 |
| **MU** | 878.84 | 983.12 | 977.54 | 717.84 | +22.43% | 0.77x | falling | falling | -0.0128 |
| **NVDA** | 214.13 | 223.08 | 214.46 | 202.97 | +5.50% | 0.92x | rising | falling | -0.2243 |
| **O** | 56.08 | 58.70 | 60.74 | 61.71 | -9.12% | 1.02x | falling | falling | -0.0122 |
| **PLTR** | 186.03 | 182.57 | 157.19 | 152.65 | +21.87% | 0.91x | rising | rising | +0.0476 |
| **QQQ** | 709.80 | 726.77 | 720.73 | 674.91 | +5.17% | 1.70x 🔺 | falling | rising | +0.0555 |
| **ROKU** | 154.54 | 154.73 | 146.16 | 125.40 | +23.24% | 0.50x | falling | rising | +0.0616 |
| **SCHD** | 34.35 | 34.00 | 33.30 | 32.01 | +7.33% | 1.13x | rising | falling | -0.0407 |
| **SMH** | 539.79 | 579.03 | 587.11 | 511.35 | +5.56% | 1.90x 🔺 | falling | rising | +0.0102 |
| **SPY** | 763.25 | 768.50 | 757.62 | 725.01 | +5.27% | 1.34x | falling | falling | -0.0115 |
| **TSLA** | 354.72 | 359.46 | 371.07 | 387.99 | -8.58% | 1.55x 🔺 | falling | falling | -0.0668 |
| **UNH** | 401.43 | 387.30 | 399.82 | 359.10 | +11.79% | 1.43x | falling | rising | +0.0027 |
| **VNQ** | 91.76 | 94.27 | 96.03 | 94.44 | -2.84% | 1.28x | falling | falling | -0.1457 |
| **XLK** | 183.47 | 189.93 | 186.60 | 167.51 | +9.53% | 1.61x 🔺 | falling | rising | +0.0659 |
| **XLU** | 42.21 | 42.02 | 43.46 | 44.31 | -4.74% | 1.36x | rising | rising | +0.1452 |

## Validation vs Twelve Data's own OBV / AD endpoints

Absolute levels are expected to differ (both are cumulative from an arbitrary
start). Only DIRECTION must agree. A mismatch means something is wrong.

- **AAPL** — ✅ pass
  - `obv`: ours **rising** vs theirs **rising**
  - `ad`: ours **falling** vs theirs **falling**
- **QQQ** — ✅ pass
  - `obv`: ours **falling** vs theirs **falling**
  - `ad`: ours **rising** vs theirs **rising**

---

_Automated market-data snapshot. Public market data only —
this repository contains no holdings, positions or personal information._
