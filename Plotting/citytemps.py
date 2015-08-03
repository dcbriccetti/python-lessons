# Inspired by an example from matplotlib

import matplotlib.pyplot as plt
import numpy as np

cities = ('Walnut Creek', 'Lafayette', 'Moraga')
y_pos = np.arange(len(cities))
temperature = 10 + 10 * np.random.rand(len(cities))

plt.barh(y_pos, temperature, align='center', alpha=0.4)
plt.yticks(y_pos, cities)
plt.xlabel('Temperature')
plt.title('Current Temperatures')
plt.show()
