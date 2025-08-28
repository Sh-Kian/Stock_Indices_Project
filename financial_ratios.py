import pandas as pd

# Load financial data
data = pd.read_csv('data/market_data.csv')


# ROI = Return on Investment (%)
data['ROI'] = (data['NetIncome'] / data['Revenue']) * 100


# EPS = Earnings Per Share
data['EPS'] = data['NetIncome'] / data['SharesOutstanding']


# P/E Ratio = Price / EPS
data['P/E'] = data['Price'] / data['EPS']


# ROE = Return on Equity (%)
data['ROE'] = (data['NetIncome'] / data['Equity']) * 100


# CAGR = Compound Annual Growth Rate (%)
data['CAGR'] = ((data['Price'] / data['Price'].iloc[0]) ** (1 / data['Years']) - 1) * 100


print(data[['Stock','ROI','EPS','P/E','ROE','CAGR']])