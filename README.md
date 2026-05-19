# 📈 Stock Price Predictor

A machine learning project that uses **Linear Regression** to predict future stock prices based on historical closing data fetched from Yahoo Finance.

---

## 🚀 Features

- Fetches real-time historical stock data using `yfinance`
- Trains a Linear Regression model on closing prices
- Predicts stock prices for the next **500 days**
- Visualizes historical vs predicted prices with `matplotlib`
- Works with **any stock symbol** (e.g., AAPL, TSLA, GOOGL)

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `yfinance` | Download historical stock data |
| `pandas` | Data manipulation |
| `numpy` | Numerical operations |
| `scikit-learn` | Linear Regression model |
| `matplotlib` | Plotting charts |

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/stock-price-predictor.git
   cd stock-price-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

Run the script:
```bash
python stock_prediction.py
```

When prompted, enter a stock symbol:
```
Enter the stock symbol (e.g., AAPL for Apple): AAPL
```

The program will:
- Download historical data from **2000 to present**
- Train and evaluate the model
- Display the **R² score**
- Show a plot of historical + predicted prices

---

## 📊 Example Output

```
Model R-squared: 0.9994
```

The chart will show:
- 🟡 **Yellow line** — Historical closing prices
- ⚫ **Black line** — Predicted prices for the next 500 days

---

## 📁 Project Structure

```
stock-price-predictor/
├── stock_prediction.py   # Main script
├── requirements.txt      # Python dependencies
├── .gitignore            # Files to ignore in Git
└── README.md             # Project documentation
```

---

## ⚠️ Disclaimer

> This project is for **educational purposes only**.  
> Stock price predictions from this model should **not** be used for real financial decisions.  
> Linear Regression is a simple model and does not account for market volatility, news events, or economic factors.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
