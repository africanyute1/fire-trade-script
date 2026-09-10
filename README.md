# fire-trade-script

Automated market-data feed for a weekly/quarterly technical trading review.

A GitHub Actions job fetches daily OHLCV from the [Twelve Data](https://twelvedata.com) API, computes volume-flow indicators that free websites do not publish, and commits the results to `data/`.

**👉 New here? Start with [SETUP.md](SETUP.md).**

---

## Why this exists

The reporting agent runs in a cloud sandbox whose egress policy blocks `api.twelvedata.com` — verified 2026-09-10, every endpoint returned `403 Forbidden` at the proxy before any request was sent. GitHub Actions runners have no such restriction, and the sandbox *can* reach `raw.githubusercontent.com`.

So GitHub acts as the bridge: the Action holds the credential and does the fetching; the report reads a committed JSON file over plain HTTPS with no credential at all.

A useful side effect — the API key never enters the reporting session. It lives only in GitHub's encrypted secret store.

## What it computes

Three indicators that no free website publishes (13 providers checked on 2026-09-09; none returned a numeric value for any of them):

| Indicator | Formula | Note |
|---|---|---|
| **OBV** | Running total: `+volume` on an up close, `−volume` on a down close | Cumulative from an arbitrary start — **level is meaningless, use direction only** |
| **A/D line** | Cumulative sum of `((C−L)−(H−C))/(H−L) × V` | Same caveat |
| **CMF(20)** | `Σ MFV(20) ÷ Σ Volume(20)` | Bounded ~−1..+1 — **the only one comparable across tickers** |

Plus 20/50/100/200-day moving averages and 5/20/50/100-day average volumes. The **100-day average volume** is the 20-week volume baseline the weekly checklist needs, and no free source publishes it.

## Layout

```
.github/workflows/fetch-market-data.yml   scheduled job
config/tickers.json                       ticker universe + tuning
scripts/fetch_market_data.py              fetch + compute (stdlib only)
data/latest.json                          machine-readable output
data/latest.md                            human-readable summary
data/history/YYYY-MM-DD.json              dated archive
```

No dependencies. Python 3.11 standard library only.

## Running locally

```bash
python3 scripts/fetch_market_data.py --dry-run          # validate config, no API calls
TWELVEDATA_API_KEY=xxxx python3 scripts/fetch_market_data.py
DEBUG=1 TWELVEDATA_API_KEY=xxxx python3 scripts/fetch_market_data.py   # verbose
```

## Verification

The indicator maths was checked against independently published values (2026-09-09):

| Metric | Computed | Published | Diff |
|---|---|---|---|
| AAPL 50-day SMA | 316.47 | 316.47 | 0.00% |
| AAPL 20-day avg volume | 40,443,806 | 40,443,806 | 0.00% |
| QQQ 50-day SMA | 711.17 | 711.09 | 0.01% |

Each run also cross-checks its own OBV and A/D **direction** against Twelve Data's own endpoints for a sample of tickers. Absolute values are expected to differ; a direction mismatch is flagged as a failure.

## Rate limits

Twelve Data's free tier allows 8 credits/minute and 800/day. The script paces itself at ~7 calls/minute and uses roughly 20 credits per run, twice weekly.

## ⚠️ Repository contents

This repository is **public**, and deliberately contains **only public market data**.

It must never contain holdings, position sizes, account values, statements, or API keys. `.gitignore` blocks files matching those patterns, and the API key is supplied at runtime from an encrypted GitHub secret.

The ticker list in `config/tickers.json` is a watchlist, not a portfolio — it says nothing about what is owned or in what size.

---

*Automated technical/volume data collection. Not financial advice.*
