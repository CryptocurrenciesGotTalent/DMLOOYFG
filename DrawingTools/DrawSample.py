import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



# x = range(0,100,2)
# line, = ax.plot(x, x)


class toto:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        x = range(0,100,2)
        self.line, = self.ax.plot(x, x)

    def animate(self,i):
        print(i)
        x = range(0,i,2)
        self.line.set_xdata(x)  # update the data
        self.line.set_ydata(x)  # update the data
        return self.line,

    def init(self):
        x = range(0,100,2)
        self.line.set_ydata(x)
        self.line.set_xdata(x)
        return self.line,

    def draw(self):
        ani = animation.FuncAnimation(self.fig, self.animate, np.arange(1, 200),
                              init_func=self.init,
                              interval=0.1, blit=True)
        plt.show()

t = toto()
t.draw()

