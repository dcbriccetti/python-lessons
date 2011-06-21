from random import shuffle
print('Welcome to the wonderful quiz on music!')

qas = [
    ('How many beats are there per measure in 2/4 time?', '2'),
    ('In what family of instruments is the piano?', 'percussion'),
    ('How many strings does a violin have?', '4')
]
shuffle(qas)
numRight = 0

for question, rightAnswer in qas:
    answer = input(question + ' ')
    if answer.lower() == rightAnswer:
        print('Right!')
        numRight += 1
    else:
        print('No, the answer is %s.' % rightAnswer)

print('You got %d right and %d wrong.' % (numRight, len(qas) - numRight))
