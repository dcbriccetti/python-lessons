from random import random, shuffle, choice
import re

WORDS_FILENAME = 'words.txt'  # A file with one word per line

r = re.compile('[aeiou]{3}')  # A regular expression that matches words with exactly three vowels
words = []
matches = []

with open(WORDS_FILENAME) as file:
    for line in file:
        line = line.strip()
        if r.match(line):
            matches.append(line)
        elif random() < .0005:
            words.append(line)

shuffle(matches)
selected_match = choice(matches)
words.append(selected_match)
shuffle(words)
print(selected_match)
print(words)
