
import pandas as pd

# Data Source
import yfinance as yf

# Data viz
import plotly.graph_objs as go

# see all columns and rows
pd.options.display.max_columns = None
pd.options.display.max_rows = None

# Interval required 1 minute
data = yf.download(tickers='AAPL', period='6mo', interval='1d')
data.to_csv('aapl.csv')


