from random import choice
items = ('soup', 'corn', 'milk', 'bread', 'eggs')
item = choice(items)
positiveSayings = ('Stay in school!', "Don't do drugs!")
guessesLeft = 3

print('Mr. T says guess the food item in', guessesLeft, 'guesses.')
print('Items:', items)

while guessesLeft > 0:
	guessesLeft -= 1
	guess = input('Your guess? ')
	if guess == item:
		print("That's right. " + choice(positiveSayings))
		break # Exit the while loop
	if guessesLeft:
		print('Wrong.', guessesLeft, 'guesses left.')

if guess != item:
	print("I pity the fool!")
