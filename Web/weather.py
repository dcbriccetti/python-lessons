import requests

def k_to_c(k):
    return k - 273.15

location = '94549'
resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&mode=json' % location)

status = resp.status_code

json = resp.json()
main = json['main']
print(main)
temp = main['temp']
c_temp = k_to_c(temp)
print('The current temperature at %s is %.1fC' % (location, c_temp))
