class Game(object):
    '''The main code for running the game.'''

    def __init__(self):
        self.health = 100

    def play(self):
        print(self.introduction)

        while True:
            print()
            print(self.location.description)

            for event in self.location.events:
                self.health += event.process()
                if self.health <= 0:
                    print("That's it for you!")
                    exit(1)

            print('Health: %d' % self.health)
            self._transition()

    def _transition(self):
        transitions = self.location.transitions
        print('You can go to these places:')
        for (index, transition) in enumerate(transitions):
            print(index + 1, transition.title)

        choice = int(input('Choose one, or 0 to exit: '))
        if choice == 0:
            exit(0)
        else:
            self.location = transitions[choice - 1]
