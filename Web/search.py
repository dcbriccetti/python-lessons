import requests

search_arg = 'TCP/IP'
resp = requests.get('https://api.duckduckgo.com/?q=%s&format=json&pretty=1' % search_arg)
status = resp.status_code
json = resp.json()
print(json['Abstract'])
