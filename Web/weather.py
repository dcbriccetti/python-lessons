import requests

key = open('openweathermap.txt').read().strip()  # Put your API key in this file


def kelvin_to_celcius(k):
    return k - 273.15


def temp_at_location(location):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&mode=json&APPID=%s' % (location, key)
    resp = requests.get(url)
    json = resp.json()
    main = json['main']
    kelvin_temp = main['temp']
    celcius_temp = kelvin_to_celcius(kelvin_temp)
    return celcius_temp

print('%.1f' % temp_at_location('94549,US'))