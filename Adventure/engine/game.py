from random import choice

class Game:
    'The main code for running the game. Extend this class for your game. See shipgame.py for an example.'

    def __init__(self):
        self.health = 100
        self.inventory = []
        self.introduction = ''
        self.location = None

    def play(self):
        print(self.introduction)

        while True:
            print()
            print(self.location.description)
            for i in self.location.inventory_items:
                print('You found: ' + i.name)
                self.inventory.append(i)

            self.location.inventory_items = ()

            for event in self.location.events:
                self.health += event.process()
                if self.health <= 0:
                    goodbyes = (
                        "That's it for you!",
                        'You lose.',
                        'So long.'
                    )
                    print(choice(goodbyes))
                    exit(1)

            print('Health: %d, Items: %s' % (self.health,
                ', '.join([i.name for i in self.inventory]) if self.inventory else 'None'))
            self._transition()

    def _have_all(self, must_have):
        missing = [mh for mh in must_have if mh not in self.inventory]
        return not missing

    def _available_transitions(self):
        return [t for t in self.location.transitions if self._have_all(t.must_have)]

    def _transition(self):
        transitions = self._available_transitions()
        print('You can go to these places:')
        for (index, transition) in enumerate(transitions):
            print(index + 1, transition.place.title)

        choice = get_numeric('Choose one, or enter 0 to exit: ')
        if choice:
            self.location = transitions[choice - 1].place
        else:
            exit(0)


def get_numeric(prompt):
    while True:
        response = input(prompt)
        try:
            return int(response)
        except ValueError:
            print("Please enter a number.")
