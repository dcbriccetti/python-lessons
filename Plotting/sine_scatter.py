from math import sin, pi
import matplotlib.pyplot as plt

domain = range(0, 360, 6)
sines = [sin(angle / 360 * 2 * pi) for angle in domain]
plt.scatter(domain, sines)
plt.show()
