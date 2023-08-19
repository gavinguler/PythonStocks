import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

tickers =['BTC-USD','ETH-USD','SOL-USD','ADA-USD','BNB-USD']

end_date = datetime.today()
print(end_date)

start_date = end_date - timedelta(days = 2 * 365)
print(start_date)

close_df = pd.DataFrame()

for ticker in tickers:
  data = yf.download(ticker, start = start_date, end = end_date)
  close_df[ticker] = data['Close']
  
print (close_df)

output_folder = r"/Users/gavinguler/Desktop"
output_file = os.path.join(output_folder, 'crypto_prices.xlsx')
close_df.to_excel(output_file)