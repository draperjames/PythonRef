# print("hello")
# print("I guess that hydrogen is actually running now!")
import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
plt.plot(x,y)
plt.show()
# mpl.pyplot.plot(x,y)
# dir(mpl)
