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
    plt.gca().set_ylim([0.1,4])
    plt.gca().set_xlim([0,30])
    self.ax.plot(x,y)

  def draw(self):
    plt.gca().set_ylim([0,5])
    ani = animation.FuncAnimation(self.fig, self.animate,self.strategy.callBackData(),
                                  interval=50)
    plt.show()


