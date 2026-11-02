import yfinance as yf
import pandas as pd 

def fetch_btc_data(start_date='2022-01-01', end_date='2026-11-01'):
    # Fetches historical OHLCV data for Bitcoin
    df = yf.download('BTC-USD', start=start_date, end=end_date, progress=False)
    return df