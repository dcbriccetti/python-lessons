import numpy as np
import matplotlib.pyplot as plt

def ym(years, months): return years * 12 + months
def fi(feet, inches):  return feet * 12 + inches

data = (
    ('Sue',     ym(12, 1),    fi(5, 2), 85,     'orange'),
    ('Bill',    ym(12, 9),    fi(5, 4), 130,    'yellow'),
    ('Jeff',    ym(13, 2),    fi(5, 3), 110,    'green'),
    ('Jenny',   ym(14, 5),    fi(5, 5), 120,    'blue'),
    ('Peter',   ym(13, 2),    fi(5, 2), 95,     'indigo')
)

for name, age, height, weight, color in data:
    plt.scatter(age / 12.0, height, s=np.pi * (weight / 15) ** 2, c=color, label=name, alpha=0.5)

plt.title('Heights and Weights by Age')
plt.legend(loc='upper left')
plt.xlabel('Age')
plt.ylabel('Height')
plt.grid()
plt.show()
