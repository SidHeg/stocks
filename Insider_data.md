# Stock Trading Data Sources
### Tracking Institutions, Insiders, Politicians

---

## 1️⃣ Institutional Investors (Funds, Hedge Funds)

### 📌 13F Filings
- **Filed with:** U.S. Securities and Exchange Commission (SEC)
- **Shows:** Long equity holdings of managers with $100M+ AUM
- **Frequency:** Quarterly (up to 45-day lag)
- **Use Case:** Idea generation, position sizing trends

**Sources:**
- SEC EDGAR
- WhaleWisdom
- Dataroma

---

## 2️⃣ Activists / Large Shareholders (5%+ Ownership)

### 📌 Schedule 13D
- **Trigger:** Ownership exceeds 5%
- **Indicates:** Activist intent or influence
- **Signal Strength:** High

### 📌 Schedule 13G
- **Trigger:** Passive ownership >5%
- **Signal Strength:** Medium

**Source:**
- SEC EDGAR

---

## 3️⃣ Company Insiders (CEO, CFO, Directors)

### 📌 Form 4 (Most Important Insider Filing)
- **Shows:** Actual executed insider buys/sells
- **Deadline:** Within 2 business days
- **Strong Signal:** Open-market buying

**Sources:**
- SEC EDGAR
- OpenInsider
- InsiderMonkey

---

### 📌 Form 144
- **Shows:** Planned sale of restricted/control shares
- **Important:** Intention only (not confirmed sale)
- **Signal Strength:** Weak alone

**Source:**
- SEC EDGAR

---

## 4️⃣ Politicians (Congress Trading)

### 📌 STOCK Act Disclosures
- Required under the Stop Trading on Congressional Knowledge Act (2012)
- **Shows:** Reported trades by U.S. Congress members
- **Lag:** Can be weeks

**Sources:**
- House Clerk Financial Disclosures
- Senate Financial Disclosures
- Quiver Quantitative
- Capitol Trades

---

## 5️⃣ Short Sellers / Bearish Positioning

### 📌 Short Interest
- **Shows:** % of float sold short
- **Use:** Sentiment, squeeze potential

**Sources:**
- FINRA
- Nasdaq
- Ortex (paid)

---

### 📌 Institutional Put Positions (via 13F)
- Shows quarterly institutional put option holdings
- Useful for hedging sentiment analysis

---

## 6️⃣ Advanced Institutional Flow (Near Real-Time)

### 📌 Dark Pool Data
- Tracks off-exchange block trades
- Useful for accumulation/distribution signals

### 📌 Options Flow
- Detects unusual call/put activity
- Often used for short-term positioning

**Sources:**
- Unusual Whales
- CBOE Data

---

# 📊 Signal Strength Ranking (Most Useful → Least)

1. Insider Form 4 (Open-Market Buys)
2. Schedule 13D (Activist Entry)
3. Major 13F Position Changes
4. Dark Pool / Options Flow
5. Politician Trades
6. Form 144 Alone
