from engine.game import Game
from engine.inventory_item import InventoryItem
from engine.place import Place
from engine.event import Event
from engine.transition import Transition as T


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
            Event(.5, 'The fish in the aquarium turn to watch you', 0, max_occurrences=1),
        ))

        lift = Place('Lift', 'You have entered the turbolift.', (
            Event(.1, "The ship's android says hello to you.", 1),
        ))

        lounge = Place('Lounge', 'Welcome to the lounge.', (
            Event(1, 'Relaxing in the lounge improves your health.', 10),
        ))

        space_suit = InventoryItem('Spacesuit')

        storage_room = Place('Storage Room', 'You enter the storage room',
            inventory_items=[space_suit])

        transporter_room = Place('Transporter Room',
            'The transporter room looks cool with all its blinking lights and sliders.')

        planet = Place('Planet', 'You have beamed down to the planet.', (
            Event(.3, 'You found the experience relaxing', +10),
        ))

        def mt(places):  # Make Transitions
            return [T(place) for place in places]

        bridge          .transitions = mt((ready_room, lift))
        ready_room      .transitions = mt((bridge,))
        lift            .transitions = mt((bridge, lounge, storage_room, transporter_room))
        lounge          .transitions = mt((lift,))
        storage_room    .transitions = mt((lift,))
        transporter_room.transitions = (T(planet, (space_suit,)), T(lift))
        planet          .transitions = mt((transporter_room,))

        self.location = bridge

game = ShipGame()
game.play()