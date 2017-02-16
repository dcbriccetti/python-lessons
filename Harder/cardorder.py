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

    while deck:
        c = deck.pop(0)
        deck_ops += 1

        if c != expected:
            return False

        if not deck:
            return True

        deck.append(deck.pop(0))
        deck_ops += 2
        expected += 1


start = time()
r = range(2, 11)

(c1, c3, c5, c7, c9) = range(1, 6)

for c2 in r:
    for c4 in r:
        for c6 in r:
            for c8 in r:
                for c10 in r:
                    deck = (c1, c2, c3, c4, c5, c6, c7, c8, c9, c10)
                    if correct_order(deck):
                        print('Deck {} found in {:.3f} seconds. {:,} decks tried. {:,} list operations performed.'.format(
                              deck, time() - start, decks, deck_ops))
                        exit()