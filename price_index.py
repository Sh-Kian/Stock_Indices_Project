import pandas as pd

# Load market data
# CSV columns: Stock, Price, Volume, NetIncome, Revenue, Equity, SharesOutstanding, Years
data = pd.read_csv('data/market_data.csv')


# Calculate Total Market Price Index
price_index = data['Price'].sum()
print('Total Market Price Index:', price_index)