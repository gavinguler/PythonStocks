import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm
import os

# Define the number of years for historical data
years = 5

# Calculate the start and end dates
end_Date = dt.datetime.now()
start_Date = end_Date - dt.timedelta(days=365 * years)

# Print the calculated dates
print("End Date:", end_Date)
print("Start Date:", start_Date)

tickers = ['BTC-USD','ETH-USD','SOL-USD']

adj_close_df = pd.DataFrame()

for ticker in tickers:
  data = yf.download(ticker, start = start_Date, end = end_Date)
  adj_close_df[ticker] = data['Adj Close']
  
print(adj_close_df)

log_returns = np.log(adj_close_df/adj_close_df.shift(1))
log_returns = log_returns.dropna()

print ()

output_folder = r"/Users/gavinguler/Desktop"
output_file = os.path.join(output_folder, 'crypto_prices.xlsx')
log_returns.to_excel(output_file)

