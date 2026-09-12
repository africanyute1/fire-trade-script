# Market data snapshot

**Generated:** 2026-09-12T12:47:20+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 18 / 18

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 332.27 | 317.97 | 305.32 | 284.95 | +16.61% | 0.97x | rising | rising | +0.1149 |
| **AMD** | 516.13 | 496.55 | 476.13 | 346.91 | +48.78% | 0.61x | rising | rising | +0.1515 |
| **AMZN** | 256.78 | 255.25 | 255.41 | 239.80 | +7.08% | 0.58x | falling | rising | +0.0724 |
| **AVGO** | 361.99 | 383.09 | 396.67 | 370.20 | -2.22% | 0.86x | falling | falling | -0.0517 |
| **BLK** | 1,079.65 | 1,101.13 | 1,070.62 | 1,060.60 | +1.80% | 0.70x | falling | falling | -0.2989 |
| **BRK.B** | 510.37 | 503.85 | 492.90 | 492.51 | +3.63% | 0.76x | falling | falling | -0.0417 |
| **CAT** | 818.57 | 856.18 | 883.02 | 778.54 | +5.14% | 0.62x | falling | falling | -0.0278 |
| **DAL** | 79.91 | 85.44 | 81.52 | 74.63 | +7.07% | 0.71x | falling | falling | -0.3263 |
| **GOOGL** | 338.50 | 347.18 | 358.80 | 336.81 | +0.50% | 0.82x | falling | rising | +0.0866 |
| **META** | 648.03 | 600.90 | 603.92 | 623.23 | +3.98% | 0.95x | rising | falling | -0.1003 |
| **MSFT** | 495.63 | 453.67 | 430.97 | 431.26 | +14.93% | 0.41x | rising | rising | +0.0667 |
| **MU** | 975.26 | 928.61 | 885.09 | 622.07 | +56.78% | 0.48x | falling | rising | +0.0775 |
| **NVDA** | 218.29 | 212.58 | 211.24 | 197.47 | +10.54% | 0.61x | falling | falling | -0.3183 |
| **PLTR** | 167.23 | 153.93 | 144.42 | 151.52 | +10.37% | 0.38x | falling | falling | -0.0979 |
| **QQQ** | 714.88 | 710.41 | 709.10 | 660.14 | +8.29% | 0.66x | falling | falling | -0.0343 |
| **SPY** | 764.29 | 758.62 | 747.61 | 714.23 | +7.01% | 0.94x | falling | falling | -0.2062 |
| **TSLA** | 365.44 | 354.50 | 380.39 | 398.93 | -8.39% | 0.66x | rising | rising | +0.0782 |
| **XLP** | 83.38 | 84.99 | 84.45 | 83.45 | -0.08% | 0.97x | falling | falling | -0.2533 |

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
