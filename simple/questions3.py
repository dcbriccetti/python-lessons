from random import shuffle
print('Welcome to the wonderful quiz on music!')

with open("questions.txt") as f:
    lines = f.readlines()
    
shuffle(lines)
numRight = 0
wrong = []

numQuestions = int(input("How many questions? "))

for line in lines[:numQuestions]:
    question, rightAnswer = line.strip().split("\t")
    answer = input(question + ' ')
    if answer.lower() == rightAnswer:
        print('Right!')
        numRight += 1
    else:
        print('No, the answer is %s.' % rightAnswer)
        wrong.append(question)

print('You got %d right' % (numRight))
if (wrong):
    print('You got these wrong: ')
    for q in wrong:
        print(q)