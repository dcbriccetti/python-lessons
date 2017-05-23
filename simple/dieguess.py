from random import randint
print('Welcome to the die-guessing game')
balance = 50

while True:
    print('Your balance is %d' % balance)
    bet = int(input('How much do you bet? (0 to quit)'))
    if bet == 0:
        break
    throw = randint(1, 6)
    guess = int(input('What do you guess we rolled? '))
    if guess == throw:
        print('Right!')
        balance += 6 * bet
    else:
        print('Too bad')
        balance -= bet
