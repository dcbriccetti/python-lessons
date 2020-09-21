import requests
from bs4 import BeautifulSoup
while True:
    state = input('What state? ').lower().replace(' ', '-')
    city  = input('What city? ') .lower().replace(' ', '-')
    response = requests.get(f'https://www.iqair.com/us/usa/{state}/{city}')
    soup = BeautifulSoup(response.text, 'html.parser')
    aqi_elem = soup.find('p', class_='aqi-value__value')
    if aqi_elem:
        aqi_value = int(aqi_elem.text)
        print(f'Air quality index: {aqi_value}')
    else:
        print('Not found')
