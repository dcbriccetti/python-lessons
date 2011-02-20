from engine.game import Game
from engine.place import Place
from engine.event import Event

class ShipGame(Game):
    def __init__(self):
        super(ShipGame, self).__init__()
        self.introduction = '''
Welcome to Ship Adventure. You are the captain of a star ship.
        '''

        bridge = Place('Bridge', "You are on the bridge of a spaceship, sitting in the captain's chair.", (
            Event(0.2, 'An intruder beams onto the bridge and shoots you.', -50),
            Event(0.1, "The ship's doctor gives you a health boost.", 30),
            ))

        readyRoom = Place('Ready Room', "You are in the captain's ready room.", ())

        lift = Place('Lift', 'You have entered the turbolift.', (
            Event(.05, "The ship's android says hello to you.", 0),
        ))

        lounge = Place('Lounge', 'Welcome to the lounge.', (
            Event(1, 'Relaxing in the lounge improves your health.', 10),
        ))

        bridge.transitions = (readyRoom, lift)
        readyRoom.transitions = (bridge,)
        lift.transitions = (bridge,lounge)
        lounge.transitions = (lift,)

        self.location = bridge

game = ShipGame()
game.play()