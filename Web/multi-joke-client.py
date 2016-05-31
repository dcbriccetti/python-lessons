import requests

targets = (
    ('Ryan',    'http://192.168.1.128:8080/joke'),
    ('Nathan',  'http://192.168.1.221:5000/joke'),
    ('Alex',    'http://192.168.1.53:5000/joke'),
    ('Hari',    'http://192.168.1.102:5000/joke')
)

while True:
    for target_name, target_url in targets:
        try:
            resp = requests.get(target_url)
            print(target_name + ': ' + resp.text)
        except requests.exceptions.ConnectionError:
            print(target_name + ' refused connection')
