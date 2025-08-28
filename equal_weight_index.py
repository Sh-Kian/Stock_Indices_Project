import pandas as pd

# Load market data
data = pd.read_csv('data/market_data.csv')


# Calculate Equal Weight Index (average of stock prices)
equal_weight_index = data['Price'].mean()
print('Equal Weight Index:', equal_weight_index)