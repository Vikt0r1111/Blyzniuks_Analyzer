# Stock Analyzer

This project provides a simple stock analysis tool using Yahoo Finance data. It consists of several files and classes to manage stock data, calculate technical indicators, and plot the results.

## Files

### 1. `stock_analyzer.py`

This file contains the `StockAnalyzer` class responsible for fetching stock data and calculating technical indicators.

#### Class: `StockAnalyzer`

```python
class StockAnalyzer:
    def __init__(self, symbol: str, start_date: str, end_date: str):
        """
        Initialize the StockAnalyzer.

        Parameters:
        - symbol (str): The stock symbol.
        - start_date (str): The start date for fetching data (YYYY-MM-DD).
        - end_date (str): The end date for fetching data (YYYY-MM-DD).
        """
        ...

    def fetch_stock_data(self) -> pd.DataFrame:
        """
        Fetch stock data from Yahoo Finance.

        Returns:
        - pd.DataFrame: Stock data with columns (Open, High, Low, Close, Volume, Adj Close).
        """
        ...

    def calculate_technical_indicator(self, indicator: str = 'SMA', window: int = 20) -> None:
        """
        Calculate technical indicators for stock data.

        Parameters:
        - indicator (str): The technical indicator to calculate (default is 'SMA').
        - window (int): The window size for the indicator calculation (default is 20).
        """
        ...#   B l y z n i u k s _ A n a l y z e r  
 