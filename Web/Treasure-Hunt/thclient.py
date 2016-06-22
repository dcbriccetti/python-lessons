import requests

treasure_found = False
URL_START = 'http://localhost:5000'
clue_loc = '/'

while not treasure_found:
    print('Going to', clue_loc)
    resp = requests.get(URL_START + clue_loc)
    if resp.text == 'You have reached the treasure!':
        treasure_found = True
        print(resp.text)
    else:
        print('Clue from %s: %s' % (clue_loc, resp.text))
        clue_loc = resp.text
