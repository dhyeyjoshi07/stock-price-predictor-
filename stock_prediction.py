import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from datetime import timedelta

# Get user input for stock symbol
stock_symbol = input("Enter the stock symbol (e.g., AAPL for Apple): ")

# Fetch historical stock data
data = yf.download(stock_symbol, start='2000-01-01', end='2026-05-01', auto_adjust=True)

# If data is MultiIndex (common in recent yfinance versions), flatten it
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Use 'Close' price and calculate moving averages
data = data[['Close']].copy()
data['MA10'] = data['Close'].rolling(window=10).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# Create a column for the "Tomorrow" stock price (next day's close)
data['Tomorrow'] = data['Close'].shift(-1)

# Drop rows with NaN values (from rolling windows and the shift)
data.dropna(inplace=True)

# Features and labels
feature_cols = ['Close', 'MA10', 'MA50']
X = data[feature_cols]
y = data['Tomorrow']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model (R-squared score)
print(f"\nModel R-squared: {model.score(X_test, y_test)}")

# --- Prediction for future days ---
prediction_days = 500
current_window = data['Close'].iloc[-50:].values.flatten().tolist()
predictions = []

for i in range(prediction_days):
    # Calculate MAs based on current window
    current_close = current_window[-1]
    ma10 = np.mean(current_window[-10:])
    ma50 = np.mean(current_window[-50:])

    # Prepare features for prediction as a DataFrame to match training feature names
    X_curr = pd.DataFrame([[current_close, ma10, ma50]], columns=feature_cols)
    next_pred = model.predict(X_curr)[0]

    predictions.append(next_pred)
    current_window.append(next_pred)
    current_window.pop(0) # Maintain window size

# Create a future date range
last_date = data.index[-1]
future_dates = [last_date + timedelta(days=i) for i in range(1, prediction_days + 1)]

# Create a DataFrame for the predicted prices
predicted_data = pd.DataFrame(predictions, index=future_dates, columns=['Predicted Close'])

# --- Plot ---
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Historical Data', color='blue', alpha=0.6)
plt.plot(predicted_data.index, predicted_data['Predicted Close'], label=f'Predicted Price ({prediction_days} Days)', color='red', linestyle='--')
plt.title(f'{stock_symbol} Stock Price Prediction with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
