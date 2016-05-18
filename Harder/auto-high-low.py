from random import randint
from math import log2, pow


class AiGuesser:
	def __init__(self, highest, smart=False, chatty=True):
		self.high = self.highest = highest
		self.smart = smart
		self.chatty = chatty
		self.low = 1
		self.last_guess = None
		self.guess_type = 'smart' if self.smart else 'random'

	def guess(self, too_high):
		if too_high is not None:
			if too_high:
				self.high = self.last_guess - 1
			else:
				self.low = self.last_guess + 1
		self.last_guess = self._middle() if self.smart else randint(self.low, self.high)
		if self.chatty:
			print('{:,}-{:,}: {:,}'.format(self.low, self.high, self.last_guess))
		return self.last_guess

	def win(self, guesses):
		if self.chatty:
			print('I got it in {} guesses.'.format(guesses))

	def _middle(self):
		return self.low + (self.high - self.low) // 2


with open('high-low-results.tsv', 'w') as results:
	results.write('Highest\tStrategy\tTrial\tGuesses\n')
	for power in (1, 2, 3, 6, 9, 12):
		highest = int(pow(10, power))
		print('Between 1 and {0:,} (binary logarithm of {0:,} is {1:.2f}).'.format(highest, log2(highest)))
		for smart in (True, False):
			print('Smart' if smart else 'Random')
			for trial in range(1, 101):
				print('Trial', trial)
				guesser = AiGuesser(highest, smart=smart, chatty=True)
				number = randint(1, highest)
				guess = guesser.guess(None)
				guesses = 1

				while guess != number:
					guesses += 1
					guess = guesser.guess(guess > number)

				guesser.win(guesses)
				results.write('{}\t{}\t{}\t{}\n'.format(highest, 'Halving' if smart else 'Random', trial, guesses))
