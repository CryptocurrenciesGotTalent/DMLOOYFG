import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Generic Drawing class, takes a strategy as a parameter
class Drawing:

  def __init__(self, strategy):
    self.strategy = strategy
    self.fig = plt.figure()
    self.ax = self.fig.add_subplot(1,1,1)
  
  # Chart values at frame i
  def animate(self,i):
    print(i)
    self.ax.clear()
    x,y = self.strategy.getXY(i)
    self.ax.plot(x,y, 'bo')

  def draw(self):
    ani = animation.FuncAnimation(self.fig, self.animate,self.strategy.callBackData(),
                                  interval=500)
    plt.show()

