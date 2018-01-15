class Strategy:

  def __init__(self):
    raise NotImplementedError()

  def callBackData(self):
    raise NotImplementedError()
    
  def getInitialX(self):
    raise NotImplementedError()

  def getInitialY(self):
    raise NotImplementedError()

  def getX(self, i):
    raise NotImplementedError()

  def getY(self, i):
    raise NotImplementedError()
