import pandas as pd

# Load market data
data = pd.read_csv('data/market_data.csv')


# Calculate volatility (std deviation of daily returns)
volatility = data['Price'].pct_change().std()
print('Volatility Index:', volatility)