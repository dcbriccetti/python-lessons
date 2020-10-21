import requests
from bs4 import BeautifulSoup
state = input('What state? (California) ').lower().replace(' ', '-') or "california"
city  = input('What city? ') .lower().replace(' ', '-')
response = requests.get(f'https://www.iqair.com/us/usa/{state}/{city}')
soup = BeautifulSoup(response.text, 'html.parser')
aqi_elem = soup.find('p', class_='aqi-value__value')
if aqi_elem:
    aqi_text = aqi_elem.text
    aqi_value = int(aqi_text)
    print(f'Air quality index: {aqi_value}')
else:
    print('Not found')
