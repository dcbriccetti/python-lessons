import requests

key = open('openweathermap.txt').read().strip()  # Put your API key in this file


def temp_at_location(location):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&mode=json&units=metric&APPID=%s' % (location, key)
    json = requests.get(url).json()
    return json['main']['temp']

print('%.1f' % temp_at_location('94549,US'))