class Place:
    'A place in the game, with a title, description, and events that can occur there.'

    def __init__(self, title, description, events=(), inventory_items=()):
        'events is a sequence of Event objects.'
        self.title = title
        self.description = description
        self.events = events
        self.inventory_items = inventory_items
