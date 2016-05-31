import requests

treasure_found = False
clue_loc = 'http://localhost:5000/n-2'

while not treasure_found:
	resp = requests.get(clue_loc)
	print(resp.text)
	if resp.text == 'You have reached the treasure!':
		treasure_found = True
	else:
		clue_loc = resp.text
