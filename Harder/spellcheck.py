with open('words.txt') as file:
    words = {line.strip() for line in file}

sentence = input('Enter a sentence and I will spell check every word => ')

set_words = set(sentence.split(' '))
print('Misspelled words: ' + ', '.join(set_words.difference(words)))
