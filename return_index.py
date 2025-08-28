import pandas as pd

# Load market data
data = pd.read_csv('data/market_data.csv')


# Calculate daily returns for each stock
data['Return'] = data['Price'].pct_change()
print('Daily Return Index:\n', data[['Stock','Return']])