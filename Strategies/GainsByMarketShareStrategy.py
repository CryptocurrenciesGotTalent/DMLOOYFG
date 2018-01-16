import random
import Strategies.Strategy as Strategy
import Adapters.marketState as MS
import datetime
class GainsByMarketShareStrategy(Strategy.Strategy):

  def __init__(self, initialDate, interval):
    self.date = initialDate
    self.interval = interval

  def callBackData(self):
    return range(0,10)
    
  # MarketShare for each coin
  def getInitialX(self):
    date = self.date.split("/")
    initialDateData = MS.MarketState(int(date[0]), int(date[1]), int(date[2]))
    self.nbCoins = initialDateData.getNbCoins()
    self.totalMarketCap = initialDateData.getTotalMarketCap()
    res = [1-initialDateData.getMarketCapAtRank(rank)/self.totalMarketCap for rank in range(0,self.nbCoins)]
    return res

  def getInitialY(self):
    return [1]*self.nbCoins

  def getX(self, i):
    date = self.date.split("/")
    initialDate = datetime.date(int(date[2]), int(date[1]), int(date[0]))
    ithDate = initialDate + datetime.timedelta(days = i*self.interval)

    ithDateData = MS.MarketState(ithDate.day, ithDate.month, ithDate.year)

    self.nbCoins = ithDateData.getNbCoins()
    self.totalMarketCap = ithDateData.getTotalMarketCap()
    res = [1-ithDateData.getMarketCapAtRank(rank)/self.totalMarketCap for rank in range(0,self.nbCoins)]
    return res

  def getY(self, i):
    date = self.date.split("/")
    initialDate = datetime.date(int(date[2]), int(date[1]), int(date[0]))
    ithDate = initialDate + datetime.timedelta(days = i*self.interval)

    ithDateData = MS.MarketState(ithDate.day, ithDate.month, ithDate.year)
    coins = [ithDateData.getCoinAtRank(k) for k in range(self.nbCoins)]

    return [coins[k].getVariation((ithDate.day, ithDate.month, ithDate.year), (initialDate.day, initialDate.month, initialDate.year)) for k in range(self.nbCoins)]
