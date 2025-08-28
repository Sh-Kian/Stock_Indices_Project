Stock\_Indices\_Project/
│
├─ README.md

```markdown
# Stock Indices Project

This project demonstrates the calculation of **five important stock market indices** and **five financial ratios** using sample stock data. The goal is to help beginners understand how to calculate and visualize stock indices and financial ratios with Python.

---

## 📊 Market Indices
1. **Price Index** – Total market price index (sum of all stock prices).
2. **Equal Weight Index** – Average stock price regardless of company size.
3. **Volume Index** – Total traded volume in the market.
4. **Return Index** – Daily return percentage for each stock.
5. **Volatility Index** – Standard deviation of daily returns (market risk).

---

## 💹 Financial Ratios
1. **ROI (Return on Investment)** – Profitability compared to revenue.
2. **EPS (Earnings Per Share)** – Net income per outstanding share.
3. **P/E Ratio (Price-to-Earnings)** – Stock price compared to EPS.
4. **ROE (Return on Equity)** – Net income compared to equity.
5. **CAGR (Compound Annual Growth Rate)** – Long-term growth rate.

---

## 📁 Project Structure
```

Stock\_Indices\_Project/
│
├─ README.md
├─ requirements.txt
├─ data/
│    └─ market\_data.xlsx
├─ price\_index.py
├─ equal\_weight\_index.py
├─ volume\_index.py
├─ return\_index.py
├─ volatility\_index.py
├─ financial\_ratios.py
└─ plot\_indices.py

````

---

## ⚙️ How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
````

2. **Run individual scripts:**

   ```bash
   python price_index.py
   python equal_weight_index.py
   python volume_index.py
   python return_index.py
   python volatility_index.py
   python financial_ratios.py
   ```

3. **Plot all indices and ratios:**

   ```bash
   python plot_indices.py
   ```

---

## 📈 Sample Data

The dataset (`market_data.xlsx`) includes the following columns:

* **Stock** – Stock symbol
* **Price** – Closing price
* **Volume** – Daily traded volume
* **NetIncome** – Company net income
* **Revenue** – Company revenue
* **Equity** – Shareholders' equity
* **SharesOutstanding** – Number of outstanding shares
* **Years** – Period in years (used for CAGR)

Example data:

```
Stock, Price, Volume, NetIncome, Revenue, Equity, SharesOutstanding, Years
A, 100, 5000, 2000, 10000, 5000, 100, 3
B, 50, 7000, 1500, 8000, 4000, 50, 3
C, 200, 3000, 5000, 20000, 10000, 200, 3
```

---

## 🛠 Tools & Libraries

* **Python 3**
* **pandas** → data handling and calculations
* **matplotlib** → plotting charts

---

## 📜 License

This project is licensed under the **MIT License** – you are free to use, modify, and share it.

```
├─ requirements.txt
├─ data/
│    └─ market_data.csv
├─ price_index.py
├─ equal_weight_index.py
├─ volume_index.py
├─ return_index.py
├─ volatility_index.py
├─ financial_ratios.py
└─ plot_indices.py

```
