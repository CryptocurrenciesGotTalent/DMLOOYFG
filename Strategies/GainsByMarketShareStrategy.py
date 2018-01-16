import random
import Strategies.Strategy as Strategy
import Adapters.marketState as MS
class GainsByMarketShareStrategy(Strategy.Strategy):

  def __init__(self, initialDate):
    self.date = initialDate

  def callBackData(self):
    return range(0,10)
    
  # MarketShare for each coin
  def getInitialX(self):
    date = self.date.split("/")
    initialDateData = MS.MarketState(int(date[0]), int(date[1]), int(date[2]))
    self.nbCoins = initialDateData.getNbCoins()
    self.totalMarketCap = initialDateData.getTotalMarketCap()
    res = [initialDateData.getMarketCapAtRank(rank)/self.totalMarketCap for rank in range(0,self.nbCoins)]
    return res

  def getInitialY(self):
    return [random.randint(1, 10) for rank in range(0,self.nbCoins)]

  def getX(self, i):
    date = self.date.split("/")
    initialDateData = MS.MarketState(int(date[0]), int(date[1]), int(date[2]))
    self.nbCoins = initialDateData.getNbCoins()
    self.totalMarketCap = initialDateData.getTotalMarketCap()
    res = [initialDateData.getMarketCapAtRank(rank)/self.totalMarketCap for rank in range(0,self.nbCoins)]
    return res

  def getY(self, i):
    return [random.randint(1, 10) for rank in range(0,self.nbCoins)]
