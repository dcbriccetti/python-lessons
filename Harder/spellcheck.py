words = set()

with open('words.txt') as file:
    for line in file:
        words.add(line.strip())

sentence = input('Enter a sentence and I will spell check every word => ')

set_words = set(sentence.split(' '))
print('Misspelled words: ' + ', '.join(set_words.difference(words)))
