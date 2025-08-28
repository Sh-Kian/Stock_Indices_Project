import pandas as pd

# Load market data
data = pd.read_csv('data/market_data.csv')


# Calculate total traded volume
volume_index = data['Volume'].sum()
print('Total Volume Index:', volume_index)