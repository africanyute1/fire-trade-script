# Setup guide — market data feed for the trading reports

**Time needed:** about 15 minutes
**Cost:** free
**What you end up with:** a robot that fetches market data every Friday night and Saturday morning, so your weekly report can read it.

---

## 🤔 What this actually does, in plain terms

Your weekly report runs in a cloud sandbox that **is not allowed** to reach the Twelve Data website. We tested it — every request came back `403 Forbidden`, blocked by a network policy before it even left the sandbox.

But that sandbox **can** reach GitHub. So GitHub becomes the middleman:

```
   Friday 22:00 UTC
   ┌──────────────────────────┐
   │  GitHub Actions robot    │   has full internet access
   │  key from GitHub Secrets │   🔐 encrypted, never visible
   └────────────┬─────────────┘
                │  asks Twelve Data for prices
                ▼
   ┌──────────────────────────┐
   │  This repo               │   data/latest.json
   └────────────┬─────────────┘
                │
   Saturday 12:00 UTC
                ▼
   ┌──────────────────────────┐
   │  Your weekly report      │   reads the file. No key needed.
   └──────────────────────────┘
```

---

## ⚠️ Do this first: get a NEW API key

The key you pasted into chat earlier should be replaced. It never actually reached Twelve Data — the connection was blocked before anything was sent — but it did land in a chat transcript, and a key in a transcript is a key you should retire.

1. Go to **[twelvedata.com](https://twelvedata.com)** → log in → **API Keys**
2. **Regenerate** / create a new key
3. Copy it. Don't paste it into chat, don't put it in a file in this repo — it goes straight into GitHub in Step 4.

---

## Step 1 — Put the files in your repo

Copy everything I sent into:

```
/Users/andrewthompson/Library/CloudStorage/OneDrive-Personal/_project/fire-trade-script
```

Your folder should look like this:

```
fire-trade-script/
├── .github/
│   └── workflows/
│       └── fetch-market-data.yml    ← the robot's instructions
├── config/
│   └── tickers.json                 ← your ticker list (edit freely)
├── scripts/
│   └── fetch_market_data.py         ← does the fetching + maths
├── data/                            ← the robot fills this in
├── .gitignore                       ← blocks secrets from being committed
├── README.md
└── SETUP.md                         ← this file
```

---

## Step 2 — Create the GitHub repository

1. Go to **[github.com/new](https://github.com/new)**
2. **Repository name:** `fire-trade-script`
3. **Visibility:** ✅ **Public**
4. Do **not** tick "Add a README" (you already have one)
5. Click **Create repository**

### 🔓 "Wait — public? Is that safe?"

Yes, **because of what goes in it.** This repo will contain only public market prices — the same numbers on Yahoo Finance. It contains:

| | |
|---|---|
| ✅ Stock prices and volumes | Public information |
| ✅ Calculated indicators | Maths on public information |
| ❌ Your holdings | **Never** — not in this repo |
| ❌ Your position sizes | **Never** |
| ❌ Your account values | **Never** |
| ❌ Your API key | **Never** — it lives in GitHub Secrets |

Public is what lets your report read the file **without needing a second password**. The `.gitignore` file actively blocks anything named like holdings, positions, portfolio, or `.env` from being committed by accident.

⚠️ **The one rule:** never put your actual holdings in this repo. The ticker list in `config/tickers.json` is fine — a list of companies you're *watching* reveals nothing about what you own or how much.

---

## Step 3 — Push the files

Open Terminal on your Mac:

```bash
cd "/Users/andrewthompson/Library/CloudStorage/OneDrive-Personal/_project/fire-trade-script"

git init
git add .
git commit -m "Add market data fetch script and workflow"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/fire-trade-script.git
git push -u origin main
```

🔁 Replace `YOUR-USERNAME` with your actual GitHub username.

---

## Step 4 — Add your API key as a secret 🔐

**This is the important one.**

1. In your repo on GitHub, click **Settings** (top row)
2. Left sidebar → **Secrets and variables** → **Actions**
3. Click the green **New repository secret** button
4. Fill in exactly:

   | Field | Value |
   |---|---|
   | **Name** | `TWELVEDATA_API_KEY` |
   | **Secret** | *paste your new key* |

5. Click **Add secret**

✅ Once saved, **nobody can read it back** — not you, not me, not anyone browsing the repo. GitHub encrypts it and only injects it into the running robot. If it's ever printed in a log, GitHub masks it as `***`.

---

## Step 5 — Test it 🧪

1. Go to the **Actions** tab in your repo
2. Click **Fetch market data** in the left sidebar
3. Click **Run workflow** ▾ → **Run workflow**
4. Wait ~4 minutes (it deliberately goes slowly to respect the free-tier rate limit)

### Reading the result

| What you see | Meaning |
|---|---|
| 🟢 Green check | Worked. Check `data/latest.md` in your repo. |
| 🔴 Red X | Click into it — the error message says what went wrong. |

Click the finished run to see a **summary table** of every ticker with its moving averages, volume ratio, OBV, A/D and CMF.

### If it fails

| Error | Fix |
|---|---|
| `TWELVEDATA_API_KEY secret is not set` | Step 4 didn't save. Check the name is spelled exactly. |
| `symbol not found` for **BRK.B** | Open `config/tickers.json`, change `"BRK.B": "BRK.B"` to `"BRK.B": "BRK/B"` under `symbol_overrides`, commit, re-run. |
| `API error 429` | Rate limit. It retries automatically; if it persists, raise `seconds_between_calls` in the config from `8.5` to `12`. |
| `Permission denied` on push | Settings → Actions → General → Workflow permissions → select **Read and write permissions**. |

---

## Step 6 — Send me the link 🔗

Once it's green, send me your repo URL. It looks like:

```
https://github.com/YOUR-USERNAME/fire-trade-script
```

I'll wire this into both scheduled tasks:

```
https://raw.githubusercontent.com/YOUR-USERNAME/fire-trade-script/main/data/latest.json
```

**Until you send that, nothing changes** — Saturday's report already works using the sources I set up. This only makes it sturdier.

---

## 🗓️ When it runs

| Schedule | UTC | Why |
|---|---|---|
| Friday | 22:00 | After the US market closes |
| Saturday | 09:00 | Backup, 3 hours before your report |
| Anytime | manual | The **Run workflow** button |

Running twice is deliberate. If Friday fails, Saturday still has time to succeed before your report needs the data.

---

## ✏️ Changing the tickers

Edit `config/tickers.json`, commit, push. **No code changes needed.**

```json
"watchlist": [
  "CAT", "GOOGL", "AMD", "META", "MU", "TSLA", "PLTR", "AVGO"
]
```

---

## 📊 What you get

`data/latest.json` — full detail for the report. `data/latest.md` — a table you can read.

| Item | Why it matters |
|---|---|
| **CMF (20-day)** | Almost no free source publishes this |
| **OBV direction** | Is volume confirming the price move? |
| **A/D direction** | Second opinion on the same question |
| **100-day average volume** | **Nothing** publishes this — it's your true 20-week volume baseline |
| **20/50/100/200-day MAs** | Trend at every timeframe |
| **Validation check** | Compares my maths against Twelve Data's own numbers |

### About that validation check

The script computes OBV and A/D itself, then asks Twelve Data for *their* versions and compares.

⚠️ The **numbers won't match** — and that's expected, not a bug. OBV and A/D are running totals that start from an arbitrary point, so different providers get different absolute values. **What must match is the direction.** If mine says "rising" and theirs says "falling," something is genuinely wrong and the summary flags it.

---

## 💵 Cost

Free. About 20 API calls per run, twice a week — roughly **40 of your 800 daily allowance**. You will not come close to the limit.
