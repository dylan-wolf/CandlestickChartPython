import yfinance as yf
import pandas as pd


SYMBOL = 'LMT'

lmt_df = yf.download(SYMBOL, start='2020-01-01')

print(lmt_df.head())

print(lmt_df.to_csv(SYMBOL+'.csv'))

df = pd.read_csv(SYMBOL + ".csv")
correct_df = df.copy()
correct_df.rename(columns={'Date': 'date', 'Open': 'open','High': 'high','Low': 'low','Close': 'close'}, inplace=True)
print(correct_df)

correct_df.to_csv(SYMBOL+'.csv', index=False,header=True)
