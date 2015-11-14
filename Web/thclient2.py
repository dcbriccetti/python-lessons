import requests

treasure_found = False
url_base = 'http://localhost:5000/'
clue_loc = url_base


def solve_largest_puzzle(text):
	open_paren = text.index('(')
	close_paren = text.index(')')
	nums_str = text[open_paren + 1:close_paren]
	nums = [int(n) for n in nums_str.split(',')]
	return url_base + str(max(nums))


def solve_multiply_puzzle():
	m1 = int(requests.get(url_base + 'm1').text)
	m2 = int(requests.get(url_base + 'm2').text)
	return url_base + str(m1 * m2)

while not treasure_found:
	resp = requests.get(clue_loc)
	text = resp.text
	print(text)

	if text == 'You have reached the treasure!':
		treasure_found = True
	else:
		if 'where number is the largest' in text:
			clue_loc = solve_largest_puzzle(text)
		elif 'm1 * http' in text:
			clue_loc = solve_multiply_puzzle()
		else:
			clue_loc = text
