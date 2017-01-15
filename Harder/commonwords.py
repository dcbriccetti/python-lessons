common_words = set()

with open('common-words.txt') as file:
    for line in file:
        if not line.startswith('#'):
            common_words.add(line.strip().lower())

while True:
    sentence = input('-> ')
    words = sentence.split(' ')
    for word in words:
        print(word if word.lower() in common_words else '*' * len(word), end=' ')

    print()
