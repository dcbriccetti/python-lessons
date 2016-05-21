from game import Game
from place import Place
from event import Event


class ShipGame(Game):
    def __init__(self):
        super(ShipGame, self).__init__()
        self.introduction = 'Welcome to Ship Adventure. You are the captain of a star ship.'

        bridge = Place('Bridge',
            "You are on the bridge of a spaceship, sitting in the captain's chair.", (
                Event(0.01, 'An intruder beams onto the bridge and shoots you.', -50, max_occurrences=1),
                Event(0.1, "The ship's doctor gives you a health boost.", 30),
            ))

        ready_room = Place('Ready Room', "You are in the captain's ready room.", (
            Event(.5, 'The fish in the aquarium turn to watch you', 0, max_occurrences=1)
        ))

        lift = Place('Lift', 'You have entered the turbolift.', (
            Event(.1, "The ship's android says hello to you.", 1),
        ))

        lounge = Place('Lounge', 'Welcome to the lounge.', (
            Event(1, 'Relaxing in the lounge improves your health.', 10),
        ))

        transporter_room = Place('Transporter Room', 'You enter the transporter room.', (
        ))

        planet = Place('Planet', 'You have beamed down to the planet.', (
            Event(.9, 'The air is too thin to breathe!', -50),
        ))

        bridge          .transitions = (ready_room, lift)
        ready_room      .transitions = (bridge,)
        lift            .transitions = (bridge, lounge, transporter_room)
        lounge          .transitions = (lift,)
        transporter_room.transitions = (planet, lift)
        planet          .transitions = (transporter_room,)

        self.location = bridge

game = ShipGame()
game.play()