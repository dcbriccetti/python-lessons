# An example from matplotlib

import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
radius = 15 * np.random.rand(N)
area = np.pi * radius ** 2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()