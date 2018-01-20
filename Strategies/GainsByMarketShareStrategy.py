import random
import Strategies.Strategy as Strategy
import Adapters.marketState as MS
import datetime
import math

def f(x):
  return math.log(x/(1.00000000001-x))

def movingAverage(Y, listMC, period):
  movingAverage = []

  for i in range(period-1):
    movingAverage.append(sum(Y[0:i+1])/(i+1))

  for i in range(period-1, len(listMC)):
    lastPeriodVariation = sum(Y[i-period+1:i+1])
    valueToDraw = lastPeriodVariation/period
    # lastPeriodTotalMCs = sum(listMC[i-period+1:i+1])
    # yMCcouples = [(Y[k], listMC[k]) for k in range(i-period+1,i+1)]
    # yi = sum([y*mc for (y,mc) in yMCcouples[i-period+1:i+1]])/lastPeriodTotalMCs

    movingAverage.append(valueToDraw)

  return movingAverage

class GainsByMarketShareStrategy(Strategy.Strategy):

  def __init__(self, initialDate, finalDate, interval, shift):
    date1 = initialDate.split("/")
    date2 = finalDate.split("/")
    self.initialDate = datetime.date(int(date1[2]), int(date1[1]), int(date1[0]))
    self.finalDate = datetime.date(int(date2[2]), int(date2[1]), int(date2[0]))
    self.previousDate = self.initialDate
    self.currentDate = self.initialDate
    self.interval = interval
    self.shift = shift
    self.previousDateData = MS.MarketState(self.initialDate.day, self.initialDate.month, self.initialDate.year)
    self.currentDateData = self.previousDateData

  def callBackData(self):
    return range(1,10)
    
  def getDate(self, i):
    return MS.dateToString(self.currentDate.day, self.currentDate.month, self.currentDate.year)

  # def getTotalMarketCap2(self, i):
  #   return MS.totalMarketCap()

  # def test(self,i):
  #   return MS.getNbCoins(self)

  def getXY(self, i):
    # date = self.date.split("/")
    # initialDate = datetime.date(int(date[2]), int(date[1]), int(date[0]))
    self.previousDate = self.previousDate + datetime.timedelta(days = self.shift)
    self.currentDate = self.previousDate + datetime.timedelta(days = self.interval)
    if self.currentDate == self.finalDate:
      return 0
    self.previousDateData = MS.MarketState(self.previousDate.day, self.previousDate.month, self.previousDate.year)
    self.currentDateData = MS.MarketState(self.currentDate.day, self.currentDate.month, self.currentDate.year)

    self.nbCoins = self.previousDateData.getNbCoins()
    # self.totalMarketCap = self.previousDateData.getTotalMarketCap()
    X = []
    Y = []
    listMC = []

    for k in range(self.nbCoins):
      coin = self.previousDateData.getCoinAtRank(k)
      variation = coin.getMarketCapVariation((self.previousDate.day,self.previousDate.month,self.previousDate.year),
                                        (self.currentDate.day,self.currentDate.month,self.currentDate.year))


      if variation != None :
        X.append(1-self.previousDateData.getMarketCapAtRank(k)/self.previousDateData.getTotalMarketCap())
        Y.append(variation)

        listMC.append(self.previousDateData.getMarketCapAtRank(k))
      #if X and Y:
      #  print("{} : {}, {}".format(k,X[-1],Y[-1]))

    X = list(map(f, X))
    Y = movingAverage(Y, listMC, 50)

    return X,Y