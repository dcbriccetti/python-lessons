import requests

def k_to_c(k):
    return k - 273.15

def temp_at_location(location):
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&mode=json' % location)
    json = resp.json()
    main = json['main']
    temp = main['temp']
    c_temp = k_to_c(temp)
    return c_temp
