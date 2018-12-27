import requests

class Requester:
    def __init__(self, date, ticker):
        self.marketData = []
        self.date = date
        self.ticker = ticker

    def getData(self):
        request = requests.get("https://api.iextrading.com/1.0/stock/aapl/chart/date/20181226")
        self.marketData = request.json()

        print(self.marketData[0])