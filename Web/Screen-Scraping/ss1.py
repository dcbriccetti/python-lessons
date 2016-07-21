import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.google.com/search?q=mlb').text

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
