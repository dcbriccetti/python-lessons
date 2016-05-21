class Place(object):
    'A place in the game, with a title, description, and events that can occur there.'

    def __init__(self, title, description, events):
        'events is a sequence of Event objects.'
        self.title = title
        self.description = description
        self.events = events
