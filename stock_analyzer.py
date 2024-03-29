import yfinance as yf
import pandas as pd

class StockAnalyzer:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data = None

    def fetch_stock_data(self):
        self.stock_data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
        return self.stock_data