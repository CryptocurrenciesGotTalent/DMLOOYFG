import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Generic Drawing class, takes a strategy as a parameter
class Drawing:

  def __init__(self, strategy):
    self.strategy = strategy
    self.fig = plt.figure()
    self.ax = self.fig.add_subplot(1,1,1)
    self.text = plt.gcf().text(0.7, 0.9, "hello", fontsize=8)
  
  # Chart values at frame i
  def animate(self,i):
    print(i)
    self.ax.clear()
    x,y = self.strategy.getXY(i)
    plt.gca().set_ylim([0.1,4])
    plt.gca().set_xlim([-1,26])
    horiz_line_data = np.array([1,1])
    plt.plot([0,50], horiz_line_data, 'r--')
    self.text.set_text(self.strategy.getDate(i))
    self.ax.plot(x,y, 'bo', markersize=2)

  def draw(self):
    plt.gca().set_ylim([0,5])
    ani = animation.FuncAnimation(self.fig, self.animate,self.strategy.callBackData(),
                                  interval=50)

    plt.show()


