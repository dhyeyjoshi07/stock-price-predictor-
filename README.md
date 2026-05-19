# 📈 Stock Price Predictor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-ML Model-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/yfinance-Stock Data-00897B?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p align="center">
  A Python tool that uses <strong>Linear Regression</strong> and <strong>Moving Averages</strong> to forecast stock prices up to 500 days into the future — powered by Yahoo Finance data.
</p>

---

## 📌 Table of Contents

- [Features](#-features)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Usage](#-usage)
- [Output](#-output)
- [Limitations](#-limitations)
- [Disclaimer](#-disclaimer)
- [License](#-license)

---

## ✨ Features

- 🔍 Fetches historical stock data automatically via `yfinance`
- 📊 Computes **10-day** and **50-day** moving averages as model features
- 🤖 Trains a **Linear Regression** model on historical close prices
- 🔮 Predicts prices up to **500 days** into the future
- 📉 Plots historical vs. predicted prices with `matplotlib`

---

## ⚙️ How It Works

```
Historical Data (yfinance)
        │
        ▼
Feature Engineering: Close, MA10, MA50
        │
        ▼
Train Linear Regression (70% train / 30% test)
        │
        ▼
Iterative 500-Day Forecast
        │
        ▼
Matplotlib Visualization
```

| Step | Detail |
|------|--------|
| **Data Source** | Yahoo Finance via `yfinance` (Jan 2000 – May 2026) |
| **Features** | `Close`, `MA10` (10-day avg), `MA50` (50-day avg) |
| **Target** | Next day's closing price (`Close.shift(-1)`) |
| **Model** | `sklearn.LinearRegression` |
| **Forecast** | Each prediction feeds back into the rolling window |

---

## 🛠️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/stock-price-predictor.git
cd stock-price-predictor
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install yfinance pandas numpy matplotlib scikit-learn
```

> **`requirements.txt`**
> ```
> yfinance
> pandas
> numpy
> matplotlib
> scikit-learn
> ```

---

## 🚀 Usage

```bash
python stock_predictor.py
```

You'll be prompted to enter a stock symbol:

```
Enter the stock symbol (e.g., AAPL for Apple): TSLA
```

The script will output:

```
Model R-squared: 0.9984

[Chart window opens]
```

### Supported Ticker Examples

| Symbol | Company |
|--------|---------|
| `AAPL` | Apple Inc. |
| `TSLA` | Tesla Inc. |
| `GOOGL` | Alphabet Inc. |
| `MSFT` | Microsoft Corp. |
| `AMZN` | Amazon.com Inc. |
| `RELIANCE.NS` | Reliance Industries (NSE) |
| `TCS.NS` | Tata Consultancy Services (NSE) |

> 💡 For Indian stocks, append `.NS` (NSE) or `.BO` (BSE) to the ticker symbol.

---

## 📊 Output

The script generates a chart with:

- 🔵 **Blue line** — Historical closing prices
- 🔴 **Red dashed line** — Predicted future prices (500 days)

---

## ⚠️ Limitations

- Linear Regression is a **simple baseline** — predictions can diverge over long horizons
- Iterative forecasting **accumulates errors** with each step
- Does **not factor in** earnings, news, or macroeconomic events
- High R² score reflects price continuity, not true predictive power

---

## 📜 Disclaimer

> This project is for **educational purposes only**.  
> It is **not financial advice**. Do not make investment decisions based on this tool's output.  
> Past stock performance does not guarantee future results.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Made with ❤️ and Python</p>
