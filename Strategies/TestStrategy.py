import Strategies.Strategy as Strategy

class TestStrategy(Strategy.Strategy) :
  def __init__(self):
    pass

  def callBackData(self):
    return range(10, 20000,10)
    
  def getXY(self, i):
    return range(0,i,5),range(0,i,5)

