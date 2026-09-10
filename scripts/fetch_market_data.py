#!/usr/bin/env python3
"""
fetch_market_data.py
====================
Pulls daily OHLCV from the Twelve Data API and computes the volume-flow
indicators that no free website publishes: OBV, Accumulation/Distribution
and Chaikin Money Flow -- plus the 100-day (20-week) moving average and
100-day average volume.

WHY THIS EXISTS
---------------
The weekly/quarterly trading reports run in a cloud sandbox whose network
policy blocks api.twelvedata.com (verified 2026-09-10: every endpoint
returned 403 at the egress proxy). GitHub Actions runners have no such
restriction. So this script runs on GitHub, writes its results into the
repo, and the report reads the committed JSON over raw.githubusercontent.com.

The API key is read from the TWELVEDATA_API_KEY environment variable, which
GitHub Actions populates from an encrypted repository secret. The key is
never printed, never logged and never committed.

Standard library only -- no pip install, no dependency drift.

Usage:
    TWELVEDATA_API_KEY=xxxx python3 scripts/fetch_market_data.py
    TWELVEDATA_API_KEY=xxxx python3 scripts/fetch_market_data.py --dry-run
"""

import json
import os
import sys
import time
import argparse
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timezone

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(REPO_ROOT, "config", "tickers.json")
DATA_DIR = os.path.join(REPO_ROOT, "data")
HISTORY_DIR = os.path.join(DATA_DIR, "history")

API_BASE = "https://api.twelvedata.com"


# --------------------------------------------------------------------------
# Logging -- plain stderr, timestamped, never emits the API key
# --------------------------------------------------------------------------
def log(level, msg):
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}] {level:<5} {msg}", file=sys.stderr, flush=True)


def info(msg):
    log("INFO", msg)


def warn(msg):
    log("WARN", msg)


def error(msg):
    log("ERROR", msg)


def debug(msg):
    if os.environ.get("DEBUG"):
        log("DEBUG", msg)


# --------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------
def load_config():
    """Read config/tickers.json. Fails loudly -- a silent default would
    quietly fetch the wrong universe."""
    if not os.path.exists(CONFIG_PATH):
        error(f"Config not found at {CONFIG_PATH}")
        sys.exit(1)
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
            cfg = json.load(fh)
    except json.JSONDecodeError as e:
        error(f"config/tickers.json is not valid JSON: {e}")
        sys.exit(1)

    required = ["short_term_holdings", "roth_holdings", "watchlist", "settings"]
    missing = [k for k in required if k not in cfg]
    if missing:
        error(f"config/tickers.json missing required keys: {missing}")
        sys.exit(1)
    return cfg


def build_universe(cfg):
    """Union of all ticker lists, de-duplicated, order preserved."""
    seen, out = set(), []
    for key in ("short_term_holdings", "roth_holdings", "watchlist"):
        for t in cfg.get(key, []):
            if t not in seen:
                seen.add(t)
                out.append(t)
    bench = cfg.get("benchmark")
    if bench and bench not in seen:
        out.append(bench)
    return out


# --------------------------------------------------------------------------
# API layer
# --------------------------------------------------------------------------
class RateLimiter:
    """Twelve Data's free tier allows 8 credits/minute. One time_series call
    costs 1 credit. Sleeping between calls is simpler and more reliable than
    reacting to 429s after the fact."""

    def __init__(self, seconds_between):
        self.seconds_between = float(seconds_between)
        self._last = 0.0

    def wait(self):
        elapsed = time.time() - self._last
        remaining = self.seconds_between - elapsed
        if remaining > 0:
            debug(f"rate limit: sleeping {remaining:.1f}s")
            time.sleep(remaining)
        self._last = time.time()


def api_get(path, params, api_key, limiter, max_retries=3):
    """Call one Twelve Data endpoint.

    Returns (data_dict, None) on success or (None, reason_string) on failure.
    The API key is stripped from anything that could reach a log."""
    query = dict(params)
    query["apikey"] = api_key
    url = f"{API_BASE}{path}?{urllib.parse.urlencode(query)}"
    safe_url = url.replace(api_key, "***")

    for attempt in range(1, max_retries + 1):
        limiter.wait()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "fire-trade-script/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            try:
                body = e.read().decode("utf-8")
            except Exception:
                body = ""
            if e.code == 429:
                backoff = 20 * attempt
                warn(f"429 rate limited on {path} (attempt {attempt}/{max_retries}); backing off {backoff}s")
                time.sleep(backoff)
                continue
            return None, f"HTTP {e.code} on {safe_url}"
        except urllib.error.URLError as e:
            # This is what a blocked egress proxy looks like.
            warn(f"network error on {path} (attempt {attempt}/{max_retries}): {e.reason}")
            if attempt == max_retries:
                return None, f"network error: {e.reason}"
            time.sleep(5 * attempt)
            continue
        except Exception as e:
            return None, f"{type(e).__name__}: {e}"

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return None, f"non-JSON response: {body[:200]}"

        # Twelve Data signals errors in the body, not the HTTP status.
        if isinstance(data, dict) and data.get("status") == "error":
            code = data.get("code")
            message = data.get("message", "")
            if code == 429:
                backoff = 20 * attempt
                warn(f"API 429 on {path} (attempt {attempt}/{max_retries}); backing off {backoff}s")
                time.sleep(backoff)
                continue
            return None, f"API error {code}: {message[:200]}"

        return data, None

    return None, "exhausted retries"


def fetch_time_series(symbol, api_key, limiter, outputsize, max_retries):
    """Daily OHLCV, newest first from the API. Returned oldest-first."""
    data, err = api_get(
        "/time_series",
        {"symbol": symbol, "interval": "1day", "outputsize": str(outputsize), "order": "desc"},
        api_key, limiter, max_retries,
    )
    if err:
        return None, err

    values = data.get("values")
    if not values:
        return None, "response contained no 'values' array"

    bars = []
    for row in values:
        try:
            bars.append({
                "date": row["datetime"],
                "open": float(row["open"]),
                "high": float(row["high"]),
                "low": float(row["low"]),
                "close": float(row["close"]),
                "volume": int(float(row.get("volume") or 0)),
            })
        except (KeyError, TypeError, ValueError) as e:
            warn(f"{symbol}: skipping malformed bar {row!r} ({e})")
            continue

    if not bars:
        return None, "no parseable bars"

    bars.reverse()  # oldest first
    return bars, None


# --------------------------------------------------------------------------
# Indicator maths
# --------------------------------------------------------------------------
def money_flow_volume(bar):
    """MFV = ((C-L) - (H-C)) / (H-L) * V.  Guards a zero range."""
    rng = bar["high"] - bar["low"]
    if rng <= 0:
        return 0.0
    mfm = ((bar["close"] - bar["low"]) - (bar["high"] - bar["close"])) / rng
    return mfm * bar["volume"]


def compute_obv(bars):
    """On-Balance Volume. CUMULATIVE FROM AN ARBITRARY START -- the absolute
    level is meaningless and is NOT comparable across tickers or providers.
    Only the direction carries signal."""
    total = 0
    series = [0]
    for i in range(1, len(bars)):
        c, pc, v = bars[i]["close"], bars[i - 1]["close"], bars[i]["volume"]
        if c > pc:
            total += v
        elif c < pc:
            total -= v
        series.append(total)
    return series


def compute_ad(bars):
    """Accumulation/Distribution line. Same cumulative caveat as OBV."""
    total = 0.0
    series = []
    for bar in bars:
        total += money_flow_volume(bar)
        series.append(total)
    return series


def compute_cmf(bars, period=20):
    """Chaikin Money Flow. Bounded roughly -1..+1 and IS comparable
    across tickers -- the only one of the three that is."""
    if len(bars) < period:
        return None
    window = bars[-period:]
    vol_sum = sum(b["volume"] for b in window)
    if vol_sum <= 0:
        return None
    return sum(money_flow_volume(b) for b in window) / vol_sum


def sma(bars, period):
    if len(bars) < period:
        return None
    return sum(b["close"] for b in bars[-period:]) / period


def avg_volume(bars, period):
    if len(bars) < period:
        return None
    return sum(b["volume"] for b in bars[-period:]) / period


def direction(series, lookback):
    """Direction of a cumulative series over a lookback window."""
    if series is None or len(series) <= lookback:
        return {"label": "insufficient_data", "change": None}
    change = series[-1] - series[-1 - lookback]
    if change > 0:
        label = "rising"
    elif change < 0:
        label = "falling"
    else:
        label = "flat"
    return {"label": label, "change": round(change, 2), "lookback_days": lookback}


def pct_vs(price, level):
    if level is None or level == 0:
        return None
    return round((price - level) / level * 100, 2)


def analyse(symbol, bars, cmf_period):
    """Build the full indicator payload for one ticker."""
    last = bars[-1]
    price = last["close"]

    obv_series = compute_obv(bars)
    ad_series = compute_ad(bars)

    mas = {}
    for p in (20, 50, 100, 200):
        val = sma(bars, p)
        mas[f"sma_{p}"] = round(val, 4) if val is not None else None
        mas[f"price_vs_sma_{p}_pct"] = pct_vs(price, val)

    vols = {}
    for p in (5, 20, 50, 100):
        val = avg_volume(bars, p)
        vols[f"avg_volume_{p}"] = round(val) if val is not None else None

    # "Recent volume vs 20-week average" -- the 100-day average volume is the
    # 20-week proxy, and no free website publishes it.
    v100 = vols.get("avg_volume_100")
    vol_ratio_20w = round(last["volume"] / v100, 3) if v100 else None
    v20 = vols.get("avg_volume_20")
    vol_ratio_20d = round(last["volume"] / v20, 3) if v20 else None

    cmf_val = compute_cmf(bars, cmf_period)

    return {
        "symbol": symbol,
        "bars_used": len(bars),
        "oldest_bar": bars[0]["date"],
        "latest_bar": last["date"],
        "price": round(price, 4),
        "latest_volume": last["volume"],
        "moving_averages": mas,
        "average_volumes": vols,
        "volume_vs_20week_avg": vol_ratio_20w,
        "volume_vs_20day_avg": vol_ratio_20d,
        "volume_spike_1_5x": (vol_ratio_20w >= 1.5) if vol_ratio_20w is not None else None,
        "obv": {
            "note": "cumulative from arbitrary start; level is meaningless, use direction only",
            "latest_value": obv_series[-1] if obv_series else None,
            "direction_20d": direction(obv_series, 20),
            "direction_60d": direction(obv_series, 60),
            "direction_120d": direction(obv_series, 120),
        },
        "accumulation_distribution": {
            "note": "cumulative from arbitrary start; level is meaningless, use direction only",
            "latest_value": round(ad_series[-1], 2) if ad_series else None,
            "direction_20d": direction(ad_series, 20),
            "direction_60d": direction(ad_series, 60),
            "direction_120d": direction(ad_series, 120),
        },
        "cmf": {
            "period": cmf_period,
            "value": round(cmf_val, 6) if cmf_val is not None else None,
            "sign": (None if cmf_val is None else ("positive" if cmf_val > 0 else "negative")),
            "note": "bounded ~-1..+1; comparable across tickers",
        },
    }


# --------------------------------------------------------------------------
# Validation -- compare our own OBV/AD against Twelve Data's own endpoints
# --------------------------------------------------------------------------
def validate_against_api(symbol, our_result, api_key, limiter, max_retries):
    """Twelve Data publishes OBV and AD (not CMF). Their absolute levels will
    NOT match ours -- both are cumulative from an arbitrary start point, and
    they use a different start. What must agree is the DIRECTION.
    A direction mismatch means something is genuinely wrong."""
    out = {"symbol": symbol, "checks": [], "passed": None}

    for endpoint, our_key in (("obv", "obv"), ("ad", "accumulation_distribution")):
        data, err = api_get(
            f"/{endpoint}",
            {"symbol": symbol, "interval": "1day", "outputsize": "25"},
            api_key, limiter, max_retries,
        )
        if err:
            out["checks"].append({"indicator": endpoint, "status": "unavailable", "detail": err})
            continue

        values = data.get("values") or []
        if len(values) < 21:
            out["checks"].append({"indicator": endpoint, "status": "unavailable",
                                  "detail": f"only {len(values)} points returned"})
            continue

        try:
            newest = float(values[0][endpoint])
            older = float(values[20][endpoint])
        except (KeyError, ValueError, TypeError) as e:
            out["checks"].append({"indicator": endpoint, "status": "unavailable",
                                  "detail": f"unexpected payload shape: {e}"})
            continue

        their_dir = "rising" if newest > older else ("falling" if newest < older else "flat")
        our_dir = our_result[our_key]["direction_20d"]["label"]
        agree = (their_dir == our_dir)
        out["checks"].append({
            "indicator": endpoint,
            "status": "ok",
            "our_direction_20d": our_dir,
            "their_direction_20d": their_dir,
            "agree": agree,
        })

    usable = [c for c in out["checks"] if c["status"] == "ok"]
    out["passed"] = all(c["agree"] for c in usable) if usable else None
    return out


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------
def write_markdown_summary(payload, path):
    """A human-scannable companion to the JSON."""
    lines = []
    lines.append("# Market data snapshot")
    lines.append("")
    lines.append(f"**Generated:** {payload['generated_utc']}  ")
    lines.append(f"**Source:** Twelve Data API via GitHub Actions  ")
    lines.append(f"**Tickers OK:** {payload['summary']['succeeded']} / {payload['summary']['requested']}")
    lines.append("")

    if payload["summary"]["failed_symbols"]:
        lines.append(f"> ⚠️ **Failed:** {', '.join(payload['summary']['failed_symbols'])}")
        lines.append("")

    lines.append("| Ticker | Price | 50d MA | 100d MA | 200d MA | vs 200d | Vol vs 20wk | OBV 20d | A/D 20d | CMF(20) |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")

    for sym in sorted(payload["tickers"].keys()):
        t = payload["tickers"][sym]
        if t.get("error"):
            lines.append(f"| {sym} | ERROR | | | | | | | | |")
            continue
        ma = t["moving_averages"]

        def fmt(v, dp=2):
            return f"{v:,.{dp}f}" if isinstance(v, (int, float)) else "n/a"

        cmf_v = t["cmf"]["value"]
        cmf_txt = f"{cmf_v:+.4f}" if cmf_v is not None else "n/a"
        vr = t["volume_vs_20week_avg"]
        vr_txt = f"{vr:.2f}x" + (" 🔺" if (vr and vr >= 1.5) else "") if vr is not None else "n/a"
        v200 = ma.get("price_vs_sma_200_pct")

        lines.append(
            f"| **{sym}** | {fmt(t['price'])} | {fmt(ma.get('sma_50'))} | {fmt(ma.get('sma_100'))} | "
            f"{fmt(ma.get('sma_200'))} | {f'{v200:+.2f}%' if v200 is not None else 'n/a'} | {vr_txt} | "
            f"{t['obv']['direction_20d']['label']} | {t['accumulation_distribution']['direction_20d']['label']} | {cmf_txt} |"
        )

    lines.append("")
    lines.append("## Validation vs Twelve Data's own OBV / AD endpoints")
    lines.append("")
    lines.append("Absolute levels are expected to differ (both are cumulative from an arbitrary")
    lines.append("start). Only DIRECTION must agree. A mismatch means something is wrong.")
    lines.append("")
    if not payload["validation"]:
        lines.append("_No validation samples configured._")
    for v in payload["validation"]:
        mark = "✅ pass" if v["passed"] else ("❌ MISMATCH" if v["passed"] is False else "⚠️ unavailable")
        lines.append(f"- **{v['symbol']}** — {mark}")
        for c in v["checks"]:
            if c["status"] == "ok":
                lines.append(f"  - `{c['indicator']}`: ours **{c['our_direction_20d']}** vs theirs **{c['their_direction_20d']}**")
            else:
                lines.append(f"  - `{c['indicator']}`: {c['status']} — {c['detail']}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("_Automated market-data snapshot. Public market data only —")
    lines.append("this repository contains no holdings, positions or personal information._")
    lines.append("")

    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description="Fetch market data and compute volume-flow indicators.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Validate config and exit without calling the API.")
    args = parser.parse_args()

    cfg = load_config()
    settings = cfg["settings"]
    universe = build_universe(cfg)
    overrides = cfg.get("symbol_overrides", {})

    info(f"Universe: {len(universe)} tickers -> {', '.join(universe)}")

    if args.dry_run:
        info("Dry run requested; config is valid. Exiting without API calls.")
        return 0

    api_key = os.environ.get("TWELVEDATA_API_KEY", "").strip()
    if not api_key:
        error("TWELVEDATA_API_KEY is not set.")
        error("In GitHub Actions this comes from an encrypted repository secret.")
        error("Add it at: Settings -> Secrets and variables -> Actions -> New repository secret")
        return 2
    info(f"API key loaded (length {len(api_key)}, value never logged).")

    limiter = RateLimiter(settings.get("seconds_between_calls", 8.5))
    max_retries = int(settings.get("max_retries", 3))
    outputsize = int(settings.get("outputsize", 300))
    cmf_period = int(settings.get("cmf_period", 20))

    results, failures = {}, []

    for idx, symbol in enumerate(universe, start=1):
        api_symbol = overrides.get(symbol, symbol)
        info(f"[{idx}/{len(universe)}] fetching {symbol}" +
             (f" (as {api_symbol})" if api_symbol != symbol else ""))

        bars, err = fetch_time_series(api_symbol, api_key, limiter, outputsize, max_retries)
        if err:
            error(f"{symbol}: {err}")
            failures.append(symbol)
            results[symbol] = {"symbol": symbol, "error": err}
            continue

        try:
            results[symbol] = analyse(symbol, bars, cmf_period)
            info(f"{symbol}: OK ({len(bars)} bars, latest {bars[-1]['date']})")
        except Exception as e:
            error(f"{symbol}: indicator computation failed: {type(e).__name__}: {e}")
            failures.append(symbol)
            results[symbol] = {"symbol": symbol, "error": f"compute failed: {e}"}

    # Cross-check our maths against the vendor's own indicator endpoints.
    validation = []
    for symbol in cfg.get("validation_sample", []):
        if symbol in results and not results[symbol].get("error"):
            info(f"validating {symbol} against vendor OBV/AD endpoints")
            try:
                validation.append(
                    validate_against_api(overrides.get(symbol, symbol), results[symbol],
                                         api_key, limiter, max_retries)
                )
            except Exception as e:
                warn(f"validation for {symbol} failed: {type(e).__name__}: {e}")
        else:
            warn(f"skipping validation for {symbol}: no usable result")

    payload = {
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "Twelve Data API (api.twelvedata.com) via GitHub Actions",
        "schema_version": 1,
        "summary": {
            "requested": len(universe),
            "succeeded": len(universe) - len(failures),
            "failed": len(failures),
            "failed_symbols": failures,
        },
        "groups": {
            "short_term_holdings": cfg["short_term_holdings"],
            "roth_holdings": cfg["roth_holdings"],
            "watchlist": cfg["watchlist"],
            "benchmark": cfg.get("benchmark"),
        },
        "validation": validation,
        "tickers": results,
    }

    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(HISTORY_DIR, exist_ok=True)

    latest_json = os.path.join(DATA_DIR, "latest.json")
    with open(latest_json, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2)
    info(f"wrote {latest_json}")

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    archive = os.path.join(HISTORY_DIR, f"{stamp}.json")
    with open(archive, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2)
    info(f"wrote {archive}")

    latest_md = os.path.join(DATA_DIR, "latest.md")
    write_markdown_summary(payload, latest_md)
    info(f"wrote {latest_md}")

    info(f"DONE: {payload['summary']['succeeded']}/{payload['summary']['requested']} succeeded")

    # Fail the workflow only if EVERY ticker failed -- a couple of bad symbols
    # should not throw away an otherwise good run.
    if payload["summary"]["succeeded"] == 0:
        error("every ticker failed; failing the run so the problem is visible")
        return 1
    if failures:
        warn(f"partial success; failed symbols: {failures}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
