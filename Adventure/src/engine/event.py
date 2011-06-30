from random import random

class Event(object):
    '''A game event, including the probability of its happening.'''

    def __init__(self, probability, message, healthChange, maxOccur=100000):
        self.probability = probability
        self.message = message
        self.healthChange = healthChange
        self.remainingOccur = maxOccur

    def process(self):
        '''Process the event, and return the change in health, or 0.'''

        if self.remainingOccur and random() < self.probability:
            self.remainingOccur -= 1
            print(self.message)
            return self.healthChange
        return 0
