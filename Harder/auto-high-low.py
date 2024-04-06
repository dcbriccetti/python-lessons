from random import randint
from math import log2
import logging
logging.basicConfig(format='%(message)s', level=logging.INFO)
POWERS_OF_TEN_FOR_HIGHEST = range(3, 13, 3)
NUM_TRIALS = 1000

class Guesser:
    def __init__(self, highest, smart=False):
        self.low = 1
        self.high = self.highest = highest
        self.smart = smart
        self.last_guess = None

    def guess(self, too_high):
        if too_high is None:
            pass  # Not set on first guess
        elif too_high:
            self.high = self.last_guess - 1
        else:
            self.low = self.last_guess + 1
        self.last_guess = self._middle() if self.smart else randint(self.low, self.high)
        logging.debug('{:,}-{:,}: {:,}'.format(self.low, self.high, self.last_guess))
        return self.last_guess

    def win(self, guesses):
        logging.info('I got it in {} guesses.'.format(guesses))

    def _middle(self):
        return self.low + (self.high - self.low) // 2


with open('high-low-results.tsv', 'w') as results:
    results.write('Highest\tStrategy\tTrial\tGuesses\n')

    for power in POWERS_OF_TEN_FOR_HIGHEST:
        highest: int = 10 ** power
        logging.info('Between 1 and {0:,} (binary logarithm of {0:,} is {1:.2f}).'.format(
            highest, log2(highest)))

        for smart in (True, False):
            logging.info('Smart' if smart else 'Random')

            for trial in range(1, NUM_TRIALS + 1):
                logging.info('Trial %d' % trial)
                guesser = Guesser(highest, smart=smart)
                number = randint(1, highest)
                guess = guesser.guess(None)
                guesses = 1

                while guess != number:
                    guesses += 1
                    guess = guesser.guess(guess > number)

                guesser.win(guesses)
                results.write('{}\t{}\t{}\t{}\n'.format(
                    highest, 'Halving' if smart else 'Random', trial, guesses))
