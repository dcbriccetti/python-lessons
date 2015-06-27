import urllib.request

response = urllib.request.urlopen("http://google.com")
print(response.read())
