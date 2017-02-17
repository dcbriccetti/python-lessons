'''
A brute-force solution to the problem posed in
http://marilynburnsmathblog.com/wordpress/when-should-and-shouldnt-we-give-answers/

Earlier versions (see history in Github) better match the YouTube video.
'''

from time import time

decks_tried = 0


def correct_order(read_only_deck):
    'Determine whether the cards in the deck are in the correct order'
    global decks_tried
    decks_tried += 1
    deck = list(read_only_deck)

    for expected in range(1, 11):
        if deck.pop(0) != expected:
            return False

        if len(deck) > 1:
            deck.append(deck.pop(0))

    return True


def permutations():
    'Return a generator of deck tuples'
    r = range(6, 11)  # We know where 1–5 are
    return ((1, c2, 2, c4, 3, c6, 4, c8, 5, c10)
            for c2 in r for c4 in r for c6 in r for c8 in r for c10 in r
            if len({c2, c4, c6, c8, c10}) == 5)  # All numbers must be different


start = time()
correct_deck = next(filter(correct_order, permutations()))
assert correct_deck == (1, 6, 2, 10, 3, 7, 4, 9, 5, 8)
print('Deck {} found in {:,.2f} microseconds. {:,} decks tried.'.format(
    correct_deck, (time() - start) * 1000000, decks_tried))
