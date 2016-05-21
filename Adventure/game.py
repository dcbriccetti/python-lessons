class Game:
    'The main code for running the game. Extend this class for your game. See shipgame.py for an example.'

    def __init__(self):
        self.health = 100
        self.introduction = ''
        self.location = None

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

        choice = get_numeric('Choose one, or enter 0 to exit: ')
        if choice:
            self.location = transitions[choice - 1]
        else:
            exit(0)


def get_numeric(prompt):
    while True:
        response = input(prompt)
        try:
            return int(response)
        except ValueError:
            print("Please enter a number.")
