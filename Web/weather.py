import requests

with open('openweathermap.txt') as file:
    key = file.read().strip()  # Put your API key in this file


def temp_at_location(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&mode=json&units=metric&APPID={key}'
    json = requests.get(url).json()
    return json['main']['temp']

if __name__ == '__main__':
    print(f'{temp_at_location("94549"):.1f}')
