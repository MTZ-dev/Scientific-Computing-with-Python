import numpy as np
import matplotlib.pyplot as plt

#EXERCISE 9.1

x = np.linspace(0,10,200)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_inv_exp = np.exp(-x)

plt.plot(x, y_sin, 'r-', label = "sin(x)")
plt.plot(x, y_cos, 'g--', label = "cos(x)")
plt.plot(x, y_inv_exp, 'b:', label = "exp(-x)")
plt.legend(loc = 'lower left', fancybox = False, edgecolor = 'black')
plt.show()

#EXERCISE 9.2

n = 100
points = np.random.rand(2, n)
colors = np.where(np.sqrt(np.square(points[0]) + np.square(points[1])) < 1,'g', 'r')
area = 40 * (np.abs(points[0]) + np.abs(points[1])) 
plt.scatter(points[0], points[1], s = area, c = colors)

#narysowałem ćwirtkę okręgu żeby sprawdzić czy wszystko jest ok
theta = np.linspace(0, 1/2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y, 'b-', linewidth=1)
plt.show()