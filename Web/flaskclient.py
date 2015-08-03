import requests

resp = requests.get('http://localhost:5000/')
status = resp.status_code

print(resp.text)
