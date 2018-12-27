import requests
import json

class Requester:
    def __init__(self, date, ticker):
        self.marketData = []
        self.date = date
        self.ticker = ticker
        self.getData()

    def getData(self):
        request = requests.get("https://api.iextrading.com/1.0/stock/aapl/chart/date/20181226")
        self.marketData = json.loads(request.text)

    def getMarketAverageColours(self):
        marketAverages = []
        for time in self.marketData:
            marketAverages.append(time["marketAverage"])

        minValue = min(marketAverages)
        maxValue = max(marketAverages)

        marketAverageColours = []
        for marketAverage in marketAverages:
            marketAverageColours.append((marketAverage-minValue)/(maxValue-minValue))

        return marketAverageColours
