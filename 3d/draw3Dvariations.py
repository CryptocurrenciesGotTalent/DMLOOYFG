import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import datetime



initialDate = datetime.date(2017,10, 1)
finalDate = datetime.date(2017,12, 30)
step = datetime.timedelta(days=1)

# y = range(0,(finalDate-initialDate).days, step.days)
# for i in y:
# 	x=0


'''
for ...
	x,z = strategy.getXY(i)
	x,z = resize(x,z,size)
	X.append(x)
	z.append(z)

construct Y
'''





# x = np.array([[0,3,4], [0,2,4], [0,3,4]])
# y = np.array([[0,0,0],[1,1,1],[2,2,2]])


# z = np.array([[1,1,1],[0.5,1,1],[1,0.5,1]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)

plt.show()