# -*- coding: utf-8 -*-
from random import random

class Place(object):
    def __init__(self, title, description, events):
        self.title = title
        self.description = description
        self.events = events

class Game(object):
    def __init__(self):
        self.health = 100

    def play(self):
        while True:
            print self.location.description

            for event in self.location.events:
                self.health += event.process()
                if self.health <= 0:
                    print 'ThatÕs it for you!'
                    exit(1)

            print 'Health: %d' % self.health
            self._transition()
            
    def _transition(self):
        print 'You can go to these places:'
        for (i,t) in enumerate(self.location.transitions):
            print i + 1, t.title

        choice = int(raw_input('Choose one '))
        self.location = self.location.transitions[choice - 1]

class Event(object):
    def __init__(self, probability, message, healthChange):
        self.probability = probability
        self.message = message
        self.healthChange = healthChange

    def process(self):
        if random() < self.probability:
            print self.message
            return self.healthChange
        return 0
