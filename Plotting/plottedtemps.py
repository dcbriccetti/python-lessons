import matplotlib.pyplot as plt
import numpy as np
import requests

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def temp_for_location(location):
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&mode=json' % location)
    json = resp.json()
    main = json['main']
    temp = main['temp']
    c_temp = kelvin_to_celcius(temp)
    return c_temp

cities = ('Walnut Creek', 'Lafayette', 'San Francisco')
zips = ('94597', '94549', '94108')
temperatures = [temp_for_location(zip) for zip in zips]
y_pos = np.arange(len(cities))

plt.barh(y_pos, temperatures, align='center', alpha=0.4)
plt.yticks(y_pos, cities)
plt.xlabel('Temperature')
plt.title('Current Temperatures')
plt.show()
