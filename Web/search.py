import requests

search_arg = 'Guido von Rossum'
response = requests.get('https://api.duckduckgo.com/?q=%s&format=json&pretty=1' % search_arg).json()
print('From {}: {}'.format(response['AbstractSource'], response['Abstract']))
