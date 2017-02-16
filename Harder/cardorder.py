# A brute-force solution to the problem posed in
# http://marilynburnsmathblog.com/wordpress/when-should-and-shouldnt-we-give-answers/

from time import time
from sys import exit

deck_ops = 0
decks = 0


def correct_order(read_only_deck):
    global deck_ops, decks
    deck = list(read_only_deck)
    decks += 1
    expected = 1
    while len(deck) > 0:
        c = deck.pop(0)
        deck_ops += 1

        if c != expected:
            return False

        if len(deck) == 0:
            return True

        deck.append(deck.pop(0))
        deck_ops += 2
        expected += 1


start = time()
r = range(2, 11)

c1 = 1
for c2 in r:
    c3 = 2
    for c4 in r:
        c5 = 3
        for c6 in r:
            c7 = 4
            for c8 in r:
                c9 = 5
                for c10 in r:
                    deck = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
                    if correct_order(deck):
                        print('Deck {} found in {:.3f} seconds. {:,} decks tried. {:,} list operations performed.'.format(
                              deck, time() - start, decks, deck_ops))
                        exit()
