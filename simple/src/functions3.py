from random import randint

def tossCoins():
    for n in range(3):
        if randint(1, 2) == 1:
            print('heads')
        else:
            print('tails')
    
print('Hello, and welcome to the simulation')
tossCoins()
print('Now for intermission')
print("Let's flip some more coins")
tossCoins()
print('We are done')
