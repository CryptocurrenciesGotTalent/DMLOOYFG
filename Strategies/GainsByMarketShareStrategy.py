import random
import Strategies.Strategy as Strategy
import Adapters.marketState as MS
import datetime
import math

def f(x):
  return math.log(x/(1-x))



class GainsByMarketShareStrategy(Strategy.Strategy):

  def __init__(self, initialDate, interval):
    date = initialDate.split("/")
    self.initialDate = datetime.date(int(date[2]), int(date[1]), int(date[0]))
    self.previousDate = self.initialDate
    self.currentDate = self.initialDate
    self.interval = interval
    self.previousDateData = MS.MarketState(self.initialDate.day, self.initialDate.month, self.initialDate.year)
    self.currentDateData = self.previousDateData

  def callBackData(self):
    return range(1,10)
    
  # MarketShare for each coin
  # def getInitialX(self):
  #   date = self.date.split("/")
  #   initialDateData = MS.MarketState(int(date[0]), int(date[1]), int(date[2]))
  #   self.nbCoins = initialDateData.getNbCoins()
  #   self.totalMarketCap = initialDateData.getTotalMarketCap()
  #   res = [1-initialDateData.getMarketCapAtRank(rank)/self.totalMarketCap for rank in range(0,self.nbCoins)]
  #   return res

  # def getInitialY(self):
  #   return [1]*self.nbCoins

  def getXY(self, i):
    # date = self.date.split("/")
    # initialDate = datetime.date(int(date[2]), int(date[1]), int(date[0]))
    self.previousDate = self.currentDate
    self.currentDate = self.currentDate + datetime.timedelta(days = self.interval)

    self.previousDateData = self.currentDateData
    self.currentDateData = MS.MarketState(self.currentDate.day, self.currentDate.month, self.currentDate.year)

    self.nbCoins = self.previousDateData.getNbCoins()
    # self.totalMarketCap = self.previousDateData.getTotalMarketCap()
    X = []
    Y = []


    for k in range(self.nbCoins):
      coin = self.previousDateData.getCoinAtRank(k)
      variation = coin.getMarketCapVariation((self.previousDate.day,self.previousDate.month,self.previousDate.year),
                                        (self.currentDate.day,self.currentDate.month,self.currentDate.year))


      if variation != None :
        X.append(1-self.previousDateData.getMarketCapAtRank(k)/self.previousDateData.getTotalMarketCap())
        Y.append(variation)

      #if X and Y:
      #  print("{} : {}, {}".format(k,X[-1],Y[-1]))

    X = list(map(f, X))
    return X,Y