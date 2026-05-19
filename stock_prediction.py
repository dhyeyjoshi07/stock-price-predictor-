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
data = yf.download(stock_symbol, start='2000-01-01', end='2026-03-15')

# Use only 'Close' price for prediction
data = data[['Close']]

# Create a column for the "Tomorrow" stock price (next day's close)
data['Tomorrow'] = data['Close'].shift(-1)

# Drop the last row since it doesn't have a "Tomorrow" value
data.dropna(inplace=True)

# Features and labels
X = data[['Close']]  # Features: Close price
y = data['Tomorrow']  # Labels: Next day's close price

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict stock prices for the test set
y_pred = model.predict(X_test)

# Evaluate the model (R-squared score)
print(f"\nModel R-squared: {model.score(X_test, y_test)}")

# --- Prediction for 3 months ---
last_price = data['Close'].iloc[-1]
predictions = []
prediction_days = 500

for i in range(prediction_days):
    prediction = model.predict(np.array(last_price).reshape(1, -1))
    predictions.append(prediction[0])
    last_price = prediction[0]

# Create a future date range
last_date = data.index[-1]
future_dates = [last_date + timedelta(days=i) for i in range(1, prediction_days + 1)]

# Create a DataFrame for the predicted prices
predicted_data = pd.DataFrame(predictions, index=future_dates, columns=['Predicted Close'])

# --- Plot ---
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Close'], label='Historical Data', color='yellow')
plt.plot(predicted_data.index, predicted_data['Predicted Close'], label='Predicted Price (Next 500 Days)', color='black')
plt.title(f'{stock_symbol} Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()