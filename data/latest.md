# Market data snapshot

**Generated:** 2026-10-24T13:15:22+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 24 / 24

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 347.73 | 329.47 | 319.37 | 294.41 | +18.11% | 0.80x | rising | falling | -0.0811 |
| **AMD** | 516.79 | 542.28 | 526.62 | 402.08 | +28.53% | 0.61x | falling | falling | -0.0468 |
| **AMZN** | 248.00 | 255.65 | 251.78 | 243.29 | +1.93% | 0.58x | falling | falling | -0.0474 |
| **BLK** | 1,118.25 | 1,104.37 | 1,076.97 | 1,062.14 | +5.28% | 1.17x | rising | falling | -0.0808 |
| **BRK.B** | 542.19 | 510.82 | 504.64 | 494.59 | +9.62% | 0.93x | rising | rising | +0.0907 |
| **CAT** | 687.00 | 799.74 | 856.83 | 808.62 | -15.04% | 1.02x | falling | falling | -0.0688 |
| **GOOGL** | 320.21 | 342.94 | 348.55 | 341.31 | -6.18% | 0.60x | falling | falling | -0.1860 |
| **INTC** | 86.96 | 102.11 | 105.86 | 85.81 | +1.34% | 0.65x | falling | falling | -0.2310 |
| **META** | 642.62 | 663.81 | 630.81 | 632.53 | +1.60% | 0.76x | falling | falling | -0.1246 |
| **MSFT** | 524.51 | 508.43 | 459.92 | 436.51 | +20.16% | 0.44x | rising | falling | -0.1212 |
| **MU** | 877.55 | 982.73 | 972.80 | 732.10 | +19.87% | 0.56x | falling | falling | -0.1207 |
| **NVDA** | 210.96 | 222.48 | 214.40 | 203.67 | +3.58% | 0.63x | falling | falling | -0.3084 |
| **O** | 56.89 | 58.08 | 60.51 | 61.69 | -7.77% | 1.00x | rising | rising | +0.0255 |
| **PLTR** | 196.75 | 184.75 | 159.55 | 153.15 | +28.47% | 0.51x | rising | rising | +0.0036 |
| **QQQ** | 704.40 | 725.81 | 719.51 | 677.30 | +4.00% | 0.76x | falling | falling | -0.1375 |
| **ROKU** | 158.58 | 155.29 | 147.56 | 126.57 | +25.29% | 0.94x | rising | rising | +0.2864 |
| **SCHD** | 35.27 | 34.06 | 33.42 | 32.18 | +9.60% | 1.00x | rising | rising | +0.1419 |
| **SMH** | 527.20 | 575.09 | 583.79 | 515.44 | +2.28% | 0.77x | falling | falling | -0.1856 |
| **SPY** | 759.97 | 767.81 | 758.15 | 727.01 | +4.53% | 0.70x | falling | falling | -0.0827 |
| **TSLA** | 372.22 | 363.77 | 368.24 | 386.35 | -3.66% | 0.87x | falling | rising | +0.0102 |
| **UNH** | 418.09 | 388.57 | 401.63 | 361.03 | +15.80% | 0.69x | falling | rising | +0.0020 |
| **VNQ** | 92.69 | 93.71 | 95.85 | 94.53 | -1.94% | 1.28x | falling | falling | -0.0658 |
| **XLK** | 183.23 | 189.64 | 186.29 | 168.50 | +8.74% | 0.80x | falling | falling | -0.0817 |
| **XLU** | 42.56 | 41.87 | 43.35 | 44.30 | -3.92% | 0.79x | rising | rising | +0.2225 |

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
