from random import random

class Event(object):
    '''A game event, including the probability of its happening.'''

    def __init__(self, probability, message, healthChange):
        self.probability = probability
        self.message = message
        self.healthChange = healthChange

    def process(self):
        '''Process the event, and return the change in health, or 0.'''

        if random() < self.probability:
            print(self.message)
            return self.healthChange
        return 0
