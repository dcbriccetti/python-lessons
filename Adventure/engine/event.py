from random import random


class Event:
    'A game event, including the probability of its happening.'

    def __init__(self, probability, message, health_change, max_occurrences=100000):
        self.probability = probability
        self.message = message
        self.health_change = health_change
        self.remaining_occurrences = max_occurrences

    def process(self):
        'Process the event, and return the change in health, or 0.'

        if self.remaining_occurrences and random() < self.probability:
            self.remaining_occurrences -= 1
            print(self.message)
            return self.health_change

        return 0
