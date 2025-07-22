import yfinance as yf
import pandas as pd


tesla = yf.Ticker("TSLA")
tesla_history = tesla.history(period="max")
tesla_history.reset_index(inplace=True)

tesla_history.head()
