import Strategies.Strategy as Strategy

class TestStrategy(Strategy.Strategy) :
  def __init__(self):
    pass

  def callBackData(self):
    return range(1, 100)
    
  def getInitialX(self):
    return range(0,100)

  def getInitialY(self):
    return range(0,100)

  def getX(self, i):
    return range(0,i)

  def getY(self, i):
    return range(0,i)
