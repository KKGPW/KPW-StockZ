from StockZ.modules.grabber import Stock

if __name__ == "__main__":
    test_stock = Stock()
    test_stock.grab()
    test_stock.to_console()
