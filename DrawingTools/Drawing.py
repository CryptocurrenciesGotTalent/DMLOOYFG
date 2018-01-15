import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Drawing:

  def __init__(self, strategy):
    self.strategy = strategy
    self.fig, self.ax = plt.subplots()
    self.line, = self.ax.plot(self.strategy.getInitialX(), 
                              self.strategy.getInitialY())

  def setUp(self):
    pass
    
  def init(self):
    self.line.set_xdata(self.strategy.getInitialX())
    self.line.set_ydata(self.strategy.getInitialY())
    return self.line,

  def animate(self,i):
    print(i)
    self.line.set_xdata(self.strategy.getX(i))  # update the data
    self.line.set_ydata(self.strategy.getY(i))  # update the data
    return self.line,

  def draw(self):
    ani = animation.FuncAnimation(self.fig, self.animate, 
                                  range(1,100), 
                                  init_func=self.init,
                                  interval=1, blit=True )
    plt.show()

