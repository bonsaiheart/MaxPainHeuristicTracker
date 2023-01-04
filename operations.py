import yfinance as yf
from datetime import timedelta
from datetime import datetime


class RetrieveHistoricalData:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_closing_price(self, date):

        first_day = datetime.strptime(date, '%Y-%m-%d')
        next_day = first_day + timedelta(1)
        ticker = yf.Ticker(self.symbol)
        stock_history = ticker.history(start=date, end=next_day, interval="1d")

        closing_price = (stock_history.at[stock_history.index[0], "Close"])
        return closing_price
