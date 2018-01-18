import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y = np.meshgrid([0,3,5,7,8,9], [0,1,2,3,4,5])

def zfunc(x, y):
    return np.exp(-(y**2)) * np.cos(3.*x) + np.exp(x**2) * np.cos(3.*y)



z = np.array([[1,1,1,1,1,1],[0.9,1,1,1,1,1],[1,0.5,1,1,1,1],[1,1,1.5,1,1,1],[1,1,1,2,1,1],[1,1,1,1,0.1,1]])

print(z)
ax.plot_surface(x, y, z)

plt.show()