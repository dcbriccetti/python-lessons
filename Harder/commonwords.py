with open('common-words.txt') as file:
    common_words = {line.strip().lower() for line in file if not line.startswith('#')}

while True:
    sentence = input('-> ')
    if not sentence:
        break
    for word in sentence.split(' '):
        print(word if word.lower() in common_words else '*' * len(word), end=' ')
    print()
