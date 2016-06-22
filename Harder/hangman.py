import turtle as t

word = 'television'
correct = set()
wrong = set()
MAX_GUESSES = 7
num_guesses = 0

def draw_background():
    t.setup(300, 500)
    t.title('Hangman')
    t.pu()
    t.setpos(-100, -200)
    t.seth(0)
    t.pd()
    t.fd(200)

def draw_head():
    t.pu()
    t.setpos(0, 0)
    t.pd()
    t.circle(10)

def draw_body():
    t.pu()
    t.setpos(0, 0)
    t.seth(270)
    t.pd()
    t.fd(100)

def draw_left_arm():
    pass

draw_functions = (draw_head, draw_body, draw_left_arm)

draw_background()

while num_guesses < MAX_GUESSES:
    print(MAX_GUESSES - num_guesses, 'guesses left')
    clue = [letter if letter in correct else '-' for letter in word]
    print(' '.join(clue))
    if wrong:
        print('Wrong:', ' '.join(sorted(list(wrong))))

    guess = input('Guess? ')
    num_guesses += 1

    if guess == word:
        print('Right!')
        break
    if len(guess) > 1:
        print('Wrong')
    else:
        if guess in correct or guess in wrong:
            print('You already guessed that')
        else:
            if guess in word:
                print('Right')
                correct.add(guess)
            else:
                print('Wrong')
                wrong.add(guess)
                draw_functions[len(wrong) - 1]()
