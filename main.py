from stock_analyzer import StockAnalyzer
from plotting import Plotter

stock_symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2024-01-18'

# Create an instance of StockAnalyzer
stock_analyzer = StockAnalyzer(stock_symbol, start_date, end_date)

# Fetch data and calculate technical indicators
stock_data = stock_analyzer.fetch_stock_data()
stock_analyzer.calculate_technical_indicator()

# Use Plotter to display the results
Plotter.plot_stock_data(stock_data)