
import urllib.request
import numpy


stockstoPull = []

class Stock:
    #constructor for Stcok class
    def __init__(self,ticker,price):

        self.sethistoricalprice(price)
        self.setticker(ticker)

    def setticker(self, ticker):
        self.tickername = ticker

    def sethistoricalprice(self,price):
        self.historicalprice = price

    def getticker(self):
        return self.tickername
    def gethistoricalprice(self):
        return self.historicalprice


class Portfolio:
    #constructor for portfolio
    def __init__(self):
        self.folio = []
        self.stockweight = 0.25

    def addtoportfolio(self, stock):
        self.folio.append(stock)

    def getportfolio(self):
        return self.folio

    def weight(self):
        return self.stockweight

class Calculator:
    #constructor for calculator
    def __init__(self):
        self.stdv = 0
        self.covariance = 0
        self.dailyreturn = []
        self.averagereturn = 0
        self.variance = 0

    def standardeviation(self, stockdata):
        self.stdv = numpy.std(stockdata)

    def dailyreturn(self, stockdata):
        #Calculating the daily returns and appending
        for i in range(1,len(stockdata)):
            self.dailyreturn.append((stockdata[i-1]/ stockdata[i]) - 1)

    def averageReturn(self):
        self.averagereturn = numpy.average(self.dailyreturn)

    def variance(self):
        self.variance = numpy.var(self.dailyreturn)




def stockData(stock):

    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
    with urllib.request.urlopen(url) as f:
        source = f.read().decode('utf-8')
    splitSource = source.split('\n')
    modified = splitSource[18:len(splitSource)]

    return modified


if __name__=="__main__":


    while True:

        ticker = input("Enter Stock Tickers, Enter 0 to stop: ").upper()
        if ticker == "0":
            break
        stockstoPull.append(ticker)

    while True:
         investment = input("Enter your investing amount: ")
         if investment.isdigit():
             break

    stockprice = []
    #Creating a portfolio object to store all of the
    #stocks
    portfolio = Portfolio()
    for eachStock in stockstoPull:
        data = stockData(eachStock)
        for eachday in range(0,len(data)-1):
            data_split = data[eachday].split(",")
            date = data_split[0]
            closingPrice = float(data_split[1])
            stockprice.append(closingPrice)
            #appending each stock to the portfolio object

        stock = Stock(eachStock,stockprice)
        portfolio.addtoportfolio(stock)






