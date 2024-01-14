import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set a seed for reproducibility
np.random.seed(42)

# Generate random time series data for stock prices
date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='B')  # Business days
stock_prices = np.cumsum(np.random.normal(0, 1, len(date_rng)))

# Create a DataFrame with date as the index and stock prices as the column
stock_df = pd.DataFrame(data={'StockPrice': stock_prices}, index=date_rng)

# Display the original time series data
print("Original Time Series Data:")
print(stock_df.head())
print("\n")

# Time Series Analysis
# Calculate rolling average (simple moving average) with a window of 5 days
stock_df['RollingAverage'] = stock_df['StockPrice'].rolling(window=10).mean()

# Visualize the time series data and rolling average
plt.figure(figsize=(10, 6))
plt.plot(stock_df['StockPrice'], label='Stock Price')
plt.plot(stock_df['RollingAverage'], label='Rolling Average (10 days)', linestyle='--', color='orange')
plt.title('Stock Price Time Series Analysis')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
