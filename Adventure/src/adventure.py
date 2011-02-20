# -*- coding: utf-8 -*-
from engine import Game, Place, Event

class ShipGame(Game):
    def __init__(self):
        super(ShipGame, self).__init__()
        bridge    = Place('Bridge', 'You are on the bridge of a spaceship, sitting in the captain’s chair.',
            [Event(0.5, 'An intruder beams onto the bridge and shoots you.', -50)])
        readyRoom = Place('Ready Room', "The captain's ready room.", [])
        lift      = Place('Lift', 'A turbolift.', [])

        bridge.transitions = (readyRoom, lift)
        readyRoom.transitions = (bridge,)
        lift.transitions = (bridge,)

        self.location = bridge

game = ShipGame()
game.play()