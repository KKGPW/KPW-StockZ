import yfinance


class Stock:
    __stock_data = None

    def __init__(self):
        pass

    def grab(self):
        self.__stock_data = yfinance.download(tickers='UBER', period='1d', interval='1m')

    def to_console(self):
        print(self.__stock_data)
