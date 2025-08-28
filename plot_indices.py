import pandas as pd
import matplotlib.pyplot as plt


# Load data
data = pd.read_csv('data/market_data.csv')


# Calculate indices
price_index = data['Price'].sum()
equal_weight_index = data['Price'].mean()
volume_index = data['Volume'].sum()
data['Return'] = data['Price'].pct_change()
volatility = data['Price'].pct_change().std()


# Financial Ratios
data['ROI'] = (data['NetIncome'] / data['Revenue']) * 100
data['EPS'] = data['NetIncome'] / data['SharesOutstanding']
data['P/E'] = data['Price'] / data['EPS']
data['ROE'] = (data['NetIncome'] / data['Equity']) * 100
data['CAGR'] = ((data['Price'] / data['Price'].iloc[0]) ** (1 / data['Years']) - 1) * 100


# Plotting
plt.figure(figsize=(12,6))


plt.subplot(2,3,1)
plt.bar(data['Stock'], data['Price'])
plt.title('Price Index')


plt.subplot(2,3,2)
plt.bar(data['Stock'], [equal_weight_index]*len(data))
plt.title('Equal Weight Index')


plt.subplot(2,3,3)
plt.bar(data['Stock'], data['Volume'])
plt.title('Volume Index')


plt.subplot(2,3,4)
plt.bar(data['Stock'], data['Return'].fillna(0))
plt.title('Return Index')


plt.subplot(2,3,5)
plt.bar(data['Stock'], [volatility]*len(data))
plt.title('Volatility Index')


plt.subplot(2,3,6)
plt.bar(data['Stock'], data['CAGR'])
plt.title('CAGR')


plt.tight_layout()
plt.show()