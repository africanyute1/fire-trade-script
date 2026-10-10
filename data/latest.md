# Market data snapshot

**Generated:** 2026-10-10T15:10:46+00:00  
**Source:** Twelve Data API via GitHub Actions  
**Tickers OK:** 20 / 20

| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |
|---|---|---|---|---|---|---|---|---|---|
| **AAPL** | 336.64 | 322.39 | 315.84 | 290.74 | +15.79% | 0.75x | rising | rising | +0.0746 |
| **AMD** | 608.10 | 528.92 | 519.94 | 385.32 | +57.82% | 0.53x | rising | rising | +0.2911 |
| **AMZN** | 262.43 | 259.10 | 252.74 | 242.15 | +8.37% | 0.79x | rising | rising | +0.0086 |
| **AVGO** | 361.54 | 371.87 | 383.81 | 368.28 | -1.83% | 0.66x | rising | falling | -0.1289 |
| **BLK** | 1,082.39 | 1,109.05 | 1,070.65 | 1,060.95 | +2.02% | 0.55x | falling | rising | +0.1559 |
| **BRK.B** | 515.62 | 507.77 | 499.26 | 492.97 | +4.59% | 0.93x | rising | rising | +0.0203 |
| **CAT** | 800.47 | 822.00 | 871.49 | 801.33 | -0.11% | 0.62x | rising | rising | +0.0983 |
| **GOOGL** | 351.66 | 346.25 | 352.81 | 340.03 | +3.42% | 0.58x | rising | falling | -0.1018 |
| **INTC** | 104.70 | 103.08 | 108.15 | 83.03 | +26.09% | 0.66x | falling | falling | -0.0452 |
| **META** | 718.67 | 639.73 | 621.42 | 630.13 | +14.05% | 0.67x | rising | falling | -0.0585 |
| **MSFT** | 535.07 | 500.45 | 449.45 | 434.00 | +23.29% | 0.56x | rising | falling | -0.0176 |
| **MU** | 1,029.00 | 976.19 | 969.27 | 701.68 | +46.65% | 0.49x | rising | rising | +0.0455 |
| **NVDA** | 229.28 | 222.08 | 214.32 | 202.15 | +13.42% | 0.62x | rising | falling | -0.1387 |
| **PLTR** | 209.05 | 176.98 | 153.97 | 152.33 | +37.23% | 1.02x | rising | rising | +0.2681 |
| **QQQ** | 751.27 | 724.52 | 719.94 | 672.18 | +11.77% | 0.54x | rising | rising | +0.1772 |
| **SCHD** | 33.04 | 33.98 | 33.23 | 31.85 | +3.73% | 0.81x | falling | falling | -0.1593 |
| **SMH** | 603.33 | 578.24 | 587.24 | 506.24 | +19.18% | 0.58x | rising | rising | +0.0742 |
| **SPY** | 778.57 | 767.57 | 756.15 | 722.93 | +7.70% | 0.47x | falling | rising | +0.0604 |
| **TSLA** | 382.70 | 354.75 | 373.68 | 390.60 | -2.02% | 0.96x | rising | falling | -0.1380 |
| **UNH** | 379.30 | 389.18 | 399.42 | 357.53 | +6.09% | 1.35x | falling | falling | -0.0031 |

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
